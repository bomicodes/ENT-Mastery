"""v23.5 — Thyroid / Parathyroid / Salivary learning-ladder pass 3.

Reviews canonical topics 11-15 from the live inventory: Submandibular
Sialolithiasis, Sialendoscopy, Submandibular Gland Excision, Graves Disease /
Toxic Goiter, and Indeterminate Thyroid Cytology / Molecular Testing.
"""
DOMAIN="Thyroid / Parathyroid / Salivary"

REUSED={"v143_tps_02":("Indeterminate Thyroid Cytology / Molecular Testing","application")}
REUSED_REASON_BY_CHOICE={
"v143_tps_02":{
"Use molecular testing as an adjunct to refine malignancy risk and help choose surveillance versus diagnostic surgery in the context of ultrasound, pretest risk, patient values, and the specific assay":"Correct. Molecular testing can meaningfully refine risk in selected Bethesda III/IV nodules, but its predictive value depends on pretest prevalence and it should inform rather than replace clinical judgment.",
"Molecular testing proves with certainty whether every nodule is benign or malignant":"No molecular assay is perfectly definitive; performance and predictive values vary by platform and pretest risk.",
"Molecular testing is useful only after total thyroidectomy":"Testing is most useful before definitive surgery when an indeterminate FNA leaves uncertainty about whether surgery is needed or how extensive it should be.",
"Ignore ultrasound and cytology once a molecular result is available":"Molecular data must be integrated with ultrasound phenotype, cytology, clinical risk, and patient preference rather than interpreted in isolation."}}

