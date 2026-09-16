"""Regression audit for the exact post-v37.9 production registry."""

import re
from collections import Counter
from pathlib import Path

import runtime_entry_pasha as production
from daily_curriculum_quality_v379 import CURVEBALL_OVERRIDES, DAILY_OVERRIDES


GENERIC = (
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
    stages = Counter(item.get("concept_id") for item in items)

    if len(items) != 1950 or len(by_id) != 1950 or len(concepts) != 325:
        failures.append(f"registry_shape:{len(items)}:{len(by_id)}:{len(concepts)}")
    if any(count != 6 for count in stages.values()):
        failures.append("incomplete_six_stage_progression")

    repaired_daily = 0
    for key, (prompt, answer) in DAILY_OVERRIDES.items():
        matches = by_key.get(key, [])
        if not matches:
            failures.append("missing_daily_override:" + ":".join(key))
            continue
        repaired_daily += len(matches)
        for item in matches:
            if app._adaptive_question(item) != prompt:
                failures.append("daily_prompt:" + str(item.get("id")))
            if item.get("answer") != answer:
                failures.append("daily_answer:" + str(item.get("id")))
        if not prompt.endswith("?"):
            failures.append("override_not_question:" + ":".join(key))
        if len(words(answer)) < 55:
            failures.append("override_answer_too_thin:" + ":".join(key))
        if any(fragment in answer.lower() for fragment in GENERIC):
            failures.append("generic_daily_answer:" + ":".join(key))

    challenges = {q.get("id"): q for q in data.CLINICAL_CHALLENGES_V119}
    for qid, answer in CURVEBALL_OVERRIDES.items():
        challenge = challenges.get(qid) or {}
        if challenge.get("curveball_answer") != answer:
            failures.append("curveball_answer:" + qid)
        if len(words(answer)) < 45:
            failures.append("curveball_answer_too_thin:" + qid)
        if any(fragment in answer.lower() for fragment in GENERIC):
            failures.append("generic_curveball_answer:" + qid)

    for item in items:
        if not app._adaptive_question(item).strip():
            failures.append("empty_prompt:" + str(item.get("id")))
        if not str(item.get("answer") or "").strip():
            failures.append("empty_answer:" + str(item.get("id")))

    curveballs = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("curveball")]
    if len(curveballs) != 1597 or any(not str(q.get("curveball_answer") or "").strip() for q in curveballs):
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

    print(f"V379_ITEMS|{len(items)}")
    print(f"V379_CONCEPTS|{len(concepts)}")
    print(f"V379_COMPLETE_SIX_STAGE|{sum(c == 6 for c in stages.values())}/{len(stages)}")
    print(f"V379_BLINDED_LABELED|{sum(bool(i.get('blind_case_label')) for i in blinded)}/{len(blinded)}")
    print(f"V379_DAILY_PAIRS_REPAIRED|{repaired_daily}")
    print(f"V379_CURVEBALLS_REPAIRED|{len(CURVEBALL_OVERRIDES)}")
    print(f"V379_CURVEBALLS_WITH_ANSWERS|{sum(bool(q.get('curveball_answer')) for q in curveballs)}/{len(curveballs)}")
    print(f"V379_FAILURES|{len(failures)}")
    for failure in failures[:100]:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: next residual pathways and curveballs reveal complete decision-matched answers")


if __name__ == "__main__":
    main()
