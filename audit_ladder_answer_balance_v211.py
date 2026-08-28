"""v21.1+ regression gate for batch-local learning-ladder answer diversity."""
from collections import Counter,defaultdict
import runtime_entry as rt
PREFIXES=("v209_","v210_","v212_","v213_","v216_","v218_","v219_","v220_","v221_","v222_","v223_","v224_","v225_","v227_","v228_","v231_","v233_","v234_","v235_","v236_","v237_","v238_","v239_","v241_","v242_","v243_","v244_","v245_","v246_","v247_","v248_","v249_","v251_","v252_","v253_","v254_","v255_","v256_","v257_","v258_","v259_","v260_","v261_","v262_","v263_","v264_","v266_","v267_","v268_","v269_","v270_","v271_","v272_")
MIN_ROWS={"v224_":2,"v268_":3}
failures=[]; groups=defaultdict(list)
for q in rt.data.CLINICAL_CHALLENGES_V119:
 qid=str(q.get("id", ""))
 for prefix in PREFIXES:
  if qid.startswith(prefix) and q.get("ladder_reviewed"): groups[prefix].append(q); break
for prefix in PREFIXES:
 rows=groups.get(prefix,[]); min_rows=MIN_ROWS.get(prefix,5)
 if len(rows)<min_rows: failures.append(f"{prefix}: expected at least {min_rows} reviewed ladder rows, found {len(rows)}"); continue
 counts=Counter()
 for q in rows:
  choices=list(q.get("choices") or []); reasons=list(q.get("why_wrong") or [])
  try: answer=int(q.get("answer"))
  except (TypeError,ValueError): failures.append(f"{q.get('id')}: invalid answer"); continue
  if not 0<=answer<len(choices): failures.append(f"{q.get('id')}: answer out of range"); continue
  if len(reasons)!=len(choices): failures.append(f"{q.get('id')}: rationale length mismatch"); continue
  if not str(reasons[answer]).strip().lower().startswith("correct."): failures.append(f"{q.get('id')}: correct rationale misaligned after balancing")
  counts[answer]+=1
 required_positions=2 if prefix=="v224_" else 3
 if len(counts)<required_positions: failures.append(f"{prefix}: only {len(counts)} answer positions used: {dict(counts)}")
 if prefix not in {"v224_","v268_"} and counts and max(counts.values())>(len(rows)+1)//2: failures.append(f"{prefix}: excessive answer-position concentration: {dict(counts)}")
 print(f"LADDER_BATCH_ANSWER_POSITIONS|{prefix}|{dict(sorted(counts.items()))}")
if failures:
 print("LADDER ANSWER-BALANCE FAILURES"); print("\n".join(failures)); raise SystemExit(1)
print("PASS: curated ladder batches retain aligned rationales and diverse answer positions")
