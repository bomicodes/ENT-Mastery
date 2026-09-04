"""v17.8 — all-domain Concept Check clinical curation.

This pass reviews every live Concept Check and repairs weak/generated items while
preserving already-sound clinical MCQs and manually curated questions.

v20.6 teaching-alignment update:
- stop forcing every concept into a dangerous-alternative/red-flag question;
- choose the retrieval target from the kind of concept being taught;
- tests/interpretation skills ask how and when to use/interpret them;
- anatomy/physiology ask localization, relationships, and clinical consequence;
- procedures ask indications, decision points, anatomy, and operative choices;
- conditions ask recognition, evaluation, or management without inventing a
  must-not-miss mimic when the concept does not have one;
- true emergencies still test escalation through their management content.

The reveal remains tied to the live Deep Curriculum so the question and teaching
answer stay on the same canonical concept.
"""

import re
from collections import Counter

from concept_check_board_repair_v177 import _find_module, _norm


DOMAIN_FRAMES = {
    "Otology / Neurotology": {
        "setting": "An adult is evaluated in otology clinic",
        "priority": "localize disease, interpret hearing/vestibular data correctly, and connect findings to management",
        "sources": ["Pasha 6e", "K.J. Lee 12e", "Cummings 7e reconciliation", "current otology/neurotology evidence"],
    },
    "Rhinology / Allergy / Skull Base": {
        "setting": "A patient is evaluated in rhinology clinic",
        "priority": "define inflammatory, structural, or skull-base disease and connect anatomy/evaluation to treatment",
        "sources": ["Pasha 6e", "K.J. Lee 12e", "Cummings 7e reconciliation", "current rhinology/skull-base society guidance"],
    },
    "Head & Neck Oncology": {
        "setting": "A patient is reviewed by the head-and-neck team",
        "priority": "stage disease correctly and connect site, extent, pathology, and function to treatment",
        "sources": ["Pasha 6e", "K.J. Lee 12e", "Cummings 7e reconciliation", "current NCCN/AJCC-aligned oncology guidance"],
    },
    "Thyroid / Parathyroid / Salivary": {
        "setting": "A patient is seen in endocrine/head-and-neck surgery clinic",
        "priority": "separate diagnosis from localization and connect risk stratification to the appropriate intervention",
        "sources": ["Pasha 6e", "K.J. Lee 12e", "Cummings 7e reconciliation", "current endocrine/salivary evidence"],
    },
    "Pediatric Otolaryngology": {
        "setting": "A child is evaluated in pediatric otolaryngology",
        "priority": "apply age-specific anatomy and physiology, then choose evaluation, timing, treatment, and disposition",
        "sources": ["Pasha 6e", "K.J. Lee 12e", "Cummings 7e reconciliation", "current pediatric ENT evidence"],
    },
    "Laryngology / Voice / Swallowing": {
        "setting": "A patient is evaluated in laryngology clinic",
        "priority": "localize structural, neurologic, voice, and swallowing dysfunction and choose the right evaluation or treatment",
        "sources": ["Pasha 6e", "K.J. Lee 12e", "Cummings 7e reconciliation", "current laryngology/swallowing evidence"],
    },
    "Facial Plastics / Trauma": {
        "setting": "A patient is assessed in facial plastics/trauma clinic",
        "priority": "connect anatomy, function, timing, tissue status, and reconstruction principles to the clinical decision",
        "sources": ["Pasha 6e", "K.J. Lee 12e", "Cummings 7e reconciliation", "current facial trauma/reconstructive evidence"],
    },
    "Sleep Surgery": {
        "setting": "A patient with sleep-disordered breathing is reviewed in sleep clinic",
        "priority": "interpret the sleep phenotype and match anatomy and physiology to treatment selection",
        "sources": ["Pasha 6e", "K.J. Lee 12e", "Cummings 7e reconciliation", "current sleep guidance"],
    },
    "General ENT / Emergencies": {
        "setting": "A patient is evaluated by the ENT service",
        "priority": "identify the immediate problem, stabilize when necessary, and move from evaluation to definitive management",
        "sources": ["Pasha 6e", "K.J. Lee 12e", "Cummings 7e reconciliation", "current emergency/airway evidence"],
    },
}


