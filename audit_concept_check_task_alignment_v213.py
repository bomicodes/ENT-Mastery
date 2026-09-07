"""v20.13 exact-canonical Submandibular Gland Excision task/source/semantic gate."""
from audit_concept_check_task_alignment_v212 import _runtime
from concept_check_depth_v213 import QID, CID, TOPIC

SEMANTIC_GROUPS = {
    "indication_and_gland_preservation": ("gland preservation", "sialendoscopy", "refractory"),
    "marginal_mandibular_protection": ("marginal mandibular", "superior flap"),
    "lingual_duct_relationship": ("lingual nerve", "wharton duct", "direct"),
    "hypoglossal_protection": ("hypoglossal", "deep"),
    "facial_vessel_control": ("facial", "vessel", "blind clamping"),
    "oncologic_boundary": ("malignancy", "tumor capsule", "oncologic"),
    "scar_bailout": ("scar", "abort", "senior"),
    "hematoma_airway_rescue": ("hematoma", "airway", "oxygenation"),
}

def main():
    checks, deep_modules, v6_item_id, final = _runtime()
    by={str(q.get("id") or ""):q for q in checks or []}; failures=[]; q=by.get(QID)
    if q is None:
        failures.append("missing_target:"+QID)
    else:
        topic=""; cid=None
        try:
            from concept_check_board_repair_v177 import _find_module
            m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get("topic") or "") if m else ""
            cid=v6_item_id(q.get("domain"),topic) if m and q.get("domain") else None
        except Exception as exc: failures.append("resolver_error:"+repr(exc))
        if topic!=TOPIC or cid!=CID or q.get("concept_id")!=CID: failures.append(f"canonical_link:{topic}|{cid}|{q.get('concept_id')}")
        if not q.get("task_alignment_v213"): failures.append("missing_marker:task_alignment_v213")
        prompt=str(q.get("prompt") or ""); answer=str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split()) < 55: failures.append("prompt_depth")
        if len(answer.split()) < 650: failures.append("answer_depth")
        if q.get("choices") not in ([],None) or q.get("answer") is not None: failures.append("not_free_response")
        for field in ("depth_layers_v213","common_traps_v213","deliberate_review_v213","source_refs_v213"):
            if not q.get(field): failures.append("missing_metadata:"+field)
        traps=list(q.get("common_traps_v213") or [])
        if len(traps)<10 or len({str(x).strip().lower() for x in traps})<10: failures.append("trap_depth")
        refs=list(q.get("source_refs_v213") or []); reftext=" ".join(str(x.get("citation") or "") for x in refs).lower()
        for anchor in ("cummings","pasha","k.j. lee","asco","2026"):
            if anchor not in reftext: failures.append("missing_source:"+anchor)
        low=answer.lower()
        for group, anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:"+group)
    repaired=set(((final.get("task_alignment_v213") or {}).get("repaired") or []))
    if repaired!={QID}: failures.append("final_gate_repaired_set:"+repr(sorted(repaired)))
    print("V213_TARGET|"+QID); print("V213_FAILURES|"+str(len(failures)))
    for failure in failures: print("FAIL|"+failure)
    if failures: raise SystemExit(1)

if __name__ == "__main__": main()
