"""v31.2 — source-grounded Secondary / Tertiary Hyperparathyroidism rebuild.

Keeps renal secondary/tertiary HPT clinically distinct from primary HPT and from
reoperative parathyroid disease. The card owns CKD-MBD physiology, serial biochemical
interpretation, nephrology-first medical therapy, the threshold for surgery, and the
multigland operative strategy/hungry-bone risk of renal hyperparathyroidism.
"""

import re

DOMAIN = "Thyroid / Parathyroid / Salivary"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


RENAL_HPT_REBUILD_V312 = {
    "secondary tertiary hyperparathyroidism": {
        "recognize": (
            "Recognize SECONDARY hyperparathyroidism (SHPT) as an adaptive CKD-mineral/bone disorder rather than a solitary-gland surgical disease. Declining renal phosphate excretion, reduced calcitriol activity, hypocalcemic drive and altered FGF23/vitamin-D physiology chronically stimulate all parathyroid glands, producing diffuse/nodular multigland hyperplasia. PTH should therefore be interpreted with calcium, phosphate, alkaline phosphatase, vitamin-D status, CKD stage and longitudinal trend—not as an isolated number. TERTIARY HPT is the later autonomous phenotype: after prolonged SHPT, hyperplastic glands become relatively calcium-insensitive and continue excessive PTH secretion, classically producing persistent hypercalcemia in advanced CKD or after successful renal transplantation. The practical discriminator from PRIMARY HPT is the disease context and gland biology: primary disease is usually autonomous single-gland disease; renal SHPT begins as physiologic multigland stimulation, and tertiary disease represents autonomy emerging from that chronic multigland process."
        ),
        "localize": (
            "Localize the problem first to the CKD-MBD physiology and only secondarily to individual glands. In renal HPT, imaging is NOT used to establish the diagnosis or decide whether an elevated PTH is 'real'; expect four-gland disease and remember supernumerary and ectopic glands, especially thymic/mediastinal tissue. Ultrasound and sestamibi/SPECT-CT can be useful once surgery is planned to identify marked asymmetry, ectopic/supernumerary tissue, concomitant thyroid disease, or a mediastinal target, but a single dominant scan focus must not convert a renal-HPT operation into an assumed focused adenoma excision. Persistent disease after prior renal parathyroid surgery is a separate REOPERATIVE localization problem and belongs in the reoperative-HPT card."
        ),
        "workup": (
            "Build the preoperative decision from SERIAL calcium, phosphate and PTH values plus alkaline phosphatase, 25-OH vitamin D, renal function/dialysis status and symptoms/end-organ burden. In CKD G3a-G5 not on dialysis, KDIGO emphasizes progressively rising or persistently elevated PTH and correction of modifiable drivers such as hyperphosphatemia, high phosphate intake, hypocalcemia and vitamin-D deficiency rather than reacting to one high value. In dialysis patients, the desired PTH range is intentionally broader than normal; oversuppression can contribute to low-turnover/adynamic bone disease. For suspected tertiary HPT after transplant, document persistent hypercalcemia with inappropriately high PTH and assess phosphate, graft function, nephrolithiasis/nephrocalcinosis, skeletal disease and the trajectory since transplantation. Before surgery, assess the severity of high-turnover bone disease because very high PTH/alkaline phosphatase and skeletal involvement predict profound postoperative hungry-bone hypocalcemia."
        ),
        "manage": (
            "Management is NEPHROLOGY-FIRST and physiology-directed. Correct modifiable phosphate/calcium/vitamin-D abnormalities and optimize dialysis/CKD-MBD therapy. In CKD G5D requiring PTH lowering, KDIGO supports calcimimetics, calcitriol/vitamin-D analogs, or selected combinations guided by calcium and phosphate. Do not normalize PTH reflexively in dialysis patients; follow trends and the whole mineral profile. Refer for parathyroidectomy when severe HPT remains refractory to appropriate medical/pharmacologic therapy or when autonomous tertiary disease produces clinically important persistent hypercalcemia/end-organ consequences despite appropriate medical management. The surgical indication should reflect refractory disease burden—not merely gland size on imaging or a single elevated PTH result."
        ),
        "operate": (
            "Operate as a MULTIGLAND disease. Common renal-HPT strategies are subtotal parathyroidectomy (leaving a deliberately measured vascularized remnant) or total parathyroidectomy with autotransplantation; institutional practice and transplant status influence the choice. Perform a systematic four-gland exploration, search predictable ectopic/supernumerary sites when a gland is missing, and consider cervical thymectomy when indicated because supernumerary/intrathymic tissue can drive persistence. Mark/document the retained remnant or autograft so future recurrence can be approached rationally. The major immediate postoperative hazard is HUNGRY BONE SYNDROME: abrupt PTH withdrawal permits avid skeletal uptake of calcium, phosphate and magnesium after prolonged high-turnover bone disease. Anticipate frequent calcium monitoring and aggressive calcium plus active-vitamin-D replacement rather than treating postoperative hypocalcemia as an unexpected complication."
        ),
        "teach": (
            "Chief/boards framework: CKD -> phosphate/vitamin-D/calcium disturbance -> diffuse multigland stimulation = SECONDARY HPT; prolonged stimulation -> nodular/autonomous secretion, often with hypercalcemia (especially post-transplant) = TERTIARY HPT. Do not diagnose or localize renal HPT from a sestamibi focus. First correct modifiable CKD-MBD drivers and use calcimimetic/vitamin-D therapy appropriately; KDIGO suggests parathyroidectomy for severe CKD G3a-G5D HPT that fails medical/pharmacologic therapy. At surgery think FOUR GLANDS + SUPERNUMERARY/THYMIC TISSUE + REMNANT/AUTOGRAFT PLAN. After surgery think HUNGRY BONE early and aggressively. Contrast: PRIMARY HPT asks 'which autonomous gland?'; RENAL HPT asks 'how severe is the systemic multigland disease, has medical therapy failed, and how much functioning tissue should remain?'"
        ),
        "tags": [
            "secondary hyperparathyroidism", "tertiary hyperparathyroidism", "renal hyperparathyroidism",
            "CKD-MBD", "calcimimetic", "cinacalcet", "subtotal parathyroidectomy",
            "total parathyroidectomy autotransplantation", "supernumerary parathyroid", "cervical thymectomy",
            "hungry bone syndrome", "renal transplant"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — renal hyperparathyroidism, multigland parathyroid surgery, ectopic/supernumerary anatomy and postoperative hypocalcemia",
            "K.J. Lee's Essential Otolaryngology, 12e — parathyroid physiology and operative management of multigland hyperparathyroidism",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — practical secondary/tertiary hyperparathyroidism and parathyroidectomy pearls",
            "KDIGO 2017 Clinical Practice Guideline Update for CKD-MBD — serial PTH interpretation, correction of modifiable factors, dialysis PTH-lowering therapy and recommendation 4.2.5 for parathyroidectomy in severe medically refractory CKD G3a-G5D hyperparathyroidism",
            "KDIGO CKD-MBD Controversies Conference Report 2025 — contemporary emphasis on individualized CKD-MBD management and persistent evidence gaps"
        ],
    },
}


def apply_renal_hpt_rebuild_v312(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = RENAL_HPT_REBUILD_V312.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v312"] = True
        module["semantic_role_v312"] = "CKD-MBD multigland physiology, refractory-disease selection, renal parathyroidectomy strategy, and hungry-bone management"
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
