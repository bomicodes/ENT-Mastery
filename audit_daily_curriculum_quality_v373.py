"""Regression audit for the exact post-v37.3 production registry."""

import re
from pathlib import Path

import runtime_entry_pasha as production
from daily_curriculum_quality_v373 import CURVEBALL_OVERRIDES, DAILY_OVERRIDES


STALE_OPERATIVE_PROMPT = "What is the highest-stakes technical or interpretive failure in"
STALE_CURVEBALL_PHRASES = (
    "State whether a procedure is indicated; if so, rehearse setup",
    "For operative/procedural cases, explicitly state indication",
)


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

    for key, (expected_prompt, expected_answer) in DAILY_OVERRIDES.items():
        item = by_key.get(key) or {}
        if app._adaptive_question(item) != expected_prompt:
            failures.append("daily_prompt:" + ":".join(key))
        if item.get("answer") != expected_answer:
            failures.append("daily_answer:" + ":".join(key))
        if not expected_prompt.endswith("?"):
            failures.append("override_not_question:" + ":".join(key))
        if len(re.findall(r"\b\w+\b", expected_answer)) < 35:
            failures.append("override_answer_too_thin:" + ":".join(key))
        if STALE_OPERATIVE_PROMPT in app._adaptive_question(item):
            failures.append("stale_operate_prompt:" + ":".join(key))

    challenges = {q.get("id"): q for q in data.CLINICAL_CHALLENGES_V119}
    for qid, expected_answer in CURVEBALL_OVERRIDES.items():
        answer = (challenges.get(qid) or {}).get("curveball_answer", "")
        if answer != expected_answer:
            failures.append("curveball_answer:" + qid)
        if len(re.findall(r"\b\w+\b", expected_answer)) < 35:
            failures.append("curveball_answer_too_thin:" + qid)
        if any(phrase in answer for phrase in STALE_CURVEBALL_PHRASES):
            failures.append("stale_curveball_boilerplate:" + qid)

    blinded = [item for item in items if item.get("blind_reveal")]
    if len(blinded) != 114 or any(not item.get("blind_case_label") for item in blinded):
        failures.append(f"blinded_case_contract:{len(blinded)}")

    curveballs = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("curveball")]
    if len(curveballs) != 1597 or any(not str(q.get("curveball_answer") or "").strip() for q in curveballs):
        failures.append(f"curveball_completion:{len(curveballs)}")

    for template, label in {
        "daily_adaptive.html": "Reveal answer",
        "clinical_challenge.html": "Reveal curveball answer",
    }.items():
        if label not in (Path("templates") / template).read_text(encoding="utf-8"):
            failures.append("missing_answer_control:" + template)

    print(f"V373_ITEMS|{len(items)}")
    print(f"V373_CONCEPTS|{len(concepts)}")
    print(f"V373_BLINDED_LABELED|{sum(bool(i.get('blind_case_label')) for i in blinded)}/{len(blinded)}")
    print(f"V373_DAILY_PAIRS_REPAIRED|{len(DAILY_OVERRIDES)}")
    print(f"V373_CURVEBALLS_REPAIRED|{len(CURVEBALL_OVERRIDES)}")
    print(f"V373_CURVEBALLS_WITH_ANSWERS|{sum(bool(q.get('curveball_answer')) for q in curveballs)}/{len(curveballs)}")
    print(f"V373_FAILURES|{len(failures)}")
    for failure in failures[:100]:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: targeted nonoperative prompts and curveballs answer the exact clinical decision asked")


if __name__ == "__main__":
    main()
