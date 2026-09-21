"""ENT Mastery v40.8 — remaining Priority 2/3 source, depth, and OR reconciliation.

Runs after v40.7.  The source pass gives every canonical topic a traceable
connected-textbook trail while retaining claim-specific guidelines already
present.  Targeted depth edits are limited to the clinical gaps identified in
the 2026-09-20 review; existing richer text is appended, not replaced.
"""
from copy import deepcopy


CUMMINGS = "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021), connected Google Drive full-text ID 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t; foundational {domain} section and index (domain-level locator, not a claim-level citation)."

PASHA_DOMAIN_LOCATORS = {
    "Otology / Neurotology": "Pasha & Golub, 6e (2022), Ch 7 Otology and Neurotology, pp 333-436; Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "Rhinology / Allergy / Skull Base": "Pasha & Golub, 6e (2022), Ch 1 Allergy and Rhinology, pp 1-74; Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "Head & Neck Oncology": "Pasha & Golub, 6e (2022), Ch 6 Head and Neck Cancer, pp 249-332; Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "Thyroid / Parathyroid / Salivary": "Pasha & Golub, 6e (2022), Ch 3 Endocrinology, pp 127-150, and Ch 5 salivary sections, pp 197-216; Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "Pediatric Otolaryngology": "Pasha & Golub, 6e (2022), Ch 9 Pediatric Otolaryngology, pp 527-628; Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "Laryngology / Voice / Swallowing": "Pasha & Golub, 6e (2022), Ch 2 Laryngology, pp 75-126; Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "Facial Plastics / Trauma": "Pasha & Golub, 6e (2022), Ch 8 Facial Plastic Surgery, pp 437-526, and Ch 10 Trauma, pp 629-670; Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "Sleep Surgery": "Pasha & Golub, 6e (2022), Ch 4 Sleep Medicine, pp 151-182; Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "General ENT / Emergencies": "Pasha & Golub, 6e (2022), Ch 5 General Otolaryngology, pp 183-248, and Ch 10 Trauma, pp 629-670; Drive ID 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
}

KJLEE_DOMAIN_LOCATORS = {
    "Otology / Neurotology": "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 2, Ch 13-23, pp 234-478; Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "Rhinology / Allergy / Skull Base": "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 3, Ch 26-34, pp 479-611; Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "Head & Neck Oncology": "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 4, Ch 35-49, pp 612-878; Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "Thyroid / Parathyroid / Salivary": "K.J. Lee's Essential Otolaryngology, 12e (2019), Ch 35, 38, and 41, pp 612-756; Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "Pediatric Otolaryngology": "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 6, Ch 51-53, pp 921-1025; Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "Laryngology / Voice / Swallowing": "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 5, Ch 50, pp 879-920; Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "Facial Plastics / Trauma": "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 7, Ch 54-58, pp 1026-1112; Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "General ENT / Emergencies": "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 1, Ch 1-12, pp 1-233, with relevant Part 4 sections; Drive ID 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
}

BLUESTONE_PEDIATRIC = "Bluestone and Stool's Pediatric Otolaryngology, 5e, connected Google Drive ID 1nZuGLB6MrLfPdmrmHqKCe9AbKtNubqcl; topic-specific pediatric chapter/index cross-reference."


def _core_sources(domain):
    sources = [CUMMINGS.format(domain=domain), PASHA_DOMAIN_LOCATORS[domain]]
    if domain in KJLEE_DOMAIN_LOCATORS:
        sources.append(KJLEE_DOMAIN_LOCATORS[domain])
    if domain == "Pediatric Otolaryngology":
        sources.append(BLUESTONE_PEDIATRIC)
    return sources

