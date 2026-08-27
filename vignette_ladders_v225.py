"""v22.5 — Head & Neck Oncology learning-ladder pass 6.

Reviews five additional canonical topics: tumor immunology/immunotherapy,
salvage surgery, neck management by primary site, reconstruction selection,
and osteoradionecrosis of the jaw.
"""
DOMAIN="Head & Neck Oncology"
REUSED={
    "v135_hn_02":("Salvage Surgery After Radiation / Chemoradiation","application"),
    "v143_hno_03":("Neck Management by Primary Site","application"),
}
REUSED_REASON_BY_CHOICE={
"v135_hn_02":{
"Re-irradiation is always preferred over surgery":"Re-irradiation is useful in selected cases but is not automatically preferable to resection when an isolated recurrence is surgically curable.",
"Evaluate for salvage surgery while counseling about higher wound, fistula, and swallowing complication risks in the irradiated field":"Correct. Resectable isolated recurrence after prior chemoradiation should prompt a salvage-surgery discussion that explicitly accounts for irradiated wound biology and functional morbidity.",
"Observation until airway compromise occurs":"Delay can sacrifice resectability and allow preventable functional deterioration.",
"Systemic therapy is mandatory before considering local salvage":"Systemic therapy is not mandatory before a potentially curative local salvage operation in every patient."},
"v143_hno_03":{
"Electively treat the appropriate ipsilateral nodal levels when occult risk is sufficiently high rather than waiting for palpable disease":"Correct. A clinically N0 neck may still warrant elective treatment based on occult-risk biology and predictable drainage.",
"Never treat a clinically negative neck":"Clinically N0 does not mean pathologically node-negative when occult risk is substantial.",
"Always perform bilateral radical neck dissection":"The extent and laterality of treatment should match primary-site drainage and risk, not a universal radical operation.",
"Use PET alone as definitive neck treatment":"Imaging helps stage the neck but is not itself definitive nodal treatment."}}

