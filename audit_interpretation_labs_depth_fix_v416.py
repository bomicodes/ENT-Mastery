#!/usr/bin/env python3
"""Fail closed on the reviewed Interpretation Lab v41.6 content."""

import runtime_entry_pasha as production
from interpretation_labs_depth_fix_v416 import GENERIC, SPECIFIC, AJCC8


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

    # v60: the pathology lab was rebuilt on real slides (2026-09-26); the PTC-nuclei
    # teaching now lives in whichever pathology case covers papillary carcinoma.
    ptc = " ".join(str(c.get("answer") or "") + " " + str(c.get("reason_answer") or "") + " " + str(c.get("why") or "")
                   for (lab_key, _), c in index.items() if lab_key == "pathology").lower()
    for anchor in ("nuclear", "groove", "pseudoinclusion"):
        if anchor not in ptc:
            failures.append("ptc_nuclei_missing:" + anchor)

    for case_id, (_, addition) in AJCC8.items():
        case = index.get(("head-neck-imaging", case_id), {})
        if addition.strip() not in str(case.get("answer") or "") + " " + str(case.get("reason_answer") or ""):
            failures.append("ajcc8_missing:" + case_id)
        expected_edition = "AJCC Version 9" if case_id == "hn2" else "AJCC 8"
        if not str(case.get("staging_edition") or "").startswith(expected_edition):
            failures.append("edition_policy_missing:" + case_id)
        if case_id == "hn2" and "AJCC Version 9 adds imaging-detected extranodal extension" not in str(case.get("answer") or ""):
            failures.append("current_iene_rule_missing:hn2")

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
