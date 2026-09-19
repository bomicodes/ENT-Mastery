"""Selective source-verified Rhinology Daily Curriculum repairs.

Rehomes six bounded learner-facing prompt/answer pairs from the older v38.1
work without importing that stale branch. Canonical topics and challenge fields
are unchanged.
"""

DAILY_OVERRIDES = {
    ("Endoscopic Maxillary Antrostomy", "localize"): (
        "Which uncinate, natural ostium, orbit, lacrimal, accessory-ostium, and dental relationships must be localized before a maxillary antrostomy?",
        "Identify the uncinate attachment and infundibulum, then find the true natural maxillary ostium rather than entering through a fontanelle accessory opening. The lamina papyracea and orbital floor define the lateral-superior danger, while the nasolacrimal duct lies anteriorly and dental roots and alveolar recess are inferior. Disease may extend into prelacrimal, lateral or odontogenic compartments not reached by a routine middle-meatal opening. Preoperative CT should also reveal hypoplastic sinus, silent-sinus remodeling, Haller cells, prior surgery and anatomic asymmetry that change orientation and access.",
    ),
    ("Endoscopic Maxillary Antrostomy", "manage"): (
        "How should pathology and anatomy determine the size and position of a maxillary antrostomy while preventing recirculation, orbital injury, and unnecessary mucosal loss?",
        "Open the natural ostium and connect any accessory opening into one common drainage pathway; leaving separated openings can create mucus recirculation. Enlarge only as needed for disease clearance, topical access or instrument reach while preserving healthy mucosa and protecting the orbit and nasolacrimal duct. Address an odontogenic, foreign-body or neoplastic source rather than treating the sinus opening as definitive therapy. Persistent symptoms after surgery should prompt review for a missed natural ostium, scar, odontogenic disease, recirculation or a compartment the chosen corridor cannot adequately reach.",
    ),
    ("Ethmoidectomy", "workup"): (
        "What must be reconstructed from preoperative CT before ethmoidectomy to anticipate skull-base, orbital, vascular, optic-nerve, and frontal-recess hazards?",
        "Review each side independently for skull-base height and slope, Keros depth and asymmetry, lamina papyracea integrity, anterior ethmoid artery course, frontal-recess and supraorbital ethmoid anatomy, and posterior ethmoid/Onodi relationships to the optic nerve and sphenoid. Identify prior surgery, osteitis, tumor, fungal disease and distorted landmarks. Trace drainage pathways rather than simply counting cells. A low or asymmetric roof, exposed or suspended artery, displaced orbit or posterior cell closely related to the optic nerve should change instrument direction, dissection extent and the need for additional navigation or exposure.",
    ),
    ("Inferior Turbinate Hypertrophy", "localize"): (
        "How do decongestion response, bony contour, mucosal disease, nasal-valve behavior, septal anatomy, and side-to-side symptoms identify whether the inferior turbinate is actually the dominant obstruction?",
        "Examine the airway before and after topical decongestion. A large reversible change supports mucosal congestion, while persistent bulk may reflect bone, fibrosis or compensatory hypertrophy. Assess the internal and external nasal valves dynamically, septal deviation, nasal cycle and other obstructing pathology. A turbinate can appear large because the opposite septum changes available space, while a seemingly adequate cavity can still fail dynamically at the valve. Treatment should target the demonstrated symptomatic bottleneck rather than every visually prominent turbinate.",
    ),
    ("Inferior Turbinate Hypertrophy", "workup"): (
        "What history and examination distinguish inflammatory turbinate congestion from fixed hypertrophy, valve collapse, septal obstruction, medication injury, or another nasal process?",
        "Clarify laterality, variability, allergens, irritants, exercise, sleep, prior surgery, trauma and use of topical decongestants or other intranasal drugs. Perform anterior examination and dynamic valve assessment before and after decongestion, documenting mucosa, septum and airflow response. Endoscopy is useful when posterior obstruction, polyps, purulence, a mass or nasopharyngeal disease is a concern. Allergy testing or CT should be selective when it will change management; unilateral bleeding, pain, progressive obstruction or a mass requires a different workup than presumed rhinitis.",
    ),
    ("Inferior Turbinate Hypertrophy", "manage"): (
        "How should medical response, tissue composition, coexisting septal or valve disease, and empty-nose risk determine whether and how the inferior turbinate is reduced?",
        "Treat the demonstrated inflammatory driver first with appropriate medical therapy and remove rebound-producing topical decongestant exposure when present. Offer reduction for persistent function-limiting hypertrophy only after the turbinate is shown to contribute meaningfully to obstruction. Match a mucosa-preserving reduction technique to tissue and anatomy and address important septal or valve disease when it is part of the bottleneck. Avoid aggressive resection that sacrifices normal humidification, sensation and airflow regulation and can produce chronic crusting or empty-nose symptoms.",
    ),
}


def apply_daily_curriculum_rhinology_selective_v382(items):
    stats = {"daily_pairs": 0, "topics": set()}
    for item in items:
        key = (item.get("topic"), item.get("stage"))
        override = DAILY_OVERRIDES.get(key)
        if not override:
            continue
        prompt, answer = override
        item["daily_prompt"] = prompt
        item["prompt"] = prompt
        item["answer"] = answer
        stats["daily_pairs"] += 1
        stats["topics"].add(item.get("topic"))
    stats["topics"] = len(stats["topics"])
    return stats


def install_daily_curriculum_rhinology_selective_v382(data_module, app_module):
    original_get_items = data_module.get_adaptive_items_v120

    def get_adaptive_items_v382():
        items = original_get_items()
        apply_daily_curriculum_rhinology_selective_v382(items)
        return items

    data_module.get_adaptive_items_v120 = get_adaptive_items_v382
    app_module._adaptive_question = lambda item: item.get("daily_prompt") or item.get("prompt") or ""
    sample = get_adaptive_items_v382()
    return {"item_stats": apply_daily_curriculum_rhinology_selective_v382(sample)}
