"""v20.16 exact-live Laryngeal Anatomy sibling task/source/semantic gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v216 import COHORT, QIDS, CID, TOPIC

SEMANTIC_GROUPS = {
    "sole_abductor": ("posterior cricoarytenoid", "only abductor", "airway"),
    "arytenoid_processes": ("vocal process", "muscular process", "lateral"),
    "nerve_territories": ("external branch", "internal branch", "cricothyroid"),
    "vocal_fold_layers": ("superficial lamina propria", "intermediate", "deep lamina propria"),
    "fibroelastic": ("quadrangular membrane", "conus elasticus", "vocal ligament"),
    "deep_spaces": ("preepiglottic", "paraglottic", "subglottic"),
    "fixation_differential": ("cricoarytenoid", "posterior glottic stenosis", "denervation"),
    "rln_variation": ("extralaryngeal branching", "inferior thyroid artery", "nonrecurrent"),
    "bilateral_bailout": ("bilateral", "controlled airway", "irreversible"),
    "nerve_rescue": ("loss of nerve signal", "release traction", "electrode"),
}

def main():
    data=runtime_entry.data; checks=list(data.CONCEPT_CHECKS_V112); deep_modules=data.DEEP_MODULES_V6; v6_item_id=data._v6_item_id
    final=getattr(runtime_entry,"CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179",{}) or {}; by={str(q.get("id") or ""):q for q in checks or []}; failures=[]
    align=final.get("task_alignment_v216") or {}
    if align.get("missing"): failures.append("runtime_missing="+",".join(align["missing"]))
    if align.get("link_mismatch"): failures.append("runtime_link_mismatch="+",".join(align["link_mismatch"]))
    for qid in QIDS:
        q=by.get(qid)
        if q is None: failures.append("missing_target:"+qid); continue
        m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get("topic") or "") if m else ""; cid=v6_item_id(q.get("domain"),topic) if m and q.get("domain") else None
        if topic!=TOPIC or cid!=CID or q.get("concept_id")!=CID: failures.append(f"canonical_link:{qid}:{topic}|{cid}|{q.get('concept_id')}")
        if not q.get("task_alignment_v216"): failures.append("missing_marker:"+qid)
        prompt=str(q.get("prompt") or ""); answer=str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split())<55: failures.append("prompt_depth:"+qid)
        if len(answer.split())<850: failures.append("answer_depth:"+qid)
        if q.get("choices") not in ([],None) or q.get("answer") is not None: failures.append("not_free_response:"+qid)
        for field in ("depth_layers_v216","common_traps_v216","deliberate_review_v216","source_refs_v216","evidence_distinction_v216"):
            if not q.get(field): failures.append("missing_metadata:"+qid+":"+field)
        traps=list(q.get("common_traps_v216") or [])
        if len(traps)<12 or len({str(x).strip().lower() for x in traps})<12: failures.append("trap_depth:"+qid)
        refs=list(q.get("source_refs_v216") or []); reftext=" ".join(str(x.get("citation") or "") for x in refs if isinstance(x,dict)).lower()
        for anchor in ("cummings","pasha","k.j. lee","american head and neck society","international neural monitoring","2026","paraglottic"):
            if anchor not in reftext: failures.append("missing_source:"+qid+":"+anchor)
        low=answer.lower()
        for group,anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:"+qid+":"+group)
    if set(align.get("repaired") or [])!=set(QIDS): failures.append("final_gate_repaired_set:"+repr(sorted(set(align.get("repaired") or []))))
    print("V216_TARGETS|"+",".join(QIDS)); print("V216_FAILURES|"+str(len(failures)))
    for failure in failures: print("FAIL|"+failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.16 Laryngeal Anatomy siblings have exact-live linkage, textbook/current-source traceability, foundation/application/senior depth, individualized traps, airway/nerve rescue and deep-space anatomy")

if __name__=="__main__": main()
