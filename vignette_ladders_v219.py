"""v21.9 — Head & Neck Oncology learning-ladder pass 1.

Begins deliberate review of the first five canonical H&N concepts. Six strong
existing cases are reused and restaged; only genuinely missing layers are added.
"""
DOMAIN = "Head & Neck Oncology"

REUSED = {
    "v128_hn_01": ("HPV-Associated Oropharyngeal SCC", "foundation"),
    "v143_hno_02": ("HPV-Associated Oropharyngeal SCC", "application"),
    "v128_hn_04": ("Laryngeal SCC", "foundation"),
    "v128_hn_02": ("Unknown Primary with Cervical Metastasis", "foundation"),
    "v135_hn_01": ("Unknown Primary with Cervical Metastasis", "application"),
    "v128_hn_03": ("Neck Dissection", "foundation"),
}

REUSED_WHY = {
    "v143_hno_02": [
        "Correct. HPV-associated OPSCC has distinct prognostic staging, but treatment still follows anatomic extent, function, and evidence-based modality selection.",
        "p16 positivity improves prognosis but does not make an invasive nodal cancer safe to observe.",
        "Total laryngectomy is not a routine treatment for a small oropharyngeal primary.",
        "Cystic level-II nodes in an adult can be a classic presentation of HPV-associated oropharyngeal metastasis rather than benign disease.",
    ],
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


VIGNETTES_V219 = [
    _q(
        "v219_hn_hpv_snr", "HPV-Associated Oropharyngeal SCC", "senior_decision",
        "A fit patient has a small, well-lateralized p16-positive tonsil SCC that is technically resectable by TORS with a limited ipsilateral nodal burden. Preoperative imaging, however, suggests a high likelihood that surgery would yield extranodal extension requiring postoperative chemoradiation. What is the best attending-level treatment discussion?",
        ["Recommend TORS automatically because every technically resectable HPV-positive cancer should be operated on", "Compare primary surgery with definitive radiation-based therapy while explicitly weighing the risk that surgery may lead to trimodality treatment and added swallowing toxicity", "Observe because HPV-positive disease usually regresses", "Perform total laryngectomy to avoid adjuvant therapy"], 1,
        "For resectable HPV-associated OPSCC, surgery and definitive radiation-based therapy can both be appropriate in selected patients. The key senior decision is not technical resectability alone: predicted pathologic risk, functional outcomes, and the chance of requiring adjuvant chemoradiation should be considered to avoid unnecessary trimodality morbidity.",
        ["Technical access alone does not make surgery the best functional strategy.", "Correct. Modality selection should anticipate likely postoperative pathology and total treatment burden.", "HPV-associated disease has favorable prognosis but still requires definitive oncologic treatment.", "Laryngectomy is not appropriate for a localized tonsillar primary."],
        "For TORS candidacy, ask not only 'can I remove it?' but also 'what treatment will the pathology force afterward?'",
        "Which postoperative pathologic findings most strongly escalate adjuvant therapy after transoral resection?",
    ),

    _q(
        "v219_hn_larynx_app", "Laryngeal SCC", "application",
        "A glottic SCC extends into the paraglottic space and the involved true vocal fold is fixed, without gross extralaryngeal extension. Which staging principle is most important?",
        ["Vocal-fold fixation and/or paraglottic-space invasion are features of T3 laryngeal disease", "Any glottic tumor with hoarseness is T1", "Paraglottic-space invasion is irrelevant to T category", "A fixed cord proves distant metastatic disease"], 0,
        "For glottic laryngeal SCC, vocal-fold fixation, paraglottic-space invasion, and invasion of the inner cortex of the thyroid cartilage are classic T3 features. Subsite anatomy and deep-space extension matter because superficial size alone can underestimate biologic and functional extent.",
        ["Correct. Fixation and paraglottic extension are central T3 discriminators.", "Hoarseness is a presenting symptom, not a T-category definition.", "The paraglottic space is a major pathway of laryngeal tumor spread and directly affects staging.", "Cord fixation is a local functional sign and does not by itself establish distant metastasis."],
        "For laryngeal cancer, mobility and deep-space invasion often matter more than the visible mucosal footprint.",
        "How does invasion through the outer cortex of thyroid cartilage or into tissues beyond the larynx change T category?",
    ),
    _q(
        "v219_hn_larynx_snr", "Laryngeal SCC", "senior_decision",
        "A patient with a bulky supraglottic SCC arrives overnight with progressive stridor, retractions, and an endoscopic airway narrowed by friable tumor. They can still sit upright and oxygenate. What is the best senior-level next step?",
        ["Send the patient supine for routine CT before involving anesthesia", "Repeatedly instrument the tumor at bedside to determine how much it bleeds", "Activate an experienced ENT/anesthesia difficult-airway plan and secure the airway in the most controlled setting feasible, with a surgical-airway strategy immediately available", "Discharge with steroids because oxygen saturation is currently normal"], 2,
        "Impending obstruction from laryngeal cancer is an airway problem before it is a staging problem. A friable distorted tumor can convert a marginal airway into complete obstruction with sedation or repeated instrumentation, so airway securement should be planned collaboratively in a controlled environment with backup options matched to anatomy.",
        ["Supine transport and delayed airway planning can destabilize a marginal upper airway.", "Repeated manipulation can provoke bleeding, edema, or complete obstruction without improving the definitive plan.", "Correct. Airway strategy takes priority and should anticipate failure of the primary technique.", "Normal oxygenation does not make progressive stridor safe for outpatient management."],
        "In a threatened tumor airway, the safest plan is the one that anticipates how the first plan could fail.",
        "What tumor location or anatomy might make awake tracheostomy preferable to attempted transoral intubation?",
        "overnight_call",
    ),

    _q(
        "v219_hn_unknown_snr", "Unknown Primary with Cervical Metastasis", "senior_decision",
        "A patient has p16-positive SCC in a level-II node. PET/CT and office examination do not reveal the primary. Before committing to broad mucosal radiation fields, what diagnostic strategy can most meaningfully identify an occult oropharyngeal source?",
        ["Repeat FNA of the same node until a primary site appears", "Open neck biopsy before any mucosal evaluation", "Observation because an occult primary cannot be found once imaging is negative", "Operative directed evaluation including palatine tonsillectomy and, when appropriate, lingual tonsillectomy/base-of-tongue mucosectomy"], 3,
        "HPV-associated unknown-primary SCC is frequently occult within palatine or lingual tonsillar tissue. Operative mucosal evaluation with tonsillar tissue removal can identify a small primary after negative office examination and imaging, which may permit more focused treatment planning.",
        ["Repeating nodal cytology does not localize the mucosal source.", "Open biopsy can disrupt planes and does not substitute for an organized unknown-primary workup.", "Modern directed workup often identifies occult HPV-associated oropharyngeal primaries despite negative imaging.", "Correct. Tonsillar evaluation is a high-yield next step after a negative nonoperative workup."],
        "A negative PET does not end an HPV-positive unknown-primary workup; tiny tonsillar primaries can remain occult.",
        "How can identification of a small lateralized tonsillar primary change radiation volumes or surgical planning?",
        "boards",
    ),

    _q(
        "v219_hn_neck_app", "Neck Dissection", "application",
        "A patient with a well-lateralized oral cavity SCC requires elective ipsilateral neck treatment and has no clinically involved nodes. Which operative concept is most appropriate?",
        ["Use a selective neck dissection that removes nodal levels at meaningful risk while preserving uninvolved nonlymphatic structures", "Perform a radical neck dissection in every cN0 patient", "Remove only one sentinel-appearing palpable node", "Avoid compartment-oriented nodal surgery because the neck is clinically negative"], 0,
        "Selective neck dissection is designed around the drainage pattern and occult-risk levels of the primary while preserving structures such as the spinal accessory nerve, internal jugular vein, and sternocleidomastoid when they are not oncologically involved. The exact levels depend on primary site and disease context.",
        ["Correct. A selective operation matches nodal risk while avoiding unnecessary nonlymphatic morbidity.", "Radical neck dissection sacrifices major structures and is not justified simply because elective neck treatment is indicated.", "Node picking is not equivalent to a compartment-oriented oncologic dissection.", "Clinically occult nodal disease is precisely why selected cN0 necks receive elective treatment."],
        "The word 'selective' describes which nodal levels are removed—not a casual or incomplete cancer operation.",
        "Which nodal levels are classically included in an elective selective neck dissection for a lateral oral cavity primary?",
        "OR_prep",
    ),
    _q(
        "v219_hn_neck_snr", "Neck Dissection", "senior_decision",
        "During planned selective neck dissection, a bulky metastatic node is found densely invading the internal jugular vein but is separable from the spinal accessory nerve and sternocleidomastoid muscle. What is the best oncologic principle?",
        ["Abort because any involved nonlymphatic structure makes the neck unresectable", "Convert automatically to sacrifice of the vein, spinal accessory nerve, and SCM regardless of involvement", "Resect the invaded vein if required for an oncologically sound specimen while preserving uninvolved major structures when feasible", "Shell the node off the vein even if that leaves gross tumor"], 2,
        "Modern neck dissection is tailored to oncologic involvement. A major nonlymphatic structure should be sacrificed when directly invaded and necessary for complete resection, but uninvolved structures should not be removed merely to recreate a historical radical neck dissection.",
        ["Isolated jugular involvement does not automatically make nodal disease unresectable.", "Unnecessary sacrifice adds shoulder and contour morbidity without oncologic benefit.", "Correct. Preserve what is uninvolved and sacrifice what is truly invaded when required for complete resection.", "Leaving gross disease to preserve a vein defeats the oncologic purpose of the operation."],
        "A therapeutic neck dissection is anatomically radical only where the tumor makes it necessary.",
        "How would carotid encasement or skull-base fixation alter resectability and multidisciplinary planning?",
        "OR_prep",
    ),

    _q(
        "v219_hn_tongue_fnd", "Oral Tongue SCC", "foundation",
        "A 61-year-old smoker has a persistent indurated ulcer on the lateral oral tongue with referred otalgia and no improvement after several weeks. What is the most appropriate next step?",
        ["Treat empirically as thrush for several months", "Obtain tissue diagnosis and examine/stage the oral cavity and neck for squamous cell carcinoma", "Assume it is traumatic because lateral tongue ulcers are rarely malignant", "Order a thyroid uptake scan"], 1,
        "A persistent indurated oral-tongue ulcer is malignant until proven otherwise. Tissue diagnosis, careful measurement of the primary, assessment of depth and adjacent structures, and neck evaluation are required before treatment planning.",
        ["Prolonged empiric treatment delays diagnosis of a classic oral-cavity cancer presentation.", "Correct. Persistent induration/ulceration warrants biopsy and oncologic staging.", "Trauma is a differential, but persistence and induration require malignancy exclusion.", "Thyroid scintigraphy does not evaluate an oral-tongue mucosal lesion."],
        "A nonhealing indurated lateral-tongue ulcer deserves a biopsy, not another empiric mouth rinse.",
        "Which examination findings suggest deep tongue or floor-of-mouth extension that would change resection and reconstruction planning?",
    ),
    _q(
        "v219_hn_tongue_app", "Oral Tongue SCC", "application",
        "A 1.8 cm lateral oral-tongue SCC has a depth of invasion of 7 mm and a clinically N0 ipsilateral neck. What management principle is most appropriate?",
        ["Observation of the neck is mandatory because no node is palpable", "Elective treatment of the at-risk ipsilateral neck should be discussed because depth of invasion predicts clinically occult nodal metastasis", "Bilateral radical neck dissection is required for every oral-tongue cancer", "Neck treatment is determined by p16 status rather than oral-cavity depth of invasion"], 1,
        "Depth of invasion is a major predictor of occult nodal disease in oral-tongue SCC and contributes to T staging. Once occult-risk is clinically meaningful, elective selective neck dissection or another evidence-based elective neck strategy is preferred over waiting for palpable metastasis.",
        ["A cN0 examination does not exclude microscopic nodal disease.", "Correct. DOI is a key driver of elective-neck decision-making in oral tongue cancer.", "A radical bilateral operation is excessive for a small lateralized cN0 primary.", "p16-driven staging applies to HPV-associated oropharyngeal disease, not conventional oral-tongue SCC."],
        "For oral tongue cancer, measure depth—not just surface diameter—because depth predicts both T category and the hidden neck.",
        "How does a tumor approaching or crossing midline change contralateral neck considerations?",
    ),
    _q(
        "v219_hn_tongue_snr", "Oral Tongue SCC", "senior_decision",
        "A lateral oral-tongue SCC can be removed with clear margins, but the planned deep resection will leave a large mobile-tongue defect. What is the best attending-level reconstructive goal?",
        ["Maximize flap bulk regardless of residual tongue mobility", "Leave the defect open because reconstruction never affects swallowing", "Choose reconstruction that restores adequate volume and lining while preserving residual tongue mobility and avoiding an overly bulky tethered neotongue", "Perform total glossectomy solely to simplify reconstruction"], 2,
        "Oral-tongue reconstruction is functional. The flap must replace enough volume for bolus control and speech while remaining compatible with movement of the residual tongue; excessive bulk or tethering can be as disabling as inadequate volume. Defect size, floor-of-mouth involvement, dentition, and remaining tongue guide flap choice.",
        ["Excessive bulk can impair mobility, articulation, and bolus propulsion.", "Unreconstructed larger defects can scar and tether the residual tongue and worsen function.", "Correct. Reconstruction should be designed around the specific missing tissue and the movement the patient needs afterward.", "Oncologic extent—not reconstructive convenience—determines whether total glossectomy is required."],
        "Reconstruct the function you want after oral-tongue cancer, not simply the volume you removed.",
        "When would a thin radial forearm-type reconstruction be favored over a bulkier anterolateral thigh reconstruction?",
        "OR_prep",
    ),
]


def apply_learning_ladders_v219(challenges, item_id_fn):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reused = []
    for qid, (topic, stage) in REUSED.items():
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v21.9: expected reusable question missing: {qid}")
        q["domain"] = DOMAIN
        q["topic"] = topic
        q["concept_id"] = item_id_fn(DOMAIN, topic)
        q["learning_stage"] = stage
        q["ladder_reviewed"] = True
        if qid in REUSED_WHY:
            q["why_wrong"] = list(REUSED_WHY[qid])
        reused.append(qid)

    existing = set(by_id)
    added = []
    for row in VIGNETTES_V219:
        if row["id"] in existing:
            continue
        item = dict(row)
        item["concept_id"] = item_id_fn(DOMAIN, item["topic"])
        challenges.append(item)
        existing.add(item["id"])
        added.append(item["id"])
    return {"reused": reused, "added": added, "topics": sorted({q[1][0] for q in REUSED.items()} | {r["topic"] for r in VIGNETTES_V219})}
