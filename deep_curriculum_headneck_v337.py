"""v33.7 — source-grounded cutaneous head-and-neck melanoma separation.

The duplicate audit flags cutaneous melanoma against cutaneous H&N cSCC because both cards can
collapse into generic skin-cancer surgery. v33.5 already rebuilt cSCC around perineural,
parotid/neck and immunosuppression risk. This patch gives melanoma a distinct resident/chief job:
Breslow/ulceration-driven staging, melanoma-specific margin and sentinel-node decisions,
head-and-neck lymphatic mapping, and modern adjuvant/systemic therapy pathways.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


CUTANEOUS_MELANOMA_REBUILD_V337 = {
    "cutaneous melanoma of the head neck": {
        "recognize": (
            "Use this card for CUTANEOUS MELANOMA OF THE HEAD AND NECK, not mucosal melanoma and not cSCC. "
            "The first biopsy must preserve the variables that drive staging: Breslow thickness, ulceration, margin status, "
            "and other adverse histologic features. A changing asymmetric pigmented lesion, amelanotic lesion, recurrent lesion, "
            "or melanoma arising on chronically sun-damaged facial/scalp skin should trigger a biopsy strategy that permits accurate "
            "microstaging. Do not transfer cSCC risk logic directly: melanoma prognosis and regional staging are dominated by tumor "
            "thickness/ulceration and nodal status rather than routine perineural/parotid-risk heuristics."
        ),
        "localize": (
            "Map the PRIMARY SITE and the LYMPHATIC BASIN separately. Head-and-neck drainage is less predictable than trunk/extremity "
            "melanoma and may involve parotid, upper cervical, occipital or postauricular basins, sometimes with multiple drainage pathways. "
            "For a clinically node-negative patient in whom sentinel lymph-node biopsy is indicated, perform lymphatic mapping rather than "
            "assuming a standard neck level. Distinguish cutaneous facial/scalp melanoma from sinonasal/oral mucosal melanoma because staging, "
            "biology and treatment evidence differ."
        ),
        "workup": (
            "Obtain a diagnostic biopsy deep enough for Breslow measurement; excisional biopsy with narrow clinical margins is preferred when "
            "feasible, while a carefully chosen incisional/punch approach is reasonable for large or anatomically constrained facial lesions. "
            "Stage using AJCC 8th principles: T1a is <0.8 mm without ulceration; T1b includes <0.8 mm with ulceration or 0.8-1.0 mm with or without "
            "ulceration. Discuss sentinel-node biopsy for clinically node-negative melanoma at least 0.8 mm thick and for selected thinner ulcerated/"
            "otherwise high-risk lesions; it is routinely considered more strongly once thickness exceeds 1 mm. Palpable or radiographically suspicious "
            "nodes are not a sentinel-node problem—sample/stage them directly. Cross-sectional or systemic staging is risk- and stage-directed rather than "
            "automatic for every thin melanoma."
        ),
        "manage": (
            "Localized cutaneous melanoma is treated with wide local excision using thickness-based radial margins while respecting critical head-and-neck "
            "function: at least 5 mm for melanoma in situ with wider margins sometimes required (especially lentigo maligna), about 1 cm for invasive melanoma "
            "<=1 mm, 1-2 cm for 1.01-2 mm lesions, and 2 cm for lesions >2 mm when anatomically feasible. A positive sentinel node no longer mandates routine "
            "completion lymph-node dissection; nodal-basin ultrasound surveillance plus melanoma-directed adjuvant therapy is often appropriate after multidisciplinary "
            "review. Modern adjuvant systemic therapy includes anti-PD-1 therapy for resected stage IIB/IIC and stage III disease; BRAF V600-mutated stage III disease "
            "also has a BRAF/MEK targeted option. Resectable bulky stage IIIB-IV disease may enter a neoadjuvant systemic-therapy pathway in melanoma oncology."
        ),
        "operate": (
            "OPERATIVE SEQUENCE: obtain accurate microstaging first -> plan wide local excision from Breslow thickness -> coordinate lymphoscintigraphy/sentinel-node "
            "mapping when indicated -> remove mapped sentinel nodes through incisions that preserve future parotid/neck options -> reconstruct only after oncologic margins "
            "are secured. On the eyelid, nose, ear and lip, function can constrain the geometric margin, but the response is multidisciplinary margin-controlled planning rather "
            "than silently substituting a narrower oncologic goal. In parotid-basin sentinel-node surgery, protect the facial nerve and remember that the mapped node may lie within "
            "or adjacent to parotid tissue. Therapeutic nodal surgery is reserved for clinically evident or otherwise appropriately selected regional disease; do not perform an "
            "elective cSCC-style parotidectomy/neck dissection simply because the primary is on the lateral face or scalp."
        ),
        "teach": (
            "Chief/boards discriminator: MELANOMA = BRESLOW + ULCERATION + SENTINEL-NODE BIOLOGY. cSCC = PNI/PAROTID/NECK RISK. For melanoma, know the 0.8-mm AJCC/SLNB "
            "threshold, thickness-based excision margins, unpredictable head-and-neck lymphatic drainage, and the fact that positive SLNB is a staging/adjuvant-therapy event rather "
            "than an automatic completion-dissection order. Keep adjuvant therapy current: anti-PD-1 is established for resected stage IIB/IIC and stage III disease, and BRAF V600 "
            "status can create a targeted adjuvant option in stage III."
        ),
        "tags": [
            "cutaneous melanoma", "head and neck melanoma", "Breslow thickness", "ulceration", "AJCC 8", "sentinel lymph node biopsy",
            "lymphoscintigraphy", "parotid sentinel node", "wide local excision", "lentigo maligna", "anti-PD-1", "BRAF V600"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — malignant melanoma of the head and neck, biopsy, regional drainage and operative management",
            "K.J. Lee's Essential Otolaryngology, 12e — Chapter 43 Malignant Melanoma of the Head and Neck; Breslow staging, regional disease and treatment principles",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — melanoma recognition, staging and head-and-neck oncologic framework",
            "NCI Melanoma Treatment (PDQ), current through 2026 — AJCC 8 T1 definitions, thickness-based excision margins and SLNB consideration at >=0.8 mm",
            "ASCO Systemic Therapy for Melanoma Guideline Update (2023, current practice basis) — adjuvant anti-PD-1 for stage IIB/IIC and stage III; neoadjuvant pembrolizumab for resectable stage IIIB-IV",
            "FDA October 13 2023 — nivolumab approved for adjuvant treatment of completely resected stage IIB/IIC melanoma",
            "MSLT-II evidence incorporated into contemporary melanoma management — positive SLNB does not require routine completion lymph-node dissection",
        ],
    },
}


def apply_cutaneous_melanoma_rebuild_v337(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = CUTANEOUS_MELANOMA_REBUILD_V337.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v337"] = True
            module["semantic_role_v337"] = (
                "cutaneous melanoma microstaging, Breslow-driven excision, sentinel-node mapping and melanoma-specific adjuvant/systemic pathway"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
