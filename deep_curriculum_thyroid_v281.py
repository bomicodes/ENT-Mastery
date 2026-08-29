"""v28.1 — source-grounded advanced thyroid Concept Hub rebuild.

Keeps Radioiodine-Refractory DTC distinct from the parent DTC card: this card starts
only after persistent/recurrent disease is established and teaches how to determine
RAI refractoriness, observe indolent disease, use local therapy, and select molecularly
directed/systemic therapy when progression warrants it.
"""

import re

DOMAIN = "Thyroid / Parathyroid / Salivary"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


RAIR_DTC_V281 = {
    "recognize": (
        "Recognize radioiodine-refractory differentiated thyroid cancer (RAIR-DTC) as persistent or metastatic follicular-cell-derived cancer for which additional radioactive iodine is unlikely to provide meaningful tumor control—not simply any patient with detectable thyroglobulin after thyroidectomy. Suspicion rises when known tumor does not concentrate iodine, loses previously demonstrated iodine avidity, progresses despite appropriate RAI, or contains clinically important lesions that behave discordantly. The clinical consequence is crucial: repeated empiric RAI can add salivary, marrow, gonadal, and second-malignancy toxicity without helping a truly refractory tumor."
    ),
    "localize": (
        "Localize both the BURDEN and the THREAT of RAIR disease. Separate isolated cervical recurrence from oligometastatic disease and diffuse multiorgan progression; map lesions threatening the airway, esophagus, recurrent laryngeal nerve, major vessels, spinal cord, weight-bearing bone, or brain. Also recognize biologic heterogeneity: one progressing non-avid lesion can drive morbidity while other deposits remain stable. Treatment therefore follows the lesion most likely to cause symptoms or irreversible harm rather than treating every radiographic deposit identically."
    ),
    "workup": (
        "Confirm structural disease and document its tempo before committing a clinically well patient to lifelong systemic therapy. Trend high-quality cross-sectional imaging using reproducible measurements, correlate thyroglobulin with anti-thyroglobulin antibodies, and use functional imaging selectively when it will clarify disease distribution or biology. Review prior RAI dose, post-therapy uptake, and structural response rather than labeling disease refractory from thyroglobulin alone. Before first-line systemic therapy, obtain comprehensive tumor molecular profiling because the 2025 ATA framework links actionable drivers to preferred targeted treatment. Baseline blood pressure, renal/proteinuria, hepatic, cardiac, and performance-status assessment matters when a multikinase inhibitor is being considered."
    ),
    "manage": (
        "Manage RAIR-DTC according to pace, symptoms, anatomy, and targetability. Stable or slowly progressive asymptomatic disease may be observed with serial imaging; RAIR status itself is not an automatic indication for a kinase inhibitor. For limited or threatening sites, prioritize effective local therapy—surgery, focused external-beam radiation/SBRT, or selected image-guided ablation—when it can prevent morbidity or delay systemic treatment. Start systemic therapy when disease is meaningfully progressive, symptomatic, threatening, and not adequately controlled by local treatment. If an actionable molecular alteration has an effective selective inhibitor, the 2025 ATA framework favors genotype-directed therapy; when no preferred actionable target is present, a multikinase inhibitor is used, with lenvatinib generally favored over sorafenib."
    ),
    "operate": (
        "The surgeon's role does not end when disease becomes RAI-refractory. Reoperation can be valuable for resectable cervical disease causing or likely to cause airway, esophageal, nerve, skin, or vascular morbidity, but should be weighed against scarred-field RLN/parathyroid risk and whether surgery will actually change the disease course. For oligoprogression, coordinate surgery, SBRT, or ablation so a patient benefiting from systemic therapy does not have to abandon an otherwise effective regimen because of one escaping lesion. Before antiangiogenic multikinase therapy, identify tumors invading aerodigestive structures because tumor necrosis/shrinkage can increase bleeding or fistula risk; multidisciplinary sequencing is essential."
    ),
    "teach": (
        "Chief/boards framework: REFRACTORY does not mean TREAT NOW. First prove that further iodine is unlikely to help; then ask whether the cancer is actually PROGRESSING, whether a particular lesion is THREATENING, whether LOCAL control can buy durable time, and what MOLECULAR driver is present before systemic therapy. Do not treat a thyroglobulin number in isolation. Do not keep giving empiric RAI to structurally progressive nonresponsive disease. Once systemic therapy is appropriate, toxicity management is part of cancer treatment—especially hypertension, proteinuria/renal effects, fatigue, diarrhea, weight loss, and other VEGF-pathway toxicities with multikinase inhibition."
    ),
    "tags": ["radioiodine refractory differentiated thyroid cancer", "RAIR DTC", "metastatic thyroid cancer", "lenvatinib", "sorafenib", "targeted therapy", "molecular testing", "local therapy"],
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — recurrent/metastatic differentiated thyroid carcinoma and salvage treatment",
        "K.J. Lee's Essential Otolaryngology, 12e — thyroid malignancy and recurrent disease",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — thyroid cancer surveillance and advanced disease",
        "American Thyroid Association — 2025 Management Guidelines for Adult Patients with Differentiated Thyroid Cancer (Ringel et al., Thyroid 2025;35:841-985) — RAIR disease, local therapy, molecular profiling, and systemic therapy",
    ],
}


def apply_thyroid_rair_rebuild_v281(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        if _norm(module.get("topic")) != "radioiodine refractory differentiated thyroid cancer":
            continue
        for field in FIELDS:
            module[field] = RAIR_DTC_V281[field]
        module["tags"] = list(RAIR_DTC_V281["tags"])
        module["source_basis"] = list(RAIR_DTC_V281["source_basis"])
        module["source_grounded_v281"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
