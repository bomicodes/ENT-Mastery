"""v20.29 exact-live Radiation-Associated Dysphagia task/source/semantic gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v229 import COHORT, QIDS

SEMANTIC_GROUPS = {
    "mechanisms": ("fibrosis", "neuropathy", "xerostomia", "stenosis"),
    "danger": ("silent aspiration", "recurrent pneumonias", "weight"),
    "oncology": ("recurrence", "second primary"),
    "instrumentation": ("fees", "modified barium swallow", "mbs"),
    "rehab": ("speech-language pathology", "exercise", "oral intake"),
    "structural": ("dilation", "perforation", "pharyngoesophageal"),
    "ues": ("cricopharyngeal", "poor pharyngeal driving force"),
    "aspiration": ("pulmonary reserve", "oral hygiene", "pneumonia"),
    "senior": ("stabilize aspiration/nutrition risk", "exclude recurrent", "reassess objectively"),
}
SOURCE_ANCHORS = (
    "cummings", "pasha", "k.j. lee", "aa0-hnsf", "american head and neck society",
    "pmid 36965195", "pmid 41340588", "pmid 41348337", "pmid 42636603"
)


def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    deep_modules = data.DEEP_MODULES_V6
    v6_item_id = data._v6_item_id
    final = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {}) or {}
    by = {str(q.get("id") or ""): q for q in checks or []}
    failures = []
    align = final.get("task_alignment_v229") or {}
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
        if not q.get("task_alignment_v229"):
            failures.append("missing_marker:" + qid)

        prompt = str(q.get("prompt") or "")
        answer = str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split()) < 70:
            failures.append("prompt_depth:" + qid + ":" + str(len(prompt.split())))
        if len(answer.split()) < 1100:
            failures.append("answer_depth:" + qid + ":" + str(len(answer.split())))
        if q.get("choices") not in ([], None) or q.get("answer") is not None:
            failures.append("not_free_response:" + qid)

        for field in ("depth_layers_v229", "common_traps_v229", "deliberate_review_v229", "source_refs_v229", "evidence_distinction_v229"):
            if not q.get(field):
                failures.append("missing_metadata:" + qid + ":" + field)
        layers = q.get("depth_layers_v229") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(layers.get(layer) or "").strip():
                failures.append("missing_depth_layer:" + qid + ":" + layer)
        traps = list(q.get("common_traps_v229") or [])
        if len(traps) < 18 or len({str(x).strip().lower() for x in traps}) < 18:
            failures.append("trap_depth:" + qid)

        refs = list(q.get("source_refs_v229") or [])
        reftext = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in reftext:
                failures.append("missing_source:" + qid + ":" + anchor)

        low = answer.lower()
        for group, anchors in SEMANTIC_GROUPS.items():
            if not all(anchor in low for anchor in anchors):
                failures.append("semantic:" + qid + ":" + group)

        evidence = str(q.get("evidence_distinction_v229") or "").lower()
        for anchor in ("durable textbook", "2023 aao-hnsf", "ahns", "2026 systematic review", "support but do not prove", "mechanism-specific"):
            if anchor not in evidence:
                failures.append("evidence_boundary:" + qid + ":" + anchor)

    if set(align.get("repaired") or []) != set(QIDS):
        failures.append("final_gate_repaired_set")

    print("V229_TARGETS|" + ",".join(QIDS))
    print("V229_FAILURES|" + str(len(failures)))
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: v20.29 Radiation-Associated Dysphagia has exact-live linkage, late-radiation mechanism reasoning, recurrence exclusion, instrumental evaluation, rehabilitation, structural escalation and aspiration/nutrition senior decisions")


if __name__ == "__main__":
    main()
