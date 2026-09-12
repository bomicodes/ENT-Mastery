"""Persistent learner-experience audit for ENT Mastery.

This audit treats discoverability and teaching flow as release requirements, not cosmetic QA.
A concept may be factually complete yet still fail if a resident cannot find the management path
where it logically belongs. Contracts here are intentionally small and extensible; add new high-yield
learner failures as they are discovered during Deep Curriculum -> Concept Check -> Daily Curriculum review.
"""
import runtime_entry
from concept_check_board_repair_v177 import _find_module

CONTRACTS = {
    "cc-v112-rec-rhinology-allergy-skull-base-sinonasal-malignancy": {
        "canonical_topic": "Sinonasal Malignancy",
        "concept_id": "v6-rhinology-allergy-skull-base-sinonasal-malignancy",
        "heading": "### Esthesioneuroblastoma (Olfactory Neuroblastoma; ONB) — management pathway",
        "aliases": ("esthesioneuroblastoma", "olfactory neuroblastoma", "onb", "esthesioblastoma"),
        "required_terms": (
            "hyams", "kadish", "surgical resection", "adjuvant radiotherapy",
            "induction chemotherapy", "node-positive", "cn0", "elective neck irradiation",
            "20 years", "surveillance",
        ),
        "minimum_subsection_words": 500,
        "learning_goal": "A resident looking under Sinonasal Malignancy can find a complete ONB diagnostic-risk-treatment-neck-surveillance pathway without hunting another module or source list.",
    },
}


def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    deep_modules = data.DEEP_MODULES_V6
    v6_item_id = data._v6_item_id
    by = {str(q.get("id") or ""): q for q in checks or []}
    failures = []

    for qid, contract in CONTRACTS.items():
        q = by.get(qid)
        if q is None:
            failures.append("learner_missing_concept:" + qid)
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != contract["canonical_topic"] or cid != contract["concept_id"]:
            failures.append("learner_wrong_canonical:" + qid)

        answer = str(q.get("answer_text") or "")
        heading = contract["heading"]
        if heading not in answer:
            failures.append("learner_not_discoverable:" + qid + ":missing_heading")
            section = ""
        else:
            section = answer.split(heading, 1)[1]
        low = section.lower()
        if len(section.split()) < contract["minimum_subsection_words"]:
            failures.append("learner_path_too_shallow:" + qid + ":" + str(len(section.split())))
        for term in contract["required_terms"]:
            if term not in low:
                failures.append("learner_path_missing_management:" + qid + ":" + term)

        aliases = {str(x).strip().lower() for x in q.get("search_aliases") or []}
        for alias in contract["aliases"]:
            if alias not in aliases:
                failures.append("learner_alias_missing:" + qid + ":" + alias)

        # A management path must be in learner-facing prose, not merely sources/traps/metadata.
        for verb in ("resect", "radiotherapy", "consider", "surveillance"):
            if verb not in low:
                failures.append("learner_actionability:" + qid + ":" + verb)

    print("LEARNER_EXPERIENCE_CONTRACTS|" + str(len(CONTRACTS)))
    print("LEARNER_EXPERIENCE_FAILURES|" + str(len(failures)))
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: learner-facing high-yield management paths are explicit, searchable, actionable, and located in their expected canonical concepts")


if __name__ == "__main__":
    main()
