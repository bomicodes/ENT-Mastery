"""Regression audit for the exact post-v37.7 production registry."""

import re
from collections import Counter
from pathlib import Path

import runtime_entry_pasha as production
from daily_curriculum_quality_v377 import CURVEBALL_OVERRIDES, DAILY_OVERRIDES


GENERIC_ANSWER_FRAGMENTS = (
    "depends on the anatomy and patient factors",
    "individualize based on clinical context",
    "the parent card",
)


def words(value):
    return re.findall(r"\b[\w'-]+\b", str(value or ""))


def main():
    data = production.runtime_entry.data
    app = production.runtime_entry.app_mod
    items = data.get_adaptive_items_v120()
    failures = []
    by_id = {item.get("id"): item for item in items}
    by_key = {}
    for item in items:
        by_key.setdefault((item.get("topic"), item.get("stage")), []).append(item)
    concepts = {item.get("concept_id") for item in items}

    if len(items) != 1950 or len(by_id) != 1950 or len(concepts) != 325:
        failures.append(f"registry_shape:{len(items)}:{len(by_id)}:{len(concepts)}")

    stage_counts = Counter(item.get("concept_id") for item in items)
    if any(count != 6 for count in stage_counts.values()):
        failures.append("incomplete_six_stage_progression")

    repaired_daily = 0
    for key, (expected_prompt, expected_answer) in DAILY_OVERRIDES.items():
        matches = by_key.get(key, [])
        if not matches:
            failures.append("missing_daily_override:" + ":".join(key))
            continue
        repaired_daily += len(matches)
        for item in matches:
            if app._adaptive_question(item) != expected_prompt:
                failures.append("daily_prompt:" + str(item.get("id")))
            if item.get("answer") != expected_answer:
                failures.append("daily_answer:" + str(item.get("id")))
        if not expected_prompt.endswith("?"):
            failures.append("override_not_question:" + ":".join(key))
        if len(words(expected_answer)) < 55:
            failures.append("override_answer_too_thin:" + ":".join(key))
        if any(fragment in expected_answer.lower() for fragment in GENERIC_ANSWER_FRAGMENTS):
            failures.append("generic_daily_answer:" + ":".join(key))

    challenges = {q.get("id"): q for q in data.CLINICAL_CHALLENGES_V119}
    for qid, expected_answer in CURVEBALL_OVERRIDES.items():
        challenge = challenges.get(qid) or {}
        if challenge.get("curveball_answer") != expected_answer:
            failures.append("curveball_answer:" + qid)
        if len(words(expected_answer)) < 45:
            failures.append("curveball_answer_too_thin:" + qid)
        if any(fragment in expected_answer.lower() for fragment in GENERIC_ANSWER_FRAGMENTS):
            failures.append("generic_curveball_answer:" + qid)

    for item in items:
        if not app._adaptive_question(item).strip():
            failures.append("empty_prompt:" + str(item.get("id")))
        if not str(item.get("answer") or "").strip():
            failures.append("empty_answer:" + str(item.get("id")))

    curveballs = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("curveball")]
    if len(curveballs) != 1597 or any(
        not str(q.get("curveball_answer") or "").strip() for q in curveballs
    ):
        failures.append(f"curveball_completion:{len(curveballs)}")

    blinded = [item for item in items if item.get("blind_reveal")]
    if len(blinded) != 114 or any(not item.get("blind_case_label") for item in blinded):
        failures.append(f"blinded_case_contract:{len(blinded)}")

    for template, label in {
        "daily_adaptive.html": "Reveal answer",
        "clinical_challenge.html": "Reveal curveball answer",
    }.items():
        if label not in (Path("templates") / template).read_text(encoding="utf-8"):
            failures.append("missing_answer_control:" + template)

    print(f"V377_ITEMS|{len(items)}")
    print(f"V377_CONCEPTS|{len(concepts)}")
    print(
        "V377_COMPLETE_SIX_STAGE|"
        f"{sum(count == 6 for count in stage_counts.values())}/{len(stage_counts)}"
    )
    print(
        "V377_BLINDED_LABELED|"
        f"{sum(bool(i.get('blind_case_label')) for i in blinded)}/{len(blinded)}"
    )
    print(f"V377_DAILY_PAIRS_REPAIRED|{repaired_daily}")
    print(f"V377_CURVEBALLS_REPAIRED|{len(CURVEBALL_OVERRIDES)}")
    print(
        "V377_CURVEBALLS_WITH_ANSWERS|"
        f"{sum(bool(q.get('curveball_answer')) for q in curveballs)}/{len(curveballs)}"
    )
    print(f"V377_FAILURES|{len(failures)}")
    for failure in failures[:100]:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: targeted pathway questions and curveballs reveal decision-matched answers")


if __name__ == "__main__":
    main()
