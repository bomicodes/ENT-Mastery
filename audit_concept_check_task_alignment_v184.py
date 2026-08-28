"""v18.4 hard gate for the next live-canonical Concept Check depth cohort."""

import json
import re

import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v184 import COHORT

TASK_TERMS = {
    "cc-v112-rec-facial-plastics-trauma-facial-synkinesis-static-dynamic-rehabilitation": ["synkinesis", "botulinum", "motor endplates", "ocular"],
    "cc-v112-rec-general-ent-emergencies-wound-healing-scar-biology-in-head-neck-surgery": ["fistula", "irradiated", "vascularized", "source control"],
    "cc-v112-mgt-facial-plastics-trauma-forehead-flap-nasal-reconstruction": ["lining", "structural support", "supratrochlear", "venous congestion"],
    "cc-v112-mgt-facial-plastics-trauma-le-fort-panfacial-trauma": ["occlusion", "buttresses", "orbital volume", "reference"],
    "cc-v112-mgt-pediatric-otolaryngology-ankyloglossia-maxillary-frenulum": ["lactation", "function", "shared decision", "salivary ducts"],
    "cc-v112-rec-facial-plastics-trauma-structured-facial-trauma-examination": ["visual acuity", "afferent", "occlusion", "csf"],
    "cc-v112-mgt-facial-plastics-trauma-cervicofacial-flap": ["ectropion", "tension", "radiation", "vascularity"],
    "cc-v112-rec-facial-plastics-trauma-septal-perforation": ["autoimmune", "biopsy", "septal button", "vascularized mucosa"],
    "cc-v112-rec-head-neck-oncology-base-of-tongue-scc": ["hpv", "lingual artery", "margins", "trimodality"],
    "cc-v112-rec-laryngology-voice-swallowing-injection-laryngoplasty": ["paraglottic", "overinjection", "posterior gap", "arytenoid adduction"],
}


def words(value):
    return re.findall(r"\b\w+[\w'-]*\b", str(value or ""))


def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    by_id = {str(q.get("id") or ""): q for q in checks}
    failures, rows = [], []
    expected = set(COHORT)
    runtime_result = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {})
    alignment = runtime_result.get("task_alignment_v184") or {}
    if alignment.get("missing"):
        failures.append("runtime_missing=" + ",".join(alignment["missing"]))
    if alignment.get("link_mismatch"):
        failures.append("runtime_link_mismatch=" + ",".join(alignment["link_mismatch"]))

    for qid in sorted(expected):
        q = by_id.get(qid)
        if not q:
            failures.append(f"{qid}:missing")
            continue
        item_failures = []
        def fail(reason):
            failures.append(f"{qid}:{reason}"); item_failures.append(reason)
        payload = COHORT[qid]
        module = _find_module(q, data.DEEP_MODULES_V6, data._v6_item_id)
        resolved_topic = str(module.get("topic") or "") if module else ""
        resolved_cid = data._v6_item_id(q.get("domain"), resolved_topic) if module and q.get("domain") else None
        if not module: fail("no_live_canonical_module")
        if resolved_topic != payload["canonical_topic"]: fail(f"resolved_topic_mismatch:{resolved_topic!r}")
        if resolved_cid != payload["concept_id"] or q.get("concept_id") != resolved_cid: fail("concept_id_changed_or_unresolved")
        prompt = str(q.get("prompt") or "")
        answer = str(q.get("answer_text") or "")
        answer_lower = answer.lower()
        if not q.get("task_alignment_v184"): fail("missing_v184_marker")
        if len(words(prompt)) < 38 or "?" not in prompt: fail(f"weak_prompt:{len(words(prompt))}")
        if len(words(answer)) < 100: fail(f"weak_answer:{len(words(answer))}")
        if q.get("choices"): fail("unexpected_choices")
        if q.get("answer") is not None: fail("unexpected_answer_index")
        if not q.get("reviewed_all_domains_v178") or not q.get("review_basis_v178"): fail("lost_v178_review_metadata")
        layers = q.get("depth_layers_v184") or {}
        if set(layers) != {"foundation", "application", "senior_decision"}: fail("missing_three_layer_depth")
        traps = q.get("common_traps_v184") or []
        if len(traps) < 2 or any(len(words(x)) < 8 for x in traps): fail("weak_individualized_trap_reasoning")
        if not str(q.get("deliberate_review_v184") or "").strip(): fail("missing_deliberate_review_metadata")
        if not str(q.get("explanation") or "").strip() or not str(q.get("board_pearl") or "").strip(): fail("missing_explanation_or_board_pearl")
        missing_terms = [term for term in TASK_TERMS[qid] if term not in answer_lower]
        if missing_terms: fail("missing_task_terms:" + ",".join(missing_terms))
        rows.append({"id": qid, "concept_id": q.get("concept_id"), "resolved_topic": resolved_topic, "prompt_words": len(words(prompt)), "answer_words": len(words(answer)), "trap_count": len(traps), "failures": item_failures})

    repaired = set(alignment.get("repaired") or [])
    if repaired != expected:
        failures.append("runtime_repaired_set_mismatch=" + ",".join(sorted(expected - repaired)) + "|extra=" + ",".join(sorted(repaired - expected)))
    report = {"expected_ids": sorted(expected), "runtime_alignment": alignment, "failures": failures, "items": rows}
    with open("V184_TASK_ALIGNMENT_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"V184_DEPTH_EXPECTED|{len(expected)}")
    print(f"V184_DEPTH_REPAIRED|{len(repaired)}")
    print(f"V184_DEPTH_FAILURES|{len(failures)}")
    for row in rows:
        print(f"V184_DEPTH_ITEM|{row['id']}|prompt={row['prompt_words']}|answer={row['answer_words']}|traps={row['trap_count']}|topic={row['resolved_topic']}")
    for failure in failures: print("FAIL|" + failure)
    if failures: raise SystemExit(1)

if __name__ == "__main__":
    main()
