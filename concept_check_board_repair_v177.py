"""v17.7 — Concept Check board-style clinical repair.

The v16.2 repair correctly removed answer-leaking diagnosis-ID prompts, but it
converted the affected cohort into generic known-topic retrieval prompts. This
pass raises the standard again: every non-clinical Concept Check becomes a
short oral-board-style vignette tied to the live Deep Curriculum, while already
credible clinical MCQs are preserved.

Principles:
- the topic header must never be the answer to the question;
- clinical context precedes the decision being tested;
- diagnosis-titled pages test workup, management, operative selection, or a
  discriminating complication rather than asking the learner to name the title;
- free-response board vignettes always have an explicit reveal answer;
- existing attending curveballs must have a reveal answer;
- several external-ear topics are hand-curated because they were the sentinel
  failure mode and require same-level clinical distinctions.
"""

import hashlib
import re


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _text(q):
    return str(q.get("prompt") or q.get("question") or q.get("stem") or "")


def _clinical_prompt(prompt):
    p = _norm(prompt)
    clinical = (
        "patient", "child", "infant", "adult", "man ", "woman ", "boy ", "girl ",
        "presents", "develops", "returns", "history", "exam", "otoscopy", "imaging",
        "ct ", "mri ", "audiogram", "postoperative", "after ", "with ",
    )
    return "?" in str(prompt) and any(x in p for x in clinical)


def _deep_lookup(deep_modules, v6_item_id):
    exact, by_id = {}, {}
    for domain, modules in (deep_modules or {}).items():
        for m in modules or []:
            topic = m.get("topic")
            if not topic:
                continue
            exact[(domain, topic)] = m
            by_id[v6_item_id(domain, topic)] = m
    return exact, by_id


def _find_module(q, deep_modules, v6_item_id):
    exact, by_id = _deep_lookup(deep_modules, v6_item_id)
    cid = q.get("concept_id")
    if cid in by_id:
        return by_id[cid]
    key = (q.get("domain"), q.get("canonical_topic") or q.get("topic"))
    if key in exact:
        return exact[key]
    target = _norm(q.get("canonical_topic") or q.get("topic"))
    best = None
    for (domain, topic), m in exact.items():
        if domain != q.get("domain"):
            continue
        a, b = set(target.split()), set(_norm(topic).split())
        if not a or not b:
            continue
        score = len(a & b) / max(1, len(a | b))
        if best is None or score > best[0]:
            best = (score, m)
    return best[1] if best and best[0] >= 0.45 else None


def _clean_case_text(text, topic):
    s = " ".join(str(text or "").split())
    if not s:
        return "a presentation consistent with the condition shown in the topic header"
    # Remove obvious pedagogic lead-ins and the exact topic label so the case does
    # not simply echo the answer. Preserve the clinical facts that follow.
    for prefix in (
        "Recognize ", "Recognition: ", "Classic presentation: ", "Typical presentation: ",
        "Boards: ", "Board pearl: ", "Key features: ",
    ):
        if s.lower().startswith(prefix.lower()):
            s = s[len(prefix):].lstrip(" :-")
    if topic:
        s = re.sub(re.escape(str(topic)), "this disorder", s, flags=re.I)
    if len(s) > 520:
        cut = s[:520]
        stop = max(cut.rfind(". "), cut.rfind("; "))
        s = cut[:stop + 1] if stop > 220 else cut.rstrip() + "…"
    return s


def _select_dimension(q, module):
    available = [k for k in ("workup", "manage", "operate") if str(module.get(k) or "").strip()]
    if not available:
        available = [k for k in ("localize", "recognize", "teach") if str(module.get(k) or "").strip()]
    if not available:
        return None
    h = hashlib.sha256(("v177:" + str(q.get("id") or q.get("topic") or "")).encode()).digest()
    return available[int.from_bytes(h[:2], "big") % len(available)]


def _make_board_free_response(q, module):
    topic = q.get("topic") or module.get("topic") or "this condition"
    case = _clean_case_text(module.get("recognize") or module.get("localize"), topic)
    dimension = _select_dimension(q, module)
    if not dimension:
        return False

    if dimension == "workup":
        ask = (
            "What is the most appropriate diagnostic evaluation now, and which result or red flag "
            "would materially change the next step?"
        )
    elif dimension == "manage":
        ask = (
            "What is the best initial management, and what finding, host factor, or treatment failure "
            "should make you escalate beyond the routine pathway?"
        )
    elif dimension == "operate":
        ask = (
            "Operative treatment is being considered. Which clinical or anatomic factors determine "
            "whether surgery is indicated and which approach is appropriate?"
        )
    elif dimension == "localize":
        ask = "Where is the lesion or pathophysiology localized, and why does that localization matter clinically?"
    elif dimension == "recognize":
        ask = "Which feature in this presentation is the most important discriminator from the closest mimic or dangerous alternative?"
    else:
        ask = "What is the single most important board-level principle that should guide the next decision?"

    q["prompt"] = f"A patient presents with {case} {ask}"
    q.pop("question", None)
    q.pop("stem", None)
    q["choices"] = []
    q["answer"] = None
    q["answer_text"] = str(module.get(dimension) or "").strip()
    q["explanation"] = (
        f"This is a clinical {dimension} question, not a request to repeat the topic label. "
        "The reveal uses the live Deep Curriculum so the answer stays aligned with the canonical teaching layer."
    )
    if module.get("teach"):
        q["board_pearl"] = module.get("teach")
    q["board_style_v177"] = True
    q["board_dimension_v177"] = dimension
    return True


