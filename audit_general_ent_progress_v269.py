"""v26.9 — General ENT / Emergencies deliberate-ladder progress gate."""
from collections import defaultdict
import runtime_entry as rt
DOMAIN="General ENT / Emergencies"; STAGES={"foundation","application","senior_decision"}
PROTECTED=("Postoperative Neck Hematoma","Peritonsillar Abscess","Deep Neck Abscess Drainage","Caustic Ingestion","Airway Foreign Body")
def main():
 data=rt.data; failures=[]; canonical={m.get("topic") for m in data.DEEP_MODULES_V6.get(DOMAIN,[]) if m.get("topic")}; by=defaultdict(list); ids=[]
 for q in data.CLINICAL_CHALLENGES_V119:
  if q.get("id"): ids.append(str(q["id"]))
  if q.get("concept_id"): by[q["concept_id"]].append(q)
 if len(ids)!=len(set(ids)): failures.append("duplicate clinical challenge IDs")
 for topic in PROTECTED:
  if topic not in canonical: failures.append(f"noncanonical protected topic: {topic}"); continue
  cid=data._v6_item_id(DOMAIN,topic); rows=[q for q in by.get(cid,[]) if q.get("ladder_reviewed")]; stages={q.get("learning_stage") for q in rows}
  if not STAGES.issubset(stages): failures.append(f"{topic}: missing stages {sorted(STAGES-stages)}")
  for q in rows:
   choices=list(q.get("choices") or []); reasons=list(q.get("why_wrong") or [])
   try: ans=int(q.get("answer"))
   except Exception: failures.append(f"{q.get('id')}: invalid answer"); continue
   if not 0<=ans<len(choices): failures.append(f"{q.get('id')}: answer out of range")
   if len(reasons)!=len(choices): failures.append(f"{q.get('id')}: rationale mismatch")
   elif not str(reasons[ans]).strip().lower().startswith("correct."): failures.append(f"{q.get('id')}: correct rationale misaligned")
   if q.get("concept_id")!=cid: failures.append(f"{q.get('id')}: concept drift")
 print(f"GENERAL_ENT_CANONICAL_TOPICS|{len(canonical)}"); print(f"GENERAL_ENT_PROTECTED_TOPICS|{len(PROTECTED)}")
 if failures: print("GENERAL ENT PROGRESS FAILURES"); print("\n".join(failures)); raise SystemExit(1)
 print("PASS: General ENT pass 1 preserves five exact canonical three-stage ladders")
if __name__=="__main__": main()
