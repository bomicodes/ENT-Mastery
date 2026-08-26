"""v21.0 — deliberate learning-ladder curation, Rhinology pass 6.

Closes five high-consequence Rhinology concepts. Existing v13.5/v14.4 cases
are reused as application layers. New foundations are added only where the live
bank lacked a true recognition layer; new senior cases focus on escalation.
"""
DOMAIN = "Rhinology / Allergy / Skull Base"

def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong, pearl, curveball, focus):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,
            "stem":stem,"choices":choices,"answer":answer,"explanation":explanation,
            "why_wrong":why_wrong,"board_pearl":pearl,"curveball":curveball,
            "tier":"Curated learning ladder","mode":"Vignette","focus":focus,
            "ladder_reviewed":True}

REVIEWED_FOUNDATION_IDS_V210 = {"v136_rhi_27"}
REUSED_APPLICATION_IDS_V210 = {
    "v135_rhino_01":"Invasive Fungal Rhinosinusitis",
    "v135_rhino_02":"Orbital Complications of Sinusitis",
    "v135_rhino_03":"Epistaxis Surgical Control",
    "v144_rh_22":"Systemic Disease of the Nose / Sinuses",
    "v144_rh_23":"Unilateral Sinonasal Disease",
}

VIGNETTES_V210 = [
_q("v210_rhi_ifrs_found","Invasive Fungal Rhinosinusitis","foundation",
   "A patient with poorly controlled diabetes and ketoacidosis develops rapidly progressive facial pain, fever, nasal numbness, and a dusky insensate middle turbinate. What diagnosis must be assumed until proven otherwise?",
   ["Acute invasive fungal rhinosinusitis","Routine viral rhinosinusitis","Allergic fungal rhinosinusitis","Simple fungal ball"],0,
   "A susceptible host plus rapidly progressive pain, sensory change, and devitalized or insensate mucosa is classic for acute invasive fungal rhinosinusitis. Angioinvasion can cause tissue ischemia and rapid orbital or intracranial spread, so diagnosis and treatment must proceed urgently.",
   ["Correct. The host, tempo, pain, and devitalized mucosa are the key recognition pattern.","Viral disease does not produce progressive necrotic or insensate mucosa in this host.","AFRS is a chronic noninvasive inflammatory disease in an immunocompetent-type host, not a necrotizing emergency.","A fungal ball is noninvasive luminal disease and does not produce this angioinvasive phenotype."],
   "Immunocompromised host + severe facial pain + devitalized mucosa = invasive fungal disease until tissue proves otherwise.","What cranial neuropathy or orbital finding signals extension beyond the sinonasal cavity?","overnight_call"),
_q("v210_rhi_ifrs_snr","Invasive Fungal Rhinosinusitis","senior_decision",
   "A neutropenic patient with suspected invasive fungal rhinosinusitis has a negative first frozen section, but the middle turbinate remains pale and insensate and MRI shows progressive orbital-apex inflammation. What is the best senior decision?",
   ["Stop the workup because one negative frozen section excludes invasive disease","Maintain high suspicion, obtain additional targeted biopsies/debridement from abnormal tissue, start or continue systemic antifungal therapy, and coordinate urgent orbital/skull-base and host-factor management","Wait several days for fungal cultures before treating","Give high-dose systemic steroids alone for orbital inflammation"],1,
   "Sampling error can produce a false-negative frozen section when the clinical and imaging phenotype remains highly concerning. In a rapidly progressive angioinvasive syndrome, repeated targeted tissue assessment and empiric treatment are appropriate while host factors and extent are addressed in parallel.",
   ["A single negative sample does not safely overrule a strongly concordant high-risk syndrome.","Correct. Senior care integrates pathology with host, examination, imaging, and disease tempo rather than treating one test as absolute.","Culture delay can allow irreversible orbital, cerebral, or vascular progression.","Steroids without antifungal control can worsen an invasive fungal infection."],
   "In invasive fungal disease, a negative sample lowers certainty; it does not erase a dangerous phenotype.","What imaging or examination findings suggest cavernous-sinus or internal-carotid involvement?","overnight_call"),
_q("v210_rhi_orbit_found","Orbital Complications of Sinusitis","foundation",
   "A child with acute ethmoid sinusitis develops eyelid swelling but has full painless extraocular movements, normal vision, no proptosis, and no afferent pupillary defect. Which complication is most likely?",
   ["Preseptal cellulitis","Orbital cellulitis with postseptal involvement","Subperiosteal orbital abscess with visual compromise","Cavernous sinus thrombosis"],0,
   "Preseptal cellulitis is anterior to the orbital septum and causes eyelid edema without ophthalmoplegia, proptosis, pain with eye movement, or visual dysfunction. Those postseptal findings move the patient into an orbital emergency pathway.",
   ["Correct. Normal vision, motility, and absence of proptosis support a preseptal process.","Orbital cellulitis typically produces pain/restriction with eye movement and may cause proptosis or visual change.","A subperiosteal abscess is a postseptal process and becomes especially urgent with visual compromise or progression.","Cavernous sinus disease generally produces deeper cranial-neuropathy or bilateral orbital findings rather than isolated lid edema."],
   "The fastest orbital-sinus distinction is preseptal swelling versus postseptal dysfunction of vision, motility, or globe position.","Which bedside eye findings must be serially documented overnight when postseptal disease is suspected?","overnight_call"),
_q("v210_rhi_orbit_snr","Orbital Complications of Sinusitis","senior_decision",
   "A child with a medial subperiosteal orbital abscess has been on IV antibiotics for several hours. Visual acuity now declines, a relative afferent pupillary defect appears, and extraocular restriction is worsening. What is the best next decision?",
   ["Continue observation because medial abscesses never require surgery","Proceed with urgent drainage and sinus source control with ophthalmologic/ENT coordination rather than waiting for a longer antibiotic trial","Switch to oral antibiotics and discharge","Delay intervention until repeat CT shows a larger collection"],1,
   "Progressive visual or pupillary dysfunction is a vision-threatening change and overrides otherwise conservative criteria. The goal is urgent decompression/source control before ischemic optic or orbital injury becomes irreversible.",
   ["Anatomic location alone does not justify observation when vision is deteriorating.","Correct. Clinical eye deterioration is a surgical escalation threshold.","Discharge is unsafe in a child developing objective postseptal visual compromise.","The eye examination, not interval enlargement on CT, should drive urgent escalation when function is worsening."],
   "A deteriorating eye is an emergency even if the abscess looked modest on the first scan.","How do age, frontal involvement, abscess location, and anaerobic infection modify operative thresholds when vision is still normal?","overnight_call"),
_q("v210_rhi_epi_found","Epistaxis Surgical Control","foundation",
   "An older patient has brisk unilateral posterior nasal bleeding with blood flowing into the oropharynx despite anterior compression. Which arterial territory most commonly becomes the operative target when conservative measures fail?",
   ["Sphenopalatine artery branches","Superficial temporal artery","Facial artery at the mandibular notch","Middle meningeal artery"],0,
   "Most severe posterior epistaxis arises from branches of the sphenopalatine artery, the terminal branch of the internal maxillary artery entering near the sphenopalatine foramen. Understanding the vascular territory is foundational to endoscopic definitive control.",
   ["Correct. The sphenopalatine arterial territory is the principal endoscopic target for refractory posterior epistaxis.","The superficial temporal artery is not the usual posterior nasal source.","The facial artery can contribute anteriorly but is not the standard operative target for posterior epistaxis.","The middle meningeal artery supplies dura and is not the usual nasal bleeding source."],
   "Posterior epistaxis is usually a sphenopalatine-territory problem until anatomy or prior treatment proves otherwise.","Where is the sphenopalatine foramen relative to the posterior middle turbinate attachment?","OR_prep"),
_q("v210_rhi_epi_snr","Epistaxis Surgical Control","senior_decision",
   "A patient continues to bleed after technically adequate endoscopic sphenopalatine artery ligation. Review shows prior maxillary surgery and bleeding appears high near the superior septum. What is the best senior framework?",
   ["Repeat posterior packing indefinitely","Reassess for missed sphenopalatine branches and alternative arterial sources such as anterior/posterior ethmoid territory, correlate the bleeding site with prior anatomy, and choose targeted surgical or endovascular control","Assume the patient is not actually bleeding because SPA ligation always succeeds","Perform total rhinectomy"],1,
   "Failure after SPA control should trigger a vascular-anatomy audit rather than repetition of the same maneuver. Missed branches, ethmoidal sources, collateral flow, tumor, vascular lesion, or altered postoperative anatomy can all explain persistent bleeding and require targeted control.",
   ["Repeated packing adds morbidity without explaining why definitive control failed.","Correct. A failed definitive maneuver should reopen localization and source anatomy.","No epistaxis operation has a 100% success rate; persistent bleeding requires explanation.","Radical tissue removal is not an appropriate response to an unlocalized arterial source."],
   "When definitive epistaxis control fails, re-localize the vessel before escalating the violence of the treatment.","What vision-threatening risk must be discussed when embolization involves vessels with potential ophthalmic collaterals?","overnight_call"),
_q("v210_rhi_systemic_snr","Systemic Disease of the Nose / Sinuses","senior_decision",
   "A patient with destructive septal disease wants immediate saddle-nose reconstruction, but inflammatory markers are elevated, pulmonary nodules are enlarging, and rheumatology suspects active granulomatosis with polyangiitis. What is the best decision?",
   ["Proceed with definitive reconstruction before systemic treatment changes the anatomy","Defer elective structural reconstruction until systemic disease is controlled, obtain adequate etiologic confirmation, and treat urgent airway or infectious problems separately if present","Perform cosmetic filler injection as definitive disease treatment","Remove additional septal cartilage to obtain stable margins"],1,
   "Reconstruction in active vasculitic or destructive disease has a high risk of wound breakdown, graft loss, recurrent collapse, and continued tissue destruction. Disease control and diagnostic certainty should precede elective rebuilding unless an urgent functional problem requires separate intervention.",
   ["Active disease can destroy the reconstruction and create avoidable morbidity.","Correct. Stabilize the disease process before asking grafts and flaps to survive in the affected tissue bed.","Filler does not treat active vasculitis and can introduce additional risk in compromised tissue.","Removing more support worsens deformity and does not control systemic inflammation."],
   "Do not reconstruct a nose while the disease is still dismantling it.","What duration or evidence of disease quiescence would you want before major framework reconstruction?","OR_prep"),
_q("v210_rhi_unilateral_found","Unilateral Sinonasal Disease","foundation",
   "An adult has new persistent unilateral nasal obstruction and unilateral polypoid tissue. Which principle is most appropriate?",
   ["Treat it exactly like routine bilateral inflammatory polyposis without further evaluation","Treat unilateral disease as a diagnostic red flag and evaluate for dental, fungal, benign neoplastic, and malignant causes with endoscopy and imaging","Assume allergy because obstruction is the dominant symptom","Avoid imaging because unilateral disease is usually benign"],1,
   "Adult unilateral sinonasal disease has a broader and more consequential differential than routine bilateral inflammatory disease. Imaging and careful endoscopy help identify odontogenic disease, fungal ball, inverted papilloma, malignancy, or anatomic obstruction before treatment is selected.",
   ["Routine bilateral inflammatory assumptions can miss important unilateral pathology.","Correct. Unilateral disease deserves explanation before it earns an inflammatory label.","Allergy commonly produces bilateral diffuse disease and does not explain every unilateral mass.","Imaging is often essential to define attachment, bone change, dental source, orbit, and skull base."],
   "A unilateral sinonasal mass must earn the diagnosis of 'just a polyp.'","What CT finding of focal hyperostosis suggests the attachment site of an inverted papilloma?","boards"),
_q("v210_rhi_unilateral_snr","Unilateral Sinonasal Disease","senior_decision",
   "CT for unilateral maxillary opacification shows focal hyperostosis along the lateral nasal wall and a cerebriform soft-tissue mass extending toward the frontal recess. What is the best operative planning principle?",
   ["Perform simple polypectomy and leave the attachment intact","Plan attachment-oriented resection with imaging-defined access sufficient to treat the origin and underlying bone while preserving critical orbit/skull-base structures","Treat indefinitely with antibiotics without tissue diagnosis","Biopsy blindly in the office even if the lesion appears highly vascular"],1,
   "The combination of unilateral disease, cerebriform morphology, and focal hyperostosis raises concern for inverted papilloma. Recurrence reduction depends on identifying and treating the attachment rather than merely removing bulk tumor; approach selection follows the attachment and extension.",
   ["Bulk removal without attachment treatment is a classic setup for recurrence.","Correct. The attachment dictates the operation and may require tailored frontal, maxillary, or skull-base access.","Antibiotics do not definitively treat a benign neoplasm with recurrence and malignant-transformation potential.","Potential vascularity and skull-base relationships should be defined before an unsafe biopsy route is chosen."],
   "For inverted papilloma, follow the attachment—not the size of the visible polyp.","How does frontal-sinus attachment change the choice between standard endoscopic, Draf, trephine, or combined access?","OR_prep"),
]

def apply_learning_ladders_v210(challenges, item_id_fn):
    by_id={q.get("id"):q for q in challenges}
    for qid in REVIEWED_FOUNDATION_IDS_V210:
        q=by_id.get(qid)
        if q:
            q["learning_stage"]="foundation"; q["ladder_reviewed"]=True; q["concept_id"]=item_id_fn(DOMAIN,q["topic"])
    for qid,topic in REUSED_APPLICATION_IDS_V210.items():
        q=by_id.get(qid)
        if q:
            q["topic"]=topic; q["learning_stage"]="application"; q["ladder_reviewed"]=True; q["concept_id"]=item_id_fn(DOMAIN,topic)
    existing={q.get("id") for q in challenges}
    added=[]
    for q in VIGNETTES_V210:
        if q["id"] not in existing:
            q["concept_id"]=item_id_fn(DOMAIN,q["topic"]); challenges.append(q); existing.add(q["id"]); added.append(q["id"])
    return {"reviewed_topics":5,"added":len(added),"ids":added}
