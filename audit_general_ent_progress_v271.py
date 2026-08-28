"""v27.1 — strict General ENT / Emergencies 15-topic deliberate-ladder hard gate."""
from collections import defaultdict
import runtime_entry as rt

DOMAIN="General ENT / Emergencies"
STAGES={"foundation","application","senior_decision"}
PROTECTED_TOPICS=(
    "Postoperative Neck Hematoma",
    "Peritonsillar Abscess",
    "Deep Neck Abscess Drainage",
    "Caustic Ingestion",
    "Airway Foreign Body",
    "Chyle Leak",
    "Common ENT Consult Triage / Disposition",
    "ENT Perioperative Anesthesia / Difficult Airway Planning",
    "Esophageal Foreign Body",
    "Hemostasis / Coagulopathy / Antithrombotic Management in ENT",
    "Post-Tonsillectomy Hemorrhage",
    "Deep Neck Space Infection",
    "Tracheostomy Emergency",
    "Epistaxis",
    "Ludwig Angina",
)

def _quality_errors(q):
    errors=[]
    choices=list(q.get("choices") or [])
    reasons=list(q.get("why_wrong") or [])
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
    if len(canonical)!=32: failures.append(f"expected 32 canonical General ENT / Emergencies topics, found {len(canonical)}")
    if len(set(canonical))!=len(canonical): failures.append("duplicate canonical General ENT / Emergencies topic names")
    missing=sorted(set(PROTECTED_TOPICS)-set(canonical))
    if missing: failures.append(f"protected topics not exact canonical IDs: {missing}")
    by_cid=defaultdict(list); ids=[]
    for q in data.CLINICAL_CHALLENGES_V119:
        if q.get("id"): ids.append(str(q["id"]))
        if q.get("concept_id"): by_cid[q["concept_id"]].append(q)
    if len(ids)!=len(set(ids)): failures.append("duplicate clinical-challenge IDs detected")
    complete=0
    for topic in PROTECTED_TOPICS:
        cid=data._v6_item_id(DOMAIN,topic)
        if not cid:
            failures.append(f"{topic}: canonical ID lookup failed"); continue
        rows=[q for q in by_cid.get(cid,[]) if q.get("ladder_reviewed")]
        stages={q.get("learning_stage") for q in rows if q.get("learning_stage") in STAGES}
        if stages!=STAGES: failures.append(f"{topic}: missing stages {sorted(STAGES-stages)}")
        else: complete+=1
        for q in rows:
            if q.get("concept_id")!=cid: failures.append(f"{q.get('id')}: concept_id drift for {topic}")
            if not q.get("_coverage_reviewed_v211"): failures.append(f"{q.get('id')}: missing deliberate-review metadata")
            for err in _quality_errors(q): failures.append(f"{q.get('id')}: {err}")
    print(f"GENERAL_ENT_CANONICAL_TOPICS|{len(canonical)}")
    print(f"GENERAL_ENT_PROTECTED_TOPICS|{len(PROTECTED_TOPICS)}")
    print(f"GENERAL_ENT_PROTECTED_COMPLETE|{complete}")
    if failures:
        print("GENERAL ENT 15-TOPIC HARD-GATE FAILURES"); print("\n".join(failures)); raise SystemExit(1)
    print("PASS: 15 exact canonical General ENT / Emergencies topics retain complete reviewed ladders and quality contracts")

if __name__=="__main__": main()
