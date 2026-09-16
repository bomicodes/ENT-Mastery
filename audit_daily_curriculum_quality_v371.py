"""Regression audit for the exact post-v37.1 production registry."""

from pathlib import Path

import runtime_entry_pasha as production
from daily_curriculum_quality_v371 import (
    CURVEBALL_OVERRIDES,
    DAILY_OVERRIDES,
    RECOGNITION_PROMPTS,
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

    recognize = {item.get("topic"): item for item in items if item.get("stage") == "recognize"}
    for topic, expected_prompt in RECOGNITION_PROMPTS.items():
        item = recognize.get(topic) or {}
        if app._adaptive_question(item) != expected_prompt:
            failures.append("recognition_prompt:" + topic)
        if not item.get("blind_reveal") or not item.get("blind_case_label"):
            failures.append("recognition_blinding:" + topic)

    forbidden_fragments = (
        "This card owns the CLINICAL",
        "The history before reaching for imaging",
        "is concerning, which can be subtle",
        "LYMPHATIC + SWALLOWING cancer phenotype",
    )
    for item in items:
        prompt = app._adaptive_question(item)
        if not prompt.endswith("?"):
            failures.append("not_question:" + str(item.get("id")))
        if any(fragment in prompt for fragment in forbidden_fragments):
            failures.append("curriculum_prose_in_prompt:" + str(item.get("id")))

    challenges = {q.get("id"): q for q in data.CLINICAL_CHALLENGES_V119}
    for qid, expected_answer in CURVEBALL_OVERRIDES.items():
        if (challenges.get(qid) or {}).get("curveball_answer") != expected_answer:
            failures.append("curveball_answer:" + qid)
    curveballs = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("curveball")]
    if any(not str(q.get("curveball_answer") or "").strip() for q in curveballs):
        failures.append("missing_curveball_answers")

    blinded = [item for item in items if item.get("blind_reveal")]
    if any(not item.get("blind_case_label") for item in blinded):
        failures.append("unlabeled_blinded_case")

    answer_controls = {
        "daily_adaptive.html": "Reveal answer",
        "clinical_challenge.html": "Reveal curveball answer",
    }
    for template_name, expected_control in answer_controls.items():
        text = (Path("templates") / template_name).read_text(encoding="utf-8")
        if expected_control not in text:
            failures.append("missing_answer_control:" + template_name)

    print(f"V371_ITEMS|{len(items)}")
    print(f"V371_CONCEPTS|{len(concepts)}")
    print(f"V371_BLINDED_LABELED|{sum(bool(i.get('blind_case_label')) for i in blinded)}/{len(blinded)}")
    print(f"V371_DAILY_PAIRS_REPAIRED|{len(DAILY_OVERRIDES)}")
    print(f"V371_RECOGNITION_STEMS_REPAIRED|{len(RECOGNITION_PROMPTS)}")
    print(f"V371_CURVEBALLS_REPAIRED|{len(CURVEBALL_OVERRIDES)}")
    print(f"V371_CURVEBALLS_WITH_ANSWERS|{sum(bool(q.get('curveball_answer')) for q in curveballs)}/{len(curveballs)}")
    print(f"V371_FAILURES|{len(failures)}")
    for failure in failures[:100]:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: Daily Curriculum prompts answer bounded clinical questions and curveball answers address the escalation actually asked")


if __name__ == "__main__":
    main()
