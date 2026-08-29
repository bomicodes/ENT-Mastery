"""v28.9 — semantic hard gate for neighboring pediatric ear canonical concepts.

Protects a deliberate distinction:
- AOM / OME / Tympanostomy Decisions = diagnose/treat otitis disease and escalate complications.
- Tympanostomy Tube Indications = decide surgical candidacy from chronicity, effusion, hearing/developmental risk.
"""
from collections import Counter, defaultdict
import runtime_entry as rt

DOMAIN = "Pediatric Otolaryngology"
OTITIS = "AOM / OME / Tympanostomy Decisions"
TUBES = "Tympanostomy Tube Indications"
STAGES = {"foundation", "application", "senior_decision"}


def _lower(q):
    fields = [q.get("stem"), q.get("explanation"), q.get("board_pearl")]
    fields += list(q.get("choices") or [])
    return " ".join(str(x or "") for x in fields).lower()


def main():
    data = rt.data
    ids = [str(q.get("id") or "") for q in data.CLINICAL_CHALLENGES_V119]
    duplicates = sorted(qid for qid, n in Counter(ids).items() if qid and n > 1)
    failures = [f"duplicate_id:{qid}" for qid in duplicates]

    grouped = defaultdict(list)
    for q in data.CLINICAL_CHALLENGES_V119:
        cid = q.get("concept_id")
        if cid:
            grouped[cid].append(q)

    rows = {}
    for topic in (OTITIS, TUBES):
        cid = data._v6_item_id(DOMAIN, topic)
        reviewed = [q for q in grouped.get(cid, []) if q.get("ladder_reviewed")]
        rows[topic] = reviewed
        stages = {q.get("learning_stage") for q in reviewed}
        if stages & STAGES != STAGES:
            failures.append(f"{topic}:missing_stages:{sorted(STAGES-stages)}")
        for q in reviewed:
            if q.get("concept_id") != cid:
                failures.append(f"{q.get('id')}:bad_canonical_link")
            choices = list(q.get("choices") or [])
            reasons = list(q.get("why_wrong") or [])
            try:
                answer = int(q.get("answer"))
            except (TypeError, ValueError):
                failures.append(f"{q.get('id')}:invalid_answer")
                continue
            if len(choices) < 2 or not 0 <= answer < len(choices):
                failures.append(f"{q.get('id')}:invalid_choices_answer")
            if len(reasons) != len(choices):
                failures.append(f"{q.get('id')}:rationale_length_mismatch")
            elif not str(reasons[answer]).strip().lower().startswith("correct."):
                failures.append(f"{q.get('id')}:correct_rationale_misaligned")

    otitis_by_id = {q.get("id"): q for q in rows[OTITIS]}
    for qid in ("v242_ped_ear_app", "v242_ped_ear_snr"):
        q = otitis_by_id.get(qid)
        if not q:
            failures.append(f"{qid}:missing")
            continue
        if not q.get("semantic_alignment_v289") or not q.get("deliberate_review_v289"):
            failures.append(f"{qid}:missing_v289_review_metadata")

    app = otitis_by_id.get("v242_ped_ear_app")
    if app:
        text = _lower(app)
        for anchor in ("48-72", "observation", "rescue", "nonsevere"):
            if anchor not in text:
                failures.append(f"v242_ped_ear_app:missing_acute_treatment_anchor:{anchor}")
        if "four well-documented episodes" in text or "candidacy assessment" in text:
            failures.append("v242_ped_ear_app:still_duplicates_recurrent_aom_tube_candidacy")

    senior = otitis_by_id.get("v242_ped_ear_snr")
    if senior:
        text = _lower(senior)
        for anchor in ("mastoid", "postauricular", "iv antibiotics", "ent"):
            if anchor not in text:
                failures.append(f"v242_ped_ear_snr:missing_complication_anchor:{anchor}")
        if "family expects tubes" in text or "episode count" in text:
            failures.append("v242_ped_ear_snr:still_duplicates_tube_candidacy")

    tube_text = " ".join(_lower(q) for q in rows[TUBES])
    for anchor in ("3 months", "hearing", "effusion", "developmental"):
        if anchor not in tube_text:
            failures.append(f"{TUBES}:missing_candidacy_anchor:{anchor}")
    if "no middle-ear effusion" not in tube_text:
        failures.append(f"{TUBES}:missing_recurrent_aom_no_effusion_modifier")

    print(f"PED_EAR_V289|otitis_reviewed={len(rows[OTITIS])}|tube_reviewed={len(rows[TUBES])}|failures={len(failures)}")
    for topic, reviewed in rows.items():
        print(f"PED_EAR_TOPIC|{topic}|ids={','.join(str(q.get('id')) for q in reviewed)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
