"""v22.6 — targeted learning-ladder stem quality repair.

Expands two otherwise sound foundation prompts that tripped the runtime
thin-stem heuristic. Clinical content and answer keys are unchanged.
"""

REPAIRS = {
    "v223_hn_merkel_fnd": (
        "An older immunosuppressed patient develops a rapidly enlarging, painless, violaceous skin nodule on the sun-exposed cheek. Biopsy shows a primary cutaneous neuroendocrine carcinoma. Which description best fits this diagnosis?"
    ),
    "v225_hn_orn_fnd": (
        "A patient previously treated with high-dose mandibular radiation develops persistent exposed nonhealing jaw bone months later. Recurrent malignancy has been excluded. Which description best defines osteoradionecrosis of the jaw?"
    ),
}


def apply_ladder_quality_stem_repair_v226(challenges):
    by_id = {str(q.get("id")): q for q in challenges if q.get("id")}
    repaired = []
    for qid, stem in REPAIRS.items():
        row = by_id.get(qid)
        if row is None:
            raise RuntimeError("v226 missing target: " + qid)
        row["stem"] = stem
        repaired.append(qid)
    return {"repaired": len(repaired), "ids": repaired}
