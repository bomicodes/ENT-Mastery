"""
v13.0 - Vignette topic-alias reconciliation.

Discovery: 93 of 176 vignettes (53%) in CLINICAL_CHALLENGES_V119 use a topic
label that does not exactly match any DEEP_MODULES_V6 canonical topic string
(e.g. "SSNHL" vs "Sudden Sensorineural Hearing Loss", "Unknown Primary" vs
"Unknown Primary with Cervical Metastasis"). Because concept_id is computed
from (domain, topic), every one of these vignettes has an orphaned concept_id
that matches no real topic - they never appear as a "related case" on the
correct concept-hub page, and they were invisible to per-domain vignette
coverage counts, making several domains look far less covered than they
actually are.

Fix: alias each drifted label to its correct canonical topic for concept_id
purposes only. The vignette's *displayed* topic label is left as-is (some of
these, like "SSNHL" or "BPPV"-style short labels, are actually better card
headings than the full canonical name) - only concept_id resolution changes.

v13.5 integration: after canonical topics are registered, merge a cross-domain
high-yield vignette batch with strict domain/topic validation. This keeps the
100%-coverage push from reintroducing silent orphan cases.
"""

from vignettes_v135 import VIGNETTES_V135

TOPIC_ALIAS_V129 = {
    "Cholesteatoma": "Chronic Otitis Media / Cholesteatoma",
    "Facial Nerve Paralysis": "Facial Paralysis",
    "Labyrinthitis": "Labyrinthitis / Infections of the Labyrinth",
    "Perilymph Fistula": "Perilymph Fistula / Inner-Ear Window Leak",
    "SSNHL": "Sudden Sensorineural Hearing Loss",
    "Superior Semicircular Canal Dehiscence": "Superior Canal Dehiscence",
    "Temporal Bone Trauma": "Temporal Bone Fracture",
    "Acute Invasive Fungal Rhinosinusitis": "Invasive Fungal Rhinosinusitis",
    "Frontal Sinus Mucocele": "Mucocele",
    "Intracranial Complication of Sinusitis": "Intracranial Complications of Sinusitis",
    "Inverted Papilloma": "Sinonasal Inverted Papilloma",
    "Orbital Cellulitis vs Preseptal Cellulitis": "Orbital Complications of Sinusitis",
    "Orbital Complication of Sinusitis": "Orbital Complications of Sinusitis",
    "Unilateral Nasal Mass": "Unilateral Sinonasal Disease",
    "Adjuvant Therapy After Head and Neck Cancer Surgery": "Adverse Pathology and Adjuvant Therapy",
    "Adult Neck Mass / HPV OPSCC": "Unknown Primary with Cervical Metastasis",
    "Cutaneous SCC / Parotid Metastasis": "Cutaneous Squamous Cell Carcinoma of the Head & Neck",
    "Cutaneous Squamous Cell Carcinoma": "Cutaneous Squamous Cell Carcinoma of the Head & Neck",
    "HPV-Positive Oropharyngeal Squamous Cell Carcinoma": "HPV-Associated Oropharyngeal SCC",
    "Organ Preservation in Advanced Laryngeal Cancer": "Laryngeal Preservation Decision",
    "Osteoradionecrosis": "Osteoradionecrosis of the Jaw",
    "Perineural Spread": "Cutaneous Squamous Cell Carcinoma of the Head & Neck",
    "Salvage Laryngectomy": "Salvage Surgery After Radiation / Chemoradiation",
    "Salvage Surgery After Radiation": "Salvage Surgery After Radiation / Chemoradiation",
    "Sinonasal Malignancy": "Sinonasal Malignancies",
    "Supraglottic SCC": "Supraglottic Cancer",
    "Unknown Primary": "Unknown Primary with Cervical Metastasis",
    "Unknown Primary Head and Neck Cancer": "Unknown Primary with Cervical Metastasis",
    "Unknown Primary Squamous Cell Carcinoma": "Unknown Primary with Cervical Metastasis",
    "Hungry Bone Syndrome": "Hungry Bone / Post-Thyroid Calcium Management",
    "Medullary Thyroid Carcinoma": "Medullary Thyroid Cancer",
    "Parathyroid Localization": "Primary Hyperparathyroidism",
    "Parotid Malignancy": "Salivary Gland Malignancy",
    "Recurrent Laryngeal Nerve / Thyroidectomy": "Recurrent Laryngeal Nerve Injury During Thyroidectomy",
    "Thyroid Storm / Airway Compression": "Graves Disease / Toxic Goiter",
    "Airway Foreign Body": "Pediatric Airway Foreign Body",
    "Congenital Neck Mass": "Congenital Neck Masses",
    "Congenital Vocal Fold Paralysis": "Pediatric Vocal Fold Immobility",
    "Pediatric OSA": "Pediatric OSA / Adenotonsillar Disease",
    "Recurrent AOM / Tympanostomy": "AOM / OME / Tympanostomy Decisions",
    "Retropharyngeal Abscess": "Pediatric Deep Neck Infection",
    "Sleep-Disordered Breathing in Down Syndrome": "Pediatric OSA / Adenotonsillar Disease",
    "Subglottic Stenosis": "Pediatric Subglottic Stenosis",
    "Arytenoid Dislocation vs RLN Paralysis": "Posterior Glottic Stenosis / Arytenoid Fixation",
    "Aspiration after Head and Neck Surgery": "Dysphagia / Aspiration",
    "Bilateral Vocal Fold Paralysis": "Bilateral Vocal Fold Immobility",
    "Idiopathic Subglottic Stenosis": "Subglottic / Tracheal Stenosis",
    "Laryngeal Granuloma": "Vocal Process Granuloma",
    "Paradoxical Vocal Fold Motion / Inducible Laryngeal Obstruction": "Inducible Laryngeal Obstruction / PVFM",
    "Posterior Glottic Stenosis": "Posterior Glottic Stenosis / Arytenoid Fixation",
    "Vocal Fold Lesion": "Benign Vocal Fold Lesions",
    "Vocal Fold Nodules, Polyps, and Cysts": "Vocal Fold Polyp / Cyst",
    "Vocal Fold Scar / Sulcus Vocalis": "Vocal Fold Sulcus / Scar",
    "Facial Nerve Laceration": "Facial Nerve Reanimation",
    "Frontal Sinus Posterior Table Fracture": "Frontal Sinus Fracture Decision Model",
    "Nasal Tip Support": "Rhinoplasty Tip Mechanics",
    "Nasal Valve Collapse": "Functional Nasal Obstruction",
    "Orbital Floor Fracture": "ZMC / Orbital Trauma",
    "Zygomaticomaxillary Complex Fracture": "ZMC / Orbital Trauma",
    "Adult OSA": "Adult PSG Interpretation",
    "Central Sleep Apnea": "Central Sleep Apnea / Treatment-Emergent CSA",
    "Drug-Induced Sleep Endoscopy": "DISE",
    "Hypoventilation": "Sleep-Related Hypoventilation",
    "Mandibular Advancement Device": "Oral Appliance Therapy",
    "Pediatric Residual OSA": "Residual OSA After Surgery",
    "Treatment-Emergent Central Sleep Apnea": "Central Sleep Apnea / Treatment-Emergent CSA",
    "Esophageal Perforation": "Esophageal Perforation / Cervical Mediastinitis",
    "Post-thyroidectomy Neck Hematoma": "Postoperative Neck Hematoma",
    "Posterior Epistaxis": "Epistaxis",
    "Severe Epistaxis": "Epistaxis",
    "Laryngeal Cancer": "Laryngeal SCC",
}