def _same_level_why(choices, answer, reasons):
    out = list(reasons or [])
    if len(out) != len(choices):
        out = [""] * len(choices)
    for i, choice in enumerate(choices):
        if i == answer:
            out[i] = "Correct."
        elif len(_norm(out[i]).split()) < 5:
            out[i] = f"{choice} does not fit the clinical decision being tested in this vignette."
    return out


# Hand-curated sentinel cluster. These are intentionally management/discrimination
# questions because the page title itself names the disease.
_CURATED_EXTERNAL_EAR = {
    "acute otitis externa": {
        "prompt": (
            "A 24-year-old swimmer has 2 days of severe otalgia and marked pain with tragal manipulation. "
            "Otoscopy shows diffuse external auditory canal edema and debris; the canal is nearly occluded, "
            "and the tympanic membrane is difficult to visualize. He is afebrile, has no diabetes or immune "
            "suppression, and has no cellulitis beyond the canal. Which is the best initial management?"
        ),
        "choices": [
            "Topical non-ototoxic antimicrobial therapy with analgesia; place an ear wick if edema prevents reliable drop delivery",
            "Routine oral antipseudomonal antibiotics because Pseudomonas is a common pathogen",
            "Urgent CT of the temporal bone and prolonged systemic antipseudomonal therapy",
            "Empiric systemic antifungal therapy without canal debridement",
        ],
        "answer": 0,
        "explanation": (
            "Uncomplicated diffuse acute otitis externa is treated topically. Marked edema that prevents drops from reaching the medial canal is an indication for a wick. "
            "Systemic antibiotics are not routine unless infection extends beyond the canal or host/clinical factors justify them."
        ),
        "why_wrong": [
            "Correct.",
            "The microbiology does not make oral antibiotics routine; uncomplicated disease is primarily treated with topical therapy.",
            "This presentation lacks the host risk, disproportionate persistent pain, granulation tissue, cranial neuropathy, or other features that should trigger concern for necrotizing disease.",
            "Otomycosis is suggested by fungal debris/pruritus and often follows moisture or topical-antibiotic exposure; treatment centers on debridement and topical therapy rather than blind systemic antifungals.",
        ],
        "board_pearl": "A wick is a drug-delivery tool for a markedly edematous canal; it is not a marker that systemic antibiotics are automatically required.",
        "curveball": "The patient returns after several days with worsening nocturnal pain out of proportion to the canal exam and friable granulation tissue at the bony-cartilaginous junction. What changes?",
        "curveball_answer": "Reconsider necrotizing otitis externa/skull-base osteomyelitis. Reassess host risk, obtain cultures/appropriate tissue when indicated, evaluate with cross-sectional imaging, and escalate to prolonged culture-directed systemic therapy with ENT/infectious-disease involvement rather than simply changing topical drops.",
    },
    "furunculosis": {
        "prompt": (
            "A healthy 31-year-old develops focal, exquisite pain at the lateral external auditory canal after manipulating the ear with a cotton swab. "
            "Examination shows a discrete erythematous fluctuant nodule confined to the hair-bearing cartilaginous canal rather than diffuse canal edema. Which diagnosis and treatment principle best fit this presentation?"
        ),
        "choices": [
            "Furunculosis; treat as a focal staphylococcal infection and drain if a true abscess has formed",
            "Diffuse acute otitis externa; treat only with canal acidification regardless of focal abscess formation",
            "Otomycosis; begin systemic azole therapy",
            "Necrotizing otitis externa; begin prolonged antipseudomonal therapy and skull-base imaging in every patient",
        ],
        "answer": 0,
        "explanation": "Furunculosis is a focal infection of a pilosebaceous unit in the lateral hair-bearing canal, usually staphylococcal. The focal nodule/abscess distinguishes it from diffuse bacterial OE.",
        "why_wrong": [
            "Correct.",
            "Diffuse OE produces generalized canal inflammation and edema rather than a single focal furuncle.",
            "Otomycosis more often causes pruritus and characteristic fungal debris; routine systemic azoles are not the default treatment.",
            "Necrotizing OE is an invasive skull-base infection associated with persistent severe pain and risk factors such as diabetes or immune compromise; it is not the default explanation for a focal lateral furuncle in a healthy adult.",
        ],
        "board_pearl": "Hair follicles are in the lateral cartilaginous canal: a focal tender pustule/nodule there is furunculosis, not simply 'severe diffuse OE.'",
    },
    "otomycosis": {
        "prompt": (
            "A patient treated repeatedly with topical antibacterial ear drops returns with intense pruritus, fullness, and mild otalgia. "
            "Microscopy shows fluffy filamentous debris with dark spores in the external canal and no invasive granulation tissue. What is the best next step?"
        ),
        "choices": [
            "Meticulous canal debridement plus topical acidifying/drying or antifungal therapy and dry-ear precautions",
            "Continue the same antibacterial drops for another 3 weeks without cleaning the canal",
            "Start prolonged IV antipseudomonal therapy for presumed skull-base osteomyelitis",
            "Perform myringotomy because the primary disease is middle-ear infection",
        ],
        "answer": 0,
        "explanation": "Otomycosis is managed by clearing fungal debris and restoring a dry/acidic canal environment, with topical antifungal or acidifying therapy as appropriate. Repeated antibacterial drops can predispose to fungal overgrowth.",
        "why_wrong": [
            "Correct.",
            "Persistent antibacterial therapy without debridement can perpetuate fungal overgrowth and leaves obstructing debris in place.",
            "There are no invasive red flags here to justify treatment for necrotizing OE/skull-base osteomyelitis.",
            "The findings localize to the external canal, not the middle ear.",
        ],
        "board_pearl": "In otomycosis, debridement is part of treatment—not merely a diagnostic maneuver.",
    },
    "necrotizing otitis externa": {
        "prompt": (
            "A 72-year-old man with poorly controlled diabetes has persistent otorrhea and deep nocturnal otalgia despite topical therapy. "
            "Examination shows granulation tissue in the external auditory canal, and the pain is disproportionate to the visible inflammation. What is the most appropriate next step?"
        ),
        "choices": [
            "Evaluate urgently for necrotizing external otitis/skull-base osteomyelitis with microbiology and cross-sectional imaging, then institute culture-directed systemic therapy",
            "Reassure him that severe pain is expected in uncomplicated swimmer's ear and continue the same drops alone",
            "Treat empirically as isolated otomycosis with topical antifungal therapy only",
            "Schedule elective canalplasty for chronic canal stenosis before further diagnostic evaluation",
        ],
        "answer": 0,
        "explanation": "Persistent severe/nocturnal otalgia, granulation tissue, treatment failure, and impaired host defenses are classic red flags for necrotizing OE. Diagnosis and extent assessment are multimodal; treatment requires systemic therapy rather than topical treatment alone.",
        "why_wrong": [
            "Correct.",
            "Disproportionate persistent pain plus diabetes and granulation tissue should not be dismissed as routine acute OE.",
            "Fungal pathogens can cause invasive disease, but this presentation first requires evaluation for skull-base infection rather than assuming uncomplicated fungal OE.",
            "Elective canal surgery does not address a potentially invasive infection and should not precede appropriate diagnostic evaluation.",
        ],
        "board_pearl": "Do not require a positive Pseudomonas culture to recognize NOE; cultures guide therapy, but the diagnosis rests on the clinical pattern plus appropriate imaging and exclusion of mimics.",
        "curveball": "The patient develops facial weakness and lower-cranial-nerve symptoms. What does this imply?",
        "curveball_answer": "Cranial neuropathy indicates advanced skull-base involvement and raises the urgency of defining disease extent, excluding alternative skull-base pathology, and coordinating prolonged systemic treatment; it is a marker of more extensive disease rather than a routine feature of uncomplicated OE.",
    },
}


