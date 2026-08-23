"""
v13.4 - Decision-heavy vignette batch for Thyroid/Parathyroid/Salivary and
Head & Neck Oncology. The cases are intentionally management-discriminating:
recognition alone is not enough to answer them.
"""

VIGNETTES_V134 = [
    {
        "id": "v134_tps_01", "domain": "Thyroid / Parathyroid / Salivary", "topic": "Differentiated Thyroid Cancer: Active Surveillance",
        "stem": "A healthy 46-year-old has a 7 mm biopsy-proven papillary thyroid carcinoma confined to one lobe. Ultrasound shows no suspicious cervical nodes, no extrathyroidal extension, and the tumor is not abutting the trachea or expected RLN course. She is reliable for follow-up and strongly prefers to avoid surgery. What is the best management framework?",
        "choices": ["Total thyroidectomy because any biopsy-proven papillary carcinoma requires surgery", "Active surveillance is a reasonable option with structured ultrasound follow-up and predefined triggers for intervention", "Radioactive iodine without surgery", "Observation without planned imaging unless symptoms develop"],
        "answer": 1,
        "explanation": "Selected small, low-risk intrathyroidal papillary carcinomas can be managed with active surveillance when anatomy is favorable, there is no clinically significant nodal disease, and the patient can comply with longitudinal ultrasound. Surveillance is structured management, not passive neglect.",
        "why_wrong": ["Modern differentiated-thyroid-cancer management does not require total thyroidectomy for every papillary carcinoma.", "Correct.", "RAI is not primary therapy for an intact small low-risk papillary carcinoma.", "Active surveillance requires scheduled imaging and explicit conversion criteria rather than symptom-only follow-up."],
        "board_pearl": "For a microcarcinoma, ask three things before reflexively operating: biology, anatomy, and whether the patient is a reliable surveillance candidate.",
        "curveball": "The same 7 mm tumor is now immediately adjacent to the tracheoesophageal groove with concern that future growth could threaten the RLN. How does that change your recommendation?",
        "tier": "Curated chief-level", "mode": "Vignette"
    },
    {
        "id": "v134_tps_02", "domain": "Thyroid / Parathyroid / Salivary", "topic": "Completion Thyroidectomy",
        "stem": "A patient underwent lobectomy for a 2.3 cm indeterminate nodule. Final pathology shows a completely excised, intrathyroidal, differentiated thyroid carcinoma without vascular invasion, aggressive histology, nodal disease, or adverse margins. The contralateral lobe is normal on ultrasound. What is the best next step?",
        "choices": ["Completion thyroidectomy is mandatory because the tumor was malignant", "Discuss surveillance versus selective completion thyroidectomy; completion is not automatically required", "Immediate neck dissection", "RAI can be given effectively without considering the remaining lobe"],
        "answer": 1,
        "explanation": "Completion thyroidectomy is now selective in properly chosen low-risk differentiated cancers. The decision should be driven by adverse pathology, persistent disease, need for RAI, the value of thyroglobulin surveillance, contralateral disease, and patient preference—not malignancy alone.",
        "why_wrong": ["Cancer after lobectomy is not itself an absolute indication for completion thyroidectomy.", "Correct.", "There is no nodal disease described to justify neck dissection.", "A large intact contralateral thyroid lobe changes the utility of RAI and thyroglobulin-based follow-up; this option bypasses the actual decision."],
        "board_pearl": "Completion thyroidectomy should answer a specific oncologic question. If you cannot name what the second operation accomplishes, reconsider whether it is necessary.",
        "curveball": "Final pathology instead shows gross extrathyroidal extension and multiple clinically significant metastatic nodes. What additional reasons now favor completion?",
        "tier": "Curated chief-level", "mode": "Vignette"
    },
    {
        "id": "v134_tps_03", "domain": "Thyroid / Parathyroid / Salivary", "topic": "Radioactive Iodine and TSH Suppression in DTC",
        "stem": "A 68-year-old is disease-free after treatment of low-risk differentiated thyroid carcinoma. Serial neck ultrasound is negative and thyroglobulin remains appropriately reassuring. He has atrial fibrillation and osteopenia. Which principle should guide long-term levothyroxine therapy?",
        "choices": ["Maintain maximal TSH suppression indefinitely regardless of response", "Reassess the need for suppression over time and avoid unnecessary aggressive suppression when there is no evidence of persistent disease", "Stop thyroid hormone entirely", "Use TSH suppression only if radioactive iodine was never given"],
        "answer": 1,
        "explanation": "TSH suppression should be dynamic and risk-adapted. In a patient with an excellent response and competing cardiovascular and skeletal risks, aggressive long-term suppression may create more harm than benefit.",
        "why_wrong": ["The modern approach does not treat initial diagnosis as a permanent mandate for maximal suppression.", "Correct.", "A patient after thyroid surgery still needs physiologic thyroid hormone replacement as appropriate; the question is the degree of suppression.", "RAI exposure is not the sole determinant of whether TSH suppression is appropriate."],
        "board_pearl": "Response-to-therapy can change the TSH goal. Reassess suppression rather than carrying the postoperative target forward forever.",
        "curveball": "What if the patient has structurally persistent metastatic disease despite therapy? How would that shift the risk-benefit balance?",
        "tier": "Curated chief-level", "mode": "Vignette"
    },
    {
        "id": "v134_tps_04", "domain": "Thyroid / Parathyroid / Salivary", "topic": "Radioiodine-Refractory Differentiated Thyroid Cancer",
        "stem": "A patient with metastatic differentiated thyroid carcinoma has pulmonary metastases that no longer concentrate iodine and have shown clear radiographic progression over serial scans. He is minimally symptomatic. What is the most appropriate next conceptual step?",
        "choices": ["Continue repeated empiric RAI indefinitely", "Establish disease tempo, symptoms and molecular profile, then decide among observation, local therapy and systemic targeted treatment", "Perform total laryngectomy", "Treat only when life-threatening symptoms appear"],
        "answer": 1,
        "explanation": "RAI-refractory disease should not trigger endless empiric RAI or reflexive systemic treatment. Management depends on clinically meaningful progression, symptoms, threat to critical structures, resectability/local options and tumor molecular biology.",
        "why_wrong": ["Repeated RAI is inappropriate when disease is clearly non-avid and progressing.", "Correct.", "Laryngectomy has no role for isolated pulmonary metastatic progression without a laryngeal indication.", "Waiting for a crisis may forfeit effective local or systemic treatment in clearly progressive disease."],
        "board_pearl": "RAI-refractory is a disease state, not an automatic drug order. First define progression and urgency; then choose the least morbid effective strategy.",
        "curveball": "One metastatic lesion is rapidly enlarging next to the spinal cord while all other disease is stable. Why might local therapy be preferable before changing systemic therapy?",
        "tier": "Curated chief-level", "mode": "Vignette"
    },
    {
        "id": "v134_tps_05", "domain": "Thyroid / Parathyroid / Salivary", "topic": "Primary Thyroid Lymphoma",
        "stem": "A 72-year-old with long-standing Hashimoto thyroiditis develops rapid thyroid enlargement over 5 weeks with dysphagia and bulky cervical adenopathy. What diagnostic strategy is most useful before planning definitive treatment?",
        "choices": ["Immediate total thyroidectomy for diagnosis and treatment", "Obtain adequate tissue for histology and flow cytometry, often with core biopsy, while assessing airway stability", "RAI scan as the only test", "Treat empirically as bacterial thyroiditis"],
        "answer": 1,
        "explanation": "The combination of rapid enlargement, Hashimoto history and bulky adenopathy is classic for thyroid lymphoma. Adequate tissue architecture and flow cytometry are important because therapy is primarily hematologic/radiation-based rather than thyroidectomy.",
        "why_wrong": ["Thyroidectomy is not routine definitive therapy for lymphoma and may add morbidity before the diagnosis is established.", "Correct.", "RAI imaging does not establish lymphoma histology.", "The pattern is not typical for ordinary bacterial thyroiditis and warrants urgent malignancy evaluation."],
        "board_pearl": "Rapid thyroid growth has two board-favorite branches—anaplastic carcinoma and lymphoma. Hashimoto plus bulky nodes should push lymphoma high on the list.",
        "curveball": "The patient develops stridor while awaiting biopsy. What immediate priorities supersede the ideal diagnostic sequence?",
        "tier": "Curated board-style", "mode": "Vignette"
    },
    {
        "id": "v134_tps_06", "domain": "Thyroid / Parathyroid / Salivary", "topic": "Familial Hyperparathyroidism and Parathyromatosis",
        "stem": "A 29-year-old has recurrent primary hyperparathyroidism after prior surgery and a family history of hyperparathyroidism and pituitary tumors. Which mistake is most important to avoid?",
        "choices": ["Assuming this is simply another sporadic solitary adenoma without evaluating hereditary multigland disease", "Checking prior operative reports", "Reviewing calcium and PTH trends", "Considering genetic evaluation"],
        "answer": 0,
        "explanation": "Young age, recurrence and a family history of pituitary tumors strongly suggest a hereditary syndrome such as MEN1, where multigland disease and recurrence are expected. The underlying biology must shape reoperative planning and family counseling.",
        "why_wrong": ["Correct.", "Prior operative anatomy is essential in reoperative parathyroid surgery.", "The biochemical chronology helps distinguish persistent from recurrent disease and confirms the indication.", "Genetic evaluation is appropriate when the phenotype suggests a hereditary syndrome."],
        "board_pearl": "In a young patient with multigland/recurrent disease, stop thinking 'find the adenoma' and start thinking 'what syndrome and what lifetime gland biology?'.",
        "curveball": "The prior pathology report notes capsular rupture with parathyroid tissue fragments in the field. What additional cause of recurrence should enter your differential?",
        "tier": "Curated board-style", "mode": "Vignette"
    },
    {
        "id": "v134_tps_07", "domain": "Thyroid / Parathyroid / Salivary", "topic": "Salivary Adenoid Cystic Carcinoma and Perineural Spread",
        "stem": "A patient with a minor salivary gland malignancy of the hard palate reports progressive numbness extending into the midface. MRI shows enhancement tracking along V2 toward foramen rotundum. What is the key oncologic implication?",
        "choices": ["The neuropathy is unrelated because salivary tumors do not spread along nerves", "Perineural spread must be mapped to the skull base and incorporated into surgical and radiation planning", "Only the palpable primary needs treatment", "A neck dissection alone addresses the principal route of spread"],
        "answer": 1,
        "explanation": "Adenoid cystic carcinoma classically tracks along named nerves. Symptoms and MRI evidence of V2 spread require treatment planning along the involved neural pathway toward the skull base rather than treating only the visible primary.",
        "why_wrong": ["Perineural spread is a hallmark concern in adenoid cystic carcinoma.", "Correct.", "Treating only the palpable lesion risks leaving gross or microscopic neural disease behind.", "Neck management does not address skull-base perineural spread."],
        "board_pearl": "Pain, numbness or weakness in a salivary cancer is an anatomic clue: follow the nerve centrally until you know where the disease stops.",
        "curveball": "The patient has no clinical numbness but pathology shows microscopic PNI. How does microscopic PNI differ from gross radiographic perineural spread in staging your surgical field?",
        "tier": "Curated chief-level", "mode": "Vignette"
    },
    {
        "id": "v134_hno_01", "domain": "Head & Neck Oncology", "topic": "Salvage Surgery After Chemoradiation",
        "stem": "A patient develops biopsy-proven recurrent oropharyngeal SCC in a previously chemoradiated field. Imaging shows no distant disease, but the recurrence abuts the carotid and the patient is already feeding-tube dependent with severe baseline dysphagia. What is the most important next step before offering salvage surgery?",
        "choices": ["Schedule resection immediately because salvage surgery is the only curative option", "Define resectability, carotid/prevertebral involvement, expected postoperative function, reconstructive needs and patient goals in a multidisciplinary setting", "Repeat definitive-dose chemoradiation automatically", "Observe until the tumor becomes symptomatic"],
        "answer": 1,
        "explanation": "Salvage surgery is appropriate only when complete resection is realistic and the expected oncologic and functional benefit justifies major morbidity. Prior radiation, carotid proximity and poor baseline swallowing make preoperative functional and reconstructive planning essential.",
        "why_wrong": ["Technical operability alone does not establish that salvage surgery is beneficial or safe.", "Correct.", "Re-irradiation can be considered selectively but is not automatic and carries major toxicity in a previously treated field.", "Delaying a potentially treatable recurrence until symptoms progress can lose the window for meaningful intervention."],
        "board_pearl": "A salvage case is a three-column decision: oncologic resectability, reconstructive safety, and post-treatment function.",
        "curveball": "Imaging now shows encasement of the carotid and prevertebral fascia fixation. How does that alter the meaning of 'resectable'?",
        "tier": "Curated chief-level", "mode": "Vignette"
    },
    {
        "id": "v134_hno_02", "domain": "Head & Neck Oncology", "topic": "Carotid Blowout Syndrome",
        "stem": "A previously irradiated patient with recurrent hypopharyngeal cancer and a draining neck fistula has 30 mL of bright-red bleeding from the wound that stops with pressure. He is currently hemodynamically stable. What is the safest interpretation?",
        "choices": ["Minor wound bleeding that can be observed overnight", "A sentinel bleed from a threatened carotid until proven otherwise", "Expected granulation-tissue bleeding after radiation", "A reason to discharge if hemoglobin is normal"],
        "answer": 1,
        "explanation": "A sentinel bleed in an irradiated, infected or fistulized neck can precede catastrophic carotid rupture. Even if bleeding stops, this is a vascular emergency requiring airway/resuscitation planning and urgent endovascular/vascular evaluation.",
        "why_wrong": ["Observation alone risks missing the warning phase before exsanguination.", "Correct.", "The clinical context makes carotid injury far too dangerous to attribute to granulation tissue without urgent evaluation.", "A normal hemoglobin does not exclude an impending carotid blowout."],
        "board_pearl": "The most dangerous carotid blowout question often starts with bleeding that has already stopped.",
        "curveball": "The patient suddenly rebleeds massively into the pharynx and cannot protect the airway. What priorities happen before diagnostic imaging?",
        "tier": "Curated overnight-call", "mode": "Vignette"
    },
    {
        "id": "v134_hno_03", "domain": "Head & Neck Oncology", "topic": "Nonfunctional Larynx and Intractable Aspiration",
        "stem": "A patient is 4 years disease-free after chemoradiation for laryngeal cancer but has recurrent aspiration pneumonia, chronic feeding-tube dependence and profound silent aspiration despite intensive swallow therapy. Imaging and biopsy show no recurrence. Which concept best frames management?",
        "choices": ["Organ preservation was successful, so laryngectomy is contraindicated", "The patient may have a nonfunctional larynx, and aspiration-prevention surgery including functional laryngectomy can be considered", "Only additional swallowing therapy is ever appropriate", "Total laryngectomy is only an oncologic operation"],
        "answer": 1,
        "explanation": "An anatomically preserved larynx may be functionally devastating after late radiation injury. In carefully selected disease-free patients with life-threatening intractable aspiration despite rehabilitation, functional/total laryngectomy can restore airway-alimentary separation.",
        "why_wrong": ["Organ preservation does not guarantee preserved function.", "Correct.", "Therapy should be maximized, but persistent life-threatening aspiration can require surgery.", "Laryngectomy can be performed for severe functional indications even without recurrent cancer."],
        "board_pearl": "The endpoint of organ-preservation therapy is not merely keeping the larynx in the neck; airway protection, swallowing and communication still matter.",
        "curveball": "What wound complication is especially important when performing laryngectomy in a heavily irradiated field, and how can reconstruction reduce that risk?",
        "tier": "Curated chief-level", "mode": "Vignette"
    },
    {
        "id": "v134_hno_04", "domain": "Head & Neck Oncology", "topic": "Free Flap Monitoring and Salvage",
        "stem": "Six hours after oral cavity free-flap reconstruction, the flap becomes swollen and violaceous. Pinprick produces brisk dark blood, and the Doppler signal is weaker than baseline. What should happen next?",
        "choices": ["Wait 6 hours and repeat the exam", "Treat this as venous compromise and urgently evaluate for takeback while correcting any obvious external compression", "Apply ice and elevate the head only", "Start antibiotics and reassess in the morning"],
        "answer": 1,
        "explanation": "Congestion, violaceous color and brisk dark bleeding are classic for venous outflow compromise. Flap salvage is time-dependent, so concern for thrombosis or pedicle compression should trigger immediate action and usually urgent exploration rather than serial delay.",
        "why_wrong": ["Delay reduces salvage probability if the pedicle is thrombosed.", "Correct.", "Positioning can help minor edema but is not definitive treatment for a failing flap.", "Infection is not the best explanation for this acute vascular pattern six hours after surgery."],
        "board_pearl": "Venous congestion is a 'now' problem: purple, swollen, dark brisk blood. Arterial failure is usually pale, cool and poorly bleeding.",
        "curveball": "The external Doppler signal is still present. Does that rule out venous thrombosis?",
        "tier": "Curated overnight-call", "mode": "Vignette"
    },
    {
        "id": "v134_hno_05", "domain": "Head & Neck Oncology", "topic": "Neck Dissection Complications",
        "stem": "After a left level IV neck dissection, the drain becomes milky after enteral feeds are started. Output is 700 mL over 24 hours. What is the most likely diagnosis and why is the anatomy predictable?",
        "choices": ["Salivary fistula from submandibular duct injury", "Chyle leak from thoracic duct injury near the left lower neck", "CSF leak from spinal accessory nerve injury", "Lymphatic leak from the right lymphatic duct, which normally enters on the left"],
        "answer": 1,
        "explanation": "The thoracic duct enters the venous system in the left lower neck near the internal jugular-subclavian junction and is at risk during level IV dissection. Milky high-volume output after feeds is classic for chyle leak.",
        "why_wrong": ["A salivary fistula is not expected from a level IV dissection and would not classically become milky with enteral fat intake.", "Correct.", "CN XI injury causes shoulder dysfunction, not CSF drainage.", "The right lymphatic duct drains the right side and enters the right venous angle."],
        "board_pearl": "A neck-dissection complication is often localized by level: left level IV plus milky drain equals thoracic duct until proven otherwise.",
        "curveball": "What clinical features would make you escalate from conservative treatment toward operative or interventional management?",
        "tier": "Curated board-style", "mode": "Vignette"
    },
    {
        "id": "v134_hno_06", "domain": "Head & Neck Oncology", "topic": "Neck Dissection Complications",
        "stem": "After a selective neck dissection, a patient has new difficulty abducting the shoulder above horizontal with scapular winging and trapezius weakness. Which structure is most likely injured?",
        "choices": ["Hypoglossal nerve", "Spinal accessory nerve", "Phrenic nerve", "Marginal mandibular nerve"],
        "answer": 1,
        "explanation": "CN XI innervates trapezius; injury produces shoulder droop, weak abduction/elevation and scapular dysfunction. Even when anatomically preserved, traction or devascularization can produce postoperative shoulder syndrome.",
        "why_wrong": ["CN XII injury causes tongue weakness and deviation.", "Correct.", "Phrenic injury causes hemidiaphragm dysfunction.", "Marginal mandibular injury causes lower-lip asymmetry."],
        "board_pearl": "Post-neck-dissection shoulder complaints are not generic pain until proven otherwise—examine trapezius and scapular mechanics specifically.",
        "curveball": "The nerve was anatomically preserved during surgery. How can postoperative shoulder dysfunction still occur, and what early intervention matters?",
        "tier": "Curated board-style", "mode": "Vignette"
    },
    {
        "id": "v134_hno_07", "domain": "Head & Neck Oncology", "topic": "Palliative Decision-Making in Head and Neck Cancer",
        "stem": "A patient with widely metastatic recurrent oral cavity cancer has a painful fungating neck mass and intermittent oozing but no impending airway compromise. Performance status is poor, and the patient prioritizes staying out of the hospital. Which approach best reflects high-quality head-and-neck care?",
        "choices": ["Offer the largest technically possible resection because local control is always the priority", "Clarify goals and use symptom-directed measures such as analgesia, wound care and palliative radiation only if the expected benefit matches the patient's priorities", "Avoid discussing prognosis because it could remove hope", "Recommend tracheostomy prophylactically even without an airway indication"],
        "answer": 1,
        "explanation": "Palliative head-and-neck care is active, goal-concordant symptom management. Procedures and radiation should be tied to a realistic symptom target and burden-benefit assessment rather than to technical feasibility alone.",
        "why_wrong": ["Major surgery can impose substantial morbidity without meaningful survival or quality-of-life benefit in this setting.", "Correct.", "Clear prognostic communication supports informed decisions and does not preclude hope.", "A prophylactic tracheostomy adds burden and risk when there is no current airway goal it addresses."],
        "board_pearl": "For every palliative procedure, finish the sentence: 'I am doing this to improve ___, with an expected benefit of ___, at the cost of ___.'.",
        "curveball": "The patient later develops recurrent major bleeding from a tumor eroding toward the carotid. How does the plan change even if the overall goals remain comfort-focused?",
        "tier": "Curated chief-level", "mode": "Vignette"
    },
    {
        "id": "v134_hno_08", "domain": "Head & Neck Oncology", "topic": "Salvage Surgery After Chemoradiation",
        "stem": "A patient has a small, biopsy-proven local recurrence after prior radiation. There is no distant disease, the recurrence is technically resectable with clear margins, baseline swallowing is good, and reconstruction can be performed with vascularized tissue. Which feature most strongly supports offering salvage surgery?",
        "choices": ["The mere fact that the patient already received radiation", "A realistic chance of complete resection with acceptable functional and reconstructive morbidity", "The patient's age alone", "The ability to perform any operation, even if gross disease must remain"],
        "answer": 1,
        "explanation": "Salvage surgery is most compelling when complete resection is realistic and the patient can tolerate the expected functional and reconstructive consequences. Prior radiation increases complexity but does not by itself argue for or against surgery.",
        "why_wrong": ["Prior radiation is context, not the treatment indication.", "Correct.", "Age alone is a poor surrogate for fitness or expected benefit.", "Leaving gross disease behind usually defeats the oncologic purpose of major salvage surgery unless a clearly palliative goal has been defined."],
        "board_pearl": "The strongest salvage indication is not 'recurrence after RT'—it is 'resectable recurrence with a meaningful chance of durable control and acceptable function.'.",
        "curveball": "What factors would make you favor systemic therapy or re-irradiation instead of salvage surgery?",
        "tier": "Curated chief-level", "mode": "Vignette"
    },
    {
        "id": "v134_hno_09", "domain": "Head & Neck Oncology", "topic": "Free Flap Monitoring and Salvage",
        "stem": "A flap that was pink and warm at midnight is pale and cool at 2 AM. Pinprick produces almost no bleeding and the arterial Doppler signal is absent. What is the best interpretation?",
        "choices": ["Expected postoperative vasoconstriction", "Arterial inflow compromise requiring urgent evaluation and likely exploration", "Venous congestion", "Normal change after fluid restriction"],
        "answer": 1,
        "explanation": "Pallor, cool temperature, poor pinprick bleeding and loss of arterial Doppler are classic for arterial inflow failure. The change from a documented normal baseline makes this especially concerning and time-sensitive.",
        "why_wrong": ["The combination of objective changes is not a benign expected variation.", "Correct.", "Venous compromise is more often swollen, violaceous and associated with dark brisk bleeding.", "Fluid status does not explain abrupt loss of arterial signal with a pale cold flap."],
        "board_pearl": "Flap monitoring is trend-based: a changed flap is more important than an isolated borderline finding.",
        "curveball": "At exploration the artery is patent but a tight neck hematoma is compressing the pedicle. What does this teach about the differential for a 'thrombosed' flap?",
        "tier": "Curated overnight-call", "mode": "Vignette"
    },
]
