"""v28.2 — source-grounded parathyroid Concept Hub rebuild.

Separates primary hyperparathyroidism from secondary/tertiary renal hyperparathyroidism
by making each six-stage ladder clinically progressive and etiology-specific.
"""

import re

DOMAIN = "Thyroid / Parathyroid / Salivary"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


PARATHYROID_V282 = {
    "primary hyperparathyroidism": {
        "recognize": (
            "Recognize primary hyperparathyroidism (PHPT) as inappropriate PTH secretion for the calcium level: usually hypercalcemia with an elevated PTH, but an inappropriately normal PTH in a hypercalcemic patient is also abnormal. Classic complications are nephrolithiasis/nephrocalcinosis, cortical bone loss or fragility fracture, and symptomatic hypercalcemia; many patients are now discovered biochemically. Normocalcemic PHPT is a diagnosis of exclusion—secondary causes of elevated PTH such as vitamin-D deficiency, renal insufficiency, low calcium intake/malabsorption, and relevant medications must be addressed first."
        ),
        "localize": (
            "Localize the DISEASE PATTERN before localizing a gland. Sporadic PHPT is most often a single adenoma, but multigland hyperplasia, double adenomas, hereditary disease (for example MEN syndromes), and rarely carcinoma change operative strategy. After the biochemical diagnosis is secure, use cervical ultrasound and sestamibi-based imaging, with 4D-CT or other advanced localization selectively, to map likely abnormal glands for surgery. Remember embryology when imaging is discordant: superior glands are more positionally constant posteriorly, whereas inferior glands have broader migration with the thymus and may be intrathymic or mediastinal."
        ),
        "workup": (
            "Confirm true PTH-dependent hypercalcemia with repeat albumin-adjusted or ionized calcium and intact PTH, then assess creatinine/eGFR, phosphorus, 25-OH vitamin D, skeletal density (lumbar spine, hip, and distal one-third radius), and renal stone burden. Obtain 24-hour urine calcium when appropriate, especially to quantify renal risk and to distinguish PHPT from familial hypocalciuric hypercalcemia (FHH); interpret urinary calcium cautiously because CKD, vitamin-D deficiency, low calcium intake, and thiazides can lower it. Current 2022 Fifth International Workshop surgical criteria for otherwise asymptomatic PHPT include any ONE of: calcium >1 mg/dL above the upper limit of normal, T-score <= -2.5 or vertebral fracture, eGFR <60 mL/min, nephrolithiasis/nephrocalcinosis, hypercalciuria >250 mg/day in women or >300 mg/day in men, or age <50 years."
        ),
        "manage": (
            "Parathyroidectomy is the definitive treatment for PHPT and is recommended for symptomatic disease and for patients meeting guideline criteria; it remains a reasonable option for other appropriate patients who prefer definitive cure. If surgery is deferred or contraindicated, monitor calcium, renal function, bone density, and renal manifestations. Correct vitamin-D deficiency carefully. Cinacalcet can lower serum calcium but does not reliably restore bone density; antiresorptive therapy such as a bisphosphonate or denosumab may be used when skeletal protection is the principal goal. Localization studies guide the operation—they do not establish or exclude the biochemical diagnosis."
        ),
        "operate": (
            "Choose focused parathyroidectomy when biochemistry and localization support a single-gland process and bilateral exploration when localization is negative/discordant, multigland disease is suspected, or the clinical context demands it. Identify abnormal tissue while protecting the recurrent laryngeal nerves and preserving viable normal parathyroid tissue. Intraoperative PTH (ioPTH) is most useful during focused surgery: a >50% fall from an appropriate pre-excision reference at the protocol-specified time is a common cure criterion, but the absolute value and clinical context matter. Renal dysfunction can slow PTH clearance and produce delayed kinetics, so a failure to fall promptly should not automatically trigger indiscriminate exploration—repeat sampling and interpret the curve with the patient's renal function and operative findings. Anticipate postoperative hypocalcemia; patients with severe skeletal disease or very high preoperative PTH/alkaline phosphatase are at particular risk for hungry-bone syndrome."
        ),
        "teach": (
            "Chief/boards framework: DIAGNOSE biochemically, then LOCALIZE for surgery. Hypercalcemia plus a non-suppressed PTH is PHPT until an important mimic—especially FHH—has been excluded. Negative imaging does not cancel a valid surgical indication. One guideline criterion is enough to recommend surgery in an otherwise asymptomatic patient. Know the operative split: convincing single-gland disease can be approached focally with ioPTH; suspected multigland/hereditary disease requires a strategy that addresses more than one gland. After surgery, durable cure is normal calcium homeostasis for at least 6 months, not merely a reassuring immediate ioPTH drop."
        ),
        "tags": ["primary hyperparathyroidism", "PHPT", "parathyroid adenoma", "familial hypocalciuric hypercalcemia", "FHH", "intraoperative PTH", "hungry bone syndrome", "parathyroidectomy"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — parathyroid physiology, localization, and operative management",
            "K.J. Lee's Essential Otolaryngology, 12e — hyperparathyroidism and parathyroid surgery",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — parathyroid disease and operative pearls",
            "Fifth International Workshop — Evaluation and Management of Primary Hyperparathyroidism (JBMR 2022;37:2293-2314) — current evaluation and surgical criteria",
            "American Association of Endocrine Surgeons — Guidelines for Definitive Management of Primary Hyperparathyroidism (JAMA Surg 2016) — operative planning, ioPTH, cure, and reoperative principles",
        ],
    },
    "secondary tertiary hyperparathyroidism": {
        "recognize": (
            "Recognize secondary hyperparathyroidism (SHPT) as an appropriate compensatory rise in PTH driven most commonly by chronic kidney disease: phosphate retention, reduced calcitriol production, hypocalcemic signaling, and skeletal resistance progressively stimulate all parathyroid glands. Biochemistry is therefore different from primary disease—PTH is elevated in the context of CKD with calcium often low or normal and phosphate often elevated. Tertiary hyperparathyroidism is autonomous PTH secretion after prolonged secondary stimulation, classically in advanced CKD or after renal transplantation, and is suggested by persistent marked PTH elevation with hypercalcemia once the original hypocalcemic drive no longer explains the physiology."
        ),
        "localize": (
            "Localize SHPT/tertiary disease as a MULTIGLAND process rather than searching for one culprit adenoma. All four glands may be enlarged, and supernumerary or ectopic tissue—especially within the thymus/mediastinum—matters when surgery is planned or disease persists. Distinguish the patient's physiologic setting first: dialysis-dependent CKD with medically refractory SHPT, a transplant recipient with persistent hypercalcemic autonomous disease, and a patient with sporadic PHPT require different expectations even if one imaging study highlights a dominant gland. Imaging is for operative mapping and reoperative planning, not for proving renal hyperparathyroidism."
        ),
        "workup": (
            "Evaluate trends rather than one isolated PTH value. Review CKD stage, dialysis adequacy, transplant status, serial calcium, phosphate, PTH, alkaline phosphatase, 25-OH vitamin D, medications, skeletal symptoms/fractures, calciphylaxis or other soft-tissue/vascular calcification, and pruritus or bone pain when clinically relevant. KDIGO emphasizes interpreting calcium, phosphate, and PTH together and correcting modifiable drivers before surgery. If parathyroidectomy is being considered, perform cervical imaging to identify enlarged, ectopic, or supernumerary tissue and coordinate timing with nephrology/transplant teams; plan perioperative dialysis and calcium management because severe postoperative hypocalcemia is common."
        ),
        "manage": (
            "Treat the underlying CKD-mineral bone disorder first: control phosphate burden and dietary/phosphate-binder exposure as appropriate, correct vitamin-D deficiency, and use active vitamin-D receptor therapy and/or a calcimimetic according to renal status and nephrology guidance. KDIGO recommends parathyroidectomy for severe hyperparathyroidism in CKD stages G3a-G5D that fails to respond to medical/pharmacologic therapy. After renal transplantation, persistent hypercalcemic tertiary disease may improve with time in selected patients, but durable symptomatic or biochemically important autonomous disease can require calcimimetic therapy or surgery. The threshold for operation is therefore refractory disease and end-organ consequence—not an arbitrary PTH number in isolation."
        ),
        "operate": (
            "Plan renal hyperparathyroid surgery as multigland surgery. Common strategies include subtotal parathyroidectomy (leaving a small vascularized remnant) or total parathyroidectomy with autotransplantation; institutional practice and the patient's transplant/dialysis trajectory influence the choice. Perform a systematic four-gland exploration and consider cervical thymectomy when appropriate because supernumerary/intrathymic glands are a major cause of persistence. The postoperative priority is calcium: high-turnover bone can avidly take up calcium and phosphate after the PTH source is removed, producing profound hungry-bone syndrome that may require aggressive calcium plus active vitamin-D replacement and close serial monitoring."
        ),
        "teach": (
            "Chief/boards discriminator: PRIMARY = autonomous secretion arising de novo, usually hypercalcemia with non-suppressed PTH and often single-gland disease; SECONDARY = compensatory PTH elevation, classically CKD with low/normal calcium and phosphate retention; TERTIARY = autonomous multigland secretion after longstanding secondary stimulation, typically with hypercalcemia. Do not let one 'hot' gland on imaging convert renal multigland disease into a presumed single adenoma. For severe medically refractory renal HPT, surgery must address all gland tissue and the postoperative calcium plan is part of the operation—not an afterthought."
        ),
        "tags": ["secondary hyperparathyroidism", "tertiary hyperparathyroidism", "renal hyperparathyroidism", "CKD MBD", "calcimimetic", "subtotal parathyroidectomy", "hungry bone syndrome", "renal transplant"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — secondary/tertiary hyperparathyroidism and multigland surgery",
            "K.J. Lee's Essential Otolaryngology, 12e — renal hyperparathyroidism and parathyroidectomy",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — parathyroid surgery and postoperative calcium management",
            "KDIGO CKD-MBD Clinical Practice Guideline Update (2017, current KDIGO CKD-MBD guideline resource) — serial biochemical assessment, medical therapy, and parathyroidectomy for severe refractory HPT",
        ],
    },
}


def apply_parathyroid_rebuild_v282(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = PARATHYROID_V282.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v282"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
