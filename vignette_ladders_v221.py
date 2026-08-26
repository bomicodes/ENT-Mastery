"""v22.1 — Head & Neck Oncology learning-ladder pass 3.

Reviews canonical topics 11-15: Hypopharyngeal Cancer, Nasopharyngeal
Carcinoma, Laryngeal Preservation Decision, Total Laryngectomy, and
Parapharyngeal Space Tumor. Existing high-value cases are retained when they
supply a distinct stage; older generic distractor rationales are replaced.
"""
DOMAIN = "Head & Neck Oncology"

REUSED = {
    "v138_hn_11": ("Hypopharyngeal Cancer", "foundation"),
    "v145_hn_08": ("Hypopharyngeal Cancer", "application"),
    "v128_hn_10": ("Nasopharyngeal Carcinoma", "foundation"),
    "v128_hn_05": ("Laryngeal Preservation Decision", "foundation"),
    "v138_hn_18": ("Parapharyngeal Space Tumor", "foundation"),
    "v143_hno_05": ("Parapharyngeal Space Tumor", "application"),
}

REUSED_REASON_BY_CHOICE = {
    "v138_hn_11": {
        "It often presents late with substantial nodal burden and requires explicit functional as well as oncologic planning": "Correct. Hypopharyngeal SCC commonly presents at advanced stage with significant nodal and swallowing morbidity.",
        "It almost never metastasizes to the neck": "Hypopharyngeal cancers frequently present with cervical nodal disease because of rich lymphatic drainage.",
        "It is usually cured by local excision alone": "Advanced presentation and regional disease commonly require multimodality treatment rather than simple local excision.",
        "HPV status determines all staging": "HPV-mediated staging is specific to p16-positive oropharyngeal cancer and does not define all hypopharyngeal staging.",
    },
    "v145_hn_08": {
        "Treat as a simple mucosal excision": "A fixed hemilarynx and bulky nodal disease signal advanced functional and oncologic disease that cannot be treated as a minor local excision.",
        "Assess laryngeal function, extent, nodal burden, nutrition, and candidacy for organ-preservation chemoradiation versus ablative surgery": "Correct. Treatment must integrate disease control with whether the laryngopharynx can remain safe and functional.",
        "Neck nodes do not matter": "Nodal burden is prognostically important and directly affects treatment fields and modality selection.",
        "Voice preservation always outweighs aspiration risk": "An anatomically preserved larynx that chronically aspirates is not a successful functional outcome.",
    },
    "v138_hn_18": {
        "Deep-lobe salivary tumor such as pleomorphic adenoma": "Correct. A prestyloid mass with continuity to the deep parotid lobe strongly favors salivary origin.",
        "Carotid body paraganglioma": "Carotid body tumors arise at the bifurcation and classically splay the internal and external carotid arteries rather than present as a deep-parotid prestyloid mass.",
        "Vagal schwannoma": "Vagal schwannoma is typically poststyloid and produces a different carotid-jugular displacement pattern.",
        "Glottic SCC": "A glottic mucosal cancer does not present as a deep prestyloid parapharyngeal mass with parotid continuity.",
    },
    "v143_hno_05": {
        "Deep-lobe parotid/salivary origin": "Correct. Prestyloid location plus posteromedial displacement of the carotid space and deep-parotid continuity supports a salivary origin.",
        "Vagal schwannoma": "Vagal schwannomas are poststyloid neurogenic tumors and usually separate/displace carotid and jugular structures differently.",
        "Carotid body tumor": "Carotid body tumors center on the carotid bifurcation rather than the prestyloid deep-parotid compartment.",
        "Thyroid nodule": "Thyroid nodules arise in the visceral neck and do not create this parapharyngeal displacement pattern.",
    },
}


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong, pearl, curveball, focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,
            "stem":stem,"choices":choices,"answer":answer,"explanation":explanation,
            "why_wrong":why_wrong,"board_pearl":pearl,"curveball":curveball,
            "tier":"Curated learning ladder","mode":"Vignette","focus":focus,
            "ladder_reviewed":True}

