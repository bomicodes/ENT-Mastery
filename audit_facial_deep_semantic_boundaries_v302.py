"""v30.2 — fail-closed semantic-boundary gate for facial-trauma Concept Hubs.

The canonical Facial Plastics contract contains one NOE Fracture topic and one
Frontal Sinus Fracture topic. v30.0/v30.1 also retain useful subordinate payloads
for operative mechanics / decision-model teaching, but those labels must never
silently become parallel canonical cards. This gate protects the one-concept
contract while requiring the live canonical cards to retain the high-yield
mechanics and management distinctions those subordinate payloads were designed
to teach.
"""

import re
import runtime_entry as rt

DOMAIN = "Facial Plastics / Trauma"
FORBIDDEN_PARALLEL_TOPICS = {
    "NOE Fracture Mechanics",
    "Frontal Sinus Fracture Decision Model",
}


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _module_text(module):
    fields = ("recognize", "localize", "workup", "manage", "operate", "teach")
    return " ".join(str(module.get(field) or "") for field in fields).lower()


def _require_any(text, groups, label, failures):
    for description, terms in groups:
        if not any(term.lower() in text for term in terms):
            failures.append(f"{label}: missing {description} anchor; expected one of {terms}")


def main():
    data = rt.data
    modules = (data.DEEP_MODULES_V6 or {}).get(DOMAIN, [])
    topics = [m.get("topic") for m in modules if m.get("topic")]
    by_topic = {m.get("topic"): m for m in modules if m.get("topic")}
    failures = []

    if len(topics) != 32:
        failures.append(f"expected 32 canonical Facial Plastics / Trauma topics, found {len(topics)}")
    for forbidden in sorted(FORBIDDEN_PARALLEL_TOPICS):
        if forbidden in by_topic:
            failures.append(
                f"noncanonical parallel card became live: {forbidden}; fold its teaching into the parent canonical concept"
            )

    noe = by_topic.get("NOE Fracture")
    frontal = by_topic.get("Frontal Sinus Fracture")
    if not noe:
        failures.append("missing canonical NOE Fracture module")
    else:
        text = _module_text(noe)
        _require_any(text, [
            ("medial-canthal-tendon", ("medial canthal tendon", "mct")),
            ("type-II retained tendon-bearing fragment", ("type ii", "type 2")),
            ("type-III avulsion", ("type iii", "type 3")),
            ("canthal reconstruction", ("canthopexy", "canthal")),
            ("central facial framework", ("central facial width", "buttress")),
            ("nasal projection/support", ("nasal projection", "dorsal support")),
        ], "NOE Fracture", failures)

    if not frontal:
        failures.append("missing canonical Frontal Sinus Fracture module")
    else:
        text = _module_text(frontal)
        _require_any(text, [
            ("anterior-table contour axis", ("anterior table", "front table")),
            ("posterior-table/dural axis", ("posterior table", "back table")),
            ("outflow-tract axis", ("fsot", "outflow tract", "frontal recess")),
            ("sinus preservation", ("sinus-preserving", "preserve", "restore drainage")),
            ("obliteration", ("obliteration", "obliterate")),
            ("cranialization", ("cranialization", "cranialize")),
            ("delayed mucocele risk", ("mucocele", "mucopyocele")),
        ], "Frontal Sinus Fracture", failures)

    # The adaptive ladders must remain linked only to the exact canonical parents.
    reviewed = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("ladder_reviewed")]
    for q in reviewed:
        if q.get("topic") in FORBIDDEN_PARALLEL_TOPICS:
            failures.append(f"{q.get('id')}: reviewed vignette linked to noncanonical parallel topic {q.get('topic')}")

    print(f"FACIAL_DEEP_CANONICAL_TOPICS|{len(topics)}")
    print(f"FACIAL_DEEP_FORBIDDEN_PARALLEL_TOPICS|{len(FORBIDDEN_PARALLEL_TOPICS)}")
    if failures:
        print("FACIAL DEEP SEMANTIC-BOUNDARY FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print(
        "PASS: NOE and frontal-sinus mechanics/decision teaching remain folded into exact canonical parents without parallel live cards"
    )


if __name__ == "__main__":
    main()
