"""v20.8 — deliberate learning-ladder curation, Rhinology pass 4.

Reviews five more canonical foundations. Strong v14.4 cases are reused as the
application layer; only senior/chief decision questions are added.
"""
DOMAIN = "Rhinology / Allergy / Skull Base"

REVIEWED_FOUNDATION_IDS_V208 = {
    "v136_rhi_16",  # Inferior Turbinate Hypertrophy
    "v136_rhi_17",  # Nasal Anatomy for Endoscopy
    "v136_rhi_18",  # Objective Assessment of Nasal Function
    "v136_rhi_20",  # Olfactory Dysfunction
    "v136_rhi_21",  # Pediatric Chronic Rhinosinusitis
}
REUSED_APPLICATION_IDS_V208 = {
    "v144_rh_10": "Inferior Turbinate Hypertrophy",
    "v144_rh_13": "Nasal Anatomy for Endoscopy",
    "v144_rh_15": "Objective Assessment of Nasal Function",
    "v144_rh_16": "Olfactory Dysfunction",
    "v144_rh_17": "Pediatric Chronic Rhinosinusitis",
}

def _q(qid, topic, stem, choices, answer, explanation, why_wrong, pearl, curveball, focus):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":"senior_decision",
            "stem":stem,"choices":choices,"answer":answer,"explanation":explanation,
            "why_wrong":why_wrong,"board_pearl":pearl,"curveball":curveball,
            "tier":"Curated learning ladder","mode":"Vignette","focus":focus,
            "ladder_reviewed":True}

