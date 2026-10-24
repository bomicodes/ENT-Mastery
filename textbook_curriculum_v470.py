"""v47.0 textbook-style Deep Curriculum.

Replaces the rigid Recognize/Localize/Evaluate/Manage/Advanced/Teach frame with a
textbook teaching order, adds mechanism-level content for every topic, and fixes
Deep Curriculum / Concept Hub links:

  1. Why it matters            (new: ``overview``)
  2. Anatomy & physiology      (new: ``physiology`` + existing ``localize``)
  3. Pathophysiology           (new: ``pathophysiology``)
  4. Clinical presentation     (existing ``recognize``)
  5. Diagnosis & workup        (existing ``workup``)
  6. Management                (existing ``manage``)
  7. Surgery & advanced        (existing ``operate``)
  8. Board pearls & teaching   (existing ``teach``)

The six legacy field names are left in place (many audits and older features read
them); only the presentation order/labels change.  New content lives in the
``pathophys_v470`` package, one module per domain.

Link fixes:
  * ``TOPIC_OR_MAP_V470`` is a hand-curated topic -> OR-prep slug map.  It replaces
    the old fuzzy keyword match (which landed on an actual OR card for only 37 of
    356 topics) and the Concept Hub's same-domain padding (which showed e.g. "Oral
    Cavity Composite Resection" on Glottic Cancer).
  * Concept Hub progressive cases are limited to genuinely linked cases.
  * Deep Curriculum card buttons point at the topic's own practice questions and
    the topic-specific Daily Path lesson instead of a whole-domain session.
"""
from __future__ import annotations

import importlib
import re

SECTIONS_V470 = [
    ("overview", "Why it matters"),
    ("physiology", "Anatomy & physiology"),
    ("pathophysiology", "Pathophysiology & mechanism"),
    ("recognize", "Clinical presentation"),
    ("workup", "Diagnosis & workup"),
    ("manage", "Management"),
    ("operate", "Surgery, advanced decisions & complications"),
    ("teach", "Board pearls & teaching points"),
]
NEW_FIELDS_V470 = ("overview", "physiology", "pathophysiology")
LEGACY_FIELDS_V470 = ("recognize", "localize", "workup", "manage", "operate", "teach")

CONTENT_MODULES_V470 = (
    "otology", "rhinology", "head_neck", "thyroid", "pediatric",
    "laryngology", "facial_plastics", "sleep", "general_ent",
)

