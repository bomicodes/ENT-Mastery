"""v29.4 semantic hard gate: Neck Dissection vs Complications of Neck Surgery."""

from collections import Counter, defaultdict
import re

import runtime_entry


data = runtime_entry.data
DOMAIN = "Head & Neck Oncology"
OPERATIVE_TOPIC = "Neck Dissection"
COMPLICATION_TOPIC = "Complications of Neck Surgery"
OPERATIVE_IDS = {"v128_hn_03", "v219_hn_neck_app", "v219_hn_neck_snr"}
COMPLICATION_IDS = {"v231_hn_neckcomp_fnd", "v231_hn_neckcomp_app", "v231_hn_neckcomp_snr"}
EXPECTED_STAGES = {"foundation", "application", "senior_decision"}


def _text(q):
    return " ".join(str(q.get(k) or "") for k in ("stem", "explanation", "board_pearl", "curveball")).lower()


def _has_any(text, terms):
    return any(term in text for term in terms)


def main():
    rows = list(data.CLINICAL_CHALLENGES_V119)
    by_id = {str(q.get("id") or ""): q for q in rows if q.get("id")}
    failures = []

    duplicate_ids = [qid for qid, n in Counter(str(q.get("id") or "") for q in rows if q.get("id")).items() if n > 1]
    failures.extend(f"duplicate_id:{qid}" for qid in duplicate_ids)

    expected = OPERATIVE_IDS | COMPLICATION_IDS
    missing = sorted(expected - set(by_id))
    failures.extend(f"missing:{qid}" for qid in missing)

    operative_cid = data._v6_item_id(DOMAIN, OPERATIVE_TOPIC)
    complication_cid = data._v6_item_id(DOMAIN, COMPLICATION_TOPIC)
    stage_map = defaultdict(set)

    for qid in sorted(expected & set(by_id)):
        q = by_id[qid]
        is_operative = qid in OPERATIVE_IDS
        topic = OPERATIVE_TOPIC if is_operative else COMPLICATION_TOPIC
        cid = operative_cid if is_operative else complication_cid
        role = "operative_selection_anatomy_and_oncologic_extent" if is_operative else "postoperative_complication_recognition_and_rescue"

        if q.get("domain") != DOMAIN: failures.append(f"{qid}:domain_drift")
        if q.get("topic") != topic: failures.append(f"{qid}:topic_drift:{q.get('topic')!r}")
        if q.get("concept_id") != cid: failures.append(f"{qid}:canonical_link_drift:{q.get('concept_id')!r}")
        if not q.get("ladder_reviewed"): failures.append(f"{qid}:lost_ladder_reviewed")
        if q.get("semantic_role_v294") != role: failures.append(f"{qid}:semantic_role_drift")
        if not str(q.get("deliberate_review_v294") or "").strip(): failures.append(f"{qid}:missing_deliberate_review")
        stage = q.get("learning_stage")
        stage_map[topic].add(stage)

        choices = list(q.get("choices") or [])
        why = list(q.get("why_wrong") or [])
        try: answer = int(q.get("answer"))
        except (TypeError, ValueError):
            failures.append(f"{qid}:invalid_answer"); continue
        if len(choices) != 4: failures.append(f"{qid}:choice_count={len(choices)}")
        if len(why) != len(choices): failures.append(f"{qid}:why_wrong_count={len(why)}")
        if not 0 <= answer < len(choices): failures.append(f"{qid}:answer_out_of_range={answer}")
        elif len(why) == len(choices):
            if "correct" not in str(why[answer]).lower(): failures.append(f"{qid}:correct_rationale_misaligned")
            for idx, reason in enumerate(why):
                if idx != answer and "correct" in str(reason).lower(): failures.append(f"{qid}:distractor_marked_correct:{idx}")
                if len(re.findall(r"\b\w+[\w'-]*\b", str(reason))) < 6: failures.append(f"{qid}:shallow_rationale:{idx}")

    for topic in (OPERATIVE_TOPIC, COMPLICATION_TOPIC):
        if stage_map[topic] != EXPECTED_STAGES:
            failures.append(f"{topic}:stage_set={sorted(stage_map[topic])}")

    operative_text = " ".join(_text(by_id[qid]) for qid in OPERATIVE_IDS if qid in by_id)
    complication_text = " ".join(_text(by_id[qid]) for qid in COMPLICATION_IDS if qid in by_id)

    operative_anchors = {
        "selective_nodal_strategy": ("selective neck dissection", "nodal levels"),
        "structure_preservation": ("spinal accessory", "internal jugular", "sternocleidomastoid"),
        "oncologic_sacrifice": ("invading the internal jugular", "preserving uninvolved"),
    }
    complication_anchors = {
        "chyle_leak": ("chyle", "milky"),
        "accessory_morbidity": ("shoulder", "trapezius"),
        "major_vessel_rescue": ("carotid", "vascularized coverage", "major-vessel"),
    }
    for label, terms in operative_anchors.items():
        if not _has_any(operative_text, terms): failures.append(f"operative_missing_anchor:{label}")
    for label, terms in complication_anchors.items():
        if not _has_any(complication_text, terms): failures.append(f"complication_missing_anchor:{label}")

    # Explicitly protect the improved reused foundation rationale.
    fnd = by_id.get("v128_hn_03")
    if fnd:
        if not fnd.get("rationale_depth_v294"): failures.append("v128_hn_03:missing_rationale_depth_marker")
        foundation_why = " ".join(str(x).lower() for x in (fnd.get("why_wrong") or []))
        for anchor in ("level iv", "level i", "superior thyroid", "level iib"):
            if anchor not in foundation_why: failures.append(f"v128_hn_03:rationale_missing:{anchor}")

    print(f"V294_NECK_SEMANTIC|operative={len(OPERATIVE_IDS)}|complications={len(COMPLICATION_IDS)}")
    print(f"V294_OPERATIVE_STAGES|{','.join(sorted(stage_map[OPERATIVE_TOPIC]))}")
    print(f"V294_COMPLICATION_STAGES|{','.join(sorted(stage_map[COMPLICATION_TOPIC]))}")
    print(f"V294_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
