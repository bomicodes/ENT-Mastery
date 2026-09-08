"""v20.17 exact-live Sinonasal Malignancy task/source/semantic gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v217 import COHORT, QID, CID, TOPIC

SEMANTIC_GROUPS = {
    "presentation": ("unilateral", "epistaxis", "diplopia"),
    "imaging": ("mri", "ct", "perineural"),
    "orbital_compartments": ("periorbita", "extraconal", "optic nerve"),
    "skull_base": ("cribriform", "dura", "csf leak"),
    "posterior_danger": ("pterygopalatine", "internal-maxillary", "carotid"),
    "margin_approach": ("endoscopic", "open", "margins"),
    "histology": ("snscc", "snuc", "onb"),
    "induction_boundary": ("selective", "induction chemotherapy", "nonrandomized"),
    "orbital_bailout": ("stop blind periorbital", "optic"),
    "skullbase_bailout": ("stop curettage", "controlled dural exposure"),
    "hemorrhage_bailout": ("never chase", "posterior vessel"),
    "regulatory_boundary": ("fda", "not", "sinonasal-specific"),
}

SOURCE_ANCHORS = ("cummings", "pasha", "k.j. lee", "esmo", "euracan", "40611588", "38829173", "fda")

def main():
    data=runtime_entry.data; checks=list(data.CONCEPT_CHECKS_V112); deep_modules=data.DEEP_MODULES_V6; v6_item_id=data._v6_item_id
    final=getattr(runtime_entry,"CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179",{}) or {}; by={str(q.get("id") or ""):q for q in checks or []}; failures=[]; q=by.get(QID)
    align=final.get("task_alignment_v217") or {}
    if align.get("missing"): failures.append("runtime_missing="+",".join(align["missing"]))
    if align.get("link_mismatch"): failures.append("runtime_link_mismatch="+",".join(align["link_mismatch"]))
    if q is None: failures.append("missing_target:"+QID)
    else:
        m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get("topic") or "") if m else ""; cid=v6_item_id(q.get("domain"),topic) if m and q.get("domain") else None
        if topic!=TOPIC or cid!=CID or q.get("concept_id")!=CID: failures.append(f"canonical_link:{topic}|{cid}|{q.get('concept_id')}")
        if not q.get("task_alignment_v217"): failures.append("missing_marker:task_alignment_v217")
        prompt=str(q.get("prompt") or ""); answer=str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split())<55: failures.append("prompt_depth")
        if len(answer.split())<850: failures.append("answer_depth")
        if q.get("choices") not in ([],None) or q.get("answer") is not None: failures.append("not_free_response")
        for field in ("depth_layers_v217","common_traps_v217","deliberate_review_v217","source_refs_v217","evidence_distinction_v217"):
            if not q.get(field): failures.append("missing_metadata:"+field)
        layers=q.get("depth_layers_v217") or {}
        for layer in ("foundation","application","senior_decision"):
            if not str(layers.get(layer) or "").strip(): failures.append("missing_depth_layer:"+layer)
        traps=list(q.get("common_traps_v217") or [])
        if len(traps)<12 or len({str(x).strip().lower() for x in traps})<12: failures.append("trap_depth")
        refs=list(q.get("source_refs_v217") or []); reftext=" ".join(str(x.get("citation") or "") for x in refs if isinstance(x,dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in reftext: failures.append("missing_source:"+anchor)
        low=answer.lower()
        for group,anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:"+group)
        evidence=str(q.get("evidence_distinction_v217") or "").lower()
        for anchor in ("durable", "esmo", "selective", "nonrandomized", "fda", "sinonasal-specific"):
            if anchor not in evidence: failures.append("evidence_boundary:"+anchor)
    if set(align.get("repaired") or [])!={QID}: failures.append("final_gate_repaired_set:"+repr(sorted(set(align.get("repaired") or []))))
    print("V217_TARGET|"+QID); print("V217_FAILURES|"+str(len(failures)))
    for failure in failures: print("FAIL|"+failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.17 Sinonasal Malignancy has exact-live linkage, core-text/current-source traceability, histology-specific management, orbital/skull-base/posterior danger-zone depth, evidence boundaries and explicit rescue/bailout reasoning")

if __name__=="__main__": main()
