"""v24.6 — Pediatric Otolaryngology deliberate ladder progress hard gate.

Protects the 25 exact canonical Pediatric topics deliberately curated in v24.1-v24.5
while the remaining domain inventory is closed. This is intentionally a progress gate,
not a claim that the full 40-topic Pediatric domain is complete.
"""
from collections import defaultdict
import runtime_entry as rt

DOMAIN = "Pediatric Otolaryngology"
STAGES = {"foundation", "application", "senior_decision"}
EXPECTED_TOPICS = [
    "Choanal Atresia",
    "Pediatric Aspiration",
    "Supraglottoplasty",
    "Laryngotracheal Reconstruction",
    "Thyroglossal Duct Cyst",
    "Pediatric OSA / Adenotonsillar Disease",
    "Pediatric Airway Foreign Body",
    "Pediatric Subglottic Stenosis",
    "Laryngomalacia",
    "AOM / OME / Tympanostomy Decisions",
    "Laryngotracheal Cleft",
    "Pediatric Tracheostomy / Decannulation",
    "Pediatric Vocal Fold Immobility",
    "Subglottic Hemangioma",
    "Tracheomalacia / Bronchomalacia",
    "Recurrent Respiratory Papillomatosis",
    "Pediatric Deep Neck Infection",
    "Recurrent Tonsillitis Decision-Making",
    "Lymphatic Malformation",
    "Branchial Cleft Anomalies",
    "Pediatric Hearing Loss Workup",
    "Congenital CMV Hearing Loss",
    "Congenital Neck Masses",
    "Button Battery Ingestion",
    "Microtia / Aural Atresia",
]


def main():
    data = rt.data
    canonical = {
        m.get("topic")
        for m in data.DEEP_MODULES_V6.get(DOMAIN, [])
        if m.get("topic")
    }
    missing_registry = [t for t in EXPECTED_TOPICS if t not in canonical]
    if missing_registry:
        raise AssertionError(f"Pediatric expected topics missing from canonical registry: {missing_registry}")

    by_cid = defaultdict(list)
    for q in data.CLINICAL_CHALLENGES_V119:
        cid = q.get("concept_id")
        if cid:
            by_cid[cid].append(q)

    failures = []
    for topic in EXPECTED_TOPICS:
        cid = data._v6_item_id(DOMAIN, topic)
        linked = by_cid.get(cid, [])
        reviewed = [q for q in linked if q.get("ladder_reviewed")]
        stages = {q.get("learning_stage") for q in reviewed if q.get("learning_stage") in STAGES}
        if not reviewed:
            failures.append(f"{topic}: no ladder_reviewed runtime question")
        elif stages != STAGES:
            failures.append(f"{topic}: missing stages {sorted(STAGES - stages)}")

    if failures:
        raise AssertionError("Pediatric ladder progress regression:\n" + "\n".join(failures))

    print(
        f"PEDIATRIC_LADDER_PROGRESS_PASS|domain={DOMAIN}|protected={len(EXPECTED_TOPICS)}|"
        f"required_stages={','.join(sorted(STAGES))}"
    )


if __name__ == "__main__":
    main()
