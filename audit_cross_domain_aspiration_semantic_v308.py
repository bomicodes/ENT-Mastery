#!/usr/bin/env python3
"""v30.8 — protect the H&N nonfunctional-larynx vs Laryngology radiation-dysphagia boundary.

Both ladders appropriately touch late radiation aspiration, but they should not collapse
into duplicate teaching. H&N owns end-stage functional salvage and irradiated operative/
reconstructive planning; Laryngology owns physiology localization, instrumental reassessment,
and the threshold for escalating to definitive aspiration prevention.
"""

import sys
import runtime_entry


data = runtime_entry.data
HN_DOMAIN = "Head & Neck Oncology"
HN_TOPIC = "Nonfunctional Larynx and Intractable Aspiration"
LAR_DOMAIN = "Laryngology / Voice / Swallowing"
LAR_TOPIC = "Radiation-Associated Dysphagia"

EXPECTED = {
    (HN_DOMAIN, HN_TOPIC): {
        "v231_hn_nfl_fnd": "foundation",
        "v231_hn_nfl_app": "application",
        "v231_hn_nfl_snr": "senior_decision",
    },
    (LAR_DOMAIN, LAR_TOPIC): {
        "v256_lar_rad_dys_fnd": "foundation",
        "v256_lar_rad_dys_app": "application",
        "v256_lar_rad_dys_snr": "senior_decision",
    },
}


def fail(msg):
    print("FAIL: " + msg)
    return 1


def full_text(q):
    parts = [q.get("stem", ""), q.get("explanation", ""), q.get("board_pearl", ""),
             q.get("curveball", ""), *q.get("choices", []), *q.get("why_wrong", [])]
    return " ".join(str(x) for x in parts).lower()


def teaching_text(q):
    # Exclude choices/why_wrong so anti-collapse checks do not punish a useful contrast.
    return " ".join(str(q.get(k, "")) for k in ("stem", "explanation", "board_pearl")).lower()


def has_any(text, needles):
    return any(n.lower() in text for n in needles)


