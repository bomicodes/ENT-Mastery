"""v32.0 — source-grounded radioiodine-refractory DTC Concept Hub rebuild.

The general DTC card owns initial staging, surgery, adjuvant RAI selection, and dynamic
response assessment. This companion card owns the later decision that persistent/metastatic
DTC is no longer meaningfully RAI-responsive, then separates observation/local control from
molecularly selected or multikinase systemic therapy. The distinction prevents advanced DTC
from collapsing back into a generic thyroid-cancer treatment card.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


RAIR_DTC_REBUILD_V320 = {
    "radioiodine refractory differentiated thyroid cancer": {
        "recognize": (
            "Use this card only after differentiated thyroid carcinoma has persistent, recurrent, or metastatic STRUCTURAL disease and the question is whether additional I-131 is still biologically useful. Radioiodine-refractory (RAIR) disease is not simply 'thyroglobulin still detectable' and is not defined by reaching an arbitrary cumulative millicurie ceiling. Suspicion is strongest when known disease does not meaningfully concentrate iodine, when lesions progress despite an appropriately prepared therapeutic RAI course, or when clinically important disease is heterogeneous with non-avid/progressive components. Before labeling a patient RAIR, confirm that prior RAI was actually indicated and appropriately delivered, and distinguish biochemical-only persistence from structural disease that needs treatment."
        ),
        "localize": (
            "Map the disease that is driving risk. High-resolution neck ultrasound identifies resectable cervical recurrence; contrast CT/MRI defines bulky central/lateral neck, mediastinal, aerodigestive, neural, or vascular relationships; chest CT characterizes pulmonary metastases; bone/brain imaging is symptom- and risk-directed. Functional iodine imaging answers a different question from FDG-PET: iodine uptake suggests differentiated biology potentially amenable to RAI, whereas FDG-avid/non-iodine-avid disease often marks dedifferentiated, higher-risk tumor. Mixed biology can coexist in one patient, so do not let one iodine-avid lesion hide a threatening non-avid lesion."
        ),
        "workup": (
            "Reconstruct the treatment history before escalating therapy: operation(s), pathology and ATA recurrence-risk features, RAI activity/preparation and post-therapy scan findings, serial thyroglobulin/anti-Tg trend, TSH context, lesion-specific imaging, symptoms, and RECIST-like structural growth. The 2025 ATA systemic-therapy framework requires comprehensive tumor molecular profiling before first-line systemic treatment so actionable RET/NTRK and other driver alterations can redirect therapy. Assess tempo as well as presence of disease: indolent stable metastases can often be observed, whereas reproducible approximately 20% structural growth over roughly 12-14 months, symptoms, or imminent threat to a critical structure pushes toward intervention. Review blood pressure, renal/hepatic function, proteinuria risk, performance status, swallowing/nutrition, and competing morbidity before a chronic TKI is chosen."
        ),
        "manage": (
            "MANAGEMENT IS NOT 'RAIR = START A TKI.' First ask whether the threatening disease is limited enough for LOCAL CONTROL. The 2025 ATA framework prioritizes observation or directed therapy—repeat surgery when safely resectable, focused external-beam radiation/SBRT, thermal ablation or other metastasis-directed therapy—when this can relieve symptoms, prevent structural catastrophe, or delay systemic toxicity. Start systemic therapy for disease that is meaningfully progressive, symptomatic, threatening, and not adequately controlled with RAI or feasible local treatment. Obtain broad molecular testing first: use an appropriate selective targeted inhibitor when an actionable driver has an approved/evidence-supported drug; when no preferable target exists, a multikinase inhibitor is appropriate, with lenvatinib generally favored over sorafenib in contemporary ATA guidance. Treat adverse effects proactively (especially hypertension, proteinuria/renal issues, fatigue, diarrhea/weight loss and wound-healing considerations) and use dose interruption/reduction rather than allowing avoidable toxicity to terminate effective therapy. Selected patients may be considered for molecularly guided redifferentiation strategies intended to restore iodine uptake, but this is not a universal substitute for established local/systemic treatment."
        ),
        "operate": (
            "THE SURGEON'S ROLE IN RAIR DISEASE IS LESION-DIRECTED, not automatic completion/revision surgery. Reoperate when a structurally defined cervical or upper-mediastinal focus is resectable and removing it is likely to improve durable local control, prevent invasion/airway-esophageal-neural morbidity, or postpone systemic therapy. Map the recurrent laryngeal nerves, trachea/esophagus, carotid/jugular system and mediastinum before committing to a scarred-field operation, and weigh R0/R1 feasibility against expected voice, swallow, parathyroid and vascular morbidity. For unresectable but focal threatening disease, multidisciplinary radiation or ablation may be safer than heroic surgery. Coordinate systemic agents around major operations because antiangiogenic TKIs can impair wound healing and increase bleeding/fistula risk; timing should be individualized with medical oncology/endocrinology and the specific drug's pharmacology."
        ),
        "teach": (
            "Chief/boards discriminator: GENERAL DTC asks HOW TO STAGE/RISK-STRATIFY AND CHOOSE INITIAL SURGERY/RAI; RAIR-DTC asks WHETHER MORE I-131 CAN STILL HELP AND, IF NOT, WHICH CURRENT LESION ACTUALLY REQUIRES TREATMENT. The sequence is: confirm structural RAIR biology -> define tempo and threat -> use observation/local therapy when sufficient -> molecularly profile BEFORE systemic therapy -> selective targeted therapy for an actionable driver when appropriate, otherwise a multikinase inhibitor such as lenvatinib. Do not equate detectable Tg, one negative scan, or a cumulative RAI dose alone with an automatic TKI indication."
        ),
        "tags": [
            "radioiodine refractory differentiated thyroid cancer",
            "RAIR-DTC",
            "metastatic thyroid cancer",
            "I-131 refractory",
            "thyroglobulin",
            "FDG PET",
            "molecular profiling",
            "RET",
            "NTRK",
            "lenvatinib",
            "sorafenib",
            "local therapy",
            "redifferentiation therapy",
            "ATA 2025",
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — differentiated thyroid carcinoma recurrence, metastatic disease, RAI biology, reoperative neck surgery, and advanced-disease management",
            "K.J. Lee's Essential Otolaryngology, 12e — thyroid malignancy, recurrent disease, cervical surgery, and adjuvant-treatment principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — thyroid cancer surveillance, recurrence, and surgical management",
            "Ringel et al. 2025 American Thyroid Association Management Guidelines for Adult Patients with Differentiated Thyroid Cancer. Thyroid. 2025;35:841-985 — current RAIR assessment, local-versus-systemic treatment sequencing, molecular profiling, and systemic-therapy framework",
            "American Thyroid Association Clinical Thyroidology for the Public, March 2026 — 2025 ATA systemic-therapy update: molecular testing before first-line systemic therapy; selective targeted therapy when actionable; lenvatinib generally preferred over sorafenib when no preferable target exists",
            "American Thyroid Association Clinical Thyroidology for the Public, July 2026 — 2025 ATA local-versus-systemic update: observation and lesion-directed surgery/radiation/ablation can precede chronic systemic therapy in appropriately selected RAIR disease",
            "Boucai L. An Update on Redifferentiation Therapy for Radioiodine Refractory Thyroid Cancer. Endocrinol Metab Clin North Am. 2025;54:419-431 — molecularly guided redifferentiation as an evolving selected-patient strategy",
        ],
    },
}


def apply_rair_dtc_rebuild_v320(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = RAIR_DTC_REBUILD_V320.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v320"] = True
            module["semantic_role_v320"] = (
                "confirm radioiodine-refractory structural DTC, define tempo/threat, and sequence local versus molecularly selected systemic therapy"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
