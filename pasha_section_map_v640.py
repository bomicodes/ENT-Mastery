"""v64.0: explicit Pasha 6e section -> curriculum topic map.

The Pasha Review quizzes used to pick questions by keyword and only from the chapter's own
domain, padding thin sections with unrelated questions (Salivary Gland Malignancy was quizzing
tonsil bleeds). Each book section now lists the curriculum topics that cover what that section of
Pasha & Golub 6e actually teaches, across domains (salivary questions live under Thyroid /
Parathyroid / Salivary, trauma under Facial Plastics / Trauma, and so on). Questions are drawn
from those topics only; keyword matching is used only to rank within them.

v64.1 (book audit of all 88 sections, 11 reviewers): topics were moved back to the section whose
book text teaches them, so a topic usually has one home section per chapter (for example vascular
anomalies to peds-general-sleep, airway foreign body and caustics to peds-laryngoesoph, bilateral
vocal fold immobility to neurogenic-voice, unknown primary to other-neoplasms, SSNHL/AIED/ANSD to
noninfectious-ear). In each list the most section-central topics come first, because the quiz
fills round-robin in list order up to 20 questions; for duplicate topic-name pairs the larger
topic is listed first and the small variant last. Chapter-wide image topics (for example
"Image review: Facial & Orbital Trauma CT") are listed in each fracture section so the keyword
ranking can place each image item in its own section.

Sections with an empty list rely only on the section-specific questions in
pasha_extra_questions_v640, because no curriculum topic covers them: sleep physiology, jaw and bone
pathology, otologic visualization, and the facial aesthetic sections (rhytidoplasty, brow lift,
liposurgery, facelift complications, chin and malar augmentation).
"""

