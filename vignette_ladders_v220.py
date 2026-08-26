"""v22.0 — Head & Neck Oncology learning-ladder pass 2.

Deliberately reviews canonical topics 6-10: Floor of Mouth SCC, Tonsil SCC,
Base of Tongue SCC, Supraglottic Cancer, and Glottic Cancer. Strong existing
cases are reused where they add a distinct layer; generic old rationales are
replaced by choice-keyed individualized teaching so upstream shuffling is safe.
"""
DOMAIN = "Head & Neck Oncology"

REUSED = {
    "v145_hn_05": ("Floor of Mouth SCC", "application"),
    "v138_hn_02": ("Base of Tongue SCC", "foundation"),
    "v145_hn_02": ("Base of Tongue SCC", "application"),
    "v138_hn_08": ("Glottic Cancer", "foundation"),
    "v143_hno_01": ("Glottic Cancer", "application"),
}

REUSED_REASON_BY_CHOICE = {
    "v145_hn_05": {
        "Hair color": "Hair color has no role in determining oral-cavity oncologic resection or neck management.",
        "Depth/extent of invasion and whether the tumor invades mandible, tongue musculature, or adjacent structures": "Correct. Three-dimensional invasion determines the ablative and reconstructive plan far more than the surface footprint alone.",
        "Patient handedness": "Handedness may occasionally influence donor-site discussion but does not determine primary tumor resection.",
        "Presence of tonsilloliths": "Tonsilloliths are unrelated to floor-of-mouth SCC extent or mandibular management.",
    },
    "v138_hn_02": {
        "p16/HPV-associated status": "Correct. Base of tongue is oropharynx, so p16/HPV-mediated status changes AJCC prognostic staging and counseling.",
        "Serum calcium": "Calcium does not define staging or prognosis for an oropharyngeal SCC.",
        "Thyroid uptake scan": "Thyroid scintigraphy does not stage a base-of-tongue mucosal cancer.",
        "Audiogram only": "Hearing testing may matter before cisplatin in selected patients, but it does not establish the defining tumor classification asked here.",
    },
    "v145_hn_02": {
        "Primary size alone determines therapy": "A small primary can coexist with substantial nodal disease; the whole treatment package must be considered.",
        "Integrate HPV status, T/N stage, swallowing function, resectability, and expected morbidity of transoral surgery versus definitive radiation-based therapy": "Correct. Base-of-tongue treatment selection is a multidisciplinary disease-burden and functional-outcome decision.",
        "Neck disease can be ignored in HPV-positive cancer": "Favorable HPV biology does not make metastatic cervical disease irrelevant to staging or treatment.",
        "Open mandibulotomy is mandatory": "Many base-of-tongue cancers can be approached transorally or treated nonsurgically; open access is not mandatory by subsite alone.",
    },
    "v138_hn_08": {
        "Transoral laser microsurgery or definitive radiation": "Correct. Properly selected T1 glottic SCC is commonly treated with one definitive local modality.",
        "Total laryngectomy only": "Total laryngectomy is excessive for a small mobile-cord T1 lesion that is amenable to organ-preserving local therapy.",
        "Chemotherapy alone": "Chemotherapy alone is not definitive local treatment for early glottic SCC.",
        "Observation": "Biopsy-proven invasive glottic SCC requires definitive treatment rather than observation.",
    },
    "v143_hno_01": {
        "Choose a single definitive modality such as transoral laser microsurgery or radiation based on exposure, voice goals, anatomy and patient factors": "Correct. Early glottic cancer is a single-modality local-control problem in properly selected patients.",
        "Routine total laryngectomy": "Total laryngectomy adds major functional morbidity without justification for a limited T1 lesion.",
        "Mandatory bilateral neck dissection": "Truly early glottic cancer has low occult nodal risk because the true vocal folds have sparse lymphatics.",
        "Induction chemotherapy alone": "Induction chemotherapy alone is not definitive treatment for early glottic SCC.",
    },
}


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong, pearl, curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic, "learning_stage": stage,
        "stem": stem, "choices": choices, "answer": answer,
        "explanation": explanation, "why_wrong": why_wrong,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette", "focus": focus,
        "ladder_reviewed": True,
    }