DOMAIN_SPECIFIC_ALIAS_V129 = {
    ("Rhinology / Allergy / Skull Base", "Posterior Epistaxis"): "Epistaxis Surgical Control",
    ("General ENT / Emergencies", "Posterior Epistaxis"): "Epistaxis",
}

ORPHANS_WITH_NO_CANONICAL_MATCH = [
    "First-Bite Syndrome",
    "Frey Syndrome",
    "Recurrent Laryngeal Nerve / Thyroidectomy",
    "Button Battery Ingestion",
    "Croup vs Epiglottitis",
    "Epiglottitis",
    "Septal Hematoma",
    "Positional OSA",
    "Lemierre Syndrome",
    "Recurrent Respiratory Papillomatosis",
]


def _merge_v135_strict(challenges, v6_item_id):
    import data

    canonical = {
        (domain, module.get("topic"))
        for domain, modules in data.DEEP_MODULES_V6.items()
        for module in modules
    }
    existing_ids = {q.get("id") for q in challenges}
    for source in VIGNETTES_V135:
        key = (source.get("domain"), source.get("topic"))
        if key not in canonical:
            raise RuntimeError(
                f"v13.5: orphan vignette {source.get('id')!r} targets non-canonical {key!r}"
            )
        if source.get("id") in existing_ids:
            continue
        q = dict(source)
        q["concept_id"] = v6_item_id(q["domain"], q["topic"])
        challenges.append(q)
        existing_ids.add(q["id"])
    data.CLINICAL_CHALLENGE_BY_ID_V119 = {q["id"]: q for q in challenges}


def apply_topic_alias_v129(challenges, v6_item_id):
    """Recomputes concept_id for any vignette whose topic has a known alias,
    then merges the strictly validated v13.5 cross-domain depth batch.
    Mutates and returns the list in place. Does not change displayed topic."""
    for q in challenges:
        key = (q.get("domain"), q.get("topic"))
        alias = DOMAIN_SPECIFIC_ALIAS_V129.get(key) or TOPIC_ALIAS_V129.get(q.get("topic"))
        if alias:
            q["concept_id"] = v6_item_id(q["domain"], alias)
            q["canonical_topic"] = alias
    _merge_v135_strict(challenges, v6_item_id)
    return challenges
