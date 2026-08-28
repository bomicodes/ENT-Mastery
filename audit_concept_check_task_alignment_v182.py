"""v18.2 hard gate for the third manually repaired Concept Check cohort.

Requires resident-level answer depth plus topic-specific decision content; generic
escalation language cannot satisfy this gate.
"""

import json
import re

import runtime_entry


TASK_TERMS = {
    "cc-v112-rec-head-neck-oncology-floor-of-mouth-scc": ["mandib", "neck", "reconstruct"],
    "cc-v112-rec-laryngology-voice-swallowing-arytenoid-adduction-reinnervation": ["posterior", "vertical", "reinnervation"],
    "cc-v112-mgt-rhinology-allergy-skull-base-frontal-recess-frontal-sinus": ["drainage pathway", "skull", "anterior ethmoid"],
    "cc-v112-rec-head-neck-oncology-glottic-cancer": ["mobility", "subglott", "cartilage"],
    "cc-v112-rec-head-neck-oncology-parapharyngeal-space-tumor": ["prestyloid", "poststyloid", "vascular"],
    "cc-v112-rec-head-neck-oncology-total-laryngectomy": ["stoma", "communication", "fistula"],
    "cc-v112-rec-laryngology-voice-swallowing-vocal-fold-polyp-cyst": ["mucosal wave", "cyst", "scar"],
    "cc-v112-rec-otology-neurotology-ototoxic-noise-induced-hearing-loss": ["baseline", "high frequ", "exposure"],
    "cc-v112-rec-pediatric-otolaryngology-congenital-neck-masses": ["embryolog", "infection", "tract"],
    "cc-v112-rec-pediatric-otolaryngology-pediatric-reflux-eosinophilic-esophagitis": ["solid-food", "atopy", "biopsy"],
}


def words(value):
    return re.findall(r"\b\w+\b", str(value or ""))


def main():
    checks = list(runtime_entry.data.CONCEPT_CHECKS_V112)
    by_id = {str(q.get("id") or ""): q for q in checks}
    runtime_result = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {})
    align_result = runtime_result.get("task_alignment_v182") or {}
    expected = set(TASK_TERMS)
    failures, rows = [], []

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
        lower = answer.lower()
        prompt_wc, answer_wc = len(words(prompt)), len(words(answer))

        if not q.get("task_alignment_v182"):
            fail("missing_task_alignment_marker")
        if prompt_wc < 38 or "?" not in prompt:
            fail(f"weak_prompt:{prompt_wc}")
        if answer_wc < 75:
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

        missing_terms = [term for term in TASK_TERMS[qid] if term not in lower]
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
            "runtime_repaired_set_mismatch=" + ",".join(sorted(expected - repaired))
            + "|extra=" + ",".join(sorted(repaired - expected))
        )

    report = {
        "expected_ids": sorted(expected),
        "runtime_alignment": align_result,
        "failures": failures,
        "items": rows,
    }
    with open("V182_TASK_ALIGNMENT_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"V182_EXPECTED|{len(expected)}")
    print(f"V182_REPAIRED|{len(repaired)}")
    print(f"V182_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