def main():
    failures = 0
    bank = list(data.CLINICAL_CHALLENGES_V119)
    by_id = {q.get("id"): q for q in bank if q.get("id")}
    ids = [q.get("id") for q in bank if q.get("id")]
    if len(ids) != len(set(ids)):
        failures += fail("duplicate vignette IDs exist in assembled runtime bank")

    rows_by_topic = {}
    for (domain, topic), expected in EXPECTED.items():
        rows = []
        expected_cid = data._v6_item_id(domain, topic)
        if not expected_cid:
            failures += fail(f"{domain} / {topic}: canonical item ID is missing")
        for qid, stage in expected.items():
            q = by_id.get(qid)
            if not q:
                failures += fail(f"{domain} / {topic}: missing expected live vignette {qid}")
                continue
            rows.append(q)
            if q.get("domain") != domain or q.get("topic") != topic:
                failures += fail(f"{qid}: domain/topic drift")
            if q.get("concept_id") != expected_cid:
                failures += fail(f"{qid}: canonical concept linkage drift")
            if q.get("learning_stage") != stage:
                failures += fail(f"{qid}: expected learning_stage={stage}, got {q.get('learning_stage')}")
            if q.get("ladder_reviewed") is not True:
                failures += fail(f"{qid}: ladder_reviewed is not true")

            choices = list(q.get("choices") or [])
            reasons = list(q.get("why_wrong") or [])
            ans = q.get("answer")
            if len(choices) != 4:
                failures += fail(f"{qid}: expected four choices")
            if len(reasons) != len(choices):
                failures += fail(f"{qid}: why_wrong length mismatch")
            if not isinstance(ans, int) or not 0 <= ans < len(choices):
                failures += fail(f"{qid}: invalid answer index after runtime balancing")
                continue
            if len(reasons) == len(choices):
                correct = [i for i, r in enumerate(reasons) if str(r).strip().lower().startswith("correct")]
                if correct != [ans]:
                    failures += fail(f"{qid}: answer/why_wrong alignment broke after deterministic shuffling")
                for i, rationale in enumerate(reasons):
                    if i != ans and len(str(rationale).split()) < 6:
                        failures += fail(f"{qid}: distractor {i} rationale is too shallow")
        rows_by_topic[(domain, topic)] = rows
        stages = {q.get("learning_stage") for q in rows}
        required = {"foundation", "application", "senior_decision"}
        if stages != required:
            failures += fail(f"{domain} / {topic}: stages={sorted(stages)}, expected={sorted(required)}")

    hn_rows = rows_by_topic.get((HN_DOMAIN, HN_TOPIC), [])
    lar_rows = rows_by_topic.get((LAR_DOMAIN, LAR_TOPIC), [])
    hn = " ".join(full_text(q) for q in hn_rows)
    lar = " ".join(full_text(q) for q in lar_rows)
    hn_teaching = " ".join(teaching_text(q) for q in hn_rows)
    lar_teaching = " ".join(teaching_text(q) for q in lar_rows)

    hn_requirements = {
        "nonfunctional organ-preservation concept": ["nonfunctional larynx", "functionally useless", "organ preservation"],
        "refractory pulmonary aspiration threshold": ["recurrent aspiration pneumonia", "life-threatening", "pulmonary"],
        "functional laryngectomy/airway-separation option": ["total laryngectomy", "airway separation"],
        "irradiated operative risk": ["irradiated field", "fibrotic", "fistula"],
        "reconstructive planning": ["vascularized reconstruction", "flap reinforcement", "pharyngeal reconstruction"],
        "communication rehabilitation": ["speech rehabilitation", "alaryngeal communication", "voice restoration"],
    }
    for label, needles in hn_requirements.items():
        if not has_any(hn, needles):
            failures += fail(f"{HN_TOPIC}: lost {label} semantic anchor")

    lar_requirements = {
        "late radiation mechanism": ["fibrosis", "neuromuscular", "sensory"],
        "instrumental physiology localization": ["fees", "modified barium swallow", "instrumental"],
        "structural/oncologic reassessment": ["recurrent tumor", "structural recurrence", "stenosis"],
        "feeding tube limitation": ["does not prevent aspiration", "does not stop aspiration", "secretion aspiration"],
        "selective aspiration-prevention escalation": ["aspiration-prevention", "definitive aspiration-control"],
        "goals and irreversibility": ["irreversible", "patient priorities", "goals-of-care"],
    }
    for label, needles in lar_requirements.items():
        if not has_any(lar, needles):
            failures += fail(f"{LAR_TOPIC}: lost {label} semantic anchor")

    # H&N must not degrade into a generic test-selection ladder; Laryngology must not
    # become a duplicate irradiated-laryngectomy reconstruction-planning ladder.
    if has_any(hn_teaching, ["fees and/or modified barium swallow chosen to phenotype", "choose fees versus modified barium"]):
        failures += fail(f"{HN_TOPIC}: teaching target collapsed into Laryngology test-selection logic")
    if has_any(lar_teaching, ["plan vascularized reconstruction", "primary flap reinforcement", "pharyngeal reconstruction in an irradiated field"]):
        failures += fail(f"{LAR_TOPIC}: teaching target collapsed into H&N functional-laryngectomy reconstruction logic")

    if failures:
        print(f"\nCross-domain aspiration semantic gate FAILED with {failures} issue(s).")
        return 1

    print("PASS: late-radiation aspiration ladders remain complementary rather than duplicative.")
    print("  H&N: nonfunctional larynx -> failed conservative safety endpoint -> functional salvage laryngectomy/reconstruction planning")
    print("  Laryngology: late-radiation physiology -> instrumental/structural reassessment -> selective aspiration-prevention escalation")
    print("  Canonical links, explicit stages, individualized rationales, and post-shuffle answer alignment are intact.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
