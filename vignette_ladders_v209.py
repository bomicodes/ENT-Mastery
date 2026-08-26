"""v20.9 — deliberate learning-ladder curation, Rhinology pass 5.

Reviews five more canonical Rhinology foundations. Existing strong second-pass
cases are reused as application layers; only missing senior/chief decisions are
added.
"""
DOMAIN = "Rhinology / Allergy / Skull Base"

REVIEWED_FOUNDATION_IDS_V209 = {
    "v136_rhi_22",  # Recurrent Acute Rhinosinusitis
    "v136_rhi_23",  # Revision FESS
    "v136_rhi_24",  # Septal Deviation
    "v136_rhi_25",  # Sinonasal Malignancy
    "v136_rhi_26",  # Sphenoidotomy
}
REUSED_APPLICATION_IDS_V209 = {
    "v144_rh_18": "Recurrent Acute Rhinosinusitis",
    "v142_rhi_04": "Revision FESS",
    "v144_rh_19": "Septal Deviation",
    "v144_rh_20": "Sinonasal Malignancy",
    "v144_rh_21": "Sphenoidotomy",
}

def _q(qid, topic, stem, choices, answer, explanation, why_wrong, pearl, curveball, focus):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":"senior_decision",
            "stem":stem,"choices":choices,"answer":answer,"explanation":explanation,
            "why_wrong":why_wrong,"board_pearl":pearl,"curveball":curveball,
            "tier":"Curated learning ladder","mode":"Vignette","focus":focus,
            "ladder_reviewed":True}