CLINICAL_MARKERS = (
    "patient", "child", "infant", "adult", "man", "woman", "boy", "girl",
    "presents", "returns", "develops", "postoperative", "after surgery", "exam",
    "otoscopy", "endoscopy", "ct ", "mri ", "ultrasound", "audiogram", "psg",
)

FOUNDATION_TERMS = (
    "anatomy", "physiology", "neuroanatomy", "embryology", "histology",
    "fundamentals", "principles", "vascular anatomy", "nerve anatomy",
)

INTERPRETATION_TERMS = (
    "interpretation", "audiogram", "audiometry", "tympanometry", "electrophysiology",
    "abr", "oae", "vemp", "vhit", "caloric", "rotational chair", "psg",
    "polysomnography", "fees", "videofluoro", "mbs", "stroboscopy", "imaging",
    "ultrasound", "endoscopy findings", "sleep study",
)

PROCEDURE_TERMS = (
    "surgery", "surgical", "ectomy", "plasty", "repair", "reconstruction", "flap",
    "dissection", "laryngoscopy", "bronchoscopy", "esophagoscopy", "tracheostomy",
    "thyroidectomy", "parathyroidectomy", "mastoidectomy", "cochlear implant",
    "implantation", "ablation", "ligation", "embolization", "septoplasty",
    "turbinate reduction", "sinus surgery", "tonsillectomy", "adenoidectomy",
    "sialendoscopy", "biopsy technique",
)

EMERGENCY_TERMS = (
    "hemorrhage", "bleeding", "hematoma", "airway emergency", "foreign body",
    "epistaxis", "abscess", "deep neck infection", "caustic", "airway fire",
    "carotid blowout", "tracheoinnominate", "orbital compartment", "anaphylaxis",
)


def _text(q):
    return str(q.get("prompt") or q.get("question") or q.get("stem") or "").strip()


def _is_clinical(text):
    n = _norm(text)
    return "?" in text and any(x in n for x in CLINICAL_MARKERS)


def _answer_index(q):
    try:
        return int(q.get("answer"))
    except (TypeError, ValueError):
        return -1


def _choice_leak(q):
    prompt = _norm(_text(q))
    for c in q.get("choices") or []:
        nc = _norm(c)
        if len(nc.split()) >= 2 and nc in prompt:
            return True
    return False


def _title_leak(q):
    topic = _norm(q.get("topic"))
    prompt = _norm(_text(q))
    if not topic or topic not in prompt:
        return False
    return any(x in prompt for x in (
        "which diagnosis", "what is the diagnosis", "most likely diagnosis",
        "which condition", "which disorder", "which disease",
    ))


def _mcq_is_structurally_sound(q):
    choices = list(q.get("choices") or [])
    a = _answer_index(q)
    why = list(q.get("why_wrong") or [])
    if len(choices) != 4 or not (0 <= a < 4):
        return False
    if not str(q.get("explanation") or "").strip() or len(why) != 4:
        return False
    if any(i != a and len(_norm(reason).split()) < 5 for i, reason in enumerate(why)):
        return False
    if _choice_leak(q) or _title_leak(q) or not _is_clinical(_text(q)):
        return False
    lengths = [len(_norm(c).split()) for c in choices]
    if min(lengths) == 0 or max(lengths) > max(32, 4 * min(lengths)):
        return False
    question = _norm(_text(q))
    if any(x in question for x in (
        "next step", "management", "treatment", "should", "most appropriate",
        "best initial", "operative", "surgery",
    )):
        action_words = (
            "treat", "observe", "obtain", "perform", "start", "place", "drain",
            "surgery", "therapy", "antibiotic", "imaging", "biopsy", "refer",
            "admit", "intub", "embol", "radiation", "chem",
        )
        if sum(any(w in _norm(c) for w in action_words) for c in choices) < 2:
            return False
    return True


