"""v19.6 hard gate for clinically specific PAP troubleshooting decisions."""
import json, re
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v196 import COHORT

TASK_TERMS = {
    "cc-v112-rec-sleep-surgery-pap-troubleshooting": [
        "large leak", "residual event", "nasal obstruction", "heated humidification",
        "aerophagia", "central apneas", "hypoventilation", "sleep medicine",
        "objective reassessment", "pap intolerance"
    ],
}

def words(v): return re.findall(r"\b\w+[\w'-]*\b", str(v or ""))
def sem(v):
    s = str(v or "").lower(); s = re.sub(r"[-–—/]", " ", s)
    return re.sub(r"\s+", " ", s).strip()

def main():
    d = runtime_entry.data
    checks = list(d.CONCEPT_CHECKS_V112)
    by = {str(q.get("id") or ""): q for q in checks}
    failures, rows = [], []
    expected = set(COHORT)
    rr = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {})
    align = rr.get("task_alignment_v196") or {}
    if align.get("missing"): failures.append("runtime_missing=" + ",".join(align["missing"]))
    if align.get("link_mismatch"): failures.append("runtime_link_mismatch=" + ",".join(align["link_mismatch"]))
    for qid in sorted(expected):
        q = by.get(qid)
        if not q:
            failures.append(qid + ":missing"); continue
        local = []
        def fail(x): failures.append(qid + ":" + x); local.append(x)
        p = COHORT[qid]
        m = _find_module(q, d.DEEP_MODULES_V6, d._v6_item_id)
        topic = str(m.get("topic") or "") if m else ""
        cid = d._v6_item_id(q.get("domain"), topic) if m and q.get("domain") else None
        if not m: fail("no_live_canonical_module")
        if topic != p["canonical_topic"]: fail("resolved_topic_mismatch:" + repr(topic))
        if cid != p["concept_id"] or q.get("concept_id") != cid: fail("concept_id_changed_or_unresolved")
        prompt = str(q.get("prompt") or ""); ans = str(q.get("answer_text") or ""); text = sem(ans)
        if not q.get("task_alignment_v196"): fail("missing_v196_marker")
        if len(words(prompt)) < 55 or "?" not in prompt: fail("weak_prompt:" + str(len(words(prompt))))
        if len(words(ans)) < 350: fail("weak_answer:" + str(len(words(ans))))
        if q.get("choices") or q.get("answer") is not None: fail("not_free_response")
        if not q.get("reviewed_all_domains_v178") or not q.get("review_basis_v178"): fail("lost_v178_review_metadata")
        if set(q.get("depth_layers_v196") or {}) != {"foundation", "application", "senior_decision"}: fail("missing_three_layer_depth")
        traps = q.get("common_traps_v196") or []
        if len(traps) < 3 or any(len(words(x)) < 25 for x in traps): fail("weak_individualized_trap_reasoning")
        if not str(q.get("deliberate_review_v196") or "").strip(): fail("missing_deliberate_review_metadata")
        miss = [t for t in TASK_TERMS[qid] if sem(t) not in text]
        if miss: fail("missing_task_terms:" + ",".join(miss))
        # Decision-boundary checks: the answer must explicitly reject two dangerous shortcuts.
        if "do not keep raising pressure" not in text: fail("missing_central_event_pressure_stop_rule")
        if "should not be presented as automatically curing osa" not in text: fail("missing_nasal_surgery_non_cure_boundary")
        if "pap intolerance is not itself an anatomic diagnosis" not in text: fail("missing_surgery_selection_boundary")
        rows.append({"id": qid, "concept_id": q.get("concept_id"), "resolved_topic": topic,
                     "prompt_words": len(words(prompt)), "answer_words": len(words(ans)),
                     "trap_count": len(traps), "failures": local})
    repaired = set(align.get("repaired") or [])
    if repaired != expected:
        failures.append("runtime_repaired_set_mismatch=" + ",".join(sorted(expected - repaired)) + "|extra=" + ",".join(sorted(repaired - expected)))
    with open("V196_TASK_ALIGNMENT_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump({"expected_ids": sorted(expected), "runtime_alignment": align, "failures": failures, "items": rows}, f, indent=2, ensure_ascii=False)
    print(f"V196_EXPECTED|{len(expected)}"); print(f"V196_REPAIRED|{len(repaired)}"); print(f"V196_FAILURES|{len(failures)}")
    for r in rows: print("V196_DEPTH_ITEM|{id}|prompt={prompt_words}|answer={answer_words}|traps={trap_count}|topic={resolved_topic}".format(**r))
    for x in failures: print("FAIL|" + x)
    if failures: raise SystemExit(1)

if __name__ == "__main__": main()