VIGNETTES_V221 = [
    _q("v221_hn_hypo_snr","Hypopharyngeal Cancer","senior_decision",
       "A patient with advanced pyriform-sinus SCC has a fixed larynx, profound baseline dysphagia, recurrent aspiration pneumonia, and feeding-tube dependence. The tumor could technically receive definitive chemoradiation. Which treatment principle is most appropriate?",
       ["Choose organ preservation automatically because retaining the larynx is always superior","Include baseline swallowing and airway function in modality selection; an already nonfunctional laryngopharynx may favor ablative surgery with reconstruction","Ignore nutrition because it does not affect treatment tolerance","Observe until distant metastasis develops"],1,
       "Organ-preservation protocols can control selected hypopharyngeal cancers, but preserving an organ that is already unsafe for swallowing may produce severe chronic morbidity. Baseline aspiration, pulmonary reserve, nutrition, tumor extent, and reconstructive options should influence whether definitive chemoradiation or laryngopharyngectomy is the better overall treatment package.",
       ["An anatomically retained but chronically aspirating larynx may not be a functional success.","Correct. Functional status is part of oncologic treatment selection, not merely an outcome measured later.","Nutrition strongly affects treatment tolerance, wound healing, and rehabilitation.","Waiting for progression can sacrifice curative options."],
       "In hypopharyngeal cancer, organ preservation only matters when the preserved organ can function safely.",
       "What reconstructive options can restore pharyngeal continuity after circumferential versus partial pharyngeal defects?","boards"),

    _q("v221_hn_npc_app","Nasopharyngeal Carcinoma","application",
       "A patient has nonkeratinizing nasopharyngeal carcinoma with bulky bilateral cervical nodal disease but no distant metastases. What is the standard treatment framework?",
       ["Primary open nasopharyngectomy with no neck treatment","Definitive radiation-based therapy to the primary and bilateral neck, with concurrent systemic therapy for appropriately advanced disease","Observation because EBV-associated tumors are indolent","Neck dissection alone"],1,
       "Nasopharyngeal carcinoma is generally managed nonsurgically because of its anatomic location and radiosensitivity. Modern definitive therapy uses intensity-modulated radiation to the nasopharynx and regional nodes, with concurrent chemotherapy for appropriate locoregionally advanced disease.",
       ["Primary open surgery is not the routine first-line strategy for locoregionally advanced NPC.","Correct. Radiation is the backbone, with systemic therapy added according to stage and risk.","NPC can be aggressive and nodal disease requires definitive treatment.","Treating only the neck leaves the mucosal primary and bilateral at-risk pathways untreated."],
       "NPC is one of the head-and-neck cancers where radiation is usually the primary local treatment, not surgery.",
       "How does plasma EBV DNA, where validated, contribute to pretreatment assessment or surveillance?","boards"),
    _q("v221_hn_npc_snr","Nasopharyngeal Carcinoma","senior_decision",
       "After definitive chemoradiation for nasopharyngeal carcinoma, a patient has a persistent isolated neck node on appropriate post-treatment reassessment while the nasopharyngeal primary appears controlled and there is no distant disease. What is the best senior-level principle?",
       ["Assume all residual nodes are sterile and never intervene","Consider salvage neck dissection for persistent regional disease after multidisciplinary confirmation of residual malignancy and resectability","Perform total laryngectomy","Treat with antibiotics indefinitely"],1,
       "Persistent or recurrent isolated cervical disease after definitive treatment can be amenable to salvage neck surgery in appropriately selected NPC patients. The decision requires confirmation of viable disease, assessment for distant metastasis, prior radiation effects, and surgical morbidity.",
       ["Residual masses may represent fibrosis, but proven persistent nodal carcinoma cannot simply be ignored.","Correct. Salvage surgery can provide regional control when disease is isolated and resectable.","Laryngectomy does not address nasopharyngeal nodal persistence.","Antibiotics do not eradicate residual metastatic carcinoma."],
       "NPC is usually treated nonsurgically up front, but surgery still has an important salvage role for selected persistent regional disease.",
       "How does prior high-dose neck radiation change wound, cranial-nerve, and carotid risk during salvage surgery?","OR_prep"),

    _q("v221_hn_pres_app","Laryngeal Preservation Decision","application",
       "A patient with locally advanced laryngeal SCC has a technically resectable tumor but already requires a tracheostomy, aspirates secretions, and has a nearly fixed larynx. What should most influence whether to pursue a nonsurgical organ-preservation pathway?",
       ["Tumor resectability alone","Whether the larynx is functionally preservable and whether chemoradiation is likely to leave a safe airway and swallow","The patient's hair color","Whether a neck dissection can be avoided"],1,
       "The goal of laryngeal preservation is not merely to avoid removing the organ. Pretreatment tracheostomy dependence, aspiration, cartilage destruction, poor pulmonary reserve, and severe baseline dysfunction can predict an anatomically preserved but nonfunctional larynx and should shape modality selection.",
       ["Resectability does not answer whether a preserved larynx would function safely.","Correct. Functional candidacy is central to an organ-preservation decision.","Hair color has no relevance to treatment selection.","Neck management is only one component and does not override primary functional considerations."],
       "Organ preservation should preserve useful function, not merely anatomy.",
       "Which T4 features or cartilage/extralaryngeal extension patterns tend to shift the discussion toward total laryngectomy?","boards"),
    _q("v221_hn_pres_snr","Laryngeal Preservation Decision","senior_decision",
       "A patient strongly wants to avoid laryngectomy. Imaging shows a bulky laryngeal tumor with frank cartilage penetration and extralaryngeal soft-tissue extension, and the patient has poor baseline swallowing. What is the best attending-level counseling approach?",
       ["Promise chemoradiation will preserve both anatomy and normal function","Explain that treatment selection must prioritize oncologic control and realistic function; primary total laryngectomy may offer the better cure/function tradeoff in selected extensive T4 disease","Refuse to discuss patient preferences","Offer observation until airway obstruction occurs"],1,
       "Some advanced laryngeal cancers—especially those with extensive cartilage destruction/extralaryngeal extension and poor baseline function—are poor candidates for nonsurgical preservation. Shared decision-making should distinguish the desire to avoid laryngectomy from the probability of durable control and a functional retained organ.",
       ["Chemoradiation cannot guarantee either cure or normal laryngeal function in extensive disease.","Correct. Counseling should be preference-sensitive but evidence- and function-grounded.","Patient goals matter and should be incorporated rather than dismissed.","Delay can worsen airway risk and reduce curative options."],
       "A technically preservable larynx is not necessarily an oncologically or functionally wise larynx to preserve.",
       "How would a disease-free but chronically aspirating larynx years after chemoradiation reopen the surgical discussion?","boards"),

    _q("v221_hn_tl_fnd","Total Laryngectomy","foundation",
       "After total laryngectomy, which statement about airway anatomy is correct?",
       ["The patient breathes permanently through a neck stoma that is completely separated from the mouth and nose","The patient can be orally intubated in an emergency","The trachea remains connected to the pharynx","The nose remains the primary route for ventilation"],0,
       "Total laryngectomy permanently separates the respiratory and alimentary tracts by bringing the trachea to the skin as an end stoma. This anatomy is fundamental for emergency airway care: oxygenation and intubation must occur through the stoma, not the mouth or nose.",
       ["Correct. A laryngectomy stoma is the only airway to the lungs.","Oral intubation cannot reach the trachea after complete laryngectomy.","The operation intentionally separates the trachea from the pharynx.","Nasal airflow no longer ventilates the lungs after total laryngectomy."],
       "A laryngectomee is a neck breather: all emergency oxygen and airway instrumentation go to the stoma.",
       "How does this differ from a patient with a tracheostomy whose larynx remains anatomically connected to the trachea?","overnight_call"),
    _q("v221_hn_tl_app","Total Laryngectomy","application",
       "On postoperative day 6 after total laryngectomy, a patient develops neck erythema, fever, and saliva appearing in the drain. What complication is most likely?",
       ["Pharyngocutaneous fistula","BPPV","Acute otitis externa","Isolated shoulder neuropraxia"],0,
       "Salivary leakage into the neck after pharyngeal closure is a pharyngocutaneous fistula. Risk is increased by prior radiation, poor nutrition, anemia, hypothyroidism, infection, and wound factors. Management depends on defect size, sepsis, vessel exposure, tissue quality, and prior treatment.",
       ["Correct. Saliva in a neck drain after pharyngeal closure is the classic clue.","BPPV causes positional vertigo and does not explain a salivary neck leak.","Otitis externa is unrelated to the pharyngeal closure.","Shoulder dysfunction does not cause fever or salivary drainage."],
       "After laryngectomy, a salivary neck leak is not just a wound issue—it can threaten carotid coverage and delay rehabilitation.",
       "Which findings make conservative fistula care unsafe and push toward operative debridement or vascularized tissue coverage?","postoperative_call"),
    _q("v221_hn_tl_snr","Total Laryngectomy","senior_decision",
       "A heavily irradiated salvage-laryngectomy patient has a tenuous pharyngeal closure with poor tissue quality. What reconstructive principle should the attending consider at the index operation?",
       ["Avoid vascularized tissue because prior radiation makes flaps impossible","Consider prophylactic well-vascularized tissue reinforcement or reconstruction to reduce fistula and protect major vessels when risk is high","Close the skin tightly and ignore the pharyngeal tension","Delay all reconstruction until a fistula develops"],1,
       "Prior chemoradiation substantially worsens tissue vascularity and healing. In selected high-risk salvage laryngectomy patients, bringing nonirradiated vascularized tissue—such as a pectoralis onlay or free-tissue reconstruction—can reinforce the pharyngeal closure and reduce the consequences of breakdown.",
       ["Vascularized tissue is often particularly valuable in irradiated fields.","Correct. Reconstruction should anticipate wound biology rather than waiting for predictable failure.","Skin closure does not compensate for a high-tension poorly vascularized pharyngeal repair.","Reactive reconstruction after major breakdown may be more morbid than planned reinforcement in a high-risk field."],
       "In salvage laryngectomy, reconstruction is often prophylaxis against irradiated wound biology, not merely defect filling.",
       "How do circumferential versus partial pharyngeal defects change flap selection and stricture risk?","OR_prep"),

    _q("v221_hn_pps_snr","Parapharyngeal Space Tumor","senior_decision",
       "A large poststyloid parapharyngeal tumor extends to the skull base and displaces the internal carotid artery. The patient has mild preoperative vagal weakness. What is the best senior-level planning principle?",
       ["Open biopsy before reviewing vascular anatomy","Define likely nerve of origin, carotid/jugular relationships, skull-base extension, contralateral lower-cranial-nerve function, and expected functional morbidity before selecting an approach","Assume all parapharyngeal tumors can be removed transorally","Sacrifice the carotid routinely"],1,
       "Poststyloid parapharyngeal tumors are often neurogenic and can be intimately related to the carotid sheath and lower cranial nerves. Approach selection must anticipate the likely nerve of origin, vascular control, skull-base access, and consequences of new vagal or sympathetic deficits rather than focusing only on tumor removal.",
       ["Unplanned biopsy can create bleeding or nerve injury and is unnecessary for many imaging-characteristic lesions.","Correct. The operative plan begins with compartment, displacement anatomy, and expected neurologic cost.","Transoral access may provide inadequate vascular control for large poststyloid skull-base tumors.","Carotid sacrifice is not routine and requires a highly specific oncologic/vascular indication and planning."],
       "In the parapharyngeal space, the morbidity is often predicted by which nerve or vessel the mass arose from before you ever make an incision.",
       "How would a vagal schwannoma versus sympathetic-chain schwannoma differ in carotid/jugular displacement and postoperative counseling?","OR_prep"),
]


