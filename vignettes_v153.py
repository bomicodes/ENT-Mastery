"""v15.3 — High-consequence deterioration and intraoperative pivot pass.

Nine cross-domain cases. Each asks the learner to change course when new
physiology, anatomy, pathology, or postoperative findings make the original
plan unsafe or inadequate.
"""


def _c(qid,d,t,s,ch,a,e,ww,p,cb,f):
    return {"id":qid,"domain":d,"topic":t,"stem":s,"choices":ch,"answer":a,
            "explanation":e,"why_wrong":ww,"board_pearl":p,"curveball":cb,
            "tier":"Curated chief-level pivot","mode":"Vignette","focus":f}

O="Otology / Neurotology"; R="Rhinology / Allergy / Skull Base"; H="Head & Neck Oncology"
T="Thyroid / Parathyroid / Salivary"; P="Pediatric Otolaryngology"; L="Laryngology / Voice / Swallowing"
F="Facial Plastics / Trauma"; S="Sleep Surgery"; G="General ENT / Emergencies"

VIGNETTES_V153=[
_c("v153_oto_01",O,"Sudden Sensorineural Hearing Loss",
"A patient with sudden unilateral SNHL started systemic steroids promptly. Two weeks later repeat audiometry shows minimal recovery and the ear remains serviceable. What management change should now be discussed?",
["Continue observation for six months before considering anything else","Offer salvage intratympanic corticosteroid therapy within the accepted salvage window while completing appropriate etiologic evaluation","Proceed directly to cochlear implantation","Treat with antibiotics because steroid nonresponse proves infection"],1,
"Incomplete recovery after initial therapy should trigger discussion of salvage intratympanic corticosteroids rather than passive delay. The treatment window is time sensitive, while retrocochlear evaluation and follow-up audiometry remain important.",
["Long delay can forfeit a time-sensitive salvage opportunity.","Correct.","Cochlear implantation is not the immediate next step for an acutely affected ear with potentially recoverable serviceable hearing.","Steroid nonresponse does not establish a bacterial cause and does not make empiric antibiotics the treatment for idiopathic SSNHL."],
"Sudden hearing loss is not a one-decision pathway: failure to recover after initial treatment creates a salvage-treatment decision.",
"How would profound persistent loss with poor speech understanding alter later rehabilitation counseling?","boards"),

_c("v153_rh_01",R,"Invasive Fungal Rhinosinusitis",
"A neutropenic patient with biopsy-proven acute invasive fungal rhinosinusitis has undergone initial debridement and started systemic antifungal therapy. The next morning facial numbness has progressed and endoscopy shows new devitalized tissue. What is the best response?",
["Continue medical therapy alone because the patient already had one operation","Treat progression as ongoing invasive disease and urgently reassess for repeat debridement while optimizing antifungal therapy and reversible immunosuppression","Wait for black eschar to involve the entire nasal cavity","Stop antifungal therapy because surgery failed"],1,
"Acute invasive fungal disease can progress despite initial treatment. New necrosis or neurologic progression requires prompt reassessment and often serial debridement in addition to systemic antifungal therapy and reversal of predisposing immunosuppression when feasible.",
["A prior debridement does not protect against residual or newly demarcated invasive disease.","Correct.","Waiting for extensive eschar delays source control in an angioinvasive process.","Progression is a reason to optimize multimodal treatment, not to withdraw essential systemic antifungal therapy."],
"For invasive fungal sinusitis, the operative plan is iterative: serial examination and biology determine whether another debridement is needed.",
"What new orbital or cranial-neuropathy findings would make the extent-of-disease discussion even more urgent?","postoperative_call"),

_c("v153_hn_01",H,"Carotid Blowout Syndrome",
"A previously irradiated neck-dissection patient has a brief episode of brisk bleeding from a chronic pharyngocutaneous wound that stops spontaneously. He is currently awake and hemodynamically stable. What should the resident assume until proven otherwise?",
["The bleeding has stopped, so routine clinic follow-up is sufficient","This may be a sentinel bleed from threatened carotid blowout: escalate urgently, protect the airway/resuscitation plan, and obtain definitive vascular evaluation/intervention","Pack the wound blindly and discharge","Restart oral intake and observe without notifying anyone"],1,
"A self-limited sentinel hemorrhage in an irradiated or infected postoperative neck can precede catastrophic carotid rupture. Temporary hemostasis does not make the problem benign; urgent multidisciplinary airway, resuscitation, and endovascular/surgical planning is required.",
["Sentinel bleeding can precede lethal rebleeding and should not be managed as a resolved minor event.","Correct.","Blind deep packing can disrupt a tenuous vessel and does not replace definitive vascular control.","Routine observation without escalation ignores a high-risk warning event."],
"In the hostile irradiated neck, a small bleed can be the warning before a very large one.",
"If the patient begins exsanguinating into the airway, what are your simultaneous airway and hemorrhage priorities?","overnight_call"),

_c("v153_tps_01",T,"Post-thyroidectomy Hematoma / Airway",
"Two hours after thyroidectomy, a patient develops rapidly increasing neck pressure, dysphagia, stridor, and a tense expanding wound while the OR team is being mobilized. What should happen immediately?",
["Send the patient for CT to define the collection","Open the incision and release the compressive hematoma immediately when airway compromise is evolving while calling for airway/surgical help and definitive OR control","Wait for the surgeon to arrive before touching the wound","Give calcium and reassess in one hour"],1,
"A rapidly expanding post-thyroidectomy hematoma with airway symptoms is a clinical diagnosis and a decompression emergency. When airway compromise is evolving, immediate wound release can be lifesaving and should occur while help, airway management, and return to the OR are organized.",
["Imaging delays decompression and can move a deteriorating airway away from immediate rescue.","Correct.","Waiting can allow venous and laryngeal edema to progress to a much more difficult or impossible airway.","Hypocalcemia does not explain a tense expanding neck with stridor and does not treat mechanical airway compression."],
"A post-thyroidectomy neck hematoma is one of the rare complications where opening the wound at bedside may precede formal OR control.",
"Why can intubation become difficult even after the hematoma itself is released?","postoperative_call"),

_c("v153_ped_01",P,"Post-tonsillectomy Hemorrhage",
"A child on postoperative day 7 after tonsillectomy arrives pale and tachycardic after vomiting bright-red blood. There is no active oral bleeding during the first look. What is the safest management principle?",
["Discharge because the bleeding has stopped","Treat the history as a significant secondary post-tonsillectomy hemorrhage: obtain IV access/resuscitate, keep NPO, involve ENT urgently, and determine need for operative control based on the full clinical picture","Perform repeated aggressive bedside throat examinations until bleeding restarts","Give oral fluids immediately to test swallowing"],1,
"Post-tonsillectomy hemorrhage may be intermittent, and children can swallow substantial blood. A convincing significant bleed with pallor or tachycardia warrants resuscitation and urgent ENT management even when the tonsillar fossae are temporarily dry.",
["Transient cessation does not erase the risk of recurrent hemorrhage or occult blood loss.","Correct.","Repeated traumatic examination can provoke bleeding and delays controlled resuscitation and definitive management.","Oral intake is inappropriate during evaluation of a potentially operative hemorrhage and increases aspiration risk."],
"For post-tonsillectomy bleeding, the history and physiology matter even when the mouth is dry at the instant you look.",
"What anesthesia concern is created by the assumption that this child has a full stomach of swallowed blood?","overnight_call"),

_c("v153_lar_01",L,"Tracheostomy Emergencies",
"A patient five days after a new tracheostomy suddenly desaturates. Suction catheter will not pass, bagging through the tube is ineffective, and the neck is becoming emphysematous. What is the key management pivot?",
["Keep forcefully ventilating through the tracheostomy tube","Suspect displacement/false passage or obstruction, stop forcing ventilation through a malpositioned tube, call airway help, and re-establish oxygenation by the safest patent route while the tracheostomy is assessed","Advance the tube blindly deeper","Wait for a chest radiograph before changing anything"],1,
"Failure to pass a suction catheter plus ineffective ventilation strongly suggests tube obstruction or displacement. In an immature tract, blind manipulation can create or worsen a false passage; oxygenation and a controlled airway rescue take priority over preserving the existing tube position.",
["Forceful ventilation into a false passage can worsen subcutaneous emphysema and delay oxygenation.","Correct.","Blind advancement in a fresh tract risks tissue injury and deeper false passage.","Imaging cannot precede airway rescue in an actively desaturating patient."],
"In a tracheostomy emergency, ask first: is the tube actually in the airway and can a suction catheter pass?",
"How does rescue differ in a mature tracheostomy versus a total-laryngectomy stoma?","overnight_call"),

_c("v153_fp_01",F,"Orbital / Zygomaticomaxillary Complex Trauma",
"A patient with an orbital floor fracture initially had normal vision. Several hours later he develops worsening orbital pain, proptosis, decreased acuity, and a relative afferent pupillary defect. What should happen now?",
["Wait for swelling to improve because orbital fractures commonly cause bruising","Treat this as a vision-threatening orbital compartment process and obtain immediate ophthalmic/ENT-facial trauma evaluation with urgent decompression when indicated","Schedule elective fracture repair in two weeks without addressing the visual change","Apply a tight pressure dressing over the orbit"],1,
"New proptosis, declining vision, and an afferent pupillary defect after facial trauma suggest optic nerve/retinal perfusion threat from orbital compartment syndrome or retrobulbar hemorrhage. Vision-saving decompression is time sensitive and supersedes routine fracture timing.",
["Expected edema does not explain progressive objective visual dysfunction and should not reassure the team.","Correct.","Elective fracture timing is irrelevant until the acute threat to vision is addressed.","External pressure can further increase orbital pressure rather than decompress the compartment."],
"In facial trauma, a change in vision changes the case from fracture management to an emergency.",
"Which bedside findings should be documented before swelling or sedation makes the examination less reliable?","overnight_call"),

_c("v153_sleep_01",S,"Hypoglossal Nerve Stimulation",
"A CPAP-intolerant patient with moderate-severe OSA is being evaluated for hypoglossal nerve stimulation. Drug-induced sleep endoscopy shows complete concentric collapse at the velum. How should this finding change the plan?",
["Proceed with implantation because DISE findings do not affect candidacy","Recognize this collapse pattern as an unfavorable/standard exclusionary phenotype for conventional hypoglossal nerve stimulation candidacy and discuss alternative treatment strategies","Implant bilateral devices automatically","Treat with supplemental oxygen alone"],1,
"Hypoglossal nerve stimulation works best in appropriately selected anatomy. Complete concentric palatal collapse on DISE is a key adverse candidacy finding for conventional unilateral stimulation pathways and should redirect treatment planning rather than be ignored.",
["DISE is used specifically because collapse phenotype can alter procedure selection.","Correct.","A second implant does not correct inappropriate anatomic selection for the standard therapy.","Oxygen does not resolve the obstructive collapse pattern or substitute for definitive OSA therapy."],
"For sleep surgery, procedure selection should follow the collapse phenotype—not just the AHI.",
"If DISE instead showed anteroposterior palatal collapse without complete concentric collapse, what other candidacy factors would you review?","OR_prep"),

_c("v153_gen_01",G,"Deep Neck Space Infection",
"An adult with a parapharyngeal infection on IV antibiotics develops increasing neck swelling, muffled voice, drooling, and new inspiratory stridor. CT was obtained six hours earlier. What is the immediate priority?",
["Repeat CT before doing anything because the previous scan is now old","Treat the clinical deterioration as a threatened airway: mobilize controlled airway expertise and source-control planning rather than delaying stabilization for repeat imaging","Continue the same antibiotics and reassess tomorrow","Perform blind bedside incision through the neck swelling"],1,
"Deep-neck infection can deteriorate rapidly from edema, abscess progression, or spread. New stridor and secretion intolerance make airway stabilization the first priority; imaging and drainage strategy are important but must not delay management of an actively threatened airway.",
["A newer image is not more important than an airway that is failing now.","Correct.","Antibiotics alone are inadequate when the patient is developing airway compromise and may also have a drainable source.","Blind incision risks major vessels and does not substitute for anatomically planned source control."],
"When physiology changes, yesterday's scan does not get a veto over today's airway examination.",
"What CT or clinical findings would make mediastinal extension part of your immediate source-control planning?","overnight_call"),
]