def _q(qid,topic,stage,stem,choices,answer,explanation,why_wrong,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":why_wrong,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True}

VIGNETTES_V225=[
_q("v225_hn_imm_fnd","Tumor Immunology / Immunotherapy in HNSCC","foundation",
"Which treatment class has become central to many recurrent/metastatic HNSCC pathways by restoring antitumor T-cell activity?",
["Immune checkpoint inhibitors targeting the PD-1/PD-L1 axis","Topical antifungals","Loop diuretics","Beta blockers"],0,
"PD-1/PD-L1 checkpoint inhibition can restore antitumor immune activity and is a major systemic-treatment strategy in recurrent/metastatic HNSCC.",
["Correct. PD-1/PD-L1 blockade is foundational to modern HNSCC immunotherapy.","Antifungals do not treat HNSCC.","Diuretics do not provide antitumor immune therapy.","Beta blockers are not standard immune therapy for HNSCC."],
"Checkpoint therapy changes the immune brake; it does not target the tumor like a cytotoxic drug.","Why can immune-related adverse events involve organs far outside the head and neck?"),
_q("v225_hn_imm_app","Tumor Immunology / Immunotherapy in HNSCC","application",
"A patient on pembrolizumab for recurrent HNSCC develops new diarrhea, rash, and rising liver enzymes. What management principle is most appropriate?",
["Assume these are unrelated because immunotherapy affects only the tumor","Recognize possible immune-related adverse events, grade severity, hold treatment when appropriate, and initiate guideline-based immunosuppression/consultation for significant toxicity","Continue therapy regardless of severity","Treat only with antibiotics"],1,
"Checkpoint inhibitors can produce immune-mediated toxicity in skin, bowel, liver, endocrine organs, lungs, and other systems. Management depends on severity and often requires holding therapy and corticosteroid-based immunosuppression for clinically significant events.",
["Immune toxicity can involve many organs.","Correct. Early recognition and severity-based management reduce morbidity.","Unconditional continuation can worsen serious toxicity.","Antibiotics do not treat immune-mediated hepatitis or colitis."],
"A new inflammatory syndrome during checkpoint therapy is immune toxicity until proven otherwise.","Which endocrine toxicities may require lifelong hormone replacement even after immunotherapy is stopped?"),
_q("v225_hn_imm_snr","Tumor Immunology / Immunotherapy in HNSCC","senior_decision",
"A patient with metastatic HNSCC has low-volume asymptomatic progression on one scan after starting immunotherapy but is clinically much better. What is the best senior-level principle?",
["Declare treatment failure from one measurement without context","Interpret imaging with clinical course and immune-response patterns, while excluding unequivocal progression or dangerous organ compromise before deciding whether to continue or change therapy","Perform immediate total laryngectomy regardless of disease distribution","Stop all cancer care"],1,
"Immune therapy can produce atypical response kinetics, although true progression is far more common than pseudoprogression. Treatment decisions should integrate symptoms, rate and site of progression, repeat imaging when appropriate, and risk of delaying an effective alternative.",
["One scan should be interpreted in clinical context, especially when disease burden is small and the patient is improving.","Correct. Senior care balances the possibility of atypical immune response against the danger of undertreating true progression.","A local laryngeal operation does not address disseminated disease by default.","Ongoing oncologic and symptom care remain appropriate."],
"Do not invoke pseudoprogression casually—but do not ignore the clinical story either.","Which progression sites would make waiting for confirmatory imaging unsafe?"),

_q("v225_hn_salv_fnd","Salvage Surgery After Radiation / Chemoradiation","foundation",
"What makes salvage surgery after prior head-and-neck chemoradiation fundamentally different from the same operation in an untreated field?",
["Previously irradiated tissues have impaired vascularity and healing with higher fistula, wound, and functional morbidity","Radiation improves wound healing","Prior radiation eliminates the need for reconstruction","Salvage surgery carries no additional vascular risk"],0,
"Fibrosis, hypovascularity, tissue friability, altered planes, and poor healing make salvage surgery more technically difficult and increase fistula, infection, vessel exposure, and reconstructive risk.",
["Correct. Prior radiation changes both anatomy and wound biology.","Radiation generally impairs rather than improves healing.","Vascularized reconstruction may be more important, not less.","Major-vessel complications can be increased in heavily treated fields."],
"Salvage surgery is not simply delayed primary surgery; the tissue has changed.","Which preoperative factors predict higher pharyngocutaneous fistula risk after salvage laryngectomy?"),
_q("v225_hn_salv_snr","Salvage Surgery After Radiation / Chemoradiation","senior_decision",
"A patient has a small technically resectable recurrence after chemoradiation, but surgery would require total laryngopharyngectomy in a frail patient with severe pulmonary disease and poor baseline function. What should determine whether salvage is offered?",
["Technical resectability alone","Probability of meaningful oncologic benefit weighed against perioperative mortality, functional outcome, competing comorbidity, reconstruction, rehabilitation, and patient goals","The surgeon's preference alone","Whether the operation can be scheduled quickly"],1,
"Salvage surgery can be curative, but technical resectability does not guarantee that the net benefit is favorable. Frailty, pulmonary reserve, nutritional status, expected function, likelihood of durable control, and patient values must shape the decision.",
["A technically possible operation can still be a poor overall treatment choice.","Correct. Curative intent must remain proportional to realistic benefit and morbidity.","Shared decision-making and multidisciplinary input are essential.","Scheduling convenience does not determine oncologic appropriateness."],
"The right salvage operation is one the patient can survive, recover from, and meaningfully benefit from.","When would nonsurgical palliation or systemic therapy be a better option despite resectability?"),

_q("v225_hn_neck_fnd","Neck Management by Primary Site","foundation",
"Why does elective neck treatment differ between a small early glottic SCC and an oral tongue SCC of similar primary size?",
["Primary sites have different lymphatic density and predictable drainage patterns, producing different occult nodal risks","All head-and-neck sites drain identically","Glottic cancers always spread to level I first","Oral tongue cancer never spreads to nodes"],0,
"Primary-site lymphatic anatomy strongly influences occult nodal risk and which levels require elective treatment. Early glottic cancers have relatively sparse lymphatics, whereas oral tongue cancers commonly metastasize to upper jugular/submandibular pathways depending on location and depth.",
["Correct. Neck treatment is site- and risk-specific.","Head-and-neck lymphatic drainage is not uniform.","Early glottic cancer does not characteristically drain first to level I.","Oral tongue SCC has clinically important occult nodal risk."],
"The clinically N0 neck is managed according to biology and drainage, not by one universal template.","How does depth of invasion alter oral tongue neck management?"),
_q("v225_hn_neck_snr","Neck Management by Primary Site","senior_decision",
"A lateralized oral cavity SCC approaches but does not cross midline and has ipsilateral nodal disease. What should determine whether the contralateral neck is treated electively?",
["Treat both necks automatically in every case","Integrate midline proximity/crossing, primary subsite, T category, ipsilateral nodal burden, and expected contralateral drainage rather than using a blanket rule","Never treat the contralateral neck","Use only patient age"],1,
"Contralateral risk is not binary. Tumor proximity to or crossing the midline, floor-of-mouth/base-of-tongue involvement, advanced primary disease, and nodal burden can increase bilateral drainage risk and influence surgery or radiation fields.",
["Universal bilateral treatment over-treats many lateralized low-risk tumors.","Correct. Laterality should follow anatomy and disease burden.","Some tumors have substantial contralateral occult risk.","Age alone does not map lymphatic drainage."],
"Midline is a lymphatic decision point, not merely a drawing on the operative diagram.","Which oral cavity or oropharyngeal subsites are most likely to require bilateral neck consideration?"),

_q("v225_hn_recon_fnd","Reconstruction Selection After Head & Neck Ablation","foundation",
"What is the primary principle when selecting reconstruction after head-and-neck cancer ablation?",
["Match the reconstruction to the functional and structural requirements of the defect rather than using the same flap for every patient","Always choose the largest free flap","Avoid vascularized tissue in irradiated fields","Prioritize donor-site appearance over airway and swallowing"],0,
"Reconstruction is defect-driven. Thin pliable lining, bulk, bone, skin, vascularized coverage, separation of compartments, speech/swallow function, and prior treatment all influence flap selection.",
["Correct. The defect's requirements define the reconstructive problem.","A larger flap is not automatically better.","Irradiated fields often benefit from healthy vascularized tissue.","Airway, swallowing, speech, contour, and wound protection usually outweigh cosmetic donor-site concerns."],
"Choose tissue by what the defect needs to do, not by the flap you most like to harvest.","Which defects require vascularized bone rather than soft tissue alone?"),
_q("v225_hn_recon_app","Reconstruction Selection After Head & Neck Ablation","application",
"A segmental mandibulectomy creates a 7-cm lateral mandibular defect plus intraoral mucosal loss. Which reconstructive concept best restores continuity and function?",
["Use vascularized bone with a skin paddle when both mandibular continuity and mucosal lining require replacement","Use a thin skin graft alone","Leave the mandibular gap unreconstructed in every patient","Use local cautery only"],0,
"A segmental bony defect typically requires restoration of mandibular continuity, and associated mucosal loss may require a skin paddle. A vascularized osseous free flap such as fibula is often well suited to this combined three-dimensional problem.",
["Correct. Bone and lining should be reconstructed together when both are missing.","A skin graft cannot restore mandibular continuity.","Leaving a major continuity defect can severely impair occlusion, mastication, and contour.","Cautery is not reconstruction."],
"Composite defects need composite solutions.","How do anticipated dental rehabilitation and number of osteotomies influence fibula planning?","OR_prep"),
_q("v225_hn_recon_snr","Reconstruction Selection After Head & Neck Ablation","senior_decision",
"A frail patient needs salvage pharyngeal reconstruction after radiation but has poor lower-extremity arterial inflow and a prior radial-artery harvest. What should the attending do?",
["Harvest fibula anyway because it is the default flap","Reassess the reconstructive goal, vascular anatomy, donor-site constraints, and alternative regional/free-tissue options before committing to a flap","Abandon reconstruction","Use irradiated local tissue only because donor evaluation is unnecessary"],1,
"Flap selection must account for patient-specific vascular anatomy and donor morbidity as well as defect needs. Preoperative vascular disease can contraindicate a preferred donor and should prompt alternative planning rather than forcing a standard flap.",
["Critical limb perfusion risk can make fibula harvest unsafe.","Correct. Reconstruction is an individualized systems problem.","Alternative reconstructive pathways usually exist.","Heavily irradiated local tissue may be unreliable and donor-site assessment remains essential."],
"The best flap is the best flap for this defect in this patient—not the flap used most often.","When is a pectoralis flap strategically preferable to a free flap in salvage surgery?","OR_prep"),

_q("v225_hn_orn_fnd","Osteoradionecrosis of the Jaw","foundation",
"What is osteoradionecrosis of the jaw?",
["Radiation-injured bone that becomes devitalized and fails to heal, after recurrent tumor has been excluded","Any dental pain after radiation","Metastatic bone disease by definition","Normal postoperative remodeling"],0,
"ORN reflects chronic radiation-related hypovascular, hypocellular tissue injury with exposed or necrotic bone and impaired healing; recurrent malignancy must be excluded when the presentation is atypical or progressive.",
["Correct. ORN is late radiation injury, but recurrent cancer remains an important mimic.","Dental pain alone does not establish ORN.","ORN is not metastatic disease by definition.","Persistent necrotic exposed bone is not normal remodeling."],
"In an irradiated jaw, never call destructive bone ORN until recurrence is adequately considered.","What dental and radiation-dose factors increase risk?"),
_q("v225_hn_orn_app","Osteoradionecrosis of the Jaw","application",
"A patient has limited exposed mandibular bone and pain after radiation but no fracture, fistula, or recurrent tumor. What is the best initial principle?",
["Start with severity-appropriate conservative management, meticulous oral care, control of infection/trauma, and close reassessment rather than immediate segmental resection","Perform mandibulectomy for every exposed bone focus","Give more radiation","Ignore symptoms indefinitely"],0,
"Early or limited ORN can often begin with conservative measures tailored to symptoms and extent. Surgery escalates as disease becomes refractory, structurally destructive, fistulizing, or complicated by fracture.",
["Correct. Treatment intensity should match disease severity.","Major resection is unnecessary for every limited lesion.","Additional radiation worsens tissue injury.","Progression can lead to infection, fistula, or fracture."],
"ORN exists on a spectrum; do not treat every exposed bone focus like a segmental defect.","What findings indicate progression to advanced ORN?"),
_q("v225_hn_orn_snr","Osteoradionecrosis of the Jaw","senior_decision",
"A patient has advanced mandibular ORN with pathologic fracture, draining fistula, severe pain, and nonviable bone after failed conservative therapy. What is the best senior-level strategy?",
["Continue the same conservative care indefinitely","Resect nonviable bone to healthy margins and reconstruct the segmental defect with well-vascularized tissue, often vascularized bone, after excluding recurrence","Give chronic topical steroid only","Avoid surgery because irradiated patients cannot heal any flap"],1,
"Advanced ORN with fracture or fistula is a structural failure problem. Definitive treatment often requires resection of necrotic bone and reconstruction with healthy vascularized tissue capable of healing in a previously irradiated field.",
["Persistent structural failure is unlikely to resolve with unchanged conservative care.","Correct. Advanced ORN often requires ablative and reconstructive surgery.","Topical steroid cannot restore a fractured necrotic mandible.","Vascularized reconstruction is specifically valuable because native irradiated tissue heals poorly."],
"Advanced ORN is a resection-and-reconstruction problem, not merely an infection problem.","How should recipient-vessel quality and prior neck dissection influence reconstructive planning?","OR_prep"),
]

def apply_learning_ladders_v225(challenges,item_id_fn):
    by_id={str(q.get("id")):q for q in challenges}; touched=0
    for qid,(topic,stage) in REUSED.items():
        q=by_id.get(qid)
        if not q: raise RuntimeError("v225 missing reused case: "+qid)
        q["topic"]=topic; q["learning_stage"]=stage; q["ladder_reviewed"]=True; q["concept_id"]=item_id_fn(DOMAIN,topic)
        mapping=REUSED_REASON_BY_CHOICE.get(qid,{})
        q["why_wrong"]=[mapping.get(c,"Use the clinical mechanism and management priority to distinguish this choice.") for c in q.get("choices",[])]
        touched+=1
    existing={str(q.get("id")) for q in challenges}; added=0
    for q in VIGNETTES_V225:
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v225 orphan: "+row["topic"])
        if row["id"] not in existing:
            challenges.append(row); existing.add(row["id"]); added+=1
    return {"reused":touched,"added":added,"reviewed_topics":5}
