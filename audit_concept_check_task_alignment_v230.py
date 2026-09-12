"""v20.30 exact-live Sinonasal Malignancy / ONB management and learner-discoverability gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v230 import COHORT, QIDS

REQUIRED_ONB = (
    "esthesioneuroblastoma", "olfactory neuroblastoma", "hyams", "kadish",
    "surgical resection", "adjuvant radiotherapy", "hyams iii-iv",
    "induction chemotherapy", "node-positive", "cn0", "elective neck irradiation",
    "20 years", "late", "surveillance",
)
SOURCE_ANCHORS = (
    "cummings", "pasha", "k.j. lee", "esmo", "refcor",
    "pmid 42442982", "pmid 39986703", "pmid 38762332", "pmid 34254061",
)


def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    deep_modules = data.DEEP_MODULES_V6
    v6_item_id = data._v6_item_id
    final = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {}) or {}
    by = {str(q.get("id") or ""): q for q in checks or []}
    failures = []
    align = final.get("task_alignment_v230") or {}
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
        if not q.get("task_alignment_v230"):
            failures.append("missing_marker:" + qid)

        answer = str(q.get("answer_text") or "")
        low = answer.lower()
        marker = "### esthesioneuroblastoma (olfactory neuroblastoma; onb) — management pathway"
        if marker not in low:
            failures.append("learner_discoverability_heading:" + qid)
        section = low.split(marker, 1)[1] if marker in low else ""
        if len(section.split()) < 500:
            failures.append("onb_management_depth:" + qid + ":" + str(len(section.split())))
        for anchor in REQUIRED_ONB:
            if anchor not in section:
                failures.append("onb_semantic:" + qid + ":" + anchor)

        meta = q.get("learner_experience_v230") or {}
        aliases = {str(x).lower() for x in meta.get("search_aliases") or []}
        for alias in ("esthesioneuroblastoma", "olfactory neuroblastoma", "onb", "esthesioblastoma"):
            if alias not in aliases:
                failures.append("missing_search_alias:" + qid + ":" + alias)
        for field in ("depth_layers_v230", "common_traps_v230", "deliberate_review_v230", "source_refs_v230", "evidence_distinction_v230"):
            if not q.get(field):
                failures.append("missing_metadata:" + qid + ":" + field)
        traps = list(q.get("common_traps_v230") or [])
        if len(traps) < 12 or len({str(x).strip().lower() for x in traps}) < 12:
            failures.append("trap_depth:" + qid)
        refs = list(q.get("source_refs_v230") or [])
        reftext = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in reftext:
                failures.append("missing_source:" + qid + ":" + anchor)
        evidence = str(q.get("evidence_distinction_v230") or "").lower()
        for anchor in ("durable textbook", "2025 esmo", "2026 refcor", "cn0", "decades"):
            if anchor not in evidence:
                failures.append("evidence_boundary:" + qid + ":" + anchor)

    if set(align.get("repaired") or []) != set(QIDS):
        failures.append("final_gate_repaired_set")
    print("V230_TARGETS|" + ",".join(QIDS))
    print("V230_FAILURES|" + str(len(failures)))
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: v20.30 makes ONB/esthesioneuroblastoma management explicit, searchable and clinically actionable inside the exact-live Sinonasal Malignancy pathway")


if __name__ == "__main__":
    main()
