"""v20.6 — all-topic Concept Check teaching-alignment regression gate.

Protects the September 2026 Concept Check cleanup from drifting back toward a
single generic oral-board template. The runtime bank is inspected after every
repair/depth layer has loaded.

Contract:
- every reviewed free-response Concept Check has a real question and reveal;
- topic-titled checks do not ask the learner simply to name the topic;
- non-emergency generated checks may not use the retired generic
  'dangerous alternative / complication must not be missed' wording;
- interpretation, foundation, procedure, emergency, and condition concepts are
  classified with the same helper used by the production curation layer;
- questions deliberately deepened/hand-curated later are preserved and audited
  structurally rather than overwritten.
"""

import json
import re
from collections import Counter

import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_domain_curation_v178 import _concept_kind


data = runtime_entry.data

GENERIC_DANGER_PATTERNS = (
    "dangerous alternative or complication must not be missed",
    "dangerous alternative must not be missed",
    "dangerous complication must not be missed",
)

DIAGNOSIS_ASK_RE = re.compile(
    r"\b(which|what(?: is|\'s)?)\s+(?:the\s+)?(?:most likely\s+)?(?:diagnosis|condition|disorder|disease)\b",
    re.I,
)


def _prompt(q):
    return str(q.get("prompt") or q.get("question") or q.get("stem") or "").strip()


def _answer(q):
    return str(q.get("answer_text") or q.get("model_answer") or q.get("correct_answer") or "").strip()


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def main():
    checks = list(data.CONCEPT_CHECKS_V112)
    failures = []
    failure_details = []
    kinds = Counter()
    reviewed = 0
    free_response = 0
    mcq = 0

    for q in checks:
        qid = str(q.get("id") or "")
        if not qid:
            failures.append("missing_id")
            continue
        if not q.get("reviewed_all_domains_v178"):
            continue
        reviewed += 1

        module = _find_module(q, data.DEEP_MODULES_V6, data._v6_item_id)
        if not module:
            failures.append(f"missing_canonical_module:{qid}")
            continue

        topic = str(q.get("canonical_topic") or q.get("topic") or module.get("topic") or "").strip()
        kind = _concept_kind(topic, module)
        kinds[kind] += 1
        prompt = _prompt(q)

        if q.get("choices"):
            mcq += 1
            continue

        free_response += 1
        answer = _answer(q)
        if not prompt or "?" not in prompt:
            failures.append(f"free_response_without_question:{qid}")
        if not answer:
            failures.append(f"free_response_without_reveal:{qid}")

        nprompt = _norm(prompt)
        ntopic = _norm(topic)
        if ntopic and ntopic in nprompt and DIAGNOSIS_ASK_RE.search(prompt):
            failures.append(f"topic_title_answer_leak:{qid}:{topic}")
            failure_details.append({"id": qid, "failure": "topic_title_answer_leak", "topic": topic, "kind": kind, "prompt": prompt, "answer": answer})

        if kind != "emergency" and any(pat in prompt.lower() for pat in GENERIC_DANGER_PATTERNS):
            failures.append(f"generic_danger_template_nonemergency:{qid}:{kind}:{topic}")
            failure_details.append({"id": qid, "failure": "generic_danger_template_nonemergency", "topic": topic, "kind": kind, "prompt": prompt, "answer": answer})

    report = {
        "audit_version": "v20.6",
        "concept_check_count": len(checks),
        "reviewed_count": reviewed,
        "reviewed_free_response_count": free_response,
        "reviewed_mcq_count": mcq,
        "concept_kind_counts": dict(sorted(kinds.items())),
        "failures": failures,
        "failure_details": failure_details,
    }
    with open("V206_CONCEPT_CHECK_TEACHING_ALIGNMENT_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"V206_REVIEWED|{reviewed}")
    print(f"V206_FREE_RESPONSE|{free_response}")
    print(f"V206_MCQ|{mcq}")
    for kind, count in sorted(kinds.items()):
        print(f"V206_KIND|{kind}|{count}")
    print(f"V206_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    for detail in failure_details:
        print("FAIL_PROMPT|" + detail["id"] + "|" + " ".join(detail["prompt"].split()))
        print("FAIL_ANSWER|" + detail["id"] + "|" + " ".join(detail["answer"].split()))

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