CLAIM_SOURCES = {
    "Facial Paralysis": ["Baugh RF et al. AAO-HNSF Clinical Practice Guideline: Bell's Palsy. Otolaryngol Head Neck Surg. 2013;149(3 Suppl):S1-S27."],
    "Age-Related Hearing Loss / Presbycusis": ["Clinical Practice Guideline: Age-Related Hearing Loss. Otolaryngol Head Neck Surg. 2024;170(1 Suppl):S1-S58."],
    "BPPV": ["Bhattacharyya N et al. AAO-HNSF Clinical Practice Guideline: BPPV (Update). Otolaryngol Head Neck Surg. 2017;156(3 Suppl):S1-S47."],
    "Epistaxis Surgical Control": ["Tunkel DE et al. AAO-HNSF Clinical Practice Guideline: Nosebleed (Epistaxis). Otolaryngol Head Neck Surg. 2020;162(1 Suppl):S1-S38."],
    "Medullary Thyroid Cancer": ["Wells SA Jr et al. Revised ATA Guidelines for the Management of Medullary Thyroid Carcinoma. Thyroid. 2015;25:567-610."],
    "MEN2 / RET": ["Wells SA Jr et al. Revised ATA Guidelines for the Management of Medullary Thyroid Carcinoma. Thyroid. 2015;25:567-610."],
    "Recurrent Tonsillitis Decision-Making": ["Mitchell RB et al. AAO-HNSF Clinical Practice Guideline: Tonsillectomy in Children (Update). Otolaryngol Head Neck Surg. 2019;160(1 Suppl):S1-S42."],
    "Pediatric Hearing Loss Workup": ["Joint Committee on Infant Hearing. Year 2019 Position Statement: Principles and Guidelines for Early Hearing Detection and Intervention Programs. J Early Hear Detect Interv. 2019;4:1-44."],
    "Recurrent Respiratory Papillomatosis": ["International Pediatric Otolaryngology Group consensus and contemporary RRP literature — systemic/intralesional bevacizumab is an adjuvant for selected aggressive disease; HPV vaccination remains primary prevention and may be discussed as adjunct prevention, not a replacement for surgery."],
    "Central Sleep Apnea / Treatment-Emergent CSA": ["American Academy of Sleep Medicine clinical practice guidance for treatment of central sleep apnea in adults (2025)."],
    "Sleep-Related Hypoventilation": ["American Academy of Sleep Medicine clinical practice guidance and ICSD-3-TR diagnostic framework for sleep-related hypoventilation."],
    "Down Syndrome Pediatric HNS": ["FDA Inspire Upper Airway Stimulation pediatric Down-syndrome indication and current device labeling; verify age, AHI, central-event burden, PAP history, BMI, anatomy, and DISE criteria against the current label."],
    "Positional OSA": ["Cartwright positional OSA definition and contemporary Amsterdam positional-OSA classification literature; report supine and nonsupine event burden rather than using an undefined 'large ratio'."],
    "Lemierre Syndrome": ["Contemporary Lemierre syndrome reviews: antibiotic duration is individualized by source control, thrombus/metastatic infection, and clinical response; published practice is variable rather than a universal 4-6-week rule."],
    "Chyle Leak": ["Contemporary head-and-neck chyle-leak management reviews — quantify output and escalate according to persistence, nutritional effects, and institutional thresholds; thoracic-duct embolization is an option in selected refractory leaks."],
    "Deep Neck Abscess Drainage": ["Contemporary deep-neck infection literature — airway control, contrast imaging when stable, culture-directed antibiotics, and space-specific drainage/source control."],
    "Graves Disease / Toxic Goiter": ["Ross DS et al. 2016 American Thyroid Association Guidelines for Diagnosis and Management of Hyperthyroidism and Other Causes of Thyrotoxicosis. Thyroid. 2016;26:1343-1421."],
    "Central Vestibular Disorders": ["Edlow JA et al. GRACE-3: Acute Dizziness and Vertigo in the Emergency Department. Acad Emerg Med. 2023;30:442-486; HINTS is restricted to trained examiners evaluating continuous acute vestibular syndrome."],
    "Ankyloglossia / Maxillary Frenulum": ["Thomas J et al. Identification and Management of Ankyloglossia and Its Effect on Breastfeeding in Infants. Pediatrics. 2024;154:e2024067605.", "Messner AH et al. Clinical Consensus Statement: Ankyloglossia in Children. Otolaryngol Head Neck Surg. 2020;162:597-611."],
    "Pediatric Reflux / Eosinophilic Esophagitis": ["Dellon ES et al. ACG Clinical Guideline: Diagnosis and Management of Eosinophilic Esophagitis. Am J Gastroenterol. 2025;120:31-59."],
    "Narcolepsy / Central Hypersomnolence Recognition": ["Krahn LE et al. Recommended protocols for the Multiple Sleep Latency Test and Maintenance of Wakefulness Test in adults. J Clin Sleep Med. 2021;17:2489-2498.", "Maski KP et al. Recommended protocols for the Multiple Sleep Latency Test and Maintenance of Wakefulness Test in children. J Clin Sleep Med. 2024;20:631-641."],
    "Restless Legs / Periodic Limb Movement Disorders": ["Winkelman JW et al. Treatment of restless legs syndrome and periodic limb movement disorder: an AASM clinical practice guideline. J Clin Sleep Med. 2025;21:137-152."],
    "Circadian Rhythm Sleep-Wake Disorders": ["Auger RR et al. AASM Clinical Practice Guideline for Treatment of Intrinsic Circadian Rhythm Sleep-Wake Disorders. J Clin Sleep Med. 2015;11:1199-1236."],
}


