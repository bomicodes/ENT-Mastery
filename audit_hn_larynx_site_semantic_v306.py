"""v30.6 semantic hard gate: Supraglottic Cancer vs Glottic Cancer.

Protects the already-strong adaptive ladders from collapsing into a generic
"laryngeal cancer" pathway as the Concept Hub continues to deepen.  This gate
intentionally preserves strong questions rather than adding filler.
"""

from collections import Counter, defaultdict
import re

import runtime_entry


data = runtime_entry.data
DOMAIN = "Head & Neck Oncology"
SUPRA = "Supraglottic Cancer"
GLOTTIC = "Glottic Cancer"
SUPRA_IDS = {"v220_hn_supra_fnd", "v220_hn_supra_app", "v220_hn_supra_snr"}
GLOTTIC_IDS = {"v138_hn_08", "v143_hno_01", "v220_hn_glottic_snr"}
EXPECTED_STAGES = {"foundation", "application", "senior_decision"}


def _text(q):
    fields = ("stem", "explanation", "board_pearl", "curveball")
    parts = [str(q.get(k) or "") for k in fields]
    parts.extend(str(x) for x in (q.get("choices") or []))
    parts.extend(str(x) for x in (q.get("why_wrong") or []))
    return " ".join(parts).lower()


def _has_any(text, terms):
    return any(term in text for term in terms)


def _require_anchor(failures, text, prefix, label, terms):
    if not _has_any(text, terms):
        failures.append(f"{prefix}_missing_anchor:{label}")


def main():
    rows = list(data.CLINICAL_CHALLENGES_V119)
    by_id = {str(q.get("id") or ""): q for q in rows if q.get("id")}
    failures = []

    duplicates = [
        qid for qid, n in Counter(str(q.get("id") or "") for q in rows if q.get("id")).items()
        if n > 1
    ]
    failures.extend(f"duplicate_id:{qid}" for qid in duplicates)

    expected = SUPRA_IDS | GLOTTIC_IDS
    failures.extend(f"missing:{qid}" for qid in sorted(expected - set(by_id)))

    supra_cid = data._v6_item_id(DOMAIN, SUPRA)
    glottic_cid = data._v6_item_id(DOMAIN, GLOTTIC)
    stage_map = defaultdict(set)

    for qid in sorted(expected & set(by_id)):
        q = by_id[qid]
        is_supra = qid in SUPRA_IDS
        topic = SUPRA if is_supra else GLOTTIC
        cid = supra_cid if is_supra else glottic_cid

        if q.get("domain") != DOMAIN:
            failures.append(f"{qid}:domain_drift")
        if q.get("topic") != topic:
            failures.append(f"{qid}:topic_drift:{q.get('topic')!r}")
        if q.get("concept_id") != cid:
            failures.append(f"{qid}:canonical_link_drift:{q.get('concept_id')!r}")
        if not q.get("ladder_reviewed"):
            failures.append(f"{qid}:lost_ladder_reviewed")
        stage = q.get("learning_stage")
        stage_map[topic].add(stage)
        if stage not in EXPECTED_STAGES:
            failures.append(f"{qid}:invalid_learning_stage:{stage!r}")

        choices = list(q.get("choices") or [])
        why = list(q.get("why_wrong") or [])
        try:
            answer = int(q.get("answer"))
        except (TypeError, ValueError):
            failures.append(f"{qid}:invalid_answer")
            continue
        if len(choices) != 4:
            failures.append(f"{qid}:choice_count={len(choices)}")
        if len(why) != len(choices):
            failures.append(f"{qid}:why_wrong_count={len(why)}")
        if not 0 <= answer < len(choices):
            failures.append(f"{qid}:answer_out_of_range={answer}")
        elif len(why) == len(choices):
            if "correct" not in str(why[answer]).lower():
                failures.append(f"{qid}:correct_rationale_misaligned")
            for idx, reason in enumerate(why):
                if idx != answer and "correct" in str(reason).lower():
                    failures.append(f"{qid}:distractor_marked_correct:{idx}")
                if len(re.findall(r"\b\w+[\w'-]*\b", str(reason))) < 6:
                    failures.append(f"{qid}:shallow_rationale:{idx}")

    for topic in (SUPRA, GLOTTIC):
        if stage_map[topic] != EXPECTED_STAGES:
            failures.append(f"{topic}:stage_set={sorted(stage_map[topic])}")

    supra_text = " ".join(_text(by_id[qid]) for qid in SUPRA_IDS if qid in by_id)
    glottic_text = " ".join(_text(by_id[qid]) for qid in GLOTTIC_IDS if qid in by_id)

    # Supraglottic disease must retain its distinctive nodal biology and the
    # functional price of supraglottic conservation/organ preservation.
    _require_anchor(failures, supra_text, "supraglottic", "rich_lymphatics",
                    ("richer bilateral lymphatic", "abundant lymphatic", "bilateral drainage"))
    _require_anchor(failures, supra_text, "supraglottic", "elective_neck_logic",
                    ("occult nodal risk", "elective neck"))
    _require_anchor(failures, supra_text, "supraglottic", "swallow_airway_reserve",
                    ("pulmonary reserve", "rehabilitate swallowing", "airway protection"))
    _require_anchor(failures, supra_text, "supraglottic", "functional_larynx_decision",
                    ("severe baseline aspiration", "nonfunctional aspirating larynx", "poorly functioning larynx"))

    # Early glottic disease must remain a local-control/voice decision with low
    # occult nodal risk rather than inheriting supraglottic neck logic.
    _require_anchor(failures, glottic_text, "glottic", "single_local_modality",
                    ("transoral laser microsurgery or definitive radiation", "single definitive modality"))
    _require_anchor(failures, glottic_text, "glottic", "sparse_lymphatics",
                    ("sparse lymphatic", "low occult nodal risk"))
    _require_anchor(failures, glottic_text, "glottic", "avoid_routine_bilateral_neck",
                    ("mandatory bilateral neck dissection", "routine total laryngectomy"))
    _require_anchor(failures, glottic_text, "glottic", "voice_exposure_shared_decision",
                    ("professional voice user", "voice priorities", "endoscopic exposure"))

    # Explicit anti-collapse checks: each ladder needs at least one defining
    # semantic family that should not become the other's core teaching target.
    if "severe baseline aspiration" in glottic_text:
        failures.append("semantic_collapse:glottic_inherited_supraglottic_aspiration_case")
    if "professional voice user" in supra_text:
        failures.append("semantic_collapse:supraglottic_inherited_glottic_voice_case")

    print(f"V306_LARYNX_SITE_SEMANTIC|supraglottic={len(SUPRA_IDS)}|glottic={len(GLOTTIC_IDS)}")
    print(f"V306_SUPRAGLOTTIC_STAGES|{','.join(sorted(stage_map[SUPRA]))}")
    print(f"V306_GLOTTIC_STAGES|{','.join(sorted(stage_map[GLOTTIC]))}")
    print(f"V306_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
