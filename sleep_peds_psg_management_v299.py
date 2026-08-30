"""v29.9 — add the missing perioperative-management layer to Pediatric PSG Interpretation.

The existing v26.6 ladder already teaches pediatric-vs-adult interpretation, low-event-rate
clinical significance, and senior recognition of postoperative hypoventilation. This module
adds only the distinct management decision that PSG must drive after tonsillectomy planning:
which children require overnight inpatient monitoring for severe OSA/high-risk age.
"""

DOMAIN = "Sleep Surgery"
TOPIC = "Pediatric PSG Interpretation"
QUESTION_ID = "v299_sleep_peds_psg_mgt"


def apply_sleep_peds_psg_management_v299(challenges, item_id_fn):
    concept_id = item_id_fn(DOMAIN, TOPIC)
    if any(q.get("id") == QUESTION_ID for q in challenges):
        return {"added": 0, "concept_id": concept_id}

    q = {
        "id": QUESTION_ID,
        "domain": DOMAIN,
        "topic": TOPIC,
        "concept_id": concept_id,
        "learning_stage": "management",
        "stem": (
            "A 4-year-old with adenotonsillar hypertrophy is scheduled for tonsillectomy for PSG-confirmed OSA. "
            "The study shows an AHI of 12 obstructive events/hour and an oxygen saturation nadir of 82%. The child "
            "has no other major comorbidity. How should the PSG change the postoperative disposition plan?"
        ),
        "choices": [
            "Arrange overnight inpatient monitoring because the AHI meets the severe-OSA threshold used by the AAO-HNS tonsillectomy guideline even though the oxygen nadir is not below 80%",
            "Plan routine unmonitored discharge because inpatient monitoring is recommended only when both AHI is at least 10 and oxygen nadir is below 80%",
            "Ignore the PSG severity because only children younger than 3 years require overnight monitoring after tonsillectomy",
            "Cancel tonsillectomy and prescribe supplemental oxygen alone because any AHI above 10 makes surgery contraindicated",
        ],
        "answer": 0,
        "explanation": (
            "The AAO-HNS tonsillectomy guideline recommends overnight inpatient monitoring after tonsillectomy "
            "for children younger than 3 years OR for severe OSA, defined as AHI at least 10 obstructive events/hour, "
            "oxygen saturation nadir below 80%, or both. This 4-year-old meets the severe-OSA criterion by AHI alone. "
            "The management lesson is that PSG is not only diagnostic: specific physiologic findings change postoperative "
            "airway surveillance and disposition. Additional comorbidity or gas-exchange abnormalities may justify even "
            "greater caution, but they are not required for this guideline-based overnight-monitoring decision."
        ),
        "why_wrong": [
            "Correct. Severe pediatric OSA is sufficient for overnight monitoring; the guideline uses AHI >=10, nadir <80%, or both, so the patient does not need to meet both PSG criteria.",
            "The criteria are joined by OR, not AND. Requiring both severe event burden and nadir <80% would incorrectly discharge some guideline-defined high-risk children.",
            "Age under 3 is an independent admission trigger, not the only trigger. Older children with severe OSA also warrant overnight inpatient monitoring after tonsillectomy.",
            "Severe OSA increases perioperative monitoring needs but is not itself a contraindication to adenotonsillar surgery; oxygen alone does not correct the anatomic obstruction or replace definitive OSA treatment planning.",
        ],
        "board_pearl": (
            "Post-tonsillectomy monitoring: age <3 years OR severe OSA. AAO-HNS severe OSA threshold for this decision: "
            "AHI >=10 obstructive events/hour, oxygen nadir <80%, or both."
        ),
        "curveball": (
            "How would the disposition change for a 5-year-old with AHI 6/hour but oxygen nadir 77%, or for a 2-year-old "
            "whose PSG shows only mild OSA?"
        ),
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "focus": "perioperative_management",
        "ladder_reviewed": True,
        "_coverage_reviewed_v211": True,
        "_semantic_review_v299": True,
        "source_basis": [
            "AAO-HNSF Clinical Practice Guideline: Tonsillectomy in Children (Update), 2019 — KAS12 inpatient monitoring after tonsillectomy"
        ],
    }
    challenges.append(q)
    return {"added": 1, "concept_id": concept_id}
