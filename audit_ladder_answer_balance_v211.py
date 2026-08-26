"""v21.1+ regression gate for batch-local learning-ladder answer diversity."""
from collections import Counter, defaultdict
import runtime_entry as rt

PREFIXES = ("v209_", "v210_", "v212_", "v213_", "v216_", "v218_", "v219_", "v220_", "v221_")
failures=[]
groups=defaultdict(list)
for q in rt.data.CLINICAL_CHALLENGES_V119:
    qid=str(q.get("id", ""))
    for prefix in PREFIXES:
        if qid.startswith(prefix) and q.get("ladder_reviewed"):
            groups[prefix].append(q)
            break

for prefix in PREFIXES:
    rows=groups.get(prefix, [])
    if len(rows) < 5:
        failures.append(f"{prefix}: expected at least 5 reviewed ladder rows, found {len(rows)}")
        continue
    counts=Counter()
    for q in rows:
        choices=list(q.get("choices") or [])
        reasons=list(q.get("why_wrong") or [])
        try: answer=int(q.get("answer"))
        except (TypeError,ValueError):
            failures.append(f"{q.get('id')}: invalid answer"); continue
        if not 0 <= answer < len(choices):
            failures.append(f"{q.get('id')}: answer out of range"); continue
        if len(reasons) != len(choices):
            failures.append(f"{q.get('id')}: rationale length mismatch"); continue
        if not str(reasons[answer]).strip().lower().startswith("correct."):
            failures.append(f"{q.get('id')}: correct rationale misaligned after balancing")
        counts[answer]+=1
    if len(counts) < 3:
        failures.append(f"{prefix}: only {len(counts)} answer positions used: {dict(counts)}")
    if counts and max(counts.values()) > (len(rows)+1)//2:
        failures.append(f"{prefix}: excessive answer-position concentration: {dict(counts)}")
    print(f"LADDER_BATCH_ANSWER_POSITIONS|{prefix}|{dict(sorted(counts.items()))}")

if failures:
    print("LADDER ANSWER-BALANCE FAILURES")
    print("\n".join(failures))
    raise SystemExit(1)
print("PASS: curated ladder batches retain aligned rationales and diverse answer positions")
