"""v29.7 hard gate — conventional allergic rhinitis vs local allergic rhinitis.

Protects the educational distinction between systemic IgE-mediated AR and LAR after
answer-position balancing.  In particular, negative routine systemic tests must not
be allowed to become a stand-alone LAR diagnosis; the application ladder must teach
the local nasal allergen-response confirmation step.
"""
from collections import Counter

import runtime_entry as rt

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPICS = ("Allergic Rhinitis", "Local Allergic Rhinitis")
TARGET_ID = "v212_rhi_lar_app"
STAGES = {"foundation", "application", "senior_decision"}


def _text(q):
    prose = " ".join(
        str(q.get(k) or "")
        for k in ("stem", "explanation", "board_pearl", "curveball")
    )
    choices = " ".join(str(x) for x in (q.get("choices") or []))
    reasons = " ".join(str(x) for x in (q.get("why_wrong") or []))
    return f"{prose} {choices} {reasons}".lower()


def main():
    cases = list(rt.data.CLINICAL_CHALLENGES_V119)
    failures = []

    ids = [q.get("id") for q in cases if q.get("id")]
    dupes = [qid for qid, n in Counter(ids).items() if n > 1]
    if dupes:
        failures.append("duplicate vignette IDs: " + ",".join(sorted(dupes)))

    by_topic = {topic: [] for topic in TOPICS}
    for q in cases:
        if q.get("domain") == DOMAIN and q.get("topic") in by_topic:
            by_topic[q["topic"]].append(q)

    for topic, rows in by_topic.items():
        cid = rt.data._v6_item_id(DOMAIN, topic)
        reviewed = [q for q in rows if q.get("ladder_reviewed")]
        stages = {q.get("learning_stage") for q in reviewed}
        missing = STAGES - stages
        if missing:
            failures.append(f"{topic}: missing deliberate stages {sorted(missing)}")
        for q in reviewed:
            if q.get("concept_id") != cid:
                failures.append(f"{q.get('id')}: bad canonical concept link")
            choices = list(q.get("choices") or [])
            reasons = list(q.get("why_wrong") or [])
            try:
                answer = int(q.get("answer"))
            except (TypeError, ValueError):
                failures.append(f"{q.get('id')}: invalid answer index")
                continue
            if not 0 <= answer < len(choices):
                failures.append(f"{q.get('id')}: answer index out of range")
            elif len(reasons) != len(choices):
                failures.append(f"{q.get('id')}: why_wrong length mismatch")
            elif not str(reasons[answer]).strip().lower().startswith("correct."):
                failures.append(f"{q.get('id')}: correct rationale misaligned after balancing")

    target = next((q for q in cases if q.get("id") == TARGET_ID), None)
    if target is None:
        failures.append(f"missing {TARGET_ID}")
    else:
        if not target.get("semantic_review_v297"):
            failures.append(f"{TARGET_ID}: missing semantic_review_v297 metadata")
        text = _text(target)
        for anchor in ("nasal allergen challenge", "negative routine systemic", "nasal specific-ige", "limited sensitivity"):
            if anchor not in text:
                failures.append(f"{TARGET_ID}: missing LAR confirmation anchor {anchor!r}")
        if "sinus ct" not in text or "immunotherapy" not in text:
            failures.append(f"{TARGET_ID}: missing individualized CT/immunotherapy distractor reasoning")

    lar_senior = next((q for q in by_topic["Local Allergic Rhinitis"] if q.get("id") == "v212_rhi_lar_snr"), None)
    if lar_senior is None:
        failures.append("missing v212_rhi_lar_snr")
    else:
        senior_text = _text(lar_senior)
        if not all(anchor in senior_text for anchor in ("cold air", "nonallergic")):
            failures.append("v212_rhi_lar_snr no longer preserves nonallergic/neurogenic discrimination")

    ar_found = next((q for q in by_topic["Allergic Rhinitis"] if q.get("id") == "v212_rhi_ar_found"), None)
    if ar_found is None:
        failures.append("missing v212_rhi_ar_found")
    else:
        ar_text = _text(ar_found)
        if not all(anchor in ar_text for anchor in ("sneezing", "itch", "season")):
            failures.append("v212_rhi_ar_found no longer preserves conventional AR phenotype recognition")

    if failures:
        print("RHINOLOGY RHINITIS SEMANTIC v29.7 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print("PASS: AR and LAR retain distinct recognition, confirmation, and senior differential decisions with aligned rationales")


if __name__ == "__main__":
    main()
