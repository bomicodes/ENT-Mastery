"""Regression audit for the exact post-v37.4 production registry."""

import re
from collections import Counter
from pathlib import Path

import runtime_entry_pasha as production
from daily_curriculum_quality_v374 import CURVEBALL_OVERRIDES, DAILY_OVERRIDES


STALE_DAILY_PREFIXES = (
    "How would you build a practical map of",
    "What structure or failure mechanism is responsible for",
)
STALE_CURVEBALL_PREFIX = (
    "For operative/procedural cases, explicitly state indication, setup, landmarks, danger structures,"
)
EXPECTED_STAGES = {"recognize", "localize", "differentiate", "workup", "manage", "operate", "teach"}


def words(value):
    return re.findall(r"\b[\w'-]+\b", str(value or ""))


def main():
    data = production.runtime_entry.data
    app = production.runtime_entry.app_mod
    items = data.get_adaptive_items_v120()
    failures = []
    by_id = {item.get("id"): item for item in items}
    by_key = {(item.get("topic"), item.get("stage")): item for item in items}
    concepts = {item.get("concept_id") for item in items}

    if len(items) != 1950 or len(by_id) != 1950 or len(concepts) != 325:
        failures.append(f"registry_shape:{len(items)}:{len(by_id)}:{len(concepts)}")

    stage_counts = Counter(item.get("concept_id") for item in items)
    if any(count != 6 for count in stage_counts.values()):
        failures.append("incomplete_six_stage_progression")

    for key, (expected_prompt, expected_answer) in DAILY_OVERRIDES.items():
        item = by_key.get(key) or {}
        if app._adaptive_question(item) != expected_prompt:
            failures.append("daily_prompt:" + ":".join(key))
        if item.get("answer") != expected_answer:
            failures.append("daily_answer:" + ":".join(key))
        if not expected_prompt.endswith("?") and key[1] not in {"recognize"}:
            failures.append("override_not_question:" + ":".join(key))
        if len(words(expected_answer)) < 35:
            failures.append("override_answer_too_thin:" + ":".join(key))

    for item in items:
        prompt = app._adaptive_question(item)
        if any(prompt.startswith(prefix) for prefix in STALE_DAILY_PREFIXES):
            failures.append("stale_category_prompt:" + str(item.get("id")))
        if not prompt.strip():
            failures.append("empty_prompt:" + str(item.get("id")))
        if not str(item.get("answer") or "").strip():
            failures.append("empty_answer:" + str(item.get("id")))

    challenges = {q.get("id"): q for q in data.CLINICAL_CHALLENGES_V119}
    for qid, expected_answer in CURVEBALL_OVERRIDES.items():
        answer = (challenges.get(qid) or {}).get("curveball_answer", "")
        if answer != expected_answer:
            failures.append("curveball_answer:" + qid)
        if len(words(expected_answer)) < 35:
            failures.append("curveball_answer_too_thin:" + qid)

    curveballs = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("curveball")]
    if len(curveballs) != 1597 or any(not str(q.get("curveball_answer") or "").strip() for q in curveballs):
        failures.append(f"curveball_completion:{len(curveballs)}")
    for challenge in curveballs:
        if str(challenge.get("curveball_answer") or "").startswith(STALE_CURVEBALL_PREFIX):
            failures.append("stale_procedural_curveball:" + str(challenge.get("id")))

    blinded = [item for item in items if item.get("blind_reveal")]
    if len(blinded) != 114 or any(not item.get("blind_case_label") for item in blinded):
        failures.append(f"blinded_case_contract:{len(blinded)}")

    for template, label in {
        "daily_adaptive.html": "Reveal answer",
        "clinical_challenge.html": "Reveal curveball answer",
    }.items():
        if label not in (Path("templates") / template).read_text(encoding="utf-8"):
            failures.append("missing_answer_control:" + template)

    print(f"V374_ITEMS|{len(items)}")
    print(f"V374_CONCEPTS|{len(concepts)}")
    print(f"V374_COMPLETE_SIX_STAGE|{sum(count == 6 for count in stage_counts.values())}/{len(stage_counts)}")
    print(f"V374_BLINDED_LABELED|{sum(bool(i.get('blind_case_label')) for i in blinded)}/{len(blinded)}")
    print(f"V374_DAILY_PAIRS_REPAIRED|{len(DAILY_OVERRIDES)}")
    print(f"V374_CURVEBALLS_REPAIRED|{len(CURVEBALL_OVERRIDES)}")
    print(f"V374_CURVEBALLS_WITH_ANSWERS|{sum(bool(q.get('curveball_answer')) for q in curveballs)}/{len(curveballs)}")
    print(f"V374_FAILURES|{len(failures)}")
    for failure in failures[:100]:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: category-literal prompts and the final shared procedural curveball fallback are absent from production")


if __name__ == "__main__":
    main()
