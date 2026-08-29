"""v29.8 semantic hard gate for the live NOE application decision."""
import runtime_entry as rt

DOMAIN = "Facial Plastics / Trauma"
TOPIC = "NOE Fracture"
TARGET_ID = "v258_fpt_noe_app"


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
    by_stage = {q.get("learning_stage") for q in rows}
    for stage in ("foundation", "application", "senior_decision"):
        if stage not in by_stage:
            failures.append(f"NOE ladder missing {stage}")

    target = next((q for q in rows if q.get("id") == TARGET_ID), None)
    if target is None:
        failures.append(f"missing {TARGET_ID}")
    else:
        if not target.get("_semantic_review_v298"):
            failures.append("v29.8 deliberate semantic marker missing")
        if target.get("learning_stage") != "application":
            failures.append("NOE classification/fixation case must remain application stage")
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
        for anchor in ("type ii", "type iii", "medial canthal tendon", "tendon bearing", "canthopexy", "comminuted"):
            if anchor not in text:
                failures.append(f"missing NOE semantic anchor: {anchor}")
        if not any(x in text for x in ("avulsed", "avulsion")):
            failures.append("type III MCT avulsion distinction missing")
        if not any(x in text for x in ("stabilize", "fixation", "fix the stable")):
            failures.append("type II tendon-bearing fragment fixation decision missing")

    ids = [q.get("id") for q in data.CLINICAL_CHALLENGES_V119 if q.get("id")]
    if len(ids) != len(set(ids)):
        failures.append("duplicate clinical challenge IDs detected")

    if failures:
        print("FACIAL NOE v29.8 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: NOE ladder preserves foundation/application/senior structure and now discriminates type II tendon-bearing fixation from type III MCT avulsion/canthopexy")


if __name__ == "__main__":
    main()
