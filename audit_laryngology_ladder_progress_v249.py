"""v24.9 — Laryngology / Voice / Swallowing deliberate-review progress gate.

Protects the first five exact canonical Laryngology topics. Progress is counted
only by canonical concept_id linkage plus ladder_reviewed metadata and all three
required learning stages. This is intentionally a progress gate, not a claim
that the 36-topic domain is complete.
"""
from collections import defaultdict
import runtime_entry as rt

DOMAIN="Laryngology / Voice / Swallowing"
STAGES={"foundation","application","senior_decision"}
PROTECTED_TOPICS=(
    "Unilateral Vocal Fold Paralysis",
    "Dysphagia / Aspiration",
    "Bilateral Vocal Fold Immobility",
    "Subglottic / Tracheal Stenosis",
    "Laryngeal Anatomy",
)


def main():
    data=rt.data
    canonical=[m.get("topic") for m in data.DEEP_MODULES_V6.get(DOMAIN,[]) if m.get("topic")]
    failures=[]
    if len(canonical)!=len(set(canonical)):
        failures.append("duplicate canonical topic names in Laryngology registry")
    for topic in PROTECTED_TOPICS:
        if topic not in canonical:
            failures.append(f"protected topic absent from canonical registry: {topic}")

    by_cid=defaultdict(list)
    for q in data.CLINICAL_CHALLENGES_V119:
        cid=q.get("concept_id")
        if cid:
            by_cid[cid].append(q)

    for topic in PROTECTED_TOPICS:
        cid=data._v6_item_id(DOMAIN,topic)
        rows=[q for q in by_cid.get(cid,[]) if q.get("ladder_reviewed")]
        stages={q.get("learning_stage") for q in rows if q.get("learning_stage") in STAGES}
        missing=STAGES-stages
        print(f"LARYNGOLOGY_PROGRESS|{topic}|concept_id={cid}|reviewed_cases={len(rows)}|stages={','.join(sorted(stages))}")
        if missing:
            failures.append(f"{topic}: missing reviewed stages {','.join(sorted(missing))}")
        for q in rows:
            choices=list(q.get("choices") or [])
            reasons=list(q.get("why_wrong") or [])
            try: answer=int(q.get("answer"))
            except (TypeError,ValueError):
                failures.append(f"{q.get('id')}: invalid answer"); continue
            if len(choices)<2 or len(reasons)!=len(choices) or not 0<=answer<len(choices):
                failures.append(f"{q.get('id')}: malformed choices/rationales/answer"); continue
            if not str(reasons[answer]).strip().lower().startswith("correct."):
                failures.append(f"{q.get('id')}: correct rationale is not aligned")
            if not str(q.get("explanation") or "").strip():
                failures.append(f"{q.get('id')}: missing explanation")
            if not str(q.get("board_pearl") or "").strip():
                failures.append(f"{q.get('id')}: missing board pearl")
            if not str(q.get("curveball") or "").strip():
                failures.append(f"{q.get('id')}: missing curveball")

    print(f"LARYNGOLOGY_PROTECTED_TOPICS|{len(PROTECTED_TOPICS)}")
    print(f"LARYNGOLOGY_CANONICAL_TOPICS|{len(canonical)}")
    if failures:
        print("LARYNGOLOGY PROGRESS GATE FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: first 5 canonical Laryngology topics retain complete deliberate-review ladders")


if __name__=="__main__":
    main()
