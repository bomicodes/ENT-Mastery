"""v15.6 — First installment of ladder-repair work identified by
audit_content_depth_v155.py.

Per the stated philosophy: upgrade redundant/weak questions in place rather
than pile on more content, and only add new questions where a genuine rung
is missing. This is a first, high-confidence batch, not a clearance of the
full 55-duplicate / 58-underweighted / 1-escalation-only backlog — those
remain for subsequent passes.

Two kinds of change:

1. VIGNETTE_UPGRADES_V156 — keyed by existing vignette ID. Applied as an
   in-place field overwrite at runtime (same ID, same concept_id linkage,
   new stem/choices/content). This is deliberately NOT a new vignette merge
   — it replaces near-duplicate content with content that actually fills the
   missing rung, so the topic's total question count does not inflate for
   inflation's own sake.

2. NEW_FOUNDATION_VIGNETTES_V156 — genuinely new questions, only for the two
   topics the audit flagged as having zero foundation-level content
   (Post-Tonsillectomy Hemorrhage: escalation-only; Carotid Blowout
   Syndrome: underweighted and missing its foundation rung specifically).
"""

VIGNETTE_UPGRADES_V156 = {
    "v135_oto_03": {
        "stem": "A patient with known cholesteatoma is being counseled on surgical indications. Which finding, if present, most strongly indicates surgery should not be delayed regardless of symptom severity?",
        "choices": [
            "Mild conductive hearing loss alone with a small, stable-appearing retraction pocket",
            "Radiographic or clinical evidence of labyrinthine fistula, facial nerve involvement, or intracranial extension",
            "Patient preference to avoid surgery when symptoms are minimal",
            "A normal contralateral ear"
        ],
        "answer": 1,
        "explanation": "Cholesteatoma is managed surgically because it is locally destructive, not because of symptom severity alone. Evidence of erosion into the labyrinth (fistula), facial nerve canal involvement, or intracranial extension represents a complication trajectory that should not be watched — these findings escalate urgency regardless of how mild the patient's current symptoms are.",
        "why_wrong": [
            "Mild hearing loss with a stable pocket may still warrant surgery given the progressive nature of the disease, but this alone is not the strongest indicator of non-negotiable urgency compared with a complication finding.",
            "Correct.",
            "Cholesteatoma's natural history of progressive bony erosion means patient preference for observation should be revisited specifically when a complication finding is present, since delay carries a different risk calculus at that point.",
            "A normal contralateral ear says nothing about the urgency of the affected side."
        ],
        "board_pearl": "Cholesteatoma surgical urgency tracks disease behavior (erosion, fistula, nerve involvement), not symptom severity — a patient can feel fine and still have a surgical emergency brewing on imaging or exam.",
        "curveball": "Intraoperatively, a fistula is confirmed over the lateral semicircular canal with the patient's hearing still serviceable. How does that specific finding change how aggressively the matrix over the fistula should be dissected?",
        "learning_stage": "application",
        "focus": "boards",
    },
    "v148_oto_01": {
        "stem": "A patient reports 'sudden hearing loss' in one ear. Examination shows a large cerumen impaction fully occluding the canal; after removal, hearing is subjectively normal and Weber lateralizes appropriately once the canal is clear. Why does this case NOT represent true sudden sensorineural hearing loss?",
        "choices": [
            "Because SSNHL by definition requires bilateral involvement",
            "Because the hearing loss was conductive and mechanically reversible once the obstructing cerumen was removed, rather than reflecting a cochlear or retrocochlear process",
            "Because SSNHL never causes a subjective sensation of sudden loss",
            "Because the patient's age excludes the diagnosis"
        ],
        "answer": 1,
        "explanation": "A meaningful fraction of 'sudden hearing loss' presentations are conductive and reversible — cerumen impaction being the classic example. True SSNHL is a diagnosis of exclusion requiring a sensorineural pattern (normal-appearing canal/TM, air-bone gap absent, Weber lateralizing away from the affected ear if truly unilateral SNHL) that does not resolve with removal of a mechanical obstruction. This distinction matters because it changes both workup and urgency.",
        "why_wrong": [
            "SSNHL is typically unilateral, not bilateral, in its classic presentation.",
            "Correct.",
            "SSNHL classically does present as a subjectively sudden loss; that is not what distinguishes it from this case.",
            "Age is not the discriminating feature here — the exam and reversibility with cerumen removal are."
        ],
        "board_pearl": "Always clear the canal and get a real look at the TM before treating 'sudden hearing loss' as SSNHL — a reversible conductive cause is a common and easily missed mimic that changes the entire workup pathway.",
        "curveball": "After cerumen removal, hearing is improved but a measurable air-bone gap persists on formal audiometry. What does that residual gap suggest, and how does the workup differ from true SSNHL?",
        "learning_stage": "application",
        "focus": None,
    },
    "v116-end-01": {
        "stem": "A patient's thyroid nodule FNA returns Bethesda III (atypia of undetermined significance). The patient has no high-risk clinical features and prefers to avoid surgery if reasonably possible. What is the most appropriate next step?",
        "choices": [
            "Proceed directly to total thyroidectomy since any indeterminate result requires definitive surgery",
            "Repeat FNA or pursue molecular testing to refine malignancy risk before choosing between surveillance and diagnostic lobectomy",
            "Disregard the result and resume routine annual ultrasound surveillance with no further action",
            "Begin thyroid hormone suppression therapy to shrink the nodule"
        ],
        "answer": 1,
        "explanation": "Bethesda III is genuinely indeterminate, not a call for automatic surgery or automatic dismissal. Repeat FNA or molecular testing helps refine which patients can be reasonably observed versus which should proceed to diagnostic lobectomy, matching the intensity of the next step to the patient's actual risk rather than defaulting to either extreme.",
        "why_wrong": [
            "Total thyroidectomy for an indeterminate result overtreats the many patients who turn out to have benign disease.",
            "Correct.",
            "Bethesda III is not the same as a benign (Bethesda II) result and should not be treated as one.",
            "Thyroid hormone suppression is not an evidence-supported strategy for managing an indeterminate cytology result and does not address the diagnostic uncertainty."
        ],
        "board_pearl": "The Bethesda system's indeterminate categories (III-V) are exactly where molecular testing adds real decision-making value — know this is a distinct decision point from the initial 'does this nodule need an FNA at all' question.",
        "curveball": "Molecular testing returns a result associated with substantial malignancy risk. How does that shift the recommended extent of initial surgery compared with a reassuring result?",
        "learning_stage": "application",
        "focus": "boards",
    },
}

