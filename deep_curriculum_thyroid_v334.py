"""v33.4 — source-grounded differentiated-thyroid-cancer role separation.

The umbrella DTC card owns diagnosis, initial risk-adapted treatment, response assessment,
and survivorship. The active-surveillance card is restricted to selected untreated low-risk
intrathyroidal PTC. The RAIR card owns persistent/metastatic disease that has lost meaningful
radioiodine responsiveness and teaches local-versus-systemic escalation plus molecular selection.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


DTC_REBUILD_V334 = {
    "differentiated thyroid cancer": {
        "recognize": (
            "Use this as the UMBRELLA DTC card: papillary, follicular and oncocytic differentiated cancers require a risk-adapted journey from diagnosis through response assessment, not one fixed operation followed by one fixed surveillance schedule. Establish histology/cytology, high-resolution thyroid-and-neck ultrasound, vocal-fold function when clinically indicated, and whether there is gross extrathyroidal, nodal, aerodigestive, or distant disease. Separate AJCC mortality staging from recurrence-risk assessment; they answer different questions."
        ),
        "localize": (
            "Map disease in compartments that change treatment: intrathyroidal primary, central neck, lateral neck, invasive laryngotracheal/esophageal disease, and distant sites. Papillary carcinoma commonly spreads lymphatically; follicular/oncocytic tumors more often raise hematogenous-risk questions. Do not use serum thyroglobulin to decide whether an intact thyroid nodule is malignant; after treatment it becomes a response/surveillance marker whose meaning depends on residual thyroid tissue, TSH, anti-thyroglobulin antibodies, prior RAI, and trend."
        ),
        "workup": (
            "Build a DATA-style decision: Diagnosis -> risk/benefit Assessment -> Treatment decision -> response Assessment. Before initial surgery define tumor size, multifocal/bilateral disease, gross ETE, suspicious nodes, distant disease, contralateral nodules, voice/RLN status when relevant, comorbidity and patient priorities. After treatment, interpret neck US plus Tg/TgAb and other imaging according to the operation and RAI received, then dynamically re-stratify as excellent/complete-remission, biochemical, indeterminate, or structural disease rather than letting the original pathology risk permanently dictate intensity."
        ),
        "manage": (
            "Current management is deliberately de-escalated for appropriate low-risk disease. Lobectomy is sufficient/preferred for many unilateral low-risk cancers and routine RAI is not indicated for low-risk DTC simply because total thyroidectomy was performed. Select RAI by recurrence risk, expected iodine avidity, residual/metastatic burden and whether treatment is remnant ablation, adjuvant therapy, or therapy of known disease. TSH targets should evolve with current disease status and treatment toxicity rather than reflexively maintaining lifelong profound suppression in a disease-free low-risk patient."
        ),
        "operate": (
            "The surgeon's job is oncologic clearance with the least unnecessary morbidity. Therapeutically dissect clinically involved nodal compartments; do not convert a cN0 low-risk thyroidectomy into routine prophylactic lateral neck dissection. For gross local invasion, decide whether shaving versus segmental aerodigestive resection can achieve appropriate control while accounting for RLN function, airway, swallowing, reconstructive burden and adjuvant options. The separate Active Surveillance card owns selected untreated microcarcinoma; the RAIR card owns advanced disease after loss of meaningful iodine responsiveness."
        ),
        "teach": (
            "Boards/chief frame: STAGE predicts death risk; RECURRENCE RISK predicts structural recurrence; RESPONSE TO THERAPY changes what you do next. Thyroglobulin is a POST-TREATMENT trend, not an initial cancer test. Surgery, RAI, TSH suppression and imaging intensity are each separately risk-adapted. Never collapse 'DTC' into 'total thyroidectomy + RAI + suppress everyone forever.'"
        ),
        "tags": ["differentiated thyroid cancer", "papillary thyroid cancer", "follicular thyroid cancer", "oncocytic carcinoma", "dynamic risk stratification", "thyroglobulin", "radioactive iodine", "thyroid lobectomy"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — differentiated thyroid carcinoma diagnosis, surgical anatomy, invasive disease, nodal disease, RAI and surveillance framework",
            "K.J. Lee's Essential Otolaryngology, 12e — WDTC surgery, risk-based I-131, thyroglobulin, cervical ultrasound and PET/CT surveillance framework",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — papillary/follicular carcinoma staging, active-surveillance option for microcarcinoma, extent of surgery, nodal management and postoperative RAI framework",
            "Ringel et al. 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer. Thyroid. 2025;35(8):841-985 — current DATA framework, surgery, RAI, response assessment and survivorship",
        ],
    },
    "differentiated thyroid cancer active surveillance": {
        "recognize": (
            "ACTIVE SURVEILLANCE here means deliberate observation of a KNOWN, UNTREATED, PRIMARY low-risk intrathyroidal PTC instead of immediate surgery. The 2025 ATA definition deliberately separates this from monitoring persistent/recurrent disease after treatment. A classic candidate is cT1aN0M0 PTC with no gross extrathyroidal extension, suspicious nodes, distant metastasis, aggressive clinical behavior, or threatened tracheal/RLN anatomy, and a patient able and willing to maintain high-quality longitudinal follow-up."
        ),
        "localize": (
            "Location matters as much as diameter. On expert ultrasound determine whether the lesion is truly intrathyroidal and whether its relationship to the trachea, posteromedial capsule/RLN course, thyroid edge and suspicious cervical nodes makes delayed growth potentially consequential. Confirm that there is no clinical nodal or distant disease. This is not 'ignore a small cancer'; it is selecting a tumor whose anatomy leaves a safe window for delayed intervention."
        ),
        "workup": (
            "Before choosing surveillance, document baseline expert neck ultrasound, tumor dimensions/location, node status, cytologic/pathologic confidence, patient age/comorbidity, anxiety/preferences and follow-up reliability. Discuss the competing paths—surveillance, surgery, and in selected centers percutaneous ablation—using shared decision-making. Follow with serial ultrasound; use Tg/TgAb only in the context recommended by the treating thyroid team and never let a single nonspecific laboratory value replace structural assessment in a patient with an intact thyroid."
        ),
        "manage": (
            "Surveillance succeeds only if EXIT CRITERIA are defined at entry. Move toward surgery for convincing structural progression, new nodal disease, development of an anatomic threat, other new adverse features, inability to maintain reliable surveillance, or patient preference. Minor measurement variation is not progression; compare reproducible dimensions and trend. Conversely, young age alone is not an automatic operation, but younger patients may have a longer lifetime during which growth can occur and deserve explicit counseling."
        ),
        "operate": (
            "Delayed surgery after appropriate surveillance is not a treatment failure—it is the planned rescue pathway when the disease crosses a predefined threshold or the patient's preference changes. When intervention is triggered, choose extent of surgery from CURRENT anatomy/risk rather than automatically escalating because surveillance was attempted. Do not confuse this card with observation of small postoperative nodal disease or metastatic RAIR DTC; those are disease-monitoring/local-control decisions after treatment and belong elsewhere."
        ),
        "teach": (
            "High-yield distinction: ACTIVE SURVEILLANCE = selected cT1aN0M0 primary PTC before surgery. MONITORING = persistent/recurrent disease after treatment. A safe AS program requires favorable biology + favorable anatomy + reliable patient/system + predefined triggers to intervene. The point is to avoid immediate treatment morbidity without surrendering the opportunity for cure."
        ),
        "tags": ["thyroid active surveillance", "papillary microcarcinoma", "cT1aN0M0", "serial ultrasound", "shared decision making", "low risk PTC", "delayed thyroid surgery"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — low-risk papillary thyroid cancer and risk-adapted surgical framework; current ATA guidance supersedes older thresholds where different",
            "Pasha 6e — active surveillance or lobectomy for selected <1-cm PTC without ETE, nodal or distant disease; based on 2015 ATA and updated here to 2025 ATA terminology",
            "Ringel et al. 2025 ATA DTC Guidelines, Recommendation 11 — active surveillance may be offered for selected cT1aN0M0 PTC with shared decision-making; guideline explicitly distinguishes active surveillance from post-treatment disease monitoring",
            "2025 Korean Thyroid Association Clinical Management Guideline on Active Surveillance for Low-Risk Papillary Thyroid Carcinoma — expert-US anatomic selection, exclusion of nodal/distant/gross invasive disease, and longitudinal shared decision-making",
        ],
    },
    "radioiodine refractory differentiated thyroid cancer": {
        "recognize": (
            "RAI-REFRACTORY DTC is not synonymous with 'any recurrence after I-131' and does not automatically mean 'start a TKI.' Establish that structural disease has lost clinically meaningful iodine responsiveness—for example disease that does not concentrate RAI, loses uptake, progresses despite appropriate RAI, or has mixed/nonresponsive clinically important lesions—and stop repeating empiric RAI when expected benefit is negligible and cumulative toxicity rises."
        ),
        "localize": (
            "Map the tempo and THREAT, not merely the number of metastases. Distinguish indolent asymptomatic lesions from focal disease threatening airway, esophagus, spinal cord, brain, major vessels or weight-bearing bone, and from diffuse objectively progressive disease. FDG-PET/CT can be useful in the classic Tg-positive/iodine-scan-negative setting and for biologically dedifferentiated disease. A single enlarging lesion in otherwise stable metastatic disease may be a LOCAL-THERAPY problem rather than a reason to expose the whole patient to indefinite systemic therapy."
        ),
        "workup": (
            "Before systemic therapy, confirm structural progression and its pace on comparable imaging, symptoms, performance status, prior RAI dose/uptake history and whether surgery, external-beam/stereotactic radiation, ablation or another focal treatment can control the threatening site. Obtain comprehensive tumor molecular profiling BEFORE choosing first-line systemic treatment because actionable RET or NTRK fusions and other targetable alterations can move a selective inhibitor ahead of a nonspecific multikinase inhibitor in the 2025 ATA framework."
        ),
        "manage": (
            "Do not treat radiographic existence alone. Stable/asymptomatic RAIR disease can often be monitored; oligoprogressive or symptomatic focal disease may be controlled with surgery, directed radiation or image-guided ablation to defer systemic toxicity. Start systemic therapy when disease is clinically meaningful, progressive/symptomatic or threatening and not adequately controllable locally. When no preferred actionable target exists, lenvatinib is generally favored over sorafenib as first-line multikinase therapy; choose/sequence agents with endocrinology/medical oncology around comorbidity, prior therapy, mutation profile and toxicity."
        ),
        "operate": (
            "The H&N surgeon remains relevant after RAIR designation. Resect accessible locoregional disease when it offers durable control or prevents airway/esophageal/vascular catastrophe, and integrate focal surgery with radiation/ablation rather than treating systemic therapy as the only remaining modality. Before invasive rescue, define whether the goal is cure, durable local control, prevention of a specific complication, or palliation. Redifferentiation strategies that may restore iodine uptake are specialist/molecular-tumor-board decisions—not a reason to give serial empiric RAI blindly."
        ),
        "teach": (
            "Chief framework: RAIR is a BIOLOGY/RESPONSE state, not simply metastatic DTC. Ask four questions in order: Is the disease truly iodine-nonresponsive? Is it actually progressing or threatening? Can the important site be controlled LOCALLY? What molecular target should determine systemic therapy if systemic treatment is now justified? The 2025 shift is LOCAL THERAPY FIRST when feasible + MOLECULAR PROFILING BEFORE first-line systemic therapy."
        ),
        "tags": ["RAI refractory DTC", "radioiodine refractory", "thyroid cancer systemic therapy", "lenvatinib", "sorafenib", "RET fusion", "NTRK fusion", "molecular profiling", "local therapy", "oligoprogression"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — recurrent/invasive DTC, aerodigestive disease, locoregional salvage and multidisciplinary advanced-thyroid-cancer framework",
            "K.J. Lee's Essential Otolaryngology, 12e — risk-based I-131, Tg/US surveillance and PET/CT in iodine-scan-negative Tg-positive WDTC; systemic-therapy details updated to current guidance",
            "Pasha 6e — postoperative RAI risk selection and differentiated-thyroid-cancer follow-up; advanced systemic treatment updated to 2025 ATA guidance",
            "Ringel et al. 2025 ATA DTC Guidelines — current RAIR definitions/management, local therapy before systemic treatment where appropriate, comprehensive molecular profiling, and genotype-directed systemic therapy",
            "ATA Clinical Thyroidology for the Public, July 2026 — 2025 ATA local-versus-systemic treatment summary for RAIR DTC",
        ],
    },
}


def apply_dtc_role_separation_v334(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = DTC_REBUILD_V334.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v334"] = True
            module["semantic_role_v334"] = {
                "differentiated thyroid cancer": "umbrella initial DTC diagnosis, risk-adapted treatment, dynamic response assessment, and survivorship",
                "differentiated thyroid cancer active surveillance": "selected untreated cT1aN0M0 primary PTC surveillance with predefined intervention triggers",
                "radioiodine refractory differentiated thyroid cancer": "post-treatment iodine-nonresponsive advanced DTC: tempo/threat assessment, local control, molecular profiling, and systemic escalation",
            }[key]
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
