"""v23.6 — Thyroid / Parathyroid / Salivary learning-ladder pass 4.

Reviews canonical topics 16-20 from the live inventory: MEN2 / RET,
Parathyroid Carcinoma, Reoperative Hyperparathyroidism, Hungry Bone / Post-
Thyroid Calcium Management, and Pleomorphic Adenoma / Warthin Tumor.
"""
DOMAIN="Thyroid / Parathyroid / Salivary"

def _q(qid,topic,stage,stem,choices,answer,explanation,why_wrong,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,"stem":stem,
            "choices":choices,"answer":answer,"explanation":explanation,"why_wrong":why_wrong,
            "board_pearl":pearl,"curveball":curveball,"tier":"Curated learning ladder",
            "mode":"Vignette","focus":focus,"ladder_reviewed":True}

VIGNETTES_V236=[
_q("v236_tps_men2_fnd","MEN2 / RET","foundation",
"A patient with medullary thyroid carcinoma is found to have a germline RET pathogenic variant. What additional disease framework must be considered?",
["MEN2 with risk for pheochromocytoma and, depending on genotype, primary hyperparathyroidism","Familial adenomatous polyposis only","Von Hippel-Lindau without endocrine tumors","Isolated Graves disease"],0,
"Germline RET variants cause MEN2 syndromes. Patients and at-risk relatives require genotype-informed evaluation for associated endocrine tumors, especially pheochromocytoma and in MEN2A primary hyperparathyroidism, as well as counseling about timing of thyroid intervention.",
["Correct. RET links medullary thyroid carcinoma to a broader hereditary endocrine syndrome.","FAP is associated with APC mutations rather than MEN2.","VHL can cause pheochromocytoma but is not the RET/MTC syndrome.","Graves disease does not explain hereditary MTC."],
"A RET-positive MTC diagnosis changes care for the patient and the family.","Why must pheochromocytoma be excluded before elective thyroid surgery in MEN2?"),
_q("v236_tps_men2_app","MEN2 / RET","application",
"A patient with MEN2A needs thyroidectomy for medullary thyroid carcinoma and also reports episodic headaches, palpitations, and diaphoresis. What is the most important next principle?",
["Proceed directly to thyroidectomy","Evaluate biochemically for pheochromocytoma and treat a catecholamine-secreting tumor before elective thyroid surgery if present","Ignore the symptoms because MTC explains them","Give radioactive iodine first"],1,
"Undiagnosed pheochromocytoma can precipitate life-threatening hypertensive crisis during anesthesia or surgery. In MEN2, pheochromocytoma screening precedes elective thyroid surgery when the syndrome or symptoms raise concern, and an identified pheochromocytoma is generally addressed first.",
["Unrecognized catecholamine excess creates major anesthetic risk.","Correct. The order of operations is driven by physiologic danger, not just which tumor was diagnosed first.","MTC does not make classic catecholamine symptoms irrelevant.","Medullary thyroid carcinoma is not treated with radioactive iodine."],
"In MEN2, rule out the adrenal danger before operating on the neck.","How does a RET genotype influence screening age and prophylactic thyroidectomy timing in an unaffected carrier?","OR_prep"),
_q("v236_tps_men2_snr","MEN2 / RET","senior_decision",
"An asymptomatic child is found through cascade testing to carry a pathogenic RET variant associated with high medullary-thyroid-cancer risk. What should determine timing of prophylactic thyroidectomy?",
["Wait for a palpable thyroid mass in every child","Use the specific RET risk category together with age, calcitonin when appropriate, family phenotype, and expert hereditary-endocrine guidance rather than one universal age for every variant","Perform radioactive iodine instead of surgery","Ignore the result until adulthood"],1,
"RET variants carry different penetrance and age-specific risks. Prophylactic thyroidectomy timing is genotype-informed and should be coordinated through experienced endocrine, surgical, and genetic teams rather than delayed until clinically apparent MTC.",
["Waiting for a palpable tumor can forfeit the preventive purpose of testing.","Correct. RET management is variant-specific rather than one-size-fits-all.","RAI does not eradicate C-cell disease.","Some high-risk variants require intervention well before adulthood."],
"RET testing is actionable because it can prevent MTC rather than merely predict it.","How would elevated calcitonin or suspicious cervical nodes change the operation from prophylactic to therapeutic?"),

_q("v236_tps_ptca_fnd","Parathyroid Carcinoma","foundation",
"Which presentation should raise concern for parathyroid carcinoma rather than a typical benign adenoma?",
["Marked hypercalcemia with very high PTH, a firm invasive neck mass, or recurrent laryngeal nerve dysfunction","Mild isolated vitamin D deficiency","Normal calcium with seasonal allergies","A painless ear canal cyst"],0,
"Parathyroid carcinoma is rare, but profound biochemical hyperparathyroidism plus a palpable or invasive cervical lesion should raise suspicion. Local invasion and recurrent laryngeal nerve dysfunction are particularly concerning because most benign adenomas do not invade adjacent structures.",
["Correct. Severe biochemistry plus invasive local behavior is the classic warning pattern.","Vitamin D deficiency causes secondary PTH elevation rather than an invasive parathyroid mass.","Seasonal allergy is unrelated.","An ear canal lesion does not localize to parathyroid tissue."],
"Parathyroid cancer announces itself more by severity and invasion than by a pathognomonic FNA result.","Why should suspected parathyroid carcinoma generally not undergo routine needle biopsy?"),
_q("v236_tps_ptca_app","Parathyroid Carcinoma","application",
"During exploration for severe primary hyperparathyroidism, a parathyroid mass is densely adherent to the ipsilateral thyroid and strap tissue with an invasive appearance. What operative principle is best?",
["Shell it out piecemeal to preserve the capsule","Avoid capsular rupture and pursue an en bloc oncologic resection of involved adjacent tissue when carcinoma is suspected","Perform curettage only","Stop and give radioactive iodine"],1,
"The best chance for durable control of localized parathyroid carcinoma is complete initial resection without tumor rupture. When gross invasion is present, en bloc removal of involved adjacent tissue—often including ipsilateral thyroid—is favored over piecemeal excision.",
["Capsular disruption can seed tumor and compromise local control.","Correct. The first operation is the best opportunity for complete oncologic resection.","Curettage is inadequate for an invasive endocrine malignancy.","Parathyroid carcinoma is not treated with radioactive iodine."],
"Do not turn a suspected parathyroid carcinoma into parathyromatosis by violating the capsule.","How should gross recurrent laryngeal nerve invasion be balanced against preoperative vocal-fold function and oncologic control?","OR_prep"),
_q("v236_tps_ptca_snr","Parathyroid Carcinoma","senior_decision",
"A patient develops recurrent hypercalcemia years after resection of parathyroid carcinoma, with a resectable neck recurrence and no widespread metastases. What should guide management?",
["Treat calcium alone and ignore structural disease","Control dangerous hypercalcemia while evaluating complete resection of locoregional recurrence when feasible, recognizing repeated surgery may provide both biochemical and disease control","Use RAI ablation","Assume recurrence is benign"],1,
"Recurrent parathyroid carcinoma often causes morbidity through PTH-mediated hypercalcemia. Management therefore has two parallel goals: control the calcium physiology and obtain structural disease control with surgery when recurrence remains resectable.",
["Severe hypercalcemia requires treatment, but structural recurrence also matters.","Correct. Biochemical and oncologic control are linked in this disease.","Parathyroid carcinoma does not concentrate radioiodine.","Prior carcinoma makes recurrent structural disease oncologically significant."],
"In parathyroid carcinoma, calcium can be the most immediate threat even when the cancer is the underlying problem.","Which medical therapies can bridge severe hypercalcemia while definitive disease control is planned?"),

_q("v236_tps_reophpt_fnd","Reoperative Hyperparathyroidism","foundation",
"A patient remains hypercalcemic with an inappropriately high PTH after prior parathyroid surgery. What is the first principle before reoperation?",
["Reconfirm the biochemical diagnosis and review the original operative/pathology record before assuming a missed gland","Reoperate immediately without localization","Assume every elevated PTH is recurrent primary disease","Perform thyroidectomy instead"],0,
"Persistent or recurrent hyperparathyroidism requires diagnostic reset: verify calcium/PTH physiology, exclude mimics such as familial hypocalciuric hypercalcemia when relevant, and reconstruct what was found, removed, biopsied, or left at the first operation.",
["Correct. Reoperation begins with proving the disease and understanding the first operation.","Blind re-exploration in scar increases nerve and parathyroid morbidity.","PTH elevation can be secondary or otherwise nonoperative depending on calcium and clinical context.","Thyroidectomy does not correct an unidentified parathyroid source."],
"Before a reoperative parathyroidectomy, rebuild the map—biochemical, operative, pathologic, and anatomic.","What defines persistent versus recurrent primary hyperparathyroidism after surgery?"),
_q("v236_tps_reophpt_app","Reoperative Hyperparathyroidism","application",
"Biochemistry confirms persistent primary hyperparathyroidism after a prior bilateral exploration. What is the best localization principle before re-entry?",
["Proceed without imaging because anatomy is unchanged","Use complementary high-quality localization tailored to the reoperative neck and require a coherent target before focused re-entry whenever possible","Use plain neck radiographs only","Biopsy every candidate lesion with a large-bore needle"],1,
"Scarred anatomy magnifies the cost of a negative exploration. Ultrasound, sestamibi/SPECT, multiphase CT, MRI, or selective venous sampling may be used according to prior studies, renal function, local expertise, and disease complexity; concordant localization improves operative planning.",
["Reoperative anatomy is distorted and blind exploration carries higher risk.","Correct. Localization should reduce—not add to—the uncertainty of re-entry.","Plain radiographs do not adequately localize parathyroid tissue.","Routine invasive biopsy risks seeding, fibrosis, and diagnostic confusion."],
"Localization is helpful in primary surgery; in reoperative parathyroid surgery it can be mission-critical.","When is selective venous PTH sampling useful after noninvasive studies disagree?","OR_prep"),
_q("v236_tps_reophpt_snr","Reoperative Hyperparathyroidism","senior_decision",
"A reoperative patient has a suspected ectopic parathyroid target deep in the scarred tracheoesophageal groove adjacent to a functioning recurrent laryngeal nerve. What should determine whether to proceed?",
["The presence of any positive scan alone","Certainty of biochemical disease and localization, symptom/organ burden, expected cure benefit, contralateral vocal-fold function, and the nerve/vascular risk of the proposed approach","Surgeon preference alone","The patient's age alone"],1,
"Reoperative parathyroidectomy should have a higher threshold than uncomplicated primary surgery. The anticipated benefit must justify the increased recurrent-laryngeal-nerve, esophageal, vascular, and permanent-hypoparathyroidism risks of scarred re-entry.",
["Imaging is only one element of the decision.","Correct. A technically possible reoperation is not automatically a wise one.","The decision should be evidence- and patient-centered.","Age alone does not define operative benefit or risk."],
"Reoperation should be targeted enough that you know what success is worth before accepting scarred-neck risk.","How would pre-existing contralateral vocal-fold paralysis alter the plan?","OR_prep"),

_q("v236_tps_hungry_fnd","Hungry Bone / Post-Thyroid Calcium Management","foundation",
"After parathyroidectomy for severe long-standing hyperparathyroidism, a patient develops prolonged hypocalcemia with low phosphate and high bone-turnover history despite an appropriately falling PTH. What is the most likely mechanism?",
["Hungry bone syndrome from rapid skeletal remineralization","Thyroid storm","Acute bacterial sialadenitis","Hyperaldosteronism"],0,
"Hungry bone syndrome occurs when chronically demineralized bone avidly takes up calcium, phosphate, and magnesium after the PTH drive is removed. It is more likely with severe bone disease, high alkaline phosphatase, large PTH burden, and renal hyperparathyroidism.",
["Correct. The skeleton becomes a powerful postoperative mineral sink.","Thyroid storm causes hypermetabolic instability rather than this mineral pattern.","Salivary infection does not explain postoperative hypocalcemia.","Aldosterone excess is unrelated to this postoperative bone flux."],
"Hungry bone is not failed parathyroid surgery—it is the skeleton responding vigorously to successful hormone withdrawal.","How does hungry bone differ biochemically from hypocalcemia caused by permanent hypoparathyroidism?"),
_q("v236_tps_hungry_app","Hungry Bone / Post-Thyroid Calcium Management","application",
"Several hours after total thyroidectomy, a patient develops perioral tingling and carpopedal spasm. What is the immediate management principle?",
["Assess calcium physiology promptly and treat symptomatic hypocalcemia, using IV calcium for severe symptoms while beginning appropriate oral calcium/vitamin-D support and monitoring","Wait for seizures before checking calcium","Give potassium only","Treat with antibiotics"],0,
"Symptomatic postoperative hypocalcemia requires prompt assessment and replacement. Severe neuromuscular symptoms, QT prolongation, or other significant manifestations can require intravenous calcium, followed by oral calcium and active vitamin D according to PTH/calcium trajectory and institutional protocol.",
["Correct. Symptoms make postoperative calcium management time-sensitive.","Delaying treatment risks laryngospasm, seizure, and arrhythmia.","Potassium does not correct hypocalcemic tetany.","Antibiotics do not treat endocrine postoperative hypocalcemia."],
"After thyroid surgery, tingling can be the first warning of a calcium problem—do not wait for tetany to declare itself.","How can an early postoperative PTH help stratify calcium-replacement and discharge planning?","postoperative_call"),
_q("v236_tps_hungry_snr","Hungry Bone / Post-Thyroid Calcium Management","senior_decision",
"A dialysis patient with severe secondary hyperparathyroidism has very high alkaline phosphatase and major skeletal disease before subtotal parathyroidectomy. What is the best attending-level postoperative plan?",
["Assume routine outpatient calcium needs","Anticipate high-risk hungry bone physiology with frequent calcium/magnesium/phosphate monitoring and proactive calcium plus active-vitamin-D replacement coordinated with nephrology","Avoid calcium because the preoperative PTH was high","Discharge before postoperative labs"],1,
"Renal hyperparathyroidism with severe bone turnover can produce profound, prolonged hungry bone syndrome. Planning should begin before surgery and include intensive mineral monitoring, dialysis-aware replacement, and readiness for substantial calcium requirements.",
["This phenotype is specifically high risk for prolonged mineral uptake.","Correct. Prevention and early replacement are safer than reacting to severe tetany.","The fall in PTH is exactly what triggers skeletal mineral uptake.","Early discharge without biochemical stability can be unsafe."],
"In high-turnover renal bone disease, the postoperative calcium plan is part of the operation—not an afterthought.","How do poor renal clearance and delayed PTH kinetics complicate interpretation of intraoperative or postoperative PTH values?","postoperative_call"),

_q("v236_tps_benignsal_fnd","Pleomorphic Adenoma / Warthin Tumor","foundation",
"Which pairing is most characteristic of the two common benign parotid tumors?",
["Pleomorphic adenoma: risk of recurrence with capsular violation and long-term malignant transformation; Warthin tumor: strong smoking association and possible bilaterality/multifocality","Pleomorphic adenoma: always bilateral; Warthin tumor: always malignant","Both are thyroid cancers","Neither occurs in the parotid"],0,
"Pleomorphic adenoma is the common mixed benign salivary tumor and can recur after inadequate excision because of pseudopods/satellite nodules; long-standing lesions have a small risk of carcinoma ex pleomorphic adenoma. Warthin tumor is strongly associated with smoking and may be multifocal or bilateral.",
["Correct. These distinctions drive counseling and management.","Pleomorphic adenoma is not characteristically always bilateral and Warthin tumor is benign.","These are salivary rather than thyroid neoplasms.","Both commonly arise in the parotid gland."],
"Pleomorphic adenoma is benign but not a shell-out tumor; Warthin is the benign parotid tumor that likes smokers and multiplicity.","What clinical change in a long-standing pleomorphic adenoma should raise concern for malignant transformation?"),
_q("v236_tps_benignsal_app","Pleomorphic Adenoma / Warthin Tumor","application",
"A young patient has a slowly growing superficial-lobe parotid pleomorphic adenoma with normal facial function. What is the best surgical principle?",
["Remove the tumor with an appropriate margin/cuff of normal parotid while preserving the facial nerve rather than performing simple enucleation","Open the capsule and scoop out the center","Observe every pleomorphic adenoma indefinitely","Sacrifice the facial nerve routinely"],0,
"Pleomorphic adenoma has microscopic extensions and capsular irregularities that make simple enucleation prone to recurrence. Contemporary surgery is tailored to tumor location and may use extracapsular dissection or partial/superficial parotid techniques in selected cases, but the capsule should not be deliberately violated and the facial nerve should be preserved when uninvolved.",
["Correct. Oncologically sound benign surgery avoids capsule violation while preserving function.","Capsular rupture can seed tumor and increase recurrence risk.","Young patients may accumulate substantial lifetime growth/recurrence risk if an operable lesion is never addressed.","A functioning uninvolved facial nerve should not be sacrificed for a benign tumor."],
"Pleomorphic adenoma is benign enough to preserve the nerve, but biologically unforgiving of careless enucleation.","How does a deep-lobe location change exposure and facial-nerve planning?","OR_prep"),
_q("v236_tps_benignsal_snr","Pleomorphic Adenoma / Warthin Tumor","senior_decision",
"An older smoker has a classic, biopsy-supported Warthin tumor in the parotid tail that has been stable, is asymptomatic, and is concordant on imaging and examination. What is the best senior-level principle?",
["Every Warthin tumor requires total parotidectomy","Observation can be reasonable when the diagnosis is secure and the lesion is asymptomatic, while growth, symptoms, diagnostic uncertainty, or patient preference can favor surgery","Treat with neck radiation","Assume facial paralysis is inevitable"],1,
"Unlike pleomorphic adenoma, a confidently diagnosed Warthin tumor often has a very low malignant potential and may be observed in selected patients. Management should consider certainty of diagnosis, symptoms, growth, comorbidity, multiplicity, smoking history, and preference.",
["Total parotidectomy would over-treat many small low-risk Warthin tumors.","Correct. Benign salivary tumors do not all share the same natural-history threshold for surgery.","Radiation is not routine treatment for a benign Warthin tumor.","Facial paralysis is not an expected natural consequence of a stable Warthin tumor."],
"The diagnosis matters: 'benign parotid tumor' is not one management category.","What discordant imaging, cytology, or growth pattern would make observation unsafe?")]

def apply_learning_ladders_v236(challenges,item_id_fn):
    existing={str(q.get("id")) for q in challenges if q.get("id")}
    added=0
    for q in VIGNETTES_V236:
        if q["id"] in existing: continue
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v236 orphan: "+row["topic"])
        challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":5}
