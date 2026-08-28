"""v25.5 — strict 30-topic Laryngology deliberate-learning-ladder progress gate.

Protects exact canonical progress across the first six reviewed Laryngology batches.
This is intentionally a progress gate, not a claim that the 36-topic domain is complete.
"""
from collections import defaultdict
import runtime_entry as rt

DOMAIN="Laryngology / Voice / Swallowing"
STAGES={"foundation","application","senior_decision"}
PROTECTED_TOPICS=(
    "Unilateral Vocal Fold Paralysis",
    "Dysphagia / Aspiration",
    "Bilateral Vocal Fold Immobility",
    "Subglottic / Tracheal Stenosis",
    "Laryngeal Anatomy",
    "Stroboscopy Interpretation",
    "Microlaryngoscopy",
    "Injection Laryngoplasty",
    "Medialization Thyroplasty",
    "Posterior Glottic Stenosis / Arytenoid Fixation",
    "Reinke Edema",
    "Presbyphonia",
    "Muscle Tension Dysphonia",
    "Vocal Fold Sulcus / Scar",
    "Inducible Laryngeal Obstruction / PVFM",
    "FEES",
    "Modified Barium Swallow",
    "Zenker Diverticulum",
    "Cricopharyngeal Dysfunction",
    "Aspiration-Prevention Surgery",
    "Benign Vocal Fold Lesions",
    "Vocal Fold Nodules",
    "Vocal Fold Polyp / Cyst",
    "Leukoplakia / Laryngeal Dysplasia",
    "Vocal Process Granuloma",
    "Spasmodic Dysphonia",
    "Vocal Tremor",
    "Arytenoid Adduction / Reinnervation",
    "Posterior Cordotomy / Arytenoidectomy",
    "Chronic Cough / Laryngeal Hypersensitivity",
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
    return errors


def main():
    data=rt.data
    canonical=[m.get("topic") for m in data.DEEP_MODULES_V6.get(DOMAIN,[]) if m.get("topic")]
    failures=[]
    if len(canonical)!=36: failures.append(f"expected 36 canonical Laryngology topics, found {len(canonical)}")
    if len(set(canonical))!=len(canonical): failures.append("duplicate canonical Laryngology topic names")
    by_cid=defaultdict(list)
    for q in data.CLINICAL_CHALLENGES_V119:
        cid=q.get("concept_id")
        if cid: by_cid[cid].append(q)
    for topic in PROTECTED_TOPICS:
        if topic not in canonical:
            failures.append(f"protected topic missing from canonical registry: {topic}")
            continue
        cid=data._v6_item_id(DOMAIN,topic)
        rows=[q for q in by_cid.get(cid,[]) if q.get("ladder_reviewed")]
        stages={q.get("learning_stage") for q in rows if q.get("learning_stage") in STAGES}
        if stages!=STAGES: failures.append(f"{topic}: missing stages {sorted(STAGES-stages)}")
        for q in rows:
            for err in _quality_errors(q): failures.append(f"{q.get('id')}: {err}")
    print(f"LARYNGOLOGY_PROTECTED_TOPICS|{len(PROTECTED_TOPICS)}")
    print(f"LARYNGOLOGY_CANONICAL_TOPICS|{len(canonical)}")
    if failures:
        print("LARYNGOLOGY LADDER PROGRESS FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: 30 exact canonical Laryngology topics retain complete reviewed ladders and quality contracts")

if __name__=="__main__": main()