def _apply_curated_external_ear(q):
    topic = _norm(q.get("topic"))
    match = None
    for key, payload in _CURATED_EXTERNAL_EAR.items():
        if key == topic or key in topic:
            match = payload
            break
    if not match:
        return False
    for k, v in match.items():
        q[k] = list(v) if isinstance(v, list) else v
    q["why_wrong"] = _same_level_why(q["choices"], q["answer"], q.get("why_wrong"))
    q["board_style_v177"] = True
    q["curated_v177"] = "external_ear"
    q.pop("answer_text", None)
    q.pop("model_answer", None)
    q.pop("correct_answer", None)
    return True


def _ensure_curveball_answer(q, module):
    if not str(q.get("curveball") or "").strip() or str(q.get("curveball_answer") or "").strip():
        return False
    if module:
        answer = str(module.get("operate") or module.get("manage") or module.get("teach") or "").strip()
    else:
        answer = "Use the new information to reassess the differential, disease extent, and treatment threshold before proceeding with the original plan."
    if answer:
        q["curveball_answer"] = answer
        q["curveball_answer_added_v177"] = True
        return True
    return False


def apply_concept_check_board_repair_v177(checks, deep_modules, v6_item_id):
    curated = []
    upgraded = []
    curveball_answers = []
    unresolved = []

    for q in checks or []:
        module = _find_module(q, deep_modules, v6_item_id)
        if _apply_curated_external_ear(q):
            curated.append(q.get("id"))
            module = _find_module(q, deep_modules, v6_item_id)
        elif not _clinical_prompt(_text(q)):
            if module and _make_board_free_response(q, module):
                upgraded.append(q.get("id"))
            else:
                unresolved.append(q.get("id"))

        if _ensure_curveball_answer(q, module):
            curveball_answers.append(q.get("id"))

    return {
        "curated": curated,
        "board_vignette_upgraded": upgraded,
        "curveball_answers_added": curveball_answers,
        "unresolved": unresolved,
    }
