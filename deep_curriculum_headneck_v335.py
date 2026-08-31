"""v33.5 — source-grounded cutaneous H&N SCC versus BCC separation.

The duplicate audit flags these cards because their titles and generic skin-cancer language overlap.
This patch keeps both but assigns different resident/chief jobs: cSCC owns aggressive-risk
stratification, perineural/parotid-neck spread, nodal management and systemic escalation; BCC
owns local-destructive risk, margin-controlled tissue-preserving treatment and advanced BCC
hedgehog/immunotherapy pathways. Later modules may supersede these cards intentionally.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


CUTANEOUS_HN_REBUILD_V335 = {
    "cutaneous squamous cell carcinoma of the head neck": {
        "recognize": (
            "Use this card for CUTANEOUS SCC OF THE HEAD AND NECK, not mucosal HNSCC and not BCC. "
            "The central question is whether a skin primary has features that make LOCAL, PERINEURAL, "
            "PAROTID or CERVICAL NODAL failure likely. Record site, size, depth, differentiation, recurrence, "
            "host immunosuppression, prior radiation, rapid growth, pain/numbness or motor deficit, and whether "
            "the lesion reaches cartilage, bone, parotid, orbit or a named nerve. A small primary can still be "
            "high risk when biology or anatomy is unfavorable."
        ),
        "localize": (
            "Localize beyond the skin defect. Map the primary relative to ear/temple/scalp/forehead/cheek/lip, "
            "the expected parotid and cervical drainage basin, and any sensory or motor nerve symptoms. Clinical "
            "perineural spread may track along trigeminal or facial nerve branches toward skull base; parotid "
            "nodes are a key regional basin for many lateral facial/scalp primaries. Distinguish microscopic PNI "
            "reported on pathology from symptomatic or radiographic named-nerve spread, because the latter changes "
            "imaging, operative planning and adjuvant treatment much more substantially."
        ),
        "workup": (
            "Biopsy deeply enough to establish invasive cSCC and permit risk assessment. Perform a deliberate skin, "
            "parotid and neck examination. Use risk stratification rather than diameter alone: BWH staging is useful "
            "for localized prognostication, while NCCN-style risk groups guide practical management. In a genuinely "
            "high-risk tumor, clinically suspicious nodes, parotid fullness, deep fixation or neurologic symptoms, "
            "obtain targeted cross-sectional imaging; MRI with contrast is preferred when meaningful perineural spread "
            "toward skull base is suspected. Sample suspicious parotid/neck nodes rather than assuming they are reactive."
        ),
        "manage": (
            "For resectable disease, surgery with complete margin assessment is the foundation. Mohs or another "
            "margin-controlled technique is particularly useful for selected high-risk facial tumors where tissue "
            "preservation and complete peripheral/deep margin control matter; conventional excision remains appropriate "
            "when oncologic margins and reconstruction can be achieved reliably. Multidisciplinary discussion is warranted "
            "for major PNI, recurrent disease, bone invasion, parotid/neck metastasis, immunosuppressed hosts or lesions "
            "requiring complex reconstruction. Adjuvant radiation is considered when adverse pathology or regional disease "
            "creates substantial recurrence risk. Advanced disease not curable with surgery/radiation has established PD-1/"
            "PD-L1-directed systemic options; current practice also includes FDA-approved adjuvant cemiplimab after surgery "
            "and radiation for appropriately defined high-risk cSCC."
        ),
        "operate": (
            "Operate by ONCOLOGIC COMPARTMENT. Clear the primary with an assessable deep plane; do not let the planned flap "
            "dictate an inadequate margin. When nodal disease involves the parotid/neck, treat the involved regional basin "
            "with the appropriate parotidectomy and neck-dissection strategy based on distribution and facial-nerve involvement, "
            "while preserving uninvolved nerve when oncologically sound. For gross named-nerve perineural spread, plan proximal "
            "nerve control and skull-base extent from preoperative imaging rather than discovering it after margin failure. "
            "Reconstruction follows margin clearance and should restore eyelid, oral competence, auricular/scalp coverage and "
            "nerve function as needed without obscuring surveillance."
        ),
        "teach": (
            "Chief/boards discriminator: H&N cSCC is the NONMELANOMA SKIN CANCER in which you must think beyond the primary "
            "lesion to PERINEURAL + PAROTID + NECK risk. Do not apply mucosal-SCC staging/HPV logic. Pain, numbness, facial weakness, "
            "recurrent tumor, poor differentiation, deep invasion and immunosuppression should lower the threshold for advanced "
            "workup. BWH is useful for localized prognostication; practical treatment is risk-stratified. Surgery is the local-control "
            "backbone, adjuvant RT is selected for adverse disease, and modern immunotherapy matters in advanced and now selected "
            "high-risk adjuvant settings."
        ),
        "tags": [
            "cutaneous squamous cell carcinoma", "head and neck skin cancer", "BWH staging", "perineural invasion",
            "perineural spread", "parotid metastasis", "neck metastasis", "Mohs", "adjuvant radiation", "cemiplimab"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — cutaneous head-and-neck malignancy, regional spread, perineural disease, parotid/neck management and reconstruction",
            "K.J. Lee's Essential Otolaryngology, 12e — cutaneous malignancy and facial/head-and-neck oncologic surgery principles",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — cutaneous SCC/BCC distinctions, Mohs concepts and regional head-and-neck management",
            "American Academy of Dermatology guideline for cutaneous squamous cell carcinoma — BWH prognostication, NCCN risk stratification and surgery as treatment foundation",
            "FDA, October 8 2025 — cemiplimab-rwlc approved as adjuvant therapy for adults with high-risk cSCC after surgery and radiation",
            "FDA — cemiplimab, pembrolizumab and cosibelimab indications for selected locally advanced/metastatic cSCC not curable by surgery or radiation",
        ],
    },
    "basal cell carcinoma of the head neck": {
        "recognize": (
            "Use this card for BASAL CELL CARCINOMA OF THE HEAD AND NECK. Unlike cSCC, the dominant threat is usually relentless "
            "LOCAL DESTRUCTION rather than routine nodal or distant metastasis. Recognize classic pearly/telangiectatic or ulcerated "
            "lesions but confirm histology; note recurrence, ill-defined borders, aggressive infiltrative/morpheaform/micronodular "
            "pattern, prior radiation and perineural symptoms. Central-face H-zone sites such as nose, periocular region, lips and ears "
            "deserve particular respect because small tumors can create major functional defects and may have subclinical extension."
        ),
        "localize": (
            "Map the lesion to the functional subunit it threatens: eyelid/canthus/lacrimal system, nasal ala/tip/sidewall, lip, ear/EAC, "
            "scalp or cheek. Determine whether disease remains cutaneous or invades cartilage, bone, orbit, parotid/temporal bone or a "
            "named nerve. Do NOT perform routine parotid/neck staging for an otherwise typical BCC; nodal spread is exceptional. Neurologic "
            "symptoms, fixation, recurrent deeply infiltrative disease or major size should instead trigger focused imaging for local and "
            "perineural extent."
        ),
        "workup": (
            "Biopsy to establish BCC subtype and depth sufficiently for treatment planning. Risk-stratify by anatomic site, size, border "
            "definition, recurrence, immunosuppression, prior radiation, aggressive histology and PNI. Most routine BCC requires no systemic "
            "staging. Use CT/MRI selectively for suspected bone, orbit, temporal-bone or named-nerve involvement. In periocular or auricular "
            "disease, explicitly assess the adjacent functional structures before choosing a margin strategy; an apparently small surface "
            "lesion may require a complex reconstruction if those structures are involved."
        ),
        "manage": (
            "Surgery is the treatment cornerstone. Favor margin-controlled surgery such as Mohs for many high-risk facial BCCs, recurrent "
            "tumors, ill-defined lesions and sites where maximal tissue preservation is functionally important; conventional excision is "
            "appropriate for selected lower-risk lesions when complete margins can be achieved. Superficial low-risk disease may have "
            "nonsurgical options, but cure rates are generally lower and those approaches are not substitutes for adequate surgery in an "
            "infiltrative H-zone tumor. Radiation can be definitive or adjuvant in selected patients who are poor surgical candidates or have "
            "high-risk residual/perineural disease. For unresectable or functionally devastating locally advanced BCC, multidisciplinary "
            "systemic therapy may use Hedgehog-pathway inhibition; PD-1 therapy is an established option in selected advanced disease after "
            "Hedgehog-inhibitor failure/intolerance or when it is not appropriate."
        ),
        "operate": (
            "The operative objective is COMPLETE MARGIN CONTROL WITH MAXIMAL FUNCTION PRESERVATION. On the nose, eyelid, lip and ear, plan "
            "margin clearance before committing to reconstruction; staged or Mohs margin assessment often prevents both undertreatment and "
            "unnecessarily large sacrifice. If tumor reaches cartilage, bone, lacrimal structures, orbit or temporal bone, escalate the resection "
            "to the involved compartment rather than repeatedly shaving a positive deep margin. Reconstruction should respect facial subunits, "
            "eyelid support, nasal valve/airway, oral competence and auricular/EAC patency. Routine elective neck dissection is not a BCC operation."
        ),
        "teach": (
            "Chief/boards discriminator: BCC is COMMON and usually METASTATICALLY QUIET but can be LOCALLY DEVASTATING. The management problem "
            "is margin control plus tissue preservation, especially in the facial H-zone—not prophylactic nodal surgery. Mohs is valuable when "
            "subclinical extension and preservation of eyelid, nose, lip or ear matter. Aggressive/recurrent disease can track deeply or along nerves, "
            "so local indolence should not be confused with harmlessness. Keep the systemic pathways straight: advanced BCC is classically Hedgehog-"
            "driven treatment territory, with PD-1 therapy available for selected patients; that is different from the nodal/parotid and immunotherapy "
            "logic emphasized in cSCC."
        ),
        "tags": [
            "basal cell carcinoma", "head and neck skin cancer", "Mohs", "H zone", "periocular BCC", "nasal BCC",
            "margin control", "Hedgehog inhibitor", "vismodegib", "sonidegib", "cemiplimab"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — facial cutaneous malignancy, margin-controlled excision and reconstructive principles",
            "K.J. Lee's Essential Otolaryngology, 12e — cutaneous malignancy and facial reconstructive surgery principles",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — BCC epidemiology, rare metastasis and Mohs treatment of high-risk facial sites",
            "American Academy of Dermatology guideline for basal cell carcinoma — NCCN-style risk stratification, surgery as cornerstone and lower cure rates for nonsurgical options",
            "AAD Mohs Appropriate Use Criteria — tumor type, location, recurrence and patient factors inform appropriateness of Mohs surgery",
            "FDA-approved advanced BCC pathway — Hedgehog-pathway inhibitors and cemiplimab for selected locally advanced/metastatic disease",
        ],
    },
}


def apply_cutaneous_hn_rebuild_v335(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = CUTANEOUS_HN_REBUILD_V335.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v335"] = True
            module["semantic_role_v335"] = (
                "cutaneous SCC risk stratification, perineural/parotid-neck spread and multidisciplinary oncologic escalation"
                if key == "cutaneous squamous cell carcinoma of the head neck"
                else "basal-cell local-control risk, margin-controlled facial treatment and advanced BCC systemic pathway"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