VIGNETTES_V209 = [
_q("v209_rhi_rars_snr","Recurrent Acute Rhinosinusitis",
   "A patient reports five 'sinus infections' per year, but records show most episodes last 3–5 days, improve without antibiotics, and have no documented purulence or objective inflammation. CT between episodes is normal. What is the best senior-level decision?",
   ["Schedule ESS because episode count alone proves recurrent acute bacterial rhinosinusitis","Verify that future episodes actually meet acute bacterial criteria and reconsider migraine, viral URI, allergy, or other mimics before offering surgery","Prescribe prophylactic antibiotics year-round","Diagnose chronic rhinosinusitis despite complete symptom-free intervals"],1,
   "The label recurrent acute rhinosinusitis should be reserved for distinct episodes that truly behave like acute bacterial rhinosinusitis with return to baseline between attacks. A high self-reported episode count without objective or temporal support should trigger diagnostic verification rather than surgery for an unproven target.",
   ["Episode count alone does not establish bacterial disease or a surgically correctable mechanism.","Correct. First prove the phenotype and capture objective disease during a representative attack when possible.","Long-term prophylactic antibiotics are not a substitute for establishing the diagnosis and create avoidable harms.","CRS requires persistent symptoms with objective inflammation rather than normal intervals."],
   "Before operating on recurrent 'sinus infections,' prove that the recurrent events are actually sinus infections.","When is CT during an acute episode most useful in a patient being considered for surgery for RARS?","boards"),
_q("v209_rhi_revision_snr","Revision FESS",
   "A patient remains symptomatic after prior ESS. Endoscopy shows a patent maxillary antrostomy and ethmoid cavity, but CT demonstrates an unaddressed odontogenic maxillary source and the operative report confirms the natural ostium is already incorporated. What is the best revision principle?",
   ["Repeat the same sinus operation because persistent symptoms after ESS imply inadequate surgery","Treat the dental source and avoid unnecessary revision of already patent sinus anatomy unless a separate correctable sinonasal target remains","Remove the middle turbinate to increase access","Perform Draf III because any prior ESS failure justifies maximal frontal surgery"],1,
   "Revision surgery should correct the mechanism of failure, not simply repeat prior procedures. When the sinus drainage pathway is already patent and a persistent odontogenic source explains the disease, source control belongs at the dental origin; unnecessary re-dissection only adds scar and complication risk.",
   ["Repeating a technically adequate operation does not correct a non-sinus source of failure.","Correct. Preserve what works and address the actual cause of persistent disease.","Middle turbinate resection does not treat an odontogenic source and may add morbidity.","Frontal escalation is unrelated when the failure mechanism is maxillary and dental."],
   "A good revision operation is defined by a new hypothesis, not by doing more of the old operation.","What operative-record and CT findings help distinguish residual uncinate, recirculation, stenosis, and nonrhinogenic failure?","OR_prep"),
_q("v209_rhi_septum_snr","Septal Deviation",
   "During septoplasty for a severe caudal deviation, correction would require removing most of the remaining caudal and dorsal L-strut. What is the best attending-level decision?",
   ["Resect the support anyway because a straight airway is the only goal","Preserve or reconstruct structural support with an appropriate caudal/extracorporeal or grafting technique rather than accepting destabilizing overresection","Convert to inferior turbinectomy","Ignore tip support because it is cosmetic only"],1,
   "The septum is both airway partition and structural support. Severe caudal deformity may require reconstruction rather than simple excision; violating the dorsal/caudal support can produce saddle deformity, tip ptosis, and valve compromise even if the septum looks straighter intraoperatively.",
   ["Overresection trades obstruction for structural collapse and can create a worse functional airway.","Correct. Reconstruct when necessary so airway correction does not sacrifice the support framework.","Turbinate surgery does not restore a destabilized septal L-strut.","Tip and valve support directly affect nasal function as well as appearance."],
   "A successful septoplasty leaves the nose both straighter and structurally competent.","When does a caudal septal deformity favor extracorporeal reconstruction or fixation to the anterior nasal spine?","OR_prep"),
_q("v209_rhi_malignancy_snr","Sinonasal Malignancy",
   "A sinonasal carcinoma extends to the orbital apex and cavernous sinus with multiple cranial neuropathies. The primary is technically accessible anteriorly, but complete resection would require major neurovascular sacrifice with little likelihood of clear margins. What is the best senior treatment principle?",
   ["Pursue radical surgery whenever any portion of the tumor is endoscopically reachable","Define resectability by the ability to achieve meaningful oncologic margins with acceptable morbidity and favor multidisciplinary nonsurgical or combined strategies when apex/cavernous-sinus disease makes curative resection unrealistic","Debulk the tumor without pathologic planning to relieve obstruction","Treat all sinonasal histologies with the same regimen"],1,
   "Operability is not the same as resectability. Skull-base, orbital-apex, cavernous-sinus, carotid, and cranial-nerve involvement may make an en bloc or margin-negative operation oncologically futile or excessively morbid. Histology and extent should drive multidisciplinary selection of surgery, radiation, and systemic therapy.",
   ["Technical access alone does not justify a morbid operation that cannot achieve a meaningful oncologic endpoint.","Correct. Resectability is an oncologic judgment balancing margins, biology, and morbidity.","Unplanned debulking can compromise staging and subsequent local therapy without providing durable control.","Sinonasal malignancies are biologically diverse and treatment is histology-specific."],
   "The question is not 'can I reach it?' but 'can surgery accomplish the oncologic goal without disproportionate harm?'.","How does perineural spread toward the cavernous sinus alter radiation-field planning and prognosis?","boards"),
_q("v209_rhi_sphenoid_snr","Sphenoidotomy",
   "During sphenoidotomy, an intersinus septum inserts directly onto a prominent carotid canal on preoperative CT. The septum limits exposure but disease can be cleared without removing its carotid attachment. What is the best operative decision?",
   ["Torque the septum off the carotid prominence with biting forceps","Leave the carotid-attached segment undisturbed or carefully drill under direct control only if truly necessary, prioritizing safe disease clearance over maximal cavity symmetry","Fracture the carotid prominence to widen the sphenoid","Abandon CT guidance because insertion patterns are not clinically important"],1,
   "Sphenoid septa can insert on the carotid canal, and levering or twisting them can transmit force to a dehiscent or thinned bony covering. Senior judgment means accepting asymmetric anatomy when disease can be safely treated without disturbing a dangerous attachment.",
   ["Blind torque can transmit force directly to the carotid canal and cause catastrophic vascular injury.","Correct. Do not sacrifice safety for a cosmetically symmetric sphenoidotomy.","Intentional injury to the carotid prominence has no role in routine sphenoid surgery.","Septal insertion anatomy is exactly why preoperative CT review matters."],
   "In the sphenoid, a septum attached to the carotid is a warning label, not a handle.","What immediate steps are required if brisk arterial bleeding suggests internal carotid injury during endoscopic sphenoid surgery?","OR_prep"),
]

def apply_learning_ladders_v209(challenges, item_id_fn):
    by_id={q.get("id"):q for q in challenges}
    for qid in REVIEWED_FOUNDATION_IDS_V209:
        q=by_id.get(qid)
        if q:
            q["learning_stage"]="foundation"; q["ladder_reviewed"]=True
    for qid,topic in REUSED_APPLICATION_IDS_V209.items():
        q=by_id.get(qid)
        if q:
            q["topic"]=topic; q["learning_stage"]="application"; q["ladder_reviewed"]=True; q["concept_id"]=item_id_fn(DOMAIN,topic)
    existing={q.get("id") for q in challenges}
    added=[]
    for q in VIGNETTES_V209:
        if q["id"] not in existing:
            q["concept_id"]=item_id_fn(DOMAIN,q["topic"]); challenges.append(q); existing.add(q["id"]); added.append(q["id"])
    for q in challenges:
        if q.get("ladder_reviewed") and q.get("domain")==DOMAIN and q.get("topic") in set(REUSED_APPLICATION_IDS_V209.values()):
            q["concept_id"]=item_id_fn(DOMAIN,q["topic"])
    return {"reviewed_topics":len(REVIEWED_FOUNDATION_IDS_V209),"added":len(added),"ids":added}
