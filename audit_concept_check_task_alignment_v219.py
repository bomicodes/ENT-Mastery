"""v20.19 exact-live Parathyroid Carcinoma task/source/semantic gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v219 import COHORT, QIDS

SEMANTIC_GROUPS = {
    "suspicion": ("marked hypercalcemia", "very high pth", "hoarseness"),
    "biopsy_boundary": ("avoid percutaneous fna", "seeding"),
    "operative_anatomy": ("recurrent laryngeal nerve", "tracheoesophageal groove", "carotid sheath"),
    "oncologic_resection": ("r0 en-bloc", "capsular rupture", "ipsilateral thyroid lobe"),
    "neck_boundary": ("prophylactic central or lateral neck dissection", "therapeutic nodal dissection"),
    "rln_tradeoff": ("functioning", "r0 clearance", "tradeoff"),
    "bailout": ("stop the routine focused-parathyroidectomy script", "defer a planned multidisciplinary operation"),
    "pth_boundary": ("renal dysfunction", "intraoperative pth", "oncologic adequacy"),
    "metabolic_rescue": ("hungry-bone", "calcium", "magnesium"),
    "genetics": ("cdc73", "parafibromin"),
    "adjuvant_boundary": ("routine adjuvant", "evidence", "individualized"),
    "systemic_boundary": ("no universal fda-approved", "molecular profiling"),
}
SOURCE_ANCHORS = ("cummings","pasha","k.j. lee","27532368","38713608","39461777","42580893")

def main():
    data=runtime_entry.data; checks=list(data.CONCEPT_CHECKS_V112); deep_modules=data.DEEP_MODULES_V6; v6_item_id=data._v6_item_id
    final=getattr(runtime_entry,"CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179",{}) or {}; by={str(q.get("id") or ""):q for q in checks or []}; failures=[]
    align=final.get("task_alignment_v219") or {}
    if align.get("missing"): failures.append("runtime_missing="+",".join(align["missing"]))
    if align.get("link_mismatch"): failures.append("runtime_link_mismatch="+",".join(align["link_mismatch"]))
    for qid in QIDS:
        q=by.get(qid); expected=COHORT.get(qid) or {}
        if q is None: failures.append("missing_target:"+qid); continue
        m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get("topic") or "") if m else ""; cid=v6_item_id(q.get("domain"),topic) if m and q.get("domain") else None
        expected_topic=str(expected.get("canonical_topic") or ""); expected_cid=str(expected.get("concept_id") or "")
        if topic!=expected_topic or cid!=expected_cid or q.get("concept_id")!=expected_cid: failures.append(f"canonical_link:{qid}:{topic}|{cid}|{q.get('concept_id')}|expected={expected_topic}|{expected_cid}")
        if not q.get("task_alignment_v219"): failures.append("missing_marker:"+qid)
        prompt=str(q.get("prompt") or ""); answer=str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split())<65: failures.append("prompt_depth:"+qid)
        if len(answer.split())<1100: failures.append("answer_depth:"+qid)
        if q.get("choices") not in ([],None) or q.get("answer") is not None: failures.append("not_free_response:"+qid)
        for field in ("depth_layers_v219","common_traps_v219","deliberate_review_v219","source_refs_v219","evidence_distinction_v219"):
            if not q.get(field): failures.append("missing_metadata:"+qid+":"+field)
        layers=q.get("depth_layers_v219") or {}
        for layer in ("foundation","application","senior_decision"):
            if not str(layers.get(layer) or "").strip(): failures.append("missing_depth_layer:"+qid+":"+layer)
        traps=list(q.get("common_traps_v219") or [])
        if len(traps)<12 or len({str(x).strip().lower() for x in traps})<12: failures.append("trap_depth:"+qid)
        refs=list(q.get("source_refs_v219") or []); reftext=" ".join(str(x.get("citation") or "") for x in refs if isinstance(x,dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in reftext: failures.append("missing_source:"+qid+":"+anchor)
        low=answer.lower()
        for group,anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:"+qid+":"+group)
        evidence=str(q.get("evidence_distinction_v219") or "").lower()
        for anchor in ("durable","aaes","eses","esmo","individualized","fda-approved"):
            if anchor not in evidence: failures.append("evidence_boundary:"+qid+":"+anchor)
    if set(align.get("repaired") or [])!=set(QIDS): failures.append("final_gate_repaired_set:"+repr(sorted(set(align.get("repaired") or []))))
    print("V219_TARGETS|"+",".join(QIDS)); print("V219_FAILURES|"+str(len(failures)))
    for failure in failures: print("FAIL|"+failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.19 Parathyroid Carcinoma has exact-live linkage, core-text/current-source traceability, intact first-operation oncologic depth, RLN/adjacent-organ tradeoffs, metabolic rescue and evidence-bounded recurrent-disease management")

if __name__=="__main__": main()
