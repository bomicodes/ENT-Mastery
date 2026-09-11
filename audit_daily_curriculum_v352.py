"""Regression audit for the Daily Path pedagogic redesign.

The audit checks the production runtime, not a parallel fixture, so future deep
curriculum additions are automatically covered.
"""

import re

import wsgi
import data
from app import _adaptive_question


STAGES = {"recognize", "localize", "workup", "manage", "operate", "teach"}
LEGACY_PROMPTS = {
    "Recognize the pattern.",
    "Localize the problem.",
    "Evaluate it efficiently.",
    "Build the management sequence.",
    "Make the advanced decision.",
    "Teach the mental model.",
}


def main():
    items = data.get_adaptive_items_v120()
    failures = []
    by_concept = {}

    for item in items:
        by_concept.setdefault(item.get("concept_id"), []).append(item)
        prompt = _adaptive_question(item)
        topic = item.get("topic") or ""
        answer = item.get("answer") or ""
        if item.get("blind_reveal") or item.get("blind_display_domain"):
            failures.append(f"{item.get('id')}: blind-case metadata remains")
        if not topic or topic.lower() not in prompt.lower():
            failures.append(f"{item.get('id')}: prompt is not topic-grounded")
        if prompt in LEGACY_PROMPTS or len(re.findall(r"\w+", prompt)) < 16:
            failures.append(f"{item.get('id')}: prompt is generic or too shallow")
        if "unidentified case" in prompt.lower():
            failures.append(f"{item.get('id')}: unidentified-case framing leaked")
        if not answer.strip():
            failures.append(f"{item.get('id')}: missing deep-curriculum answer")

    for concept_id, concept_items in by_concept.items():
        stages = {item.get("stage") for item in concept_items}
        if stages != STAGES:
            failures.append(f"{concept_id}: stage coverage is {sorted(stages)}")

    if failures:
        raise SystemExit("FAIL\n" + "\n".join(failures[:100]))

    client = wsgi.app.test_client()
    response = client.get("/daily-adaptive?minutes=15")
    html = response.get_data(as_text=True)
    assert response.status_code == 200, response.status_code
    assert "Unidentified case" not in html
    for label in (
        "Core concept", "Mechanism &amp; anatomy", "Evaluation &amp; evidence",
        "Clinical application", "Senior decisions", "Synthesis &amp; teaching",
    ):
        assert label in html, label

    print(
        f"PASS: {len(items)} Daily Path questions across {len(by_concept)} "
        "canonical topics are deep-curriculum-linked, topic-grounded, fully "
        "staged, and free of blanket unidentified-case framing."
    )


if __name__ == "__main__":
    main()
