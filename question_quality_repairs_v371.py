"""Final-boundary repairs for question-quality audit findings.

This pass keeps source modules immutable and repairs the fully assembled objects
served by ``runtime_entry_pasha``.  It replaces terse distractor feedback with
choice-specific reasoning, removes one answer-shape giveaway, and converts any
recognition card whose own text reveals its topic into an explicitly named card.
"""

import re

from daily_curriculum_quality_v368 import _clean, _named_recognition_prompt


WHY_WRONG_BY_CHOICE = {
    "v11_lar_02": {
        "Hearing loss": "Hearing loss does not explain postoperative stridor or bilateral vocal folds fixed near the midline.",
        "Ménière disease": "Ménière disease causes episodic vertigo and fluctuating hearing symptoms, not acute postoperative glottic obstruction.",
    },
    "v11_lar_04": {
        "Pure-tone audiogram": "Audiometry evaluates hearing and does not demonstrate a pharyngoesophageal pouch.",
        "CT temporal bones": "Temporal-bone CT evaluates otologic anatomy, not the suspected pharyngoesophageal diverticulum.",
        "Dix-Hallpike maneuver": "Dix-Hallpike testing assesses positional vertigo and does not evaluate structural dysphagia.",
    },
    "v11_fprs_02": {
        "Periorbital ecchymosis alone": "Ecchymosis is common after orbital trauma but does not establish extraocular-muscle entrapment.",
        "Subconjunctival hemorrhage": "Subconjunctival hemorrhage confirms local trauma but is not a functional sign of muscle entrapment.",
        "Mild facial edema": "Mild edema is nonspecific and lacks the gaze restriction or autonomic response that signals entrapment.",
    },
    "v11_fprs_03": {
        "Hair color": "Hair color provides no information about mandibular alignment, displacement, or functional occlusion.",
        "Tympanic membrane color": "Tympanic-membrane appearance does not assess mandibular reduction or restoration of dental occlusion.",
    },
    "v11_fprs_04": {
        "External auditory canal": "The external auditory canal is not part of the central naso-orbito-ethmoid complex or its canthal support.",
        "Thyroid cartilage": "Thyroid cartilage belongs to the laryngeal framework and does not determine NOE fracture classification.",
        "Styloid process": "The styloid process is remote from the medial canthal tendon attachment that drives NOE repair planning.",
    },
    "v11_fprs_05": {
        "Middle ear": "Middle-ear disease can affect hearing but does not explain nasal obstruction improved by lateral cheek traction.",
        "Subglottis": "Subglottic narrowing causes lower-airway symptoms and is not altered by the modified Cottle maneuver.",
        "Piriform sinus": "The piriform sinus is a hypopharyngeal structure and does not contribute to dynamic nasal-valve narrowing.",
    },
    "v11_gen_02": {
        "Acute otitis externa": "Otitis externa causes ear-canal pain and inflammation, not trismus with asymmetric palatal bulging and uvular deviation.",
        "Bell palsy": "Bell palsy produces acute peripheral facial weakness and does not cause this unilateral oropharyngeal inflammatory pattern.",
        "Epiglottic cyst": "An epiglottic cyst does not produce the classic peritonsillar swelling, trismus, and uvular deviation described here.",
    },
    "v11_gen_04": {
        "Otitis media": "Otitis media is a middle-ear infection and does not account for rapidly progressive tongue and floor-of-mouth edema.",
        "Thyroid storm": "Thyroid storm causes systemic thyrotoxicosis rather than isolated bradykinin-mediated upper-airway swelling.",
        "Labyrinthitis": "Labyrinthitis causes acute vestibular symptoms and hearing loss, not progressive oral and pharyngeal edema.",
    },
    "v11_gen_06": {
        "Wait for spontaneous cessation": "Continued bleeding with hypotension is immediately dangerous; observation delays resuscitation and hemorrhage control.",
    },
    "v132_fprs_09": {
        "The procedure must be completed before age 2 regardless of cartilage availability": "Costal cartilage is usually inadequate at this age, so forcing early autologous reconstruction compromises framework creation.",
    },
}


