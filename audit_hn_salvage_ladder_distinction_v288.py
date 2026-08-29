"""v28.8 — semantic ladder gate for the two Head & Neck salvage concepts.

The canonical curriculum intentionally contains two adjacent but non-interchangeable
salvage concepts:
  * Salvage Surgery After Radiation/Chemoradiation — broad salvage candidacy,
    irradiated-field operative planning, reconstruction, and complication rescue.
  * Salvage Surgery After Chemoradiation — post-definitive-CRT response assessment,
    PET-directed neck management, and selection for site-specific salvage.

The ordinary ladder-completeness gate validates links/stages/schema. This gate adds
semantic separation so three generic "salvage" questions cannot satisfy both cards.
Topic lookup uses the same punctuation-insensitive normalization used by the v28.7
Concept Hub rebuild so historical slash spacing cannot create a false orphan.
"""

import re
import runtime_entry

DOMAIN = "Head & Neck Oncology"
BROAD = "Salvage Surgery After Radiation/Chemoradiation"
POST_CRT = "Salvage Surgery After Chemoradiation"


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def case_text(q):
    parts = [
        q.get("stem"), q.get("prompt"), q.get("question"), q.get("explanation"),
        q.get("board_pearl"), q.get("curveball"), " ".join(q.get("choices") or []),
        " ".join(q.get("why_wrong") or []),
    ]
    return norm(" ".join(str(x or "") for x in parts))


def has_any(text, terms):
    return any(norm(term) in text for term in terms)


def require_groups(topic, text, groups, failures):
    for label, terms in groups:
        if not has_any(text, terms):
            failures.append(f"{topic}:missing_semantic_group:{label}")


def main():
    data = runtime_entry.data
    failures = []
    canonical_by_norm = {
        norm(m.get("topic")): m
        for m in data.DEEP_MODULES_V6.get(DOMAIN, [])
        if str(m.get("topic") or "").strip()
    }

    target_cases = {}
    actual_topics = {}
    for semantic_topic in (BROAD, POST_CRT):
        module = canonical_by_norm.get(norm(semantic_topic))
        if not module:
            failures.append(f"missing_canonical_topic:{semantic_topic}")
            target_cases[semantic_topic] = []
            continue
        actual_topic = str(module.get("topic") or "").strip()
        actual_topics[semantic_topic] = actual_topic
        cid = data._v6_item_id(DOMAIN, actual_topic)
        linked = [
            q for q in data.VIGNETTES_V7
            if q.get("domain") == DOMAIN
            and q.get("concept_id") == cid
            and q.get("ladder_reviewed")
        ]
        target_cases[semantic_topic] = linked
        stages = {q.get("learning_stage") for q in linked}
        missing = {"foundation", "application", "senior_decision"} - stages
        if missing:
            failures.append(f"{semantic_topic}:missing_stages:{','.join(sorted(missing))}")
        for q in linked:
            if q.get("concept_id") != cid:
                failures.append(f"{semantic_topic}:{q.get('id')}:bad_concept_link")
            print(
                "HN_SALVAGE_CASE|{}|actual_topic={}|{}|{}|{}".format(
                    semantic_topic,
                    actual_topic,
                    q.get("learning_stage"),
                    q.get("id"),
                    norm(q.get("stem") or q.get("prompt") or q.get("question")),
                )
            )

    broad_text = " ".join(case_text(q) for q in target_cases.get(BROAD, []))
    post_text = " ".join(case_text(q) for q in target_cases.get(POST_CRT, []))

    require_groups(BROAD, broad_text, (
        ("prior_irradiated_field", ("irradiated", "prior radiation", "full-dose chemoradiation", "previous radiation")),
        ("salvage_candidacy", ("resectable", "distant staging", "metastatic", "functional reserve")),
        ("vascularized_reconstruction", ("vascularized", "reconstruct", "flap", "outside the irradiated field")),
        ("major_salvage_complication", ("fistula", "carotid", "recipient vessel", "vessel mapping", "flap compromise")),
    ), failures)

    require_groups(POST_CRT, post_text, (
        ("response_assessment", ("response assessment", "metabolic response", "pet/ct", "pet")),
        ("timing_after_crt", ("12 week", "12-week", "10-12 week", "approximately 12", "about 12")),
        ("avoid_routine_planned_neck_dissection", ("planned neck dissection", "routine neck dissection", "complete response", "surveillance")),
        ("equivocal_or_residual_workup", ("equivocal", "residual", "persistent", "biopsy", "reimage", "re-imag")),
        ("selected_salvage", ("salvage neck dissection", "salvage surgery", "curably resectable", "resectable")),
    ), failures)

    distinctive_terms = ("pet", "metabolic response", "planned neck dissection", "complete response", "equivocal")
    distinctive_hits = sum(1 for term in distinctive_terms if norm(term) in post_text)
    if distinctive_hits < 3:
        failures.append(f"{POST_CRT}:insufficient_post_crt_distinction:hits={distinctive_hits}")

    print(f"HN_SALVAGE_BROAD_CANONICAL|{actual_topics.get(BROAD, 'MISSING')}")
    print(f"HN_SALVAGE_POST_CRT_CANONICAL|{actual_topics.get(POST_CRT, 'MISSING')}")
    print(f"HN_SALVAGE_BROAD_REVIEWED|{len(target_cases.get(BROAD, []))}")
    print(f"HN_SALVAGE_POST_CRT_REVIEWED|{len(target_cases.get(POST_CRT, []))}")
    print(f"HN_SALVAGE_DISTINCTION_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
