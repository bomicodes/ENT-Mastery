"""v20.12 hard gate for exact-canonical Tracheomalacia / Bronchomalacia Concept Check depth."""
import re
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v212 import COHORT, QID


def _words(value):
    return len(re.findall(r"\b\w+[\w'-]*\b", str(value or "")))


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    by = {str(q.get("id") or ""): q for q in checks}
    failures = []
    final_gate = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {}) or {}
    align = final_gate.get("task_alignment_v212") or {}
    if align.get("missing"):
        failures.append("runtime_missing=" + ",".join(align["missing"]))
    if align.get("link_mismatch"):
        failures.append("runtime_link_mismatch=" + ",".join(align["link_mismatch"]))

    q = by.get(QID)
    if not q:
        failures.append("missing:" + QID)
    else:
        patch = COHORT[QID]
        module = _find_module(q, data.DEEP_MODULES_V6, data._v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = data._v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != patch["canonical_topic"]:
            failures.append("topic:" + QID)
        if cid != patch["concept_id"] or q.get("concept_id") != cid:
            failures.append("concept_link:" + QID)
        if not q.get("task_alignment_v212"):
            failures.append("marker:" + QID)
        if "?" not in str(q.get("prompt") or "") or _words(q.get("prompt")) < 55:
            failures.append("weak_prompt:" + QID)
        if _words(q.get("answer_text")) < 650:
            failures.append("shallow_answer:" + QID)
        if q.get("choices") or q.get("answer") is not None:
            failures.append("not_free_response:" + QID)
        for field in ("depth_layers_v212", "common_traps_v212", "deliberate_review_v212", "source_refs_v212"):
            if not q.get(field):
                failures.append("missing_" + field + ":" + QID)
        traps = q.get("common_traps_v212") or []
        if len(traps) < 10 or len(set(map(str, traps))) < 10:
            failures.append("traps:" + QID)
        refs = q.get("source_refs_v212") or []
        cites = " ".join(str(x.get("citation") or "") for x in refs if isinstance(x, dict)).lower()
        for required in ("cummings", "pasha", "k.j. lee", "ers statement", "aortopexy", "posterior tracheopexy"):
            if required not in cites:
                failures.append("source_" + required + ":" + QID)

        answer = _norm(q.get("answer_text"))
        semantic_groups = {
            "dynamic_free_breathing": (("free breathing", "free spontaneous breathing", "spontaneous free breathing"), ("positive pressure",), ("stent", "splint")),
            "complete_mapping": (("right",), ("left mainstem", "left mainstem bronchi", "left mainstem bronchomalacia"), ("tracheobronchial tree", "both main bronchi", "mainstem bronchi")),
            "vascular": (("vascular ring", "vascular rings"), ("innominate",), ("compression",)),
            "support": (("cpap",), ("airway clearance", "airway clearance strategies"), ("limited evidence",)),
            "severity": (("cyanotic",), ("failure to extubate", "inability to extubate"), ("recurrent pneumon",)),
            "geometry": (("aortopexy",), ("posterior tracheopexy",), ("posterior membranous",), ("anterior",)),
            "bailout": (("tracheostomy",), ("stent",), ("migration",), ("granulation",)),
            "failure_analysis": (("persistent symptoms",), ("remap", "new dynamic airway map"), ("bronchomalacia",)),
        }
        for label, groups in semantic_groups.items():
            if not all(any(_norm(term) in answer for term in alternatives) for alternatives in groups):
                failures.append("semantic_" + label + ":" + QID)

    repaired = set(align.get("repaired") or [])
    if repaired != {QID}:
        failures.append("runtime_repaired_set_mismatch")
    print("V212_TARGET|" + QID)
    print("V212_FAILURES|" + str(len(failures)))
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: v20.12 Tracheomalacia / Bronchomalacia has exact-canonical linkage, textbook/current-source traceability, dynamic-airway reasoning, anatomy-directed surgery, and rescue depth")


if __name__ == "__main__":
    main()
