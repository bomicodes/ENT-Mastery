"""v37.3: operational DTC risk stratification, RAI selection and response-driven TSH.

2025 ATA-aligned teaching. Append only; safe to apply repeatedly.
Reference: 2025 ATA adult DTC guideline, recommendations 28, 32, 45-46,
Tables 9-10: https://pmc.ncbi.nlm.nih.gov/articles/PMC13090833/
"""
import re

TOPIC_KEY = "differentiated thyroid cancer"

RISK_CRITERIA_ADDENDUM = (
    " RISK-BAND CRITERIA (2025 ATA): classify the final pathology using the four "
    "2025 recurrence-risk bands: LOW (<10%), LOW-INTERMEDIATE (10-15%), "
    "INTERMEDIATE-HIGH (16-30%), and HIGH (>30%). An intrathyroidal "
    "well-differentiated tumor without clinically meaningful vascular invasion, "
    "aggressive histology, gross extension, significant nodal burden, or distant "
    "metastases generally favors low risk. Microscopic extension, aggressive "
    "histology, vascular invasion, nodal metastasis number/size, extranodal "
    "extension and postoperative findings can shift classification across the "
    "two intermediate bands; gross extrathyroidal extension, distant metastasis, "
    "large-volume nodal disease, or substantial residual disease raise concern "
    "for high risk. Use the histology-specific 2025 ATA risk table/algorithm "
    "rather than treating this abbreviated feature list as an exhaustive "
    "one-feature-to-one-band rule; distinguish recurrence risk from AJCC stage."
)

RAI_CANDIDACY_ADDENDUM = (
    " WHO IS ACTUALLY OFFERED RAI (2025 ATA recommendation 32): after total "
    "thyroidectomy, do not routinely give remnant ablation for ATA low-risk "
    "DTC; consider adjuvant RAI for low-intermediate or intermediate-high risk "
    "based on pathology, postoperative thyroglobulin/anti-Tg, imaging, patient "
    "preferences, and anticipated benefit; routinely recommend RAI for "
    "high-risk disease and for distant metastases when appropriate. RAI is not "
    "routine after lobectomy; completion thyroidectomy may be considered if "
    "RAI is indicated. Appropriately selected low-risk papillary microcarcinoma "
    "may be observed with active surveillance or treated surgically without "
    "RAI. Discuss salivary/lacrimal toxicity, marrow effects, reproductive "
    "precautions and potential second malignancies. Pregnancy and lactation "
    "preclude RAI administration; check pregnancy status, ensure lactation has "
    "ceased for the guideline-recommended interval, and plan low-iodine "
    "preparation and TSH stimulation by withdrawal or rhTSH when appropriate."
)

TSH_RESPONSE_ADDENDUM = (
    " POSTOPERATIVE TSH TARGET AND DYNAMIC RISK RESPONSE (2025 ATA "
    "recommendations 45-46, Table 9): individualize initial suppression "
    "according to recurrence risk, persistent disease, and harms such as "
    "atrial fibrillation and osteoporosis; do not automatically apply older "
    "fixed numeric goals (<0.1, 0.1-0.5, 0.5-2 mIU/L) to every 2025 ATA "
    "patient. Reassess response over time. EXCELLENT = negative imaging and "
    "appropriately low thyroglobulin for treatment received (after total "
    "thyroidectomy plus RAI: nonstimulated Tg <0.2 or stimulated Tg <1 ng/mL; "
    "thresholds differ without RAI or after lobectomy). INDETERMINATE = "
    "nonspecific imaging or low-level Tg/stable or declining anti-Tg antibodies. "
    "BIOCHEMICALLY INCOMPLETE = elevated Tg or increasing antibodies without "
    "structural disease. STRUCTURALLY INCOMPLETE = persistent/recurrent "
    "structural disease regardless of Tg. TSH is generally targeted within "
    "the normal reference range for excellent or indeterminate response and "
    "may be targeted below the reference range for biochemical or structural "
    "incomplete response, balancing progression risk against suppression "
    "toxicity. Long-term suppression is not suggested for low/intermediate "
    "risk with no biochemical or structural recurrence. Indeterminate "
    "findings generally prompt surveillance, but rising Tg or new disease "
    "requires renewed assessment; further RAI is not categorically prohibited."
)


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def apply_dtc_rai_criteria_v373(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            if _norm(module.get("topic")) != TOPIC_KEY:
                continue
            workup = module.get("workup", "") or ""
            if "RISK-BAND CRITERIA" not in workup:
                module["workup"] = workup.rstrip() + RISK_CRITERIA_ADDENDUM
            manage = module.get("manage", "") or ""
            if "WHO IS ACTUALLY OFFERED RAI" not in manage:
                manage = manage.rstrip() + RAI_CANDIDACY_ADDENDUM
            if "DYNAMIC RISK RESPONSE" not in manage:
                manage = manage.rstrip() + TSH_RESPONSE_ADDENDUM
            module["manage"] = manage
            tags = module.setdefault("tags", [])
            for tag in ("RAI candidacy", "ATA risk criteria", "TSH suppression targets",
                        "dynamic risk response", "excellent response", "structural incomplete response"):
                if tag not in tags:
                    tags.append(tag)
            patched.append(module.get("topic"))
    if not patched:
        raise RuntimeError("v37.3: could not find the canonical Differentiated Thyroid Cancer topic")
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