DEPTH_UPDATES = {
    ("Thyroid / Parathyroid / Salivary", "Graves Disease / Toxic Goiter"): {
        "workup": "Quantify biochemical severity with TSH and free T4/T3, establish Graves versus toxic nodular etiology, document orbitopathy and compressive/substernal anatomy, and score suspected thyroid storm clinically (for example with Burch-Wartofsky) rather than relying on hormone concentration alone. Before elective thyroidectomy obtain euthyroid or near-euthyroid control when feasible, assess vocal-fold function when indicated, and plan the difficult-airway implications of a large goiter.",
        "manage": "Use a beta blocker for adrenergic symptoms and methimazole for most nonpregnant patients; propylthiouracil is favored in the first trimester and in thyroid storm because it also reduces peripheral T4-to-T3 conversion. For urgent thyroid storm, give beta blockade as appropriate, thionamide, then iodine after thionamide, glucocorticoid, supportive care, and treat the precipitant. Before Graves thyroidectomy, short-course iodine is commonly used to reduce hormone release and vascularity after antithyroid therapy has begun; exact timing follows the endocrine/surgical protocol.",
    },
    ("Thyroid / Parathyroid / Salivary", "Primary Thyroid Lymphoma"): {
        "manage": "Separate histology before treatment: localized indolent thyroid MALT lymphoma may be managed with involved-site radiation in selected patients, whereas diffuse large B-cell lymphoma generally requires systemic chemoimmunotherapy, often with radiation according to stage/response. Thyroidectomy is not routine oncologic treatment; secure the airway with the least morbid effective strategy while obtaining adequate core tissue for histology, immunophenotyping, and flow cytometry.",
    },
    ("Pediatric Otolaryngology", "Recurrent Respiratory Papillomatosis"): {
        "manage": "Preserve airway and voice with tissue-sparing endoscopic control. For aggressive disease requiring frequent procedures, distal spread, or unacceptable morbidity, consider adjuvant therapy in a multidisciplinary pathway; systemic or intralesional bevacizumab has become an important option but dosing/monitoring remain center-specific. Promote HPV vaccination as primary prevention and discuss vaccination in affected eligible patients as an adjunctive measure without promising eradication of established disease.",
        "teach": "RRP treatment endpoints are airway patency, functional voice, and longer intervals between interventions—not a scar-producing attempt at microscopic eradication. Bevacizumab is an adjuvant for selected aggressive disease; vaccination prevents HPV-associated disease at the population level but is not a substitute for operative airway control.",
    },
    ("Pediatric Otolaryngology", "Lymphatic Malformation"): {
        "workup": "Classify the lesion under the ISSVA vascular-anomaly framework and describe macrocystic, microcystic, or mixed architecture rather than using the imprecise term cystic hygroma as the final diagnosis. MRI defines trans-spatial extent and airway involvement; ultrasound helps characterize accessible cysts and guide treatment.",
        "manage": "Observe stable asymptomatic disease. Macrocystic lesions often respond to image-guided sclerotherapy; diffuse microcystic disease may require staged debulking and, for severe complex disease, multidisciplinary systemic targeted therapy such as sirolimus or pathway-directed treatment when a qualifying molecular diagnosis and specialty protocol support it. Acute infection or intralesional hemorrhage can abruptly threaten the airway and changes urgency.",
    },
    ("Laryngology / Voice / Swallowing", "Medialization Thyroplasty"): {
        "operate": "Choose implant material and shape to the defect (commonly carved Silastic or a prefabricated implant such as Gore-Tex/titanium systems according to surgeon technique). Local anesthesia with light sedation permits awake voice and airway tuning; adjust medialization to improve closure without overcompression, mucosal violation, implant extrusion, or airway compromise. A dominant posterior gap or vertical-level mismatch may require arytenoid adduction rather than an oversized anterior implant. Counsel regarding hematoma, edema/airway compromise, implant migration/extrusion, infection, persistent dysphonia, and need for revision.",
    },
    ("Laryngology / Voice / Swallowing", "Cricopharyngeal Dysfunction"): {
        "manage": "Match treatment to demonstrated physiology: dilation can be diagnostic/therapeutic for focal narrowing; botulinum toxin offers temporary reduction in sphincter tone and can help predict benefit; durable endoscopic or open myotomy is reserved for selected patients with adequate pharyngeal propulsion and a true outflow restriction. Global pharyngeal weakness or poor hyolaryngeal excursion will not be corrected by simply cutting the cricopharyngeus.",
        "operate": "For endoscopic myotomy, expose the posterior UES, divide the dysfunctional cricopharyngeal muscle across the stenotic segment to an adequate depth while preserving the buccopharyngeal fascia/esophageal wall, and inspect for perforation; open myotomy uses a lateral cervical approach with RLN protection. Incomplete myotomy risks persistent obstruction, whereas full-thickness perforation risks cervical infection and mediastinitis. Postoperative contrast evaluation and diet advancement are individualized to technique and concern for leak.",
    },
    ("Laryngology / Voice / Swallowing", "Vocal Process Granuloma"): {
        "teach": "Treat mechanical collision, cough/throat clearing, voice behavior, and clearly relevant inflammatory contributors. Evidence for empiric antireflux medication in an unselected contact-granuloma patient is mixed; reflux therapy should not replace voice/cough-directed treatment or reassessment of an atypical lesion.",
    },
    ("Facial Plastics / Trauma", "Facial Nerve Reanimation"): {
        "teach": "Use denervation duration as a practical, not absolute, discriminator: native mimetic muscle is often still reinnervatable within roughly 12 months and becomes progressively unreliable by about 18-24 months. When viable muscle remains, nerve repair/grafting or masseteric/hypoglossal/cross-facial input can restore native movement; after long-standing denervation with motor-endplate loss, regional or free functional muscle transfer is usually required. Electrical testing and clinical muscle viability override a calendar cutoff when discordant.",
    },
    ("Facial Plastics / Trauma", "Bilobed Flap"): {
        "operate": "Use the Zitelli reduced-arc concept: design each lobe through roughly 45-50 degrees of transposition (about 90-100 degrees total rather than the older 180-degree arc), size the first lobe near the defect and the second smaller, and perform broad undermining in the correct plane. Distribute tension away from the alar rim and thin conservatively to limit pincushioning, trapdoor deformity, necrosis, and alar retraction.",
    },
    ("Facial Plastics / Trauma", "Cervicofacial Flap"): {
        "operate": "Design a broad rotation-advancement flap with the incision hidden along facial/neck boundaries when possible. Elevate in a subcutaneous or deep-plane/sub-SMAS plane according to defect, prior treatment, and surgeon plan; protect facial-nerve branches when working deep and preserve a broad vascular base. Anchor deep tension to stable fascia/periosteum rather than the lower eyelid or lip, trim standing cones after inset, and anticipate distal-tip ischemia, hematoma, ectropion, facial-nerve injury, and contour mismatch—especially in irradiated tissue.",
    },
    ("Sleep Surgery", "Tongue Base Surgery"): {
        "workup": "Confirm retrolingual contribution using awake examination plus DISE when appropriate, and distinguish lingual-tonsil hypertrophy from muscular tongue-base collapse, epiglottic interaction, and lateral-wall collapse. Review dysphagia/aspiration risk, prior radiation or surgery, anticoagulation, tongue mobility, and the relationship of the lingual arteries and hypoglossal nerves to the planned resection.",
        "manage": "Choose lingual tonsillectomy, midline glossectomy, robotic/laser reduction, suspension, or a nonresective alternative only when the collapse phenotype fits. Plan postoperative airway observation, bleeding rescue, pain/hydration, and swallow assessment. Avoid assuming that visible tongue-base bulk is the sole cause of multilevel OSA.",
        "operate": "Maintain a midline, depth-controlled resection with deliberate hemostasis and respect for paired lingual arteries and hypoglossal motor pathways. Stop before uncontrolled deep lateral dissection; postoperative hemorrhage, tongue edema, airway obstruction, dysphagia/aspiration, taste disturbance, and tongue weakness are the defining rescue concerns.",
    },
    ("Sleep Surgery", "Positional OSA"): {
        "workup": "Report total, supine, and nonsupine event indices plus actual sleep time in each position. A commonly used Cartwright definition is supine AHI at least twice the nonsupine AHI, but classification should also identify whether nonsupine disease normalizes and whether adequate nonsupine sleep was captured. Do not label disease positional from an undefined 'large ratio' or a few minutes of lateral sleep.",
        "manage": "Use positional therapy when a reproducible positional phenotype and adequate nonsupine control make it plausible, then verify adherence and residual disease. Severe oxygen burden, persistent nonsupine OSA, limited mobility, pregnancy/body-habitus constraints, or inability to maintain lateral sleep may require PAP, oral appliance, surgery, or combination therapy rather than positional therapy alone.",
    },
    ("General ENT / Emergencies", "Lemierre Syndrome"): {
        "manage": "Start prompt IV therapy active against Fusobacterium and oral anaerobes, drain the primary/deep-neck or thoracic source when indicated, and narrow with cultures and response. Duration is not a universal fixed 4-6 weeks: tailor IV-to-oral transition and total course to source control, internal-jugular thrombus, metastatic infection, complications, and clinical/radiographic response. Anticoagulation remains individualized for progression, extensive clot, cerebral-sinus extension, or poor response rather than routine for every patient.",
    },
    ("Head & Neck Oncology", "Tonsil SCC"): {
        "workup": "Perform complete mucosal and cranial-nerve examination, contrast CT or MRI of primary/neck, chest/distant staging as risk dictates, and p16 testing for oropharyngeal SCC with HPV-specific testing when morphology/site or institutional protocol requires clarification. For an adult cystic cervical node, obtain image-guided FNA/core with appropriate HPV-related testing and complete the unknown-primary pathway before open excision. Retain AJCC 8 as a clearly labelled board/pre-2026 comparison; use the separate AJCC Version 9 protocol for HPV-associated oropharyngeal cancers diagnosed from 2026-01-01, and do not mix their nodal categories.",
    },
    ("Head & Neck Oncology", "Hypopharyngeal Cancer"): {
        "manage": "Discuss definitive chemoradiation/organ preservation versus primary surgery according to T extent, cartilage/prevertebral invasion, baseline laryngeal and swallowing function, nutrition, comorbidity, and likelihood of salvage. EORTC 24891 established that induction-chemotherapy responders could receive radiation with larynx preservation without an overall-survival penalty versus immediate laryngectomy in selected advanced hypopharyngeal cancer; it does not justify preservation of a nonfunctional or extensively destructive larynx.",
    },
    ("Rhinology / Allergy / Skull Base", "Recurrent Acute Rhinosinusitis"): {
        "operate": "Offer surgery only after documenting true discrete bacterial-pattern episodes with symptom-free intervals, failure of appropriate medical/preventive management, and relevant endoscopic or CT anatomy. Tailor limited sinus opening to the repeatedly involved sinus and natural drainage pathway; surgery is not justified by four self-diagnosed viral URIs or a normal inter-episode evaluation without corroborating evidence.",
        "teach": "RARS requires at least four distinct acute episodes per year with resolution between them. The surgical question is not the count alone—it is whether objectively credible recurrent disease maps to an anatomic drainage target after medical contributors have been addressed.",
    },
    ("Rhinology / Allergy / Skull Base", "Sinonasal Inverted Papilloma"): {
        "workup": "Document a Krouse stage for operative communication: T1 nasal-cavity disease; T2 disease involving the ostiomeatal complex/ethmoid and/or medial maxillary sinus; T3 disease involving other maxillary walls or frontal/sphenoid sinus; T4 disease extending beyond the sinonasal tract or associated with malignancy. Use staging as an extent descriptor, not a substitute for attachment-directed imaging and surgical planning.",
    },
    ("Rhinology / Allergy / Skull Base", "Juvenile Nasopharyngeal Angiofibroma"): {
        "workup": "Stage radiographic extent with a named system such as Radkowski or Fisch and document skull-base/intracranial and internal-carotid relationships explicitly. Radkowski progresses from nasal/nasopharyngeal disease through pterygopalatine/infratemporal extension to skull-base erosion/intracranial disease; Fisch similarly escalates from nasal/nasopharyngeal disease to pterygopalatine/maxillary/ethmoid disease, then infratemporal/orbital disease, and finally intracranial extension. Do not biopsy a classic hypervascular lesion merely to obtain a tissue label.",
    },
    ("Otology / Neurotology", "Facial Paralysis"): {
        "workup": "Grade function serially with a named scale such as House-Brackmann (I normal; II mild; III moderate with complete eye closure; IV moderately severe with incomplete/weak closure; V barely perceptible motion; VI no movement) and separately document ocular protection and synkinesis. Typical new Bell palsy does not require routine imaging, but progressive, recurrent, segmental, traumatic, or tumor-associated weakness does.",
        "manage": "For new Bell palsy, start oral corticosteroids promptly when not contraindicated and protect the eye. Antiviral monotherapy is not recommended; combination antiviral plus steroid may be offered selectively because any added benefit is modest/uncertain. Vesicles, severe pain, hearing/vestibular symptoms, or other cranial neuropathies redirect evaluation toward Ramsay Hunt or another cause.",
    },
    ("Otology / Neurotology", "Age-Related Hearing Loss / Presbycusis"): {
        "manage": "Follow a function-centered pathway: counsel on communication strategies, offer appropriately fitted amplification and assistive technology, verify benefit rather than merely documenting device purchase, and refer for cochlear-implant evaluation when aided speech understanding remains inadequate. Asymmetry, sudden change, conductive findings, or focal neurologic symptoms require diagnostic workup beyond an age-related label.",
    },
    ("Otology / Neurotology", "Auditory Neuroanatomy / Cochlear Physiology"): {
        "recognize": "Trace sound from stapes motion through the cochlear traveling wave to inner-hair-cell transduction, spiral-ganglion activation, CN VIII, cochlear nuclei, superior olivary complex, lateral lemniscus, inferior colliculus, medial geniculate, and auditory cortex. Basal cochlea encodes high frequencies and apical cochlea low frequencies; tonotopy is preserved centrally.",
        "workup": "Localize using the measurement: OAEs reflect outer-hair-cell function, cochlear microphonic reflects receptor potentials, ABR reflects synchronized auditory-nerve/brainstem activity, speech discrimination stresses neural/central encoding, and behavioral thresholds integrate the entire pathway. Cross-check discordant tests before assigning a lesion.",
        "teach": "Conductive disease attenuates input before the cochlea; cochlear loss disrupts transduction/compression; auditory neuropathy preserves cochlear receptor activity but loses synchronized neural firing; central lesions impair pathway processing despite a potentially normal peripheral audiogram.",
    },
    ("Otology / Neurotology", "Audiologic Electrophysiology / ABR-OAE-ECoG"): {
        "workup": "For ABR, verify stimulus, transducer, artifact, reproducibility, absolute wave I/III/V latencies, interpeak intervals, interaural wave-V difference, and threshold estimate. OAEs require a usable ear canal/middle ear and report cochlear outer-hair-cell function, not hearing comprehension. ECoG separates cochlear summating potential and compound action potential but an elevated SP/AP ratio alone is not a definitive Ménière diagnosis. Present OAEs/cochlear microphonic with absent or grossly abnormal ABR supports auditory neuropathy when the clinical setting fits.",
        "manage": "Use diagnostic ABR for infants or patients unable to provide reliable behavioral thresholds, for suspected retrocochlear/neural dysfunction, and for intraoperative trend monitoring. Confirm electrophysiologic threshold estimates with age-appropriate behavioral testing when possible and do not delay hearing access while waiting for a child to become behaviorally testable.",
        "teach": "Ask what generator each waveform represents, then account for conductive delay, temperature, sedation/anesthetic effects, electrode noise, and stimulus intensity before calling a neural lesion. A technically poor absent waveform is not a diagnosis.",
    },
    ("Otology / Neurotology", "Cortical Neuroplasticity in Hearing Loss"): {
        "workup": "Reconstruct onset, duration, consistency of auditory access, language exposure, aided use, and speech/language trajectory. In children, test functional communication in addition to thresholds; in adults with prolonged deprivation, include aided speech recognition and realistic counseling about central adaptation.",
        "manage": "Provide stable auditory access early through amplification, bone-conduction technology, or cochlear implantation when indicated, paired with language-rich habilitation or rehabilitation. Device fitting without consistent use and therapy does not supply the repeated input required for cortical learning.",
        "teach": "Plasticity explains both urgency and uncertainty: early consistent input supports auditory-language network development, while long deprivation may limit later speech outcomes even when an implant produces excellent electrode function. It is not a reason to deny evaluation; it is a counseling and rehabilitation variable.",
    },
    ("Otology / Neurotology", "Otologic Manifestations of Systemic Disease"): {
        "workup": "Start with the audiovestibular phenotype and tempo, then use systemic clues to direct—not shotgun—testing: autoimmune symptoms and fluctuating bilateral SNHL, vasculitic neurologic/renal/pulmonary findings, syphilis or Lyme exposure, granulomatous disease, hematologic hyperviscosity, or medication toxicity. Obtain targeted serology/imaging in partnership with the relevant specialty.",
        "manage": "Treat urgent inner-ear loss promptly while pursuing the systemic cause, stop or modify ototoxic exposure when feasible, and coordinate immunosuppression or antimicrobial therapy with rheumatology, infectious disease, oncology, or primary teams. Do not label an isolated nonspecific positive autoimmune test as autoimmune inner-ear disease.",
        "teach": "Systemic disease is a hypothesis generated by phenotype and associated findings. The ear may be the presenting organ, but treatment must address both time-sensitive hearing loss and the underlying disease without allowing indiscriminate panels to replace clinical localization.",
    },
    ("Otology / Neurotology", "Hyperacusis / Decreased Sound Tolerance"): {
        "workup": "Define whether ordinary sounds are uncomfortably loud (loudness hyperacusis), painful, fear-provoking (phonophobia), or trigger disproportionate anger/aversion (misophonia). Perform audiometry and uncomfortable-loudness levels when useful, screen migraine, tinnitus, anxiety/PTSD and facial-nerve/stapedius disorders, and investigate unilateral neurologic or middle-ear findings selectively.",
        "manage": "Counsel against continuous overprotection in safe environments because excessive earplug use can reinforce central gain and avoidance. Use gradual sound enrichment/desensitization, hearing protection for truly hazardous noise, migraine treatment when relevant, and audiology/behavioral-health support for distress and avoidance. Treat an identified otologic or neurologic cause rather than promising a single procedural cure.",
        "teach": "Hyperacusis, phonophobia, and misophonia overlap but are not interchangeable. The goal is safe sound tolerance and restored function—not eliminating all sound exposure or normalizing one uncomfortable-loudness number.",
    },
    ("Otology / Neurotology", "Labyrinthitis / Infections of the Labyrinth"): {
        "workup": "Differentiate vestibular neuritis (acute vestibular syndrome without new cochlear loss) from labyrinthitis (vertigo plus new sensorineural hearing loss). Otitis media/mastoiditis, meningitis, fever, neurologic deficits, severe headache, or immunocompromise raises concern for suppurative/intracranial disease and warrants urgent audiometry, imaging, cultures, and specialty evaluation rather than a benign neuritis label.",
        "manage": "Use brief vestibular suppressants only during the most disabling acute period, then mobilize and begin vestibular rehabilitation. Treat bacterial otogenic or meningitic disease urgently with IV antibiotics and source control as indicated; steroids/antivirals follow the specific hearing-loss or viral syndrome rather than being automatic for every acute vertigo presentation.",
        "teach": "New hearing loss is the branch point: pure vestibular neuritis should not cause it. Suppurative labyrinthitis is an otologic/intracranial emergency and may permanently destroy hearing and vestibular function.",
    },
    ("Otology / Neurotology", "Central Vestibular Disorders"): {
        "workup": "In an acute vestibular syndrome, a trained HINTS/HINTS-plus examination can identify central physiology, but it is not a screening mnemonic for intermittent dizziness or untrained use. Direction-changing gaze-evoked nystagmus, skew, severe truncal ataxia, new hearing loss, focal neurologic deficits, headache/neck pain, vascular risk, or an atypical course lowers the threshold for stroke-pathway imaging and neurology involvement; early MRI can be falsely negative in posterior circulation stroke.",
        "manage": "Activate urgent stroke/neurologic evaluation for suspected central acute vestibular syndrome. For established nonacute central imbalance, treat the underlying disorder and use individualized vestibular/physical rehabilitation, fall prevention, and assistive strategies rather than chronic vestibular suppressants.",
        "teach": "Peripheral-appearing vertigo does not exclude stroke. HINTS is powerful only in the correct continuous acute vestibular syndrome, performed and interpreted by a trained examiner.",
    },
    ("Otology / Neurotology", "Vestibular Rehabilitation"): {
        "workup": "Identify the impairment before prescribing exercises: deficient vestibulo-ocular reflex, motion/visual sensitivity, positional vertigo, gait/balance limitation, or maladaptive avoidance. Measure fall risk and functional goals and exclude an untreated fluctuating or central process that needs separate management.",
        "manage": "Use gaze-stabilization/adaptation exercises for vestibulo-ocular-reflex deficits, habituation for reproducible motion sensitivity, substitution when vestibular recovery is limited, and balance/gait training with graded exposure. Repositioning maneuvers treat BPPV and should not be replaced by generic exercises. Minimize long-term vestibular suppressants because they can delay compensation.",
        "teach": "Rehabilitation must provoke a controlled, recoverable error signal to drive compensation; exercises that never challenge the impaired system do little, while excessive unsupervised provocation reduces adherence and fall safety.",
    },
    ("Otology / Neurotology", "Neurotologic Intraoperative Cranial-Nerve Monitoring"): {
        "workup": "Select modalities by nerve and operation: free-running/triggered EMG for facial or lower cranial motor nerves, BAER/ABR for auditory pathway trends, and somatosensory/motor evoked potentials when central pathways are at risk. Document baseline neurologic/hearing status and confirm that anesthesia, temperature, electrodes, stimulation current, and neuromuscular blockade permit interpretable signals.",
        "operate": "A signal change triggers a team response: announce it, stop the maneuver, release traction or irrigation/thermal stress, inspect the field, correct blood pressure/oxygenation/temperature/anesthetic and technical factors, retest, and alter or abort the approach when recovery fails. Stimulation identifies excitable nerve but does not guarantee postoperative function, and monitoring never substitutes for anatomic dissection.",
        "teach": "Trend, context, and reversibility matter more than one alarm. The useful question is what changed immediately before the signal and what reversible surgical, physiologic, anesthetic, or technical cause can be corrected now.",
    },
    ("Otology / Neurotology", "Lateral Skull-Base Tumor Framework"): {
        "workup": "Define epicenter, compartment, growth on serial imaging, hearing class, facial and lower-cranial-nerve function, vascularity, brainstem compression, venous-sinus/carotid relationship, and patient age/comorbidity. CT answers bone/air-cell questions; contrast MRI defines nerve, dura, brainstem, and soft tissue; angiography is selective for vascular tumors or planned embolization.",
        "manage": "Choose observation, stereotactic radiation, microsurgery, or combined therapy by diagnosis, growth, size, symptoms, hearing/facial goals, brainstem effect, and patient priorities. Vestibular schwannoma, paraganglioma, meningioma, facial-nerve schwannoma, endolymphatic-sac tumor, and temporal-bone malignancy do not share one algorithm.",
        "operate": "Match corridor to tumor and functional goal: middle fossa for selected small intracanalicular lesions with serviceable hearing, retrosigmoid for CPA access with potential hearing preservation, translabyrinthine when hearing is nonserviceable or exposure favors it, and infratemporal/jugular-foramen approaches for selected lower-skull-base disease. Plan CSF-leak closure, facial-nerve strategy, lower-CN morbidity, hearing rehabilitation, and vascular control before incision.",
        "teach": "Approach selection is a tradeoff among exposure, hearing, facial/lower-CN function, vascular control, and CSF-leak risk—not a tumor-name reflex.",
    },
    ("Pediatric Otolaryngology", "Pediatric Speech Disorders"): {
        "workup": "Separate speech-sound production, motor speech, resonance, fluency, and language delay. Confirm hearing, oral mechanism, palate/velopharyngeal function, development/cognition, multilingual exposure, and neurologic signs; use formal speech-language evaluation rather than attributing delay to ankyloglossia or recurrent otitis by assumption.",
        "manage": "Provide early speech-language intervention matched to the deficit, restore hearing access when impaired, and route structural resonance disease to a cleft/velopharyngeal team. Surgery treats a demonstrated structural mechanism; it does not replace therapy for phonologic, language, or motor-planning disorders.",
        "teach": "A child can pronounce sounds poorly, plan speech poorly, resonate abnormally, or have delayed language—four different problems. Name the domain before ordering an operation.",
    },
    ("Pediatric Otolaryngology", "Cleft Lip / Palate — ENT Surgical Fundamentals"): {
        "workup": "Assess cleft anatomy, feeding/growth, airway, hearing/OME, speech and resonance, dental/maxillary development, syndromic features, and prior repairs in a multidisciplinary cleft team. Before secondary speech surgery, define the velopharyngeal closure pattern with perceptual assessment and nasoendoscopy/videofluoroscopy rather than operating on hypernasality alone.",
        "manage": "Coordinate feeding support, tympanostomy/hearing surveillance, primary palatal repair, longitudinal speech therapy, dental/orthodontic care, and secondary VPI surgery when a structural gap persists. Repeated tubes address middle-ear disease but do not correct the Eustachian-tube muscular dysfunction caused by cleft anatomy.",
        "operate": "Primary palatoplasty restores separation and reconstructs the levator sling while minimizing fistula and growth disturbance. Secondary VPI procedures—pharyngeal flap, sphincter pharyngoplasty, or selected palatal revision—are chosen from closure pattern and gap, with explicit counseling about postoperative OSA and airway obstruction.",
        "teach": "Cleft care is a longitudinal airway-hearing-speech-growth program, not a single palate operation.",
    },
    ("Pediatric Otolaryngology", "Microtia Reconstruction"): {
        "workup": "Classify auricular deficiency, document canal atresia and facial-nerve/craniofacial anomalies, complete diagnostic hearing evaluation early, and obtain temporal-bone CT only when it will guide atresia surgery planning rather than routinely in infancy. Discuss autologous rib cartilage, porous polyethylene, prosthesis, and no reconstruction with the family.",
        "manage": "Provide early hearing rehabilitation for bilateral loss and appropriate unilateral counseling while sequencing auricular and canal reconstruction deliberately. Autologous framework construction is typically deferred until adequate rib/auricular growth; alloplastic reconstruction may occur earlier in selected centers. Coordinate any canalplasty with the reconstructive surgeon because incision location and vascularized tissue planes can compromise a future or existing framework.",
        "operate": "Autologous reconstruction builds and pockets a rib-cartilage framework, later elevating it to create projection; alloplastic reconstruction requires durable vascularized soft-tissue coverage, commonly temporoparietal fascia plus skin graft. Protect the facial nerve and superficial temporal vascular supply and avoid a canal approach that devascularizes the auricular construct.",
        "teach": "Hearing access comes first; aesthetic reconstruction and atresia surgery are sequenced, not independently scheduled.",
    },
    ("Pediatric Otolaryngology", "Pediatric Vestibular Disorders"): {
        "workup": "Use age-appropriate history from child and caregiver, neurologic/ocular-motor examination, hearing testing, positional testing, and selective vestibular tests. Common branches include vestibular migraine/recurrent vertigo of childhood, BPPV after trauma, unilateral/bilateral vestibular hypofunction, inner-ear malformation, medication effect, and central disease; school difficulty or delayed motor milestones may be the presenting functional clue.",
        "manage": "Treat the cause, use migraine lifestyle/preventive therapy when indicated, perform repositioning for BPPV, and prescribe pediatric vestibular/balance rehabilitation for hypofunction. Coordinate neurology, audiology, physical therapy, and school/fall-safety support; chronic vestibular suppressants impede compensation and are rarely a long-term solution.",
        "teach": "Children often report dizziness imprecisely. Translate the complaint into timing, triggers, hearing/neurologic associations, and observed balance function before assigning an adult vestibular label.",
    },
    ("Pediatric Otolaryngology", "Ankyloglossia / Maxillary Frenulum"): {
        "workup": "Document a functional feeding or articulation problem with direct observation and lactation/speech assessment rather than grading appearance alone. For breastfeeding, assess latch, maternal pain/trauma, milk transfer, weight gain, positioning, and alternative causes. An upper-lip frenulum is common anatomy and should not be released solely because it looks prominent.",
        "manage": "Begin with skilled feeding support. Consider lingual frenotomy when a restrictive lingual frenulum clearly contributes to persistent breastfeeding dysfunction despite conservative help; counsel that evidence is strongest for short-term maternal nipple-pain improvement and less certain for long-term feeding or prophylactic speech benefit. Do not promise prevention of sleep, dental, or speech disorders without a demonstrated functional indication.",
        "teach": "Treat function, not a photograph or score. Maxillary frenulum appearance alone is not an operative diagnosis.",
    },
    ("Pediatric Otolaryngology", "Pediatric Reflux / Eosinophilic Esophagitis"): {
        "workup": "Separate physiologic infant reflux, GERD with troublesome symptoms/complications, and eosinophilic esophagitis. Dysphagia, food impaction, feeding aversion, atopy, poor growth, or refractory symptoms warrant GI evaluation; EoE requires endoscopy with esophageal biopsies and cannot be diagnosed from laryngeal erythema or response to acid suppression.",
        "manage": "Use feeding/lifestyle measures and targeted acid suppression for appropriately selected GERD rather than empiric prolonged PPI therapy for nonspecific laryngeal symptoms. EoE treatment is coordinated with gastroenterology/allergy and may include dietary elimination, swallowed topical steroid, PPI-responsive pathways, dilation for selected strictures, and biologic therapy in qualifying disease.",
        "teach": "Reflux and EoE can share feeding and airway complaints, but only EoE is a biopsy-defined immune-mediated esophageal disease. A red larynx is not proof of either diagnosis.",
    },
    ("Pediatric Otolaryngology", "Laryngotracheal Cleft"): {
        "workup": "Suspect a cleft with persistent aspiration, recurrent pneumonia, cyanotic feeding events, chronic cough, or failure to thrive despite an unrevealing flexible examination. Swallow testing defines functional aspiration, but definitive diagnosis requires rigid endoscopy with palpation of the interarytenoid/posterior laryngeal region because a shallow cleft can be visually subtle.",
        "manage": "Use feeding modification, thickening when safe, reflux/nutrition support, and multidisciplinary aspiration management for suitable low-grade disease. Persistent pulmonary morbidity, failure of conservative therapy, or a deeper cleft supports endoscopic repair; extensive clefts may require open reconstruction and coordinated airway/esophageal planning.",
        "teach": "A normal-looking flexible larynx does not exclude a cleft. Palpation during rigid endoscopy is the diagnostic commitment point.",
    },
    ("Sleep Surgery", "Narcolepsy / Central Hypersomnolence Recognition"): {
        "workup": "Confirm chronic daily sleepiness despite adequate sleep opportunity, obtain sleep logs/actigraphy, exclude insufficient sleep, circadian misalignment, medication/substance effects, OSA and depression, then perform attended PSG followed by properly conducted MSLT when indicated. Cataplexy strongly supports narcolepsy type 1; CSF hypocretin testing is reserved for selected diagnostic uncertainty.",
        "manage": "Refer to sleep medicine for wake-promoting therapy and cataplexy/REM-symptom management, scheduled sleep strategies, driving/work/school safety, and treatment of coexisting OSA. Airway surgery does not treat central hypersomnolence when obstructive disease is absent or controlled.",
        "teach": "MSLT is interpretable only after adequate sleep and exclusion/treatment of confounders; sleep-onset REM periods are not meaningful when sleep deprivation or REM-modulating medications invalidate the test.",
    },
    ("Sleep Surgery", "Restless Legs / Periodic Limb Movement Disorders"): {
        "workup": "Diagnose RLS clinically by an urge to move the legs with unpleasant sensations, worse at rest and in the evening/night, relieved by movement, and not better explained by another condition. Check ferritin/iron indices and aggravating medications; periodic limb movements on PSG are supportive but do not by themselves diagnose symptomatic RLS or PLMD.",
        "manage": "Check morning ferritin and transferrin saturation. AASM good-practice thresholds support oral or IV iron in adults when ferritin is <=75 ng/mL or transferrin saturation is <20%, IV iron when ferritin is 75-100 ng/mL, and iron supplementation in children when ferritin is <50 ng/mL. Address alcohol, caffeine, antihistaminergic, serotonergic, and antidopaminergic drugs plus untreated OSA. For adults needing medication, gabapentin enacarbil, gabapentin, or pregabalin are guideline-supported; routine chronic dopamine-agonist use is discouraged because of augmentation and impulse-control risk.",
        "teach": "RLS is a waking symptom diagnosis; PLMS is a PSG observation. Treat the patient, not an isolated limb-movement index.",
    },
    ("Sleep Surgery", "Circadian Rhythm Sleep-Wake Disorders"): {
        "workup": "Define habitual sleep timing across work and free days with sleep diary and actigraphy, then distinguish delayed phase, advanced phase, irregular rhythm, non-24-hour disorder, shift-work disorder, and behaviorally imposed insufficient sleep. PSG is reserved for suspected comorbid sleep disease, not required to prove a timing disorder.",
        "manage": "Use precisely timed light, darkness, melatonin, and schedule shifts matched to the circadian phase; timing determines whether the clock advances or delays. Address school/work constraints and avoid sedatives or stimulants as substitutes for realignment when possible.",
        "teach": "Circadian treatment is a phase-response intervention: the right therapy at the wrong clock time can push the patient farther in the wrong direction.",
    },
}


