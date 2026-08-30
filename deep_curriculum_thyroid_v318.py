"""v31.8 — source-grounded DTC vs active-surveillance Concept Hub separation.

The broad differentiated-thyroid-cancer card owns staging, risk-adapted initial treatment,
and response-directed follow-up. The active-surveillance card owns selection of a low-risk
papillary cancer for observation, ultrasound technique, longitudinal monitoring, and
conversion-to-intervention triggers. Keeping those jobs separate prevents surveillance
from becoming a shallow duplicate of the general thyroid-cancer pathway.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


DTC_SURVEILLANCE_REBUILD_V318 = {
    "differentiated thyroid cancer": {
        "recognize": (
            "Use this card for the OVERALL DTC MANAGEMENT PATHWAY after papillary, follicular, or oncocytic differentiated thyroid carcinoma is diagnosed—not for the mechanics of observing an intentionally untreated microcarcinoma. Separate an intrathyroidal low-risk tumor from gross extrathyroidal extension, clinically involved nodes, distant disease, aggressive histology, extensive vascular invasion, and oncocytic/follicular patterns with different metastatic behavior. The 2025 ATA framework emphasizes individualized diagnosis, risk/benefit assessment, treatment selection, and reassessment rather than a single 'total thyroidectomy + RAI' recipe."
        ),
        "localize": (
            "Map disease before choosing treatment: high-resolution thyroid/central/lateral-neck ultrasound defines multifocality, capsular relationships, and suspicious nodes; contrast CT/MRI is appropriate when invasive primary disease, bulky nodal disease, mediastinal extension, or aerodigestive involvement is suspected. PTC commonly spreads through cervical lymphatics, whereas follicular and oncocytic carcinomas more often declare risk through vascular invasion and hematogenous metastasis. Distinguish microscopic pathology risk from gross invasion of the RLN, trachea, esophagus, carotid, or prevertebral space because gross invasion changes both resectability and operative planning."
        ),
        "workup": (
            "Integrate cytology/pathology, ultrasound, vocal-fold function when voice symptoms or invasive/reoperative disease raise RLN concern, and selective cross-sectional/distant staging. After resection, use the final histology—not tumor diameter alone—to define recurrence risk: subtype, vascular invasion, margins, extrathyroidal extension, number/size of nodal metastases, extranodal extension, distant metastases, and molecular findings when they affect therapy. The 2025 ATA model uses four recurrence-risk bands (low <10%, low-intermediate 10-15%, intermediate-high 16-30%, high >30%) and then modifies management again according to response to therapy; TNM mortality stage and ATA recurrence risk answer different questions."
        ),
        "manage": (
            "Choose treatment proportionate to disease. For a unilateral cancer <=2 cm confined to the thyroid with no clinical nodal disease, the 2025 ATA guidance favors lobectomy when surgery is selected; for >2 to <=4 cm intrathyroidal cN0 disease, lobectomy or total thyroidectomy can be appropriate depending on tumor features, contralateral disease, downstream RAI/follow-up needs, and patient preference. Total thyroidectomy and compartment-oriented nodal surgery are reserved for appropriate bilateral, invasive, nodal, metastatic, or adjuvant-treatment contexts rather than performed automatically. RAI is risk- and goal-directed, not routine for every DTC. Follow-up is dynamic: thyroglobulin/anti-Tg interpretation depends on the operation and RAI history, cervical ultrasound is risk-adapted, and TSH targets should be reassessed as treatment response becomes clear. Persistent disease that no longer benefits from RAI belongs in the companion radioiodine-refractory card."
        ),
        "operate": (
            "OPERATIVE PRINCIPLE: match the extent of thyroid and nodal surgery to preoperative disease while minimizing avoidable RLN and parathyroid morbidity. Lobectomy can be definitive treatment for properly selected low-risk unilateral DTC; completion thyroidectomy is no longer an automatic consequence of every postoperative cancer diagnosis and may instead be considered for persistent cancer, planned RAI, or follow-up needs. Perform therapeutic central/lateral compartment dissection for clinically involved nodal disease rather than node-picking. Gross aerodigestive or neural invasion requires an oncologic resection plan that balances R0/R1 feasibility, function, adjuvant options, and patient goals."
        ),
        "teach": (
            "Chief/boards discriminator: GENERAL DTC = WHAT IS THE EXTENT/RISK OF THIS CANCER, HOW MUCH INITIAL THYROID/NODAL TREATMENT IS JUSTIFIED, AND HOW DOES RESPONSE CHANGE FOLLOW-UP? Do not turn every small PTC into total thyroidectomy + RAI. Do not turn this card into an active-surveillance protocol either: eligibility, serial ultrasound, and delayed-surgery triggers belong in 'Differentiated Thyroid Cancer: Active Surveillance.'"
        ),
        "tags": ["differentiated thyroid cancer", "papillary thyroid carcinoma", "follicular thyroid carcinoma", "oncocytic thyroid carcinoma", "ATA 2025", "lobectomy", "thyroidectomy", "radioactive iodine", "dynamic risk stratification"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — differentiated thyroid carcinoma evaluation, thyroidectomy, nodal disease, and recurrent disease",
            "K.J. Lee's Essential Otolaryngology, 12e — thyroid malignancy staging, surgery, and complications",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — thyroid cancer workup and operative management",
            "Ringel et al. 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer. Thyroid. 2025;35:841-985 — current risk-adapted initial treatment, response assessment, surveillance, and systemic-therapy framework",
        ],
    },
    "differentiated thyroid cancer active surveillance": {
        "recognize": (
            "Use this card only when the clinical question is WHETHER A SMALL LOW-RISK PAPILLARY THYROID CANCER CAN SAFELY REMAIN IN SITU. Active surveillance is an intentional treatment strategy, not 'doing nothing' and not routine postoperative follow-up. The strongest evidence is for adult low-risk papillary thyroid microcarcinoma, classically T1aN0M0, without gross extrathyroidal extension, clinically apparent nodal/distant metastasis, aggressive histology, or a location where modest growth could threaten the recurrent laryngeal nerve or trachea. Patient preference, anxiety, age/comorbidity, reliable follow-up, and access to expert ultrasound are part of candidacy."
        ),
        "localize": (
            "Eligibility is anatomy-sensitive. On baseline expert ultrasound, record three orthogonal tumor dimensions and its relationship to the thyroid capsule, trachea, and expected RLN course; survey central and lateral nodal basins rather than measuring the primary alone. A posterior/posteromedial lesion abutting the tracheoesophageal groove or a lesion with convincing gross extrathyroidal extension deserves more caution than an equally small intraparenchymal tumor. Suspicious lymph nodes should be evaluated because newly proven nodal metastasis changes the surveillance pathway."
        ),
        "workup": (
            "Confirm that this is truly low-risk disease before observation. Review cytology/pathology for papillary carcinoma and features suggesting aggressive subtype; perform high-quality neck ultrasound to exclude gross ETE and nodal metastasis, and use cross-sectional imaging selectively when anatomy is uncertain. Establish a reproducible baseline size so apparent millimeter-level change is not mistaken for biologic progression. Contemporary structured guidance commonly uses ultrasound and thyroid-function assessment every 6 months for the first 2 years and annually thereafter if stable; local protocols can vary, but surveillance must be longitudinal and dependable."
        ),
        "manage": (
            "Shared decision-making must compare two valid strategies—surveillance versus surgery—using oncologic safety, operative risks, quality of life, anxiety, cost, life expectancy, pregnancy plans when relevant, and the patient's willingness to return for serial imaging. During surveillance, follow both primary-tumor dimensions and nodal basins. A reproducible increase of about 3 mm in maximal diameter is a commonly used structural-progression threshold; newly detected/proven nodal or distant metastasis, development of gross invasion/threat to critical structures, or patient preference should prompt conversion to treatment. Small measurement fluctuation alone is not failure. Delayed surgery after appropriately monitored progression remains the safety net, so the program must have a clear exit pathway before observation begins."
        ),
        "operate": (
            "WHEN SURVEILLANCE ENDS, operate according to the disease present at that time—not simply because the patient was once on surveillance. For progression still confined to a low-risk unilateral lobe, lobectomy may remain adequate; proven nodal disease or invasive features can require a broader compartment-oriented operation. Do not perform prophylactic total thyroidectomy merely to 'make up for' prior observation. Conversely, do not persist with surveillance when anatomy or documented progression has crossed the agreed safety boundary."
        ),
        "teach": (
            "Chief/boards discriminator: ACTIVE SURVEILLANCE = WHO IS SAFE TO OBSERVE, HOW WILL YOU MEASURE THEM, AND WHAT SPECIFIC FINDING ENDS OBSERVATION? Think low-risk papillary microcarcinoma, no gross ETE/nodes/distant disease/aggressive biology, favorable anatomy, reliable expert ultrasound, informed patient preference, and explicit progression triggers. This is distinct from routine surveillance AFTER thyroidectomy and from the broad DTC card's surgery/RAI/risk-stratification pathway."
        ),
        "tags": ["thyroid active surveillance", "papillary thyroid microcarcinoma", "PTMC", "T1aN0M0", "low-risk papillary thyroid cancer", "serial ultrasound", "3 mm growth", "delayed thyroid surgery", "shared decision making"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — papillary thyroid carcinoma biology, surgical anatomy, and risk-adapted management",
            "K.J. Lee's Essential Otolaryngology, 12e — thyroid cancer evaluation and operative decision-making",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — thyroid malignancy workup and surgical management",
            "Ringel et al. 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer. Thyroid. 2025;35:841-985 — expanded role for active surveillance within individualized DTC care",
            "Lee et al. 2025 Korean Thyroid Association Clinical Management Guideline on Active Surveillance for Low-Risk Papillary Thyroid Carcinoma. Endocrinol Metab. 2025;40:307-341 — candidacy, expert-ultrasound baseline, follow-up schedule, and conversion-to-surgery framework",
            "Korean Society of Thyroid Radiology 2024 consensus statement — standardized ultrasound assessment for low-risk thyroid microcarcinoma active surveillance",
        ],
    },
}


def apply_dtc_active_surveillance_rebuild_v318(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = DTC_SURVEILLANCE_REBUILD_V318.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v318"] = True
            module["semantic_role_v318"] = (
                "DTC extent/risk, risk-adapted initial treatment, and response-directed follow-up"
                if key == "differentiated thyroid cancer"
                else "low-risk PTC active-surveillance selection, serial ultrasound, and conversion-to-treatment triggers"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
