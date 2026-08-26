"""v22.2 — Head & Neck Oncology learning-ladder pass 4.

Reviews canonical topics 16-20 from the live inventory: Carotid Body
Paraganglioma, Adverse Pathology and Adjuvant Therapy, Head & Neck Radiation
Toxicity / Survivorship, TEP and Alaryngeal Speech, and Neck Lymphoma.
"""
DOMAIN="Head & Neck Oncology"

def _q(qid,topic,stage,stem,choices,answer,explanation,why_wrong,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":why_wrong,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True}

VIGNETTES_V222=[
_q("v222_hn_cbp_fnd","Carotid Body Paraganglioma","foundation",
"A slowly enlarging painless upper neck mass is very vascular on imaging and splays the internal and external carotid arteries at the bifurcation. What is the most likely diagnosis?",
["Carotid body paraganglioma","Second branchial cleft cyst","Vagal schwannoma","Metastatic thyroid carcinoma"],0,
"Carotid body paragangliomas arise at the carotid bifurcation and classically produce splaying of the internal and external carotid arteries (the lyre-sign pattern).",
["Correct. The carotid-bifurcation origin and arterial splaying are characteristic.","A branchial cyst is not a hypervascular bifurcation-centered mass.","A vagal schwannoma usually displaces rather than splays the internal and external carotids at their bifurcation.","Metastatic thyroid carcinoma does not characteristically center on and splay the carotid bifurcation."],
"For a hypervascular carotid-space mass, displacement anatomy often tells you the compartment and likely origin.","What additional history should raise concern for a hereditary paraganglioma syndrome?"),
_q("v222_hn_cbp_app","Carotid Body Paraganglioma","application",
"A 34-year-old has bilateral carotid body tumors and a family history of similar tumors. Before planning treatment, what additional principle is most important?",
["Treat each as an isolated sporadic tumor","Pursue hereditary paraganglioma evaluation and assess for multifocal disease before committing to bilateral interventions","Perform bilateral open biopsy","Ignore cranial-nerve function because these tumors are benign"],1,
"Young age, bilaterality, multifocality, and family history increase the likelihood of a germline susceptibility syndrome. Genetic evaluation and whole-patient tumor assessment can materially change surveillance and sequencing of treatment.",
["The phenotype is strongly suggestive of hereditary disease.","Correct. Genetics and multifocal-disease assessment should precede irreversible bilateral treatment decisions.","Open biopsy of a hypervascular paraganglioma is hazardous and usually unnecessary when imaging is characteristic.","Lower cranial-nerve morbidity is a major determinant of treatment strategy even for histologically benign tumors."],
"Bilateral paragangliomas turn a local tumor problem into a lifetime cranial-nerve and hereditary-risk problem.","How would pre-existing contralateral vagal dysfunction change the sequence of treatment?"),
_q("v222_hn_cbp_snr","Carotid Body Paraganglioma","senior_decision",
"A large carotid body paraganglioma encases the carotid bifurcation and extends high in the neck. The opposite vagus is weak from prior surgery. What should dominate the attending-level treatment discussion?",
["Tumor size alone mandates immediate resection","Balance tumor control against carotid and lower-cranial-nerve morbidity; observation or radiation may be preferable when surgery risks catastrophic bilateral functional loss","Open biopsy before deciding","Routine sacrifice of the internal carotid without vascular assessment"],1,
"Management is individualized by growth, symptoms, age, secretory/hereditary status, vascular involvement, and expected cranial-nerve morbidity. A technically removable tumor is not automatically the best tumor to remove when the functional price is extreme.",
["Size matters, but it does not override the consequences of bilateral lower-cranial-nerve dysfunction.","Correct. Treatment should optimize lifetime tumor control and function rather than default to resection.","Characteristic hypervascular lesions generally do not require hazardous open biopsy.","Carotid sacrifice requires rigorous cerebrovascular planning and is not routine."],
"For paraganglioma, resectability and wisdom of resection are different questions.","When might preoperative embolization be considered, and what risks must be discussed?","OR_prep"),

_q("v222_hn_adv_fnd","Adverse Pathology and Adjuvant Therapy","foundation",
"After resection of oral cavity SCC, final pathology shows a positive microscopic margin and extranodal extension in a metastatic cervical node. Which postoperative framework is most appropriate?",
["Observation only","Postoperative concurrent chemoradiation if the patient can tolerate it","Radiation is contraindicated after surgery","Chemotherapy alone is always sufficient"],1,
"Positive margins and extranodal extension are classic high-risk pathologic findings for which postoperative concurrent chemoradiation provides the standard intensification framework in appropriately fit patients.",
["These are high-risk features with substantial locoregional recurrence risk.","Correct. Positive margin and extranodal extension are the key classic indications for postoperative chemoradiation in a fit patient.","Postoperative radiation is central to adjuvant treatment of high-risk resected HNSCC.","Systemic therapy alone does not replace indicated postoperative local-regional radiation."],
"After HNSCC surgery, distinguish features that justify PORT from the highest-risk findings that justify adding concurrent systemic therapy.","How would severe renal dysfunction alter the systemic-therapy discussion?"),
_q("v222_hn_adv_app","Adverse Pathology and Adjuvant Therapy","application",
"An oral tongue SCC is completely resected with negative margins. Pathology shows pT3 disease, perineural invasion, and two ipsilateral nodes without extranodal extension. What is the best general adjuvant principle?",
["No further therapy because margins are negative","Recommend postoperative radiation based on adverse intermediate-risk pathology; concurrent chemotherapy is not automatically indicated without a high-risk feature such as positive margin or extranodal extension","Give chemotherapy alone","Repeat the glossectomy solely because perineural invasion is present"],1,
"Negative margins do not eliminate recurrence risk. T3/T4 disease, nodal burden, perineural invasion, lymphovascular invasion, and other adverse features can support postoperative radiation, while concurrent chemotherapy is generally reserved for the highest-risk pathologic settings.",
["Margin status is only one component of postoperative risk.","Correct. This is an adjuvant-radiation problem, not automatically a chemoradiation problem.","Chemotherapy alone does not provide the required locoregional adjuvant treatment.","Perineural invasion influences adjuvant therapy but does not by itself require wider resection when the surgical margin is adequate."],
"Adjuvant therapy is pathology-driven: read the entire specimen, not just the margin line.","Which nodal and primary-site features most strongly alter postoperative radiation volumes?"),
_q("v222_hn_adv_snr","Adverse Pathology and Adjuvant Therapy","senior_decision",
"A frail patient has resected HNSCC with extranodal extension but severe chronic kidney disease, hearing loss, neuropathy, and poor performance status. What is the best senior-level principle?",
["Cisplatin must be given regardless of toxicity risk","Preserve the oncologic rationale for treatment intensification while individualizing systemic therapy or radiation-alone options through multidisciplinary assessment of competing toxicity and benefit","Omit all adjuvant therapy automatically","Delay the decision until recurrence"],1,
"High-risk pathology establishes the reason to consider postoperative treatment intensification, but regimen selection must account for cisplatin fitness, renal function, hearing, neuropathy, performance status, and patient goals. Contraindication to standard cisplatin does not erase the need for multidisciplinary adjuvant planning.",
["Severe renal, auditory, neurologic, and functional comorbidity can make cisplatin unsafe.","Correct. Pathologic risk and treatment fitness must both be respected.","High-risk pathology still carries substantial recurrence risk even when standard systemic therapy is unsuitable.","Waiting for recurrence forfeits the purpose of adjuvant therapy."],
"The indication for intensification and the patient's ability to tolerate the standard intensifier are separate decisions.","How would a truly positive surgical margin change the discussion about re-resection before adjuvant therapy?"),

_q("v222_hn_rts_fnd","Head & Neck Radiation Toxicity / Survivorship","foundation",
"Years after head-and-neck radiation, a patient has progressive xerostomia, dental decay, dysphagia, neck fibrosis, and hypothyroidism. What is the best overarching principle?",
["These are unrelated aging changes","Head-and-neck radiation produces important late toxicities requiring lifelong multidisciplinary surveillance and prevention","Late toxicity ends one year after treatment","Only cancer recurrence should be monitored"],1,
"Radiation survivorship includes chronic salivary dysfunction, dental disease, dysphagia/aspiration, fibrosis, thyroid dysfunction, carotid disease, lymphedema, and other late effects that may evolve for years.",
["The clustered late effects are characteristic of prior head-and-neck radiation.","Correct. Survivorship is active longitudinal care, not merely recurrence surveillance.","Late radiation injury can emerge or progress many years after treatment.","Functional and medical late effects materially affect morbidity and quality of life."],
"Cancer control is only one survivorship endpoint; swallowing, teeth, thyroid, vessels, fibrosis, and nutrition remain long-term ENT concerns.","What preventive dental strategy is especially important before and after high-dose mandibular radiation?"),
_q("v222_hn_rts_app","Head & Neck Radiation Toxicity / Survivorship","application",
"A disease-free survivor of chemoradiation develops recurrent pneumonias, weight loss, and coughing with meals five years later. Flexible laryngoscopy shows no tumor recurrence. What is the best next step?",
["Reassure because the cancer is gone","Evaluate for late radiation-associated dysphagia and aspiration with formal swallowing assessment and multidisciplinary rehabilitation","Start antibiotics indefinitely without evaluating swallowing","Perform neck dissection"],1,
"Late radiation fibrosis and neuromuscular dysfunction can produce progressive dysphagia and silent aspiration long after treatment. Recurrent pneumonia and weight loss warrant objective swallowing assessment and targeted rehabilitation/nutrition planning.",
["Absence of recurrence does not make aspiration symptoms benign.","Correct. Late dysphagia can be progressive and clinically dangerous.","Antibiotics treat episodes of infection but not the aspiration mechanism.","Neck dissection does not address radiation-associated swallowing dysfunction."],
"In a head-and-neck cancer survivor, recurrent pneumonia may be the presenting sign of late swallowing failure.","What findings would make aspiration-prevention surgery enter the discussion?"),
_q("v222_hn_rts_snr","Head & Neck Radiation Toxicity / Survivorship","senior_decision",
"A long-term oropharyngeal cancer survivor has severe mandibular pain and exposed bone after dental extraction in a previously high-dose radiation field. Imaging suggests osteoradionecrosis without recurrent tumor. What should guide management?",
["Treat every case with immediate segmental mandibulectomy","Stage the extent and consequences of osteoradionecrosis, exclude recurrence, optimize oral care/infection control and escalate from conservative measures to vascularized reconstruction when disease is advanced or structurally threatening","Assume exposed bone always represents recurrent SCC","Give additional radiation"],1,
"Osteoradionecrosis exists on a spectrum. Management depends on extent, infection, fracture/fistula, pain, dental status, prior dose, and response to conservative therapy; advanced destructive disease may require resection and vascularized bone reconstruction.",
["Limited disease can often begin with less morbid management.","Correct. Treatment should match severity while maintaining vigilance for recurrent malignancy.","Recurrence must be excluded, but exposed irradiated bone is not synonymous with cancer.","Additional radiation worsens tissue injury rather than treating osteoradionecrosis."],
"Late radiation injury is a tissue-vascularity problem; advanced reconstruction succeeds by bringing healthy vascularized tissue into the field.","Which clinical findings suggest impending pathologic fracture or need for segmental reconstruction?","OR_prep"),

_q("v222_hn_tep_fnd","TEP and Alaryngeal Speech","foundation",
"After total laryngectomy, how does a tracheoesophageal puncture prosthesis generate voice?",
["Pulmonary air is diverted through a one-way prosthesis into the esophagus/pharyngoesophageal segment to create vibration for speech","The prosthesis reconnects the larynx to the trachea","It electrically stimulates the tongue","It restores normal vocal folds"],0,
"TEP speech uses pulmonary airflow routed through a one-way tracheoesophageal voice prosthesis to vibrate the pharyngoesophageal segment. It does not recreate the removed larynx.",
["Correct. Pulmonary air powers vibration of the reconstructed pharyngoesophageal sound source.","The larynx has been removed and is not reconnected.","TEP is an aerodynamic rather than tongue-stimulation system.","Normal vocal folds are absent after total laryngectomy."],
"TEP preserves pulmonary-powered speech, not laryngeal phonation.","How do esophageal speech and an electrolarynx differ from TEP speech?"),
_q("v222_hn_tep_app","TEP and Alaryngeal Speech","application",
"A laryngectomy patient with a TEP suddenly coughs when drinking liquids. Examination shows fluid leaking through the center of the prosthesis. What is the most likely problem?",
["Central prosthesis valve failure requiring prosthesis assessment/replacement","Carotid blowout","Normal TEP function","Bilateral vocal fold paralysis"],0,
"Leakage through the prosthesis usually reflects failure of the one-way valve, biofilm/debris, or prosthesis dysfunction and commonly prompts cleaning or replacement after appropriate evaluation.",
["Correct. Transprosthetic central leakage points to valve/prosthesis dysfunction.","Carotid blowout presents with hemorrhage, not reproducible liquid passage through the prosthesis.","A functioning one-way prosthesis should prevent swallowed liquid from entering the trachea.","The vocal folds have been removed after total laryngectomy."],
"For TEP leakage, distinguish leakage through the prosthesis from leakage around it—the mechanism and management differ.","What does periprosthetic leakage suggest about tract size, prosthesis fit, or tissue quality?"),
_q("v222_hn_tep_snr","TEP and Alaryngeal Speech","senior_decision",
"A salvage-laryngectomy patient wants primary TEP, but the pharyngeal closure is tenuous in a heavily irradiated field and major flap reconstruction is required. What is the best planning principle?",
["Primary TEP is mandatory for every patient","Individualize primary versus secondary TEP based on wound risk, reconstruction, pulmonary/manual dexterity factors, rehabilitation access, and patient goals","TEP is contraindicated after all radiation","Speech rehabilitation should wait until after recurrence surveillance ends"],1,
"Primary TEP can provide excellent rehabilitation, but timing is individualized. Extensive salvage reconstruction, fistula risk, tissue quality, pulmonary status, cognition/dexterity, support, and access to speech-language pathology all influence whether primary or delayed secondary puncture is preferable.",
["There is no universal requirement for primary puncture.","Correct. Voice rehabilitation should be planned prospectively but tailored to surgical and patient factors.","Prior radiation does not universally preclude TEP.","Communication rehabilitation is part of cancer care and should not be deferred for years."],
"TEP timing is a rehabilitation decision embedded inside reconstructive and wound-risk planning.","How would inability to occlude the stoma manually affect device and rehabilitation planning?","OR_prep"),

_q("v222_hn_lym_fnd","Neck Lymphoma","foundation",
"An adult has persistent painless cervical adenopathy, night sweats, and weight loss. Imaging shows multiple enlarged nodes without an obvious mucosal primary. What diagnostic principle is most important?",
["Assume metastatic SCC and perform neck dissection","Obtain tissue in a way that preserves architecture and allows lymphoma phenotyping when lymphoma is suspected","Treat with prolonged antibiotics before any diagnosis","FNA cytology alone is always sufficient for every lymphoma"],1,
"Lymphoma diagnosis often requires adequate tissue for architecture, immunophenotyping, flow cytometry, and molecular studies. The biopsy strategy should be coordinated with pathology rather than treating the neck as a metastatic-SCC operation.",
["The systemic symptoms and nodal pattern require a lymphoma-aware diagnostic pathway.","Correct. Tissue handling and architecture can be crucial for classification.","Persistent constitutional symptoms and adenopathy should not be delayed by repeated empiric antibiotics.","FNA may suggest lymphoma but often cannot provide all information needed for definitive classification."],
"When lymphoma is in the differential, plan the biopsy with the pathologist before the specimen leaves the neck.","When can image-guided core biopsy provide adequate diagnosis and when is excisional biopsy preferable?"),
_q("v222_hn_lym_app","Neck Lymphoma","application",
"A patient with suspected cervical lymphoma needs an excisional node biopsy. Several nodes are available. Which operative principle is best?",
["Choose a representative accessible node and avoid unnecessary radical dissection while delivering fresh tissue promptly for the requested lymphoma studies","Remove every enlarged node","Place the specimen in formalin before asking pathology what studies are needed","Perform mucosal resection at the same time without an indication"],0,
"The goal is diagnosis with minimal morbidity. A representative accessible node is selected, crush/cautery artifact is minimized, and specimen handling is coordinated so fresh tissue is available for flow cytometry or other studies when requested.",
["Correct. Diagnostic adequacy and specimen handling matter more than the extent of surgery.","Lymphoma is systemic disease; therapeutic clearance of all cervical nodes is not the purpose of diagnostic biopsy.","Premature fixation can prevent some ancillary studies.","Unindicated mucosal surgery adds morbidity without improving lymphoma classification."],
"A lymphoma node biopsy is a specimen-quality operation, not a neck-dissection operation.","How would a deeply situated node adjacent to major vessels change the choice between core and excisional biopsy?","OR_prep"),
_q("v222_hn_lym_snr","Neck Lymphoma","senior_decision",
"A patient with a massive cervical/mediastinal lymphomatous mass has orthopnea and cannot tolerate lying flat. An excisional biopsy is requested. What should the surgeon prioritize?",
["Routine general anesthesia and paralysis because the operation is short","Recognize possible critical airway/mediastinal-mass physiology and coordinate the least destabilizing diagnostic strategy with anesthesia, oncology, pathology, and interventional teams","Delay all diagnosis for months","Perform bilateral neck dissections under general anesthesia"],1,
"Large mediastinal or cervical lymphoma can produce dynamic airway and cardiovascular compromise, especially with supine positioning or loss of spontaneous ventilation. The safest tissue strategy may be awake/local biopsy or another accessible site rather than routine induction.",
["Induction and positive-pressure ventilation can precipitate collapse in susceptible mediastinal-mass physiology.","Correct. The diagnostic plan must be subordinate to airway and hemodynamic safety.","Urgent diagnosis is often necessary to initiate disease-specific therapy.","Radical surgery increases risk and is not the treatment for systemic lymphoma."],
"In lymphoma, the safest biopsy is the one that gets enough tissue without converting a diagnostic procedure into an airway catastrophe.","What preoperative symptoms and imaging features make anesthesia particularly hazardous?","overnight_call"),
]

def apply_learning_ladders_v222(challenges,item_id_fn):
    existing={str(q.get("id")) for q in challenges}
    added=0
    for q in VIGNETTES_V222:
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v222 orphan: "+row["topic"])
        if row["id"] not in existing:
            challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":5}