VIGNETTES_V220 = [
    _q(
        "v220_hn_fom_fnd", "Floor of Mouth SCC", "foundation",
        "A 59-year-old tobacco user has a persistent ulcerated lesion in the anterior floor of mouth with induration around Wharton duct. Which diagnosis must be excluded promptly?",
        ["Oral cavity squamous cell carcinoma", "Acute bacterial parotitis", "BPPV", "Allergic rhinitis"], 0,
        "A persistent indurated floor-of-mouth lesion in an adult with carcinogen exposure is suspicious for oral-cavity SCC and requires tissue diagnosis plus careful assessment of tongue, mandible, salivary ducts, and the neck.",
        ["Correct. Persistence and induration in this subsite are classic red flags for oral-cavity malignancy.", "Parotitis causes painful parotid-region swelling and ductal purulence rather than a persistent floor-of-mouth ulcer.", "BPPV is a vestibular disorder and does not cause oral lesions.", "Allergic rhinitis does not cause an indurated oral-cavity ulcer."],
        "A persistent indurated oral lesion is a biopsy problem, not a prolonged empiric-treatment problem.",
        "What examination finding would raise particular concern for mandibular or deep tongue involvement?",
    ),
    _q(
        "v220_hn_fom_snr", "Floor of Mouth SCC", "senior_decision",
        "A floor-of-mouth SCC abuts the lingual cortex of the mandible. Imaging shows no medullary invasion and the periosteum can be cleared with an oncologically sound margin. What is the best attending-level mandibular strategy?",
        ["Perform segmental mandibulectomy for every floor-of-mouth SCC", "Preserve the mandible or use marginal resection when an adequate margin is achievable, reserving segmental resection for true bone invasion or inability to clear disease", "Ignore the deep margin because the mucosal margin is negative", "Replace surgery with antibiotics"], 1,
        "Mandibular sacrifice should match actual tumor invasion and margin requirements. Marginal resection can preserve continuity when disease does not require segmental removal; medullary invasion, extensive cortical involvement, or an inadequate remaining mandibular height may make segmental resection necessary.",
        ["Routine segmental resection creates major functional and reconstructive morbidity without oncologic benefit when bone continuity can safely be preserved.", "Correct. The operation should be as extensive as the cancer requires, not as extensive as the subsite permits.", "The deep margin is critical in oral-cavity cancer and cannot be dismissed because mucosal edges are clear.", "Antibiotics do not treat invasive SCC."],
        "Mandibular resection is driven by invasion and margin feasibility, not proximity alone.",
        "How would a segmental defect change reconstruction and dental-rehabilitation planning?",
        "OR_prep",
    ),

    _q(
        "v220_hn_tonsil_fnd", "Tonsil SCC", "foundation",
        "A 52-year-old never-smoker presents with an asymmetric tonsillar mass and a cystic ipsilateral level-II node. Biopsy shows squamous cell carcinoma. Which additional tumor test is essential for contemporary staging?",
        ["p16 testing as a surrogate for HPV-mediated oropharyngeal carcinoma in the appropriate setting", "Serum PTH", "Urine catecholamines", "Temporal-bone CT"], 0,
        "The palatine tonsil is an oropharyngeal subsite. p16 status is central to AJCC staging of HPV-mediated OPSCC and materially changes prognostic counseling, although it does not eliminate the need for anatomic staging and definitive therapy.",
        ["Correct. p16 status separates the HPV-mediated prognostic staging pathway from p16-negative disease.", "PTH evaluates parathyroid physiology rather than tonsillar SCC biology.", "Catecholamine testing is relevant to functional paraganglioma evaluation, not routine tonsillar SCC.", "Temporal-bone imaging does not establish HPV-mediated oropharyngeal staging."],
        "A cystic level-II node in an adult with a tonsillar lesion is HPV-associated OPSCC until proven otherwise.",
        "How does p16-negative tonsillar SCC differ prognostically and in AJCC staging?",
    ),
    _q(
        "v220_hn_tonsil_app", "Tonsil SCC", "application",
        "A small lateralized tonsil SCC is being considered for TORS. Which preoperative factor most directly threatens the safety of a transoral resection?",
        ["A retropharyngeal or parapharyngeal internal carotid artery lying unusually medial and close to the tonsillar tumor", "A normal contralateral tonsil", "An intact tympanic membrane", "A normal serum calcium"], 0,
        "TORS tonsil surgery occurs near the parapharyngeal carotid system. Cross-sectional imaging must be reviewed for carotid position, tumor-vessel relationship, deep extension, and whether a safe deep margin can be obtained transorally. A dangerously medialized carotid can make the transoral route inappropriate.",
        ["Correct. Carotid position is a critical route-selection and catastrophic-bleeding consideration.", "The contralateral tonsil does not determine the vascular safety of the operative corridor.", "Middle-ear examination is not the key TORS safety discriminator.", "Calcium level does not define transoral vascular anatomy."],
        "Before TORS, know where the carotid is relative to your deep margin—not just whether the tumor fits in the mouth.",
        "What postoperative hemorrhage pattern after TORS requires immediate airway and operative escalation?",
        "OR_prep",
    ),
    _q(
        "v220_hn_tonsil_snr", "Tonsil SCC", "senior_decision",
        "After TORS and neck dissection for tonsil SCC, pathology shows a negative primary margin but extranodal extension in a metastatic node. What is the key attending-level implication?",
        ["The negative primary margin guarantees no adjuvant treatment", "Extranodal extension is a high-risk pathologic feature that can drive postoperative concurrent chemoradiation in an eligible patient", "The neck pathology is irrelevant once the primary is removed", "Only observation is appropriate because the tumor is HPV-associated"], 1,
        "Extranodal extension is one of the classic high-risk postoperative features in mucosal HNSCC. In an eligible patient it can escalate adjuvant therapy to concurrent chemoradiation, which is why predicted nodal pathology matters when selecting primary surgery versus definitive nonsurgical therapy.",
        ["Primary-margin status does not erase adverse nodal pathology.", "Correct. ENE can convert a seemingly attractive surgical plan into trimodality treatment.", "Nodal pathology is a major determinant of postoperative risk and treatment intensity.", "Favorable HPV biology does not nullify established high-risk pathologic features."],
        "TORS planning should anticipate the adjuvant treatment the neck pathology may trigger.",
        "How does a positive surgical margin compare with ENE as an adjuvant-treatment trigger?",
    ),

    _q(
        "v220_hn_bot_snr", "Base of Tongue SCC", "senior_decision",
        "A base-of-tongue SCC crosses midline and has bilateral cervical nodal disease. The primary is technically accessible transorally, but resection would remove a large amount of functional tongue base and adjuvant chemoradiation is highly likely. What is the best treatment-selection principle?",
        ["Choose TORS simply because the tumor is technically reachable", "Compare definitive radiation-based therapy with surgery based on total treatment burden, expected swallowing function, nodal pathology risk, and patient goals rather than access alone", "Ignore bilateral nodal disease because HPV-positive nodes are favorable", "Perform total glossectomy in every midline-crossing tumor"], 1,
        "For base-of-tongue SCC, technical transoral access is only one part of candidacy. Extensive tongue-base resection plus likely adjuvant chemoradiation may produce more functional burden than a definitive nonsurgical pathway. The senior decision is to select the best overall treatment package rather than the easiest primary resection.",
        ["Reachability does not guarantee favorable function or avoidance of trimodality therapy.", "Correct. Functional reserve and likely downstream therapy are central to modality selection.", "Bilateral nodes materially affect staging, fields, and treatment planning.", "Total glossectomy is not dictated simply by crossing the midline."],
        "For oropharyngeal surgery, resectability and desirability are not the same question.",
        "Which pre-treatment swallowing and nutrition factors should enter shared decision-making?",
    ),

    _q(
        "v220_hn_supra_fnd", "Supraglottic Cancer", "foundation",
        "A patient has biopsy-proven SCC centered on the epiglottis. Why is elective neck treatment considered more often than for an equally small true-vocal-fold cancer?",
        ["The supraglottis has a richer bilateral lymphatic network and therefore greater occult nodal risk", "The epiglottis drains only to level V", "Supraglottic cancers never cause symptoms", "The true vocal folds have more lymphatics than the supraglottis"], 0,
        "The supraglottis has abundant lymphatics with bilateral drainage potential, whereas the true vocal folds have relatively sparse lymphatics. This anatomic difference drives the higher nodal risk and neck-management requirements of supraglottic disease.",
        ["Correct. Subsite lymphatic anatomy explains the different neck behavior.", "Level V is not the exclusive or characteristic drainage explanation.", "Supraglottic cancers can cause dysphagia, odynophagia, otalgia, voice change, and airway symptoms.", "The opposite is true: the glottis is relatively lymphatically sparse."],
        "Laryngeal subsite predicts nodal behavior: supraglottis is lymphatic-rich; early glottis is lymphatic-poor.",
        "Which neck levels are commonly at risk from a lateralized supraglottic primary?",
    ),
    _q(
        "v220_hn_supra_app", "Supraglottic Cancer", "application",
        "A patient with a lateralized supraglottic SCC has preserved vocal-fold mobility and is being considered for transoral supraglottic laryngectomy. Which patient factor is most important beyond tumor resectability?",
        ["Adequate pulmonary reserve and ability to rehabilitate swallowing and protect the airway", "A normal audiogram", "Absence of seasonal allergies", "Dominant hand"], 0,
        "Supraglottic laryngectomy removes structures important for airway protection. Successful organ-preserving surgery requires appropriate tumor extent plus sufficient pulmonary reserve, cognition, laryngeal function, and rehabilitation potential to tolerate the expected period of aspiration and recover safe swallowing.",
        ["Correct. Functional candidacy is as important as anatomic candidacy for conservation surgery.", "Hearing status does not determine postoperative airway protection.", "Allergic rhinitis does not determine whether the patient can rehabilitate swallowing.", "Hand dominance does not define laryngeal functional reserve."],
        "Conservation laryngeal surgery preserves an organ only if the patient can make the preserved organ work safely.",
        "Which tumor extension or arytenoid dysfunction would make a conservation approach less attractive?",
        "OR_prep",
    ),
    _q(
        "v220_hn_supra_snr", "Supraglottic Cancer", "senior_decision",
        "A patient with advanced supraglottic SCC has severe baseline aspiration, recurrent pneumonias, poor pulmonary reserve, and a poorly functioning larynx before treatment. The tumor is technically eligible for an organ-preservation chemoradiation protocol. What is the best attending-level principle?",
        ["Choose chemoradiation automatically because an anatomically preserved larynx is always the best outcome", "Include baseline laryngeal function in treatment selection; a nonfunctional aspirating larynx may favor ablative surgery despite technical eligibility for organ preservation", "Ignore aspiration because it is unrelated to cancer treatment", "Delay all treatment until pulmonary function normalizes"], 1,
        "Organ preservation is not synonymous with functional preservation. Severe pretreatment aspiration and poor laryngeal function predict major morbidity if a damaged organ is preserved. In selected patients, total laryngectomy may provide safer swallowing and a more reliable airway while maintaining oncologic control.",
        ["An organ that remains unsafe for swallowing is not a successful functional preservation outcome.", "Correct. Baseline function must be part of the oncologic modality decision.", "Aspiration is central to treatment morbidity and long-term quality of life.", "Cancer treatment should not be indefinitely deferred while waiting for unrealistic normalization of chronic pulmonary disease."],
        "Before promising larynx preservation, decide whether the larynx is worth preserving functionally.",
        "How would pretreatment feeding-tube dependence or tracheostomy affect counseling about organ-preservation outcomes?",
    ),

    _q(
        "v220_hn_glottic_snr", "Glottic Cancer", "senior_decision",
        "A professional voice user has a small T1a glottic SCC that is oncologically suitable for either transoral laser microsurgery or radiation. What is the best attending-level recommendation framework?",
        ["Claim one modality always produces a better voice for every patient", "Use shared decision-making that weighs endoscopic exposure, exact lesion location, anticipated depth of cord resection, voice priorities, treatment logistics, salvage options, and patient preference", "Perform total laryngectomy to maximize local control", "Observe until vocal-fold mobility is lost"], 1,
        "Both transoral laser microsurgery and definitive radiation can cure properly selected early glottic SCC. Voice outcome varies with lesion and treatment details, so counseling should be individualized rather than based on a universal voice-superiority claim. Exposure, anterior commissure/depth, patient priorities, logistics, and salvage pathways all matter.",
        ["Voice outcomes depend on lesion and treatment specifics; no single modality is universally superior for every T1 patient.", "Correct. Early-glottic treatment selection is a nuanced single-modality shared decision.", "Total laryngectomy is disproportionate for a small T1a lesion.", "Waiting for progression can sacrifice a highly curable early-stage treatment opportunity."],
        "For T1 glottic cancer, cure is usually achievable by either route; the art is choosing the route that best fits anatomy and the patient's functional priorities.",
        "How does anterior commissure involvement affect exposure, resection, and recurrence counseling?",
    ),
]


def _align_reused(qid, q):
    mapping = REUSED_REASON_BY_CHOICE.get(qid, {})
    q["why_wrong"] = [mapping.get(str(choice), "This choice does not match the case-specific oncologic principle.") for choice in list(q.get("choices") or [])]


def apply_learning_ladders_v220(challenges, item_id_fn):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reused = []
    for qid, (topic, stage) in REUSED.items():
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v22.0: expected reusable question missing: {qid}")
        q["domain"] = DOMAIN
        q["topic"] = topic
        q["concept_id"] = item_id_fn(DOMAIN, topic)
        q["learning_stage"] = stage
        q["ladder_reviewed"] = True
        _align_reused(qid, q)
        reused.append(qid)

    existing = set(by_id)
    added = []
    for row in VIGNETTES_V220:
        if row["id"] in existing:
            continue
        item = dict(row)
        item["concept_id"] = item_id_fn(DOMAIN, item["topic"])
        challenges.append(item)
        existing.add(item["id"])
        added.append(item["id"])
    return {"reused": reused, "added": added, "topics": ["Floor of Mouth SCC", "Tonsil SCC", "Base of Tongue SCC", "Supraglottic Cancer", "Glottic Cancer"]}
