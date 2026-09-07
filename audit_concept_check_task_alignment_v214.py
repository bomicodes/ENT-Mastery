"""v20.14 exact-canonical Central Neck Dissection task/source/semantic gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v214 import COHORT
from concept_check_depth_v214 import QID, CID, TOPIC

SEMANTIC_GROUPS = {
    "indication_boundary": ("therapeutic", "prophylactic", "cn0"),
    "compartment_orientation": ("prelaryngeal", "pretracheal", "paratracheal", "berry picking"),
    "rln_protection": ("recurrent laryngeal", "thermal", "traction"),
    "parathyroid_perfusion": ("parathyroid", "perfusion", "devascularized"),
    "oncologic_nerve_decision": ("gross", "nerve", "oncologic"),
    "revision_bailout": ("revision", "scar", "senior"),
    "contralateral_commitment": ("first-side", "staged", "bilateral"),
    "hematoma_airway_rescue": ("hematoma", "airway", "oxygenation"),
}

def main():
    data=runtime_entry.data; checks=list(data.CONCEPT_CHECKS_V112); deep_modules=data.DEEP_MODULES_V6; v6_item_id=data._v6_item_id
    final=getattr(runtime_entry,"CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179",{}) or {}; by={str(q.get("id") or ""):q for q in checks or []}; failures=[]; q=by.get(QID)
    align=final.get("task_alignment_v214") or {}
    if align.get("missing"): failures.append("runtime_missing="+",".join(align["missing"]))
    if align.get("link_mismatch"): failures.append("runtime_link_mismatch="+",".join(align["link_mismatch"]))
    if q is None: failures.append("missing_target:"+QID)
    else:
        m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get("topic") or "") if m else ""; cid=v6_item_id(q.get("domain"),topic) if m and q.get("domain") else None
        if topic!=TOPIC or cid!=CID or q.get("concept_id")!=CID: failures.append(f"canonical_link:{topic}|{cid}|{q.get('concept_id')}")
        if not q.get("task_alignment_v214"): failures.append("missing_marker:task_alignment_v214")
        prompt=str(q.get("prompt") or ""); answer=str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split())<55: failures.append("prompt_depth")
        if len(answer.split())<650: failures.append("answer_depth")
        if q.get("choices") not in ([],None) or q.get("answer") is not None: failures.append("not_free_response")
        for field in ("depth_layers_v214","common_traps_v214","deliberate_review_v214","source_refs_v214"):
            if not q.get(field): failures.append("missing_metadata:"+field)
        traps=list(q.get("common_traps_v214") or [])
        if len(traps)<10 or len({str(x).strip().lower() for x in traps})<10: failures.append("trap_depth")
        refs=list(q.get("source_refs_v214") or []); reftext=" ".join(str(x.get("citation") or "") for x in refs if isinstance(x,dict)).lower()
        for anchor in ("cummings","pasha","k.j. lee","2025 american thyroid association","american head and neck society","2026"):
            if anchor not in reftext: failures.append("missing_source:"+anchor)
        low=answer.lower()
        for group,anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:"+group)
    if set(align.get("repaired") or [])!={QID}: failures.append("final_gate_repaired_set:"+repr(sorted(set(align.get("repaired") or []))))
    print("V214_TARGET|"+QID); print("V214_FAILURES|"+str(len(failures)))
    for failure in failures: print("FAIL|"+failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.14 Central Neck Dissection has exact-canonical linkage, textbook/current-source traceability, selective indication reasoning, compartment anatomy, RLN/parathyroid protection, and bailout depth")

if __name__=="__main__": main()
