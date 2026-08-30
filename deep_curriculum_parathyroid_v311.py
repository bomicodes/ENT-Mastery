"""v31.1 — source-grounded primary vs reoperative hyperparathyroidism Concept Hub rebuild.

Primary PHPT owns biochemical diagnosis, operative indications, first-operation strategy,
intraoperative PTH interpretation, and cure. Reoperative HPT owns confirmation of persistent/
recurrent disease, review of prior operative/pathology data, high-confidence relocalization,
scarred-neck risk, and reoperative rescue strategy.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


PARATHYROID_REBUILD_V311 = {
    "primary hyperparathyroidism": {
        "recognize": (
            "Recognize PRIMARY hyperparathyroidism (PHPT) biochemically before thinking about localization: repeated hypercalcemia with an elevated or inappropriately non-suppressed intact PTH is the classic pattern. Correct/confirm calcium as needed, assess renal function and vitamin D, and exclude important mimics such as familial hypocalciuric hypercalcemia (FHH) when the phenotype fits. A localization study does not diagnose PHPT. Symptomatic disease includes nephrolithiasis/nephrocalcinosis, skeletal disease/fracture, and clinically important hypercalcemia; many modern patients are asymptomatic or discovered incidentally. Normocalcemic PHPT requires persistently normal total/ionized calcium with elevated PTH only after secondary causes of PTH elevation have been rigorously excluded."
        ),
        "localize": (
            "Localization is for OPERATIVE PLANNING after a biochemical diagnosis. High-resolution surgeon-performed or expert ultrasound and sestamibi/SPECT-CT are common first-line tests; 4D-CT or other advanced imaging is useful when first-line studies are discordant or nonlocalizing. Concordant single-gland imaging supports a focused approach, but imaging cannot reliably exclude multigland disease. Know the embryologic search pattern: superior glands are usually posterior and more constant; inferior glands descend with thymus and are more variable, including thyrothymic ligament/thymic locations. Ectopic glands may be retroesophageal, tracheoesophageal, intrathyroidal, mediastinal, or carotid-sheath related."
        ),
        "workup": (
            "Confirm the PHPT phenotype and document end-organ consequences. Obtain calcium, albumin and/or ionized calcium when appropriate, intact PTH, creatinine/eGFR or creatinine clearance, 25-OH vitamin D, and urinary calcium/stone-risk evaluation when relevant; DXA should include lumbar spine, hip, and distal one-third radius, and evaluate for vertebral fracture when indicated. The 2022 Fifth International Workshop recommends surgery for symptomatic PHPT and for asymptomatic patients meeting any major criterion: serum calcium >1 mg/dL above the upper limit of normal, skeletal involvement (fracture or T-score <= -2.5), renal involvement (eGFR/creatinine clearance <60 mL/min, nephrolithiasis/nephrocalcinosis, or hypercalciuria >250 mg/day in women or >300 mg/day in men), or age <50 years. Surgery remains an option for other appropriate patients who prefer definitive treatment."
        ),
        "manage": (
            "Parathyroidectomy is the definitive treatment when operative criteria are met or an appropriate informed patient elects surgery. The core preoperative decision is focused image-guided parathyroidectomy versus bilateral neck exploration. A focused operation is appropriate for a well-localized presumed single adenoma when the surgeon can verify biochemical success; bilateral exploration is favored when multigland disease is known/suspected, imaging is discordant or nonlocalizing, hereditary disease is likely, or intraoperative findings/PTH kinetics do not support cure. Optimize vitamin D when appropriate and anticipate postoperative hypocalcemia/hungry-bone risk in patients with severe biochemical or skeletal disease."
        ),
        "operate": (
            "At first operation, preserve normal-gland blood supply, identify the abnormal gland in its expected embryologic compartment, and avoid treating imaging as infallible anatomy. In a focused procedure, use a validated intraoperative PTH (ioPTH) protocol; a commonly used criterion is a >50% fall from the appropriate baseline by roughly 10 minutes, interpreted together with the absolute value and trajectory. If PTH does not fall adequately, first verify timing/specimen issues and consider additional samples before automatically declaring another abnormal gland. IMPORTANT RENAL PEARL: impaired renal function can slow PTH clearance and delay the decline, so a failure to reach a >50% fall at the earliest time point can reflect altered kinetics rather than missed multigland disease; later samples and the full operative context matter. If the biochemical trajectory remains inadequate, proceed systematically to further exploration rather than blind excision. Postoperatively monitor for neck hematoma, symptomatic hypocalcemia, and hungry-bone syndrome."
        ),
        "teach": (
            "Chief/boards framework: PHPT = DIAGNOSE BIOCHEMICALLY -> IDENTIFY SURGICAL INDICATION -> LOCALIZE FOR PLANNING -> CHOOSE FOCUSED VS BILATERAL STRATEGY -> VERIFY CURE. Do not order imaging to decide whether PHPT exists. Do not let a negative scan deny an otherwise indicated operation by an experienced parathyroid surgeon. Know the 2022 asymptomatic-surgery thresholds, recognize multigland/hereditary disease, and understand ioPTH as a kinetic test rather than a magic single number. Cure is durable eucalcemia after surgery; persistent disease is hypercalcemia that never resolves or returns within 6 months, whereas recurrence occurs after a documented period of normocalcemia beyond 6 months. Those failures belong to the separate reoperative pathway."
        ),
        "tags": ["primary hyperparathyroidism", "parathyroidectomy", "intraoperative PTH", "Miami criterion", "multigland disease", "4D CT", "sestamibi", "FHH", "hungry bone", "thyrothymic ligament"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — parathyroid physiology, localization, operative anatomy, primary and reoperative parathyroid surgery",
            "K.J. Lee's Essential Otolaryngology, 12e, Ch. 38 Thyroid and Parathyroid Glands — PHPT, parathyroid anatomy/localization, and operative management",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — thyroid/parathyroid disease and parathyroid surgery",
            "Fifth International Workshop on Primary Hyperparathyroidism, JBMR 2022 — diagnosis, evaluation, and current operative indications",
            "AAES Guidelines for Definitive Management of Primary Hyperparathyroidism, JAMA Surgery 2016 — focused versus bilateral exploration, ioPTH, postoperative assessment, and reoperative expertise"
        ],
    },
    "reoperative hyperparathyroidism": {
        "recognize": (
            "Reoperative hyperparathyroidism is a FAILURE/RECURRENCE problem, not simply 'severe PHPT.' First classify the timeline: persistent PHPT means hypercalcemia persists after the original operation or returns within 6 months; recurrent PHPT returns after a documented normocalcemic interval longer than 6 months. Before planning another neck exploration, reconfirm that the patient truly has PTH-dependent hypercalcemia and that there is a meaningful indication to accept reoperative risk. Common mechanisms include a missed ectopic adenoma, unrecognized multigland disease, supernumerary glands, an incompletely treated hyperfunctioning gland, parathyromatosis, or—less commonly—carcinoma; recurrence can also reflect progressive multigland/hereditary disease."
        ),
        "localize": (
            "Reoperative localization requires a HIGHER CONFIDENCE BAR because scar destroys normal tissue planes and RLN/parathyroid risk is higher. Reconstruct the first operation before ordering more scans: obtain the operative report, pathology, original imaging, ioPTH curve, which glands were seen/removed, any autotransplant, and postoperative calcium/PTH course. Repeat expert ultrasound plus functional imaging as appropriate; 4D-CT is especially useful for distorted anatomy and ectopic candidates, while choline PET/CT can be valuable in difficult nonlocalizing cases where available. Selective venous sampling is a problem-solving regionalization test for truly difficult cases, not routine first-line localization. Require anatomically coherent evidence rather than chasing every equivocal focus."
        ),
        "workup": (
            "Reconfirm calcium/PTH physiology, renal function, vitamin D, medications, and FHH exclusion when relevant, then re-establish the OPERATIVE INDICATION. Review prior pathology critically: was parathyroid tissue actually removed, was the weight/cellularity plausible, and was a normal gland mistakenly removed while the adenoma remained? Map prior surgery onto embryology—retroesophageal superior glands, descended superior glands, thyrothymic/intrathymic inferior glands, mediastinum, intrathyroidal tissue, and supernumerary glands are classic misses. Document current vocal-fold mobility before reoperative exploration because a pre-existing RLN deficit fundamentally changes the risk discussion and operative plan."
        ),
        "manage": (
            "Do not reoperate merely because PTH is elevated or because imaging shows a possible gland. Reoperation should follow confirmed recurrent/persistent PTH-dependent hypercalcemia, an appropriate indication for definitive treatment, and convincing localization/operative logic—ideally in a high-volume endocrine-surgery setting. If disease is mild and the localization-risk balance is poor, surveillance or medical control may be safer than blind re-exploration. When surgery is justified, plan the side/compartment, nerve strategy, and contingency for multigland disease before incision; counsel explicitly that cure remains achievable but RLN injury and permanent hypoparathyroidism are more likely than at first operation."
        ),
        "operate": (
            "Reoperative surgery is anatomy plus information discipline. Enter through the least scarred safe plane when possible, use preoperative localization to target a compartment rather than performing an indiscriminate scarred-neck dissection, and identify/protect the RLN with heightened attention to altered anatomy. Intraoperative nerve monitoring is particularly useful as an adjunct in a reoperative field, though it does not replace visual/anatomic nerve preservation. Use ioPTH to test whether the suspected culprit explains the biochemical disease; if the fall is delayed or inadequate, integrate timing, baseline choice, renal clearance, and the preoperative disease model before extending exploration. In CKD, delayed PTH clearance can blunt an early >50% decline—obtain later samples rather than reflexively converting a kinetic delay into a diagnosis of another abnormal gland. Avoid devascularizing the remaining normal parathyroid reserve while pursuing biochemical perfection."
        ),
        "teach": (
            "Chief/boards framework: REOPERATIVE HPT = PROVE DISEASE -> CLASSIFY PERSISTENT VS RECURRENT -> RECONSTRUCT THE PRIOR OPERATION -> RELOCALIZE WITH HIGH CONFIDENCE -> REOPERATE ONLY WHEN BENEFIT EXCEEDS SCARRED-NECK RISK. The highest-yield mistake is treating reoperation like a repeat first operation. The prior op note, pathology, ioPTH trace, and exact glands already encountered are part of today's anatomy. A nonlocalizing patient is not a mandate for blind bilateral re-exploration. Preoperative laryngoscopy, experienced localization, deliberate RLN strategy, and preservation of remaining parathyroid function are central."
        ),
        "tags": ["reoperative hyperparathyroidism", "persistent hyperparathyroidism", "recurrent hyperparathyroidism", "4D CT", "choline PET", "venous sampling", "reoperative parathyroidectomy", "recurrent laryngeal nerve", "intraoperative PTH"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — reoperative parathyroid localization, ectopic/supernumerary glands, RLN risk, and operative strategy",
            "K.J. Lee's Essential Otolaryngology, 12e, Ch. 38 Thyroid and Parathyroid Glands — parathyroid operative anatomy and recurrent/persistent disease principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — parathyroid localization and operative management",
            "AAES Guidelines for Definitive Management of Primary Hyperparathyroidism, JAMA Surgery 2016 — reoperative parathyroidectomy as a challenging entity requiring special expertise",
            "Fifth International Workshop on Primary Hyperparathyroidism, JBMR 2022 — biochemical disease framework and operative indications"
        ],
    },
}


def apply_parathyroid_rebuild_v311(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = PARATHYROID_REBUILD_V311.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v311"] = True
            module["semantic_role_v311"] = (
                "initial PHPT diagnosis, operative indication, first-operation strategy, ioPTH interpretation, and cure"
                if key == "primary hyperparathyroidism"
                else "persistent/recurrent disease confirmation, prior-operation reconstruction, high-confidence relocalization, and scarred-neck rescue"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