OR_ROLE_NOTES = {
    "tonsillectomy": "ROLE: technique-centered standalone tonsil dissection and hemorrhage-rescue card. Use tonsillectomy-adenoidectomy for the combined pediatric OSA/disposition pathway and adenoidectomy for palate/Eustachian-tube-specific adenoid work.",
    "tonsillectomy-adenoidectomy": "ROLE: combined pediatric adenotonsillectomy decision, PSG-risk, disposition, and two-site operative card. Link to tonsillectomy for isolated tonsil technique/hemorrhage rescue and adenoidectomy for isolated adenoid indications or VPI-risk modification.",
    "adenoidectomy": "ROLE: isolated adenoid surgery card emphasizing choanae, torus tubarius, palate/VPI risk, and otologic indications. Do not duplicate the combined pediatric OSA pathway taught in tonsillectomy-adenoidectomy.",
    "DLB": "ROLE: pediatric-airway diagnostic measurement card, emphasizing stenosis mapping, spontaneous-versus-controlled ventilation, and postoperative airway disposition.",
    "direct-laryngoscopy-bronchoscopy": "ROLE: comprehensive exact-sequence airway-evaluation card with synchronous-lesion search and shared-airway rescue; retain as the advanced companion to the concise pediatric DLB card rather than presenting it as a separate operation.",
}


