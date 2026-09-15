"""Regression audit for the exact post-v37.0 production registry."""

import re

import runtime_entry_pasha as production
from daily_curriculum_quality_v370 import (
    CASE_LABEL_OVERRIDES,
    CURVEBALL_OVERRIDES,
    DAILY_OVERRIDES,
    NAMED_RECOGNITION_TOPICS,
    PROMPT_ONLY_OVERRIDES,
)


def main():
    data = production.runtime_entry.data
    app = production.runtime_entry.app_mod
    items = data.get_adaptive_items_v120()
    failures = []

    by_id = {item.get("id"): item for item in items}
    by_key = {(item.get("topic"), item.get("stage")): item for item in items}
    concepts = {item.get("concept_id") for item in items}
    expected = sum(len(modules) for modules in data.DEEP_MODULES_V6.values()) * 6
    if len(items) != expected or len(by_id) != expected:
        failures.append(f"registry_shape:{len(items)}:{len(by_id)}:{expected}")

    for key, (expected_prompt, expected_answer) in DAILY_OVERRIDES.items():
        item = by_key.get(key) or {}
        if app._adaptive_question(item) != expected_prompt:
            failures.append("daily_prompt_override:" + ":".join(key))
        if item.get("answer") != expected_answer:
            failures.append("daily_answer_override:" + ":".join(key))
        if key[1] == "recognize" and item.get("blind_reveal"):
            failures.append("curated_comparison_still_blinded:" + key[0])

    for key, expected_prompt in PROMPT_ONLY_OVERRIDES.items():
        item = by_key.get(key) or {}
        if app._adaptive_question(item) != expected_prompt:
            failures.append("prompt_only_override:" + ":".join(key))

    recognize = {
        item.get("topic"): item for item in items if item.get("stage") == "recognize"
    }
    for topic in NAMED_RECOGNITION_TOPICS:
        item = recognize.get(topic) or {}
        if item.get("blind_reveal"):
            failures.append("alias_reveal_still_blinded:" + topic)
        if topic not in app._adaptive_question(item):
            failures.append("named_recognition_missing_topic:" + topic)

    for topic, expected_label in CASE_LABEL_OVERRIDES.items():
        item = recognize.get(topic) or {}
        # Some topics are intentionally converted to named recognition cards.
        if item.get("blind_reveal") and item.get("blind_case_label") != expected_label:
            failures.append(f"case_label:{topic}:{item.get('blind_case_label')}")

    bad_fragments = (" H. What is", " ne. What is")
    for item in items:
        prompt = app._adaptive_question(item)
        if not prompt or not prompt.endswith("?"):
            failures.append("not_question:" + str(item.get("id")))
        if any(fragment in prompt for fragment in bad_fragments):
            failures.append("midword_truncation:" + str(item.get("id")))
        if re.search(r"\b(?:ne|negl|respon|approp)\. What is the most likely diagnosis\?", prompt):
            failures.append("probable_midword_truncation:" + str(item.get("id")))

    challenges = {q.get("id"): q for q in data.CLINICAL_CHALLENGES_V119}
    for qid, expected_answer in CURVEBALL_OVERRIDES.items():
        if (challenges.get(qid) or {}).get("curveball_answer") != expected_answer:
            failures.append("curveball_override:" + qid)

    curveballs = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("curveball")]
    missing_answers = [q.get("id") for q in curveballs if not str(q.get("curveball_answer") or "").strip()]
    failures.extend("missing_curveball_answer:" + str(qid) for qid in missing_answers)

    blinded = [item for item in items if item.get("blind_reveal")]
    print(f"V370_ITEMS|{len(items)}")
    print(f"V370_CONCEPTS|{len(concepts)}")
    print(f"V370_BLINDED_CASES|{len(blinded)}")
    print(f"V370_BLINDED_LABELED|{sum(bool(item.get('blind_case_label')) for item in blinded)}/{len(blinded)}")
    print(f"V370_CURVEBALLS_WITH_ANSWERS|{sum(bool(q.get('curveball_answer')) for q in curveballs)}/{len(curveballs)}")
    print(f"V370_TARGETED_CURVEBALL_REPAIRS|{len(CURVEBALL_OVERRIDES)}")
    print(f"V370_FAILURES|{len(failures)}")
    for failure in failures[:100]:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: rendered Daily Curriculum has diagnosis-honest cards, presentation-aligned labels, complete stems, nonliteral advanced questions, and targeted curveball answers")


if __name__ == "__main__":
    main()