VIGNETTES_V208 = [
_q("v208_rhi_turb_snr","Inferior Turbinate Hypertrophy",
   "A patient remains obstructed after technically adequate septoplasty and conservative submucosal turbinate reduction. The turbinates are small and patent, but inspiration produces marked lateral-wall/internal nasal-valve collapse. What is the best next decision?",
   ["Repeat aggressive turbinectomy because persistent obstruction proves residual turbinate tissue","Identify and treat the dynamic nasal-valve mechanism rather than removing additional functioning turbinate tissue","Perform Draf III","Prescribe indefinite topical oxymetazoline"],1,
   "Persistent obstruction after turbinate reduction requires reassessing the mechanism. Dynamic lateral-wall or internal-valve collapse will not be corrected by further turbinate removal, which instead risks dryness, crusting, and empty-nose symptoms.",
   ["Further resection targets the wrong mechanism and sacrifices functional mucosa.","Correct. Treat the demonstrated valve collapse rather than escalating turbinate resection.","Frontal sinusotomy does not address inspiratory nasal-valve collapse.","Chronic topical vasoconstrictor use risks rhinitis medicamentosa and is not structural treatment."],
   "When the turbinate is no longer the bottleneck, stop treating it as one.","How would improvement with lateral-wall support during examination influence functional rhinoplasty planning?","OR_prep"),
_q("v208_rhi_anat_snr","Nasal Anatomy for Endoscopy",
   "During revision ESS, familiar middle-meatal landmarks are distorted and the surgeon is uncertain whether a superior partition is residual ethmoid cell or skull base. What is the safest attending-level move?",
   ["Continue dissecting until the anatomy becomes obvious","Stop, re-establish orientation from fixed landmarks and multiplanar CT/navigation as available, then proceed only when orbit and skull base are confidently localized","Use the microdebrider blindly because revision scar is usually safe","Convert the uncertain partition into a larger opening with forceps"],1,
   "Revision surgery removes many of the landmarks used in primary ESS. When orientation is lost near orbit or skull base, the correct response is to stop and deliberately re-localize using preserved fixed anatomy, imaging, and navigation when appropriate rather than allowing momentum to convert uncertainty into injury.",
   ["Dissection without localization turns uncertainty into skull-base or orbital risk.","Correct. Losing orientation is an indication to stop and rebuild the three-dimensional map.","Powered instrumentation can rapidly worsen an injury when the tissue boundary is uncertain.","Making an unknown structure larger is not a localization strategy."],
   "The safest instrument in distorted sinus anatomy is sometimes the one you stop moving.","Which fixed landmarks remain especially useful after prior uncinectomy and ethmoidectomy?","OR_prep"),
_q("v208_rhi_objective_snr","Objective Assessment of Nasal Function",
   "A patient has a very high NOSE score and clear subjective improvement when the lateral nasal wall is supported, but rhinomanometry is only mildly abnormal. What is the best senior interpretation?",
   ["Reject surgery because one objective airflow test is not severely abnormal","Integrate symptoms, dynamic examination, anatomy, and adjunctive testing; no single physiologic threshold should overrule a concordant clinical mechanism","Diagnose malingering because symptom and airflow scores differ","Perform turbinectomy because rhinomanometry cannot assess obstruction"],1,
   "Perceived nasal obstruction reflects resistance, geometry, mucosal sensation, and dynamic collapse. Objective tests can quantify selected components but do not supply a universal surgical threshold. Concordant history and dynamic examination remain central to mechanism-based planning.",
   ["Objective testing is an adjunct rather than a universal veto threshold.","Correct. Discordance should prompt synthesis, not automatic dismissal of either the patient or the test.","Symptom-test discordance is expected in a multidimensional sensory/airflow system and does not establish malingering.","A turbinate operation is inappropriate without evidence that turbinate tissue is the limiting mechanism."],
   "Measure airflow, but operate on a demonstrated mechanism—not on a number alone.","Why can a nonspecific Cottle maneuver overestimate benefit compared with targeted lateral-wall support?","boards"),
_q("v208_rhi_smell_snr","Olfactory Dysfunction",
   "A patient with persistent postviral anosmia asks for sinus surgery despite normal endoscopy and CT and no conductive obstruction. What is the best counseling decision?",
   ["Offer ESS because anosmia alone proves occult sinus obstruction","Explain that surgery has no anatomic target, continue structured olfactory rehabilitation and safety counseling, and investigate new focal neurologic or unilateral red flags if they emerge","Give prolonged antibiotics","Recommend permanent avoidance of odor exposure"],1,
   "Postviral olfactory dysfunction is primarily sensorineural when the nasal airway and olfactory cleft are unobstructed. ESS cannot restore smell by opening already normal sinuses. Management emphasizes olfactory training, prognosis and safety counseling, with targeted investigation for atypical features.",
   ["Normal objective sinonasal anatomy provides no surgically correctable target.","Correct. Match treatment to the sensorineural mechanism and reserve imaging/workup escalation for atypical features.","Antibiotics do not rehabilitate postviral olfactory neurons.","Structured odor exposure is therapeutic; blanket avoidance does not promote recovery."],
   "Before operating for smell loss, prove there is something obstructive for surgery to fix.","What household safety counseling is important for patients who cannot reliably detect smoke, gas, or spoiled food?","boards"),
_q("v208_rhi_pedscrs_snr","Pediatric Chronic Rhinosinusitis",
   "A 7-year-old has persistent CRS after medical therapy and adenoidectomy. CT shows diffuse disease, but the history also includes neonatal respiratory distress, chronic wet cough, recurrent otitis media, and bronchiectasis. What should happen before simply escalating to extensive ESS?",
   ["Proceed directly to adult-style complete ESS because the CT is diffuse","Evaluate for an underlying mucociliary disorder such as primary ciliary dyskinesia and coordinate systemic airway care while tailoring any sinus surgery to a defined goal","Perform frontal sinus obliteration","Assume adenoidectomy failure proves immunoglobulin deficiency"],1,
   "Persistent pediatric CRS accompanied by lifelong lower-airway disease, neonatal respiratory symptoms, recurrent middle-ear disease, or bronchiectasis should trigger evaluation for disorders such as PCD or CF. Surgery can improve drainage and topical access but does not correct the systemic clearance defect.",
   ["Diffuse CT disease does not explain the multisystem phenotype or replace etiologic evaluation.","Correct. The systemic mucociliary phenotype changes counseling, medical care, cultures, and the goals of surgery.","Frontal obliteration is not a routine escalation for pediatric inflammatory CRS.","Adenoidectomy failure is nonspecific and does not establish a particular immune disorder."],
   "A child with sinus disease plus bronchiectasis needs a host diagnosis, not just a bigger sinus operation.","Which laterality or fertility findings can further support a primary ciliary dyskinesia phenotype?","boards"),
]

def apply_learning_ladders_v208(challenges, item_id_fn):
    by_id={q.get("id"):q for q in challenges}
    touched=[]
    for qid in REVIEWED_FOUNDATION_IDS_V208:
        q=by_id.get(qid)
        if q:
            q["learning_stage"]="foundation"; q["ladder_reviewed"]=True; touched.append(qid)
    for qid,topic in REUSED_APPLICATION_IDS_V208.items():
        q=by_id.get(qid)
        if q:
            q["topic"]=topic; q["learning_stage"]="application"; q["ladder_reviewed"]=True; touched.append(qid)
    existing={q.get("id") for q in challenges}
    added=[]
    for q in VIGNETTES_V208:
        if q["id"] not in existing:
            q["concept_id"]=item_id_fn(DOMAIN,q["topic"]); challenges.append(q); existing.add(q["id"]); added.append(q["id"])
    # Ensure all reviewed rows link to the canonical concept.
    for q in challenges:
        if q.get("ladder_reviewed") and q.get("domain")==DOMAIN and q.get("topic") in set(REUSED_APPLICATION_IDS_V208.values()):
            q["concept_id"]=item_id_fn(DOMAIN,q["topic"])
    return {"reviewed_foundations":len(touched),"added":len(added),"ids":added}
