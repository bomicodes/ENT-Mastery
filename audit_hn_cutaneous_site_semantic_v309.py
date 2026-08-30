#!/usr/bin/env python3
"""v30.9 — hard-gate head/neck cutaneous SCC vs BCC adaptive ladder semantics.

The v30.8 Concept Hub rebuild deliberately separates cSCC's perineural/regional
metastatic-risk pathway from BCC's local margin-control/tissue-preservation pathway.
This audit verifies that the *live reviewed adaptive questions* preserve that same
clinical distinction after runtime assembly and deterministic answer balancing.
"""

import sys
import runtime_entry


data = runtime_entry.data
DOMAIN = "Head & Neck Oncology"
CSCC = "Cutaneous Squamous Cell Carcinoma of the Head & Neck"
BCC = "Basal Cell Carcinoma of the Head & Neck"
REQUIRED_STAGES = {"foundation", "application", "senior_decision"}


def fail(msg):
    print(f"FAIL: {msg}")
    return 1


def joined(rows, include_distractors=True):
    fields = []
    for q in rows:
        fields.extend([q.get("stem", ""), q.get("explanation", ""), q.get("board_pearl", ""), q.get("curveball", "")])
        if include_distractors:
            fields.extend(q.get("choices") or [])
            fields.extend(q.get("why_wrong") or [])
    return " ".join(str(x) for x in fields).lower()


def any_term(text, terms):
    return any(term.lower() in text for term in terms)


def main():
    failures = 0
    bank = list(data.CLINICAL_CHALLENGES_V119)
    ids = [q.get("id") for q in bank if q.get("id")]
    if len(ids) != len(set(ids)):
        failures += fail("duplicate vignette IDs exist in assembled runtime bank")

    rows_by_topic = {}
    for topic in (CSCC, BCC):
        concept_id = data._v6_item_id(DOMAIN, topic)
        rows = [q for q in bank if q.get("concept_id") == concept_id and q.get("ladder_reviewed") is True]
        rows_by_topic[topic] = rows
        if not rows:
            failures += fail(f"{topic}: no reviewed adaptive questions linked to canonical concept")
            continue

        stages = {q.get("learning_stage") for q in rows}
        missing = REQUIRED_STAGES - stages
        if missing:
            failures += fail(f"{topic}: missing reviewed stages {sorted(missing)}")

        for q in rows:
            qid = q.get("id", "<missing-id>")
            if q.get("domain") != DOMAIN or q.get("topic") != topic:
                failures += fail(f"{qid}: domain/topic drifted from {DOMAIN} / {topic}")
            if q.get("concept_id") != concept_id:
                failures += fail(f"{qid}: canonical concept link drifted")
            if q.get("learning_stage") not in REQUIRED_STAGES | {"management"}:
                failures += fail(f"{qid}: unexpected learning_stage={q.get('learning_stage')}")

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

    cscc = joined(rows_by_topic.get(CSCC, []))
    bcc = joined(rows_by_topic.get(BCC, []))
    cscc_teaching = joined(rows_by_topic.get(CSCC, []), include_distractors=False)
    bcc_teaching = joined(rows_by_topic.get(BCC, []), include_distractors=False)

    cscc_requirements = {
        "perineural-risk reasoning": ["perineural", "named nerve", "cranial nerve"],
        "regional metastatic-risk reasoning": ["parotid", "nodal", "neck metast", "regional"],
        "risk-directed escalation": ["high-risk", "adjuvant radiation", "skull base", "therapeutic neck", "parotidectomy"],
    }
    for label, terms in cscc_requirements.items():
        if not any_term(cscc, terms):
            failures += fail(f"{CSCC}: lost {label} semantic anchor")

    bcc_requirements = {
        "margin-control/local-control reasoning": ["mohs", "margin", "local control", "complete margin"],
        "facial tissue/function preservation": ["tissue", "reconstruct", "eyelid", "nose", "facial"],
        "non-routine regional staging distinction": ["rare", "metasta", "neck dissection", "parotid"],
    }
    for label, terms in bcc_requirements.items():
        if not any_term(bcc, terms):
            failures += fail(f"{BCC}: lost {label} semantic anchor")

    # Teaching targets—not distractors—must not collapse into the neighboring pathway.
    if any_term(bcc_teaching, ["routine elective neck dissection", "routine parotidectomy", "common parotid metastasis"]):
        failures += fail(f"{BCC}: teaching target collapsed into routine cSCC-style regional treatment")
    if any_term(cscc_teaching, ["metastasis is extraordinarily uncommon", "nodal staging is unnecessary in high-risk disease"]):
        failures += fail(f"{CSCC}: teaching target collapsed into BCC-style purely local behavior")

    if failures:
        print(f"\nCutaneous-site semantic gate FAILED with {failures} issue(s).")
        return 1

    print("PASS: cSCC and BCC remain semantically distinct in the live adaptive ladder.")
    print("  cSCC: perineural risk + parotid/neck metastatic risk + risk-directed escalation")
    print("  BCC: local/margin control + facial tissue preservation + exceptional regional spread")
    print("  Canonical links, learning stages, individualized rationales, and post-shuffle alignment are intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