NEW_FOUNDATION_VIGNETTES_V156 = [
    {
        "id": "v156_gen_pth_fnd", "domain": "General ENT / Emergencies", "topic": "Post-Tonsillectomy Hemorrhage",
        "stem": "A resident is taught to distinguish 'primary' from 'secondary' post-tonsillectomy hemorrhage. What defines each, and why does the distinction matter clinically?",
        "choices": [
            "Primary bleeding occurs within the first 24 hours (usually a technical/vascular issue at the operative site); secondary bleeding occurs after day 5-10 (often related to eschar separation) — the timing affects the likely cause and index of suspicion, not just the calendar count",
            "Primary and secondary are interchangeable terms for the same event",
            "Primary bleeding only occurs in children; secondary bleeding only occurs in adults",
            "The distinction has no clinical significance and does not affect management"
        ],
        "answer": 0,
        "explanation": "Primary hemorrhage (within the first 24 hours) usually reflects a technical issue with hemostasis at the time of surgery. Secondary hemorrhage (classically day 5-10) usually relates to sloughing of the eschar covering the tonsillar fossa as it heals. Both are true emergencies, but knowing which window a patient is in helps calibrate suspicion — secondary bleeding is the more common reason a patient re-presents from home after discharge.",
        "why_wrong": ["Correct.", "These describe genuinely different timeframes and different underlying mechanisms, not interchangeable labels.", "Both patterns occur across all ages; this is not an age-based distinction.", "The timing meaningfully affects clinical suspicion and counseling, even though both categories require prompt evaluation."],
        "board_pearl": "Warn every tonsillectomy patient and family specifically about the day 5-10 window before discharge — secondary hemorrhage is the pattern most likely to present at home rather than in the hospital.",
        "curveball": "A child on postoperative day 7 has a single episode of blood-tinged saliva that resolves before arrival. Does a benign-appearing exam on arrival rule out a clinically significant secondary bleed?",
        "tier": "Curated board-style", "mode": "Vignette", "learning_stage": "foundation", "focus": None,
    },
    {
        "id": "v156_gen_cbs_fnd", "domain": "General ENT / Emergencies", "topic": "Carotid Blowout Syndrome",
        "stem": "Which combination of factors most classically predisposes a head and neck cancer patient to carotid blowout syndrome?",
        "choices": [
            "Prior neck irradiation combined with a wound-healing problem such as pharyngocutaneous fistula, flap breakdown, or exposed/infected vessel in the operative bed",
            "Young age and no prior treatment history",
            "A well-healed, unirradiated neck with normal wound healing",
            "Isolated hypertension with no local neck pathology"
        ],
        "answer": 0,
        "explanation": "Carotid blowout syndrome arises from breakdown of the vessel wall's normal protective coverage — classically in a previously irradiated field where tissue healing is already impaired, compounded by a local problem such as a fistula, wound dehiscence, or infection that exposes or directly threatens the vessel. Recognizing this risk profile is what should raise suspicion before a catastrophic bleed occurs, not just reacting once one happens.",
        "why_wrong": ["Correct.", "This is a disease of compromised, previously treated tissue, not a presentation in young, treatment-naive patients.", "Normal healing in an unirradiated neck is the opposite of the risk profile for this condition.", "Hypertension is not the defining risk factor; local vascular/wound-bed compromise is."],
        "board_pearl": "Think of carotid blowout risk as a running background assessment for any irradiated neck-dissection patient with a wound problem — the diagnosis is made by recognizing the risk profile before the bleed, not only after it starts.",
        "curveball": "A patient with this exact risk profile has a wound clinic visit for slow-healing tissue but no bleeding at all. What surveillance or imaging consideration is reasonable given the underlying risk?",
        "tier": "Curated board-style", "mode": "Vignette", "learning_stage": "foundation", "focus": None,
    },
]


def apply_vignette_upgrades_v156(challenges):
    by_id = {q["id"]: q for q in challenges}
    for qid, fields in VIGNETTE_UPGRADES_V156.items():
        target = by_id.get(qid)
        if target is not None:
            target.update(fields)
    return challenges


def apply_new_foundation_vignettes_v156(challenges, v6_item_id):
    existing_ids = {q.get("id") for q in challenges}
    for q_src in NEW_FOUNDATION_VIGNETTES_V156:
        if q_src.get("id") in existing_ids:
            continue
        q = dict(q_src)
        q["concept_id"] = v6_item_id(q["domain"], q["topic"])
        challenges.append(q)
        existing_ids.add(q["id"])
    return challenges
