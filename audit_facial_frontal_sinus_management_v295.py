"""v29.5 hard gate for the added frontal-sinus outflow-tract management layer."""

from collections import Counter

import runtime_entry


data = runtime_entry.data
DOMAIN = "Facial Plastics / Trauma"
TOPIC = "Frontal Sinus Fracture"
QUESTION_ID = "v295_fpt_frontal_outflow_mgt"
EXISTING_IDS = (
    "v258_fpt_frontal_fnd",
    "v258_fpt_frontal_app",
    "v258_fpt_frontal_snr",
)


def _words(value):
    return len(str(value or "").split())


def main():
    challenges = list(data.CLINICAL_CHALLENGES_V119)
    failures = []
    counts = Counter(str(q.get("id") or "") for q in challenges)
    duplicate_ids = sorted(qid for qid, count in counts.items() if qid and count > 1)
    if duplicate_ids:
        failures.extend("duplicate_id:" + qid for qid in duplicate_ids)

    by_id = {str(q.get("id") or ""): q for q in challenges}
    expected_cid = data._v6_item_id(DOMAIN, TOPIC)
    required_ids = EXISTING_IDS + (QUESTION_ID,)
    missing = [qid for qid in required_ids if qid not in by_id]
    if missing:
        failures.append("missing_cases:" + ",".join(missing))

    rows = [q for q in challenges if q.get("concept_id") == expected_cid and q.get("ladder_reviewed")]
    stages = {str(q.get("learning_stage") or "") for q in rows}
    for stage in ("foundation", "application", "senior_decision"):
        if stage not in stages:
            failures.append("missing_stage:" + stage)

    if QUESTION_ID in by_id:
        q = by_id[QUESTION_ID]
        if q.get("domain") != DOMAIN or q.get("topic") != TOPIC:
            failures.append("new_case_domain_topic_drift")
        if q.get("concept_id") != expected_cid:
            failures.append("new_case_canonical_link_drift")
        if q.get("learning_stage") != "application":
            failures.append("new_case_stage_not_application")
        if not q.get("ladder_reviewed"):
            failures.append("new_case_not_ladder_reviewed")
        if not q.get("management_layer_v295"):
            failures.append("missing_management_layer_marker")
        if not str(q.get("deliberate_review_v295") or "").strip():
            failures.append("missing_deliberate_review_metadata")

        choices = list(q.get("choices") or [])
        reasons = list(q.get("why_wrong") or [])
        try:
            answer = int(q.get("answer"))
        except (TypeError, ValueError):
            answer = -1
        if len(choices) != 4 or len(reasons) != 4:
            failures.append(f"choice_rationale_shape:{len(choices)}:{len(reasons)}")
        if not 0 <= answer < len(choices):
            failures.append("invalid_answer_index")
        elif answer >= len(reasons) or not str(reasons[answer]).startswith("Correct."):
            failures.append("correct_rationale_not_aligned_after_balance")
        for i, reason in enumerate(reasons):
            if _words(reason) < 12:
                failures.append(f"weak_rationale:{i}:{_words(reason)}")
            if i != answer and str(reason).startswith("Correct."):
                failures.append(f"incorrect_option_marked_correct:{i}")
        if len({str(r).strip() for r in reasons}) != len(reasons):
            failures.append("duplicate_distractor_reasoning")

        semantic_text = " ".join(
            [str(q.get("stem") or ""), str(q.get("explanation") or ""), str(q.get("board_pearl") or ""), str(q.get("curveball") or "")]
            + [str(x) for x in choices]
            + [str(x) for x in reasons]
        ).lower()
        anchor_groups = {
            "outflow_axis": ("outflow", "frontal recess"),
            "durable_drainage": ("durable drainage", "functional sinus", "drainage"),
            "nonreflex_cranialization": ("not the automatic", "not a reflex", "rather than being a reflex", "not the automatic treatment"),
            "late_mucocele": ("mucocele",),
            "posterior_dural_distinction": ("posterior-table", "posterior table", "dural"),
        }
        for name, anchors in anchor_groups.items():
            if not any(anchor in semantic_text for anchor in anchors):
                failures.append("missing_semantic_anchor:" + name)

    # Protect the original three questions rather than allowing the new case to
    # replace a strong foundation, observation application, or skull-base senior decision.
    for qid in EXISTING_IDS:
        q = by_id.get(qid)
        if not q:
            continue
        if q.get("concept_id") != expected_cid:
            failures.append(qid + ":canonical_link_drift")
        if not q.get("ladder_reviewed"):
            failures.append(qid + ":lost_ladder_reviewed")
    expected_stages = {
        "v258_fpt_frontal_fnd": "foundation",
        "v258_fpt_frontal_app": "application",
        "v258_fpt_frontal_snr": "senior_decision",
    }
    for qid, expected_stage in expected_stages.items():
        q = by_id.get(qid)
        if q and q.get("learning_stage") != expected_stage:
            failures.append(f"{qid}:stage_drift:{q.get('learning_stage')!r}")

    print(f"V295_FRONTAL_EXPECTED_CID|{expected_cid}")
    print(f"V295_FRONTAL_REVIEWED_CASES|{len(rows)}")
    print("V295_FRONTAL_STAGES|" + ",".join(sorted(stages)))
    print(f"V295_FRONTAL_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
