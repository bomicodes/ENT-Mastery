"""v18.0 hard gate for manually repaired Concept Check task/answer alignment."""

import json
import re

import runtime_entry


EXPECTED_IDS = {
    "cc-v112-rec-rhinology-allergy-skull-base-ethmoidectomy",
    "cc-v112-mgt-thyroid-parathyroid-salivary-submandibular-gland-excision",
    "cc-v112-mgt-thyroid-parathyroid-salivary-secondary-tertiary-hyperparathyroidism",
    "cc-v112-rec-head-neck-oncology-hypopharyngeal-cancer",
    "cc-v112-rec-pediatric-otolaryngology-laryngotracheal-reconstruction",
    "cc-v112-rec-sleep-surgery-tongue-base-surgery",
    "cc-v112-rec-general-ent-emergencies-deep-neck-abscess-drainage",
    "cc-v112-rec-laryngology-voice-swallowing-reinke-edema",
    "cc-v112-rec-thyroid-parathyroid-salivary-men2-ret",
    "cc-v112-rec-thyroid-parathyroid-salivary-sialendoscopy",
}

# Broad enough to recognize real resident/chief decisions across ENT without
# counting generic explanatory prose as management content. In particular,
# oncologic extent/margin/nodal/nerve planning is decision content even when an
# answer does not literally contain the word "surgery".
DECISION_WORDS = re.compile(
    r"\b(airway|escalat|surg|operat|drain|source.control|biopsy|malignan|oncolog|"
    r"complication|protect|stage|imaging|monitor|reconstruct|therapy|treatment|"
    r"plan|extent|margin|nodal|nerve|resect|convert|pheochromocytoma|hypocalc|"
    r"csf|orbital|mediastin|multigland)\b",
    re.I,
)


def words(value):
    return re.findall(r"\b\w+\b", str(value or ""))


def main():
    checks = list(runtime_entry.data.CONCEPT_CHECKS_V112)
    by_id = {str(q.get("id") or ""): q for q in checks}
    failures = []
    rows = []

    runtime_result = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {})
    align_result = runtime_result.get("task_alignment_v180") or {}
    if align_result.get("missing"):
        failures.append("runtime_missing=" + ",".join(align_result["missing"]))

    missing = sorted(EXPECTED_IDS - set(by_id))
    if missing:
        failures.append("missing_ids=" + ",".join(missing))

    for qid in sorted(EXPECTED_IDS):
        q = by_id.get(qid)
        if not q:
            continue
        item_failures = []

        def fail(reason):
            failures.append(f"{qid}:{reason}")
            item_failures.append(reason)

        prompt = str(q.get("prompt") or "")
        answer = str(q.get("answer_text") or "")
        if not q.get("task_alignment_v180"):
            fail("missing_task_alignment_marker")
        if len(words(prompt)) < 28 or "?" not in prompt:
            fail(f"weak_prompt:{len(words(prompt))}")
        if len(words(answer)) < 35:
            fail(f"weak_answer:{len(words(answer))}")
        if q.get("choices"):
            fail("unexpected_choices")
        if q.get("answer") is not None:
            fail("unexpected_answer_index")
        if not DECISION_WORDS.search(answer):
            fail("answer_lacks_decision_content")
        if not str(q.get("explanation") or "").strip():
            fail("missing_explanation")
        if not str(q.get("board_pearl") or "").strip():
            fail("missing_board_pearl")

        # Existing all-domain canonical metadata must survive the repair exactly;
        # this gate does not invent or substitute aliases.
        if not q.get("reviewed_all_domains_v178"):
            fail("lost_v178_review_metadata")
        if not q.get("review_basis_v178"):
            fail("lost_review_basis")

        rows.append({
            "id": qid,
            "prompt_words": len(words(prompt)),
            "answer_words": len(words(answer)),
            "decision_content": bool(DECISION_WORDS.search(answer)),
            "task_alignment_v180": bool(q.get("task_alignment_v180")),
            "post_alignment_clinical_frame_v181": bool(q.get("post_alignment_clinical_frame_v181")),
            "failures": item_failures,
        })

    repaired = set(align_result.get("repaired") or [])
    if repaired != EXPECTED_IDS:
        failures.append(
            "runtime_repaired_set_mismatch="
            + ",".join(sorted(EXPECTED_IDS - repaired))
            + "|extra="
            + ",".join(sorted(repaired - EXPECTED_IDS))
        )

    report = {
        "expected_ids": sorted(EXPECTED_IDS),
        "runtime_alignment": align_result,
        "runtime_post_alignment_reframed_v181": runtime_result.get("post_alignment_reframed_v181") or [],
        "failures": failures,
        "items": rows,
    }
    with open("V180_TASK_ALIGNMENT_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"V180_EXPECTED|{len(EXPECTED_IDS)}")
    print(f"V180_REPAIRED|{len(repaired)}")
    print(f"V180_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
