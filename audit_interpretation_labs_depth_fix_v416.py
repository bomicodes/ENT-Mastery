#!/usr/bin/env python3
"""Fail closed on the reviewed Interpretation Lab v41.6 content."""

import runtime_entry_pasha as production
from interpretation_labs_depth_fix_v416 import GENERIC, SPECIFIC, P10_NEW, AJCC8


def main():
    labs = production.runtime_entry.data.INTERPRETATION_LABS
    index = {
        (lab_key, case.get("id")): case
        for lab_key, lab in labs.items()
        if isinstance(lab, dict)
        for case in lab.get("cases", [])
        if isinstance(case, dict)
    }
    prefixes = {"p": "pathology", "v": "vestibular", "a": "audiology", "e": "laryngeal-endoscopy"}
    failures = []
    for case_id, (why, follow) in SPECIFIC.items():
        case = index.get((prefixes[case_id[0]], case_id))
        if case is None:
            failures.append("missing_case:" + case_id)
            continue
        if case.get("why") != why or case.get("follow_answer") != follow:
            failures.append("specific_text_mismatch:" + case_id)
        if case.get("why") == GENERIC:
            failures.append("generic_why_retained:" + case_id)
        sources = " ".join(case.get("review_sources_v416") or []).lower()
        for anchor in ("cummings", "pasha", "k.j. lee"):
            if anchor not in sources:
                failures.append(f"textbook_missing:{case_id}:{anchor}")

    p10 = index.get(("pathology", "p10"), {})
    for anchor in ("nuclear", "grooves", "pseudoinclusions", "orphan annie"):
        if anchor not in str(p10.get("answer") or "").lower():
            failures.append("p10_missing:" + anchor)
    if p10.get("answer") != P10_NEW:
        failures.append("p10_answer_mismatch")

    for case_id, (_, addition) in AJCC8.items():
        case = index.get(("head-neck-imaging", case_id), {})
        if addition.strip() not in str(case.get("answer") or ""):
            failures.append("ajcc8_missing:" + case_id)
        if not str(case.get("staging_edition") or "").startswith("AJCC 8"):
            failures.append("edition_policy_missing:" + case_id)

    joined = " ".join(str(c.get("answer") or "") + " " + str(c.get("why") or "") for c in index.values()).lower()
    forbidden = (
        "recurrent laryngeal nerve, larynx, or prevertebral fascia is t4a",
        "radiographically or pathologically confirmed ene is itself an indication",
        "choose a bone-conduction pathway when the better ear has a significant conductive component",
    )
    for phrase in forbidden:
        if phrase in joined:
            failures.append("known_inaccuracy:" + phrase)

    print(f"INTERPRETATION_SPECIFIC_CASES={len(SPECIFIC)}")
    print(f"INTERPRETATION_DEPTH_FAILURES={len(failures)}")
    for failure in failures:
        print("FAIL:", failure)
    if failures:
        return 1
    print("PASS: 28 lab cases are specific, p10 teaches PTC nuclei, and AJCC 8 thresholds are accuracy-gated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
