"""Targeted v20.9 regression gate for the fourth Rhinology learning-ladder batch.

The clinical content was strong, but the first v20.8 version accidentally placed all
five senior answers in choice B. This gate protects answer-position diversity while
also checking the live runtime linkage and rationale contract.
"""
from collections import Counter

import runtime_entry as rt

PREFIX = "v208_rhi_"
EXPECTED_TOPICS = {
    "Inferior Turbinate Hypertrophy",
    "Nasal Anatomy for Endoscopy",
    "Objective Assessment of Nasal Function",
    "Olfactory Dysfunction",
    "Pediatric Chronic Rhinosinusitis",
}

rows = [q for q in rt.data.CLINICAL_CHALLENGES_V119 if str(q.get("id", "")).startswith(PREFIX)]
failures = []

if len(rows) != 5:
    failures.append(f"expected 5 v208 Rhinology senior rows, found {len(rows)}")

answers = []
seen_topics = set()
for q in rows:
    qid = q.get("id")
    topic = q.get("topic")
    seen_topics.add(topic)
    if q.get("learning_stage") != "senior_decision":
        failures.append(f"{qid}: learning_stage is not senior_decision")
    expected_cid = rt.data._v6_item_id(q.get("domain"), topic)
    if q.get("concept_id") != expected_cid:
        failures.append(f"{qid}: bad canonical concept_id")
    choices = list(q.get("choices") or [])
    reasons = list(q.get("why_wrong") or [])
    try:
        answer = int(q.get("answer"))
    except (TypeError, ValueError):
        failures.append(f"{qid}: invalid answer")
        continue
    answers.append(answer)
    if not 0 <= answer < len(choices):
        failures.append(f"{qid}: answer index out of range")
        continue
    if len(reasons) != len(choices):
        failures.append(f"{qid}: why_wrong length mismatch")
    elif not str(reasons[answer]).strip().lower().startswith("correct."):
        failures.append(f"{qid}: correct-answer rationale is not aligned after choice reorder")

if seen_topics != EXPECTED_TOPICS:
    failures.append(f"topic set mismatch: {sorted(seen_topics)}")

counts = Counter(answers)
if len(counts) < 3:
    failures.append(f"answer positions use only {len(counts)} unique indices: {dict(counts)}")
if counts and max(counts.values()) > 2:
    failures.append(f"one answer position appears >2 times in the five-question batch: {dict(counts)}")

if failures:
    print("RHINOLOGY v20.9 REGRESSION FAILURES")
    print("\n".join(failures))
    raise SystemExit(1)

print(f"PASS: v208 Rhinology senior batch retains canonical linkage and balanced answer positions {dict(sorted(counts.items()))}")