def _append(row, field, text):
    prior = row.get(field) or ""
    if not isinstance(prior, str):
        raise RuntimeError("v40.8: nontext field %s on %s" % (field, row.get("topic") or row.get("slug")))
    marker = "v40.8 priority completion: " + text
    if marker not in prior:
        row[field] = prior.rstrip() + ("\n\n" if prior.strip() else "") + marker


def apply_priority_remainder_v408(data_module, app_module=None):
    deep_source = getattr(data_module, "DEEP_MODULES_V6", None)
    ops_source = getattr(data_module, "OR_PREP_REGISTRY", None)
    if not isinstance(deep_source, dict) or not isinstance(ops_source, dict):
        raise RuntimeError("v40.8: production registries unavailable")
    deep, ops = deepcopy(deep_source), deepcopy(ops_source)
    index = {(domain, row.get("topic")): row for domain, rows in deep.items() for row in rows}
    missing = [key for key in DEPTH_UPDATES if key not in index]
    if missing:
        raise RuntimeError("v40.8: missing depth targets: %r" % (missing,))
    if any(slug not in ops for slug in OR_ROLE_NOTES):
        raise RuntimeError("v40.8: overlapping OR targets changed")

    source_rows = 0
    for domain, rows in deep.items():
        for row in rows:
            topic = str(row.get("topic") or "").strip()
            current = row.get("source_basis") or []
            if isinstance(current, str):
                current = [current]
            if not isinstance(current, list):
                raise RuntimeError("v40.8: malformed source_basis on %s > %s" % (domain, topic))
            additions = _core_sources(domain)
            additions += CLAIM_SOURCES.get(topic, [])
            row["source_basis"] = list(dict.fromkeys(current + additions))
            row["source_metadata_v408"] = {
                "canonical_domain": domain,
                "canonical_topic": topic,
                "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
                "locator_level": "domain-foundational",
                "reviewed_after": "v40.7",
            }
            source_rows += 1

    for key, fields in DEPTH_UPDATES.items():
        row = index[key]
        for field, text in fields.items():
            _append(row, field, text)
        row["depth_reviewed_v408"] = True

    for slug, note in OR_ROLE_NOTES.items():
        entry = ops[slug]
        entry["relationship_note_v408"] = note
        _append(entry, "indications", note)

    data_module.DEEP_MODULES_V6.clear(); data_module.DEEP_MODULES_V6.update(deep)
    data_module.OR_PREP_REGISTRY.clear(); data_module.OR_PREP_REGISTRY.update(ops)
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
        app_module.OR_PREP_REGISTRY = data_module.OR_PREP_REGISTRY
    return {
        "source_rows_traced": source_rows,
        "depth_topics_updated": len(DEPTH_UPDATES),
        "or_role_overlaps_reconciled": list(OR_ROLE_NOTES),
        "claim_specific_source_topics": len(CLAIM_SOURCES),
    }
