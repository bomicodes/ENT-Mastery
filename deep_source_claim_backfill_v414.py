"""ENT Mastery v41.4 -- claim-specific source backfill.

Adds a traceable topic-level reference to each canonical topic that still had
only the v40.8 domain textbook locators.  Keys include the domain so repeated
topic names cannot cross-wire.  Existing provenance is preserved and deduped.

The source list was reconciled against the named guideline/classification or
landmark publication.  Narrative-review entries are explicitly labelled as
practice syntheses and do not imply a universal guideline or threshold.
"""
from copy import deepcopy


S = {
"Otology / Neurotology": {
"Audiogram Interpretation": "American Speech-Language-Hearing Association. Guidelines for Manual Pure-Tone Threshold Audiometry. 2005.",
"Tympanometry / Acoustic Reflexes": "Jerger J. Clinical experience with impedance audiometry. Arch Otolaryngol. 1970;92:311-324.",
"Tympanic Membrane Perforation": "Harvie M et al. Traumatic tympanic membrane perforations. CMAJ. 2024;196:E100; consistent with Pasha & Golub 6e and K.J. Lee 12e conservative management and referral principles.",
"Ossicular Discontinuity": "Kartush JM. Ossicular chain reconstruction: capitulum to malleus. Otolaryngol Clin North Am. 1994;27:689-715.",
"Ménière Disease": "Lopez-Escamez JA et al. Diagnostic criteria for Menière's disease: Bárány Society consensus. J Vestib Res. 2015;25:1-7; Basura GJ et al. Clinical Practice Guideline: Ménière's Disease. Otolaryngol Head Neck Surg. 2020;162(2 Suppl):S1-S55.",
"Vestibular Migraine": "Lempert T et al. Vestibular migraine: Diagnostic criteria (Update), literature update 2021. Bárány Society/IHS consensus. J Vestib Res. 2022;32:1-6 (criteria unchanged from 2012).",
"Tinnitus": "Tunkel DE et al. Clinical Practice Guideline: Tinnitus. Otolaryngol Head Neck Surg. 2014;151(2 Suppl):S1-S40.",
"Hearing Aids and Bone-Conduction Devices": "US Food and Drug Administration. Medical Devices; Ear, Nose, and Throat Devices; Establishing Over-the-Counter Hearing Aids. Final rule, 87 FR 50698 (2022).",
"Vestibular Test Battery": "Strupp M et al. Vestibular Disorders: Diagnosis, New Classification and Treatment. Dtsch Arztebl Int. 2020;117:300-310; Pasha & Golub 6e, ch 7, pp 412-416. Interpret vHIT/VEMP against laboratory- and age-specific norms rather than one universal cutoff.",
"Ototoxic / Noise-Induced Hearing Loss": "NIOSH. Criteria for a Recommended Standard: Occupational Noise Exposure. 1998; ASHA. Audiologic Management of Individuals Receiving Cochleotoxic Drug Therapy. 1994.",
"Autoimmune Inner Ear Disease": "McCabe BF. Autoimmune sensorineural hearing loss. Ann Otol Rhinol Laryngol. 1979;88:585-589.",
"CSF Otorrhea / Temporal Encephalocele": "Oakley GM et al. Management of cerebrospinal fluid rhinorrhea: an evidence-based review with recommendations. Int Forum Allergy Rhinol. 2016;6:17-24 (CSF biomarker and localization principles also apply to otologic leaks).",
"Petrous Apex Lesions": "Isaacson B. Cholesterol granuloma and other petrous apex lesions. Otolaryngol Clin North Am. 2015;48:361-373.",
"Acute Mastoiditis / Petrous Apicitis": "Cassano P et al. Acute mastoiditis in children. Acta Biomed. 2020;91(Suppl 1):54-59; Gradenigo syndrome remains the classic petrous-apicitis localization.",
"Persistent Postural-Perceptual Dizziness (PPPD)": "Staab JP et al. Diagnostic criteria for persistent postural-perceptual dizziness: Bárány Society consensus. J Vestib Res. 2017;27:191-208.",
"Perilymph Fistula / Inner-Ear Window Leak": "Sarna B et al. Perilymphatic fistula: a review of classification, etiology, diagnosis, and treatment. Front Neurol. 2020;11:1046.",
"Congenital Inner-Ear Malformations": "Sennaroglu L, Bajin MD. Classification and current management of inner ear malformations. Balkan Med J. 2017;34:397-411.",
},
"Rhinology / Allergy / Skull Base": {
"Nasal Anatomy for Endoscopy": "Stammberger H, Kennedy DW. Paranasal sinuses: anatomic terminology and nomenclature. Ann Otol Rhinol Laryngol Suppl. 1995;167:7-16.",
"Inferior Turbinate Hypertrophy": "Cingi C et al. Surgical interventions for inferior turbinate hypertrophy: a comprehensive review. Clin Otolaryngol. 2010;35:25-31.",
"Septal Deviation": "Mladina R et al. The clinical significance of nasal septal deformities in relation to rhinosinusitis. Rhinology. 2008;46:283-288.",
"Recurrent Acute Rhinosinusitis": "Fokkens WJ et al. European Position Paper on Rhinosinusitis and Nasal Polyps 2020. Rhinology. 2020;58(Suppl S29):1-464.",
"Sinonasal Inverted Papilloma": "Krouse JH. Development of a staging system for inverted papilloma. Laryngoscope. 2000;110:965-968.",
"Endoscopic Maxillary Antrostomy": "Stammberger H. Endoscopic endonasal surgery—the Messerklinger technique. Otolaryngol Head Neck Surg. 1986;94:143-156.",
"Ethmoidectomy": "Stammberger H. Endoscopic endonasal surgery—the Messerklinger technique. Otolaryngol Head Neck Surg. 1986;94:143-156.",
"Frontal Sinusotomy / Draf Procedures": "Draf W. Endonasal micro-endoscopic frontal sinus surgery: the Fulda concept. Oper Tech Otolaryngol Head Neck Surg. 1991;2:234-240.",
"Juvenile Nasopharyngeal Angiofibroma": "Radkowski D et al. Angiofibroma: changes in staging and treatment. Arch Otolaryngol Head Neck Surg. 1996;122:122-129.",
"CF / Primary Ciliary Dyskinesia Sinonasal Disease": "Lucas JS et al. European Respiratory Society guidelines for diagnosis of primary ciliary dyskinesia. Eur Respir J. 2017;49:1601090.",
"Immunodeficiency-Associated Chronic Rhinosinusitis": "Chiarella SE, Grammer LC. Immune deficiency in chronic rhinosinusitis: screening and treatment. Expert Rev Clin Immunol. 2017;13:117-123.",
},
"Thyroid / Parathyroid / Salivary": {
"Thyroid Nodule": "Haugen BR et al. 2015 ATA Management Guidelines for Thyroid Nodules and Differentiated Thyroid Cancer. Thyroid. 2016;26:1-133.",
"Anaplastic Thyroid Cancer": "Bible KC et al. 2021 ATA Guidelines for Management of Patients with Anaplastic Thyroid Cancer. Thyroid. 2021;31:337-386.",
"Central Neck Dissection": "Carty SE et al. Consensus statement on terminology and classification of central neck dissection for thyroid cancer. Thyroid. 2009;19:1153-1158.",
"Reoperative Thyroid Surgery": "American Head and Neck Society Endocrine Surgery Committee. Evaluation and management of recurrent well-differentiated thyroid carcinoma in the neck. Head Neck. 2016;38:693-704.",
"Four-Gland Parathyroid Exploration": "Wilhelm SM et al. AAES Guidelines for Definitive Management of Primary Hyperparathyroidism. JAMA Surg. 2016;151:959-968.",
"Submandibular Gland Excision": "Beahm DD et al. Surgical approaches to the submandibular gland: a review of literature. Int J Surg. 2009;7:503-509.",
"Indeterminate Thyroid Cytology / Molecular Testing": "Ali SZ, Cibas ES, eds. The Bethesda System for Reporting Thyroid Cytopathology. 3rd ed. Springer; 2023.",
"Parathyroid Carcinoma": "Schulte KM et al. European Society of Endocrine Surgeons consensus on advanced parathyroid cancer. Langenbecks Arch Surg. 2018;403:521-537.",
"Hungry Bone / Post-Thyroid Calcium Management": "Witteveen JE et al. Hungry bone syndrome: still a challenge in the post-operative management of primary hyperparathyroidism. Eur J Endocrinol. 2013;168:R45-R53.",
"Recurrent Laryngeal Nerve Injury During Thyroidectomy": "Randolph GW et al. Electrophysiologic recurrent laryngeal nerve monitoring: international standards guideline statement. Laryngoscope. 2011;121(Suppl 1):S1-S16.",
"Completion Thyroidectomy": "Ringel MD et al. 2025 ATA Management Guidelines for Adult Patients with Differentiated Thyroid Cancer. Thyroid. 2025;35:841-985; compare with the 2015 ATA framework retained in Pasha & Golub 6e for board-era context.",
"Radioactive Iodine and TSH Suppression in DTC": "Ringel MD et al. 2025 ATA Management Guidelines for Adult Patients with Differentiated Thyroid Cancer. Thyroid. 2025;35:841-985; use current response- and risk-adapted recommendations while retaining explicitly labelled 2015-era textbook context.",
"Primary Thyroid Lymphoma": "NCCN Clinical Practice Guidelines in Oncology: B-Cell Lymphomas, current version; treatment depends on lymphoma histology and stage rather than thyroidectomy as routine oncologic therapy.",
"Familial Hyperparathyroidism and Parathyromatosis": "Thakker RV et al. Clinical Practice Guidelines for Multiple Endocrine Neoplasia Type 1. J Clin Endocrinol Metab. 2012;97:2990-3011.",
"Salivary Adenoid Cystic Carcinoma and Perineural Spread": "NCCN Clinical Practice Guidelines in Oncology: Head and Neck Cancers, current version; named-nerve/skull-base imaging is risk-directed for perineural spread.",
},
"Pediatric Otolaryngology": {
"Pediatric OSA / Adenotonsillar Disease": "Marcus CL et al. AAP Clinical Practice Guideline: Diagnosis and Management of Childhood OSA. Pediatrics. 2012;130:e714-e755; Mitchell RB et al. AAO-HNSF Clinical Practice Guideline: Tonsillectomy in Children (Update). Otolaryngol Head Neck Surg. 2019;160(1 Suppl):S1-S42.",
"Pediatric Airway Foreign Body": "Foltran F et al. Inhaled foreign bodies in children: a global perspective on their epidemiological, clinical, and preventive aspects. Pediatr Pulmonol. 2013;48:344-351.",
"Thyroglossal Duct Cyst": "Sistrunk WE. The surgical treatment of cysts of the thyroglossal tract. Ann Surg. 1920;71:121-122.",
"Branchial Cleft Anomalies": "Work WP. Newer concepts of first branchial cleft defects. Laryngoscope. 1972;82:1581-1593.",
"Lymphatic Malformation": "ISSVA Classification & Glossary for Vascular Anomalies (2025), © International Society for the Study of Vascular Anomalies; macrocystic, microcystic, and mixed lymphatic-malformation terminology.",
"Laryngomalacia": "Olney DR et al. Laryngomalacia and its treatment. Laryngoscope. 1999;109:1770-1775.",
"Supraglottoplasty": "Olney DR et al. Laryngomalacia and its treatment. Laryngoscope. 1999;109:1770-1775.",
"Pediatric Subglottic Stenosis": "Myer CM 3rd et al. Proposed grading system for subglottic stenosis based on endotracheal tube sizes. Ann Otol Rhinol Laryngol. 1994;103:319-323.",
"Laryngotracheal Reconstruction": "Cotton RT. Pediatric laryngotracheal stenosis. J Pediatr Surg. 1984;19:699-704.",
"Choanal Atresia": "Blake KD et al. CHARGE association: an update and review. Clin Pediatr (Phila). 1998;37:159-173.",
"Pediatric Deep Neck Infection": "Wong DK et al. To drain or not to drain—management of pediatric deep neck abscesses: a case-control study. Int J Pediatr Otorhinolaryngol. 2012;76:1810-1813.",
"Velopharyngeal Insufficiency": "American Cleft Palate-Craniofacial Association. Parameters for Evaluation and Treatment of Patients with Cleft Lip/Palate or Other Craniofacial Differences. Current edition.",
"Pediatric Tracheostomy / Decannulation": "Mitchell RB et al. Clinical Consensus Statement: Tracheostomy Care. Otolaryngol Head Neck Surg. 2013;148:6-20; airway endoscopy and capping/downsizing are protocol- and patient-specific, not universal fixed steps.",
"Pediatric Vocal Fold Immobility": "Daya H et al. Pediatric vocal fold paralysis: a long-term retrospective study. Arch Otolaryngol Head Neck Surg. 2000;126:21-25; Pasha & Golub 6e identifies iatrogenic cardiothoracic surgery/PDA ligation as a leading cause, but etiology varies by age and center.",
"Subglottic Hemangioma": "Léauté-Labrèze C et al. A randomized controlled trial of oral propranolol in infantile hemangioma. N Engl J Med. 2015;372:735-746; airway use is supported by subglottic-hemangioma series rather than this cutaneous trial alone.",
"Tracheomalacia / Bronchomalacia": "Fraga JC et al. Tracheomalacia in children: review of the literature. Semin Pediatr Surg. 2016;25:156-164.",
"Microtia / Aural Atresia": "Jahrsdoerfer RA et al. Grading system for selection of patients with congenital aural atresia. Am J Otol. 1992;13:6-12.",
"Pediatric Aspiration": "Arvedson JC. Assessment of pediatric dysphagia and feeding disorders: clinical and instrumental approaches. Dev Disabil Res Rev. 2008;14:118-127.",
"Cleft / Craniofacial Otologic-Airway Care": "American Cleft Palate-Craniofacial Association. Parameters for Evaluation and Treatment of Patients with Cleft Lip/Palate or Other Craniofacial Differences. Current edition.",
"Juvenile Recurrent Parotitis": "Garavello W et al. Sialendoscopy in juvenile recurrent parotitis: a systematic review. Laryngoscope. 2018;128:1471-1479; it is a minimally invasive option for recurrent/refractory disease, not a universal first-line replacement for conservative care.",
"Pediatric Head & Neck Tumors": "PDQ Pediatric Treatment Editorial Board. Childhood Rhabdomyosarcoma Treatment and relevant pediatric lymphoma/thyroid cancer summaries. National Cancer Institute, current versions.",
"Button Battery Ingestion": "National Capital Poison Center. Button Battery Ingestion Triage and Treatment Guideline, current version. https://www.poison.org/battery/guideline",
},
"Laryngology / Voice / Swallowing": {
"Unilateral Vocal Fold Paralysis": "Rosen CA et al. Clinical Consensus Statement: Evaluation and Management of Unilateral Vocal Fold Paralysis. Otolaryngol Head Neck Surg. 2023;168:S1-S42.",
"Benign Vocal Fold Lesions": "Johns MM. Update on the etiology, diagnosis, and treatment of vocal fold nodules, polyps, and cysts. Curr Opin Otolaryngol Head Neck Surg. 2003;11:456-461.",
"Dysphagia / Aspiration": "Langmore SE. History of fiberoptic endoscopic evaluation of swallowing for evaluation and management of pharyngeal dysphagia. Am J Speech Lang Pathol. 2017;26:451-455.",
"Subglottic / Tracheal Stenosis": "Myer CM 3rd et al. Proposed grading system for subglottic stenosis. Ann Otol Rhinol Laryngol. 1994;103:319-323; application in adults should be identified as extrapolation.",
"Laryngeal Anatomy": "Pasha & Golub. Otolaryngology—Head and Neck Surgery: Clinical Reference Guide. 6e (2022), ch 2, pp 76-85 (laryngeal framework, membranes, intrinsic spaces, innervation, and operative relationships); Cummings Otolaryngology 7e laryngeal anatomy chapters.",
"Stroboscopy Interpretation": "Poburka BJ et al. Voice-Vibratory Assessment with Laryngeal Imaging rating form. J Voice. 2017;31:513.e1-513.e14.",
"Vocal Fold Nodules": "Pedersen M, McGlashan J. Surgical versus non-surgical interventions for vocal cord nodules. Cochrane Database Syst Rev. 2012:CD001934.",
"Vocal Fold Polyp / Cyst": "Johns MM. Update on vocal fold nodules, polyps, and cysts. Curr Opin Otolaryngol Head Neck Surg. 2003;11:456-461.",
"Bilateral Vocal Fold Immobility": "Li Y et al. Surgery for bilateral vocal fold paralysis: systematic review and meta-analysis. Front Surg. 2022;9:956338.",
"FEES": "Langmore SE, Schatz K, Olsen N. Fiberoptic endoscopic examination of swallowing safety: a new procedure. Dysphagia. 1988;2:216-219.",
"Modified Barium Swallow": "Martin-Harris B et al. MBS measurement tool for swallow impairment—MBSImP. Dysphagia. 2008;23:392-405.",
"Medialization Thyroplasty": "Isshiki N et al. Thyroplasty type I for dysphonia due to vocal cord paralysis. Acta Otolaryngol. 1975;80:465-473.",
"Microlaryngoscopy": "Zeitels SM. Universal modular glottiscope system: the evolution of a century of design and technique for direct laryngoscopy. Ann Otol Rhinol Laryngol Suppl. 1999;179:2-24.",
"Reinke Edema": "Dikkers FG, Nikkels PG. Benign lesions of the vocal folds: histopathology and phonotrauma. Ann Otol Rhinol Laryngol. 1995;104:698-703.",
"Presbyphonia": "Johns MM 3rd et al. Presbylaryngis and presbyphonia: a state-of-the-art review. Laryngoscope. 2011;121:371-378.",
"Muscle Tension Dysphonia": "Van Houtte E et al. Pathophysiology and treatment of muscle tension dysphonia: a review. J Voice. 2011;25:202-207.",
"Vocal Tremor": "Barkmeier-Kraemer J, Lato A. Development of a speech treatment program for a client with essential vocal tremor. Semin Speech Lang. 2011;32:43-57.",
"Leukoplakia / Laryngeal Dysplasia": "WHO Classification of Tumours Editorial Board. Head and Neck Tumours. 5th ed. IARC; 2022: laryngeal squamous dysplasia uses a two-tier low-grade/high-grade framework; do not map older mild/moderate/severe terms without stating the system.",
"Posterior Glottic Stenosis / Arytenoid Fixation": "Bogdasarian RS, Olson NR. Posterior glottic laryngeal stenosis. Otolaryngol Head Neck Surg. 1980;88:765-772.",
"Injection Laryngoplasty": "Mallur PS, Rosen CA. Vocal fold injection: review of indications, techniques, and materials. Clin Exp Otorhinolaryngol. 2010;3:177-182.",
"Arytenoid Adduction / Reinnervation": "Isshiki N et al. Arytenoid adduction for unilateral vocal cord paralysis. Arch Otolaryngol. 1978;104:555-558.",
"Posterior Cordotomy / Arytenoidectomy": "Li Y et al. Surgery for bilateral vocal fold paralysis: systematic review and meta-analysis. Front Surg. 2022;9:956338.",
"Cricopharyngeal Dysfunction": "Cook IJ, Kahrilas PJ. AGA technical review on management of oropharyngeal dysphagia. Gastroenterology. 1999;116:455-478.",
"Inducible Laryngeal Obstruction / PVFM": "Christensen PM et al. ERS/ELS/ACCP consensus nomenclature for inducible laryngeal obstruction. Eur Respir Rev. 2015;24:445-450.",
"Chronic Cough / Laryngeal Hypersensitivity": "Irwin RS et al. Classification of cough and management algorithms: CHEST guideline. Chest. 2018;153:196-209.",
"Vocal Fold Sulcus / Scar": "Ford CN et al. Sulcus vocalis: a rational classification system. J Voice. 1996;10:189-201.",
"Vocal Process Granuloma": "Karkos PD et al. Vocal process granulomas: a systematic review of treatment. Ann Otol Rhinol Laryngol. 2014;123:314-320.",
"Radiation-Associated Dysphagia": "Eisbruch A et al. Chemo-IMRT of oropharyngeal cancer aiming to reduce dysphagia. Int J Radiat Oncol Biol Phys. 2011;81:e93-e99.",
"Aspiration-Prevention Surgery": "Ueha R et al. Aspiration prevention surgeries: a review. Respir Res. 2023;24:43.",
},
"Facial Plastics / Trauma": {
"Mohs Defect Reconstruction": "Janis JE et al. A practical guide to wound healing. Plast Reconstr Surg. 2010;125:230e-244e.",
"Scar Management": "Mustoe TA et al. International clinical recommendations on scar management. Plast Reconstr Surg. 2002;110:560-571.",
"Functional Septorhinoplasty": "Rhee JS et al. Clinical consensus statement: diagnosis and management of nasal valve compromise. Otolaryngol Head Neck Surg. 2010;143:48-59.",
"Open Rhinoplasty Fundamentals": "Sheen JH. Aesthetic Rhinoplasty. Mosby; 1978.",
"Otoplasty": "Mustardé JC. The correction of prominent ears using simple mattress sutures. Br J Plast Surg. 1963;16:170-178; Furnas DW. Plast Reconstr Surg. 1968;42:189-193.",
"Rhinoplasty Tip Mechanics": "Anderson JR. A reasoned approach to nasal base surgery. Arch Otolaryngol. 1984;110:349-358.",
"Bilobed Flap": "Zitelli JA. The bilobed flap for nasal surgery. Arch Dermatol. 1989;125:957-959.",
"Cervicofacial Flap": "Rapstine ED et al. Single-stage reconstruction of large medial cheek defects with a cervicofacial rotation advancement flap. Dermatol Surg. 2012;38:131-136.",
"Septal Perforation": "Kridel RWH. Considerations in etiology, treatment, and repair of septal perforations. Facial Plast Surg Clin North Am. 2004;12:435-450.",
"Facial Synkinesis / Static-Dynamic Rehabilitation": "Ross BG et al. Development of a sensitive clinical facial grading system. Otolaryngol Head Neck Surg. 1996;114:380-386.",
"Auricular Reconstruction": "Brent B. Correction of microtia with autogenous cartilage grafts. Plast Reconstr Surg. 1980;66:1-12; Nagata S. Plast Reconstr Surg. 1993;92:187-201.",
"Alar Retraction / Nasal Vestibular Stenosis": "Toriumi DM et al. Alar batten grafts. Arch Otolaryngol Head Neck Surg. 1997;123:802-808.",
},
"Sleep Surgery": {
"DISE": "Kezirian EJ et al. Drug-induced sleep endoscopy: the VOTE classification. Eur Arch Otorhinolaryngol. 2011;268:1233-1236.",
"Hypoglossal Nerve Stimulation": "Strollo PJ Jr et al. Upper-airway stimulation for obstructive sleep apnea. N Engl J Med. 2014;370:139-149.",
"PAP Troubleshooting": "Patil SP et al. AASM Clinical Practice Guideline for PAP treatment of adult OSA. J Clin Sleep Med. 2019;15:335-343.",
"Tongue Base Surgery": "Friedman M et al. Clinical staging for sleep-disordered breathing. Otolaryngol Head Neck Surg. 2002;127:13-21.",
"Maxillomandibular Advancement": "Holty JEC, Guilleminault C. Maxillomandibular advancement for OSA: systematic review and meta-analysis. Sleep Med Rev. 2010;14:287-297.",
"Oral Appliance Therapy": "Ramar K et al. Clinical Practice Guideline for Oral Appliance Therapy. J Clin Sleep Med. 2015;11:773-827.",
"HNS Activation / Programming": "US FDA. Inspire Upper Airway Stimulation device labeling, current version; programming and titration must follow the device protocol.",
"Residual OSA After Surgery": "Aurora RN et al. AASM practice parameters for surgical modifications of the upper airway for OSA. Sleep. 2010;33:1408-1413.",
"Central Events / Hypoventilation": "Badr MS et al. Treatment of central sleep apnea in adults: AASM clinical practice guideline. J Clin Sleep Med. 2025;21:2181-2191; ICSD-3-TR defines hypoventilation disorders.",
"Lingual Tonsil / Tongue-Base Obstruction": "Friedman M et al. Clinical staging for sleep-disordered breathing. Otolaryngol Head Neck Surg. 2002;127:13-21.",
"HNS Troubleshooting / Nonresponse": "Heiser C et al. Post-approval upper-airway stimulation predictors in the ADHERE registry. Laryngoscope. 2019;129:2377-2383.",
},
"General ENT / Emergencies": {
"Deep Neck Space Infection": "Chow AW. Life-threatening infections of the head, neck, and upper respiratory tract. In: Mandell, Douglas, and Bennett's Principles and Practice of Infectious Diseases. 9th ed.",
"Tracheostomy Emergency": "McGrath BA et al. Multidisciplinary guidelines for management of tracheostomy and laryngectomy airway emergencies. Anaesthesia. 2020;75:1659-1670.",
"Postoperative Neck Hematoma": "Iliff HA et al. Management of haematoma after thyroid surgery: multidisciplinary consensus guidelines. Anaesthesia. 2022;77:82-95.",
"Esophageal Perforation / Cervical Mediastinitis": "Chirica M et al. Esophageal emergencies: WSES guidelines. World J Emerg Surg. 2019;14:26.",
"ENT Perioperative Anesthesia / Difficult Airway Planning": "Apfelbaum JL et al. 2022 ASA Practice Guidelines for Management of the Difficult Airway. Anesthesiology. 2022;136:31-81.",
"Hemostasis / Coagulopathy / Antithrombotic Management in ENT": "Douketis JD et al. Perioperative management of antithrombotic therapy: CHEST clinical practice guideline. Chest. 2022;162:e207-e243.",
"ENT Fluids / Electrolytes / Nutrition": "Weimann A et al. ESPEN practical guideline: Clinical nutrition in surgery. Clin Nutr. 2021;40:4745-4761.",
"Antimicrobial Stewardship in Otolaryngology": "US Centers for Disease Control and Prevention. Core Elements of Hospital Antibiotic Stewardship Programs. 2019.",
"Cranial Nerve Examination / Skull Base Localization": "Brazis PW et al. Localization in Clinical Neurology. 7th ed. Wolters Kluwer; 2016.",
"ENT Imaging Fundamentals": "American College of Radiology. ACR Appropriateness Criteria, relevant head-and-neck, sinus, and temporal-bone panels; current versions.",
"Wound Healing / Scar Biology in Head & Neck Surgery": "Mustoe TA et al. International clinical recommendations on scar management. Plast Reconstr Surg. 2002;110:560-571.",
"Grafts / Implants / Biomaterials in ENT": "Berghaus A. Porous polyethylene in reconstructive head and neck surgery. Arch Otolaryngol. 1985;111:154-160; material choice remains indication- and site-specific.",
"Systemic / Granulomatous Disease Manifestations in ENT": "Jennette JC et al. 2012 Revised International Chapel Hill Consensus Conference Nomenclature of Vasculitides. Arthritis Rheum. 2013;65:1-11.",
"Laser / Energy Safety in Otolaryngology": "American National Standards Institute. ANSI Z136.3: Safe Use of Lasers in Health Care, current edition.",
"Common ENT Consult Triage / Disposition": "ENT UK. Emergency Otolaryngology guidance and condition-specific emergency pathways; airway compromise, uncontrolled hemorrhage, and progressive deep infection require immediate escalation.",
},
}

