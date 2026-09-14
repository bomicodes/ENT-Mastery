"""v20.32 exact-live Cleft / Craniofacial Otologic-Airway Care depth/source gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v232 import COHORT, QIDS

REQUIRED = (
    "longitudinal airway-hearing-speech", "eustachian-tube", "developmental vital sign",
    "universal prophylactic tubes", "tensor veli palatini tenopexy", "robin-sequence",
    "superior-partial", "velopharynx", "pharyngeal flap", "rescue airway plan",
)
SOURCE_ANCHORS = (
    "cummings", "pasha", "k.j. lee", "acpa", "rosenfeld", "pmid 41930721",
    "pmid 42213516", "pmid 42266256", "pmid 42298364", "pmid 42536027",
)


def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    deep_modules = data.DEEP_MODULES_V6
    v6_item_id = data._v6_item_id
    final = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {}) or {}
    by = {str(q.get("id") or ""): q for q in checks or []}
    failures = []
    align = final.get("task_alignment_v232") or {}
    if align.get("missing"):
        failures.append("runtime_missing=" + ",".join(align["missing"]))
    if align.get("link_mismatch"):
        failures.append("runtime_link_mismatch=" + ",".join(align["link_mismatch"]))

    for qid in QIDS:
        q = by.get(qid)
        expected = COHORT[qid]
        if q is None:
            failures.append("missing_target:" + qid)
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != expected["canonical_topic"] or cid != expected["concept_id"] or q.get("concept_id") != expected["concept_id"]:
            failures.append("canonical_link:" + qid)
        if not q.get("task_alignment_v232"):
            failures.append("missing_marker:" + qid)

        answer = str(q.get("answer_text") or "").lower()
        if len(answer.split()) < 650:
            failures.append("depth_words:" + qid + ":" + str(len(answer.split())))
        for anchor in REQUIRED:
            if anchor not in answer:
                failures.append("semantic:" + qid + ":" + anchor)
        for field in ("depth_layers_v232", "common_traps_v232", "deliberate_review_v232", "source_refs_v232", "evidence_distinction_v232"):
            if not q.get(field):
                failures.append("missing_metadata:" + qid + ":" + field)
        layers = q.get("depth_layers_v232") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(layers.get(layer) or "").strip():
                failures.append("missing_layer:" + qid + ":" + layer)
        traps = list(q.get("common_traps_v232") or [])
        if len(traps) < 20 or len({str(x).strip().lower() for x in traps}) < 20:
            failures.append("trap_depth:" + qid)
        refs = list(q.get("source_refs_v232") or [])
        reftext = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in reftext:
                failures.append("missing_source:" + qid + ":" + anchor)
        evidence = str(q.get("evidence_distinction_v232") or "").lower()
        for anchor in ("durable textbook", "universal prophylactic", "tensor-tenopexy", "phenotype-based"):
            if anchor not in evidence:
                failures.append("evidence_boundary:" + qid + ":" + anchor)

    if set(align.get("repaired") or []) != set(QIDS):
        failures.append("final_gate_repaired_set")
    print("V232_TARGETS|" + ",".join(QIDS))
    print("V232_FAILURES|" + str(len(failures)))
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: v20.32 preserves exact-live linkage while deepening cleft craniofacial hearing-airway-VPI decision making with traceable sources")


if __name__ == "__main__":
    main()
