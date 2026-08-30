"""v30.9 — source-grounded head-and-neck cutaneous melanoma rebuild.

The duplicate audit flags cutaneous melanoma against head-and-neck cSCC. They share a
cutaneous site, but the oncologic decision models are different: melanoma is driven by
Breslow depth/ulceration, sentinel-node staging, stage and molecular biology, whereas
cSCC emphasizes local high-risk features, perineural spread and parotid/neck metastatic
risk. This patch keeps those pathways clinically distinct.
"""

import re

DOMAIN = "Head & Neck Oncology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


CUTANEOUS_MELANOMA_V309 = {
    "cutaneous melanoma of the head neck": {
        "recognize": (
            "Recognize HEAD-AND-NECK CUTANEOUS MELANOMA as a melanocytic malignancy whose first resident-level "
            "questions are Breslow depth, ulceration, nodal status and stage—not the cSCC checklist of perineural "
            "invasion and parotid-risk features. Suspicious lesions may follow ABCDE change (asymmetry, border "
            "irregularity, color variation, diameter/evolution), but nodular melanoma may present as a rapidly "
            "growing relatively symmetric papule or nodule. Biopsy establishes diagnosis. Head-and-neck sites "
            "have complex lymphatic drainage and can map to parotid/intraparotid, upper cervical, occipital or "
            "postauricular basins, so the primary site alone does not reliably predict a single first-echelon node."
        ),
        "localize": (
            "Localize the PRIMARY and the LYMPHATIC BASIN separately. Record exact cutaneous subsite, prior biopsy "
            "scar, proximity to eyelid/nose/lip/ear/scalp structures and whether a definitive resection can preserve "
            "function. For staging, the pathology map matters more than surface diameter alone: Breslow thickness "
            "and ulceration drive the T category, while clinically occult nodal disease is staged with sentinel "
            "lymph-node biopsy when indicated. In the head and neck, preoperative lymphoscintigraphy and often "
            "SPECT/CT help identify unexpected drainage, including intraparotid sentinel nodes. Do not substitute "
            "an elective neck dissection template for actual sentinel-node mapping."
        ),
        "workup": (
            "Obtain a COMPLETE EXCISIONAL BIOPSY with narrow margins when anatomically feasible so Breslow depth, "
            "ulceration and other staging features can be measured accurately; partial sampling is reasonable when "
            "a complete diagnostic excision would create major functional/cosmetic morbidity, but the specimen must "
            "be deep enough to avoid transecting the lesion if possible. Review Breslow thickness, ulceration, "
            "mitotic activity and margin status and perform a focused skin and nodal examination. Routine systemic "
            "imaging is not required for every thin clinically node-negative melanoma. For clinically suspicious "
            "nodes, obtain tissue confirmation and stage appropriately. Discuss sentinel-node biopsy for T1b lesions "
            "and generally offer it for clinically node-negative melanomas >1 mm when the result would affect staging "
            "or treatment; individualize in very thin or frail patients. Molecular testing, especially BRAF V600, "
            "becomes important in resected high-risk/advanced disease when it can change systemic therapy."
        ),
        "manage": (
            "Definitive local therapy is WIDE LOCAL EXCISION with margins based on Breslow thickness rather than a "
            "single head-and-neck skin-cancer margin: melanoma in situ generally 0.5-1 cm; invasive melanoma <=1 mm "
            "uses 1 cm; >1-2 mm uses 1-2 cm; and >2 mm uses 2 cm when anatomy permits. Coordinate SLNB at the time of "
            "wide excision when indicated because prior rearrangement can disrupt lymphatic mapping. A positive SLN "
            "does not automatically mandate completion neck/parotid dissection; modern management commonly uses "
            "active nodal-basin ultrasound surveillance with multidisciplinary systemic-therapy planning. Resected "
            "stage IIB/IIC and stage III disease may merit adjuvant anti-PD-1 therapy; BRAF V600-mutant stage III "
            "disease may also have a BRAF/MEK targeted option. Unresectable/metastatic disease is managed by melanoma "
            "stage, immune-therapy strategy and actionable biology—not by the advanced-cSCC cemiplimab pathway."
        ),
        "operate": (
            "Plan the definitive operation only after the diagnostic pathology establishes depth. Mark the biopsy "
            "scar and planned Breslow-based radial margin, then carry the excision through the subcutaneous tissue "
            "to the appropriate deep anatomic plane; unnecessarily sacrificing deep fascia is not required when it "
            "is uninvolved. If SLNB is indicated, obtain lymphatic mapping before wide local rearrangement and use "
            "the mapped basin rather than guessing from neck level. Intraparotid sentinel nodes require facial-nerve-"
            "aware dissection and are not equivalent to an automatic formal parotidectomy. Reconstruct only after "
            "oncologic geometry and margin strategy are clear; on the scalp, nose, eyelid or ear, staged reconstruction "
            "may be useful when margin certainty is limited. Therapeutic nodal surgery is reserved for clinically "
            "evident/resectable regional disease selected in a multidisciplinary melanoma pathway."
        ),
        "teach": (
            "Chief/boards discriminator: MELANOMA = BRESLOW + ULCERATION + SENTINEL NODE + STAGE/BIOLOGY. cSCC = "
            "LOCAL HIGH-RISK FEATURES + PNI + PAROTID/NECK metastatic-risk reasoning. For melanoma, do not perform a "
            "wide definitive excision before obtaining a biopsy that can establish Breslow depth; do not use lesion "
            "diameter to choose the excision margin; and do not replace SLNB with an elective neck dissection. Know "
            "the practical margin ladder (in situ 0.5-1 cm; <=1 mm 1 cm; >1-2 mm 1-2 cm; >2 mm 2 cm), the T1b SLNB "
            "discussion threshold, complex head-and-neck lymphatic mapping, and the post-MSLT-II principle that a "
            "positive sentinel node is not synonymous with mandatory completion lymph-node dissection."
        ),
        "tags": [
            "cutaneous melanoma", "Breslow thickness", "ulceration", "sentinel lymph node biopsy",
            "SLNB", "lymphoscintigraphy", "SPECT CT", "parotid sentinel node", "BRAF V600",
            "anti-PD-1", "wide local excision"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — head-and-neck cutaneous melanoma, lymphatic mapping, surgery and regional disease",
            "K.J. Lee's Essential Otolaryngology, 12e, Ch. 42 — Cutaneous Malignancies of the Head and Neck / melanoma",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Cutaneous Malignancies / melanoma",
            "NCCN Clinical Practice Guidelines in Oncology: Melanoma: Cutaneous, Version 2.2026 (Apr 17, 2026) — biopsy, Breslow-based excision margins, SLNB, stage-directed adjuvant/systemic therapy",
            "ASCO/SSO Clinical Practice Guideline Update — sentinel lymph node biopsy and regional nodal management in melanoma; completion dissection is not routine after a positive SLN",
        ],
    },
}


def apply_cutaneous_melanoma_rebuild_v309(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = CUTANEOUS_MELANOMA_V309.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v309"] = True
        module["semantic_role_v309"] = "melanoma_breslow_slnb_stage_biology_pathway"
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
