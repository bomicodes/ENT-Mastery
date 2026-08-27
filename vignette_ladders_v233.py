"""v23.3 — Thyroid / Parathyroid / Salivary learning-ladder pass 1.

Reviews the first five canonical topics from the live inventory: Thyroid Nodule,
Differentiated Thyroid Cancer, Primary Hyperparathyroidism, Salivary Gland
Malignancy, and Medullary Thyroid Cancer. DTC extent-of-surgery logic reflects
the 2025 ATA framework rather than older routine-total-thyroidectomy heuristics.
"""
DOMAIN="Thyroid / Parathyroid / Salivary"


def _q(qid,topic,stage,stem,choices,answer,explanation,why_wrong,pearl,curveball,focus="boards"):
    return {"id":qid,"domain":DOMAIN,"topic":topic,"learning_stage":stage,
            "stem":stem,"choices":choices,"answer":answer,"explanation":explanation,
            "why_wrong":why_wrong,"board_pearl":pearl,"curveball":curveball,
            "tier":"Curated learning ladder","mode":"Vignette","focus":focus,
            "ladder_reviewed":True}


VIGNETTES_V233=[
_q("v233_tps_nodule_fnd","Thyroid Nodule","foundation",
"A patient has a newly discovered 1.8-cm thyroid nodule. What is the best initial evaluation framework?",
["Measure serum TSH and perform risk-stratifying thyroid/neck ultrasound, then decide whether FNA is indicated from sonographic pattern and size","Proceed directly to total thyroidectomy","Order PET-CT for every nodule","Measure calcitonin only and skip ultrasound"],0,
"Thyroid nodule evaluation begins with clinical assessment, serum TSH, and high-quality ultrasound of the thyroid and cervical nodes. FNA is selected according to ultrasound risk pattern and nodule size rather than size alone. A suppressed TSH may shift evaluation toward radionuclide assessment for an autonomously functioning nodule.",
["Correct. TSH plus ultrasound establishes the physiologic and structural risk framework before biopsy decisions.","Most nodules are benign and do not warrant immediate total thyroidectomy.","PET-CT is not routine first-line evaluation of an incidental thyroid nodule.","Calcitonin can be relevant in selected contexts, but it does not replace ultrasound-based risk stratification."],
"For a thyroid nodule, ask two questions first: is it functionally autonomous, and does the ultrasound phenotype warrant biopsy?",
"How does a suppressed TSH change the next diagnostic step?"),

_q("v233_tps_nodule_app","Thyroid Nodule","application",
"Ultrasound shows a highly suspicious 1.2-cm solid hypoechoic thyroid nodule with irregular margins and punctate echogenic foci. TSH is normal. What is the best next step?",
["Observe for ten years without follow-up","Perform ultrasound-guided FNA because the sonographic risk and size meet biopsy criteria","Start radioactive iodine empirically","Perform central neck dissection without tissue diagnosis"],1,
"A nodule with high-suspicion ultrasound features at a size meeting guideline thresholds warrants ultrasound-guided FNA. The purpose is to establish cytologic risk before choosing observation, molecular testing, surgery, or another pathway.",
["High-suspicion morphology at this size should not be dismissed without tissue assessment.","Correct. Sonographic pattern and size together determine the FNA threshold.","Radioactive iodine is not empiric therapy for an uncharacterized euthyroid nodule.","Nodal surgery requires an oncologic indication, not a suspicious thyroid image alone."],
"Biopsy thresholds are risk-pattern thresholds, not simply diameter thresholds.",
"What ultrasound findings in the lateral or central neck should be sampled separately from the thyroid nodule?"),

_q("v233_tps_nodule_snr","Thyroid Nodule","senior_decision",
"A 72-year-old with severe cardiopulmonary disease has a 9-mm highly suspicious thyroid nodule without suspicious nodes, compressive symptoms, or invasive features. What is the best senior-level principle?",
["Every suspicious nodule requires immediate surgery regardless of competing risk","Individualize biopsy and treatment intensity by tumor risk, life expectancy, comorbidity, patient preference, and whether the result would change management","Perform prophylactic bilateral neck dissections","Ignore the nodule permanently"],1,
"Very small suspicious nodules can have indolent biology, and management should reflect whether diagnosis or intervention will meaningfully benefit the patient. Frailty, life expectancy, invasive features, nodal disease, tumor growth, and patient goals all influence whether active surveillance, biopsy, or surgery is appropriate.",
["Competing mortality and treatment morbidity matter in low-volume thyroid disease.","Correct. A test or operation is useful only when its result is likely to improve the patient's outcome.","There is no indication for prophylactic bilateral neck dissection in this setting.","Surveillance is different from abandonment; follow-up should be intentional when observation is chosen."],
"Do not turn a tiny thyroid imaging abnormality into a major operation without proving the patient benefits from that escalation.",
"Which interval growth or new nodal finding would make surveillance less attractive?"),

_q("v233_tps_dtc_fnd","Differentiated Thyroid Cancer","foundation",
"A 38-year-old has a 1.4-cm papillary thyroid carcinoma confined to one lobe, no gross extrathyroidal extension, and no suspicious cervical nodes. Which operation is appropriate under the contemporary risk-adapted framework?",
["Thyroid lobectomy","Mandatory total thyroidectomy plus radioactive iodine","Total laryngectomy","Bilateral radical neck dissection"],0,
"For properly selected low-risk unilateral differentiated thyroid cancer confined to one lobe and no nodal or gross extrathyroidal disease, thyroid lobectomy can be definitive. Contemporary guidelines increasingly emphasize the minimum oncologically adequate operation rather than routine total thyroidectomy for every cancer.",
["Correct. Lobectomy is an appropriate definitive operation for selected low-risk unilateral disease.","Total thyroidectomy and radioactive iodine are not mandatory for every small low-risk papillary carcinoma.","Laryngectomy is unrelated to an intrathyroidal papillary carcinoma.","There is no clinical nodal disease to justify bilateral radical dissection."],
"The word cancer does not automatically make the correct thyroid operation bilateral.",
"Which preoperative findings would shift the recommendation toward total thyroidectomy or therapeutic nodal surgery?"),

_q("v233_tps_dtc_app","Differentiated Thyroid Cancer","application",
"A patient has a 3.2-cm unilateral papillary thyroid carcinoma with no gross extrathyroidal extension or suspicious nodes and a normal contralateral lobe. Which counseling statement best reflects the 2025 ATA approach?",
["Total thyroidectomy is mandatory because the tumor is over 2 cm","Either lobectomy or total thyroidectomy may be reasonable after considering tumor features, contralateral disease, anticipated adjuvant/surveillance needs, and patient preference","Observation is mandatory","Central neck dissection is required in every cN0 patient"],1,
"The 2025 ATA framework permits lobectomy or total thyroidectomy for selected unilateral cancers greater than 2 cm and up to 4 cm when there is no gross extrathyroidal extension or nodal disease. The choice is individualized by cancer features, contralateral nodules, follow-up strategy, potential radioactive iodine needs, and patient preference.",
["Tumor size alone in this range no longer mandates total thyroidectomy when other high-risk features are absent.","Correct. Extent of surgery is a shared, risk-adapted decision in selected 2-4 cm unilateral DTC.","Observation is not automatically appropriate for a 3.2-cm established carcinoma.","Prophylactic central neck dissection is not required for every clinically node-negative papillary carcinoma."],
"For selected 2-4 cm unilateral DTC, lobectomy versus total thyroidectomy is a decision—not a reflex.",
"How would a suspicious contralateral nodule or planned radioactive iodine alter the choice?"),

_q("v233_tps_dtc_snr","Differentiated Thyroid Cancer","senior_decision",
"After lobectomy for a low-risk papillary carcinoma, final pathology is favorable and there is no persistent disease. The patient asks whether completion thyroidectomy is automatically required. What is the best response?",
["Yes; completion thyroidectomy is mandatory after any cancer diagnosis","No; completion thyroidectomy is now selective and may be considered for persistent disease, radioactive-iodine strategy, surveillance needs, or other risk features rather than performed routinely","Yes, because thyroglobulin can never be followed after lobectomy","No further surveillance is necessary"],1,
"Current risk-adapted management does not require completion thyroidectomy for every favorable cancer discovered after lobectomy. Completion is considered when residual disease, risk features, radioactive iodine plans, or surveillance strategy make removal of the remaining lobe clinically useful.",
["Routine completion would over-treat many low-risk patients.","Correct. The indication depends on what completion would accomplish oncologically or for subsequent management.","Thyroglobulin interpretation is different after lobectomy but follow-up remains possible.","Lobectomy does not eliminate the need for risk-appropriate surveillance."],
"Completion thyroidectomy should answer a management need, not merely complete an anatomic symmetry.",
"Which adverse pathology findings would make completion more compelling?"),

_q("v233_tps_php_fnd","Primary Hyperparathyroidism","foundation",
"A patient has repeatedly elevated serum calcium with inappropriately elevated PTH. What diagnosis is most likely after appropriate exclusion of mimics?",
["Primary hyperparathyroidism","Primary hypothyroidism","SIADH","Addison disease"],0,
"Primary hyperparathyroidism is characterized by hypercalcemia with a PTH level that is elevated or inappropriately non-suppressed. Evaluation also assesses renal function, vitamin D status, skeletal effects, kidney stones, and alternative diagnoses such as familial hypocalciuric hypercalcemia.",
["Correct. PTH should be suppressed by hypercalcemia; an elevated or non-suppressed level is inappropriate.","Hypothyroidism does not produce this calcium-PTH pattern.","SIADH is a sodium/water disorder rather than a PTH-mediated hypercalcemia syndrome.","Adrenal insufficiency does not classically create this persistent PTH-dependent pattern."],
"In hypercalcemia, an unsuppressed PTH localizes the problem to a PTH-dependent pathway.",
"How does urinary calcium help distinguish primary hyperparathyroidism from familial hypocalciuric hypercalcemia?"),

_q("v233_tps_php_app","Primary Hyperparathyroidism","application",
"A patient with confirmed primary hyperparathyroidism has recurrent nephrolithiasis and osteoporosis. What is the best management principle?",
["Parathyroidectomy is indicated if the patient is an acceptable operative candidate","Observation is mandatory because symptoms do not matter","Treat only with antibiotics","Perform total thyroidectomy"],0,
"Symptomatic end-organ disease such as nephrolithiasis, skeletal disease, or other guideline-based indications supports parathyroidectomy in an appropriate surgical candidate. Localization imaging is used for operative planning after the biochemical diagnosis is established, not to decide whether the disease exists.",
["Correct. Kidney stones and osteoporosis are clinically important target-organ manifestations supporting surgery.","Symptomatic disease is not an observation-only condition by default.","Antibiotics do not treat PTH-mediated hypercalcemia.","Thyroid removal does not treat a parathyroid adenoma."],
"Diagnose hyperparathyroidism biochemically; localize the gland only after deciding surgery is indicated.",
"Why is a negative sestamibi scan not a reason to revoke a biochemical diagnosis?"),

_q("v233_tps_php_snr","Primary Hyperparathyroidism","senior_decision",
"A patient has biochemically proven primary hyperparathyroidism, but ultrasound and sestamibi are discordant and suggest different glands. What is the best attending-level principle?",
["Cancel surgery because localization is not concordant","Choose an operative strategy based on disease biology and confidence in localization; bilateral exploration remains valid when focused surgery cannot be reliably targeted","Operate on whichever image was performed last","Biopsy both parathyroid glands percutaneously"],1,
"Localization studies guide the route of surgery but do not establish the diagnosis. Discordant or nonlocalizing imaging may make a focused approach less appropriate and should prompt consideration of bilateral exploration, intraoperative PTH strategy, surgeon experience, and the possibility of multigland disease.",
["Imaging failure does not erase a biochemical surgical indication.","Correct. The operative plan should become more comprehensive when localization confidence falls.","Recency does not determine imaging truth.","Percutaneous parathyroid biopsy is generally unnecessary and can create diagnostic and operative problems."],
"When localization is weak, broaden the operation—not the biochemical uncertainty.",
"Which history features should raise concern for multigland or hereditary disease?","OR_prep"),

_q("v233_tps_sgmal_fnd","Salivary Gland Malignancy","foundation",
"Which presentation is most concerning for a malignant parotid tumor rather than a typical benign neoplasm?",
["Slow painless mobile mass with intact facial function","Facial weakness, pain, fixation, skin involvement, rapid growth, or suspicious cervical nodes","Stable soft lesion unchanged for years","Bilateral symmetric gland enlargement during dehydration"],1,
"Most parotid masses are benign, but facial nerve dysfunction, pain, fixation, skin involvement, rapid growth, and nodal disease raise concern for malignancy. Preoperative evaluation should define histology as well as facial-nerve and regional-neck status because both alter surgery.",
["This phenotype is more typical of a benign salivary neoplasm.","Correct. Cranial-nerve dysfunction or invasive clinical behavior is a major malignant warning sign.","Long-term stability lowers concern for an aggressive malignancy.","Symmetric physiologic swelling is not the typical presentation of a focal salivary carcinoma."],
"A parotid mass plus facial weakness is malignant until proven otherwise.",
"Which imaging and tissue-sampling strategy best evaluates suspected deep-lobe or skull-base extension?"),

_q("v233_tps_sgmal_app","Salivary Gland Malignancy","application",
"A high-grade parotid carcinoma is resectable and has clinically positive cervical nodes. What is the best operative framework?",
["Treat the parotid primary alone and ignore the neck","Resect the primary with facial-nerve management based on actual nerve involvement and perform therapeutic neck treatment appropriate to the nodal disease","Sacrifice the facial nerve automatically in every malignancy","Observe the nodes until they become symptomatic"],1,
"Salivary malignancy surgery is driven by histology, extent, nerve involvement, and neck status. A functioning facial nerve that is not invaded should generally be preserved, whereas gross nerve invasion may require oncologic sacrifice with reconstruction planning. Clinically positive nodal disease warrants therapeutic regional treatment.",
["Ignoring established nodal metastasis undertreats regional disease.","Correct. Primary, nerve, and neck decisions should match the actual disease map.","Malignancy alone is not an indication to sacrifice an uninvolved functioning facial nerve.","Known nodal disease should not be observed until symptomatic when curative regional treatment is appropriate."],
"In parotid cancer, preserve a clean nerve; sacrifice and reconstruct an invaded nerve when oncologically necessary.",
"How would preoperative facial paralysis change counseling about nerve resection and reconstruction?","OR_prep"),

_q("v233_tps_sgmal_snr","Salivary Gland Malignancy","senior_decision",
"A salivary carcinoma tracks along a named cranial nerve toward the skull base on MRI. What should dominate the senior treatment plan?",
["Treat only the visible gland mass","Map the full perineural pathway centrally, define resectability and skull-base extent, and coordinate surgery and adjuvant radiation around the nerve trajectory","Assume all perineural invasion is microscopic and irrelevant","Perform superficial parotidectomy without reviewing the MRI"],1,
"Clinical or radiographic perineural spread can extend far beyond the apparent gland mass and materially changes surgical margins, skull-base planning, cranial-nerve morbidity, and radiation fields. The treatment plan must follow the nerve to its central endpoint rather than treating only the primary bed.",
["Local-only treatment can leave gross proximal disease behind.","Correct. Named-nerve spread is an anatomic route of cancer extension that must be staged and treated deliberately.","Radiographic nerve enhancement and neuropathy indicate clinically meaningful disease, not an incidental microscopic finding.","Ignoring extent-defining MRI risks an incomplete operation."],
"For salivary cancer with named-nerve spread, the nerve is part of the tumor map.",
"When does proximal skull-base extension make definitive radiation preferable to morbid incomplete resection?"),

_q("v233_tps_mtc_fnd","Medullary Thyroid Cancer","foundation",
"Which biomarker pair is particularly useful in medullary thyroid carcinoma?",
["Calcitonin and CEA","Thyroglobulin and anti-thyroglobulin antibody only","AFP and beta-hCG","PSA and alkaline phosphatase"],0,
"Medullary thyroid carcinoma arises from parafollicular C cells and commonly secretes calcitonin; CEA is also useful for burden and surveillance. Unlike differentiated follicular-cell cancers, thyroglobulin is not the primary disease marker.",
["Correct. Calcitonin and CEA are central biomarkers for MTC.","Thyroglobulin is a follicular-cell marker rather than the principal marker for MTC.","AFP and beta-hCG are not standard MTC markers.","PSA is a prostate marker and alkaline phosphatase is nonspecific."],
"MTC is a C-cell cancer: think calcitonin, CEA, and RET—not thyroglobulin and radioactive iodine.",
"Why does MTC not respond to radioactive iodine the way differentiated thyroid cancer can?"),

_q("v233_tps_mtc_app","Medullary Thyroid Cancer","application",
"A patient is newly diagnosed with medullary thyroid carcinoma. What additional evaluation has major implications for the patient and family?",
["Germline RET testing and assessment for associated MEN2 disease","No genetic testing because MTC is never hereditary","BRCA testing only","Testing only if distant metastases are present"],0,
"A meaningful proportion of MTC is hereditary through germline RET variants. RET testing informs MEN2 evaluation, pheochromocytoma and hyperparathyroidism screening, family counseling, and timing of prophylactic thyroid surgery in affected relatives.",
["Correct. Germline RET status can change the patient's endocrine workup and relatives' care.","Hereditary MTC is well established.","BRCA is not the principal hereditary pathway for MTC.","Genetic evaluation is relevant at diagnosis, not only after distant spread."],
"Before operating on hereditary MTC, remember that an unrecognized pheochromocytoma can be more immediately dangerous than the thyroid cancer.",
"What endocrine condition must be excluded and treated first in a MEN2 patient before thyroid surgery?"),

_q("v233_tps_mtc_snr","Medullary Thyroid Cancer","senior_decision",
"A patient with MTC has a markedly elevated calcitonin level and bulky lateral neck adenopathy. What is the best attending-level planning principle?",
["Treat as a small isolated thyroid nodule","Stage the central and lateral neck and distant disease burden before defining thyroid and compartment-oriented nodal surgery; avoid limited node-picking","Give radioactive iodine first","Perform lobectomy only regardless of hereditary status or nodal disease"],1,
"MTC frequently involves central and lateral cervical nodes, and the extent of surgery should reflect structural disease rather than isolated removal of palpable nodes. Very high calcitonin levels also raise concern for distant disease and can influence the proportionality of extensive local surgery.",
["Bulky nodal disease requires a regional-cancer framework.","Correct. MTC surgery should be compartment-oriented and informed by the full disease burden.","MTC does not use iodine uptake as an effective therapeutic mechanism.","Lobectomy alone is generally inadequate for established MTC with bulky nodal disease."],
"In MTC, stage the patient before escalating the neck; biomarker burden can be a clue that disease extends beyond what you can palpate.",
"How should extensive distant metastases change the morbidity you are willing to accept for cervical disease control?","boards"),
]


def apply_learning_ladders_v233(challenges,item_id_fn):
    existing={str(q.get("id")) for q in challenges if q.get("id")}; added=0
    for q in VIGNETTES_V233:
        row=dict(q); row["concept_id"]=item_id_fn(DOMAIN,row["topic"])
        if not row["concept_id"]: raise RuntimeError("v233 orphan: "+row["topic"])
        if row["id"] not in existing:
            challenges.append(row); existing.add(row["id"]); added+=1
    return {"added":added,"reviewed_topics":5}
