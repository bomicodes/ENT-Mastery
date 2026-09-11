"""v20.25 exact-live Transoral Laser Microsurgery for Laryngeal Cancer task/source/semantic gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v225 import COHORT, QIDS

SEMANTIC_GROUPS = {
    "tool_not_indication": ("laser", "tool", "indication"),
    "selection": ("tumor extent", "exposure", "function"),
    "anterior_commissure": ("anterior commissure", "broyles"),
    "exposure_bailout": ("poor exposure", "abort", "blind"),
    "margins": ("deep margin", "thermal artifact", "universal millimeter"),
    "neck": ("neck management", "primary site", "regional"),
    "function": ("voice", "swallow", "radiation"),
    "fire": ("airway fire", "oxidizer", "remove the burning"),
    "senior_bailout": ("stop", "convert", "another strategy"),
}
SOURCE_ANCHORS = (
    "cummings", "pasha", "k.j. lee", "national cancer institute", "34226992",
    "40400378", "42585753", "36900281", "39403814", "39140205",
    "food and drug administration", "anesthesia patient safety foundation",
)

def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    deep_modules = data.DEEP_MODULES_V6
    v6_item_id = data._v6_item_id
    final = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {}) or {}
    by = {str(q.get("id") or ""): q for q in checks or []}
    failures = []
    align = final.get("task_alignment_v225") or {}
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
        if not q.get("task_alignment_v225"): failures.append("missing_marker:" + qid)
        prompt = str(q.get("prompt") or ""); answer = str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split()) < 70: failures.append("prompt_depth:" + qid)
        if len(answer.split()) < 1300: failures.append("answer_depth:" + qid + ":" + str(len(answer.split())))
        if q.get("choices") not in ([], None) or q.get("answer") is not None: failures.append("not_free_response:" + qid)
        for field in ("depth_layers_v225","common_traps_v225","deliberate_review_v225","source_refs_v225","evidence_distinction_v225"):
            if not q.get(field): failures.append("missing_metadata:" + qid + ":" + field)
        layers = q.get("depth_layers_v225") or {}
        for layer in ("foundation","application","senior_decision"):
            if not str(layers.get(layer) or "").strip(): failures.append("missing_depth_layer:" + qid + ":" + layer)
        traps = list(q.get("common_traps_v225") or [])
        if len(traps) < 18 or len({str(x).strip().lower() for x in traps}) < 18: failures.append("trap_depth:" + qid)
        refs = list(q.get("source_refs_v225") or [])
        reftext = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in reftext: failures.append("missing_source:" + qid + ":" + anchor)
        low = answer.lower()
        for group, anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:" + qid + ":" + group)
        evidence = str(q.get("evidence_distinction_v225") or "").lower()
        for anchor in ("durable", "current", "nci", "els", "fda", "apsf", "universal millimeter"):
            if anchor not in evidence: failures.append("evidence_boundary:" + qid + ":" + anchor)
    if set(align.get("repaired") or []) != set(QIDS): failures.append("final_gate_repaired_set")
    print("V225_TARGETS|" + ",".join(QIDS)); print("V225_FAILURES|" + str(len(failures)))
    for failure in failures: print("FAIL|" + failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.25 TLM laryngeal cancer has exact-live linkage, exposure/margin/neck/function reasoning, current NCI/ELS/FDA/APSF evidence boundaries, individualized traps and explicit airway-fire/exposure bailout logic")

if __name__ == "__main__":
    main()