# --------------------------------------------------------------------------
# Curated topic -> OR-prep slugs.  An empty list means "no dedicated operative
# module" (clinic/medical/interpretation topics) -- shown honestly rather than
# padded with unrelated procedures.
# --------------------------------------------------------------------------
TOPIC_OR_MAP_V470 = {
    # Otology / Neurotology
    "Acute Otitis Externa": [],
    "Chronic Otitis Media / Cholesteatoma": ["mastoidectomy", "tympanoplasty", "ossiculoplasty"],
    "Sudden Sensorineural Hearing Loss": [],
    "Otosclerosis / Stapes Fixation": ["stapedotomy"],
    "Vestibular Schwannoma": ["vestibular-schwannoma", "translabyrinthine-skull-base", "retrosigmoid-skull-base", "middle-fossa-skull-base"],
    "Temporal Bone Anatomy": ["mastoidectomy"],
    "Audiogram Interpretation": [],
    "Tympanometry / Acoustic Reflexes": [],
    "Eustachian Tube Dysfunction": ["tympanostomy-tubes"],
    "Tympanic Membrane Perforation": ["tympanoplasty"],
    "Ossicular Discontinuity": ["ossiculoplasty"],
    "Superior Canal Dehiscence": ["middle-fossa-skull-base"],
    "Ménière Disease": [],
    "Vestibular Migraine": [],
    "Vestibular Neuritis": [],
    "BPPV": [],
    "Facial Paralysis": ["facial-nerve-reanimation"],
    "Temporal Bone Fracture": ["tegmen-repair", "facial-nerve-reanimation"],
    "Cochlear Implant Candidacy": ["cochlear-implant"],
    "Cochlear Implant Surgery": ["cochlear-implant"],
    "Tinnitus": [],
    "Hearing Aids and Bone-Conduction Devices": [],
    "Vestibular Test Battery": [],
    "Ototoxic / Noise-Induced Hearing Loss": [],
    "Autoimmune Inner Ear Disease": [],
    "CSF Otorrhea / Temporal Encephalocele": ["tegmen-repair", "middle-fossa-skull-base"],
    "Necrotizing Otitis Externa": [],
    "Petrous Apex Lesions": [],
    "Age-Related Hearing Loss / Presbycusis": [],
    "Acute Mastoiditis / Petrous Apicitis": ["mastoidectomy", "tympanostomy-tubes"],
    "Persistent Postural-Perceptual Dizziness (PPPD)": [],
    "Patulous Eustachian Tube Dysfunction": [],
    "Perilymph Fistula / Inner-Ear Window Leak": [],
    "Cochlear Implant Failure / Revision": ["cochlear-implant"],
    "Congenital Inner-Ear Malformations": ["cochlear-implant"],
    "Auditory Neuroanatomy / Cochlear Physiology": [],
    "Audiologic Electrophysiology / ABR-OAE-ECoG": [],
    "Cortical Neuroplasticity in Hearing Loss": [],
    "Otologic Manifestations of Systemic Disease": [],
    "Hyperacusis / Decreased Sound Tolerance": [],
    "Labyrinthitis / Infections of the Labyrinth": [],
    "Central Vestibular Disorders": [],
    "Vestibular Rehabilitation": [],
    "Neurotologic Intraoperative Cranial-Nerve Monitoring": ["vestibular-schwannoma", "mastoidectomy"],
    "Lateral Skull-Base Tumor Framework": ["middle-fossa-skull-base", "retrosigmoid-skull-base", "translabyrinthine-skull-base", "jugular-foramen-tumor"],
    "External Auditory Canal Cholesteatoma": ["canalplasty"],
    "Keratosis Obturans": [],
    "EAC Exostoses / Osteoma (Canalplasty)": ["canalplasty"],
    "Ramsay Hunt Syndrome (Herpes Zoster Oticus)": [],
    "Facial Nerve Schwannoma": ["facial-nerve-reanimation", "middle-fossa-skull-base"],
    "Auditory Neuropathy Spectrum Disorder": ["cochlear-implant"],
    "Vernet Syndrome (Jugular Foramen Syndrome)": ["jugular-foramen-tumor"],
    "Gradenigo Syndrome (Petrous Apicitis)": ["mastoidectomy"],
    "Glomus Tumor / Paraganglioma": ["jugular-foramen-tumor"],
    # Rhinology / Allergy / Skull Base
    "Allergic Rhinitis": [],
    "CRS Phenotyping": ["endoscopic-sinus-surgery"],
    "AERD": ["endoscopic-sinus-surgery"],
    "Frontal Recess / Frontal Sinus": ["draf"],
    "CSF Rhinorrhea": ["csf-nasoseptal"],
    "Nasal Anatomy for Endoscopy": ["endoscopic-sinus-surgery", "maxillary-antrostomy"],
    "Inferior Turbinate Hypertrophy": ["septoplasty"],
    "Septal Deviation": ["septoplasty", "septorhino"],
    "Recurrent Acute Rhinosinusitis": ["endoscopic-sinus-surgery", "maxillary-antrostomy"],
    "CRSsNP": ["endoscopic-sinus-surgery"],
    "CRSwNP": ["endoscopic-sinus-surgery", "draf"],
    "AFRS": ["endoscopic-sinus-surgery"],
    "Invasive Fungal Rhinosinusitis": ["endoscopic-sinus-surgery"],
    "Mucocele": ["draf", "endoscopic-sinus-surgery"],
    "Sinonasal Inverted Papilloma": ["endoscopic-sinus-surgery", "maxillary-antrostomy"],
    "Sinonasal Malignancy": [],
    "Endoscopic Maxillary Antrostomy": ["maxillary-antrostomy"],
    "Ethmoidectomy": ["endoscopic-sinus-surgery"],
    "Sphenoidotomy": ["sphenoidotomy"],
    "Epistaxis Surgical Control": ["spa-ligation"],
    "Acute Bacterial Rhinosinusitis": [],
    "Odontogenic Sinusitis": ["maxillary-antrostomy"],
    "Fungal Ball": ["maxillary-antrostomy", "sphenoidotomy"],
    "Orbital Complications of Sinusitis": ["orbital-abscess"],
    "Intracranial Complications of Sinusitis": ["endoscopic-sinus-surgery", "draf"],
    "Revision FESS": ["endoscopic-sinus-surgery", "draf"],
    "Frontal Sinusotomy / Draf Procedures": ["draf"],
    "Endoscopic CSF Leak Repair / Nasoseptal Flap": ["csf-nasoseptal"],
    "Juvenile Nasopharyngeal Angiofibroma": [],
    "Olfactory Dysfunction": [],
    "Nonallergic Rhinitis / Rhinitis Medicamentosa": [],
    "Unilateral Sinonasal Disease": ["endoscopic-sinus-surgery"],
    "Pediatric Chronic Rhinosinusitis": ["adenoidectomy", "endoscopic-sinus-surgery"],
    "CF / Primary Ciliary Dyskinesia Sinonasal Disease": ["endoscopic-sinus-surgery"],
    "Immunodeficiency-Associated Chronic Rhinosinusitis": ["endoscopic-sinus-surgery"],
    "Objective Assessment of Nasal Function": [],
    "Facial Pain / Headache vs Rhinogenic Disease": [],
    "Benign Sinonasal Tumor Framework": ["endoscopic-sinus-surgery"],
    "Systemic Disease of the Nose / Sinuses": [],
    "Allergy Testing & Interpretation": [],
    "Allergen Immunotherapy — SCIT / SLIT": [],
    "Local Allergic Rhinitis": [],
    "Empty Nose Syndrome": [],
    "Silent Sinus Syndrome": ["maxillary-antrostomy"],
    "Endoscopic Pituitary / Anterior Skull Base Approach": ["sphenoidotomy", "csf-nasoseptal"],
    "Orbital Apex Syndrome": ["orbital-abscess"],
    "Anaphylaxis": [],
    "Oral Allergy Syndrome (Pollen-Food Syndrome)": [],
    # Head & Neck Oncology
    "HPV-Associated Oropharyngeal SCC": ["tors", "neck-dissection"],
    "Laryngeal SCC": ["total-laryngectomy", "conservation-laryngectomy", "transoral-laser-laryngeal-cancer"],
    "Unknown Primary with Cervical Metastasis": ["tors", "neck-dissection"],
    "Neck Dissection": ["neck-dissection"],
    "Oral Tongue SCC": ["oral-composite", "neck-dissection"],
    "Floor of Mouth SCC": ["oral-composite", "neck-dissection"],
    "Tonsil SCC": ["tors", "neck-dissection"],
    "Base of Tongue SCC": ["tors", "neck-dissection"],
    "Supraglottic Cancer": ["transoral-laser-laryngeal-cancer", "conservation-laryngectomy", "total-laryngectomy"],
    "Glottic Cancer": ["transoral-laser-laryngeal-cancer", "conservation-laryngectomy"],
    "Hypopharyngeal Cancer": ["total-laryngectomy", "neck-dissection", "free-flap-basics"],
    "Nasopharyngeal Carcinoma": [],
    "Laryngeal Preservation Decision": ["total-laryngectomy", "conservation-laryngectomy"],
    "Total Laryngectomy": ["total-laryngectomy", "tep", "pharyngocutaneous-fistula"],
    "Parapharyngeal Space Tumor": ["parotidectomy"],
    "Carotid Body Paraganglioma": [],
    "Adverse Pathology and Adjuvant Therapy": ["neck-dissection"],
    "Head & Neck Radiation Toxicity / Survivorship": [],
    "TEP and Alaryngeal Speech": ["tep"],
    "Neck Lymphoma": [],
    "Cutaneous Squamous Cell Carcinoma of the Head & Neck": ["parotidectomy", "skin-graft-face"],
    "Basal Cell Carcinoma of the Head & Neck": ["skin-graft-face", "bilobed-flap", "melolabial-flap"],
    "Cutaneous Melanoma of the Head & Neck": ["parotidectomy", "neck-dissection"],
    "Merkel Cell Carcinoma": ["parotidectomy", "neck-dissection"],
    "Recurrent / Metastatic HNSCC": [],
    "Tumor Immunology / Immunotherapy in HNSCC": [],
    "Salvage Surgery After Radiation / Chemoradiation": ["total-laryngectomy", "free-flap-basics", "pharyngocutaneous-fistula"],
    "Neck Management by Primary Site": ["neck-dissection", "central-neck"],
    "Reconstruction Selection After Head & Neck Ablation": ["free-flap-basics", "free-flap-takeback", "forehead-flap"],
    "Osteoradionecrosis of the Jaw": ["free-flap-basics"],
    "Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy": ["total-laryngectomy"],
    "Head & Neck Cancer Surveillance / Second Primaries": [],
    "Sinonasal Malignancies": [],
    "Tracheal Malignancy": ["tracheal-resection"],
    "Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer": [],
    "Radiation Therapy Principles for Head & Neck Surgeons": [],
    "Systemic Therapy Foundations in Head & Neck Cancer": [],
    "Free-Flap Monitoring / Compromise / Salvage": ["free-flap-takeback", "free-flap-basics"],
    "Open Partial / Conservation Laryngectomy": ["conservation-laryngectomy"],
    "Transoral Laser Microsurgery for Laryngeal Cancer": ["transoral-laser-laryngeal-cancer"],
    "Complications of Neck Surgery": ["neck-dissection"],
    "Sentinel Lymph Node Biopsy in Oral Cavity Cancer": ["oral-composite", "neck-dissection"],
    "Villaret Syndrome (Retroparotid Space Syndrome)": [],
    "Lip Cancer": [],
    # Thyroid / Parathyroid / Salivary
    "Thyroid Nodule": ["thyroid-lobectomy"],
    "Differentiated Thyroid Cancer": ["total-thyroidectomy", "thyroid-lobectomy", "central-neck"],
    "Primary Hyperparathyroidism": ["parathyroidectomy", "four-gland"],
    "Salivary Gland Malignancy": ["parotidectomy", "parotid-total", "submandibular-gland"],
    "Medullary Thyroid Cancer": ["total-thyroidectomy", "central-neck"],
    "Anaplastic Thyroid Cancer": ["tracheostomy"],
    "Central Neck Dissection": ["central-neck"],
    "Reoperative Thyroid Surgery": ["reop-thyroid"],
    "Secondary / Tertiary Hyperparathyroidism": ["four-gland"],
    "Four-Gland Parathyroid Exploration": ["four-gland"],
    "Sialolithiasis": ["sialendoscopy", "submandibular-gland"],
    "Sialendoscopy": ["sialendoscopy"],
    "Submandibular Gland Excision": ["submandibular-gland"],
    "Graves Disease / Toxic Goiter": ["total-thyroidectomy"],
    "Indeterminate Thyroid Cytology / Molecular Testing": ["thyroid-lobectomy"],
    "MEN2 / RET": ["total-thyroidectomy", "central-neck"],
    "Parathyroid Carcinoma": ["parathyroidectomy"],
    "Reoperative Hyperparathyroidism": ["reop-parathyroid"],
    "Hungry Bone / Post-Thyroid Calcium Management": ["total-thyroidectomy", "parathyroidectomy"],
    "Pleomorphic Adenoma / Warthin Tumor": ["parotidectomy"],
    "Acute Sialadenitis / Sjögren": ["sialendoscopy"],
    "Ranula": [],
    "Thyroid Eye Disease / Graves Ophthalmopathy": [],
    "First-Bite Syndrome": ["parotidectomy"],
    "Frey Syndrome": ["parotidectomy"],
    "Recurrent Laryngeal Nerve Injury During Thyroidectomy": ["total-thyroidectomy", "thyroid-lobectomy"],
    "Completion Thyroidectomy": ["total-thyroidectomy", "reop-thyroid"],
    "Radioactive Iodine and TSH Suppression in DTC": [],
    "Radioiodine-Refractory Differentiated Thyroid Cancer": [],
    "Primary Thyroid Lymphoma": [],
    "Familial Hyperparathyroidism and Parathyromatosis": ["four-gland", "reop-parathyroid"],
    "Salivary Adenoid Cystic Carcinoma and Perineural Spread": ["parotid-total", "facial-nerve-reanimation"],
    "Subacute (de Quervain) Thyroiditis": [],
    "Hashimoto Thyroiditis": [],
    "External Branch of the Superior Laryngeal Nerve Injury": ["total-thyroidectomy", "thyroid-lobectomy"],
    # Pediatric Otolaryngology
    "AOM / OME / Tympanostomy Decisions": ["tympanostomy-tubes", "adenoidectomy"],
    "Pediatric OSA / Adenotonsillar Disease": ["tonsillectomy-adenoidectomy"],
    "Congenital Neck Masses": ["thyroglossal", "branchial"],
    "Pediatric Airway Foreign Body": ["airway-fb", "rigid-tracheobronchoscopy"],
    "Tympanostomy Tube Indications": ["tympanostomy-tubes"],
    "Pediatric Hearing Loss Workup": ["cochlear-implant"],
    "Congenital CMV Hearing Loss": ["cochlear-implant"],
    "Thyroglossal Duct Cyst": ["thyroglossal"],
    "Branchial Cleft Anomalies": ["branchial"],
    "Lymphatic Malformation": [],
    "Laryngomalacia": ["supraglottoplasty"],
    "Supraglottoplasty": ["supraglottoplasty"],
    "Pediatric Subglottic Stenosis": ["direct-laryngoscopy-bronchoscopy", "airway-dilation", "peds-ltr", "ctr"],
    "Laryngotracheal Reconstruction": ["peds-ltr"],
    "Choanal Atresia": [],
    "Pediatric Deep Neck Infection": ["deep-neck-drain"],
    "Velopharyngeal Insufficiency": ["palatoplasty"],
    "Recurrent Tonsillitis Decision-Making": ["tonsillectomy", "tonsillectomy-adenoidectomy"],
    "Pediatric Tracheostomy / Decannulation": ["tracheostomy"],
    "Pediatric Vocal Fold Immobility": ["direct-laryngoscopy-bronchoscopy"],
    "Recurrent Respiratory Papillomatosis": ["rrp-debridement"],
    "Subglottic Hemangioma": ["direct-laryngoscopy-bronchoscopy"],
    "Tracheomalacia / Bronchomalacia": ["rigid-tracheobronchoscopy"],
    "Microtia / Aural Atresia": ["microtia-reconstruction"],
    "Pediatric Aspiration": ["direct-laryngoscopy-bronchoscopy", "laryngotracheal-cleft-repair"],
    "Congenital Hearing Loss Genetics": ["cochlear-implant"],
    "Cleft / Craniofacial Otologic-Airway Care": ["tympanostomy-tubes", "palatoplasty"],
    "Juvenile Recurrent Parotitis": ["sialendoscopy"],
    "Pediatric Head & Neck Tumors": [],
    "Pediatric Speech Disorders": [],
    "Nonobstructive Pediatric Sleep Disorders": [],
    "Cleft Lip / Palate — ENT Surgical Fundamentals": ["palatoplasty"],
    "Microtia Reconstruction": ["microtia-reconstruction"],
    "Pediatric Vestibular Disorders": [],
    "Ankyloglossia / Maxillary Frenulum": [],
    "Pediatric Reflux / Eosinophilic Esophagitis": [],
    "Laryngotracheal Cleft": ["laryngotracheal-cleft-repair"],
    "Croup vs Epiglottitis": [],
    "Button Battery Ingestion": ["button-battery", "esophageal-fb"],
    "Epiglottitis": [],
    "Pierre Robin Sequence": ["tracheostomy"],
    "Nasal Dermoid Cyst": [],
    "Infantile Hemangioma / PHACE Syndrome": [],
    # Laryngology / Voice / Swallowing
    "Unilateral Vocal Fold Paralysis": ["medialization", "injection-laryngoplasty", "arytenoid-adduction"],
    "Benign Vocal Fold Lesions": ["microflap"],
    "Dysphagia / Aspiration": ["cp-myotomy", "zenker"],
    "Subglottic / Tracheal Stenosis": ["airway-dilation", "ctr", "tracheal-resection", "adult-ltr"],
    "Laryngeal Anatomy": ["microflap"],
    "Stroboscopy Interpretation": [],
    "Vocal Fold Nodules": ["microflap"],
    "Vocal Fold Polyp / Cyst": ["microflap"],
    "Bilateral Vocal Fold Immobility": ["cordotomy", "tracheostomy"],
    "Spasmodic Dysphonia": ["laryngeal-botox"],
    "Zenker Diverticulum": ["zenker"],
    "FEES": [],
    "Modified Barium Swallow": [],
    "Medialization Thyroplasty": ["medialization"],
    "Microlaryngoscopy": ["microflap"],
    "Reinke Edema": ["microflap"],
    "Presbyphonia": ["injection-laryngoplasty"],
    "Muscle Tension Dysphonia": [],
    "Vocal Tremor": ["laryngeal-botox"],
    "Leukoplakia / Laryngeal Dysplasia": ["microflap", "transoral-laser-laryngeal-cancer"],
    "Posterior Glottic Stenosis / Arytenoid Fixation": ["cordotomy", "adult-ltr"],
    "Injection Laryngoplasty": ["injection-laryngoplasty"],
    "Arytenoid Adduction / Reinnervation": ["arytenoid-adduction"],
    "Posterior Cordotomy / Arytenoidectomy": ["cordotomy"],
    "Cricopharyngeal Dysfunction": ["cp-myotomy"],
    "Inducible Laryngeal Obstruction / PVFM": [],
    "Chronic Cough / Laryngeal Hypersensitivity": [],
    "Vocal Fold Sulcus / Scar": ["injection-laryngoplasty", "microflap"],
    "Vocal Process Granuloma": ["laryngeal-botox", "microflap"],
    "Radiation-Associated Dysphagia": ["cp-myotomy"],
    "Aspiration-Prevention Surgery": ["total-laryngectomy", "tracheostomy"],
    "Professional Voice": ["microflap"],
    "Acute / Chronic Laryngopharyngitis": [],
    "Esophageal Disease for the Otolaryngologist": ["transnasal-esophagoscopy", "zenker"],
    "Transnasal Esophagoscopy": ["transnasal-esophagoscopy"],
    "Tracheobronchial Endoscopy Principles": ["rigid-tracheobronchoscopy", "direct-laryngoscopy-bronchoscopy"],
    "Laryngopharyngeal Reflux (LPR)": ["transnasal-esophagoscopy"],
    "Laryngeal Electromyography (LEMG)": [],
    "Laryngocele": [],
    # Facial Plastics / Trauma
    "Functional Nasal Obstruction": ["septoplasty", "septorhino"],
    "ZMC / Orbital Trauma": ["zmc-orif", "orbital-floor"],
    "Mandible Fracture": ["mandible-orif"],
    "Local Flap Reconstruction": ["bilobed-flap", "melolabial-flap", "forehead-flap", "cervicofacial-flap"],
    "Nasal Fracture": ["closed-nasal-reduction"],
    "NOE Fracture": ["noe-orif"],
    "Frontal Sinus Fracture": ["frontal-sinus-trauma"],
    "Facial Nerve Reanimation": ["facial-nerve-reanimation"],
    "Mohs Defect Reconstruction": ["bilobed-flap", "melolabial-flap", "forehead-flap", "skin-graft-face"],
    "Scar Management": [],
    "Functional Septorhinoplasty": ["septorhino"],
    "Open Rhinoplasty Fundamentals": ["septorhino"],
    "Otoplasty": ["otoplasty"],
    "Forehead Flap / Nasal Reconstruction": ["forehead-flap"],
    "Le Fort / Panfacial Trauma": ["zmc-orif", "mandible-orif", "orbital-floor"],
    "Structured Facial Trauma Examination": ["zmc-orif", "orbital-floor", "mandible-orif"],
    "Mandibular Biomechanics and Occlusion": ["mandible-orif"],
    "Rhinoplasty Tip Mechanics": ["septorhino"],
    "Rhinoplasty Graft Selection": ["septorhino"],
    "Bilobed Flap": ["bilobed-flap"],
    "Cervicofacial Flap": ["cervicofacial-flap"],
    "Skin Graft Selection": ["skin-graft-face"],
    "Septal Perforation": ["septoplasty"],
    "Facial Synkinesis / Static-Dynamic Rehabilitation": ["facial-nerve-reanimation"],
    "Periocular Reconstruction": [],
    "Auricular Reconstruction": ["microtia-reconstruction"],
    "Alar Retraction / Nasal Vestibular Stenosis": ["septorhino"],
    "Aesthetic Facial Analysis": [],
    "Facial Soft-Tissue Lacerations / Burns": [],
    "Aging Face / Injectables / Resurfacing": [],
    "Hair Restoration Fundamentals": [],
    "Septal Hematoma": ["septoplasty"],
    "Laryngeal Fracture / External Laryngeal Trauma": ["laryngeal-fracture", "tracheostomy"],
    "Blepharoplasty / Eyelid Malposition (Ptosis, Ectropion, Entropion)": [],
    # Sleep Surgery
    "Adult PSG Interpretation": [],
    "DISE": ["hypoglossal-stimulator"],
    "Hypoglossal Nerve Stimulation": ["hypoglossal-stimulator"],
    "Pediatric PSG Interpretation": ["tonsillectomy-adenoidectomy"],
    "PAP Troubleshooting": [],
    "Palatal Surgery": ["reconstructive-palate"],
    "Tongue Base Surgery": ["lingual-tonsillectomy", "hyoid-genioglossus"],
    "Maxillomandibular Advancement": ["mma"],
    "Oral Appliance Therapy": [],
    "HNS Activation / Programming": ["hypoglossal-stimulator"],
    "Residual OSA After Surgery": ["hypoglossal-stimulator", "mma", "reconstructive-palate"],
    "Central Events / Hypoventilation": [],
    "Lingual Tonsil / Tongue-Base Obstruction": ["lingual-tonsillectomy"],
    "HNS Troubleshooting / Nonresponse": ["hypoglossal-stimulator"],
    "Down Syndrome Pediatric HNS": ["hypoglossal-stimulator"],
    "Central Sleep Apnea / Treatment-Emergent CSA": [],
    "Sleep-Related Hypoventilation": [],
    "Narcolepsy / Central Hypersomnolence Recognition": [],
    "Restless Legs / Periodic Limb Movement Disorders": [],
    "Circadian Rhythm Sleep-Wake Disorders": [],
    "Positional OSA": [],
    "Nasal Surgery as a CPAP-Adherence Adjunct": ["septoplasty"],
    "Adult Epiglottic Collapse / Epiglottopexy": [],
    "Tracheostomy as Definitive OSA Therapy": ["tracheostomy"],
    # General ENT / Emergencies
    "Post-Tonsillectomy Hemorrhage": ["tonsillectomy"],
    "Deep Neck Space Infection": ["deep-neck-drain"],
    "Tracheostomy Emergency": ["tracheostomy"],
    "Epistaxis": ["spa-ligation"],
    "Peritonsillar Abscess": ["pta-drainage"],
    "Ludwig Angina": ["deep-neck-drain", "tracheostomy"],
    "Angioedema": ["tracheostomy"],
    "Caustic Ingestion": [],
    "Esophageal Foreign Body": ["esophageal-fb", "button-battery"],
    "Airway Foreign Body": ["airway-fb"],
    "Postoperative Neck Hematoma": ["total-thyroidectomy"],
    "Chyle Leak": ["neck-dissection"],
    "Deep Neck Abscess Drainage": ["deep-neck-drain"],
    "Carotid Blowout Syndrome": [],
    "Esophageal Perforation / Cervical Mediastinitis": ["esophageal-fb"],
    "ENT Perioperative Anesthesia / Difficult Airway Planning": ["tracheostomy", "direct-laryngoscopy-bronchoscopy"],
    "Hemostasis / Coagulopathy / Antithrombotic Management in ENT": [],
    "ENT Fluids / Electrolytes / Nutrition": [],
    "Antimicrobial Stewardship in Otolaryngology": [],
    "Cranial Nerve Examination / Skull Base Localization": [],
    "ENT Imaging Fundamentals": [],
    "Wound Healing / Scar Biology in Head & Neck Surgery": [],
    "Grafts / Implants / Biomaterials in ENT": [],
    "Systemic / Granulomatous Disease Manifestations in ENT": [],
    "Laser / Energy Safety in Otolaryngology": ["rrp-debridement", "transoral-laser-laryngeal-cancer"],
    "Common ENT Consult Triage / Disposition": [],
    "Evidence Interpretation / Outcomes Research": [],
    "Pain Management in the Head & Neck Patient": [],
    "Geriatric Otolaryngology / Frailty": [],
    "Immunocompromised Host in Otolaryngology": [],
    "Oral Manifestations of Systemic Disease": [],
    "Lemierre Syndrome": ["deep-neck-drain"],
    "Penetrating and Blunt Neck Trauma": ["laryngeal-fracture", "tracheostomy"],
    "Cervical Necrotizing Fasciitis": ["deep-neck-drain"],
    "Ear and Nasal Foreign Body Removal": [],
}

