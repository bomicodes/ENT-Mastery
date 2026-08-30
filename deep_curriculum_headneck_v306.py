"""v30.6 — source-grounded oral tongue vs base-of-tongue SCC separation.

The duplicate audit flags Oral Tongue SCC <-> Base of Tongue SCC. These are not one
"tongue cancer" concept: oral tongue is oral-cavity SCC (anterior two thirds; DOI-driven
T staging and surgery/neck-first reasoning), whereas tongue base is oropharyngeal SCC
(p16/HPV biology, distinct staging, bilateral lymphatics, and transoral vs RT/CRT pathways).
"""

import re

DOMAIN = "Head & Neck Oncology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


TONGUE_SCC_V306 = {
    "oral tongue scc": {
        "recognize": (
            "Recognize ORAL TONGUE SCC as an ORAL-CAVITY cancer of the mobile anterior two thirds of the tongue, classically presenting with a persistent ulcer, indurated lesion, pain, dysarthria, bleeding, or referred otalgia. Do not confuse it with base-of-tongue/oropharyngeal SCC. Tobacco/alcohol exposure remains relevant, but p16 is not used as the site-defining staging surrogate that it is for HPV-mediated oropharyngeal SCC. The resident should immediately think local depth of invasion (DOI), floor-of-mouth proximity, mandibular relationship, intrinsic/extrinsic tongue involvement, and occult cervical nodal risk."
        ),
        "localize": (
            "Map anterior tongue subsite, laterality, distance from midline, floor-of-mouth extension, tongue musculature, mandible, and cervical nodes. Oral-cavity AJCC T staging incorporates DOI: DOI is measured from the basement membrane of adjacent normal mucosa to the deepest invasive front and is not the same as gross tumor thickness. Midline approach/crossing matters because lymphatic drainage can become bilateral. Imaging should define deep tongue/floor-of-mouth extent and nodal disease; the surgical map must anticipate whether a partial glossectomy can preserve speech/swallow or whether larger composite resection/reconstruction is required."
        ),
        "workup": (
            "Perform complete mucosal examination and flexible endoscopy to exclude synchronous disease, obtain biopsy, and stage the primary/neck with contrast CT or MRI as appropriate. Chest imaging and PET/CT are selected by stage/risk rather than ordered reflexively for every tiny lesion. Document dentition, nutrition, speech/swallow baseline, and reconstructive needs. For a surgically treated cN0 oral tongue cancer, do not ignore the neck: ASCO recommends ipsilateral elective neck dissection for cT2-4 cN0 disease and generally for cT1 cN0 disease, with surveillance reserved for carefully selected reliable patients in experienced programs."
        ),
        "manage": (
            "Treat most resectable oral-tongue SCC with surgery to the primary plus risk-appropriate neck management, then use pathology to decide adjuvant RT versus chemoradiation. Favor margin-negative resection with enough functional tongue preserved to maintain articulation and bolus control. Elective cN0 dissection generally includes ipsilateral levels I-III; a clinically positive neck requires a therapeutic dissection tailored to disease burden. Consider contralateral neck treatment when the tumor approaches/crosses midline or is advanced. Adjuvant intensity is driven by adverse pathology such as positive margin, extranodal extension, nodal burden, perineural/lymphovascular invasion, T stage and other risk features; positive margin and ENE are classic high-risk triggers for concurrent postoperative systemic therapy with RT when the patient can tolerate it."
        ),
        "operate": (
            "Plan the glossectomy from three-dimensional extent, not surface diameter alone. Achieve an oncologically adequate deep margin while protecting residual tongue mobility when feasible. Decide whether primary closure, local tissue, or free-flap reconstruction best restores bulk and mobility; a larger defect may need radial forearm or anterolateral-thigh-type reconstruction depending on volume and goals. Coordinate neck dissection in the same oncologic plan. For advanced lesions involving floor of mouth/mandible, escalate to composite resection only when invasion requires it rather than removing mandible prophylactically. Frozen sections can help margin assessment but do not replace correct initial resection geometry."
        ),
        "teach": (
            "Chief/boards discriminator: ORAL TONGUE = ORAL CAVITY + DOI + SURGERY/NECK. Anterior two thirds belongs to oral cavity; posterior tongue base belongs to oropharynx. DOI changes oral-cavity T staging and informs occult neck risk. A cN0 neck is not automatically observed: elective neck treatment is commonly part of curative surgery. p16 positivity does not convert an anterior oral-tongue primary into HPV-mediated oropharyngeal staging. Think: resectable primary, functional tongue preservation, elective/therapeutic neck plan, then pathology-driven adjuvant treatment."
        ),
        "tags": ["oral tongue SCC", "oral cavity cancer", "depth of invasion", "partial glossectomy", "elective neck dissection", "levels I-III", "midline", "free flap"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — oral cavity cancer, oral tongue anatomy, DOI, neck management, resection and reconstruction",
            "K.J. Lee's Essential Otolaryngology, 12e — oral cavity/tongue carcinoma staging and management",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — oral cavity cancer and tongue SCC",
            "ASCO Clinical Practice Guideline: Management of the Neck in Squamous Cell Carcinoma of the Oral Cavity and Oropharynx (JCO 2019;37:1753-1774)",
            "NCI Lip and Oral Cavity Cancer Treatment (PDQ), Health Professional Version — oral-cavity anatomy, staging, and treatment",
        ],
    },
    "base of tongue scc": {
        "recognize": (
            "Recognize BASE-OF-TONGUE SCC as an OROPHARYNGEAL cancer arising posterior to the circumvallate papillae, not as posterior extension of an oral-tongue card. Presentations include neck mass, dysphagia/odynophagia, globus, otalgia, bleeding, voice change, or an occult/subtle primary with nodal metastasis. Determine p16/HPV status because HPV-mediated oropharyngeal SCC has distinct biology, prognosis, and AJCC staging. BOT tumors often present with cervical nodes despite a relatively small primary because the tongue base has rich bilateral lymphatics."
        ),
        "localize": (
            "Map laterality and midline involvement of the tongue base, vallecula, glossotonsillar sulcus, tonsillar fossa, lingual surface of epiglottis, deep tongue musculature and pre-epiglottic relationship when relevant. Evaluate both necks because BOT lymphatic drainage is frequently bilateral; a lesion reaching midline changes contralateral-neck planning. Stage HPV-mediated (p16-positive) and p16-negative oropharyngeal SCC using the appropriate distinct AJCC systems rather than borrowing oral-cavity DOI rules. DOI is not the oral-cavity-style T-stage driver for BOT cancer."
        ),
        "workup": (
            "Perform flexible endoscopy, tissue diagnosis, contrast CT or MRI of primary/neck, and PET/CT when indicated for nodal/advanced disease or an occult primary workup. Obtain p16 immunohistochemistry for oropharyngeal SCC and use HPV-specific testing when required by the clinical/pathology context. Assess dental status before radiation, swallowing/nutrition, airway, performance status, smoking history and candidacy for either transoral surgery or definitive radiation-based therapy. In a neck-node presentation with no obvious primary, directed examination under anesthesia and modern transoral evaluation of tonsil/tongue-base lymphoid tissue may localize an HPV-associated occult primary."
        ),
        "manage": (
            "Choose treatment according to stage, HPV status, anatomy, functional consequences and expected adjuvant burden. Early/select BOT tumors may be managed with transoral laser/TORS plus neck dissection or with definitive radiation; more advanced disease is commonly treated with definitive chemoradiation or selected surgery followed by risk-adapted adjuvant therapy. Avoid 'trimodality by accident': if transoral resection is likely to yield margins/nodes that mandate full-dose postoperative chemoradiation, a nonsurgical definitive strategy may offer better functional value. Neck management differs from oral tongue: surgically treated lateralized oropharyngeal cancer generally receives ipsilateral levels II-IV dissection, while midline BOT involvement commonly requires bilateral neck treatment unless bilateral adjuvant RT is planned."
        ),
        "operate": (
            "For transoral BOT resection, confirm exposure, carotid relationship, depth, midline extent and anticipated swallowing impact before committing. TORS/TLM aims for oncologic margins while avoiding unnecessary loss of tongue-base constrictor function. When performing neck dissection with transoral oropharyngeal surgery, consider prophylactic ligation of at-risk external-carotid feeding vessels because postoperative hemorrhage can be catastrophic; ASCO specifically recommends ligation of at-risk feeding vessels with transoral endoscopic surgery. Reconstruction is less often a simple 'fill the defect' problem than in oral tongue—the functional issue is preservation of tongue-base propulsion and pharyngeal swallowing."
        ),
        "teach": (
            "Chief/boards discriminator: BASE OF TONGUE = OROPHARYNX + p16/HPV + BILATERAL LYMPHATICS + RT/TORS DECISION. A posterior tongue lesion is not staged by oral-cavity DOI. A small HPV-mediated BOT primary can present with a large cystic node and still have favorable biology. In surgical cases, think levels II-IV and contralateral treatment when the primary reaches midline; in transoral cases anticipate bleeding and swallowing consequences. The decision is not 'can I remove it?' but whether surgery will avoid or merely add to definitive chemoradiation."
        ),
        "tags": ["base of tongue SCC", "oropharyngeal cancer", "HPV", "p16", "TORS", "levels II-IV", "bilateral neck", "occult primary"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — oropharyngeal cancer, tongue-base anatomy, HPV biology, transoral surgery and chemoradiation",
            "K.J. Lee's Essential Otolaryngology, 12e — oropharyngeal/base-of-tongue carcinoma staging and treatment",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — oropharyngeal carcinoma and HPV-associated disease",
            "ASCO Clinical Practice Guideline: Management of the Neck in Squamous Cell Carcinoma of the Oral Cavity and Oropharynx (JCO 2019;37:1753-1774)",
            "NCI Oropharyngeal Cancer Treatment (PDQ), Health Professional Version — BOT anatomy, HPV/p16 staging and treatment",
        ],
    },
}


def apply_tongue_site_rebuild_v306(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        payload = TONGUE_SCC_V306.get(_norm(module.get("topic")))
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v306"] = True
        module["semantic_role_v306"] = (
            "oral_cavity_doi_surgery_neck_pathway"
            if _norm(module.get("topic")) == "oral tongue scc"
            else "oropharynx_hpv_bilateral_neck_modality_pathway"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