CLAIM_SOURCES_V414 = {
    (domain, topic): [citation]
    for domain, topics in S.items()
    for topic, citation in topics.items()
}


def _append_source(row, citations):
    current = row.get("source_basis") or []
    if isinstance(current, str):
        current = [current]
    if not isinstance(current, list):
        raise RuntimeError("v41.4: malformed source_basis on %s" % row.get("topic"))
    row["source_basis"] = list(dict.fromkeys(current + citations))


def apply_deep_source_claim_backfill_v414(data_module, app_module=None):
    deep_source = getattr(data_module, "DEEP_MODULES_V6", None)
    if not isinstance(deep_source, dict):
        raise RuntimeError("v41.4: DEEP_MODULES_V6 unavailable")
    deep = deepcopy(deep_source)
    index = {(domain, row.get("topic")): row for domain, rows in deep.items() for row in rows}
    missing = [key for key in CLAIM_SOURCES_V414 if key not in index]
    if missing:
        raise RuntimeError("v41.4: missing claim-source targets: %r" % missing)
    updated = []
    for key, citations in CLAIM_SOURCES_V414.items():
        row = index[key]
        before = list(row.get("source_basis") or [])
        _append_source(row, citations)
        if row["source_basis"] != before:
            updated.append(key)
        row["claim_source_backfill_v414"] = True
    data_module.DEEP_MODULES_V6.clear()
    data_module.DEEP_MODULES_V6.update(deep)
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"claim_sources_targeted": len(CLAIM_SOURCES_V414), "topics_updated": len(updated)}
