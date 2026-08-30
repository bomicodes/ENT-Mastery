#!/usr/bin/env python3
"""v30.7 — hard-gate Oral Tongue SCC vs Base of Tongue SCC ladder semantics.

Protects the already-strong adaptive distinction between oral-cavity mobile-tongue
cancer and base-of-tongue oropharyngeal cancer without forcing filler questions.
The audit runs against the fully assembled runtime bank, after deterministic answer
balancing, so answer/why_wrong alignment and exact canonical linkage are checked in
production form.
"""

import sys
import runtime_entry as data

DOMAIN = "Head & Neck Oncology"
ORAL = "Oral Tongue SCC"
BOT = "Base of Tongue SCC"

EXPECTED = {
    ORAL: {
        "v219_hn_tongue_fnd": "foundation",
        "v219_hn_tongue_app": "application",
        "v219_hn_tongue_snr": "senior_decision",
    },
    BOT: {
        "v138_hn_02": "foundation",
        "v145_hn_02": "application",
        "v220_hn_bot_snr": "senior_decision",
    },
}


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def text(q):
    parts = [
        q.get("stem", ""), q.get("explanation", ""), q.get("board_pearl", ""),
        q.get("curveball", ""), *q.get("choices", []), *q.get("why_wrong", []),
    ]
    return " ".join(str(x) for x in parts).lower()


def teaching_text(q):
    # Exclude distractor text so anti-collapse checks do not punish a deliberately
    # wrong option that contrasts oral-cavity and HPV-mediated oropharyngeal logic.
    parts = [q.get("stem", ""), q.get("explanation", ""), q.get("board_pearl", "")]
    return " ".join(str(x) for x in parts).lower()


def contains_any(haystack, needles):
    return any(n.lower() in haystack for n in needles)


def main():
    failures = 0
    bank = list(data.CLINICAL_CHALLENGES_V119)
    by_id = {q.get("id"): q for q in bank if q.get("id")}

    ids = [q.get("id") for q in bank if q.get("id")]
    if len(ids) != len(set(ids)):
        failures += fail("duplicate vignette IDs exist in assembled runtime bank")

    topic_rows = {}
    for topic, expected_ids in EXPECTED.items():
        rows = []
        expected_concept = data._v6_item_id(DOMAIN, topic)
        for qid, stage in expected_ids.items():
            q = by_id.get(qid)
            if not q:
                failures += fail(f"{topic}: missing expected live vignette {qid}")
                continue
            rows.append(q)
            if q.get("domain") != DOMAIN or q.get("topic") != topic:
                failures += fail(f"{qid}: domain/topic drifted from {DOMAIN} / {topic}")
            if q.get("concept_id") != expected_concept:
                failures += fail(f"{qid}: canonical concept link drifted")
            if q.get("learning_stage") != stage:
                failures += fail(f"{qid}: expected learning_stage={stage}, got {q.get('learning_stage')}")
            if q.get("ladder_reviewed") is not True:
                failures += fail(f"{qid}: ladder_reviewed is not true")

            choices = q.get("choices") or []
            why = q.get("why_wrong") or []
            ans = q.get("answer")
            if len(choices) != 4:
                failures += fail(f"{qid}: expected four answer choices")
            if len(why) != len(choices):
                failures += fail(f"{qid}: why_wrong length no longer matches choices")
            if not isinstance(ans, int) or not 0 <= ans < len(choices):
                failures += fail(f"{qid}: invalid answer index after runtime balancing")
                continue
            if len(why) == len(choices):
                correct_flags = [i for i, r in enumerate(why) if str(r).strip().lower().startswith("correct")]
                if correct_flags != [ans]:
                    failures += fail(f"{qid}: answer/why_wrong alignment broke after deterministic shuffling")
                for i, rationale in enumerate(why):
                    if i != ans and len(str(rationale).split()) < 6:
                        failures += fail(f"{qid}: distractor {i} rationale is too shallow")
        topic_rows[topic] = rows

    for topic, rows in topic_rows.items():
        stages = {q.get("learning_stage") for q in rows}
        required = {"foundation", "application", "senior_decision"}
        if stages != required:
            failures += fail(f"{topic}: live reviewed ladder stages are {sorted(stages)}, expected {sorted(required)}")

    oral = " ".join(text(q) for q in topic_rows.get(ORAL, []))
    bot = " ".join(text(q) for q in topic_rows.get(BOT, []))
    oral_teaching = " ".join(teaching_text(q) for q in topic_rows.get(ORAL, []))
    bot_teaching = " ".join(teaching_text(q) for q in topic_rows.get(BOT, []))

    # Oral tongue must remain an oral-cavity depth/occult-neck/reconstruction ladder.
    oral_requirements = {
        "tissue diagnosis / biopsy": ["biopsy", "tissue diagnosis"],
        "depth of invasion": ["depth of invasion", "doi"],
        "occult/elective neck decision": ["occult", "elective treatment", "elective neck"],
        "functional mobile-tongue reconstruction": ["residual tongue mobility", "mobile-tongue defect", "bolus", "articulation"],
    }
    for label, needles in oral_requirements.items():
        if not contains_any(oral, needles):
            failures += fail(f"{ORAL}: lost {label} semantic anchor")

    # BOT must remain an HPV/p16 oropharyngeal, total-treatment-burden/function ladder.
    bot_requirements = {
        "p16/HPV oropharyngeal biology": ["p16", "hpv"],
        "oropharyngeal site identity": ["oropharynx", "oropharyngeal"],
        "multimodality treatment selection": ["transoral", "radiation", "treatment burden"],
        "swallowing/function": ["swallow", "functional tongue base", "functional burden"],
        "midline/bilateral neck behavior": ["crosses midline", "bilateral cervical", "bilateral nodal"],
    }
    for label, needles in bot_requirements.items():
        if not contains_any(bot, needles):
            failures += fail(f"{BOT}: lost {label} semantic anchor")

    # Fail if the central teaching logic collapses across subsites. Distractors are
    # intentionally excluded because they may correctly contrast the two diseases.
    if contains_any(oral_teaching, ["p16-positive staging", "hpv-mediated staging", "p16 status is central"]):
        failures += fail(f"{ORAL}: teaching target collapsed into HPV-mediated oropharyngeal staging")
    if contains_any(bot_teaching, ["depth of invasion predicts occult", "doi is a key driver of elective-neck"]):
        failures += fail(f"{BOT}: teaching target collapsed into oral-cavity DOI-driven neck logic")

    if failures:
        print(f"\nTongue-site semantic gate FAILED with {failures} issue(s).")
        return 1

    print("PASS: Oral Tongue SCC and Base of Tongue SCC remain semantically distinct in the live adaptive ladder.")
    print("  Oral tongue: biopsy/local extent -> DOI/occult neck -> functional mobile-tongue reconstruction")
    print("  Base of tongue: p16/HPV oropharynx -> multimodality selection -> total treatment burden/swallowing/bilateral neck")
    print("  Schema, canonical links, individualized rationales, and post-shuffle answer alignment are intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
