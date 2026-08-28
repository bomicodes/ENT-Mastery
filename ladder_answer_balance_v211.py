"""v21.1+ — deterministic answer-position balancing for newly curated ladders.

Completed domains are chained immediately before balancing. v26.8 completes
Sleep Surgery; v26.9-v27.0 advance exact-canonical General ENT / Emergencies review.
"""
from collections import defaultdict
from vignette_ladders_v231 import apply_learning_ladders_v231
from otology_review_alignment_v232 import apply_otology_review_alignment_v232
from vignette_ladders_v233 import apply_learning_ladders_v233
from vignette_ladders_v234 import apply_learning_ladders_v234
from vignette_ladders_v235 import apply_learning_ladders_v235
from vignette_ladders_v235_fix import apply_learning_ladders_v235_fix
from vignette_ladders_v236 import apply_learning_ladders_v236
from vignette_ladders_v237 import apply_learning_ladders_v237
from vignette_ladders_v238 import apply_learning_ladders_v238
from vignette_ladders_v239 import apply_learning_ladders_v239
from tps_final_alignment_v240 import apply_tps_final_alignment_v240
from vignette_ladders_v241 import apply_learning_ladders_v241
from vignette_ladders_v242 import apply_learning_ladders_v242
from vignette_ladders_v243 import apply_learning_ladders_v243
from vignette_ladders_v244 import apply_learning_ladders_v244
from vignette_ladders_v245 import apply_learning_ladders_v245
from vignette_ladders_v246 import apply_learning_ladders_v246
from vignette_ladders_v247 import apply_learning_ladders_v247
from vignette_ladders_v248 import apply_learning_ladders_v248
from vignette_ladders_v249 import apply_learning_ladders_v249
from vignette_ladders_v251 import apply_learning_ladders_v251
from vignette_ladders_v252 import apply_learning_ladders_v252
from vignette_ladders_v253 import apply_learning_ladders_v253
from vignette_ladders_v254 import apply_learning_ladders_v254
from vignette_ladders_v255 import apply_learning_ladders_v255
from vignette_ladders_v256 import apply_learning_ladders_v256
from vignette_ladders_v257 import apply_learning_ladders_v257
from vignette_ladders_v258 import apply_learning_ladders_v258
from vignette_ladders_v259 import apply_learning_ladders_v259
from vignette_ladders_v260 import apply_learning_ladders_v260
from vignette_ladders_v261 import apply_learning_ladders_v261
from vignette_ladders_v262 import apply_learning_ladders_v262
from vignette_ladders_v263 import apply_learning_ladders_v263
from vignette_ladders_v264 import apply_learning_ladders_v264
from vignette_ladders_v266 import apply_learning_ladders_v266
from vignette_ladders_v267 import apply_learning_ladders_v267
from vignette_ladders_v268 import apply_learning_ladders_v268
from vignette_ladders_v269 import apply_learning_ladders_v269
from vignette_ladders_v270 import apply_learning_ladders_v270
from vignette_ladders_v270_fix import apply_general_ent_v270_quality_fix
from laryngology_foundation_alignment_v252 import apply_laryngology_foundation_alignment_v252
TARGET_PREFIXES=("v209_","v210_","v212_","v213_","v216_","v218_","v219_","v220_","v221_","v222_","v223_","v224_","v225_","v227_","v228_","v231_","v233_","v234_","v235_","v236_","v237_","v238_","v239_","v241_","v242_","v243_","v244_","v245_","v246_","v247_","v248_","v249_","v251_","v252_","v253_","v254_","v255_","v256_","v257_","v258_","v259_","v260_","v261_","v262_","v263_","v264_","v266_","v267_","v268_","v269_","v270_")
def _prefix(qid):
 text=str(qid or "")
 for prefix in TARGET_PREFIXES:
  if text.startswith(prefix): return prefix
 return None
def _normalize_correct_rationale(reasons,answer):
 if 0<=answer<len(reasons):
  text=str(reasons[answer] or "")
  if text.startswith("Correct:"): reasons[answer]="Correct."+text[len("Correct:"):]
def _move_answer(q,target):
 choices=list(q.get("choices") or []); reasons=list(q.get("why_wrong") or [])
 if len(choices)<2 or len(reasons)!=len(choices): return False
 try: answer=int(q.get("answer"))
 except (TypeError,ValueError): return False
 if not 0<=answer<len(choices): return False
 _normalize_correct_rationale(reasons,answer); target%=len(choices)
 if answer==target: q["why_wrong"]=reasons; return False
 choice=choices.pop(answer); reason=reasons.pop(answer); choices.insert(target,choice); reasons.insert(target,reason)
 q["choices"]=choices; q["why_wrong"]=reasons; q["answer"]=target; return True
def apply_ladder_answer_balance_v211(challenges):
 import data
 for fn in (apply_learning_ladders_v231,apply_learning_ladders_v233,apply_learning_ladders_v234,apply_learning_ladders_v235,apply_learning_ladders_v235_fix,apply_learning_ladders_v236,apply_learning_ladders_v237,apply_learning_ladders_v238,apply_learning_ladders_v239): fn(challenges,data._v6_item_id)
 apply_otology_review_alignment_v232(challenges,data._v6_item_id); apply_tps_final_alignment_v240(challenges,data._v6_item_id)
 for fn in (apply_learning_ladders_v241,apply_learning_ladders_v242,apply_learning_ladders_v243,apply_learning_ladders_v244,apply_learning_ladders_v245,apply_learning_ladders_v246,apply_learning_ladders_v247,apply_learning_ladders_v248,apply_learning_ladders_v249,apply_learning_ladders_v251,apply_learning_ladders_v252): fn(challenges,data._v6_item_id)
 apply_laryngology_foundation_alignment_v252(challenges,data._v6_item_id)
 for fn in (apply_learning_ladders_v253,apply_learning_ladders_v254,apply_learning_ladders_v255,apply_learning_ladders_v256,apply_learning_ladders_v257,apply_learning_ladders_v258,apply_learning_ladders_v259,apply_learning_ladders_v260,apply_learning_ladders_v261,apply_learning_ladders_v262,apply_learning_ladders_v263,apply_learning_ladders_v264,apply_learning_ladders_v266,apply_learning_ladders_v267,apply_learning_ladders_v268,apply_learning_ladders_v269,apply_learning_ladders_v270): fn(challenges,data._v6_item_id)
 apply_general_ent_v270_quality_fix(challenges)
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