def _clean_case(text, topic):
    s = " ".join(str(text or "").split())
    if not s:
        return "the relevant clinical findings are being reviewed"
    for prefix in (
        "Recognition:", "Recognize", "Classic presentation:", "Typical presentation:",
        "Key features:", "Boards:", "Board pearl:",
    ):
        if s.lower().startswith(prefix.lower()):
            s = s[len(prefix):].lstrip(" :-")
    if topic:
        s = re.sub(re.escape(str(topic)), "this condition", s, flags=re.I)
    s = re.sub(r"\b(on boards|for boards|board(?:s)? pearl)\b[:,]?", "", s, flags=re.I)
    if len(s) > 470:
        cut = s[:470]
        stop = max(cut.rfind(". "), cut.rfind("; "))
        s = cut[:stop + 1] if stop > 190 else cut.rstrip() + "…"
    return s.strip().rstrip(".")


def _contains_term(text, term):
    t = _norm(term)
    if not t:
        return False
    if " " in t:
        return t in text
    return t in set(text.split())


def _concept_kind(topic, module):
    text = _norm(" ".join([
        str(topic or ""),
        " ".join(str(x) for x in (module.get("tags") or [])) if isinstance(module, dict) else "",
    ]))
    # Emergency takes precedence over procedure: e.g. post-tonsillectomy
    # hemorrhage is an emergency concept, not a tonsillectomy-technique prompt.
    if any(_contains_term(text, t) for t in EMERGENCY_TERMS):
        return "emergency"
    if any(_contains_term(text, t) for t in INTERPRETATION_TERMS):
        return "interpretation"
    if any(_contains_term(text, t) for t in FOUNDATION_TERMS):
        return "foundation"
    if any(_contains_term(text, t) for t in PROCEDURE_TERMS):
        return "procedure"
    return "condition"


def _dimension(q, module):
    topic = q.get("canonical_topic") or q.get("topic") or module.get("topic") or ""
    kind = _concept_kind(topic, module)
    available = {k for k in ("recognize", "localize", "workup", "manage", "operate", "teach")
                 if str(module.get(k) or "").strip()}
    preference = {
        "interpretation": ("workup", "localize", "manage", "recognize", "teach"),
        "foundation": ("localize", "recognize", "workup", "operate", "teach"),
        "procedure": ("operate", "manage", "localize", "workup", "teach"),
        "emergency": ("manage", "workup", "operate", "recognize", "teach"),
        "condition": ("manage", "workup", "localize", "recognize", "operate", "teach"),
    }[kind]
    return next((dim for dim in preference if dim in available), None)


def _ask_for(kind, dimension, topic):
    if kind == "interpretation":
        if dimension == "workup":
            return f"When is {topic} the right test or evaluation, what information does it provide, and what limitation or pitfall should you remember when interpreting it?"
        if dimension == "localize":
            return f"Which findings on {topic} carry the most diagnostic or localizing weight, and how do they change your interpretation?"
        return f"How should you use the result of {topic} to make the next clinical decision?"

    if kind == "foundation":
        if dimension == "localize":
            return f"For {topic}, what structures, relationships, or physiologic mechanisms must you be able to map, and why do they matter clinically?"
        return f"What are the core principles of {topic}, and what practical clinical or operative consequence follows from them?"

    if kind == "procedure":
        if dimension == "operate":
            return f"When is {topic} indicated, what key anatomy or decision points determine how you perform it, and what would make you change the operative plan?"
        if dimension == "manage":
            return f"Where does {topic} fit in the management pathway, and what patient or disease factors determine whether it is appropriate?"
        return f"What must you establish before choosing {topic}, and which findings most affect procedural planning?"

    if kind == "emergency":
        if dimension == "manage":
            return "What are your immediate priorities, what is the first definitive management step, and which finding should trigger escalation?"
        if dimension == "workup":
            return "What information or testing is needed now without delaying stabilization or definitive treatment?"
        return "What feature determines the urgency of this presentation and the next action?"

    if dimension == "workup":
        return "What evaluation is most useful next, and which finding would actually change the diagnosis, staging, or management?"
    if dimension == "manage":
        return "What is the initial management strategy, and what finding, response, or failure would change the next step?"
    if dimension == "operate":
        return "Which findings determine whether surgery is indicated, and what factor most strongly changes the choice or extent of the procedure?"
    if dimension == "localize":
        return "Where is the process localized, and why does that localization matter for the differential, workup, or treatment?"
    return "Which findings are most characteristic here, and which feature best distinguishes or confirms the diagnosis?"


