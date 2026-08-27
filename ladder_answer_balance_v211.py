"""v21.1+ — deterministic answer-position balancing for newly curated ladders.

v23.1 chains the final H&N closure immediately before balancing. v23.2 then
reconciles six Otology topics whose three-stage coverage already existed but
lacked deliberate-review metadata; only structurally sound reusable cases are
marked reviewed. v23.3-v23.4 begin deliberate Thyroid/Parathyroid/Salivary review.
"""
from collections import defaultdict
from vignette_ladders_v231 import apply_learning_ladders_v231
from otology_review_alignment_v232 import apply_otology_review_alignment_v232
from vignette_ladders_v233 import apply_learning_ladders_v233
from vignette_ladders_v234 import apply_learning_ladders_v234

TARGET_PREFIXES=("v209_","v210_","v212_","v213_","v216_","v218_","v219_","v220_","v221_","v222_","v223_","v224_","v225_","v227_","v228_","v231_","v233_","v234_")

def _prefix(qid):
    text=str(qid or "")
    for prefix in TARGET_PREFIXES:
        if text.startswith(prefix): return prefix
    return None

def _move_answer(q,target):
    choices=list(q.get("choices") or []); reasons=list(q.get("why_wrong") or [])
    if len(choices)<2 or len(reasons)!=len(choices): return False
    try: answer=int(q.get("answer"))
    except (TypeError,ValueError): return False
    if not 0<=answer<len(choices): return False
    target%=len(choices)
    if answer==target: return False
    choice=choices.pop(answer); reason=reasons.pop(answer)
    choices.insert(target,choice); reasons.insert(target,reason)
    q["choices"]=choices; q["why_wrong"]=reasons; q["answer"]=target
    return True

def apply_ladder_answer_balance_v211(challenges):
    # data.py is already fully initialized by runtime_entry before this hook.
    import data
    apply_learning_ladders_v231(challenges, data._v6_item_id)
    apply_otology_review_alignment_v232(challenges, data._v6_item_id)
    apply_learning_ladders_v233(challenges, data._v6_item_id)
    apply_learning_ladders_v234(challenges, data._v6_item_id)

    groups=defaultdict(list)
    for q in challenges:
        if not q.get("ladder_reviewed"): continue
        prefix=_prefix(q.get("id"))
        if prefix and q.get("learning_stage") in {"foundation","application","senior_decision"}: groups[prefix].append(q)
    moved=0; summary={}
    for prefix,rows in sorted(groups.items()):
        rows.sort(key=lambda q:str(q.get("id")))
        for i,q in enumerate(rows):
            n=len(q.get("choices") or [])
            if n: moved+=int(_move_answer(q,i%n))
        counts=defaultdict(int)
        for q in rows:
            try: counts[int(q.get("answer"))]+=1
            except (TypeError,ValueError): pass
        summary[prefix]=dict(sorted(counts.items()))
    return {"moved":moved,"groups":summary}