def _align(qid,q):
    mapping=REUSED_REASON_BY_CHOICE.get(qid)
    if mapping:
        q["why_wrong"]=[mapping.get(str(c),"This choice does not match the case-specific oncologic principle.") for c in list(q.get("choices") or [])]


def apply_learning_ladders_v221(challenges,item_id_fn):
    by_id={q.get("id"):q for q in challenges if q.get("id")}
    reused=[]
    for qid,(topic,stage) in REUSED.items():
        q=by_id.get(qid)
        if q is None: raise RuntimeError(f"v22.1: expected reusable question missing: {qid}")
        q["domain"]=DOMAIN; q["topic"]=topic; q["concept_id"]=item_id_fn(DOMAIN,topic)
        q["learning_stage"]=stage; q["ladder_reviewed"]=True; _align(qid,q); reused.append(qid)
    existing=set(by_id); added=[]
    for row in VIGNETTES_V221:
        if row["id"] in existing: continue
        item=dict(row); item["concept_id"]=item_id_fn(DOMAIN,item["topic"])
        challenges.append(item); existing.add(item["id"]); added.append(item["id"])
    return {"reused":reused,"added":added,"topics":["Hypopharyngeal Cancer","Nasopharyngeal Carcinoma","Laryngeal Preservation Decision","Total Laryngectomy","Parapharyngeal Space Tumor"]}