def _q(qid,topic,stage,stem,choices,answer,explanation,why_wrong,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":why_wrong,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True}

VIGNETTES_V235=[
_q("v235_tps_smstone_fnd","Submandibular Sialolithiasis","foundation",
"A patient has recurrent painful swelling under the jaw every time they eat. Bimanual palpation finds a hard focus in the floor of mouth along Wharton duct. What is the most likely diagnosis?",
["Submandibular sialolithiasis","Parotid malignancy","Thyroglossal duct cyst","Peritonsillar abscess"],0,
"Meal-triggered submandibular pain and swelling with a palpable ductal calculus is classic obstructive submandibular sialolithiasis. The submandibular gland is particularly prone to stones because of its mucous-rich saliva and long uphill duct course.",
["Correct. The temporal relationship to salivary stimulation and ductal stone localize the problem.","A parotid tumor does not usually cause reproducible meal-triggered submandibular swelling.","A thyroglossal cyst is a midline developmental lesion rather than an obstructed Wharton duct.","A peritonsillar abscess presents with acute pharyngeal infection, not recurrent meal-related gland swelling."],
"Recurrent swelling with meals is salivary obstruction until proven otherwise.","Which stone locations are most accessible to transoral removal versus endoscopic or combined approaches?"),
_q("v235_tps_smstone_app","Submandibular Sialolithiasis","application",
"Ultrasound shows a mobile distal Wharton-duct stone in a patient with recurrent obstructive symptoms but no abscess. What treatment principle best preserves gland function?",
["Choose a gland-preserving ductal approach such as transoral stone removal or sialendoscopic management based on size and location before defaulting to gland excision","Excise the submandibular gland for every stone","Treat indefinitely with antibiotics despite no infection","Observe until the gland becomes permanently fibrotic"],0,
"Most accessible ductal stones can be treated with gland-preserving techniques. Distal stones may be removed transorally, while endoscopic or combined approaches can address selected more proximal disease; gland excision is generally reserved for disease not amenable to conservative or minimally invasive management.",
["Correct. Modern management is location- and anatomy-driven with gland preservation when feasible.","Routine gland excision creates avoidable nerve and scar morbidity for many accessible stones.","Antibiotics treat bacterial sialadenitis, not the obstructing calculus itself.","Waiting for repeated inflammation can worsen ductal stenosis and gland damage."],
"Treat the obstruction, not just each inflammatory flare.","How does an intraparenchymal or impacted hilar stone change the discussion?","OR_prep"),
_q("v235_tps_smstone_snr","Submandibular Sialolithiasis","senior_decision",
"A patient has a large impacted hilar submandibular stone, recurrent infections, and a functioning gland. Endoscopic retrieval alone is unlikely. What is the best senior-level principle?",
["Automatically excise the gland","Consider a combined endoscopic-transoral gland-preserving approach when expertise and anatomy permit, while counseling that gland excision may be necessary if safe stone clearance is not achievable","Break the stone blindly with forceps","Leave the obstruction untreated permanently"],1,
"Large hilar stones may require a combined approach that uses endoscopy for localization and transoral access for removal. The decision depends on duct anatomy, stone position, gland function, prior infection, and local expertise; submandibular gland excision remains a fallback rather than an automatic first step.",
["Gland excision can be appropriate but is not mandatory for every proximal stone.","Correct. The least morbid approach that reliably clears obstruction and preserves function should be considered.","Blind instrumentation risks duct perforation, lingual-nerve injury, and incomplete treatment.","Persistent obstruction predisposes to recurrent pain, infection, and gland damage."],
"A proximal stone is an access problem, not automatically a gland-removal problem.","Where is the lingual nerve relative to Wharton duct during a transoral hilar approach?","OR_prep"),

_q("v235_tps_sialendo_fnd","Sialendoscopy","foundation",
"What is the primary role of diagnostic and interventional sialendoscopy?",
["Directly visualize the salivary duct system and treat selected obstructive stones, mucus plugs, or stenoses while preserving the gland","Stage thyroid cancer","Biopsy the vocal folds","Treat cervical lymph-node metastases"],0,
"Sialendoscopy uses small-caliber endoscopes to inspect and intervene within the major salivary ducts. It can diagnose stenosis or obstructive debris and permit dilation, irrigation, basket retrieval, or assistance with combined stone procedures.",
["Correct. It is a gland-preserving ductal diagnostic and therapeutic platform.","Thyroid cancer staging does not involve salivary duct endoscopy.","Vocal-fold biopsy requires laryngeal evaluation, not sialendoscopy.","Cervical nodal disease is outside the salivary duct lumen."],
"Sialendoscopy treats the duct from the inside rather than removing the gland from the outside.","What anatomy makes submandibular duct endoscopy technically different from parotid duct endoscopy?"),
_q("v235_tps_sialendo_app","Sialendoscopy","application",
"During submandibular sialendoscopy for an obstructive stone, resistance increases and the duct wall begins to blanch. What is the safest principle?",
["Force the scope forward","Stop and reassess rather than forcing instrumentation, because duct perforation or false passage can convert a limited procedure into edema, extravasation, and future stenosis","Convert immediately to total parotidectomy","Use electrocautery blindly in the duct"],1,
"Sialendoscopy requires gentle serial dilation and controlled advancement under visualization. Force against resistance can perforate the duct or create a false passage, making continued endoscopy difficult and increasing postoperative edema and stenosis.",
["Forcing the scope risks duct injury.","Correct. Resistance is information that should trigger reassessment of access, dilation, or an alternate approach.","Parotidectomy is unrelated to a submandibular duct complication.","Blind thermal energy in a salivary duct risks tissue injury."],
"In sialendoscopy, resistance is a reason to change strategy—not push harder.","When should a combined transoral approach replace repeated attempts at purely endoscopic extraction?","OR_prep"),
_q("v235_tps_sialendo_snr","Sialendoscopy","senior_decision",
"A patient has recurrent obstructive submandibular symptoms from a tight proximal duct stenosis without a removable stone. What should guide treatment?",
["Assume gland excision is the only option","Use the endoscopic phenotype to individualize dilation, irrigation, temporary stenting or other duct-preserving measures, while recognizing refractory diffuse disease may still require gland-directed surgery","Prescribe antibiotics indefinitely without obstruction management","Perform thyroid lobectomy"],1,
"Sialendoscopy can define focal versus diffuse stenosis and permit minimally invasive treatment. Long-term success depends on the underlying inflammatory disease, length and severity of stenosis, gland reserve, and recurrence rather than one universal maneuver.",
["Many stenoses can be treated without immediate gland removal.","Correct. Management should match the actual ductal pathology and gland function.","Antibiotics do not correct noninfectious duct stenosis.","Thyroid surgery does not treat salivary obstruction."],
"The endoscope is valuable because it turns 'salivary swelling' into an anatomic duct diagnosis.","How would suspected Sjögren disease change expectations for durable symptom control?"),

_q("v235_tps_smgex_fnd","Submandibular Gland Excision","foundation",
"Which nerves are particularly important during transcervical submandibular gland excision?",
["Marginal mandibular branch of the facial nerve, lingual nerve, and hypoglossal nerve","Optic nerve only","Recurrent laryngeal nerve only","Spinal accessory nerve only"],0,
"The marginal mandibular nerve is at risk superficially near the facial vessels, while the lingual nerve and submandibular ganglion relate to the duct superiorly and the hypoglossal nerve lies deep/inferior to the gland. Safe surgery depends on deliberate identification of these relationships.",
["Correct. These are the major nerve structures that frame the operation.","The optic nerve is not in the submandibular triangle.","The RLN is a thyroid/tracheoesophageal structure rather than the principal nerve at risk here.","CN XI is primarily a lateral-neck/posterior-triangle concern."],
"Submandibular gland excision is a three-nerve operation: marginal mandibular, lingual, and hypoglossal.","How does the facial artery relate to the gland and marginal mandibular nerve?","OR_prep"),
_q("v235_tps_smgex_app","Submandibular Gland Excision","application",
"During submandibular gland excision, the deep lobe is being separated from the floor of mouth and the duct is identified. Which structure must be protected as it loops around the duct?",
["Lingual nerve","Phrenic nerve","Vagus nerve","Optic chiasm"],0,
"The lingual nerve has a close three-dimensional relationship with Wharton duct and the submandibular ganglion. Identifying and protecting it before ligating the duct or dividing ganglionic attachments prevents tongue sensory and taste morbidity.",
["Correct. The lingual nerve is the critical deep-lobe/ductal neighbor.","The phrenic nerve lies in the lower lateral neck on the anterior scalene.","The vagus lies in the carotid sheath and is not the ductal crossing structure.","The optic chiasm is intracranial."],
"Before dividing Wharton duct, know where the lingual nerve is.","What deficit would indicate postoperative hypoglossal rather than lingual nerve injury?","OR_prep"),
_q("v235_tps_smgex_snr","Submandibular Gland Excision","senior_decision",
"A firm submandibular mass is suspicious for malignancy rather than chronic sialadenitis. What changes the operative plan most?",
["Treat it exactly like a routine stone gland","Plan oncologic resection based on imaging, tissue diagnosis when appropriate, nerve involvement, and regional nodal risk rather than assuming a benign extracapsular shell-out","Avoid evaluating the neck","Morcellate the mass to reduce incision length"],1,
"A suspected submandibular malignancy requires an oncologic framework. Tumor relationship to lingual and hypoglossal nerves, floor of mouth, mandible, skin, and cervical nodes can change the extent of resection and whether neck treatment is indicated.",
["A malignant process may require wider margins and regional management.","Correct. The pathology changes both the goals and boundaries of surgery.","Nodal staging can be important for salivary malignancy.","Morcellation compromises margin assessment and risks tumor spillage."],
"The same anatomic gland can require a completely different operation when the indication changes from stone to cancer.","How would gross hypoglossal or lingual nerve invasion affect counseling and resection?","OR_prep"),

_q("v235_tps_graves_fnd","Graves Disease / Toxic Goiter","foundation",
"A patient with Graves disease has a large diffuse goiter, compressive symptoms, and difficult medication control. Which statement about surgery is most accurate?",
["Total or near-total thyroidectomy can provide rapid definitive control when surgery is favored by goiter size, symptoms, treatment preference, or other clinical factors","Surgery is contraindicated in all Graves disease","Only partial thyroid biopsy is needed","Radioactive iodine is mandatory for every patient"],0,
"Graves disease can be treated with antithyroid medication, radioactive iodine, or surgery. Thyroidectomy is particularly useful when rapid definitive control is desired, a large/compressive goiter is present, suspicious nodules coexist, or other factors make nonsurgical therapy less attractive.",
["Correct. Treatment is individualized and surgery is a standard definitive option.","Graves disease is a common indication for thyroidectomy in selected patients.","A biopsy does not treat diffuse autonomous thyroid stimulation.","Radioactive iodine is one option, not a universal requirement."],
"Graves treatment is preference- and phenotype-driven; surgery is often the fastest definitive option.","How can active thyroid eye disease influence the choice between radioactive iodine and other definitive treatments?"),
_q("v235_tps_graves_app","Graves Disease / Toxic Goiter","application",
"A patient with Graves disease is scheduled for thyroidectomy but remains markedly thyrotoxic with tachycardia. What is the best preoperative principle?",
["Proceed electively without preparation","Optimize thyroid hormone control and adrenergic symptoms before elective surgery when feasible, with coordinated antithyroid therapy and procedure-specific preparation to reduce thyroid-storm and bleeding risk","Stop all medications abruptly","Give only antibiotics"],1,
"Elective Graves thyroidectomy is safest after coordinated endocrine preparation. Antithyroid medication and beta blockade are commonly used to control hormone production and adrenergic symptoms; iodine may be used in selected preoperative regimens to reduce hormone release and gland vascularity.",
["Uncontrolled thyrotoxicosis increases perioperative cardiovascular and thyroid-storm risk.","Correct. Preparation aims to make a hypermetabolic, hypervascular operation safer.","Abrupt medication cessation can worsen thyrotoxicosis.","Antibiotics do not control Graves physiology."],
"A Graves thyroidectomy begins days to weeks before the incision with physiologic preparation.","What would make urgent surgery necessary despite incomplete biochemical optimization?","OR_prep"),
_q("v235_tps_graves_snr","Graves Disease / Toxic Goiter","senior_decision",
"A patient with Graves disease has severe active orbitopathy, a very large goiter, and wants definitive therapy. What is the best senior-level counseling principle?",
["All definitive therapies are equivalent for every phenotype","Integrate goiter anatomy, orbitopathy activity, smoking, medication history, pregnancy plans, comorbidity, and patient preference; thyroidectomy may be attractive when rapid control is needed or radioiodine could worsen active eye disease","Ignore the eye disease because it is unrelated to thyroid treatment","Choose treatment based only on TSH"],1,
"Definitive Graves therapy is individualized. Active orbitopathy can materially influence treatment choice because radioiodine may worsen eye disease in susceptible patients, whereas surgery offers rapid control without radiation exposure but carries operative risks.",
["Treatment tradeoffs differ substantially by phenotype.","Correct. Senior counseling connects thyroid control with the patient's extra-thyroidal disease and goals.","Thyroid treatment can affect Graves orbitopathy risk and trajectory.","TSH alone does not capture anatomic, ophthalmologic, reproductive, or treatment-preference factors."],
"Treat the patient with Graves disease—not just the thyroid lab values.","Which preoperative laryngeal and calcium-related issues deserve special planning in a large vascular goiter?","OR_prep"),

_q("v235_tps_indet_fnd","Indeterminate Thyroid Cytology / Molecular Testing","foundation",
"A thyroid FNA returns Bethesda III or IV cytology. What does 'indeterminate' mean clinically?",
["Cytology alone cannot reliably classify the nodule as benign or malignant, so malignancy risk must be refined using clinical, ultrasound, repeat-cytology, molecular, or diagnostic-surgical information","The nodule is definitely cancer","The nodule is definitely benign","The specimen always represents medullary thyroid cancer"],0,
"Bethesda III and IV categories occupy an intermediate malignancy-risk range. Management therefore depends on the specific cytology, ultrasound pattern, nodule characteristics, institutional prevalence, patient goals, and whether repeat FNA, molecular testing, surveillance, or diagnostic lobectomy will meaningfully reduce uncertainty.",
["Correct. Indeterminate cytology is a risk category rather than a final histologic diagnosis.","Many indeterminate nodules prove benign.","A meaningful minority are malignant, so indeterminate does not equal benign.","Medullary carcinoma is a distinct diagnosis and is not synonymous with Bethesda III/IV."],
"Bethesda III/IV is a decision problem, not a diagnosis of cancer.","Why does local malignancy prevalence change the positive and negative predictive value of a molecular test?"),
_q("v235_tps_indet_snr","Indeterminate Thyroid Cytology / Molecular Testing","senior_decision",
"A Bethesda IV nodule has a molecular result reported as high risk, but the patient has major comorbidity and a low-suspicion ultrasound phenotype. What is the best senior-level interpretation?",
["Molecular testing automatically mandates total thyroidectomy","Use the molecular result to update—not replace—the pretest risk estimate, then choose surveillance or extent of surgery using assay performance, ultrasound, nodule features, comorbidity, and patient preference","Ignore molecular results entirely","Assume every positive molecular result predicts aggressive cancer"],1,
"Molecular tests are decision aids whose PPV and NPV depend on assay characteristics and disease prevalence. A high-risk result may strengthen the case for surgery or influence extent, but it does not eliminate the need to consider sonographic risk, clinical context, anticipated histology, operative risk, and patient goals.",
["A molecular result does not create a universal total-thyroidectomy indication.","Correct. Bayesian interpretation and shared decision-making remain essential.","Molecular data can be clinically useful when interpreted appropriately.","Some detected alterations predict malignancy risk more strongly than aggressiveness, and phenotype still matters."],
"A molecular test changes probability; it does not replace judgment.","How would a convincingly benign molecular result change management when ultrasound remains highly suspicious?")]


def apply_learning_ladders_v235(challenges,item_id_fn):
    by_id={str(q.get("id")):q for q in challenges if q.get("id")}
    reused=0
    for qid,(topic,stage) in REUSED.items():
        q=by_id.get(qid)
        if not q: continue
        reasons=REUSED_REASON_BY_CHOICE.get(qid,{})
        choices=list(q.get("choices") or [])
        mapped=[reasons.get(str(c)) for c in choices]
        if any(x is None for x in mapped):
            continue
        q["topic"]=topic; q["learning_stage"]=stage; q["why_wrong"]=mapped
        q["concept_id"]=item_id_fn(DOMAIN,topic); q["ladder_reviewed"]=True
        q["tier"]="Curated learning ladder"; reused+=1
    existing=set(by_id)
    added=0
    for q in VIGNETTES_V235:
        if q["id"] in existing: continue
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v235 orphan: "+row["topic"])
        challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reused":reused,"reviewed_topics":5}
