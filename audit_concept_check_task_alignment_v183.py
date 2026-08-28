"""v18.3 hard gate for the live-canonical high-risk Concept Check cohort."""

import json
import re

import runtime_entry
from concept_check_board_repair_v177 import _find_module
from concept_check_task_alignment_v183 import COHORT

TASK_TERMS = {
    "cc-v112-rec-sleep-surgery-central-events-hypoventilation": ["co2", "central", "hypoventilation", "obstructive surgery"],
    "cc-v112-rec-rhinology-allergy-skull-base-frontal-recess-frontal-sinus": ["ct plane", "skull-base", "anterior ethmoidal", "visual loss"],
    "cc-v112-mgt-facial-plastics-trauma-facial-soft-tissue-lacerations-burns": ["facial nerve", "parotid duct", "blind deep clamping", "vision"],
    "cc-v112-rec-head-neck-oncology-open-partial-conservation-laryngectomy": ["cricoarytenoid", "margins", "aspiration", "usable organ"],
    "cc-v112-rec-general-ent-emergencies-common-ent-consult-triage-disposition": ["airway", "hemorrhage", "vision", "transfer"],
    "cc-v112-rec-head-neck-oncology-reconstruction-selection-after-head-neck-ablation": ["recipient-vessel", "vascularized", "flap monitoring", "salvage"],
    "cc-v112-rec-general-ent-emergencies-ent-perioperative-anesthesia-difficult-airway-planning": ["spontaneous ventilation", "awake", "front-of-neck", "repeated"],
    "cc-v112-rec-rhinology-allergy-skull-base-sphenoidotomy": ["superior turbinate", "carotid", "optic", "septation"],
    "cc-v112-rec-general-ent-emergencies-postoperative-neck-hematoma": ["decompression", "venous", "lymphatic", "ct"],
    "cc-v112-mgt-laryngology-voice-swallowing-posterior-cordotomy-arytenoidectomy": ["cordotomy", "arytenoidectomy", "aspiration", "tracheostomy"],
}


def words(value):
    return re.findall(r"\b\w+[\w'-]*\b", str(value or ""))


def main():
    data = runtime_entry.data
    checks = list(data.CONCEPT_CHECKS_V112)
    by_id = {str(q.get("id") or ""): q for q in checks}
    failures = []
    rows = []
    expected = set(COHORT)

    runtime_result = getattr(runtime_entry, "CONCEPT_CHECK_FINAL_CLINICAL_GATE_V179", {})
    alignment = runtime_result.get("task_alignment_v183") or {}
    if alignment.get("missing"):
        failures.append("runtime_missing=" + ",".join(alignment["missing"]))
    if alignment.get("link_mismatch"):
        failures.append("runtime_link_mismatch=" + ",".join(alignment["link_mismatch"]))

    for qid in sorted(expected):
        q = by_id.get(qid)
        if not q:
            failures.append(f"{qid}:missing")
            continue
        item_failures = []

        def fail(reason):
            failures.append(f"{qid}:{reason}")
            item_failures.append(reason)

        payload = COHORT[qid]
        module = _find_module(q, data.DEEP_MODULES_V6, data._v6_item_id)
        resolved_topic = str(module.get("topic") or "") if module else ""
        resolved_cid = data._v6_item_id(q.get("domain"), resolved_topic) if module and q.get("domain") else None
        if not module:
            fail("no_live_canonical_module")
        if resolved_topic != payload["canonical_topic"]:
            fail(f"resolved_topic_mismatch:{resolved_topic!r}")
        if resolved_cid != payload["concept_id"] or q.get("concept_id") != resolved_cid:
            fail("concept_id_changed_or_unresolved")

        prompt = str(q.get("prompt") or "")
        answer = str(q.get("answer_text") or "")
        answer_lower = answer.lower()
        if not q.get("task_alignment_v183"):
            fail("missing_v183_marker")
        if len(words(prompt)) < 45 or "?" not in prompt:
            fail(f"weak_prompt:{len(words(prompt))}")
        if len(words(answer)) < 90:
            fail(f"weak_answer:{len(words(answer))}")
        if q.get("choices"):
            fail("unexpected_choices")
        if q.get("answer") is not None:
            fail("unexpected_answer_index")
        if not q.get("reviewed_all_domains_v178") or not q.get("review_basis_v178"):
            fail("lost_v178_review_metadata")
        layers = q.get("depth_layers_v183") or {}
        if set(layers) != {"foundation", "application", "senior_decision"}:
            fail("missing_three_layer_depth")
        traps = q.get("common_traps_v183") or []
        if len(traps) < 2 or any(len(words(x)) < 8 for x in traps):
            fail("weak_individualized_trap_reasoning")
        if not str(q.get("deliberate_review_v183") or "").strip():
            fail("missing_deliberate_review_metadata")
        if not str(q.get("explanation") or "").strip() or not str(q.get("board_pearl") or "").strip():
            fail("missing_explanation_or_board_pearl")
        missing_terms = [term for term in TASK_TERMS[qid] if term not in answer_lower]
        if missing_terms:
            fail("missing_task_terms:" + ",".join(missing_terms))
        rows.append({
            "id": qid,
            "concept_id": q.get("concept_id"),
            "resolved_topic": resolved_topic,
            "prompt_words": len(words(prompt)),
            "answer_words": len(words(answer)),
            "trap_count": len(traps),
            "failures": item_failures,
        })

    repaired = set(alignment.get("repaired") or [])
    if repaired != expected:
        failures.append("runtime_repaired_set_mismatch=" + ",".join(sorted(expected - repaired)) + "|extra=" + ",".join(sorted(repaired - expected)))

    report = {"expected_ids": sorted(expected), "runtime_alignment": alignment, "failures": failures, "items": rows}
    with open("V183_TASK_ALIGNMENT_AUDIT.json", "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"V183_DEPTH_EXPECTED|{len(expected)}")
    print(f"V183_DEPTH_REPAIRED|{len(repaired)}")
    print(f"V183_DEPTH_FAILURES|{len(failures)}")
    for row in rows:
        print(f"V183_DEPTH_ITEM|{row['id']}|prompt={row['prompt_words']}|answer={row['answer_words']}|traps={row['trap_count']}|topic={row['resolved_topic']}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
