"""v30.8 — source-grounded cutaneous SCC vs basal-cell carcinoma separation.

The duplicate audit flags head-and-neck cSCC <-> BCC. Both are keratinocyte cancers, but
they are not one "nonmelanoma skin cancer" concept: cSCC demands explicit perineural,
parotid/neck metastatic-risk reasoning, whereas BCC is primarily a local-control and
tissue-preservation problem with metastatic disease being exceptional.
"""

import re

DOMAIN = "Head & Neck Oncology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


CUTANEOUS_ONCOLOGY_V308 = {
    "cutaneous squamous cell carcinoma of the head neck": {
        "recognize": (
            "Recognize HEAD-AND-NECK CUTANEOUS SCC (cSCC) as a keratinocyte carcinoma whose key "
            "resident-level question is not merely whether the lesion can be excised, but whether it "
            "has biologic features that predict recurrence, perineural spread, parotid/neck metastasis, "
            "or skull-base progression. Typical lesions are keratotic, ulcerated, indurated, tender, "
            "bleeding, or rapidly enlarging, but biopsy establishes diagnosis. Escalate concern with "
            "recurrence, immunosuppression, poor differentiation, substantial depth/invasion beyond "
            "subcutaneous fat, large-caliber or clinically evident perineural invasion, ear/lip or other "
            "high-risk head-and-neck location, rapid growth, fixation, neurologic symptoms, or bone "
            "invasion. Do not import BCC's overwhelmingly local behavior into cSCC."
        ),
        "localize": (
            "Map the primary in three dimensions and map its LYMPHATIC + NEURAL escape routes. Record "
            "site, size, depth, mobility/fixation, relationship to cartilage/bone, and named-nerve symptoms. "
            "For temple, forehead, scalp, auricular and lateral-face disease, examine the parotid and "
            "appropriate cervical nodal basins; drainage patterns vary by site, so a normal-looking primary "
            "scar does not end the exam. Facial numbness, pain, paresthesia, weakness, or multiple cranial-"
            "nerve findings should trigger concern for clinical perineural spread along V or VII toward the "
            "skull base. Keep AJCC 8 head-and-neck cSCC staging distinct from Brigham and Women's Hospital "
            "(BWH) risk stratification: they answer related but nonidentical prognostic questions."
        ),
        "workup": (
            "Obtain a biopsy deep enough to characterize invasive tumor and request pathology details that "
            "change risk: differentiation, depth/thickness when reported, invasion beyond subcutaneous fat, "
            "perineural invasion including nerve caliber/clinical correlation, lymphovascular invasion, and "
            "margin status. Routine imaging is unnecessary for every small low-risk cSCC, but high-risk, "
            "deep/fixed, recurrent, clinically node-positive, or neurologically symptomatic disease deserves "
            "risk-directed imaging. Contrast CT is useful for nodal/parotid and bony disease; MRI with "
            "appropriate skull-base/nerve coverage is favored when substantial or clinical perineural spread "
            "is suspected. Ultrasound/FNA or core biopsy can confirm suspicious parotid/neck nodes. Use BWH "
            "risk stratification for localized prognostication rather than treating all cSCCs as equivalent."
        ),
        "manage": (
            "Surgery is the curative backbone for most resectable cSCC. Use margin-controlled surgery such "
            "as Mohs when exhaustive margin assessment and tissue preservation are especially valuable, or "
            "wide excision when oncologic geometry/reconstruction makes that preferable. High-risk disease "
            "may require multidisciplinary postoperative radiation based on margin, PNI, recurrence, nodal "
            "disease, bone invasion and other adverse features. Established parotid or cervical metastasis "
            "requires therapeutic regional management rather than a BCC-style local excision alone, with "
            "adjuvant RT commonly considered according to burden/pathology. For disease not curable by "
            "surgery or radiation, immune-checkpoint therapy is a major systemic option. Current U.S. therapy "
            "also includes adjuvant cemiplimab for selected adults at high risk of recurrence after surgery "
            "and radiation; do not teach immunotherapy only as end-stage salvage."
        ),
        "operate": (
            "Plan resection around the likely routes of extension. Preserve function, but do not compromise "
            "deep or neural margins to simplify reconstruction. When a named nerve is grossly involved, "
            "define proximal extent and coordinate skull-base expertise if disease tracks centrally. For "
            "parotid metastasis, tailor parotidectomy to disease location/extent and protect or sacrifice "
            "facial nerve branches according to oncologic involvement rather than reflexively. Neck "
            "dissection levels are selected from primary site and nodal pattern; clinically involved regional "
            "disease is a therapeutic operation, not a sentinel concept borrowed from melanoma. Delay complex "
            "reconstruction when margin uncertainty would jeopardize re-excision, and select local/regional "
            "flaps or free tissue according to exposed nerve, bone, dura, vessel and anticipated radiation."
        ),
        "teach": (
            "Chief/boards discriminator: cSCC = LOCAL TUMOR + PERINEURAL RISK + PAROTID/NECK METASTATIC RISK. "
            "A numb cheek, facial weakness, recurrent temple lesion, parotid mass, immunosuppressed patient, "
            "or invasion beyond subcutaneous fat is not 'just another skin cancer.' BWH risk stratification "
            "is useful for localized prognostication; AJCC 8 provides the formal head-and-neck cSCC TNM "
            "framework. Image selectively when high-risk anatomy, nodal disease or perineural spread is "
            "suspected. Treat the regional basin when metastatic disease is present, and know that modern "
            "checkpoint therapy—including a 2025 U.S. adjuvant cemiplimab indication after surgery + RT in "
            "selected high-risk adults—has changed the advanced/high-risk treatment landscape."
        ),
        "tags": [
            "cutaneous SCC", "cSCC", "BWH staging", "AJCC8", "perineural invasion",
            "parotid metastasis", "neck metastasis", "Mohs", "cemiplimab"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — cutaneous malignancy risk stratification, perineural and regional metastatic disease",
            "K.J. Lee's Essential Otolaryngology, 12e, Ch. 42 — Cutaneous Malignancies of the Head and Neck",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Cutaneous Malignancies / Squamous Cell Carcinoma",
            "American Academy of Dermatology guideline of care for management of cutaneous squamous cell carcinoma — risk stratification and treatment",
            "U.S. FDA — cemiplimab indications for advanced cSCC and, since Oct 2025, adjuvant treatment after surgery and radiation in selected high-risk adults",
        ],
    },
    "basal cell carcinoma of the head neck": {
        "recognize": (
            "Recognize HEAD-AND-NECK BASAL CELL CARCINOMA (BCC) as the most common cutaneous malignancy and, "
            "in contrast with cSCC, primarily a problem of LOCAL DESTRUCTION, MARGIN CONTROL, and preservation "
            "of facial tissue/function. Classic morphology includes a pearly or translucent papule/plaque, "
            "telangiectasia, rolled border, ulceration, or a scar-like morpheaform lesion, but biopsy is required "
            "before definitive planning when diagnosis or subtype is uncertain. Risk rises with recurrence, "
            "poorly defined borders, aggressive/morpheaform or infiltrative histology, perineural involvement, "
            "large size, immunosuppression, prior radiation, and anatomically constrained high-risk facial sites. "
            "Metastasis is extraordinarily uncommon; do not give every BCC a cSCC-style nodal workup."
        ),
        "localize": (
            "Map BCC by the tissue it threatens: eyelid/canthus, nose, lip, ear, temple, scalp, cartilage, "
            "bone, orbit, and named nerves. On the central face and other high-risk anatomic zones, a small "
            "surface footprint can hide infiltrative extension and create major reconstructive consequences. "
            "Document prior treatment because recurrent tumors may have indistinct subclinical spread. Examine "
            "regional nodes as part of a complete cancer exam, but routine elective parotid/neck staging is not "
            "the governing pathway for ordinary BCC. Neurologic deficits, deep fixation, orbital symptoms or "
            "bone involvement are atypical red flags for advanced local/perineural disease and justify escalation."
        ),
        "workup": (
            "Biopsy enough of the lesion to establish BCC subtype and guide risk classification. For typical "
            "localized lesions, diagnosis plus careful clinical mapping is usually sufficient; do not reflexively "
            "order CT, PET, or neck imaging. Use imaging for unusually extensive, recurrent, fixed, orbital/bony, "
            "or clinically perineural disease when it will define resectability or reconstruction. Risk-stratify "
            "by anatomic location, size, borders, recurrence, histology and host factors. The key workup distinction "
            "from cSCC is what is usually absent: routine nodal-basin imaging, parotid staging, and metastatic "
            "evaluation. If a 'BCC' presents with a parotid mass or widespread nodes, confirm pathology and "
            "reconsider whether there is direct extension, rare metastatic BCC, or another cutaneous primary."
        ),
        "manage": (
            "Surgery remains the cornerstone. Favor Mohs or another complete margin-control strategy for recurrent, "
            "poorly defined, aggressive-histology or tissue-critical facial BCCs; standard excision is appropriate "
            "for selected lower-risk lesions when reliable margins and reconstruction are straightforward. Topical "
            "or destructive approaches belong to carefully selected superficial/low-risk disease and generally trade "
            "lower cure certainty for less invasive treatment. Radiation is an option when surgery is unsuitable or "
            "in selected advanced settings. For unresectable/locally advanced or metastatic BCC, Hedgehog-pathway "
            "inhibition (for example vismodegib/sonidegib according to indication) is disease-specific systemic "
            "therapy; cemiplimab is FDA-indicated after prior Hedgehog inhibitor or when a Hedgehog inhibitor is "
            "not appropriate. That systemic pathway is different from advanced cSCC."
        ),
        "operate": (
            "Choose the operation that maximizes reliable margin clearance while preserving critical facial units. "
            "Mohs is especially useful when millimeters matter around eyelid, nose, lip, ear and other constrained "
            "sites or when recurrent/infiltrative growth makes subclinical extension likely. With standard excision, "
            "orient the specimen and coordinate margin assessment before committing to reconstruction that would "
            "obscure a positive margin. Reconstruct by defect—not by diagnosis—using secondary intention, graft, "
            "local flap, regional flap or free tissue as needed, but restore eyelid support, nasal lining/framework, "
            "oral competence and auricular function deliberately. Routine elective parotidectomy or neck dissection "
            "has no role in ordinary localized BCC."
        ),
        "teach": (
            "Chief/boards discriminator: BCC = LOCAL CONTROL + TISSUE PRESERVATION; cSCC = add meaningful PNI and "
            "PAROTID/NECK metastatic reasoning. Both may deserve Mohs, but for different risk geometry, and neither "
            "should be reduced to a memorized margin number. A recurrent morpheaform BCC on the nose is a margin-"
            "control/reconstruction problem, not an automatic neck-dissection problem. Advanced BCC also has a "
            "distinct systemic ladder: Hedgehog-pathway inhibitor first when appropriate, then/otherwise cemiplimab "
            "under its current FDA indication. Reserve metastatic workup for exceptional clinical behavior rather "
            "than importing the cSCC algorithm into every BCC card."
        ),
        "tags": [
            "basal cell carcinoma", "BCC", "Mohs", "H-zone", "morpheaform",
            "local control", "Hedgehog inhibitor", "vismodegib", "cemiplimab"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — basal-cell carcinoma of the head and neck, margin control and reconstruction",
            "K.J. Lee's Essential Otolaryngology, 12e, Ch. 42 — Cutaneous Malignancies of the Head and Neck",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Cutaneous Malignancies / Basal Cell Carcinoma",
            "American Academy of Dermatology guideline of care for management of basal cell carcinoma — risk stratification and treatment",
            "U.S. FDA current cemiplimab label — locally advanced/metastatic BCC after Hedgehog-pathway inhibitor or when a Hedgehog inhibitor is not appropriate",
        ],
    },
}


def apply_cutaneous_oncology_rebuild_v308(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = CUTANEOUS_ONCOLOGY_V308.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v308"] = True
        module["semantic_role_v308"] = (
            "cutaneous_scc_perineural_parotid_neck_metastatic_risk_pathway"
            if _norm(module.get("topic")) == "cutaneous squamous cell carcinoma of the head neck"
            else "bcc_local_margin_control_tissue_preservation_pathway"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
