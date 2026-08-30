"""v29.9 semantic hard gate for Pediatric PSG perioperative disposition."""
import runtime_entry as rt

DOMAIN = "Sleep Surgery"
TOPIC = "Pediatric PSG Interpretation"
TARGET_ID = "v299_sleep_peds_psg_mgt"


def _text(q):
    fields = [q.get("stem"), q.get("explanation"), q.get("board_pearl"), q.get("curveball")]
    fields += list(q.get("choices") or [])
    fields += list(q.get("why_wrong") or [])
    return " ".join(str(x or "") for x in fields).lower().replace("-", " ")


def main():
    data = rt.data
    cid = data._v6_item_id(DOMAIN, TOPIC)
    rows = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("concept_id") == cid and q.get("ladder_reviewed")]
    failures = []
    stages = {q.get("learning_stage") for q in rows}
    for stage in ("foundation", "application", "management", "senior_decision"):
        if stage not in stages:
            failures.append(f"Pediatric PSG ladder missing {stage}")

    target = next((q for q in rows if q.get("id") == TARGET_ID), None)
    if target is None:
        failures.append(f"missing {TARGET_ID}")
    else:
        if target.get("topic") != TOPIC or target.get("domain") != DOMAIN or target.get("concept_id") != cid:
            failures.append("v29.9 exact canonical linkage lost")
        if target.get("learning_stage") != "management" or not target.get("_semantic_review_v299"):
            failures.append("v29.9 deliberate management metadata missing")
        choices = list(target.get("choices") or [])
        reasons = list(target.get("why_wrong") or [])
        try:
            answer = int(target.get("answer"))
        except (TypeError, ValueError):
            answer = -1
        if len(choices) != 4 or len(reasons) != len(choices) or not 0 <= answer < len(choices):
            failures.append("choice/answer/rationale schema invalid")
        elif not str(reasons[answer]).strip().lower().startswith("correct."):
            failures.append("correct rationale lost alignment after deterministic balancing")
        text = _text(target)
        for anchor in ("overnight", "inpatient", "ahi", "10", "80", "severe osa"):
            if anchor not in text:
                failures.append(f"missing pediatric PSG disposition anchor: {anchor}")
        if "or both" not in text and "or, not and" not in text:
            failures.append("AHI-versus-nadir OR logic is not explicit")
        if "younger than 3" not in text and "under 3" not in text and "age <3" not in text:
            failures.append("independent age-based overnight-monitoring trigger missing")

    ids = [q.get("id") for q in data.CLINICAL_CHALLENGES_V119 if q.get("id")]
    if len(ids) != len(set(ids)):
        failures.append("duplicate clinical challenge IDs detected")

    if failures:
        print("SLEEP PEDIATRIC PSG v29.9 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: Pediatric PSG now spans foundation/application/management/senior decision-making and protects AAO-HNS postoperative monitoring logic")


if __name__ == "__main__":
    main()