ANSWER_BY_CHOICE = {
    "v132_fprs_09": "Adequate costal cartilage size/framework material, generally reached by around age 8-10",
}


CSCC_OLD_ANSWER = (
    "Clinical perineural symptoms, deep invasion, poor differentiation, recurrent disease, "
    "or other major high-risk features"
)
CSCC_NEW_ANSWER = "Clinical perineural spread along a named nerve"


def _topic_variants(topic):
    variants = {topic.strip(), topic.replace("&", "and").strip()}
    for part in re.split(r"\s*(?:/|—|\(|\)|\bof the\b|\bof\b)\s*", topic, flags=re.IGNORECASE):
        part = part.strip(" -")
        if len(part) >= 6:
            variants.add(part)
    return {variant for variant in variants if variant}


def _reveals_topic(item):
    topic = _clean(item.get("topic"))
    combined = " ".join((item.get("prompt") or "", item.get("answer") or "")).lower()
    return any(
        re.search(r"(?<!\w)" + re.escape(variant.lower()) + r"(?!\w)", combined)
        for variant in _topic_variants(topic)
    )


def _repair_challenges(challenges):
    repaired_reasons = 0
    repaired_answers = 0
    by_id = {str(question.get("id")): question for question in challenges}

    for qid, choice_map in WHY_WRONG_BY_CHOICE.items():
        question = by_id.get(qid)
        if not question:
            raise RuntimeError(f"v371 missing clinical challenge: {qid}")
        choices = question.get("choices") or []
        reasons = list(question.get("why_wrong") or [])
        if len(reasons) < len(choices):
            reasons.extend([""] * (len(choices) - len(reasons)))
        for index, choice in enumerate(choices):
            replacement = choice_map.get(choice)
            if replacement:
                reasons[index] = replacement
                repaired_reasons += 1
        question["why_wrong"] = reasons

    for qid, correct_choice in ANSWER_BY_CHOICE.items():
        question = by_id[qid]
        if correct_choice not in question.get("choices", []):
            raise RuntimeError(f"v371 missing keyed answer choice for: {qid}")
        question["answer"] = question["choices"].index(correct_choice)
        question["why_wrong"][question["answer"]] = "Correct."
        repaired_answers += 1

    cscc = by_id.get("v223_hn_cscc_fnd")
    if not cscc:
        raise RuntimeError("v371 missing clinical challenge: v223_hn_cscc_fnd")
    if CSCC_OLD_ANSWER in cscc.get("choices", []):
        index = cscc["choices"].index(CSCC_OLD_ANSWER)
        cscc["choices"][index] = CSCC_NEW_ANSWER
        cscc["answer"] = index
        cscc["why_wrong"][index] = (
            "Correct. Clinical named-nerve perineural spread is a major high-risk feature that changes imaging, regional planning, and adjuvant treatment."
        )
        repaired_answers += 1

    return {
        "distractor_reasons_repaired": repaired_reasons,
        "answer_keys_or_shapes_repaired": repaired_answers,
    }


def install_question_quality_repairs_v371(data_module, app_module):
    challenge_stats = _repair_challenges(data_module.CLINICAL_CHALLENGES_V119)

    original_get_items = data_module.get_adaptive_items_v120

    def get_adaptive_items_v371():
        items = original_get_items()
        for item in items:
            if item.get("stage") != "recognize" or not item.get("blind_reveal"):
                continue
            if not _reveals_topic(item):
                continue
            topic = _clean(item.get("topic"))
            prompt = _named_recognition_prompt(topic)
            item["daily_prompt"] = prompt
            item["prompt"] = prompt
            item["blind_reveal"] = False
            item.pop("blind_case_label", None)
        return items

    data_module.get_adaptive_items_v120 = get_adaptive_items_v371
    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {
        question["id"]: question
        for question in data_module.CLINICAL_CHALLENGES_V119
        if question.get("id")
    }
    app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119

    sample = get_adaptive_items_v371()
    named_cards = sum(
        1
        for item in sample
        if item.get("stage") == "recognize"
        and not item.get("blind_reveal")
        and (item.get("prompt") or "").startswith("For ")
    )
    return {**challenge_stats, "named_recognition_cards": named_cards}
