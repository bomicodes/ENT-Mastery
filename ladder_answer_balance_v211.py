"""v21.1+ — deterministic answer-position balancing for newly curated ladders."""
from collections import defaultdict
TARGET_PREFIXES=("v209_","v210_","v212_","v213_","v216_","v218_","v219_","v220_","v221_","v222_","v223_","v224_")
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
