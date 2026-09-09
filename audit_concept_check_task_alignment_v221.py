"""v20.21 exact-live Le Fort / Panfacial Trauma task/source/semantic gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v221 import COHORT, QIDS

SEMANTIC_GROUPS = {
    "airway": ("difficult airway", "front-of-neck", "mobile midface"),
    "nasal_airway_boundary": ("nasotracheal", "skull-base", "blind"),
    "hemorrhage": ("hemorrhage", "embolization", "blindly clamp"),
    "vision": ("orbital compartment syndrome", "afferent pupillary defect", "vision"),
    "skull_base": ("csf", "cribriform", "pneumocephalus"),
    "occlusion": ("preinjury occlusion", "false occlusal platform", "maxillomandibular fixation"),
    "three_dimensional": ("facial width", "height", "projection"),
    "sequence": ("top-down", "bottom-up", "most reliable"),
    "noe": ("medial canthal tendon", "telecanthus"),
    "orbit_framework": ("orbital volume", "zygomatic"),
    "bailout": ("stop or stage", "temporary stabilization", "delayed definitive fixation"),
}
SOURCE_ANCHORS = ("cummings", "pasha", "k.j. lee", "ao surgery reference", "40498582", "40728925", "difficult airway society")

def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    deep_modules = data.DEEP_MODULES_V6
    v6_item_id = data._v6_item_id
    final = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {}) or {}
    by = {str(q.get("id") or ""): q for q in checks or []}
    failures = []
    align = final.get("task_alignment_v221") or {}
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
        if not q.get("task_alignment_v221"): failures.append("missing_marker:" + qid)
        prompt = str(q.get("prompt") or ""); answer = str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split()) < 65: failures.append("prompt_depth:" + qid)
        if len(answer.split()) < 1050: failures.append("answer_depth:" + qid + ":" + str(len(answer.split())))
        if q.get("choices") not in ([], None) or q.get("answer") is not None: failures.append("not_free_response:" + qid)
        for field in ("depth_layers_v221", "common_traps_v221", "deliberate_review_v221", "source_refs_v221", "evidence_distinction_v221"):
            if not q.get(field): failures.append("missing_metadata:" + qid + ":" + field)
        layers = q.get("depth_layers_v221") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(layers.get(layer) or "").strip(): failures.append("missing_depth_layer:" + qid + ":" + layer)
        traps = list(q.get("common_traps_v221") or [])
        if len(traps) < 14 or len({str(x).strip().lower() for x in traps}) < 14: failures.append("trap_depth:" + qid)
        refs = list(q.get("source_refs_v221") or [])
        reftext = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in reftext: failures.append("missing_source:" + qid + ":" + anchor)
        low = answer.lower()
        for group, anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:" + qid + ":" + group)
        evidence = str(q.get("evidence_distinction_v221") or "").lower()
        for anchor in ("durable", "ao surgery reference", "nasotracheal", "skull base", "front-of-neck"):
            if anchor not in evidence: failures.append("evidence_boundary:" + qid + ":" + anchor)
    if set(align.get("repaired") or []) != set(QIDS): failures.append("final_gate_repaired_set")
    print("V221_TARGETS|" + ",".join(QIDS)); print("V221_FAILURES|" + str(len(failures)))
    for failure in failures: print("FAIL|" + failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.21 Le Fort/Panfacial Trauma has exact-live linkage, source traceability, airway/hemorrhage/vision/skull-base rescue, occlusal reconstruction and sequencing/bailout depth")

if __name__ == "__main__": main()
