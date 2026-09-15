"""Regression audit for the exact post-v37.2 production registry."""

import re
from pathlib import Path

import runtime_entry_pasha as production
from daily_curriculum_quality_v372 import CURVEBALL_OVERRIDES, DAILY_OVERRIDES


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
        if len(re.findall(r"\b\w+\b", expected_answer)) < 30:
            failures.append("override_answer_too_thin:" + ":".join(key))

    challenges = {q.get("id"): q for q in data.CLINICAL_CHALLENGES_V119}
    for qid, expected_answer in CURVEBALL_OVERRIDES.items():
        challenge = challenges.get(qid) or {}
        if challenge.get("curveball_answer") != expected_answer:
            failures.append("curveball_answer:" + qid)
        if len(re.findall(r"\b\w+\b", expected_answer)) < 35:
            failures.append("curveball_answer_too_thin:" + qid)

    generic_curveball_fallbacks = {
        "v146_slp_06": "Targets retroglossal obstruction from lingual tonsil/tongue-base volume or collapse.",
        "v255_lar_tremor_fnd": "Perceptual/laryngoscopic examination across tasks; neurologic evaluation when broader tremor suspected.",
        "v137_tps_06": "Integrate ultrasound phenotype, cytology category, nodule size, clinical risk and test characteristics.",
    }
    for qid, stale_answer in generic_curveball_fallbacks.items():
        if (challenges.get(qid) or {}).get("curveball_answer") == stale_answer:
            failures.append("generic_curveball_fallback_returned:" + qid)

    blinded = [item for item in items if item.get("blind_reveal")]
    if len(blinded) != 114 or any(not item.get("blind_case_label") for item in blinded):
        failures.append(f"blinded_case_contract:{len(blinded)}")

    curveballs = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("curveball")]
    if len(curveballs) != 1597 or any(not str(q.get("curveball_answer") or "").strip() for q in curveballs):
        failures.append(f"curveball_completion:{len(curveballs)}")

    controls = {
        "daily_adaptive.html": "Reveal answer",
        "clinical_challenge.html": "Reveal curveball answer",
    }
    for template, label in controls.items():
        if label not in (Path("templates") / template).read_text(encoding="utf-8"):
            failures.append("missing_answer_control:" + template)

    print(f"V372_ITEMS|{len(items)}")
    print(f"V372_CONCEPTS|{len(concepts)}")
    print(f"V372_BLINDED_LABELED|{sum(bool(i.get('blind_case_label')) for i in blinded)}/{len(blinded)}")
    print(f"V372_DAILY_PAIRS_REPAIRED|{len(DAILY_OVERRIDES)}")
    print(f"V372_CURVEBALLS_REPAIRED|{len(CURVEBALL_OVERRIDES)}")
    print(f"V372_CURVEBALLS_WITH_ANSWERS|{sum(bool(q.get('curveball_answer')) for q in curveballs)}/{len(curveballs)}")
    print(f"V372_FAILURES|{len(failures)}")
    for failure in failures[:100]:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: residual broad Daily prompts now match bounded answers and targeted curveballs answer the exact clinical decision asked")


if __name__ == "__main__":
    main()
