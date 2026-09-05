"""v20.10 — deepen exact live General ENT / Emergencies Peritonsillar Abscess Concept Check.

Durable peritonsillar-space anatomy, drainage technique, airway assessment, and complication principles
are cross-checked against Cummings 7e, Pasha 6e, and K.J. Lee 12e in the connected Drive corpus.
Contemporary diagnostic and treatment nuance is updated against recent ultrasound, CT-predictor, and
randomized drainage-versus-tonsillectomy literature through 2026.
"""
from concept_check_board_repair_v177 import _find_module

SOURCE_REFS_V210 = [
 {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed., Chapter 9 Deep Neck and Odontogenic Infections; connected Drive corpus.","role":"foundation/operative: peritonsillar space, airway/dehydration assessment, transoral aspiration/incision and drainage, delayed versus acute tonsillectomy, deep-neck complication awareness"},
 {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022); connected Drive copy.","role":"foundation/application: PTA presentation, cellulitis/abscess distinction, drainage, antibiotics, steroids, airway and deep-neck escalation"},
 {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019); connected Drive copy.","role":"operative safety: tonsillar/peritonsillar anatomy, controlled aspiration/incision, avoidance of deep lateral dissection and carotid injury, tonsillectomy decision context"},
 {"type":"systematic_review","citation":"Kim DJ, et al. Test characteristics of ultrasound for the diagnosis of peritonsillar abscess: a systematic review and meta-analysis. Acad Emerg Med. 2023;30:859-869. doi:10.1111/acem.14660.","role":"current diagnosis: ultrasound has high sensitivity and moderate specificity and can reduce reliance on CT or blind aspiration when anatomy/exam is uncertain"},
 {"type":"randomized_trial","citation":"Todsen T, et al. Transoral Ultrasound in the Diagnostic Workup of Peritonsillar Abscess—A Randomized Clinical Trial. Laryngoscope. 2026. doi:10.1002/lary.70679.","role":"current diagnostic workflow: transoral ultrasound reduced unsuccessful needle-aspiration attempts without demonstrating improved diagnostic accuracy or patient outcomes"},
 {"type":"peer_reviewed","citation":"Li AC, et al. Computed Tomographic and Clinical Findings Predictive of Successful Peritonsillar Abscess Drainage. Laryngoscope. 2026;136:151-157. doi:10.1002/lary.70024.","role":"current selective imaging nuance: when CT is obtained, abscess size, soft-palate effacement and continuous ring enhancement can help predict drainage yield"},
 {"type":"randomized_trial","citation":"Voruz F, et al. A randomized clinical trial of peritonsillar abscess treatment comparing drainage and tonsillectomy. Am J Otolaryngol. 2025;46:104745. doi:10.1016/j.amjoto.2025.104745.","role":"current treatment nuance: immediate tonsillectomy can be effective but must be balanced against operative bleeding/morbidity rather than taught as routine first-line care for every PTA"},
]

CONCEPT_ID="v6-general-ent-emergencies-peritonsillar-abscess"
TOPIC="Peritonsillar Abscess"
Q_REC="cc-v112-rec-general-ent-emergencies-peritonsillar-abscess"

ANSWER="""Foundation — peritonsillar abscess is a collection between the tonsillar capsule and the pharyngeal constrictor, usually presenting with severe unilateral sore throat, odynophagia, muffled 'hot-potato' voice, trismus, drooling, soft-palate/peritonsillar bulge and often uvular deviation away from the affected side. Uvular deviation supports the diagnosis but is not required. The first senior-resident question is not 'where do I stick the needle?' but whether the patient can protect the airway, handle secretions, maintain hydration and safely tolerate a bedside examination/procedure.

Differentiate abscess from cellulitis/phlegmon, intratonsillar abscess, parapharyngeal disease and a noninfectious lateral-oropharyngeal mass. A classic uncomplicated PTA in a stable, cooperative patient often does not require CT before drainage. Imaging becomes more useful when the exam is equivocal, trismus or anatomy prevents adequate visualization, there is concern for deep-neck extension, the patient is toxic or atypical, a first drainage attempt fails despite persistent suspicion, or another diagnosis must be excluded. Ultrasound is especially useful as a radiation-sparing localization tool; contemporary evidence supports good sensitivity but only moderate specificity. A 2026 randomized trial found transoral ultrasound reduced unsuccessful needle attempts even though overall diagnostic accuracy and patient outcomes were not significantly improved. If CT has already been obtained, recent data suggest larger size, soft-palate effacement and continuous ring enhancement make successful drainage more likely; that is a selective decision aid, not a reason to CT every routine PTA.

Application — stabilize first. Address airway risk, give analgesia, rehydrate when needed, and start antibiotics covering the expected polymicrobial aerobic/anaerobic flora. Steroids can be useful as an adjunct for pain, edema and oral-intake recovery in selected patients. Definitive source control for a drainable PTA is usually needle aspiration or incision and drainage. Optimize the procedure before declaring failure: topical/local anesthesia, hydration, analgesia and time for treatment to work can substantially improve exposure and tolerance.

Drainage safety — localize the most fluctuant/prominent region rather than blindly chasing the lateral pharyngeal wall. Needle aspiration can confirm pus and map the pocket. For incision and drainage, use a controlled mucosal incision with blunt spreading into the peritonsillar space rather than deep lateral cutting. The carotid artery lies posterolateral to the tonsillar/peritonsillar field; the practical protection is not a magic centimeter measurement but staying medial, using controlled depth, avoiding blind lateral dissection and stopping when the anatomy does not match expectations. A negative aspiration is not proof that no abscess exists: the pocket may be small, multiloculated, intratonsillar, unusually positioned or simply missed.

Disposition — discharge is reasonable only when the airway is safe, bleeding is controlled, the patient can tolerate oral intake/medications, pain is manageable, there is reliable follow-up and no concerning deep-neck or systemic complication. Admit or escalate for airway concern, inability to hydrate, sepsis/toxicity, immunocompromise with poor reserve, significant deep-space extension, uncontrolled pain, repeated failed drainage with persistent disease, or inability to ensure follow-up.

Senior decision — failed bedside drainage should trigger a diagnosis and exposure reset rather than repeated blind passes. Reconsider cellulitis versus a deeper or atypically located collection, use ultrasound or CT selectively, and move to the OR when exposure, cooperation, airway risk or disease extent makes bedside management unsafe. Acute 'quinsy' tonsillectomy is an option in selected patients, particularly when a general anesthetic is already required, exposure is poor, disease is recurrent, or there is a compelling tonsillectomy indication. It is not mandatory after every first PTA. Recent randomized evidence supports that immediate tonsillectomy can be highly effective but also reinforces that bleeding and operative morbidity must be weighed against drainage-based management. Interval tonsillectomy is individualized based on recurrent PTA, recurrent/chronic tonsillitis, obstruction and patient-specific recurrence risk rather than prescribed reflexively after one uncomplicated episode.

Complication frame — worsening neck swelling, torticollis, toxic appearance, cranial neuropathy, chest symptoms, persistent fever, airway change or pain out of proportion should raise concern for parapharyngeal/retropharyngeal spread, Lemierre syndrome, mediastinal extension or vascular complication. The dangerous bedside mistake is to keep treating a deep-neck complication as a simple PTA because the tonsil still looks asymmetric.

Textbook-versus-current distinction — Cummings, Pasha and K.J. Lee remain the durable sources for peritonsillar anatomy, airway/dehydration assessment, controlled aspiration/I&D, carotid-safe technique and tonsillectomy principles. Newer evidence mainly refines diagnostic efficiency and selection: ultrasound can reduce blind aspiration attempts, CT morphology can help predict drainage yield when CT is already obtained, and immediate tonsillectomy is a selective strategy rather than a universal default.

Senior synthesis — AIRWAY, HYDRATION, ABSCESS OR CELLULITIS, SAFE LOCALIZATION, SOURCE CONTROL, then DISPOSITION. Escalate when the anatomy, airway, response or disease extent stops behaving like an uncomplicated PTA."""

COHORT={
 Q_REC:{"concept_id":CONCEPT_ID,"canonical_topic":TOPIC,
 "prompt":"A young adult presents with severe unilateral odynophagia, trismus, muffled voice, drooling and a prominent peritonsillar/soft-palate bulge. Walk through how the ENT resident should distinguish PTA from cellulitis or deeper disease, decide whether imaging is needed, drain it safely, choose disposition, and recognize when failed bedside treatment should escalate to the OR or tonsillectomy?",
 "answer_text":ANSWER,
 "explanation":"PTA management is a sequence: airway and hydration, distinguish drainable abscess from mimics, use imaging selectively, obtain safe source control, then choose disposition and tonsillectomy strategy according to recurrence, exposure and disease severity.",
 "board_pearl":"Do not turn a routine PTA into a carotid injury with blind lateral/deep instrumentation; a negative aspiration should trigger relocalization or reconsideration, not repeated uncontrolled passes.",
 "depth_layers_v210":{"foundation":"Peritonsillar-space anatomy, classic presentation, abscess-versus-cellulitis differential, airway and hydration physiology.","application":"Selective ultrasound/CT, antibiotics and adjuncts, aspiration versus I&D, safe controlled depth and outpatient-versus-admission criteria.","senior_decision":"Reset after failed drainage, recognize deep-neck/vascular extension, and individualize OR drainage, quinsy tonsillectomy or later tonsillectomy rather than using reflex algorithms."}}
}

TRAPS=[
 "Ordering CT reflexively for every classic uncomplicated PTA instead of using imaging when diagnosis, localization or extension is uncertain.",
 "Treating uvular deviation as mandatory and missing a true PTA without dramatic deviation.",
 "Performing repeated blind needle passes after a negative aspiration instead of relocalizing the pocket or reconsidering the diagnosis.",
 "Cutting or dissecting deeply/laterally in the peritonsillar field and increasing carotid injury risk.",
 "Calling bedside drainage a failure before optimizing analgesia, hydration, local anesthesia and exposure.",
 "Discharging a patient who still cannot handle secretions or oral hydration because pus was technically drained.",
 "Missing parapharyngeal/retropharyngeal spread, Lemierre syndrome or another deep-neck complication when the clinical course is atypical.",
 "Teaching immediate or interval tonsillectomy as obligatory after every first uncomplicated PTA instead of individualizing the indication."
]
for _p in COHORT.values():
 _p["common_traps_v210"]=list(TRAPS)
 _p["deliberate_review_v210"]="Selected from the exact successful v20.9 live-canonical backlog because Peritonsillar Abscess remained shallow despite high ED, board, airway and bedside-procedure consequence. Rehomed only after concurrent v20.9 Posterior Cordotomy / Arytenoidectomy reached an exact-head green main, preserving that newer lineage rather than overwriting it."
 _p["source_refs_v210"]=SOURCE_REFS_V210

def apply_concept_check_task_alignment_v210(checks, deep_modules, v6_item_id):
 by={str(q.get('id') or ''):q for q in checks or []}; repaired=[]; missing=[]; link_mismatch=[]
 for qid,p in COHORT.items():
  q=by.get(qid)
  if q is None: missing.append(qid); continue
  m=_find_module(q,deep_modules,v6_item_id); topic=str(m.get('topic') or '') if m else ''; cid=v6_item_id(q.get('domain'),topic) if m and q.get('domain') else None
  if m is None or topic!=p['canonical_topic'] or cid!=p['concept_id'] or q.get('concept_id')!=cid: link_mismatch.append(qid); continue
  for field in ('prompt','answer_text','explanation','board_pearl','depth_layers_v210','common_traps_v210','deliberate_review_v210','source_refs_v210'): q[field]=p[field]
  q['choices']=[]; q['answer']=None; q['task_alignment_v210']=True; repaired.append(qid)
 return {'repaired':repaired,'missing':missing,'link_mismatch':link_mismatch}
