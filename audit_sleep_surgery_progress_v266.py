"""v26.8+ — strict full-domain Sleep Surgery deliberate-ladder hard gate.

Foundation, application, and senior-decision remain required for every protected topic.
A deliberately reviewed management stage is also valid when a concept has a distinct
perioperative/clinical management decision that should not be collapsed into application.
"""
from collections import defaultdict
import runtime_entry as rt
DOMAIN="Sleep Surgery"
REQUIRED_STAGES={"foundation","application","senior_decision"}
ALLOWED_STAGES=REQUIRED_STAGES|{"management"}
PROTECTED_TOPICS=("Adult PSG Interpretation","DISE","Hypoglossal Nerve Stimulation","PAP Troubleshooting","HNS Activation / Programming","Palatal Surgery","Tongue Base Surgery","Maxillomandibular Advancement","Residual OSA After Surgery","HNS Troubleshooting / Nonresponse","Pediatric PSG Interpretation","Central Events / Hypoventilation","Central Sleep Apnea / Treatment-Emergent CSA","Sleep-Related Hypoventilation","Positional OSA","Circadian Rhythm Sleep-Wake Disorders","Down Syndrome Pediatric HNS","Lingual Tonsil / Tongue-Base Obstruction","Narcolepsy / Central Hypersomnolence Recognition","Restless Legs / Periodic Limb Movement Disorders","Oral Appliance Therapy")
def _quality_errors(q):
 errors=[]; choices=list(q.get("choices") or []); reasons=list(q.get("why_wrong") or [])
 try: answer=int(q.get("answer"))
 except (TypeError,ValueError): return ["invalid answer"]
 if len(choices)<2: errors.append("fewer than 2 choices")
 if not 0<=answer<len(choices): errors.append("answer out of range")
 if len(reasons)!=len(choices): errors.append("rationale length mismatch")
 elif 0<=answer<len(reasons) and not str(reasons[answer]).strip().lower().startswith("correct."): errors.append("correct rationale not aligned")
 for field in ("stem","explanation","board_pearl","curveball"):
  if not str(q.get(field) or "").strip(): errors.append(f"blank {field}")
 if q.get("learning_stage") not in ALLOWED_STAGES: errors.append("invalid or missing learning_stage")
 if not q.get("concept_id"): errors.append("missing concept_id")
 return errors
def main():
 data=rt.data; canonical=[m.get("topic") for m in data.DEEP_MODULES_V6.get(DOMAIN,[]) if m.get("topic")]; failures=[]
 if len(canonical)!=21: failures.append(f"expected 21 canonical Sleep Surgery topics, found {len(canonical)}")
 if len(set(canonical))!=len(canonical): failures.append("duplicate canonical Sleep Surgery topic names")
 missing=sorted(set(PROTECTED_TOPICS)-set(canonical)); extra=sorted(set(canonical)-set(PROTECTED_TOPICS))
 if missing: failures.append(f"protected topics not exact canonical IDs: {missing}")
 if extra: failures.append(f"canonical topics not protected by full Sleep gate: {extra}")
 by_cid=defaultdict(list); ids=[]
 for q in data.CLINICAL_CHALLENGES_V119:
  if q.get("id"): ids.append(str(q["id"]))
  if q.get("concept_id"): by_cid[q["concept_id"]].append(q)
 if len(ids)!=len(set(ids)): failures.append("duplicate clinical-challenge IDs detected")
 for topic in PROTECTED_TOPICS:
  cid=data._v6_item_id(DOMAIN,topic)
  if not cid: failures.append(f"{topic}: canonical ID lookup failed"); continue
  rows=[q for q in by_cid.get(cid,[]) if q.get("ladder_reviewed")]
  stages={q.get("learning_stage") for q in rows if q.get("learning_stage") in ALLOWED_STAGES}
  if not REQUIRED_STAGES.issubset(stages): failures.append(f"{topic}: missing stages {sorted(REQUIRED_STAGES-stages)}")
  for q in rows:
   if q.get("concept_id")!=cid: failures.append(f"{q.get('id')}: concept_id drift for {topic}")
   for err in _quality_errors(q): failures.append(f"{q.get('id')}: {err}")
 print(f"SLEEP_SURGERY_PROTECTED_TOPICS|{len(PROTECTED_TOPICS)}"); print(f"SLEEP_SURGERY_CANONICAL_TOPICS|{len(canonical)}")
 if failures: print("SLEEP SURGERY FULL-DOMAIN FAILURES"); print("\n".join(failures)); raise SystemExit(1)
 print("PASS: all 21 exact canonical Sleep Surgery topics retain required foundation/application/senior ladders; deliberate management layers are quality-checked when present")
if __name__=="__main__": main()