def _stem_for(domain, kind, topic, case, ask):
    frame = DOMAIN_FRAMES.get(domain, {})
    setting = frame.get("setting", "A patient is evaluated by the otolaryngology service")
    if kind == "interpretation":
        return f"{setting}. You are considering {topic}. {case}. {ask}"
    if kind == "foundation":
        return f"In the clinical or operative context of {topic}, {case}. {ask}"
    if kind == "procedure":
        return f"{setting}. {topic} is being considered. {case}. {ask}"
    return f"{setting}. {case}. {ask}"


def _convert_to_domain_oral_board(q, module):
    domain = q.get("domain")
    if domain not in DOMAIN_FRAMES or not module:
        return False
    topic = q.get("topic") or module.get("topic") or "this topic"
    dim = _dimension(q, module)
    if not dim:
        return False
    kind = _concept_kind(topic, module)
    case = _clean_case(module.get("recognize") or module.get("localize"), topic)
    q["prompt"] = _stem_for(domain, kind, topic, case, _ask_for(kind, dim, topic))
    q.pop("question", None)
    q.pop("stem", None)
    q["choices"] = []
    q["answer"] = None
    q["answer_text"] = str(module.get(dim) or "").strip()
    q["explanation"] = (
        f"This check tests the {dim} layer of {topic}. The reveal comes from the live canonical "
        "Deep Curriculum, so the question is testing the concept itself rather than a generic red-flag template."
    )
    if str(module.get("teach") or "").strip():
        q["board_pearl"] = str(module.get("teach")).strip()
    q["board_dimension_v178"] = dim
    q["concept_kind_v206"] = kind
    q["converted_to_oral_board_v178"] = True
    q["teaching_aligned_v206"] = True
    return True


def _ensure_curveball(q, module):
    if not str(q.get("curveball") or "").strip() or str(q.get("curveball_answer") or "").strip():
        return False
    if module:
        q["curveball_answer"] = str(
            module.get("operate") or module.get("manage") or module.get("workup") or module.get("teach") or ""
        ).strip()
    if not str(q.get("curveball_answer") or "").strip():
        q["curveball_answer"] = "Use the new information to reassess the diagnosis, disease extent, and next management decision."
    q["curveball_answer_added_v178"] = True
    return True


def _review_metadata(q, module):
    frame = DOMAIN_FRAMES.get(q.get("domain"), {})
    q["reviewed_all_domains_v178"] = True
    q["board_review_standard_v178"] = frame.get("priority", "clinical decision-making")
    basis = []
    for s in list((module or {}).get("source_basis") or []) + list(frame.get("sources") or []):
        if s and s not in basis:
            basis.append(s)
    q["review_basis_v178"] = basis


def apply_concept_check_domain_curation_v178(checks, deep_modules, v6_item_id):
    stats = Counter()
    unresolved = []
    per_domain = Counter()

    for q in checks or []:
        stats["reviewed"] += 1
        per_domain[q.get("domain") or "UNKNOWN"] += 1
        module = _find_module(q, deep_modules, v6_item_id)

        if q.get("curated_v177") == "external_ear":
            stats["preserved_manual_v177"] += 1
        elif q.get("choices"):
            if _mcq_is_structurally_sound(q):
                stats["mcq_approved"] += 1
            elif _convert_to_domain_oral_board(q, module):
                stats["mcq_converted"] += 1
            else:
                unresolved.append(q.get("id"))
        else:
            if _convert_to_domain_oral_board(q, module):
                stats["oral_board_rebuilt"] += 1
            elif _is_clinical(_text(q)) and str(q.get("answer_text") or q.get("model_answer") or "").strip():
                stats["oral_board_approved"] += 1
            else:
                unresolved.append(q.get("id"))

        if _ensure_curveball(q, module):
            stats["curveball_answers_added"] += 1
        _review_metadata(q, module)

    return {
        "stats": dict(stats),
        "per_domain": dict(per_domain),
        "unresolved": unresolved,
    }
