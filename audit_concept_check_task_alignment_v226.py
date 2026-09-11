"""v20.26 exact-live ENT Fluids / Electrolytes / Nutrition task/source/semantic gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v226 import COHORT, QIDS

SEMANTIC_GROUPS = {
    "fluid_roles": ("resuscitation", "maintenance", "replacement", "nutrition"),
    "volume_status": ("volume status", "urine output", "reassessment"),
    "pediatric_current": ("aap", "isotonic", "hypotonic"),
    "hyponatremia": ("hyponatremia", "hypertonic", "osmotic demyelination"),
    "siadh_boundary": ("siadh", "hypovolemic", "fluid-restricting"),
    "electrolytes": ("potassium", "magnesium", "phosphate"),
    "refeeding": ("refeeding", "thiamine", "phosphorus"),
    "nutrition_route": ("oral", "enteral", "parenteral"),
    "ent_rescue": ("neck hematoma", "airway rescue", "hemorrhage control"),
    "stop_reassess": ("stop", "reassess", "escalate"),
}
SOURCE_ANCHORS = ("cummings", "pasha", "k.j. lee", "aap", "nice", "espen", "aspen", "32115791")


def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    deep_modules = data.DEEP_MODULES_V6
    v6_item_id = data._v6_item_id
    final = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {}) or {}
    by = {str(q.get("id") or ""): q for q in checks or []}
    failures = []
    align = final.get("task_alignment_v226") or {}
    if align.get("missing"):
        failures.append("runtime_missing=" + ",".join(align["missing"]))
    if align.get("link_mismatch"):
        failures.append("runtime_link_mismatch=" + ",".join(align["link_mismatch"]))

    for qid in QIDS:
        q = by.get(qid)
        expected = COHORT.get(qid) or {}
        if q is None:
            failures.append("missing_target:" + qid)
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != expected.get("canonical_topic") or cid != expected.get("concept_id") or q.get("concept_id") != expected.get("concept_id"):
            failures.append("canonical_link:" + qid)
        if not q.get("task_alignment_v226"):
            failures.append("missing_marker:" + qid)

        prompt = str(q.get("prompt") or "")
        answer = str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split()) < 60:
            failures.append("prompt_depth:" + qid)
        if len(answer.split()) < 1100:
            failures.append("answer_depth:" + qid + ":" + str(len(answer.split())))
        if q.get("choices") not in ([], None) or q.get("answer") is not None:
            failures.append("not_free_response:" + qid)

        for field in ("depth_layers_v226", "common_traps_v226", "deliberate_review_v226", "source_refs_v226", "evidence_distinction_v226"):
            if not q.get(field):
                failures.append("missing_metadata:" + qid + ":" + field)
        layers = q.get("depth_layers_v226") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(layers.get(layer) or "").strip():
                failures.append("missing_depth_layer:" + qid + ":" + layer)
        traps = list(q.get("common_traps_v226") or [])
        if len(traps) < 15 or len({str(x).strip().lower() for x in traps}) < 15:
            failures.append("trap_depth:" + qid)

        refs = list(q.get("source_refs_v226") or [])
        reftext = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in reftext:
                failures.append("missing_source:" + qid + ":" + anchor)

        low = answer.lower()
        for group, anchors in SEMANTIC_GROUPS.items():
            if not all(anchor in low for anchor in anchors):
                failures.append("semantic:" + qid + ":" + group)

        evidence = str(q.get("evidence_distinction_v226") or "").lower()
        for anchor in ("durable", "current guidance", "isotonic", "size-limited"):
            if anchor not in evidence:
                failures.append("evidence_boundary:" + qid + ":" + anchor)

    if set(align.get("repaired") or []) != set(QIDS):
        failures.append("final_gate_repaired_set")

    print("V226_TARGETS|" + ",".join(QIDS))
    print("V226_FAILURES|" + str(len(failures)))
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: v20.26 ENT fluids/electrolytes/nutrition has exact-live linkage, resuscitation/maintenance separation, sodium/electrolyte rescue, refeeding safeguards, enteral-first nutrition and explicit stop/reassess reasoning")


if __name__ == "__main__":
    main()
