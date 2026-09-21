#!/usr/bin/env python3
"""Fail closed on the v41.6 CSF-rhinorrhea on-call disposition pathway."""

import runtime_entry_pasha as production


DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "CSF Rhinorrhea"
QUESTION_ID = "v416_rhi_csf_oncall_disposition"


def main():
    data = production.runtime_entry.data
    rows = [row for row in data.DEEP_MODULES_V6.get(DOMAIN, []) if row.get("topic") == TOPIC]
    failures = []
    if len(rows) != 1:
        failures.append(f"canonical_topic_count:{len(rows)}")
    else:
        row = rows[0]
        blob = " ".join(str(row.get(field) or "").lower() for field in ("workup", "manage", "teach"))
        for anchor in (
            "on-call disposition",
            "expedited outpatient",
            "beta-2 transferrin",
            "thin-cut high-resolution ct",
            "fever or meningismus",
            "altered mental status",
            "recent sinonasal or skull-base surgery",
            "avoid nose blowing",
            "meningitis return precautions",
            "routine prophylactic antibiotics",
            "pneumococcal vaccination",
            "current cdc/acip",
        ):
            if anchor not in blob:
                failures.append("deep_missing:" + anchor)
        sources = " ".join(str(x).lower() for x in row.get("source_basis") or [])
        for anchor in ("cummings", "pasha", "k.j. lee", "33099888", "25918919", "cdc/acip", "40650638", "2026;136(1):36-49"):
            if anchor not in sources:
                failures.append("source_missing:" + anchor)
        if "meta-analysis. 2025. pmid 40650638" in sources:
            failures.append("stale_meta_analysis_year")

    questions = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("id") == QUESTION_ID]
    if len(questions) != 1:
        failures.append(f"question_count:{len(questions)}")
    else:
        q = questions[0]
        if q.get("focus") != "overnight_call":
            failures.append("question_not_overnight_call")
        if q.get("concept_id") != data._v6_item_id(DOMAIN, TOPIC):
            failures.append("question_concept_link")
        if not str(q.get("curveball_answer") or "").strip():
            failures.append("question_curveball_answer")
        qblob = " ".join(str(q.get(field) or "").lower() for field in ("stem", "explanation", "curveball"))
        for anchor in ("expedited", "outpatient", "fever", "meningismus", "recent postoperative"):
            if anchor not in qblob:
                failures.append("question_missing:" + anchor)

    print(f"CSF_ONCALL_FAILURES={len(failures)}")
    for failure in failures:
        print("FAIL:", failure)
    if failures:
        return 1
    print("PASS: CSF rhinorrhea has explicit outpatient, same-day, and emergency on-call disposition with diagnostics and meningitis precautions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