SECTION_TOPICS_V640 = {
    # 1 Allergy and Rhinology
    "nose-sinus-anatomy": ["Nasal Anatomy for Endoscopy", "Frontal Recess / Frontal Sinus", "Image review: Sinus CT & Pre-FESS Planning"],
    "nose-sinus-physiology": ["CF / Primary Ciliary Dyskinesia Sinonasal Disease", "Olfactory Dysfunction"],
    "nasal-obstruction": ["Objective Assessment of Nasal Function", "Unilateral Sinonasal Disease", "Nonallergic Rhinitis / Rhinitis Medicamentosa", "CSF Rhinorrhea"],
    "nasal-diseases": ["Nasal Valve Collapse", "Functional Nasal Obstruction", "Septal Deviation", "Septal Perforation", "Septal Hematoma", "Inferior Turbinate Hypertrophy", "Epistaxis", "Epistaxis Surgical Control", "Olfactory Dysfunction", "Sinonasal Inverted Papilloma", "Benign Sinonasal Tumor Framework", "Juvenile Nasopharyngeal Angiofibroma", "Systemic Disease of the Nose / Sinuses", "Systemic / Granulomatous Disease Manifestations in ENT", "Ear and Nasal Foreign Body Removal", "CSF Rhinorrhea", "Posterior Epistaxis"],
    "allergy-rhinitis": ["Allergic Rhinitis", "Allergy Testing & Interpretation", "Allergen Immunotherapy — SCIT / SLIT", "Nonallergic Rhinitis / Rhinitis Medicamentosa", "Anaphylaxis", "Empty Nose Syndrome", "Systemic Disease of the Nose / Sinuses", "Image review: Allergy Testing & Rhinitis"],
    "sinus-disease": ["CRS Phenotyping", "Acute Bacterial Rhinosinusitis", "Recurrent Acute Rhinosinusitis", "CRSsNP", "CRSwNP", "AERD", "AFRS", "Fungal Ball", "Invasive Fungal Rhinosinusitis", "Odontogenic Sinusitis", "Orbital Complications of Sinusitis", "Intracranial Complications of Sinusitis", "Orbital Apex Syndrome", "Mucocele", "Silent Sinus Syndrome", "Unilateral Sinonasal Disease", "Facial Pain / Headache vs Rhinogenic Disease", "CF / Primary Ciliary Dyskinesia Sinonasal Disease", "Immunocompromised Host in Otolaryngology", "Acute Invasive Fungal Rhinosinusitis", "Orbital Complication of Sinusitis", "Orbital Cellulitis vs Preseptal Cellulitis", "Intracranial Complication of Sinusitis", "Frontal Sinus Mucocele"],
    "sinus-surgery": ["Endoscopic Maxillary Antrostomy", "Ethmoidectomy", "Sphenoidotomy", "Frontal Sinusotomy / Draf Procedures", "Revision FESS", "Image review: Sinus CT & Pre-FESS Planning", "Endoscopic CSF Leak Repair / Nasoseptal Flap", "Endoscopic Pituitary / Anterior Skull Base Approach"],
    "immunology": ["Immunodeficiency-Associated Chronic Rhinosinusitis", "Immunocompromised Host in Otolaryngology"],
    # 2 Laryngology
    "laryngeal-anatomy": ["Laryngeal Anatomy"],
    "dysphonia": ["Stroboscopy Interpretation", "Image review: Laryngeal Endoscopy & Stroboscopy", "Professional Voice", "Laryngopharyngeal Reflux (LPR)", "Muscle Tension Dysphonia", "Acute / Chronic Laryngopharyngitis"],
    "upper-airway-obstruction": ["Tracheostomy Emergency", "Subglottic / Tracheal Stenosis", "Idiopathic Subglottic Stenosis", "Airway Foreign Body", "ENT Perioperative Anesthesia / Difficult Airway Planning", "Tracheobronchial Endoscopy Principles", "Image review: Airway & Bronchoscopy", "Tracheal Malignancy"],
    "benign-larynx": ["Benign Vocal Fold Lesions", "Vocal Fold Nodules", "Vocal Fold Polyp / Cyst", "Reinke Edema", "Vocal Fold Sulcus / Scar", "Vocal Process Granuloma", "Laryngocele", "Acute / Chronic Laryngopharyngitis", "Laryngopharyngeal Reflux (LPR)", "Angioedema", "Presbyphonia", "Systemic / Granulomatous Disease Manifestations in ENT", "Microlaryngoscopy", "Vocal Fold Nodules, Polyps, and Cysts", "Laryngeal Granuloma"],
    "neurogenic-voice": ["Unilateral Vocal Fold Paralysis", "Bilateral Vocal Fold Immobility", "Arytenoid Dislocation vs RLN Paralysis", "Injection Laryngoplasty", "Medialization Thyroplasty", "Arytenoid Adduction / Reinnervation", "Laryngeal Electromyography (LEMG)", "Spasmodic Dysphonia", "Vocal Tremor", "External Branch of the Superior Laryngeal Nerve Injury", "Posterior Glottic Stenosis / Arytenoid Fixation", "Posterior Cordotomy / Arytenoidectomy", "Inducible Laryngeal Obstruction / PVFM", "Muscle Tension Dysphonia", "Bilateral Vocal Fold Paralysis", "Posterior Glottic Stenosis"],
    "swallowing": ["Dysphagia / Aspiration", "Modified Barium Swallow", "FEES", "Image review: Swallow Study (MBS / FEES)", "Zenker Diverticulum", "Cricopharyngeal Dysfunction", "Esophageal Disease for the Otolaryngologist", "Transnasal Esophagoscopy", "Radiation-Associated Dysphagia", "Aspiration-Prevention Surgery", "Aspiration after Head and Neck Surgery", "Esophageal Foreign Body", "Caustic Ingestion", "Esophageal Perforation / Cervical Mediastinitis", "Laryngopharyngeal Reflux (LPR)", "Eagle Syndrome"],
    # 3 Endocrinology
    "thyroid": ["Thyroid Nodule", "Indeterminate Thyroid Cytology / Molecular Testing", "Image review: Thyroid & Neck Ultrasound", "Differentiated Thyroid Cancer", "Differentiated Thyroid Cancer: Active Surveillance", "Radioactive Iodine and TSH Suppression in DTC", "Radioiodine-Refractory Differentiated Thyroid Cancer", "Medullary Thyroid Cancer", "MEN2 / RET", "Anaplastic Thyroid Cancer", "Primary Thyroid Lymphoma", "Graves Disease / Toxic Goiter", "Thyroid Eye Disease / Graves Ophthalmopathy", "Hashimoto Thyroiditis", "Subacute (de Quervain) Thyroiditis", "Thyroid Storm / Airway Compression", "Recurrent Laryngeal Nerve Injury During Thyroidectomy", "External Branch of the Superior Laryngeal Nerve Injury", "Central Neck Dissection", "Completion Thyroidectomy", "Reoperative Thyroid Surgery", "Postoperative Neck Hematoma", "Post-thyroidectomy Neck Hematoma", "Medullary Thyroid Carcinoma", "Recurrent Laryngeal Nerve / Thyroidectomy"],
    "parathyroid": ["Primary Hyperparathyroidism", "Parathyroid Localization", "Four-Gland Parathyroid Exploration", "Secondary / Tertiary Hyperparathyroidism", "Familial Hyperparathyroidism and Parathyromatosis", "Hungry Bone / Post-Thyroid Calcium Management", "Reoperative Hyperparathyroidism", "Parathyroid Carcinoma", "Hungry Bone Syndrome"],
    # 4 Sleep
    "sleep-physiology": [],
    "psg": ["Adult PSG Interpretation", "Central Events / Hypoventilation", "Narcolepsy / Central Hypersomnolence Recognition"],
    "sdb": ["Adult OSA", "PAP Troubleshooting", "Positional OSA", "Oral Appliance Therapy", "DISE", "Central Sleep Apnea / Treatment-Emergent CSA", "Sleep-Related Hypoventilation", "Central Events / Hypoventilation", "Palatal Surgery", "Tongue Base Surgery", "Lingual Tonsil / Tongue-Base Obstruction", "Adult Epiglottic Collapse / Epiglottopexy", "Hypoglossal Nerve Stimulation", "HNS Activation / Programming", "HNS Troubleshooting / Nonresponse", "Maxillomandibular Advancement", "Nasal Surgery as a CPAP-Adherence Adjunct", "Tracheostomy as Definitive OSA Therapy", "Residual OSA After Surgery", "Palatal Surgery Selection for OSA", "Mandibular Advancement Device", "Drug-Induced Sleep Endoscopy", "Residual OSA after Surgery", "Central Sleep Apnea", "Treatment-Emergent Central Sleep Apnea", "Hypoventilation"],
    "other-sleep": ["Narcolepsy / Central Hypersomnolence Recognition", "Restless Legs / Periodic Limb Movement Disorders", "Circadian Rhythm Sleep-Wake Disorders"],
    # 5 General Otolaryngology
    "oral-benign": ["Oral Manifestations of Systemic Disease"],
    "salivary-anatomy": ["Frey Syndrome", "First-Bite Syndrome", "Submandibular Gland Excision"],
    "salivary-pathology": ["Sialolithiasis", "Acute Sialadenitis / Sjögren", "Sialendoscopy", "Ranula"],
    "benign-salivary": ["Pleomorphic Adenoma / Warthin Tumor"],
    "salivary-malignancy": ["Salivary Gland Malignancy", "Salivary Adenoid Cystic Carcinoma and Perineural Spread", "Cutaneous SCC / Parotid Metastasis", "Parotid Malignancy"],
    "salivary-surgery": ["Submandibular Gland Excision", "Frey Syndrome", "First-Bite Syndrome", "Pleomorphic Adenoma / Warthin Tumor"],
    "jaw-bone": [],
    "neck-masses": ["Adult Neck Mass / HPV OPSCC", "Neck Lymphoma"],
    "deep-neck": ["Deep Neck Space Infection", "Deep Neck Abscess Drainage", "Ludwig Angina", "Retropharyngeal Abscess", "Pediatric Deep Neck Infection", "Cervical Necrotizing Fasciitis", "Esophageal Perforation / Cervical Mediastinitis"],
    "systemic": ["Systemic / Granulomatous Disease Manifestations in ENT", "Systemic Disease of the Nose / Sinuses", "Otologic Manifestations of Systemic Disease", "Oral Manifestations of Systemic Disease"],
    # 6 Head and Neck Cancer
    "staging": ["Image review: Head & Neck CT / MRI Staging", "Oral Tongue SCC", "HPV-Associated Oropharyngeal SCC", "Glottic Cancer", "Supraglottic Cancer", "Hypopharyngeal Cancer", "Cutaneous Melanoma of the Head & Neck"],
    "hnc-intro": ["Head & Neck Cancer Surveillance / Second Primaries", "ENT Imaging Fundamentals", "Image review: Head & Neck Pathology", "Unknown Primary Head and Neck Cancer", "Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer", "Evidence Interpretation / Outcomes Research"],
    "chemoradiation": ["Radiation Therapy Principles for Head & Neck Surgeons", "Systemic Therapy Foundations in Head & Neck Cancer", "Head & Neck Radiation Toxicity / Survivorship", "Adverse Pathology and Adjuvant Therapy", "Laryngeal Preservation Decision", "Recurrent / Metastatic HNSCC", "Tumor Immunology / Immunotherapy in HNSCC", "Osteoradionecrosis of the Jaw", "Radiation-Associated Dysphagia", "Adjuvant Therapy After Head and Neck Cancer Surgery", "Osteoradionecrosis"],
    "neck-cancer": ["Neck Dissection", "Neck Management by Primary Site", "Complications of Neck Surgery", "Postoperative Neck Hematoma", "Carotid Blowout Syndrome", "Neck Dissection Complications"],
    "oral-cancer": ["Oral Tongue SCC", "Floor of Mouth SCC", "Lip Cancer", "Sentinel Lymph Node Biopsy in Oral Cavity Cancer", "Reconstruction Selection After Head & Neck Ablation"],
    "oropharynx": ["HPV-Associated Oropharyngeal SCC", "Tonsil SCC", "Base of Tongue SCC", "Adult Neck Mass / HPV OPSCC", "Reconstruction Selection After Head & Neck Ablation"],
    "hypopharynx": ["Hypopharyngeal Cancer", "Laryngeal Preservation Decision", "Total Laryngectomy"],
    "larynx-cancer": ["Laryngeal SCC", "Glottic Cancer", "Supraglottic Cancer", "Laryngeal Preservation Decision", "Transoral Laser Microsurgery for Laryngeal Cancer", "Open Partial / Conservation Laryngectomy", "Total Laryngectomy", "Salvage Laryngectomy", "Salvage Surgery After Radiation / Chemoradiation", "TEP and Alaryngeal Speech", "Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy", "Leukoplakia / Laryngeal Dysplasia", "Laryngeal Cancer", "Supraglottic SCC", "Salvage Surgery After Chemoradiation"],
    "nasopharynx": ["Nasopharyngeal Carcinoma"],
    "sinonasal-cancer": ["Sinonasal Malignancy", "Sinonasal Malignancies"],
    "cutaneous": ["Basal Cell Carcinoma of the Head & Neck", "Cutaneous Squamous Cell Carcinoma of the Head & Neck", "Cutaneous Melanoma of the Head & Neck", "Merkel Cell Carcinoma", "Image review: Skin Lesions & Facial Reconstruction", "Cutaneous SCC / Parotid Metastasis", "Perineural Spread", "Cutaneous Squamous Cell Carcinoma"],
    "other-neoplasms": ["Unknown Primary with Cervical Metastasis", "Parapharyngeal Space Tumor", "Neck Lymphoma", "Villaret Syndrome (Retroparotid Space Syndrome)", "Unknown Primary Head and Neck Cancer", "Unknown Primary"],
    "robotic": ["Tonsil SCC", "Base of Tongue SCC", "Tongue Base Surgery"],
    # 7 Otology
    "hearing-balance-anatomy": ["Temporal Bone Anatomy", "Auditory Neuroanatomy / Cochlear Physiology", "Congenital Inner-Ear Malformations", "Image review: Temporal Bone CT / MRI"],
    "audiology": ["Audiogram Interpretation", "Tympanometry / Acoustic Reflexes", "Audiologic Electrophysiology / ABR-OAE-ECoG", "Image review: Audiology", "Image review: Audiologic Electrophysiology", "Hearing Aids and Bone-Conduction Devices", "Cochlear Implant Candidacy", "Cochlear Implant Surgery", "Cochlear Implant Failure / Revision", "Cortical Neuroplasticity in Hearing Loss"],
    "hearing-loss-tinnitus": ["Tinnitus", "Sudden Sensorineural Hearing Loss", "Patulous Eustachian Tube Dysfunction", "Hyperacusis / Decreased Sound Tolerance", "Ototoxic / Noise-Induced Hearing Loss", "Vestibular Schwannoma"],
    "ear-infection": ["Acute Otitis Externa", "Necrotizing Otitis Externa", "Eustachian Tube Dysfunction", "Chronic Otitis Media / Cholesteatoma", "Acute Mastoiditis / Petrous Apicitis", "Labyrinthitis / Infections of the Labyrinth", "Vestibular Neuritis", "Ossicular Discontinuity", "AOM / OME / Tympanostomy Decisions"],
    "noninfectious-ear": ["Otosclerosis / Stapes Fixation", "Cholesteatoma", "External Auditory Canal Cholesteatoma", "Keratosis Obturans", "EAC Exostoses / Osteoma (Canalplasty)", "Tympanic Membrane Perforation", "Vestibular Schwannoma", "Glomus Tumor / Paraganglioma", "Carotid Body Paraganglioma", "Lateral Skull-Base Tumor Framework", "Petrous Apex Lesions", "Sudden Sensorineural Hearing Loss", "Age-Related Hearing Loss / Presbycusis", "Autoimmune Inner Ear Disease", "Ototoxic / Noise-Induced Hearing Loss", "Auditory Neuropathy Spectrum Disorder", "Otologic Manifestations of Systemic Disease", "Neurotologic Intraoperative Cranial-Nerve Monitoring", "Superior Semicircular Canal Dehiscence", "Otosclerosis"],
    "otologic-visualization": [],
    "vestibular": ["BPPV", "Vestibular Neuritis", "Ménière Disease", "Vestibular Migraine", "Superior Canal Dehiscence", "Persistent Postural-Perceptual Dizziness (PPPD)", "Central Vestibular Disorders", "Vestibular Test Battery", "Image review: Vestibular", "Vestibular Rehabilitation", "Perilymph Fistula / Inner-Ear Window Leak"],
    "facial-nerve": ["Facial Paralysis", "Image review: Facial Nerve", "Ramsay Hunt Syndrome (Herpes Zoster Oticus)", "Facial Nerve Schwannoma", "Facial Nerve Reanimation", "Static Facial Reanimation", "Dynamic Facial Reanimation", "Facial Synkinesis / Static-Dynamic Rehabilitation", "Temporal Bone Fracture", "Facial Nerve Paralysis"],
    # 8 Facial Plastics
    "wound-healing": ["Wound Healing / Scar Biology in Head & Neck Surgery"],
    "flaps": ["Free-Flap Monitoring / Compromise / Salvage", "Reconstruction Selection After Head & Neck Ablation", "Local Flap Reconstruction", "Bilobed Flap", "Cervicofacial Flap", "Forehead Flap / Nasal Reconstruction", "Free Flap Monitoring and Salvage"],
    "grafts": ["Grafts / Implants / Biomaterials in ENT", "Skin Graft Selection"],
    "facial-reconstruction": ["Mohs Defect Reconstruction", "Local Flap Reconstruction", "Forehead Flap / Nasal Reconstruction", "Bilobed Flap", "Cervicofacial Flap", "Periocular Reconstruction", "Auricular Reconstruction", "Reconstruction Selection After Head & Neck Ablation", "Image review: Skin Lesions & Facial Reconstruction"],
    "facial-aesthetics": ["Aesthetic Facial Analysis"],
    "rhinoplasty": ["Open Rhinoplasty Fundamentals", "Rhinoplasty Tip Mechanics", "Nasal Tip Support", "Rhinoplasty Graft Selection", "Functional Septorhinoplasty", "Alar Retraction / Nasal Vestibular Stenosis"],
    "otoplasty": ["Otoplasty"],
    "blepharoplasty": ["Blepharoplasty / Eyelid Malposition (Ptosis, Ectropion, Entropion)"],
    "rhytidoplasty": [],
    "brow": [],
    "lipo": [],
    "facelift-complications": [],
    "augmentation": [],
    "resurfacing": ["Aging Face / Injectables / Resurfacing"],
    "fillers": ["Aging Face / Injectables / Resurfacing"],
    "alopecia": ["Hair Restoration Fundamentals"],
    "scar-revision": ["Scar Management"],
    # 9 Pediatrics
    "peds-encounter": ["Pediatric Speech Disorders"],
    "peds-general-sleep": ["Pediatric OSA / Adenotonsillar Disease", "Pediatric PSG Interpretation", "Recurrent Tonsillitis Decision-Making", "Peritonsillar Abscess", "Post-Tonsillectomy Hemorrhage", "Infantile Hemangioma / PHACE Syndrome", "Lymphatic Malformation", "Pediatric Residual OSA", "Sleep-Disordered Breathing in Down Syndrome", "Down Syndrome Pediatric HNS", "Nonobstructive Pediatric Sleep Disorders", "Image review: PSG / Sleep Study", "Pediatric OSA", "Post-tonsillectomy Hemorrhage"],
    "peds-rhinology": ["Choanal Atresia", "Nasal Dermoid Cyst", "Pediatric Chronic Rhinosinusitis", "CF / Primary Ciliary Dyskinesia Sinonasal Disease"],
    "peds-laryngoesoph": ["Laryngomalacia", "Supraglottoplasty", "Pediatric Subglottic Stenosis", "Subglottic Hemangioma", "Pediatric Vocal Fold Immobility", "Laryngotracheal Cleft", "Recurrent Respiratory Papillomatosis", "Tracheomalacia / Bronchomalacia", "Pediatric Airway Foreign Body", "Airway Foreign Body", "Button Battery Ingestion", "Caustic Ingestion", "Esophageal Foreign Body", "Croup vs Epiglottitis", "Pediatric Aspiration", "Pediatric Reflux / Eosinophilic Esophagitis", "Laryngotracheal Reconstruction", "Pediatric Tracheostomy / Decannulation", "Subglottic Stenosis", "Congenital Vocal Fold Paralysis"],
    "peds-salivary": ["Juvenile Recurrent Parotitis", "Sialolithiasis", "Sialendoscopy"],
    "peds-otology": ["AOM / OME / Tympanostomy Decisions", "Tympanostomy Tube Indications", "Pediatric Hearing Loss Workup", "Congenital Hearing Loss Genetics", "Congenital CMV Hearing Loss", "Congenital Inner-Ear Malformations", "Cochlear Implant Candidacy", "Hearing Aids and Bone-Conduction Devices", "Pediatric Vestibular Disorders", "Image review: Pediatric Congenital Imaging", "Recurrent AOM / Tympanostomy"],
    "peds-syndromes": ["Pierre Robin Sequence", "Sleep-Disordered Breathing in Down Syndrome", "Down Syndrome Pediatric HNS", "Image review: Pediatric Congenital Imaging"],
    "peds-hn-surgery": ["Branchial Cleft Anomalies", "Thyroglossal Duct Cyst", "Congenital Neck Masses", "Pediatric Head & Neck Tumors", "Pediatric Deep Neck Infection", "Retropharyngeal Abscess", "Ranula", "Lemierre Syndrome", "Image review: Pediatric Congenital Imaging", "Congenital Neck Mass"],
    "peds-reconstruction": ["Cleft Lip / Palate — ENT Surgical Fundamentals", "Velopharyngeal Insufficiency", "Cleft / Craniofacial Otologic-Airway Care", "Microtia Reconstruction", "Microtia / Aural Atresia", "Otoplasty", "Auricular Reconstruction"],
    "peds-trauma": ["Septal Hematoma", "Nasal Fracture", "Mandible Fracture"],
    # 10 Trauma
    "trauma-eval": ["Structured Facial Trauma Examination"],
    "mandible": ["Mandible Fracture", "Mandibular Biomechanics and Occlusion", "Image review: Facial & Orbital Trauma CT"],
    "maxilla": ["Le Fort / Panfacial Trauma", "Image review: Facial & Orbital Trauma CT"],
    "zmc-orbit": ["ZMC / Orbital Trauma", "Image review: Facial & Orbital Trauma CT", "Orbital Floor Fracture", "Zygomaticomaxillary Complex Fracture"],
    "frontal-noe": ["Frontal Sinus Fracture", "NOE Fracture", "Frontal Sinus Fracture Decision Model", "NOE Fracture Mechanics", "Frontal Sinus Posterior Table Fracture", "Image review: Facial & Orbital Trauma CT"],
    "nasal-fracture": ["Nasal Fracture", "Septal Hematoma", "Image review: Facial & Orbital Trauma CT"],
    "temporal-trauma": ["Temporal Bone Fracture", "Ossicular Discontinuity", "Tympanic Membrane Perforation", "Temporal Bone Trauma"],
    "penetrating": ["Penetrating and Blunt Neck Trauma"],
    "laryngeal-trauma": ["Laryngeal Fracture / External Laryngeal Trauma", "Arytenoid Dislocation vs RLN Paralysis"],
    "soft-tissue": ["Facial Soft-Tissue Lacerations / Burns", "Facial Nerve Laceration"],
}
