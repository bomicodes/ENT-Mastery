"""v23.4 — Thyroid / Parathyroid / Salivary learning-ladder pass 2.

Reviews canonical topics 6-10 from the live inventory: Anaplastic Thyroid
Cancer, Central Neck Dissection, Reoperative Thyroid Surgery, Secondary /
Tertiary Hyperparathyroidism, and Four-Gland Parathyroid Exploration.
"""
DOMAIN="Thyroid / Parathyroid / Salivary"

def _q(qid,topic,stage,stem,choices,answer,explanation,why_wrong,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":why_wrong,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True}

VIGNETTES_V234=[
_q("v234_tps_atc_fnd","Anaplastic Thyroid Cancer","foundation",
"An older adult develops a rapidly enlarging hard thyroid mass over weeks with dysphagia, hoarseness, and cervical adenopathy. What diagnosis should be assumed until proven otherwise?",
["Anaplastic thyroid carcinoma","Benign colloid nodule","Simple Hashimoto thyroiditis","Parathyroid adenoma"],0,
"Anaplastic thyroid carcinoma classically presents with explosive growth, compressive symptoms, vocal-fold dysfunction, and locally invasive disease in an older patient. Diagnosis and staging must move rapidly because airway compromise and systemic progression can occur over days to weeks.",
["Correct. The tempo and invasive symptoms are classic for ATC.","A benign colloid nodule does not usually enlarge explosively with invasive symptoms.","Hashimoto thyroiditis can enlarge the gland but does not typically produce this rapidly destructive phenotype.","A parathyroid adenoma usually presents biochemically rather than as a rapidly invasive neck mass."],
"A rapidly enlarging thyroid mass with airway or voice symptoms is an oncologic emergency until tissue proves otherwise.","Which other diagnosis—especially thyroid lymphoma—must remain in the rapid-growth differential?","overnight_call"),
_q("v234_tps_atc_app","Anaplastic Thyroid Cancer","application",
"Biopsy confirms anaplastic thyroid carcinoma. The patient is stable but the tumor is rapidly progressive. What should happen early in the workup?",
["Wait several weeks before molecular testing","Urgently stage disease and obtain rapid molecular testing, including BRAF V600E, while multidisciplinary treatment and airway planning proceed in parallel","Perform radioactive iodine ablation first","Schedule routine surveillance ultrasound"],1,
"Modern ATC care is time-critical and multidisciplinary. Rapid molecular characterization can identify actionable alterations such as BRAF V600E, while imaging defines locoregional and distant disease and the team simultaneously addresses airway risk, resectability, radiation/systemic therapy, and goals of care.",
["Delaying actionable genomic information can lose critical treatment time.","Correct. Staging, molecular testing, airway assessment, and treatment planning should proceed in parallel.","ATC does not respond to radioactive iodine as differentiated thyroid cancer may.","Routine surveillance is inappropriate for an aggressively progressive malignancy."],
"In ATC, molecular testing is part of the emergency workup—not a later academic add-on.","How can BRAF-directed therapy change management of an initially unresectable BRAF V600E-positive tumor?"),
_q("v234_tps_atc_snr","Anaplastic Thyroid Cancer","senior_decision",
"A patient with ATC has bulky airway-adjacent disease but no current stridor. The family asks for a prophylactic tracheostomy 'before things get worse.' What is the best senior-level principle?",
["Perform prophylactic tracheostomy in every ATC patient","Individualize airway intervention; avoid reflexive prophylactic tracheostomy when the airway is not imminently threatened because tumor anatomy can make the procedure morbid, while maintaining a clear emergency airway strategy","Never intervene on the airway in ATC","Wait for cardiopulmonary arrest before planning"],1,
"ATC airway decisions are difficult because tracheostomy can be technically hazardous through bulky invasive tumor and may not improve outcomes when performed preemptively without imminent obstruction. Current ATA guidance emphasizes individualized airway planning, rapid tumor-directed therapy when feasible, and frank goals-of-care discussion rather than routine prophylactic tracheostomy.",
["Routine prophylactic tracheostomy can add morbidity without clear benefit in every patient.","Correct. Airway strategy should reflect actual obstruction risk, anatomy, treatment response, and patient goals.","Some patients develop true airway emergencies requiring intervention.","A rescue plan must exist before decompensation occurs."],
"The safest ATC airway is the one planned before crisis—but planning does not automatically mean tracheostomy.","Which symptoms or endoscopic/imaging findings would convert observation into urgent airway intervention?","overnight_call"),

_q("v234_tps_cnd_fnd","Central Neck Dissection","foundation",
"Which nodal compartment is targeted by a central neck dissection for thyroid cancer?",
["Level VI, with level VII included when indicated","Levels I-II only","Posterior triangle only","Parotid basin only"],0,
"The central compartment primarily includes level VI nodes around the larynx, trachea, and recurrent laryngeal nerves; upper mediastinal level VII disease may also be addressed depending on extent and definition. The operation carries specific RLN and parathyroid risks.",
["Correct. Central neck dissection is a prelaryngeal, pretracheal, and paratracheal compartment operation.","Levels I-II are lateral/superior neck compartments, not the central thyroid nodal basin.","The posterior triangle is lateral neck disease.","Parotid nodes are not the thyroid central compartment."],
"Central neck dissection is a compartment operation wrapped around the recurrent laryngeal nerves and parathyroids.","Why does the right recurrent laryngeal nerve create a different paratracheal geometry than the left?","OR_prep"),
_q("v234_tps_cnd_app","Central Neck Dissection","application",
"A patient with papillary thyroid carcinoma has biopsy-proven central compartment nodal metastasis. What is the best operative principle?",
["Perform therapeutic compartment-oriented central neck dissection with the thyroid operation rather than plucking only the visible node","Observe the positive node because it is central","Remove only the largest node","Perform radical neck dissection including sternocleidomastoid, IJV, and CN XI"],0,
"Clinically involved central nodal disease is treated with therapeutic compartment-oriented dissection when surgery is appropriate. Node-picking leaves adjacent disease behind and makes future reoperation more difficult, while classic radical neck dissection is unnecessary for isolated central thyroid nodal disease.",
["Correct. Known nodal metastasis should be treated by the involved compartment rather than isolated node removal.","Established structural disease is not a prophylactic-dissection question.","Node-picking compromises regional disease control and future anatomy.","Sacrifice of major lateral-neck structures is not indicated for isolated central disease."],
"Therapeutic central neck surgery is compartment surgery, not lymph-node whack-a-mole.","How do preoperative vocal-fold status and parathyroid-autotransplant planning affect the operation?","OR_prep"),
_q("v234_tps_cnd_snr","Central Neck Dissection","senior_decision",
"A patient with a small cN0 papillary thyroid carcinoma asks whether prophylactic central neck dissection should be routine. What is the best counseling principle?",
["Yes, because microscopic nodes must always be removed","No universal rule: balance primary-tumor risk and staging value against higher hypoparathyroidism and recurrent-laryngeal-nerve morbidity; routine prophylactic dissection is not required for every cN0 low-risk tumor","No central neck dissection is ever appropriate","Perform bilateral lateral neck dissection instead"],1,
"The value of prophylactic central neck dissection depends on tumor risk, extent, whether nodal information will alter treatment, and surgical morbidity. For many small clinically node-negative papillary cancers, routine prophylactic central dissection is not necessary.",
["Microscopic nodal disease does not automatically justify added bilateral central-compartment morbidity.","Correct. The operation should provide meaningful oncologic or staging benefit proportional to risk.","Therapeutic central dissection remains appropriate for known nodal disease.","Lateral neck dissection is not a substitute for risk-adapted central management."],
"A prophylactic neck operation should earn its morbidity by changing outcome or management.","Which advanced primary-tumor features make prophylactic central treatment more reasonable?"),

_q("v234_tps_reopthy_fnd","Reoperative Thyroid Surgery","foundation",
"Why is reoperative thyroid or central-neck surgery higher risk than primary thyroidectomy?",
["Scar and distorted planes make the recurrent laryngeal nerve and parathyroid blood supply harder to identify and preserve","The recurrent laryngeal nerve disappears after the first operation","Bleeding is impossible in a scarred field","Anatomy is always simpler after surgery"],0,
"Reoperation creates fibrosis, altered landmarks, tethered nerve, devascularized parathyroids, and scar around the tracheoesophageal groove. Prior operative reports and current vocal-fold function become especially important for planning.",
["Correct. Distorted planes increase nerve, parathyroid, vascular, and aerodigestive risk.","The nerve remains present but may be displaced or scarred.","Reoperative fields can bleed significantly from scarred vessels or recurrent disease.","Anatomy is less predictable, not simpler."],
"In the reoperative central neck, the map from the first surgery matters almost as much as the current scan.","Which details from the original operative and pathology reports are most useful before re-entry?","OR_prep"),
_q("v234_tps_reopthy_app","Reoperative Thyroid Surgery","application",
"A patient with recurrent thyroid cancer needs reoperative central neck surgery. What preoperative assessment is particularly important before risking the contralateral recurrent laryngeal nerve?",
["Document bilateral vocal-fold mobility","Check only the patient's hearing","Skip laryngoscopy if the voice sounds normal","Perform nasal endoscopy only"],0,
"Baseline laryngeal examination is essential in reoperative thyroid surgery because occult unilateral vocal-fold paralysis changes the risk of contralateral nerve injury and may fundamentally alter the surgical plan. Voice alone is not sufficiently sensitive to exclude prior nerve dysfunction.",
["Correct. Known preoperative nerve function is crucial before operating in a scarred bilateral-risk field.","Hearing status does not define RLN risk.","Patients can compensate for unilateral paralysis and sound deceptively normal.","Nasal endoscopy does not establish vocal-fold mobility."],
"Before reoperative thyroid surgery, never assume a normal-sounding voice means two functioning recurrent laryngeal nerves.","How would pre-existing contralateral vocal-fold paralysis change the threshold for surgery or nerve sacrifice?","OR_prep"),
_q("v234_tps_reopthy_snr","Reoperative Thyroid Surgery","senior_decision",
"Recurrent thyroid cancer is tightly adherent to a functioning recurrent laryngeal nerve in a scarred central neck. What should determine whether the nerve is shaved, dissected free, or sacrificed?",
["Sacrifice every nerve touching tumor","Integrate gross invasion versus adherence, likelihood of complete disease control, preoperative function, contralateral nerve status, tumor biology, and reconstructive options rather than using one automatic maneuver","Preserve the nerve even through gross intraneural tumor at any oncologic cost","Stop the operation without assessing resectability"],1,
"Reoperative nerve management is an oncologic and functional tradeoff. A functioning nerve that can be separated without leaving gross disease may be preserved, whereas true gross nerve invasion can require sacrifice when that improves meaningful disease control and the contralateral nerve is safe. Reconstruction or reinnervation should be considered when sacrifice is necessary.",
["Automatic sacrifice can create avoidable morbidity.","Correct. The decision depends on true invasion, cancer control, and the patient's remaining laryngeal reserve.","Leaving gross invasive tumor solely to preserve motion may compromise oncologic goals in selected curative cases.","The purpose of exploration is to define and act on resectability safely."],
"In reoperative thyroid cancer, 'tumor touching nerve' and 'tumor invading nerve' are not synonymous.","When might intentional gross residual disease be reasonable because nerve sacrifice would create disproportionate harm?","OR_prep"),

_q("v234_tps_secpar_fnd","Secondary / Tertiary Hyperparathyroidism","foundation",
"Which distinction best separates secondary from tertiary hyperparathyroidism in advanced kidney disease?",
["Secondary disease is a compensatory PTH response to chronic mineral imbalance, whereas tertiary disease is autonomous hypersecretion that persists despite correction or becomes associated with hypercalcemia","They are identical terms","Secondary disease always causes severe hypercalcemia from the start","Tertiary disease is caused by a single thyroid nodule"],0,
"Chronic kidney disease drives secondary hyperparathyroidism through phosphate retention, altered vitamin D metabolism, hypocalcemic stimulus, and gland hyperplasia. With prolonged stimulation, glands can become relatively autonomous, producing tertiary hyperparathyroidism—often with hypercalcemia, including after renal transplantation.",
["Correct. The key distinction is compensatory versus autonomous PTH secretion.","The etiologies and management thresholds differ.","Secondary renal hyperparathyroidism is not defined by primary autonomous hypercalcemia.","Tertiary disease is parathyroid hyperplasia/autonomy, not a thyroid nodule."],
"Secondary hyperparathyroidism is a response; tertiary hyperparathyroidism has learned to keep secreting after the original signal should have stopped.","How does successful renal transplantation change the expected calcium-PTH physiology?"),
_q("v234_tps_secpar_app","Secondary / Tertiary Hyperparathyroidism","application",
"A dialysis patient has severe medically refractory secondary hyperparathyroidism with bone pain, very high PTH, and progressive mineral-bone complications despite optimized nephrology therapy. What is the appropriate surgical principle?",
["Parathyroidectomy can be considered for severe refractory disease after multidisciplinary optimization","Surgery is never used in renal hyperparathyroidism","Remove only the thyroid gland","Treat only with antibiotics"],0,
"Most secondary hyperparathyroidism is treated medically, but severe refractory disease with major skeletal, biochemical, calcific, or symptomatic complications can warrant parathyroidectomy. The operation must account for multigland hyperplasia and postoperative hypocalcemia/hungry-bone risk.",
["Correct. Surgery is reserved for medically refractory clinically significant disease.","Parathyroidectomy remains an important option in selected severe cases.","Thyroidectomy does not treat multigland parathyroid hyperplasia.","Antibiotics do not correct renal mineral-bone physiology."],
"Renal hyperparathyroid surgery is usually a multigland operation for failure of medical control—not a focused adenoma operation.","What preoperative calcium, phosphate, alkaline phosphatase, and vitamin D findings predict difficult postoperative calcium management?"),
_q("v234_tps_secpar_snr","Secondary / Tertiary Hyperparathyroidism","senior_decision",
"A renal-transplant recipient has persistent hypercalcemia and markedly elevated PTH months after successful graft function, with nephrolithiasis and bone disease. What should guide management?",
["Assume the transplant cured all parathyroid disease","Recognize likely tertiary hyperparathyroidism and weigh surgery against medical therapy using calcium burden, symptoms, graft function, skeletal/renal complications, and expected multigland disease","Perform focused excision of whichever gland is largest on ultrasound without considering the others","Ignore the hypercalcemia because PTH elevation is expected after transplant"],1,
"Persistent autonomous PTH secretion after renal transplantation can cause tertiary hyperparathyroidism. Significant hypercalcemia and target-organ complications may justify surgery, but the plan should reflect the multigland biology and the needs of the transplanted kidney.",
["Autonomous hyperplasia can persist despite restored renal function.","Correct. Treatment should protect both the patient and the renal graft from sustained calcium/PTH excess.","Imaging size does not convert a multigland disease process into a single-adenoma diagnosis.","Persistent hypercalcemia with complications is clinically meaningful."],
"After transplant, persistent hypercalcemia is the clue that the parathyroids may no longer be listening to the kidney.","How do subtotal parathyroidectomy and total parathyroidectomy with autotransplantation differ in recurrence and hypoparathyroidism tradeoffs?","OR_prep"),

_q("v234_tps_4g_fnd","Four-Gland Parathyroid Exploration","foundation",
"What is the central goal of a bilateral four-gland parathyroid exploration?",
["Identify the expected parathyroid glands systematically and treat the abnormal gland or multigland pattern while preserving adequate viable parathyroid function","Remove the thyroid without looking for parathyroids","Excise every visible lymph node","Operate only on the first enlarged gland encountered"],0,
"A four-gland exploration is a systematic bilateral operation that uses embryologic anatomy and common ectopic locations to assess the full parathyroid set. It is particularly useful when localization is poor, multigland disease is likely, or focused exploration would be unreliable.",
["Correct. The operation seeks a complete anatomic and disease assessment while avoiding permanent hypoparathyroidism.","Thyroidectomy is not the objective.","Lymph-node clearance does not treat hyperparathyroidism.","Stopping at the first large gland can miss double adenoma or hyperplasia when multigland disease is present."],
"Four-gland exploration is a systematic anatomy operation, not a search for whichever brown structure appears first.","Where are the most important ectopic locations for superior versus inferior glands?","OR_prep"),
_q("v234_tps_4g_app","Four-Gland Parathyroid Exploration","application",
"During bilateral exploration for primary hyperparathyroidism, three glands appear normal and one enlarged inferior gland is removed. Intraoperative PTH fails to fall appropriately. What is the best next principle?",
["End the operation because one enlarged gland was removed","Reassess for additional hyperfunctioning or ectopic tissue and the possibility of multigland disease before declaring cure","Remove the thyroid immediately","Ignore the PTH result regardless of timing or assay validity"],1,
"Failure of an appropriately timed intraoperative PTH decline should prompt reassessment of operative findings, assay timing, and the possibility of another hyperfunctioning gland or ectopic parathyroid tissue. The biochemical signal can prevent premature closure when the disease model is incomplete.",
["Persistent PTH suggests the operation may not yet have removed all hyperfunctioning tissue.","Correct. Reconcile the biochemical response with the anatomy before ending exploration.","Thyroid removal does not correct an unidentified hyperfunctioning parathyroid gland.","The result should be interpreted thoughtfully, not reflexively ignored."],
"When the intraoperative PTH does not behave like a single adenoma, reconsider the single-adenoma story.","Which ectopic sites should be revisited before escalating to more extensive mediastinal exploration?","OR_prep"),
_q("v234_tps_4g_snr","Four-Gland Parathyroid Exploration","senior_decision",
"A MEN1 patient has primary hyperparathyroidism with multigland enlargement. Why is a focused single-gland excision usually the wrong operation?",
["MEN1-associated hyperparathyroidism is commonly multigland disease, so the operative strategy must address the broader parathyroid burden while balancing recurrence against permanent hypoparathyroidism","MEN1 affects only the thyroid","One enlarged gland proves all others are normal","Parathyroid surgery is contraindicated in hereditary disease"],0,
"Hereditary hyperparathyroidism such as MEN1 is usually multigland and asynchronous. Operative strategies therefore address multiple glands and may include subtotal parathyroidectomy or other syndrome-specific approaches, with long-term recurrence and reoperative risk explicitly considered.",
["Correct. The disease biology is multigland, so a single-gland operation often under-treats it.","MEN1 affects multiple endocrine organs, including parathyroids.","Gross size at one operation does not reliably exclude disease in the remaining glands.","Surgery is often appropriate when indicated, but the strategy differs from sporadic single-adenoma disease."],
"The operation should match the disease model: hereditary hyperparathyroidism is a lifetime multigland problem.","How does preservation or cryopreservation planning change when the patient is young and recurrence is likely?","OR_prep"),
]

def apply_learning_ladders_v234(challenges,item_id_fn):
    existing={str(q.get("id")) for q in challenges if q.get("id")}; added=0
    for q in VIGNETTES_V234:
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v234 orphan: "+row["topic"])
        if row["id"] not in existing:
            challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":5}
