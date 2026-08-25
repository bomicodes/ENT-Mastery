"""v17.6 — Deliberate learning-ladder curation, Otology pass 8.

Completes the two remaining v13.6 Otology foundations with application and
senior/chief decision layers. Strong foundation questions remain unchanged.
"""


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong, pearl, curveball, focus):
    return {
        "id": qid, "domain": "Otology / Neurotology", "topic": topic,
        "learning_stage": stage, "stem": stem, "choices": choices,
        "answer": answer, "explanation": explanation, "why_wrong": why_wrong,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette", "focus": focus,
    }


REVIEWED_FOUNDATION_IDS_V176 = {
    "v136_oto_21",  # Vestibular Rehabilitation
    "v136_oto_22",  # Vestibular Test Battery
}


VIGNETTES_V176 = [
    _q(
        "v176_oto_vr_app", "Vestibular Rehabilitation", "application",
        "Three weeks after a unilateral vestibular neuritis, a patient no longer has spontaneous vertigo but remains visually blurry with head turns and avoids walking outside because movement provokes disequilibrium. What is the best next management step?",
        ["Continue scheduled meclizine until all motion sensitivity disappears", "Begin targeted vestibular rehabilitation with gaze-stabilization, balance, habituation, and progressive walking while tapering unnecessary suppressants", "Prescribe strict bed rest", "Perform repeated canalith repositioning despite absent positional nystagmus"], 1,
        "After the acute phase of a stable unilateral vestibular loss, recovery depends on central compensation. Gaze-stabilization and graded balance/motion exercises provide the error signals needed for adaptation, while prolonged vestibular suppression and avoidance can slow compensation.",
        ["Chronic suppressants can blunt the vestibular error signals needed for compensation.", "Correct. Rehabilitation should match the residual gaze and balance deficits and progressively restore motion exposure.", "Bed rest promotes deconditioning and delays compensation.", "Canalith maneuvers are appropriate only when positional testing demonstrates BPPV."],
        "Acute vestibular suppressants are symptom tools; vestibular rehabilitation is the recovery tool once the acute crisis has passed.",
        "What bedside finding would make you test specifically for secondary BPPV before simply escalating habituation exercises?",
        "boards",
    ),
    _q(
        "v176_oto_vr_snr", "Vestibular Rehabilitation", "senior_decision",
        "Six weeks after vestibular neuritis, a patient has adhered to vestibular therapy but is getting worse rather than better, with new direction-changing gaze-evoked nystagmus and progressive gait ataxia. What is the best senior-level decision?",
        ["Increase exercise intensity because all persistent dizziness represents incomplete compensation", "Stop treating this as uncomplicated peripheral compensation failure and reassess urgently for a central or alternative diagnosis", "Add chronic benzodiazepines and continue the same plan", "Reassure that worsening neurologic signs are expected during vestibular rehabilitation"], 1,
        "Vestibular rehabilitation is appropriate only after the diagnosis is sufficiently secure. Failure to follow an expected recovery trajectory—especially with new central ocular-motor or gait signs—should reopen localization and prompt neurologic/imaging evaluation rather than reflexively intensifying therapy.",
        ["More rehabilitation is unsafe when the syndrome has developed central red flags.", "Correct. Senior care recognizes when a rehabilitation problem has become a diagnostic problem again.", "Chronic benzodiazepines can impede compensation and do not explain progressive neurologic findings.", "Direction-changing gaze-evoked nystagmus and worsening ataxia are not routine compensation findings."],
        "A plateau can be rehabilitation; progressive central signs are re-diagnosis.",
        "Which ocular-motor findings most strongly separate central vestibular disease from an incompletely compensated unilateral peripheral loss?",
        "overnight_call",
    ),

    _q(
        "v176_oto_vtb_app", "Vestibular Test Battery", "application",
        "A patient with episodic imbalance has normal caloric responses but an abnormal video head-impulse test for one horizontal canal. Which interpretation is most appropriate?",
        ["One test must be discarded because calorics and vHIT should always agree", "The tests interrogate the vestibulo-ocular reflex at different stimulus frequencies, so discordance can be real and should be interpreted with the clinical syndrome", "Calorics measure only saccular function", "vHIT is primarily a hearing test"], 1,
        "Caloric irrigation tests the horizontal-canal VOR at very low frequencies, whereas vHIT interrogates higher-frequency head impulses. Disease can affect these frequency ranges differently, so discordance is physiologically plausible and sometimes diagnostically useful.",
        ["Vestibular tests are not redundant copies of the same stimulus.", "Correct. Interpret the pattern across tests rather than declaring a winner.", "Calorics predominantly interrogate low-frequency horizontal-canal/superior-vestibular-nerve function.", "vHIT measures high-frequency vestibulo-ocular reflex behavior, not auditory thresholds."],
        "A vestibular battery is a set of different physiologic stress tests, not a collection of interchangeable pass/fail screens.",
        "How would a pattern of reduced calorics with preserved vHIT influence the differential in a patient suspected of Ménière disease?",
        "boards",
    ),
    _q(
        "v176_oto_vtb_snr", "Vestibular Test Battery", "senior_decision",
        "A patient with chronic disequilibrium has normal calorics and vHIT but absent cervical VEMPs bilaterally. The patient is 79 years old, has no sound- or pressure-induced vertigo, and otherwise has a nonlocalizing examination. What is the best interpretation?",
        ["Diagnose bilateral inferior vestibular neuritis from the VEMP result alone", "Interpret the VEMP in the context of age, stimulus adequacy, conductive status, and the rest of the battery before assigning a lesion", "Schedule bilateral labyrinthectomy", "Conclude that normal calorics and vHIT exclude all vestibular disease"], 1,
        "cVEMP responses depend on saccular/inferior-vestibular pathways but are also affected by age, sternocleidomastoid activation, stimulus delivery, and conductive hearing status. An isolated absent response—particularly in an older adult—must be contextualized rather than overlocalized.",
        ["A single physiologic abnormality does not establish bilateral neuritis without a compatible syndrome.", "Correct. Senior interpretation integrates test limitations, age effects, technical quality, and concordance with history and other end organs.", "Destructive surgery has no basis in a nonlocalizing test pattern.", "Normal canal tests do not assess every vestibular end organ or every central vestibular disorder."],
        "The hardest part of vestibular testing is not obtaining abnormalities; it is deciding which abnormalities actually explain the patient.",
        "What cVEMP and oVEMP pattern would you expect from a true third-window syndrome, and how would you correlate it with audiometry and CT?",
        "boards",
    ),
]


def apply_learning_ladders_v176(challenges, id_factory):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reviewed = 0
    for qid in REVIEWED_FOUNDATION_IDS_V176:
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v17.6: reviewed foundation missing from live registry: {qid}")
        q["learning_stage"] = "foundation"
        q["ladder_reviewed"] = True
        reviewed += 1

    existing = {q.get("id") for q in challenges if q.get("id")}
    added = 0
    for q in VIGNETTES_V176:
        item = dict(q)
        if item["id"] in existing:
            continue
        item["concept_id"] = id_factory(item["domain"], item["topic"])
        item["ladder_reviewed"] = True
        challenges.append(item)
        existing.add(item["id"])
        added += 1

    return {
        "reviewed_foundations": reviewed,
        "added_questions": added,
        "topics": sorted({q["topic"] for q in VIGNETTES_V176}),
    }
