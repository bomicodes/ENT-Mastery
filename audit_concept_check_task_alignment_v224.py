"""v20.24 exact-live Intraoperative Nerve Monitoring Parameters task/source/semantic gate."""
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v224 import COHORT, QIDS

SEMANTIC_GROUPS = {
    "adjunct": ("adjunct", "anatomy", "visual"),
    "modalities": ("free-running emg", "triggered stimulation"),
    "anesthesia": ("neuromuscular blockade", "train-of-four", "threshold"),
    "parameters": ("amplitude", "latency", "universal"),
    "warning": ("neurotonic", "stop", "traction"),
    "technical": ("electrodes", "impedance", "probe", "shunt"),
    "localize": ("proximal", "distal", "localize"),
    "rescue": ("release traction", "thermal", "change the surgical"),
}
SOURCE_ANCHORS = (
    "cummings", "pasha", "k.j. lee", "34000898", "41371257", "31521756",
    "42533397", "42520282", "american academy of otolaryngology"
)
RETRACTED_SOURCE = "41353726"


def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    deep_modules = data.DEEP_MODULES_V6
    v6_item_id = data._v6_item_id
    final = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {}) or {}
    by = {str(q.get("id") or ""): q for q in checks or []}
    failures = []
    align = final.get("task_alignment_v224") or {}
    if align.get("missing"): failures.append("runtime_missing=" + ",".join(align["missing"]))
    if align.get("link_mismatch"): failures.append("runtime_link_mismatch=" + ",".join(align["link_mismatch"]))
    for qid in QIDS:
        q = by.get(qid); expected = COHORT.get(qid) or {}
        if q is None: failures.append("missing_target:" + qid); continue
        m = _find_module(q, deep_modules, v6_item_id)
        topic = str(m.get("topic") or "") if m else ""
        cid = v6_item_id(q.get("domain"), topic) if m and q.get("domain") else None
        if topic != expected.get("canonical_topic") or cid != expected.get("concept_id") or q.get("concept_id") != expected.get("concept_id"):
            failures.append("canonical_link:" + qid)
        if not q.get("task_alignment_v224"): failures.append("missing_marker:" + qid)
        prompt = str(q.get("prompt") or ""); answer = str(q.get("answer_text") or "")
        if "?" not in prompt or len(prompt.split()) < 55: failures.append("prompt_depth:" + qid)
        if len(answer.split()) < 850: failures.append("answer_depth:" + qid + ":" + str(len(answer.split())))
        if q.get("choices") not in ([], None) or q.get("answer") is not None: failures.append("not_free_response:" + qid)
        for field in ("depth_layers_v224", "common_traps_v224", "deliberate_review_v224", "source_refs_v224", "evidence_distinction_v224"):
            if not q.get(field): failures.append("missing_metadata:" + qid + ":" + field)
        layers = q.get("depth_layers_v224") or {}
        for layer in ("foundation", "application", "senior_decision"):
            if not str(layers.get(layer) or "").strip(): failures.append("missing_depth_layer:" + qid + ":" + layer)
        traps = list(q.get("common_traps_v224") or [])
        if len(traps) < 15 or len({str(x).strip().lower() for x in traps}) < 15: failures.append("trap_depth:" + qid)
        refs = list(q.get("source_refs_v224") or [])
        reftext = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
        for anchor in SOURCE_ANCHORS:
            if anchor not in reftext: failures.append("missing_source:" + qid + ":" + anchor)
        # Retraction hygiene is fail-closed: PMID 41353726 may appear only to document
        # that it was retracted, with the formal retraction PMID present. It must not
        # appear as an unqualified supporting evidence citation.
        if RETRACTED_SOURCE in reftext and not ("retract" in reftext and "42520282" in reftext):
            failures.append("unbounded_retracted_source:" + qid + ":" + RETRACTED_SOURCE)
        low = answer.lower()
        for group, anchors in SEMANTIC_GROUPS.items():
            if not all(a in low for a in anchors): failures.append("semantic:" + qid + ":" + group)
        if "42533397" not in low: failures.append("missing_current_2026_evidence:" + qid)
        if "retract" not in low or RETRACTED_SOURCE not in low or "42520282" not in low:
            failures.append("missing_retraction_boundary:" + qid)
        evidence = str(q.get("evidence_distinction_v224") or "").lower()
        for anchor in ("durable", "current", "universal", "fda", "42533397", "retract", RETRACTED_SOURCE, "42520282"):
            if anchor not in evidence: failures.append("evidence_boundary:" + qid + ":" + anchor)
    if set(align.get("repaired") or []) != set(QIDS): failures.append("final_gate_repaired_set")
    print("V224_TARGETS|" + ",".join(QIDS)); print("V224_FAILURES|" + str(len(failures)))
    for failure in failures: print("FAIL|" + failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.24 facial nerve monitoring has exact-live linkage, current non-retracted 2026 evidence, explicit retraction hygiene, physiology/anesthesia interpretation, procedure-specific parameter boundaries and stop-troubleshoot-localize-rescue reasoning")


if __name__ == "__main__": main()
