"""v20.23 exact-live Forehead Flap / Nasal Reconstruction task/source/semantic gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v223 import COHORT, QIDS

SEMANTIC_GROUPS = {
    "layers": ("lining", "structural support", "cover"),
    "pedicle": ("supratrochlear", "kink", "torsion", "compression"),
    "staging": ("two-stage", "three-stage", "intermediate"),
    "division": ("3 to 4 weeks", "selected", "perfusion", "calendar"),
    "function": ("external valve", "alar", "airway"),
    "arterial": ("pale", "arterial inflow"),
    "venous": ("dusky", "venous outflow"),
    "rescue": ("release", "hematoma", "operative reassessment"),
    "evidence_boundary": ("no fda indication", "no major society guideline", "observational"),
}
SOURCE_ANCHORS = ("cummings", "pasha", "k.j. lee", "39697410", "39871421", "40062609", "38575283")

def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    deep_modules = data.DEEP_MODULES_V6
    v6_item_id = data._v6_item_id
    final = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {}) or {}
    by = {str(q.get("id") or ""): q for q in checks or []}
    failures = []
    align = final.get("task_alignment_v223") or {}
    if align.get("missing"): failures.append("runtime_missing=" + ",".join(align["missing"]))
    if align.get("link_mismatch"): failures.append("runtime_link_mismatch=" + ",".join(align["link_mismatch"]))
    for qid in QIDS:
        q = by.get(qid); expected = COHORT.get(qid) or {}
        if q is None: failures.append("missing_target:" + qid); continue
        m = _find_module(q, deep_modules, v6_item_id)
        topic = str(m.get("topic") or "") if m else ""
        cid = v6_item_id(q.get("domain"), topic) if m and q.get("domain") else None
        if topic != expected.get("canonical_topic") or cid != expected.get("concept_id") or q.get("concept_id") != expected.get("concept_id"):
            failures.append("canonical_link:" + qid)
        if not q.get("task_alignment_v223"): failures.append("missing_marker:" + qid)
        prompt = str(q.get("prompt") or ""); answer = str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split()) < 65: failures.append("prompt_depth:" + qid)
        if len(answer.split()) < 1100: failures.append("answer_depth:" + qid + ":" + str(len(answer.split())))
        if q.get("choices") not in ([], None) or q.get("answer") is not None: failures.append("not_free_response:" + qid)
        for field in ("depth_layers_v223", "common_traps_v223", "deliberate_review_v223", "source_refs_v223", "evidence_distinction_v223"):
            if not q.get(field): failures.append("missing_metadata:" + qid + ":" + field)
        layers = q.get("depth_layers_v223") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(layers.get(layer) or "").strip(): failures.append("missing_depth_layer:" + qid + ":" + layer)
        traps = list(q.get("common_traps_v223") or [])
        if len(traps) < 15 or len({str(x).strip().lower() for x in traps}) < 15: failures.append("trap_depth:" + qid)
        refs = list(q.get("source_refs_v223") or [])
        reftext = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in reftext: failures.append("missing_source:" + qid + ":" + anchor)
        low = answer.lower()
        for group, anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:" + qid + ":" + group)
        evidence = str(q.get("evidence_distinction_v223") or "").lower()
        for anchor in ("durable", "traditional", "selected", "no fda indication", "no major society guideline"):
            if anchor not in evidence: failures.append("evidence_boundary:" + qid + ":" + anchor)
    if set(align.get("repaired") or []) != set(QIDS): failures.append("final_gate_repaired_set")
    print("V223_TARGETS|" + ",".join(QIDS)); print("V223_FAILURES|" + str(len(failures)))
    for failure in failures: print("FAIL|" + failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.23 Forehead Flap / Nasal Reconstruction has exact-live linkage, layered reconstruction, supratrochlear staging, perfusion-based division and immediate vascular rescue reasoning")

if __name__ == "__main__": main()
