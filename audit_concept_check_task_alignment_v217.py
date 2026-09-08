"""v20.17 exact-live task/source/semantic gate for Endoscopic Maxillary Antrostomy."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v217 import COHORT, QIDS

SEMANTIC_GROUPS = {
    "natural_ostium": ("natural ostium", "infundibulum", "uncinate"),
    "accessory_recirculation": ("accessory ostium", "recirculation", "mucociliary"),
    "visualization": ("angled endoscope", "true ostium", "direct visualization"),
    "orbital_danger": ("direct-lateral", "orbit", "lamina"),
    "revision_failure": ("residual uncinate", "stenosis", "revision"),
    "extent": ("tailor", "mega-antrostomy", "medial maxillectomy"),
    "bailout": ("stop", "remap", "blind instrumentation"),
    "orbital_rescue": ("orbital entry", "vision", "compartment"),
}
SOURCE_ANCHORS = ("cummings","pasha","k.j. lee","2025","aaohnsf","28107148","38566669")

def main():
    data=runtime_entry.data; checks=list(data.CONCEPT_CHECKS_V112); deep_modules=data.DEEP_MODULES_V6; v6_item_id=data._v6_item_id
    final=getattr(runtime_entry,"CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179",{}) or {}; by={str(q.get("id") or ""):q for q in checks or []}; failures=[]
    align=final.get("task_alignment_v217") or {}
    if align.get("missing"): failures.append("runtime_missing="+",".join(align["missing"]))
    if align.get("link_mismatch"): failures.append("runtime_link_mismatch="+",".join(align["link_mismatch"]))
    for qid in QIDS:
        q=by.get(qid); expected=COHORT.get(qid) or {}
        if q is None: failures.append("missing_target:"+qid); continue
        m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get("topic") or "") if m else ""; cid=v6_item_id(q.get("domain"),topic) if m and q.get("domain") else None
        expected_topic=str(expected.get("canonical_topic") or ""); expected_cid=str(expected.get("concept_id") or "")
        if topic!=expected_topic or cid!=expected_cid or q.get("concept_id")!=expected_cid: failures.append(f"canonical_link:{qid}:{topic}|{cid}|{q.get('concept_id')}|expected={expected_topic}|{expected_cid}")
        if not q.get("task_alignment_v217"): failures.append("missing_marker:"+qid)
        prompt=str(q.get("prompt") or ""); answer=str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split())<55: failures.append("prompt_depth:"+qid)
        if len(answer.split())<1000: failures.append("answer_depth:"+qid)
        if q.get("choices") not in ([],None) or q.get("answer") is not None: failures.append("not_free_response:"+qid)
        for field in ("depth_layers_v217","common_traps_v217","deliberate_review_v217","source_refs_v217","evidence_distinction_v217"):
            if not q.get(field): failures.append("missing_metadata:"+qid+":"+field)
        layers=q.get("depth_layers_v217") or {}
        for layer in ("foundation","application","senior_decision"):
            if not str(layers.get(layer) or "").strip(): failures.append("missing_depth_layer:"+qid+":"+layer)
        traps=list(q.get("common_traps_v217") or [])
        if len(traps)<12 or len({str(x).strip().lower() for x in traps})<12: failures.append("trap_depth:"+qid)
        refs=list(q.get("source_refs_v217") or []); reftext=" ".join(str(x.get("citation") or "") for x in refs if isinstance(x,dict)).lower().replace("-","")
        for anchor in SOURCE_ANCHORS:
            normalized=anchor.lower().replace("-","")
            if normalized not in reftext: failures.append("missing_source:"+qid+":"+anchor)
        low=answer.lower()
        for group,anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:"+qid+":"+group)
        evidence=str(q.get("evidence_distinction_v217") or "").lower()
        for anchor in ("cummings","pasha","k.j. lee","2025","individualized","fda"):
            if anchor not in evidence: failures.append("evidence_boundary:"+qid+":"+anchor)
    if set(align.get("repaired") or [])!=set(QIDS): failures.append("final_gate_repaired_set:"+repr(sorted(set(align.get("repaired") or []))))
    print("V217_TARGETS|"+",".join(QIDS)); print("V217_FAILURES|"+str(len(failures)))
    for failure in failures: print("FAIL|"+failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.17 exact-live maxillary-antrostomy cohort has canonical linkage, Cummings/Pasha/K.J. Lee/current-source traceability, foundation/application/senior depth, individualized traps and explicit orbital bailout reasoning")

if __name__=="__main__": main()
