"""v26.7 — strict full-domain Sleep Surgery deliberate-ladder hard gate."""
from collections import defaultdict
import runtime_entry as rt

DOMAIN="Sleep Surgery"
STAGES={"foundation","application","senior_decision"}
PROTECTED_TOPICS=(
    "Adult PSG Interpretation",
    "DISE",
    "Hypoglossal Nerve Stimulation",
    "PAP Troubleshooting",
    "HNS Activation / Programming",
    "Palatal Surgery",
    "Tongue Base Surgery",
    "Maxillomandibular Advancement",
    "Residual OSA After Surgery",
    "HNS Troubleshooting / Nonresponse",
    "Pediatric PSG Interpretation",
    "Central Events / Hypoventilation",
    "Central Sleep Apnea / Treatment-Emergent CSA",
    "Sleep-Related Hypoventilation",
    "Positional OSA",
    "Circadian Rhythm Sleep-Wake Disorders",
    "Down Syndrome Pediatric HNS",
    "Lingual Tonsil / Tongue-Base Obstruction",
    "Narcolepsy / Central Hypersomnolence Recognition",
    "Palatal Surgery Selection for OSA",
    "Restless Legs / Periodic Limb Movement Disorders",
)


def _quality_errors(q):
    errors=[]; choices=list(q.get("choices") or []); reasons=list(q.get("why_wrong") or [])
    try: answer=int(q.get("answer"))
    except (TypeError,ValueError): return ["invalid answer"]
    if len(choices)<2: errors.append("fewer than 2 choices")
    if not 0<=answer<len(choices): errors.append("answer out of range")
    if len(reasons)!=len(choices): errors.append("rationale length mismatch")
    elif 0<=answer<len(reasons) and not str(reasons[answer]).strip().lower().startswith("correct."):
        errors.append("correct rationale not aligned")
    for field in ("stem","explanation","board_pearl","curveball"):
        if not str(q.get(field) or "").strip(): errors.append(f"blank {field}")
    if q.get("learning_stage") not in STAGES: errors.append("invalid or missing learning_stage")
    if not q.get("concept_id"): errors.append("missing concept_id")
    return errors


def main():
    data=rt.data
    canonical=[m.get("topic") for m in data.DEEP_MODULES_V6.get(DOMAIN,[]) if m.get("topic")]
    failures=[]
    if len(canonical)!=21: failures.append(f"expected 21 canonical Sleep Surgery topics, found {len(canonical)}")
    if len(set(canonical))!=len(canonical): failures.append("duplicate canonical Sleep Surgery topic names")
    missing_from_registry=sorted(set(PROTECTED_TOPICS)-set(canonical))
    extra_registry=sorted(set(canonical)-set(PROTECTED_TOPICS))
    if missing_from_registry: failures.append(f"protected topics not exact canonical IDs: {missing_from_registry}")
    if extra_registry: failures.append(f"canonical topics not protected by full Sleep gate: {extra_registry}")
    by_cid=defaultdict(list)
    ids=[]
    for q in data.CLINICAL_CHALLENGES_V119:
        qid=q.get("id")
        if qid: ids.append(str(qid))
        cid=q.get("concept_id")
        if cid: by_cid[cid].append(q)
    if len(ids)!=len(set(ids)): failures.append("duplicate clinical-challenge IDs detected")
    for topic in PROTECTED_TOPICS:
        cid=data._v6_item_id(DOMAIN,topic)
        if not cid:
            failures.append(f"{topic}: canonical ID lookup failed")
            continue
        rows=[q for q in by_cid.get(cid,[]) if q.get("ladder_reviewed")]
        stages={q.get("learning_stage") for q in rows if q.get("learning_stage") in STAGES}
        if stages!=STAGES: failures.append(f"{topic}: missing stages {sorted(STAGES-stages)}")
        for q in rows:
            if q.get("concept_id")!=cid: failures.append(f"{q.get('id')}: concept_id drift for {topic}")
            for err in _quality_errors(q): failures.append(f"{q.get('id')}: {err}")
    print(f"SLEEP_SURGERY_PROTECTED_TOPICS|{len(PROTECTED_TOPICS)}")
    print(f"SLEEP_SURGERY_CANONICAL_TOPICS|{len(canonical)}")
    if failures:
        print("SLEEP SURGERY FULL-DOMAIN FAILURES"); print("\n".join(failures)); raise SystemExit(1)
    print("PASS: all 21 exact canonical Sleep Surgery topics retain complete reviewed ladders and quality contracts")


if __name__=="__main__": main()