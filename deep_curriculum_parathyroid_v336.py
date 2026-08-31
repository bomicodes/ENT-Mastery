"""v33.6 — source-grounded primary / reoperative hyperparathyroidism role separation.

Primary HPT owns biochemical diagnosis, operative indications, first-operation localization and
strategy. Reoperative HPT begins only after prior parathyroid surgery and owns persistent-versus-
recurrent disease confirmation, prior-record reconstruction, high-confidence re-localization and
safe re-entry into a scarred neck. Renal secondary/tertiary HPT remains owned by v31.2.
"""

import re

DOMAIN = "Thyroid / Parathyroid / Salivary"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


PARATHYROID_REBUILD_V336 = {
    "primary hyperparathyroidism": {
        "recognize": (
            "PRIMARY hyperparathyroidism (PHPT) is a BIOCHEMICAL diagnosis before it is an imaging diagnosis: establish reproducible hypercalcemia with an elevated or inappropriately non-suppressed intact PTH after accounting for albumin/ionized calcium when needed, renal function, vitamin-D status and medication effects. Think sporadic single adenoma most often, but keep multigland hyperplasia, double adenomas, MEN/familial disease and parathyroid carcinoma in the differential. Do not call a sestamibi focus 'PHPT' when the calcium/PTH physiology does not support it."
        ),
        "localize": (
            "LOCALIZATION is for OPERATIVE PLANNING, not diagnosis. Once a patient has confirmed PHPT and is proceeding to surgery, use high-quality neck ultrasound plus functional/anatomic imaging according to local expertise (commonly sestamibi/SPECT-CT; 4D-CT or other advanced imaging when first-line studies are negative/discordant). Interpret localization together with thyroid pathology, prior neck surgery, familial/multigland risk and embryologic ectopic sites. Concordant single-gland imaging can support focused parathyroidectomy; negative imaging does not invalidate biochemically proven PHPT and may instead favor bilateral exploration by an experienced surgeon."
        ),
        "workup": (
            "Confirm the phenotype and exclude important mimics before operating. Obtain calcium, intact PTH, creatinine/eGFR, 25-OH vitamin D and a 24-hour urine calcium assessment when appropriate; calculate/interpret calcium-creatinine clearance in the clinical context when familial hypocalciuric hypercalcemia (FHH) is possible, recognizing overlap from vitamin-D deficiency, CKD or low calcium intake. Assess renal stones/nephrocalcinosis and skeletal involvement with DXA including the distal one-third radius; vertebral imaging is appropriate when indicated. Consider genetic/familial evaluation for young patients, multigland disease, syndromic features or family history."
        ),
        "manage": (
            "Parathyroidectomy is definitive treatment and is appropriate for symptomatic PHPT and for asymptomatic patients meeting accepted criteria. Fifth International Workshop criteria include any ONE of: serum calcium >1.0 mg/dL above the upper limit of normal; vertebral fracture or T-score <= -2.5 at a relevant site; eGFR <60 mL/min, nephrolithiasis/nephrocalcinosis, or hypercalciuria (>250 mg/day women or >300 mg/day men); or age <50 years. Surgery may also be chosen by an informed patient without a formal criterion if there is no contraindication. If observing, follow calcium, renal and skeletal status rather than treating the scan."
        ),
        "operate": (
            "Choose the FIRST operation to maximize durable cure while minimizing unnecessary dissection. A well-localized, apparently sporadic single adenoma can be treated with focused exploration in experienced hands, often with intraoperative PTH (ioPTH) as an adjunct; suspected multigland/familial disease, nonlocalizing/discordant studies or intraoperative biochemical concern should lower the threshold for bilateral exploration. Know the superior/inferior gland embryology and ectopic pathways before declaring a gland 'missing.' Preserve viable normal parathyroid tissue and RLN integrity. Failure to cure is not solved by repeatedly excising normal-appearing tissue without a physiologic/anatomic plan."
        ),
        "teach": (
            "Chief/boards sequence: PROVE PHPT -> EXCLUDE MIMICS/FHH -> decide whether surgery is INDICATED -> LOCALIZE only after the decision to operate -> choose focused versus bilateral exploration from localization plus multigland risk. The 2022 asymptomatic criteria are one-of-many, not an all-of-the-above checklist. A negative scan does NOT mean no PHPT. Contrast with renal HPT (systemic multigland CKD-MBD) and with REOPERATIVE HPT (a failed/relapsed prior operation requiring a new localization and risk calculation)."
        ),
        "tags": [
            "primary hyperparathyroidism", "parathyroid adenoma", "FHH", "calcium creatinine clearance",
            "parathyroid localization", "sestamibi", "4D CT", "bilateral neck exploration",
            "focused parathyroidectomy", "intraoperative PTH", "Fifth International Workshop"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — parathyroid physiology, embryology/ectopic anatomy, localization and operative exploration framework",
            "K.J. Lee's Essential Otolaryngology, 12e — hyperparathyroidism diagnosis, localization and parathyroidectomy anatomy/strategy",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — practical PHPT workup, localization, ioPTH and parathyroidectomy pearls",
            "Bilezikian et al. 2022 Fifth International Workshop: Evaluation and Management of Primary Hyperparathyroidism — current biochemical evaluation and operative criteria",
            "AAES 2016 Guidelines for Definitive Management of Primary Hyperparathyroidism — operative strategy, cure/failure definitions and reoperative principles"
        ],
    },
    "reoperative hyperparathyroidism": {
        "recognize": (
            "REOPERATIVE hyperparathyroidism is not simply 'PHPT again.' First classify the failure: PERSISTENT PHPT = failure to achieve normocalcemia within 6 months of parathyroidectomy; RECURRENT PHPT = hypercalcemia returning after >6 months of documented normocalcemia. Reconfirm that the patient truly has PTH-dependent hypercalcemia and reconsider FHH, medications, renal disease and other diagnostic errors before accepting the morbidity of another neck exploration. A high PTH with normal calcium after surgery is not by itself recurrent PHPT."
        ),
        "localize": (
            "Reoperation requires a TARGET, not exploratory optimism. Start localization with the PRIOR OPERATION: obtain the operative note, pathology, ioPTH curve, prior imaging and any record of which glands were identified, biopsied, removed, autotransplanted or left in situ. Then obtain expert reoperative imaging—high-resolution ultrasound and sestamibi/SPECT-CT when useful, with 4D-CT and increasingly fluorocholine PET/CT for nonlocalizing/discordant cases. Search embryologic ectopic/supernumerary sites, mediastinum/thymus and prior operative beds. Selective venous PTH sampling is reserved for difficult cases when noninvasive studies cannot provide a sufficiently actionable target."
        ),
        "workup": (
            "Before offering reoperation, answer four questions: (1) Is the biochemical diagnosis secure? (2) Does the patient still meet a meaningful indication for surgery? (3) What exactly happened at the first operation? (4) Is there convincing localization that justifies scarred-neck risk? Document current vocal-fold/RLN function before re-entry, especially after prior central neck surgery or voice change. Consider whether persistence reflects a missed adenoma, ectopic/supernumerary gland, unrecognized multigland disease, parathyromatosis or rarely carcinoma; recurrence after a true disease-free interval raises residual/multigland/familial biology rather than simply 'the surgeon missed it.'"
        ),
        "manage": (
            "The threshold for reoperation is deliberately higher than for an index operation because RLN injury and permanent hypoparathyroidism are more consequential in a scarred neck. Refer to a high-volume parathyroid surgeon and do not re-explore solely for an abnormal scan or modest biochemical abnormality without a clear expected benefit. When disease is biochemically significant and the surgical indication persists, require the best localization achievable and plan the approach around prior dissection. Nonoperative surveillance/medical control is reasonable when localization is inadequate or operative risk exceeds expected benefit."
        ),
        "operate": (
            "At reoperation, enter through the least hostile route that reliably reaches the localized target, using prior records and imaging to avoid unnecessary bilateral scar dissection. Identify/protect the RLN deliberately; remove the pathologic target while preserving the patient's remaining parathyroid reserve. ioPTH should be considered to confirm biochemical success and detect unsuspected additional hyperfunctioning tissue. If the expected gland is absent, follow embryologic pathways rather than blind scar excision. Extensive repeat exploration without a convincing target can convert persistent PHPT into permanent RLN injury or hypoparathyroidism—know when to stop and re-localize."
        ),
        "teach": (
            "Chief framework: INDEX PHPT asks 'does this patient have PHPT, should I operate, and which operative strategy fits?' REOPERATIVE PHPT asks 'persistent or recurrent, was the original diagnosis correct, what did the first surgeon actually do, where is the remaining hyperfunctioning tissue NOW, and is the target worth the scarred-neck risk?' AAES defines persistence as no normocalcemia by 6 months and recurrence as hypercalcemia after >6 months of normocalcemia. In 2026 practice, fluorocholine PET/CT is an important advanced localization option when conventional studies are insufficient, but even an excellent image must be reconciled with the biochemical diagnosis and prior operative map."
        ),
        "tags": [
            "reoperative hyperparathyroidism", "persistent hyperparathyroidism", "recurrent hyperparathyroidism",
            "reoperative parathyroidectomy", "fluorocholine PET CT", "4D CT", "selective venous PTH",
            "ectopic parathyroid", "supernumerary parathyroid", "recurrent laryngeal nerve", "intraoperative PTH"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — reoperative parathyroid anatomy, ectopic/supernumerary glands, RLN risk and revision exploration framework",
            "K.J. Lee's Essential Otolaryngology, 12e — parathyroid embryology, localization and reoperative surgical principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — persistent/recurrent HPT localization and operative pearls",
            "AAES 2016 Guidelines for Definitive Management of Primary Hyperparathyroidism, Recommendations 15-4 and 17-1 through 17-3 — persistent/recurrent definitions, diagnostic confirmation, prior-record/RLN review, expert-surgeon referral and ioPTH",
            "Vu et al. World Journal of Surgery 2026 — 18F-choline PET/CT localization in reoperative parathyroidectomy",
            "Persistent and Recurrent Primary Hyperparathyroidism: Etiological Factors and Pre-Operative Evaluation (2023) — contemporary reoperative diagnostic/localization framework"
        ],
    },
}


def apply_parathyroid_role_separation_v336(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = PARATHYROID_REBUILD_V336.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v336"] = True
        module["semantic_role_v336"] = {
            "primary hyperparathyroidism": "index PHPT biochemical diagnosis, operative indication, first-operation localization and strategy",
            "reoperative hyperparathyroidism": "persistent/recurrent PHPT confirmation, prior-operation reconstruction, high-confidence re-localization and scarred-neck reoperation",
        }[key]
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
