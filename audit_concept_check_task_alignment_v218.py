"""v20.18 exact-live task/source/semantic gate for Cranial Nerve Examination / Skull Base Localization."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v218 import COHORT, QIDS

SEMANTIC_GROUPS = {
    "cavernous": ("cavernous", "iii", "vi"),
    "orbital_apex": ("orbital apex", "optic", "vision"),
    "lower_skull_base": ("jugular foramen", "ix", "xii", "collet-sicard"),
    "imaging": ("mri", "ct", "vascular imaging"),
    "bell_boundary": ("bell palsy", "other cranial", "atypical"),
    "functional_rescue": ("cornea", "airway", "swallow", "nutrition"),
    "sbo": ("skull-base osteomyelitis", "otalgia", "cranial neuropath"),
    "vascular_bailout": ("pulsatile", "biopsy", "vascular characterization"),
}
SOURCE_ANCHORS = ("cummings","pasha","k.j. lee","acr","2026","40351881","37142448")

def main():
    data=runtime_entry.data; checks=list(data.CONCEPT_CHECKS_V112); deep_modules=data.DEEP_MODULES_V6; v6_item_id=data._v6_item_id
    final=getattr(runtime_entry,"CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179",{}) or {}; by={str(q.get("id") or ""):q for q in checks or []}; failures=[]
    align=final.get("task_alignment_v218") or {}
    if align.get("missing"): failures.append("runtime_missing="+",".join(align["missing"]))
    if align.get("link_mismatch"): failures.append("runtime_link_mismatch="+",".join(align["link_mismatch"]))
    for qid in QIDS:
        q=by.get(qid); expected=COHORT.get(qid) or {}
        if q is None: failures.append("missing_target:"+qid); continue
        m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get("topic") or "") if m else ""; cid=v6_item_id(q.get("domain"),topic) if m and q.get("domain") else None
        expected_topic=str(expected.get("canonical_topic") or ""); expected_cid=str(expected.get("concept_id") or "")
        if topic!=expected_topic or cid!=expected_cid or q.get("concept_id")!=expected_cid: failures.append(f"canonical_link:{qid}:{topic}|{cid}|{q.get('concept_id')}|expected={expected_topic}|{expected_cid}")
        if not q.get("task_alignment_v218"): failures.append("missing_marker:"+qid)
        prompt=str(q.get("prompt") or ""); answer=str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split())<60: failures.append("prompt_depth:"+qid)
        if len(answer.split())<1200: failures.append("answer_depth:"+qid+":"+str(len(answer.split())))
        if q.get("choices") not in ([],None) or q.get("answer") is not None: failures.append("not_free_response:"+qid)
        for field in ("depth_layers_v218","common_traps_v218","deliberate_review_v218","source_refs_v218","evidence_distinction_v218"):
            if not q.get(field): failures.append("missing_metadata:"+qid+":"+field)
        layers=q.get("depth_layers_v218") or {}
        for layer in ("foundation","application","senior_decision"):
            if not str(layers.get(layer) or "").strip(): failures.append("missing_depth_layer:"+qid+":"+layer)
        traps=list(q.get("common_traps_v218") or [])
        if len(traps)<14 or len({str(x).strip().lower() for x in traps})<14: failures.append("trap_depth:"+qid)
        refs=list(q.get("source_refs_v218") or []); reftext=" ".join(str(x.get("citation") or "") for x in refs if isinstance(x,dict)).lower().replace("-","")
        for anchor in SOURCE_ANCHORS:
            normalized=anchor.lower().replace("-","")
            if normalized not in reftext: failures.append("missing_source:"+qid+":"+anchor)
        low=answer.lower()
        for group,anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:"+qid+":"+group)
        evidence=str(q.get("evidence_distinction_v218") or "").lower()
        for anchor in ("cummings","pasha","k.j. lee","acr","2026","fda","durable"):
            if anchor not in evidence: failures.append("evidence_boundary:"+qid+":"+anchor)
    if set(align.get("repaired") or [])!=set(QIDS): failures.append("final_gate_repaired_set:"+repr(sorted(set(align.get("repaired") or []))))
    print("V218_TARGETS|"+",".join(QIDS)); print("V218_FAILURES|"+str(len(failures)))
    for failure in failures: print("FAIL|"+failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.18 exact-live cranial-nerve/skull-base cohort has canonical linkage, core-text/current-source traceability, foundation/application/senior depth, individualized traps and functional/vascular bailout reasoning")

if __name__=="__main__": main()
