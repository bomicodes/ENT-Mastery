"""v27.4 — strict 32/32 General ENT / Emergencies deliberate-ladder completion gate."""
from collections import defaultdict
import runtime_entry as rt
DOMAIN="General ENT / Emergencies"
STAGES={"foundation","application","senior_decision"}
EXPECTED={
"Postoperative Neck Hematoma","Peritonsillar Abscess","Deep Neck Abscess Drainage","Caustic Ingestion","Airway Foreign Body",
"Chyle Leak","Common ENT Consult Triage / Disposition","ENT Perioperative Anesthesia / Difficult Airway Planning","Esophageal Foreign Body","Hemostasis / Coagulopathy / Antithrombotic Management in ENT",
"Post-Tonsillectomy Hemorrhage","Deep Neck Space Infection","Tracheostomy Emergency","Epistaxis","Ludwig Angina",
"Angioedema","Carotid Blowout Syndrome","Esophageal Perforation / Cervical Mediastinitis","Lemierre Syndrome","Immunocompromised Host in Otolaryngology",
"Cranial Nerve Examination / Skull Base Localization","ENT Imaging Fundamentals","ENT Fluids / Electrolytes / Nutrition","Pain Management in the Head & Neck Patient","Antimicrobial Stewardship in Otolaryngology",
"Wound Healing / Scar Biology in Head & Neck Surgery","Grafts / Implants / Biomaterials in ENT","Systemic / Granulomatous Disease Manifestations in ENT","Laser / Energy Safety in Otolaryngology","Evidence Interpretation / Outcomes Research","Geriatric Otolaryngology / Frailty","Oral Manifestations of Systemic Disease"}
def _quality(q):
 e=[]; choices=list(q.get("choices") or []); reasons=list(q.get("why_wrong") or [])
 try: a=int(q.get("answer"))
 except (TypeError,ValueError): return ["invalid answer"]
 if len(choices)<2:e.append("fewer than 2 choices")
 if not 0<=a<len(choices):e.append("answer out of range")
 if len(reasons)!=len(choices):e.append("rationale length mismatch")
 elif 0<=a<len(reasons) and not str(reasons[a]).strip().lower().startswith("correct."):e.append("correct rationale not aligned")
 for f in ("stem","explanation","board_pearl","curveball"):
  if not str(q.get(f) or "").strip(): e.append(f"blank {f}")
 if q.get("learning_stage") not in STAGES:e.append("invalid learning_stage")
 if not q.get("concept_id"):e.append("missing concept_id")
 return e
def main():
 d=rt.data; failures=[]
 canonical=[m.get("topic") for m in d.DEEP_MODULES_V6.get(DOMAIN,[]) if m.get("topic")]
 if len(canonical)!=32: failures.append(f"expected 32 canonical topics, found {len(canonical)}")
 if len(set(canonical))!=len(canonical): failures.append("duplicate canonical topic names")
 if set(canonical)!=EXPECTED:
  failures.append(f"canonical set drift; missing={sorted(EXPECTED-set(canonical))}; extra={sorted(set(canonical)-EXPECTED)}")
 bycid=defaultdict(list); ids=[]
 for q in d.CLINICAL_CHALLENGES_V119:
  if q.get("id"):ids.append(str(q["id"]))
  if q.get("concept_id"):bycid[q["concept_id"]].append(q)
 if len(ids)!=len(set(ids)): failures.append("duplicate clinical-challenge IDs detected")
 complete=0
 for topic in sorted(EXPECTED):
  cid=d._v6_item_id(DOMAIN,topic)
  if not cid: failures.append(f"{topic}: canonical ID lookup failed"); continue
  rows=[q for q in bycid.get(cid,[]) if q.get("ladder_reviewed")]
  stages={q.get("learning_stage") for q in rows if q.get("learning_stage") in STAGES}
  if stages!=STAGES: failures.append(f"{topic}: missing stages {sorted(STAGES-stages)}")
  else: complete+=1
  for q in rows:
   if q.get("concept_id")!=cid: failures.append(f"{q.get('id')}: concept drift")
   if not q.get("_coverage_reviewed_v211"): failures.append(f"{q.get('id')}: missing deliberate-review metadata")
   for err in _quality(q): failures.append(f"{q.get('id')}: {err}")
 print(f"GENERAL_ENT_CANONICAL_TOPICS|{len(canonical)}")
 print(f"GENERAL_ENT_REVIEWED_COMPLETE|{complete}")
 if failures:
  print("GENERAL ENT FULL-DOMAIN HARD-GATE FAILURES"); print("\n".join(failures)); raise SystemExit(1)
 print("PASS: General ENT / Emergencies retains exact 32/32 canonical reviewed foundation/application/senior-decision ladders")
if __name__=="__main__":main()
