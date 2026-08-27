"""v24.8 — full Pediatric Otolaryngology deliberate ladder hard gate.

Requires the live canonical Pediatric registry to contain exactly 40 unique topics and
requires every one to have ladder_reviewed runtime cases spanning foundation,
application, and senior_decision. Progress is resolved by canonical concept_id, not
by aliases or source-file presence.
"""
from collections import defaultdict
import runtime_entry as rt

DOMAIN="Pediatric Otolaryngology"
STAGES={"foundation","application","senior_decision"}
EXPECTED_TOPICS=[
"Choanal Atresia","Pediatric Aspiration","Supraglottoplasty","Laryngotracheal Reconstruction","Thyroglossal Duct Cyst",
"Pediatric OSA / Adenotonsillar Disease","Pediatric Airway Foreign Body","Pediatric Subglottic Stenosis","Laryngomalacia","AOM / OME / Tympanostomy Decisions",
"Laryngotracheal Cleft","Pediatric Tracheostomy / Decannulation","Pediatric Vocal Fold Immobility","Subglottic Hemangioma","Tracheomalacia / Bronchomalacia",
"Recurrent Respiratory Papillomatosis","Pediatric Deep Neck Infection","Recurrent Tonsillitis Decision-Making","Lymphatic Malformation","Branchial Cleft Anomalies",
"Pediatric Hearing Loss Workup","Congenital CMV Hearing Loss","Congenital Neck Masses","Button Battery Ingestion","Microtia / Aural Atresia",
"Tympanostomy Tube Indications","Velopharyngeal Insufficiency","Cleft / Craniofacial Otologic-Airway Care","Croup vs Epiglottitis","Epiglottitis",
"Congenital Hearing Loss Genetics","Cleft Lip / Palate — ENT Surgical Fundamentals","Pediatric Head & Neck Tumors","Microtia Reconstruction","Ankyloglossia / Maxillary Frenulum",
"Juvenile Recurrent Parotitis","Pediatric Speech Disorders","Nonobstructive Pediatric Sleep Disorders","Pediatric Vestibular Disorders","Pediatric Reflux / Eosinophilic Esophagitis",
]


def main():
    data=rt.data
    modules=data.DEEP_MODULES_V6.get(DOMAIN,[])
    canonical=[m.get("topic") for m in modules if m.get("topic")]
    if len(canonical)!=40:
        raise AssertionError(f"Expected exactly 40 canonical Pediatric topics, found {len(canonical)}")
    if len(set(canonical))!=40:
        raise AssertionError("Duplicate canonical Pediatric topic names detected")
    if set(canonical)!=set(EXPECTED_TOPICS):
        missing=sorted(set(EXPECTED_TOPICS)-set(canonical)); unexpected=sorted(set(canonical)-set(EXPECTED_TOPICS))
        raise AssertionError(f"Pediatric canonical registry drift: missing={missing}; unexpected={unexpected}")

    by_cid=defaultdict(list)
    for q in data.CLINICAL_CHALLENGES_V119:
        cid=q.get("concept_id")
        if cid: by_cid[cid].append(q)

    failures=[]
    reviewed_rows=0
    for topic in EXPECTED_TOPICS:
        cid=data._v6_item_id(DOMAIN,topic)
        linked=by_cid.get(cid,[])
        reviewed=[q for q in linked if q.get("ladder_reviewed")]
        reviewed_rows+=len(reviewed)
        stages={q.get("learning_stage") for q in reviewed if q.get("learning_stage") in STAGES}
        if not reviewed:
            failures.append(f"{topic}: no ladder_reviewed runtime question")
        elif stages!=STAGES:
            failures.append(f"{topic}: missing stages {sorted(STAGES-stages)}")
        for q in reviewed:
            choices=list(q.get("choices") or []); reasons=list(q.get("why_wrong") or [])
            try: answer=int(q.get("answer"))
            except (TypeError,ValueError): failures.append(f"{q.get('id')}: invalid answer"); continue
            if len(choices)<2 or not 0<=answer<len(choices): failures.append(f"{q.get('id')}: invalid choices/answer")
            if len(reasons)!=len(choices): failures.append(f"{q.get('id')}: rationale length mismatch")
            elif not str(reasons[answer]).strip().lower().startswith("correct."):
                failures.append(f"{q.get('id')}: correct rationale misaligned")
    if failures:
        raise AssertionError("Pediatric full-domain ladder regression:\n"+"\n".join(failures))
    print(f"PEDIATRIC_LADDER_COMPLETE_PASS|domain={DOMAIN}|canonical=40|complete=40|reviewed_rows={reviewed_rows}|required_stages={','.join(sorted(STAGES))}")


if __name__=="__main__": main()
