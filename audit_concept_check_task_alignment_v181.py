"""v18.1 hard gate for the second manually repaired Concept Check cohort.

This gate is intentionally task-specific. It does not accept generic domain-wide
escalation language as evidence of depth: each repaired reveal must contain terms
that demonstrate the decision actually asked by that canonical topic.
"""

import json
import re

import runtime_entry


TASK_TERMS = {
    "cc-v112-rec-rhinology-allergy-skull-base-olfactory-dysfunction": ["conductive", "endoscopy", "imaging"],
    "cc-v112-rec-laryngology-voice-swallowing-vocal-fold-nodules": ["voice therapy", "asymmetry", "mucosal wave"],
    "cc-v112-rec-facial-plastics-trauma-otoplasty": ["antihelical", "conchal", "hematoma"],
    "cc-v112-rec-sleep-surgery-hns-activation-programming": ["threshold", "programming", "hardware"],
    "cc-v112-rec-head-neck-oncology-tep-and-alaryngeal-speech": ["leakage", "prosthesis", "pharyngoesophageal"],
    "cc-v112-mgt-thyroid-parathyroid-salivary-reoperative-hyperparathyroidism": ["biochemical", "localization", "reoperation"],
    "cc-v112-rec-laryngology-voice-swallowing-muscle-tension-dysphonia": ["voice therapy", "compensation", "stroboscopy"],
    "cc-v112-mgt-facial-plastics-trauma-scar-management": ["maturation", "contracture", "revision"],
    "cc-v112-rec-facial-plastics-trauma-local-flap-reconstruction": ["free margins", "tension", "vascular"],
    "cc-v112-rec-rhinology-allergy-skull-base-endoscopic-maxillary-antrostomy": ["natural ostium", "recirculation", "orbit"],
}


def words(value):
    return re.findall(r"\b\w+\b", str(value or ""))


def main():
    checks = list(runtime_entry.data.CONCEPT_CHECKS_V112)
    by_id = {str(q.get("id") or ""): q for q in checks}
    failures = []
    rows = []

    runtime_result = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {})
    align_result = runtime_result.get("task_alignment_v181") or {}
    expected = set(TASK_TERMS)

    if align_result.get("missing"):
        failures.append("runtime_missing=" + ",".join(align_result["missing"]))

    missing = sorted(expected - set(by_id))
    if missing:
        failures.append("missing_ids=" + ",".join(missing))

    for qid in sorted(expected):
        q = by_id.get(qid)
        if not q:
            continue
        item_failures = []

        def fail(reason):
            failures.append(f"{qid}:{reason}")
            item_failures.append(reason)

        prompt = str(q.get("prompt") or "")
        answer = str(q.get("answer_text") or "")
        answer_lower = answer.lower()
        prompt_wc = len(words(prompt))
        answer_wc = len(words(answer))

        if not q.get("task_alignment_v181"):
            fail("missing_task_alignment_marker")
        if prompt_wc < 32 or "?" not in prompt:
            fail(f"weak_prompt:{prompt_wc}")
        if answer_wc < 55:
            fail(f"weak_answer:{answer_wc}")
        if q.get("choices"):
            fail("unexpected_choices")
        if q.get("answer") is not None:
            fail("unexpected_answer_index")
        if not str(q.get("explanation") or "").strip():
            fail("missing_explanation")
        if not str(q.get("board_pearl") or "").strip():
            fail("missing_board_pearl")
        if not q.get("reviewed_all_domains_v178") or not q.get("review_basis_v178"):
            fail("lost_v178_review_metadata")

        missing_terms = [term for term in TASK_TERMS[qid] if term not in answer_lower]
        if missing_terms:
            fail("missing_task_terms:" + ",".join(missing_terms))

        rows.append({
            "id": qid,
            "prompt_words": prompt_wc,
            "answer_words": answer_wc,
            "required_terms": TASK_TERMS[qid],
            "failures": item_failures,
        })

    repaired = set(align_result.get("repaired") or [])
    if repaired != expected:
        failures.append(
            "runtime_repaired_set_mismatch="
            + ",".join(sorted(expected - repaired))
            + "|extra="
            + ",".join(sorted(repaired - expected))
        )

    report = {
        "expected_ids": sorted(expected),
        "runtime_alignment": align_result,
        "failures": failures,
        "items": rows,
    }
    with open("V181_TASK_ALIGNMENT_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"V181_EXPECTED|{len(expected)}")
    print(f"V181_REPAIRED|{len(repaired)}")
    print(f"V181_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