# --------------------------------------------------------------------------
# Text hygiene for legacy fields
# --------------------------------------------------------------------------
_MARKER_LABELLED = re.compile(r"\*\*v40\.8 priority completion\s*[-—–]+\s*([^*]+?)\*\*")
_MARKER_BOLD = re.compile(r"\*\*v40\.8 priority completion\*\*\s*:?")
_MARKER_PLAIN = re.compile(r"v40\.8 priority completion\s*[:\-—–]?\s*", re.I)
# Other leaked authoring tags, e.g. "v40.7 evidence update:" / "**v44.1 evidence addition**:".
_VERSION_LABEL = re.compile(r"(?:\*\*)?\bv\d{2}\.\d+\s+([a-z][a-z \-]{2,40}?)(?:\*\*)?\s*:")
_LABEL_NAMES = {"evidence update": "Current evidence", "evidence addition": "Current evidence",
                "grading-scale addition": "Grading scale"}
_SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[*A-Z(])")


def _norm_sentence(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", re.sub(r"\*\*", "", s.lower())).strip()


def clean_field_v470(text):
    """Strip the leaked internal authoring marker and exact-duplicate sentences."""
    if not isinstance(text, str) or not text:
        return text
    out = _MARKER_LABELLED.sub(lambda m: "**" + m.group(1).strip() + "**", text)
    out = _MARKER_BOLD.sub("**Also**:", out)
    out = _MARKER_PLAIN.sub("", out)
    out = _VERSION_LABEL.sub(lambda m: "**" + _LABEL_NAMES.get(m.group(1).strip(), m.group(1).strip().capitalize()) + "**:", out)
    paragraphs = re.split(r"\n\s*\n", out)
    seen = set()
    kept_paras = []
    for para in paragraphs:
        kept = []
        for sent in _SENT_SPLIT.split(para.strip()):
            key = _norm_sentence(sent)
            if len(key) > 25 and key in seen:
                continue
            if re.search(r"\bv\d{2}\.\d+\b", sent):
                continue  # authoring meta-commentary about card versions, not teaching
            if key:
                seen.add(key)
            kept.append(sent)
        if kept:
            kept_paras.append(" ".join(kept))
    return "\n\n".join(kept_paras).strip()


# --------------------------------------------------------------------------
# Section model used by both templates
# --------------------------------------------------------------------------
def topic_sections_v470(module):
    sections = []
    for key, label in SECTIONS_V470:
        blocks = []
        main = (module.get(key) or "").strip() if isinstance(module.get(key), str) else ""
        if main:
            blocks.append({"sub": None, "text": main})
        if key == "physiology":
            loc = module.get("localize")
            if isinstance(loc, str) and loc.strip():
                blocks.append({"sub": "Clinical anatomy & localization", "text": loc.strip()})
        if blocks:
            sections.append({"key": key, "label": label, "blocks": blocks})
    return sections


def _load_content():
    import pkgutil
    import pathophys_v470
    merged = {}
    for info in sorted(pkgutil.iter_modules(pathophys_v470.__path__), key=lambda i: i.name):
        mod = importlib.import_module("pathophys_v470." + info.name)
        for topic, entry in getattr(mod, "CONTENT", {}).items():
            if topic in merged:
                raise RuntimeError("v47.0 duplicate pathophysiology entry: %s" % topic)
            merged[topic] = entry
    return merged


def install_textbook_curriculum_v470(data, app_mod, app):
    from flask import render_template, request

    content = _load_content()
    missing, cleaned = [], 0
    for domain, modules in data.DEEP_MODULES_V6.items():
        for module in modules:
            for field in LEGACY_FIELDS_V470:
                before = module.get(field)
                after = clean_field_v470(before)
                if after != before:
                    module[field] = after
                    cleaned += 1
            entry = content.get(module["topic"])
            if entry:
                for field in NEW_FIELDS_V470:
                    if entry.get(field):
                        module[field] = entry[field].strip()
            if not all(module.get(f) for f in NEW_FIELDS_V470):
                missing.append(module["topic"])

    registry = app_mod.OR_PREP_REGISTRY
    unknown_slugs = sorted({s for v in TOPIC_OR_MAP_V470.values() for s in v if s not in registry})
    if unknown_slugs:
        raise RuntimeError("v47.0 OR map references unknown OR-prep slugs: %s" % unknown_slugs)

    # ---- question index (topic -> ladder-ordered clinical challenges)
    stage_rank = {"foundation": 0, "application": 1, "senior_decision": 2}

    def questions_for(cid):
        qs = [q for q in data.CLINICAL_CHALLENGES_V119 if q.get("concept_id") == cid]
        return sorted(qs, key=lambda q: stage_rank.get(q.get("learning_stage"), 1))

    def or_cards_for(topic):
        return [dict(registry[s], slug=s) for s in TOPIC_OR_MAP_V470.get(topic, []) if s in registry]

    case_topic_map = getattr(data, "INTEGRATED_CASE_TOPIC_V98", {}) or {}

    def cases_for(cid, topic):
        out = []
        for c in data.INTEGRATED_CASES:
            if c.get("concept_id") == cid or case_topic_map.get(c.get("id")) == topic:
                out.append(c)
        return out[:4]

    def or_href(op):
        from urllib.parse import quote
        return "/case-tomorrow?q=" + quote(op.get("title", ""))

    original_context = app_mod._concept_context_v1006

    def concept_context_v470(dname, mod):
        ctx = original_context(dname, mod)
        cid = ctx.get("concept_id") or app_mod._v6_item_id(dname, mod["topic"])
        ctx["related_or"] = or_cards_for(mod["topic"])
        ctx["related_cases"] = cases_for(cid, mod["topic"])
        qs = questions_for(cid)
        ctx["related_questions"] = qs[:8]
        ctx["question_total"] = len(qs)
        ctx["sections"] = topic_sections_v470(mod)
        ctx["concept_id"] = cid
        ctx["module"] = mod
        return ctx

    app_mod._concept_context_v1006 = concept_context_v470

    # ---- Deep Curriculum: lightweight index + lazily loaded topic bodies
    def curriculum_depth():
        evidence = getattr(data, "EVIDENCE_HIERARCHY_V6", [])
        topic = request.args.get("topic")
        if topic:
            dname, mod = app_mod._find_deep_module_v94(request.args.get("domain", ""), topic)
            if not mod:
                return ("Topic not found", 404)
            return render_template("curriculum_depth.html", partial_topic=True,
                                   modules={}, evidence=evidence, **_card_ctx(dname, mod))
        cards = {d: [_card_meta(d, m) for m in mods] for d, mods in data.DEEP_MODULES_V6.items()}
        return render_template("curriculum_depth.html", partial_topic=False,
                               modules=data.DEEP_MODULES_V6, cards=cards, evidence=evidence)

    def _card_meta(dname, mod):
        cid = app_mod._v6_item_id(dname, mod["topic"])
        return {"topic": mod["topic"], "cid": cid,
                "qcount": sum(1 for q in data.CLINICAL_CHALLENGES_V119 if q.get("concept_id") == cid),
                "ors": or_cards_for(mod["topic"])}

    def _card_ctx(dname, mod):
        meta = _card_meta(dname, mod)
        return {"m": mod, "domain": dname, "meta": meta, "sections": topic_sections_v470(mod)}

    app.view_functions["curriculum_depth"] = curriculum_depth
    app.jinja_env.globals["topic_sections_v470"] = topic_sections_v470
    app.jinja_env.globals["or_href_v470"] = or_href

    data.TOPIC_OR_MAP_V470 = TOPIC_OR_MAP_V470
    data.SECTIONS_V470 = SECTIONS_V470
    data.textbook_questions_for_v470 = questions_for
    data.textbook_or_cards_for_v470 = or_cards_for
    data.textbook_cases_for_v470 = cases_for
    result = {"legacy_fields_cleaned": cleaned, "topics_missing_new_content": missing,
              "or_mapped_topics": sum(1 for v in TOPIC_OR_MAP_V470.values() if v)}
    data.TEXTBOOK_CURRICULUM_V470 = result
    return result
