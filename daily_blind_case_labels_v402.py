"""
v40.2 -- Curated, diagnosis-neutral blind-case labels for the Daily Curriculum
blind-quiz mode.

Problem: `daily_curriculum_quality_v368._case_label()` falls back to ~20
generic keyword-matched bucket labels (e.g. "Sinonasal symptoms", "Voice
change", "Ear symptoms") when a topic has no curated `TOPIC_CASE_LABELS`
entry. Several of those buckets are shared across many unrelated topics
(e.g. "Sinonasal symptoms" was reused by 11 different topics), so the
"Unidentified case ***" header on the Daily Adaptive path gave the learner
zero real discriminating information despite implying a helpful hint.

Fix: add specific-but-diagnosis-neutral overrides for every topic currently
falling into a collision-prone generic bucket (2+ topics sharing one label).
`_case_label()` checks the module-global `TOPIC_CASE_LABELS` dict first, so
updating that dict in place works regardless of patch-chain load order.
"""

NEW_CASE_LABELS = {
    # "Sinonasal symptoms" bucket (was shared by 11 topics)
    "AERD": "Nasal polyps, asthma, and respiratory symptoms after analgesic exposure",
    "AFRS": "Asymmetric nasal polyposis with thick, tenacious mucin",
    "Acute Bacterial Rhinosinusitis": "Acute purulent sinus symptoms",
    "Branchial Cleft Anomalies": "Congenital neck pit or tract with recurrent drainage",
    "CF / Primary Ciliary Dyskinesia Sinonasal Disease": "Pediatric sinonasal disease with chronic wet cough",
    "Fungal Ball": "Unilateral chronic sinus opacification without bone erosion",
    "Immunodeficiency-Associated Chronic Rhinosinusitis": "Refractory sinus disease in an immunocompromised host",
    "Invasive Fungal Rhinosinusitis": "Rapidly progressive sinonasal disease in a neutropenic host",
    "Orbital Complications of Sinusitis": "Sinusitis with periorbital swelling",
    "Septal Deviation": "Fixed unilateral nasal obstruction",
    "Sinonasal Malignancy": "Unilateral nasal obstruction with epistaxis and facial numbness",

    # "Airway symptoms" bucket (was shared by 11 topics)
    "Airway Foreign Body": "Sudden choking with a witnessed aspiration event",
    "Bilateral Vocal Fold Immobility": "Biphasic stridor after neck or thyroid surgery",
    "Choanal Atresia": "Neonatal cyclical respiratory distress relieved by crying",
    "Epiglottitis": "Rapidly progressive drooling and muffled voice",
    "Laryngeal Fracture / External Laryngeal Trauma": "Anterior neck blunt trauma with voice change",
    "Laryngomalacia": "Infant inspiratory stridor worse supine and with feeding",
    "Pediatric Airway Foreign Body": "Sudden pediatric coughing or choking episode with unilateral wheeze",
    "Pediatric Vocal Fold Immobility": "Weak cry and stridor in an infant",
    "Postoperative Neck Hematoma": "Rapidly expanding neck swelling after neck surgery",
    "Tracheal Malignancy": "Progressive positional dyspnea and wheeze unresponsive to inhalers",
    "Tracheostomy Emergency": "Acute respiratory distress in a tracheostomy-dependent patient",

    # "Voice change" bucket (was shared by 8 topics)
    "Laryngeal SCC": "Progressive hoarseness in a longtime smoker",
    "Muscle Tension Dysphonia": "Effortful, strained voice with a normal-appearing larynx",
    "Reinke Edema": "Deep, rough voice in a longtime smoker",
    "Unilateral Vocal Fold Paralysis": "Breathy voice with a weak cough after surgery",
    "Vocal Fold Polyp / Cyst": "Intermittent breathy hoarseness in a heavy voice user",
    "Vocal Fold Sulcus / Scar": "Chronic hoarseness after phonotrauma or prior laryngeal surgery",
    "Vocal Process Granuloma": "Chronic throat pain and hoarseness with a reflux or intubation history",
    "Vocal Tremor": "Quavering voice that worsens with sustained phonation",

    # "Swallowing symptoms" bucket (was shared by 7 topics)
    "Button Battery Ingestion": "Witnessed battery ingestion with drooling",
    "Cricopharyngeal Dysfunction": "Cervical dysphagia with a sensation of a high obstruction",
    "Hypopharyngeal Cancer": "Progressive dysphagia and referred otalgia in a smoker",
    "Laryngotracheal Cleft": "Infant feeding-related coughing or choking with recurrent aspiration pneumonia",
    "Oral Tongue SCC": "Non-healing tongue ulcer with pain",
    "Radiation-Associated Dysphagia": "Progressive dysphagia years after head and neck radiation",
    "Recurrent / Metastatic HNSCC": "New mass or symptom after treated head and neck cancer",

    # "Ear symptoms" bucket (was shared by 6 topics)
    "Acute Mastoiditis / Petrous Apicitis": "Postauricular swelling and fever after an ear infection",
    "Acute Otitis Externa": "Painful ear canal worse with tragal pressure",
    "CSF Otorrhea / Temporal Encephalocele": "Persistent watery ear drainage after tympanostomy or trauma",
    "Chronic Otitis Media / Cholesteatoma": "Chronic malodorous ear drainage with hearing loss",
    "Keratosis Obturans": "Bilateral canal fullness with pressure and conductive hearing loss",
    "Necrotizing Otitis Externa": "Severe ear pain out of proportion to exam in a diabetic patient",

    # "Hearing complaint" bucket (was shared by 6 topics)
    "Age-Related Hearing Loss / Presbycusis": "Gradual bilateral high-frequency hearing loss in an older adult",
    "Labyrinthitis / Infections of the Labyrinth": "Acute vertigo with hearing loss during or after an ear or viral infection",
    "Ménière Disease": "Episodic vertigo with fluctuating hearing loss and ear fullness",
    "Perilymph Fistula / Inner-Ear Window Leak": "Dizziness and hearing change triggered by straining or a pressure change",
    "Superior Canal Dehiscence": "Sound- or pressure-induced vertigo with autophony",
    "Vestibular Schwannoma": "Progressive unilateral hearing loss with imbalance",

    # "Salivary presentation" bucket (was shared by 5 topics)
    "First-Bite Syndrome": "Severe pain with the first bite of a meal after parapharyngeal surgery",
    "Frey Syndrome": "Facial sweating and flushing while eating after parotid surgery",
    "Juvenile Recurrent Parotitis": "Recurrent childhood parotid swelling without stones",
    "Salivary Adenoid Cystic Carcinoma and Perineural Spread": "Persistent salivary mass with progressive sensory or motor symptoms",
    "Submandibular Sialolithiasis": "Painful mealtime submandibular swelling",

    # "Thyroid presentation" bucket (was shared by 4 topics)
    "Familial Hyperparathyroidism and Parathyromatosis": "Recurrent hypercalcemia across multiple family members",
    "Graves Disease / Toxic Goiter": "Diffuse goiter with tremor, weight loss and eye findings",
    "MEN2 / RET": "Family history of medullary thyroid cancer and pheochromocytoma",
    "Secondary / Tertiary Hyperparathyroidism": "Elevated PTH in chronic kidney disease; calcium varies with disease stage",

    # "Trauma presentation" bucket (was shared by 3 topics)
    "Alar Retraction / Nasal Vestibular Stenosis": "Nasal valve narrowing after prior nasal surgery or trauma",
    "Mandible Fracture": "Malocclusion and jaw pain after facial trauma",
    "Ossicular Discontinuity": "Sudden conductive hearing loss after head trauma",

    # "Nasal drainage" bucket (was shared by 3 topics)
    "Allergic Rhinitis": "Seasonal clear rhinorrhea with sneezing and itchy eyes",
    "CSF Rhinorrhea": "Unilateral clear watery rhinorrhea worse with bending forward",
    "Nonallergic Rhinitis / Rhinitis Medicamentosa": "Chronic congestion worsened by prolonged decongestant spray use",

    # "Neck mass" bucket (was shared by 3 topics)
    "Neck Lymphoma": "Persistent painless rubbery cervical lymphadenopathy, with or without systemic symptoms",
    "Primary Thyroid Lymphoma": "Rapidly enlarging thyroid mass in a patient with Hashimoto thyroiditis",
    "Unknown Primary with Cervical Metastasis": "Metastatic neck node without an identified primary tumor on exam",

    # "Nasal bleeding" bucket (was shared by 3 topics)
    "Nasopharyngeal Carcinoma": "Neck mass with unilateral serous otitis media and epistaxis",
    "Septal Perforation": "Whistling nasal airflow with crusting and intermittent bleeding",
    "Sinonasal Malignancies": "Unilateral nasal obstruction with facial numbness or diplopia",

    # "Sleep-breathing presentation" / "Sleep-breathing symptoms" buckets (2 each)
    "Circadian Rhythm Sleep-Wake Disorders": "Sleep-wake timing mismatched with the desired schedule",
    "Sleep-Related Hypoventilation": "Daytime hypersomnolence with elevated morning CO2",
    "Narcolepsy / Central Hypersomnolence Recognition": "Irresistible daytime sleep attacks with possible cataplexy",
    "Positional OSA": "Snoring and apneas only in the supine position",
}


def apply_daily_blind_case_labels_v402(daily_curriculum_quality_module, data_module=None):
    """Update TOPIC_CASE_LABELS in place with curated, collision-free labels.

    Idempotent: safe to call on every import/reload, since it simply ensures
    every curated label is present (it never removes or overwrites an
    existing entry once written). If a data_module is supplied, verifies at
    least one of the topic names still exists in the live curriculum, so a
    silent full mismatch (e.g. every topic renamed) is caught rather than
    quietly writing labels for topics that no longer exist anywhere.
    """
    labels = daily_curriculum_quality_module.TOPIC_CASE_LABELS
    for topic, label in NEW_CASE_LABELS.items():
        labels.setdefault(topic, label)

    if data_module is not None:
        live_topics = set()
        for topics in data_module.DEEP_MODULES_V6.values():
            for t in topics:
                name = t.get("topic") if isinstance(t, dict) else t
                live_topics.add(name)
        matched = sum(1 for topic in NEW_CASE_LABELS if topic in live_topics)
        if matched == 0:
            raise RuntimeError(
                "apply_daily_blind_case_labels_v402: none of the curated "
                "topic names matched a live DEEP_MODULES_V6 topic -- topics "
                "may have been renamed."
            )
    return labels
