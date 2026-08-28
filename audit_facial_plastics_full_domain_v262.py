"""v26.2 — strict full-domain Facial Plastics / Trauma deliberate-ladder gate."""
from collections import defaultdict
import runtime_entry as rt

DOMAIN="Facial Plastics / Trauma"
STAGES={"foundation","application","senior_decision"}
PROTECTED_TOPICS=(
    "Structured Facial Trauma Examination","ZMC / Orbital Trauma","Mandible Fracture","Nasal Fracture","Septal Hematoma",
    "NOE Fracture","Frontal Sinus Fracture","Le Fort / Panfacial Trauma","Mandibular Biomechanics and Occlusion","Facial Soft-Tissue Lacerations / Burns",
    "Local Flap Reconstruction","Mohs Defect Reconstruction","Bilobed Flap","Cervicofacial Flap","Skin Graft Selection",
    "Functional Nasal Obstruction","Functional Septorhinoplasty","Open Rhinoplasty Fundamentals","Rhinoplasty Tip Mechanics","Rhinoplasty Graft Selection",
    "Facial Nerve Reanimation","Facial Synkinesis / Static-Dynamic Rehabilitation","Scar Management","Periocular Reconstruction","Forehead Flap / Nasal Reconstruction",
    "Otoplasty","Septal Perforation","Auricular Reconstruction","Alar Retraction / Nasal Vestibular Stenosis","Aesthetic Facial Analysis",
    "Aging Face / Injectables / Resurfacing","Hair Restoration Fundamentals",
)

def _quality_errors(q):
    errors=[]; choices=list(q.get("choices") or []); reasons=list(q.get("why_wrong") or [])
    try: answer=int(q.get("answer"))
    except (TypeError,ValueError): return ["invalid answer"]
    if len(choices)<2: errors.append("fewer than 2 choices")
    if not 0<=answer<len(choices): errors.append("answer out of range")
    if len(reasons)!=len(choices): errors.append("rationale length mismatch")
    elif 0<=answer<len(reasons) and not str(reasons[answer]).strip().lower().startswith("correct."):
        errors.append("correct rationale not aligned")
    for field in ("stem","explanation","board_pearl","curveball"):
        if not str(q.get(field) or "").strip(): errors.append(f"blank {field}")
    return errors

def main():
    data=rt.data
    canonical=[m.get("topic") for m in data.DEEP_MODULES_V6.get(DOMAIN,[]) if m.get("topic")]
    failures=[]
    if len(canonical)!=32: failures.append(f"expected 32 canonical Facial Plastics / Trauma topics, found {len(canonical)}")
    if len(set(canonical))!=len(canonical): failures.append("duplicate canonical Facial Plastics / Trauma topic names")
    if set(canonical)!=set(PROTECTED_TOPICS):
        failures.append(f"full-domain topic mismatch missing={sorted(set(canonical)-set(PROTECTED_TOPICS))} stale={sorted(set(PROTECTED_TOPICS)-set(canonical))}")
    by_cid=defaultdict(list)
    for q in data.CLINICAL_CHALLENGES_V119:
        cid=q.get("concept_id")
        if cid: by_cid[cid].append(q)
    for topic in PROTECTED_TOPICS:
        cid=data._v6_item_id(DOMAIN,topic)
        rows=[q for q in by_cid.get(cid,[]) if q.get("ladder_reviewed")]
        stages={q.get("learning_stage") for q in rows if q.get("learning_stage") in STAGES}
        if stages!=STAGES: failures.append(f"{topic}: missing stages {sorted(STAGES-stages)}")
        for q in rows:
            for err in _quality_errors(q): failures.append(f"{q.get('id')}: {err}")
    print(f"FACIAL_PLASTICS_PROTECTED_TOPICS|{len(PROTECTED_TOPICS)}")
    print(f"FACIAL_PLASTICS_CANONICAL_TOPICS|{len(canonical)}")
    if failures:
        print("FACIAL PLASTICS FULL-DOMAIN FAILURES"); print("\n".join(failures)); raise SystemExit(1)
    print("PASS: all 32 exact canonical Facial Plastics / Trauma topics retain complete reviewed ladders and quality contracts")

if __name__=="__main__": main()
