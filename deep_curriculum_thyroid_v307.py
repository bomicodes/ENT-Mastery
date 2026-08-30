"""v30.7 — source-grounded differentiated thyroid cancer pathway separation.

The duplicate audit flags Differentiated Thyroid Cancer against both Active Surveillance
and Radioiodine-Refractory DTC. This rebuild gives the parent card the full initial-risk
and longitudinal framework while reserving the child cards for two opposite clinical
branches: deliberate de-escalation in carefully selected low-risk disease, and escalation
for structurally progressive disease that no longer benefits from additional RAI.
"""

import re

DOMAIN = "Thyroid / Parathyroid / Salivary"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


DTC_V307 = {
    "differentiated thyroid cancer": {
        "recognize": (
            "Recognize DIFFERENTIATED THYROID CANCER (DTC) as the parent pathway encompassing papillary, follicular, and oncocytic-lineage carcinomas. Start by separating initial disease extent from biologic recurrence risk: tumor size, gross extrathyroidal extension, clinically apparent nodal/distant metastasis, aggressive histology, vascular invasion, and molecular features do not all answer the same question. The 2025 ATA framework emphasizes individualized treatment rather than automatic total thyroidectomy plus radioactive iodine for every DTC."
        ),
        "localize": (
            "Map the thyroid primary and neck with high-quality ultrasound, documenting laterality, multifocality, relationship to trachea/esophagus/recurrent-laryngeal-nerve corridor, suspicious central/lateral nodes, and contralateral thyroid disease. Use cross-sectional imaging when invasive disease, bulky nodal disease, substernal extension, or anatomy beyond ultrasound is suspected. Follicular-pattern malignancy requires attention to capsular/vascular invasion and distant hematogenous spread; papillary carcinoma more often follows lymphatic cervical pathways."
        ),
        "workup": (
            "Confirm cytology/histology and obtain the preoperative information that can change extent of therapy. Evaluate vocal-fold function when voice is abnormal, prior neck surgery exists, or invasive/posterior disease threatens the recurrent laryngeal nerve. Do not treat serum thyroglobulin as a primary diagnostic test for an intact thyroid nodule. After treatment, interpret thyroglobulin together with anti-thyroglobulin antibodies, the amount of thyroid tissue remaining, imaging, and the patient's response-to-therapy category. Molecular testing is selectively useful when it changes diagnosis, prognosis, surgical planning, or later targeted-therapy decisions."
        ),
        "manage": (
            "Use the 2025 ATA direction toward de-escalation when oncologically appropriate. For intrathyroidal, node-negative unilateral cancer <=2 cm, lobectomy is generally the preferred initial operation; for >2 to <=4 cm disease confined to one lobe without nodal disease or gross extension, lobectomy or total thyroidectomy can be appropriate based on tumor factors, contralateral disease, anticipated RAI/follow-up needs, and patient preference. Total thyroidectomy remains appropriate when bilateral disease, gross extrathyroidal extension, clinically meaningful nodal/distant disease, or another treatment/follow-up reason warrants it. RAI is risk-adapted, not automatic. Longitudinal management then follows structural/biochemical response rather than repeating the initial risk label forever."
        ),
        "operate": (
            "Match the operation to the disease actually present. Preserve the recurrent laryngeal nerves and viable parathyroid tissue, avoid prophylactic sacrifice of uninvolved structures, and perform therapeutic compartment-oriented neck dissection for clinically involved nodes rather than berry-picking. Do not add completion thyroidectomy reflexively after an initial lobectomy: the 2025 ATA update shifts completion surgery toward a selective decision when persistent disease, RAI planning, or surveillance strategy provides a concrete benefit."
        ),
        "teach": (
            "Chief/boards framework: DTC PARENT CARD = EXTENT -> RISK -> INITIAL THERAPY -> RESPONSE-TO-THERAPY. Do not collapse three separate decisions into 'thyroid cancer = total thyroidectomy + RAI.' Small low-risk disease may qualify for active surveillance or lobectomy; intermediate/high-risk disease may need broader surgery and selective RAI; later structural progression may require local therapy or systemic therapy. Active Surveillance and RAIR-DTC are therefore opposite branches of this parent framework, not duplicate summaries."
        ),
        "tags": ["differentiated thyroid cancer", "papillary thyroid carcinoma", "follicular thyroid carcinoma", "lobectomy", "total thyroidectomy", "radioactive iodine", "response to therapy", "thyroglobulin"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — differentiated thyroid carcinoma, thyroidectomy, nodal disease, adjuvant therapy, and surveillance",
            "K.J. Lee's Essential Otolaryngology, 12e — papillary/follicular thyroid carcinoma staging and management",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — thyroid carcinoma evaluation, surgery, RAI, and follow-up",
            "American Thyroid Association 2025 Management Guidelines for Adult Patients with Differentiated Thyroid Cancer (Thyroid 2025;35:841-985) — individualized extent of surgery, active surveillance, risk-adapted RAI, response assessment, and systemic therapy",
        ],
    },
    "differentiated thyroid cancer active surveillance": {
        "recognize": (
            "Recognize ACTIVE SURVEILLANCE (AS) as a deliberate management strategy for carefully selected LOW-RISK papillary thyroid carcinoma, not as passive neglect and not as a substitute for staging. The classic high-confidence candidate is a small intrathyroidal PTC without clinically apparent nodal/distant metastasis, gross extrathyroidal extension, aggressive histology, or invasion risk to the trachea/recurrent laryngeal nerve. Patient age, comorbidity, competing mortality, anxiety, preference, and ability to return for expert ultrasound follow-up all modify whether AS is sensible."
        ),
        "localize": (
            "Eligibility depends heavily on ultrasound geography. Define whether the tumor is truly intrathyroidal and whether its position makes future progression dangerous: posterior-medial tumors abutting the tracheoesophageal groove or recurrent-laryngeal-nerve course, lesions with suspected gross extrathyroidal extension, and tumors associated with suspicious nodes are poor AS candidates. Survey the central and lateral neck before labeling disease 'low risk.' A technically small lesion is not automatically a safe surveillance lesion."
        ),
        "workup": (
            "Establish a reproducible baseline with expert high-resolution neck ultrasound and pathology/cytology sufficient to support the low-risk diagnosis. Document maximal dimensions and tumor-node relationships so future change can be measured against the same landmarks. Routine serial CT, PET/CT, RAI scanning, or thyroglobulin-driven escalation is not the backbone of AS in an intact thyroid; ultrasound and clinical assessment are. Follow-up interval should be protocolized, commonly closer early and then spaced if stable, with thyroid function testing as clinically appropriate."
        ),
        "manage": (
            "Counsel AS and surgery as two active options with different burdens. Continue surveillance while the lesion remains stable and there is no new nodal disease, gross extrathyroidal extension, or other adverse change. Conversion to surgery is appropriate for meaningful reproducible growth, new nodal/distant metastasis, development of invasion risk, patient preference, inability to maintain reliable follow-up, or other clinical progression. Do not declare failure based on a trivial single-axis measurement difference within ultrasound variability. The core skill is recognizing when delayed surgery remains oncologically safe and when the risk profile has changed."
        ),
        "operate": (
            "If surveillance converts to surgery, perform the operation appropriate to CURRENT disease rather than treating prior observation as an indication for maximal surgery. A still-localized unilateral low-risk lesion may remain a lobectomy problem; new nodal disease or invasive features change the operation accordingly. Delayed surgery after properly selected AS is not inherently a rescue procedure. Preserve RLN/parathyroid function and avoid prophylactic central dissection unless there is a disease-specific indication."
        ),
        "teach": (
            "Chief/boards discriminator: ACTIVE SURVEILLANCE = SMALL/LOW-RISK PTC + SAFE LOCATION + NO CLINICAL NODES/METS + RELIABLE ULTRASOUND FOLLOW-UP + SHARED DECISION-MAKING. 'Less than 1 cm' alone is not enough. Exclude gross ETE, tracheal/RLN invasion risk, aggressive biology, and nodal disease. Progression means reproducible structural change or new disease, not anxiety about the word carcinoma and not microscopic measurement noise."
        ),
        "tags": ["active surveillance", "papillary thyroid microcarcinoma", "low-risk PTC", "thyroid ultrasound", "shared decision-making", "tumor growth", "nodal metastasis", "delayed surgery"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — low-risk papillary thyroid carcinoma and risk-adapted surgical management",
            "K.J. Lee's Essential Otolaryngology, 12e — papillary thyroid microcarcinoma and treatment selection",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — thyroid carcinoma risk stratification and surgical decision-making",
            "American Thyroid Association 2025 Management Guidelines for Adult Patients with Differentiated Thyroid Cancer — expanded role of active surveillance and shared decision-making",
            "2025 Korean Thyroid Association Clinical Management Guideline on Active Surveillance for Low-Risk Papillary Thyroid Carcinoma — ultrasound eligibility, exclusion criteria, and longitudinal monitoring",
        ],
    },
    "radioiodine refractory differentiated thyroid cancer": {
        "recognize": (
            "Recognize RADIOIODINE-REFRACTORY DTC (RAIR-DTC) as an ADVANCED-DISEASE state in which additional empiric RAI is unlikely to provide meaningful tumor control. The practical patterns include structurally evident disease that does not concentrate iodine, loss of uptake after prior iodine-avid disease, discordant lesions with some non-avid/progressive sites, or structural progression despite appropriately administered RAI. Do not equate an elevated thyroglobulin alone with RAIR disease, and do not keep repeating RAI simply because metastatic DTC exists."
        ),
        "localize": (
            "Define which lesions are threatening the patient and whether progression is focal/oligoprogressive or broadly systemic. Map airway/esophageal invasion, cervical nodes, lung/bone/brain metastases, pain-producing lesions, and sites at risk for fracture, neurologic compromise, hemorrhage, or fistula. Compare serial cross-sectional imaging using a consistent structural framework; FDG-PET can help characterize biologically aggressive non-iodine-avid disease in selected patients. The location and pace of disease determine whether local therapy can postpone systemic treatment."
        ),
        "workup": (
            "Before systemic therapy, confirm true structural progression and review prior RAI dose, uptake pattern, treatment response, TSH status, pathology, and current imaging. Obtain comprehensive tumor molecular profiling when systemic therapy is being considered: the 2025 ATA guideline moves molecular drivers into first-line treatment selection. Assess blood pressure, renal/hepatic function, nutrition, performance status, bleeding/fistula risk, and drug interactions before multikinase therapy. A stable asymptomatic patient with low-volume RAIR disease may be observed rather than treated immediately."
        ),
        "manage": (
            "Prioritize local control when a limited number of lesions are driving morbidity or progression: surgery, external-beam radiation, thermal/ablative therapy, or other site-directed treatment can control threatening disease and delay chronic systemic toxicity. Start systemic therapy for clinically meaningful progressive, symptomatic, threatening, or disseminated disease not adequately controlled locally. If an actionable driver is present, the 2025 ATA framework favors matched selective targeted therapy when appropriate; without a targetable alteration, lenvatinib is generally preferred over sorafenib as first-line multikinase therapy, with later-line choices such as cabozantinib depending on prior therapy and context. Manage toxicity proactively because treatment is often chronic."
        ),
        "operate": (
            "Surgery in RAIR-DTC is usually LOCAL-CONTROL surgery, not a promise of systemic cure. Resect a threatening cervical recurrence or isolated metastatic focus when morbidity is acceptable and control would protect airway, swallowing, neural structures, bone stability, or defer systemic therapy. Do not perform morbid surgery for diffuse indolent disease simply to reduce thyroglobulin. In previously operated/radiated necks, reoperative RLN/parathyroid/vascular risk and the likelihood of meaningful durable control must be explicit before incision."
        ),
        "teach": (
            "Chief/boards discriminator: RAIR-DTC = STOP ASKING 'MORE RAI?' AND ASK 'WHAT IS PROGRESSING, WHAT THREATENS THE PATIENT, CAN I CONTROL IT LOCALLY, AND WHAT DRIVER DOES THE TUMOR HAVE?' Stable asymptomatic RAIR disease can be watched. Focal threatening disease may deserve surgery/EBRT/ablation before a TKI. Progressive systemic disease should undergo molecular profiling before first-line therapy selection; lenvatinib is the usual multikinase default when no better matched target exists."
        ),
        "tags": ["RAIR differentiated thyroid cancer", "radioiodine refractory", "lenvatinib", "sorafenib", "cabozantinib", "molecular testing", "targeted therapy", "local therapy"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — recurrent/metastatic differentiated thyroid cancer, RAI, reoperative surgery, and local control",
            "K.J. Lee's Essential Otolaryngology, 12e — advanced thyroid carcinoma and recurrent disease",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — recurrent/metastatic thyroid carcinoma and treatment principles",
            "American Thyroid Association 2025 Management Guidelines for Adult Patients with Differentiated Thyroid Cancer — RAIR disease, molecular profiling, local therapy, and systemic-therapy sequencing",
            "ATA Clinical Thyroidology for the Public 2026 summaries of the 2025 guideline — local versus systemic therapy and molecularly directed first-line systemic treatment",
        ],
    },
}


ALIASES = {
    "differentiated thyroid cancer active surveillance": "differentiated thyroid cancer active surveillance",
    "differentiated thyroid cancer active surveillance for low risk disease": "differentiated thyroid cancer active surveillance",
    "radioiodine refractory differentiated thyroid cancer": "radioiodine refractory differentiated thyroid cancer",
    "radioiodine refractory dtc": "radioiodine refractory differentiated thyroid cancer",
}


def apply_thyroid_dtc_rebuild_v307(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        key = ALIASES.get(key, key)
        payload = DTC_V307.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v307"] = True
        if key == "differentiated thyroid cancer":
            role = "dtc_parent_extent_risk_initial_therapy_response"
        elif key == "differentiated thyroid cancer active surveillance":
            role = "low_risk_deescalation_surveillance_conversion_pathway"
        else:
            role = "rair_progression_local_control_molecular_systemic_pathway"
        module["semantic_role_v307"] = role
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
