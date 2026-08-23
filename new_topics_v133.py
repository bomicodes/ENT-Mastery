"""
v13.3 - Depth-pass curriculum expansion for the two weakest domains after the
facial-plastics patch. These are decision-heavy, board- and chief-level topics
that were either absent or too fragmented to support good adaptive cases.

The runtime merge is idempotent and skips an exact canonical topic if it
already exists in DEEP_MODULES_V6.
"""

NEW_TOPICS_V133 = {
    "Thyroid / Parathyroid / Salivary": [
        {
            "topic": "Differentiated Thyroid Cancer: Active Surveillance",
            "recognize": "A small, intrathyroidal, low-risk papillary thyroid carcinoma without clinically apparent nodal disease, aggressive features, or threatening proximity to critical structures may be appropriate for active surveillance rather than immediate surgery in a reliable patient.",
            "localize": "Suitability depends on tumor behavior and anatomy: intrathyroidal disease away from the trachea and recurrent laryngeal nerve, no clinically significant nodal disease, and no evidence of invasive/aggressive biology.",
            "workup": "Confirm high-quality neck ultrasound, document tumor size and relationship to the capsule/trachea/RLN, evaluate the central and lateral neck, and establish that the patient can comply with serial ultrasound follow-up. Cytology and molecular information can refine risk when available.",
            "manage": "Use shared decision-making between active surveillance and surgery. Surveillance requires a defined ultrasound schedule and explicit triggers for intervention such as meaningful growth, new nodal disease, invasion, or patient preference.",
            "operate": "When surgery is chosen for a low-risk unilateral differentiated cancer, lobectomy is often sufficient; the 2025 ATA framework further favors lobectomy for properly selected cancers confined to one lobe and no larger than 2 cm, with individualized decisions for 2-4 cm tumors.",
            "teach": "Active surveillance is not 'doing nothing' - it is structured longitudinal management for selected low-risk disease, with anatomy, biology, patient reliability, and defined conversion-to-treatment criteria driving safety.",
            "tags": ["papillary thyroid cancer", "active surveillance", "lobectomy", "2025 ATA"]
        },
        {
            "topic": "Completion Thyroidectomy",
            "recognize": "A patient who underwent thyroid lobectomy and is found on final pathology to have differentiated thyroid carcinoma does not automatically require removal of the contralateral lobe.",
            "localize": "The key question is whether residual thyroid tissue creates a meaningful oncologic, adjuvant-therapy, or surveillance problem rather than whether carcinoma is simply present in the removed lobe.",
            "workup": "Review final pathology for tumor size, margins, extrathyroidal extension, vascular invasion, aggressive histology, multifocality and nodal disease; reassess the contralateral thyroid and neck ultrasound and clarify whether radioactive iodine or thyroglobulin-based follow-up would materially benefit from total thyroidectomy.",
            "manage": "Completion thyroidectomy is selective, not routine. It may be considered for persistent disease, when radioactive iodine is planned, when bilateral surgery would meaningfully improve surveillance, or when adverse pathology changes the original risk assessment.",
            "operate": "Before reoperation, document vocal fold mobility and review the first operative note. Reoperative thyroid surgery increases RLN and parathyroid risk, so the benefit of completion must justify the added morbidity.",
            "teach": "The modern question is not 'cancer after lobectomy = completion?' but 'what additional oncologic benefit will the second operation provide this specific patient?'.",
            "tags": ["thyroid cancer", "completion thyroidectomy", "reoperation", "2025 ATA"]
        },
        {
            "topic": "Radioactive Iodine and TSH Suppression in DTC",
            "recognize": "Radioactive iodine and TSH suppression are risk-adapted adjuvant tools after differentiated thyroid cancer treatment, not automatic consequences of total thyroidectomy.",
            "localize": "RAI targets iodine-avid residual thyroid cancer; TSH suppression reduces trophic stimulation of differentiated thyroid cells. Their value depends on recurrence risk, residual disease, treatment response, age and competing cardiovascular/bone risks.",
            "workup": "Use postoperative pathology, nodal burden, thyroglobulin/antibody trends, neck imaging and response-to-therapy assessment to determine whether RAI or ongoing TSH suppression offers meaningful benefit.",
            "manage": "Avoid reflexive aggressive TSH suppression in patients with no evidence of persistent disease; reassess the degree of suppression over time as response-to-therapy changes. Reserve RAI for patients whose recurrence-risk or residual disease profile makes benefit plausible.",
            "operate": "Surgical extent should not be escalated solely out of habit to enable RAI; decide the operation first on oncologic grounds, then determine adjuvant therapy from final risk assessment.",
            "teach": "Both RAI and TSH suppression are dynamic risk-adapted therapies. The more important question is 'what disease remains and how likely is recurrence?' rather than 'did the patient have thyroid cancer?'.",
            "tags": ["RAI", "TSH suppression", "thyroglobulin", "dynamic risk stratification"]
        },
        {
            "topic": "Radioiodine-Refractory Differentiated Thyroid Cancer",
            "recognize": "Progressive metastatic differentiated thyroid cancer that no longer takes up radioactive iodine, progresses despite appropriate RAI, or has disease unlikely to respond to additional RAI should be considered radioiodine-refractory.",
            "localize": "Dedifferentiated metastatic deposits may lose sodium-iodide symporter function and iodine avidity; disease can remain indolent for long periods or become structurally progressive and symptomatic.",
            "workup": "Document structural progression with cross-sectional imaging, reassess disease tempo and symptoms, review prior iodine avidity and doses, and obtain tumor molecular profiling when systemic therapy is being considered because actionable alterations can change treatment selection.",
            "manage": "Do not give repeated empiric RAI to clearly refractory disease. Observe indolent asymptomatic disease when appropriate; use local therapies for threatening oligoprogressive sites and systemic therapy for progressive, symptomatic, unresectable disease, increasingly guided by molecular targets.",
            "operate": "Surgery still has a role for selected locoregional recurrence or threatening focal disease when complete or meaningful debulking is feasible; refractory systemic disease alone is not an indication for nonbeneficial extensive neck surgery.",
            "teach": "RAI-refractory does not automatically mean 'start a TKI today.' First establish clinically meaningful progression, symptoms, threat to critical structures, and targetable biology.",
            "tags": ["RAI refractory", "metastatic thyroid cancer", "systemic therapy", "molecular testing"]
        },
        {
            "topic": "Primary Thyroid Lymphoma",
            "recognize": "A rapidly enlarging thyroid mass over weeks to months, particularly in an older patient with Hashimoto thyroiditis, with compressive symptoms or cervical adenopathy should raise concern for primary thyroid lymphoma.",
            "localize": "This is a lymphoid malignancy arising in the thyroid, often in a background of chronic autoimmune thyroiditis; diffuse large B-cell lymphoma and MALT lymphoma are important histologies.",
            "workup": "Obtain ultrasound and cross-sectional imaging when compressive or bulky disease is present. Tissue diagnosis requires adequate material for histology and flow cytometry, often core biopsy rather than relying on thyroid FNA cytology alone.",
            "manage": "Treatment is primarily nonsurgical and depends on histology/stage, typically systemic therapy with or without radiation. Secure or protect the airway when clinically necessary while expediting diagnosis.",
            "operate": "Thyroidectomy is not routine therapy for lymphoma; surgery is generally limited to diagnostic uncertainty or airway situations not manageable by less morbid means.",
            "teach": "Rapid thyroid enlargement does not equal anaplastic carcinoma. Hashimoto history plus bulky, fast-growing thyroid disease should make lymphoma an early diagnostic branch because the treatment is fundamentally different.",
            "tags": ["thyroid lymphoma", "Hashimoto", "rapid neck mass", "core biopsy"]
        },
        {
            "topic": "Familial Hyperparathyroidism and Parathyromatosis",
            "recognize": "Primary hyperparathyroidism at a young age, multigland disease, recurrent disease, family history, jaw tumors, pituitary/pancreatic tumors, or unusual parathyroid pathology should prompt consideration of a hereditary syndrome; recurrent hyperparathyroidism after prior parathyroid surgery can also rarely reflect parathyromatosis.",
            "localize": "Hereditary syndromes such as MEN1, MEN2A, CDC73-related disease and familial isolated hyperparathyroidism alter the expected gland distribution and recurrence risk. Parathyromatosis refers to multiple implants/foci of hyperfunctioning parathyroid tissue, sometimes after capsular disruption or seeding.",
            "workup": "Review calcium/PTH chronology, prior operative and pathology reports, family history and syndromic features; pursue syndrome-directed genetic evaluation when indicated and use localization imaging to guide reoperative planning rather than to establish the biochemical diagnosis.",
            "manage": "Management is syndrome- and anatomy-specific. Counsel that multigland/hereditary disease has different recurrence expectations from a solitary sporadic adenoma, and that reoperative disease should be managed in an experienced center.",
            "operate": "Avoid rupturing a parathyroid adenoma or spilling tissue. In reoperative disease, identify the expected recurrent laryngeal nerve course, use prior operative information and localization, and tailor the operation to hereditary versus sporadic biology.",
            "teach": "Young age, multigland disease and recurrence are clues that 'one bad adenoma' may be the wrong mental model; the biology determines the operation and the lifetime surveillance plan.",
            "tags": ["MEN1", "CDC73", "parathyromatosis", "reoperative parathyroid"]
        },
        {
            "topic": "Salivary Adenoid Cystic Carcinoma and Perineural Spread",
            "recognize": "A salivary gland malignancy with disproportionate pain, numbness, weakness, or a long infiltrative course should raise concern for adenoid cystic carcinoma and perineural invasion/spread.",
            "localize": "Adenoid cystic carcinoma has a strong propensity for perineural spread along named cranial nerves toward the skull base and for late distant metastasis, particularly to lung.",
            "workup": "Map cranial nerve deficits on exam and obtain contrast MRI with attention to the involved nerve pathway and skull base when perineural spread is suspected; stage the primary, neck and chest according to disease extent.",
            "manage": "Primary treatment is surgical resection when feasible, commonly followed by postoperative radiation for adverse features including perineural invasion. Long-term surveillance matters because recurrence and distant metastasis can occur late.",
            "operate": "Resection must follow the disease rather than stopping at an arbitrary gland boundary; grossly involved nerve may require sacrifice toward a negative proximal margin when oncologically appropriate, with reconstruction/rehabilitation planned in advance.",
            "teach": "Pain or neuropathy in a salivary tumor is an oncologic localizing sign. Think along the nerve all the way to the skull base, not just around the palpable gland mass.",
            "tags": ["adenoid cystic", "perineural invasion", "skull base", "salivary cancer"]
        },
    ],
    "Head & Neck Oncology": [
        {
            "topic": "Salvage Surgery After Chemoradiation",
            "recognize": "Persistent or recurrent head and neck squamous cell carcinoma in a previously irradiated field requires a new assessment of resectability, expected function, metastatic status and patient goals rather than automatic salvage surgery.",
            "localize": "Prior radiation distorts tissue planes, impairs vascularity and wound healing, and changes the reconstructive problem; recurrence may track along nerves, cartilage, prevertebral fascia or carotid spaces.",
            "workup": "Restage with high-quality cross-sectional imaging and chest assessment, confirm recurrence when feasible, define carotid/prevertebral/skull-base involvement, evaluate baseline swallowing/airway function and review the prior radiation field and dose.",
            "manage": "Offer salvage resection when disease is technically resectable and the expected oncologic and functional benefit justifies morbidity. Otherwise consider systemic therapy, re-irradiation in selected patients, clinical trials or symptom-directed/palliative care.",
            "operate": "Plan reconstruction early. In heavily irradiated fields, vascularized tissue is often needed to protect major vessels and close pharyngeal defects; anticipated carotid exposure, fistula and wound complications should shape flap choice.",
            "teach": "The right salvage question is not 'can I remove it?' but 'can I remove it completely, reconstruct it safely, and leave the patient with a result that is better than nonoperative alternatives?'.",
            "tags": ["salvage surgery", "recurrent SCC", "reirradiation", "reconstruction"]
        },
        {
            "topic": "Carotid Blowout Syndrome",
            "recognize": "Sentinel bleeding from the mouth, pharynx, neck wound or tracheostoma in a previously irradiated or surgically treated head and neck cancer patient can herald carotid blowout and must be treated as a vascular emergency.",
            "localize": "Threatened or ruptured carotid segments are often exposed by recurrent tumor, infection, fistula, wound breakdown or radiation injury; the common or internal carotid can rupture catastrophically.",
            "workup": "Resuscitate first, secure the airway when needed, activate massive-transfusion/vascular pathways, and obtain urgent CTA only if the patient is stable enough. Definitive angiography is frequently both diagnostic and therapeutic.",
            "manage": "Apply temporizing direct pressure/packing when anatomically possible, reverse coagulopathy, and obtain immediate interventional radiology/vascular and head-and-neck surgical support. Endovascular embolization or covered stenting is commonly used depending on anatomy and collateral circulation.",
            "operate": "Open surgical ligation or repair in a hostile irradiated infected field carries major morbidity and is generally reserved for situations in which endovascular control is unavailable or inappropriate; vascularized tissue coverage is critical for threatened exposed vessels.",
            "teach": "A small sentinel bleed in an irradiated neck is not reassuring - it may be the warning before exsanguination. Treat the vessel as threatened until proven otherwise.",
            "tags": ["carotid blowout", "sentinel bleed", "irradiated neck", "emergency"]
        },
        {
            "topic": "Nonfunctional Larynx and Intractable Aspiration",
            "recognize": "A disease-free patient after organ-preservation therapy who has recurrent aspiration pneumonia, feeding-tube dependence, airway compromise or profound dysphagia may have a nonfunctional larynx despite retaining the organ anatomically.",
            "localize": "Late radiation fibrosis, impaired sensation, poor pharyngeal propulsion, reduced laryngeal elevation/closure and chondroradionecrosis can create chronic aspiration that is not equivalent to tumor recurrence.",
            "workup": "Exclude recurrent malignancy, define swallowing physiology with instrumental assessment, evaluate pulmonary consequences and nutritional status, and establish whether aspiration is potentially rehabilitatable.",
            "manage": "Maximize swallowing therapy and reversible contributors first. For severe, persistent life-threatening aspiration despite rehabilitation, aspiration-prevention surgery including functional/total laryngectomy may be appropriate after detailed counseling.",
            "operate": "In irradiated tissue, anticipate pharyngocutaneous fistula and wound-healing risk and consider vascularized reinforcement. The operative goal is separation of airway and alimentary tract, not cancer clearance when the patient is disease-free.",
            "teach": "Organ preservation and function preservation are not the same outcome. A larynx can be present yet fail its airway-protection role so severely that laryngectomy becomes a functional operation.",
            "tags": ["aspiration", "late radiation toxicity", "functional laryngectomy", "dysphagia"]
        },
        {
            "topic": "Free Flap Monitoring and Salvage",
            "recognize": "A newly reconstructed free flap that becomes congested, pale, cool, loses Doppler signal, develops brisk dark bleeding or fails to bleed appropriately on pinprick should raise immediate concern for vascular compromise.",
            "localize": "Venous thrombosis commonly causes congestion and dark rapid bleeding; arterial compromise causes pallor, coolness and delayed or absent bright-red bleeding. External compression, kinking or hematoma can compromise either side.",
            "workup": "Perform immediate bedside examination and compare with the documented baseline, check implantable/external Doppler if used, inspect the neck for hematoma or pedicle compression, and do not let confirmatory tests delay OR return when the flap is clinically failing.",
            "manage": "Flap compromise is a time-sensitive surgical emergency. Correct reversible external causes immediately and return to the OR urgently for exploration when vascular compromise is suspected.",
            "operate": "At takeback, release compression, inspect the pedicle and anastomoses, thrombectomize/revise as needed, irrigate appropriately and re-establish inflow/outflow. Salvage probability falls as ischemia time increases.",
            "teach": "The best flap monitor is a team that knows the baseline and acts on change. A questionable flap at 2 AM is not a 'recheck in the morning' problem.",
            "tags": ["microvascular", "flap salvage", "venous thrombosis", "postoperative emergency"]
        },
        {
            "topic": "Neck Dissection Complications",
            "recognize": "New shoulder dysfunction, lower-lip asymmetry, tongue weakness, diaphragmatic dysfunction, chylous drainage, Horner syndrome or major sensory deficit after neck dissection should be localized to the specific injured structure rather than labeled generically as postoperative weakness.",
            "localize": "Key structures at risk include CN XI, marginal mandibular nerve, hypoglossal nerve, vagus/RLN, phrenic nerve, sympathetic chain, brachial plexus, thoracic duct and major vessels; the dissection level predicts the likely injury.",
            "workup": "Use focused cranial nerve and shoulder examination, flexible laryngoscopy when vagal/RLN injury is possible, chest imaging for suspected phrenic injury, and drain triglycerides/chylomicrons when chyle leak is suspected.",
            "manage": "Management depends on the structure and severity: early shoulder rehabilitation after CN XI dysfunction, nutritional/pressure strategies for low-output chyle leak, escalation for high-output leak, and targeted voice/swallow or airway intervention for vagal/RLN injury.",
            "operate": "If a nerve is transected and recognized intraoperatively, repair or graft when appropriate; uncontrolled high-output chyle leak or major vascular injury may require prompt re-exploration.",
            "teach": "A neck-dissection complication question is usually an anatomy question in disguise: identify the level, identify the structure, then choose the complication-specific response.",
            "tags": ["neck dissection", "CN XI", "chyle leak", "cranial nerves"]
        },
        {
            "topic": "Palliative Decision-Making in Head and Neck Cancer",
            "recognize": "Advanced recurrent or metastatic head and neck cancer may produce airway obstruction, bleeding, pain, dysphagia, aspiration and fungating wounds even when curative treatment is no longer realistic.",
            "localize": "Symptoms are driven by the specific threatened function or structure - airway, carotid, pharynx/esophagus, cranial nerves, mandible or skin - and should be treated according to the patient's goals and expected trajectory.",
            "workup": "Clarify prognosis, disease extent, performance status, prior treatments and what the patient values most. Distinguish interventions that meaningfully improve comfort or function from burdensome procedures unlikely to achieve those goals.",
            "manage": "Integrate palliative care early; use symptom-directed radiation, systemic therapy, analgesia, secretion control, nutritional planning and airway/bleeding strategies when they match the patient's goals.",
            "operate": "Tracheostomy, gastrostomy, debulking or hemostatic procedures can be appropriate for palliation, but an operation should have a clear symptom target and realistic benefit rather than being performed simply because a technical procedure exists.",
            "teach": "Palliative care is active head-and-neck care. The chief-level skill is matching each intervention to a symptom, a realistic benefit and the patient's priorities.",
            "tags": ["palliative care", "recurrent cancer", "airway", "bleeding"]
        },
    ],
}
