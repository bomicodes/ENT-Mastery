"""v19.8 hard gate for pediatric airway foreign-body diagnosis, OR planning, and rescue."""
import json
import re
import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v198 import COHORT

QID = "cc-v112-rec-pediatric-otolaryngology-pediatric-airway-foreign-body"
TERM_GROUPS = {
    "normal_imaging_boundary": ("normal chest radiograph", "does not exclude aspiration"),
    "definitive_platform": ("rigid bronchoscopy", "ventilating airway"),
    "ventilation_planning": ("spontaneous or controlled ventilation", "surgeon and anesthesiologist"),
    "migration_rescue": ("complete tracheal obstruction", "mainstem bronchus", "contralateral-lung ventilation"),
    "post_removal_reinspection": ("both bronchial trees", "retained fragments"),
    "senior_stop_rule": ("oxygenation first", "stop repetitive extraction attempts"),
}


def words(v):
    return re.findall(r"\b\w+[\w'-]*\b", str(v or ""))


def sem(v):
    s = str(v or "").lower()
    s = re.sub(r"[-–—/]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    d = runtime_entry.data
    checks = list(d.CONCEPT_CHECKS_V112)
    by = {str(q.get("id") or ""): q for q in checks}
    failures, rows = [], []
    expected = set(COHORT)
    rr = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {})
    align = rr.get("task_alignment_v198") or {}
    if align.get("missing"):
        failures.append("runtime_missing=" + ",".join(align["missing"]))
    if align.get("link_mismatch"):
        failures.append("runtime_link_mismatch=" + ",".join(align["link_mismatch"]))

    for qid in sorted(expected):
        q = by.get(qid)
        if not q:
            failures.append(qid + ":missing")
            continue
        local = []

        def fail(x):
            failures.append(qid + ":" + x)
            local.append(x)

        p = COHORT[qid]
        m = _find_module(q, d.DEEP_MODULES_V6, d._v6_item_id)
        topic = str(m.get("topic") or "") if m else ""
        cid = d._v6_item_id(q.get("domain"), topic) if m and q.get("domain") else None
        if not m:
            fail("no_live_canonical_module")
        if topic != p["canonical_topic"]:
            fail("resolved_topic_mismatch:" + repr(topic))
        if cid != p["concept_id"] or q.get("concept_id") != cid:
            fail("concept_id_changed_or_unresolved")
        prompt = str(q.get("prompt") or "")
        ans = str(q.get("answer_text") or "")
        text = sem(ans)
        if not q.get("task_alignment_v198"):
            fail("missing_v198_marker")
        if len(words(prompt)) < 65 or "?" not in prompt:
            fail("weak_prompt:" + str(len(words(prompt))))
        if len(words(ans)) < 500:
            fail("weak_answer:" + str(len(words(ans))))
        if q.get("choices") or q.get("answer") is not None:
            fail("not_free_response")
        if not q.get("reviewed_all_domains_v178") or not q.get("review_basis_v178"):
            fail("lost_v178_review_metadata")
        if set(q.get("depth_layers_v198") or {}) != {"foundation", "application", "senior_decision"}:
            fail("missing_three_layer_depth")
        traps = q.get("common_traps_v198") or []
        if len(traps) < 5 or any(len(words(x)) < 25 for x in traps):
            fail("weak_individualized_trap_reasoning")
        if not str(q.get("deliberate_review_v198") or "").strip():
            fail("missing_deliberate_review_metadata")
        for label, terms in TERM_GROUPS.items():
            if not all(sem(term) in text for term in terms):
                fail("missing_semantic_group:" + label)
        if "ct can be useful in selected stable equivocal cases" not in text:
            fail("missing_ct_non_delay_boundary")
        if "avoid blind instrumentation" not in text:
            fail("missing_blind_instrumentation_trap")
        if "bailout, not a routine technique" not in text:
            fail("missing_mainstem_bailout_boundary")
        rows.append({
            "id": qid,
            "concept_id": q.get("concept_id"),
            "resolved_topic": topic,
            "prompt_words": len(words(prompt)),
            "answer_words": len(words(ans)),
            "trap_count": len(traps),
            "failures": local,
        })

    repaired = set(align.get("repaired") or [])
    if repaired != expected:
        failures.append(
            "runtime_repaired_set_mismatch=" + ",".join(sorted(expected - repaired))
            + "|extra=" + ",".join(sorted(repaired - expected))
        )
    with open("V198_TASK_ALIGNMENT_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump({"expected_ids": sorted(expected), "runtime_alignment": align, "failures": failures, "items": rows}, f, indent=2, ensure_ascii=False)
    print(f"V198_EXPECTED|{len(expected)}")
    print(f"V198_REPAIRED|{len(repaired)}")
    print(f"V198_FAILURES|{len(failures)}")
    for r in rows:
        print("V198_DEPTH_ITEM|{id}|prompt={prompt_words}|answer={answer_words}|traps={trap_count}|topic={resolved_topic}".format(**r))
    for x in failures:
        print("FAIL|" + x)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
