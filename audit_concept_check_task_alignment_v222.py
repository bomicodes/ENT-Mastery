"""v20.22 exact-live Pediatric Lymphatic Malformation task/source/semantic gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v222 import COHORT, QIDS

SEMANTIC_GROUPS = {
    "airway": ("airway", "stridor", "surgical airway"),
    "flare": ("infection", "intralesional hemorrhage", "inflammatory"),
    "morphology": ("macrocystic", "microcystic", "mixed"),
    "sclerotherapy": ("sclerotherapy", "post-sclerotherapy", "edema"),
    "surgery_bailout": ("subtotal", "debulking", "stop"),
    "pi3k": ("pik3ca", "alpelisib", "pros"),
    "regulatory_boundary": ("not the same statement", "all lymphatic malformations", "age 2 years"),
    "systemic": ("sirolimus", "off-label", "monitoring"),
    "outcomes": ("breathing", "swallowing", "speech"),
}
SOURCE_ANCHORS = ("cummings", "pasha", "k.j. lee", "issva", "fda", "36066547", "38951201", "37115326")

def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    deep_modules = data.DEEP_MODULES_V6
    v6_item_id = data._v6_item_id
    final = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {}) or {}
    by = {str(q.get("id") or ""): q for q in checks or []}
    failures = []
    align = final.get("task_alignment_v222") or {}
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
        if not q.get("task_alignment_v222"): failures.append("missing_marker:" + qid)
        prompt = str(q.get("prompt") or ""); answer = str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split()) < 65: failures.append("prompt_depth:" + qid)
        if len(answer.split()) < 950: failures.append("answer_depth:" + qid + ":" + str(len(answer.split())))
        if q.get("choices") not in ([], None) or q.get("answer") is not None: failures.append("not_free_response:" + qid)
        for field in ("depth_layers_v222", "common_traps_v222", "deliberate_review_v222", "source_refs_v222", "evidence_distinction_v222"):
            if not q.get(field): failures.append("missing_metadata:" + qid + ":" + field)
        layers = q.get("depth_layers_v222") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(layers.get(layer) or "").strip(): failures.append("missing_depth_layer:" + qid + ":" + layer)
        traps = list(q.get("common_traps_v222") or [])
        if len(traps) < 14 or len({str(x).strip().lower() for x in traps}) < 14: failures.append("trap_depth:" + qid)
        refs = list(q.get("source_refs_v222") or [])
        reftext = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in reftext: failures.append("missing_source:" + qid + ":" + anchor)
        low = answer.lower()
        for group, anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:" + qid + ":" + group)
        evidence = str(q.get("evidence_distinction_v222") or "").lower()
        for anchor in ("durable", "issva 2025", "off-label", "fda", "not generically"):
            if anchor not in evidence: failures.append("evidence_boundary:" + qid + ":" + anchor)
    if set(align.get("repaired") or []) != set(QIDS): failures.append("final_gate_repaired_set")
    print("V222_TARGETS|" + ",".join(QIDS)); print("V222_FAILURES|" + str(len(failures)))
    for failure in failures: print("FAIL|" + failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.22 Pediatric Lymphatic Malformation has exact-live linkage, airway/flare rescue, morphology-specific treatment, function-preserving bailout and precise PIK3CA/alpelisib regulatory boundaries")

if __name__ == "__main__": main()
