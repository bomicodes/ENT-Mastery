"""v23.2 — reconcile six Otology review-accounting gaps without duplicating cases.

The runtime ladder audit already shows complete foundation/application/senior
coverage for these canonical concepts. Their only gap is ladder_reviewed metadata.
This pass marks one structurally sound existing case per stage as deliberately
reviewed and refuses to bless weak or misaligned rows.
"""
DOMAIN="Otology / Neurotology"
TOPICS=(
    "Audiogram Interpretation",
    "Tympanometry / Acoustic Reflexes",
    "Vestibular Migraine",
    "Facial Paralysis",
    "Temporal Bone Fracture",
    "Cochlear Implant Candidacy",
)
STAGES=("foundation","application","senior_decision")


def _sound(q):
    choices=list(q.get("choices") or [])
    reasons=list(q.get("why_wrong") or [])
    try: answer=int(q.get("answer"))
    except (TypeError,ValueError): return False
    if len(choices)<4 or len(reasons)!=len(choices) or not 0<=answer<len(choices): return False
    if not str(q.get("stem") or "").strip() or not str(q.get("explanation") or "").strip(): return False
    if not str(reasons[answer]).strip().lower().startswith("correct."): return False
    # Reject the old generic placeholder rationale pattern rather than blessing it.
    joined=" ".join(str(x).lower() for x in reasons)
    if "use the mechanism, anatomy, and management priority" in joined: return False
    return True


def apply_otology_review_alignment_v232(challenges,item_id_fn):
    aligned=[]
    for topic in TOPICS:
        cid=item_id_fn(DOMAIN,topic)
        if not cid: raise RuntimeError("v232 missing canonical topic: "+topic)
        linked=[q for q in challenges if q.get("concept_id")==cid]
        for stage in STAGES:
            candidates=[q for q in linked if q.get("learning_stage")==stage and _sound(q)]
            if not candidates:
                raise RuntimeError(f"v232 no sound reusable {stage} case for {topic}")
            # Prefer a row already carrying richer board/call/OR framing.
            candidates.sort(key=lambda q:(0 if q.get("focus") in {"boards","OR_prep","overnight_call","postoperative_call"} else 1,
                                          -len(str(q.get("explanation") or "")),str(q.get("id") or "")))
            q=candidates[0]
            q["ladder_reviewed"]=True
            q["review_alignment_v232"]=True
            aligned.append(str(q.get("id")))
    return {"aligned":len(aligned),"topics":len(TOPICS),"ids":aligned}
