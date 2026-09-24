"""v44.1: close the "missing topics & grading scales" bucket from the 2026-09-23 deep
audit (bucket 4 + bucket 5 of the recommended prioritization list).

Adds 7 new dedicated topics that the audit flagged as classic/frequently-tested content
with no home in the curriculum:
  - Otology / Neurotology: Glomus Tumor / Paraganglioma
  - Laryngology / Voice / Swallowing: Laryngeal Electromyography (LEMG); Laryngocele
  - Head & Neck Oncology: Lip Cancer
  - Sleep Surgery: Nasal Surgery as a CPAP-Adherence Adjunct; Adult Epiglottic
    Collapse / Epiglottopexy; Tracheostomy as Definitive OSA Therapy

Confirmed via live audit of runtime_entry_pasha that congenital aural atresia/microtia
already has a dedicated topic (Pediatric Otolaryngology: "Microtia / Aural Atresia") --
per audit guidance this is extended with the Jahrsdoerfer scale below rather than
duplicated as a new topic.

Also adds named grading/classification-system content the audit found referenced or
implied but never actually taught, to 12 existing topics (appended to their `workup` or
`manage` field, guarded by a per-topic marker string for idempotency; no existing content
is removed):
  - Ménière Disease: AAO-HNS 1995 four-tone staging (I-IV)
  - Vestibular Schwannoma: Gardner-Robertson hearing classification (I-V)
  - Facial Paralysis: Sunnybrook Facial Grading System
  - External Branch of the Superior Laryngeal Nerve Injury: Cernea classification (1/2a/2b)
  - Auricular Reconstruction: Nagata / Brent / Tanzer staged technique framework
  - ZMC / Orbital Trauma: Manson orbital-floor-defect volume criterion
  - Facial Synkinesis / Static-Dynamic Rehabilitation: Sunnybrook synkinesis subscore
  - Hypoglossal Nerve Stimulation: <25% central+mixed-apnea eligibility threshold and
    STAR trial 12-month outcome data
  - Stroboscopy Interpretation: GRBAS, CAPE-V, VHI-10; AAO-HNSF Hoarseness (Dysphonia)
    CPG 2018 citation
  - Dysphagia / Aspiration: IDDSI framework and Penetration-Aspiration Scale
  - Microtia / Aural Atresia: Jahrsdoerfer 10-point grading scale
  - Palatal Surgery: Friedman tongue position/staging system; Sher surgical-success
    criteria

New-topic clinical content and grading-scale numbers were researched and cross-checked
against primary/authoritative sources before writing (AAO-HNS committee guidelines,
Gardner & Robertson 1988, Cernea et al. 1992, Jahrsdoerfer et al. 1992, Strollo et al.
STAR trial NEJM 2014, Rosenbek et al. 1996, IDDSI framework, Friedman 2002, Sher et al.
1996, Manson orbital-fracture literature, Fisch/Glasscock-Jackson paraganglioma staging).
Two items carry an explicit hedge in the curriculum text itself because the exact wording
could not be confirmed against a primary source during authoring (Jahrsdoerfer's precise
per-item list, and Tanzer's original stage count) -- flagged for a future citation-level
review rather than stated as more precise than verified.

Also bumps the 4 affected domains' expected topic counts in
audit_all_topic_source_saturation_v368.py's EXPECTED_DOMAIN_COUNTS (handled by a
one-line edit to that file alongside this module, not inside apply_fn) and adds 2
Concept Checks per new topic (14 total) so the new topics don't recreate the
zero-Concept-Check gap that v43.8 just closed.
"""

NEW_TOPICS_V441 = [
    {
        "topic": "Glomus Tumor / Paraganglioma",
        "primary_domain": "Otology / Neurotology",
        "recognize": (
            "Pulsatile tinnitus with a reddish or bluish mass behind an intact tympanic "
            "membrane, often with conductive hearing loss, suggests a jugulotympanic "
            "paraganglioma (glomus tympanicum or glomus jugulare). A positive Brown sign "
            "(the mass blanches with pneumatic otoscopy) supports a vascular middle-ear "
            "lesion over a simple effusion or granulation tissue."
        ),
        "localize": (
            "These tumors arise from paraganglion cells along Jacobson's nerve (tympanic "
            "branch of CN IX, on the cochlear promontory) or Arnold's nerve, or from the "
            "adventitia of the jugular bulb. Glomus tympanicum stays confined to the "
            "middle ear/promontory; glomus jugulare arises from the jugular bulb and can "
            "extend through the temporal bone toward the carotid canal, jugular foramen, "
            "and posterior fossa."
        ),
        "workup": (
            "CT temporal bone characterizes the bone-erosion pattern (permeative jugular "
            "plate erosion favors jugulare; a promontory-confined lesion favors "
            "tympanicum); MRI shows soft-tissue and dural extent, classically with a "
            "\"salt-and-pepper\" enhancement pattern from flow voids in a vascular tumor. "
            "Catheter angiography with preoperative embolization is used for large, "
            "vascular tumors to reduce operative blood loss. Because up to roughly a "
            "third to half of these are hereditary (paraganglioma-pheochromocytoma "
            "syndromes, most often SDHB/SDHD and also SDHC), obtain a family history, "
            "consider biochemical screening for catecholamine secretion, and refer for "
            "genetic counseling/testing -- SDHB in particular carries higher malignant/"
            "metastatic potential and should raise the threshold for full-body staging."
        ),
        "manage": (
            "Treatment is class- and patient-dependent: observation with serial imaging "
            "is reasonable for small tumors, older or frail patients, or limited-disease "
            "glomus tympanicum; stereotactic radiosurgery is a good option for higher-"
            "class tumors or when surgical morbidity (lower cranial neuropathy risk) "
            "outweighs the benefit of resection; microsurgical resection is preferred "
            "when a durable cure with acceptable morbidity is achievable."
        ),
        "operate": (
            "The Modified Fisch classification stages extent and guides the operative "
            "plan: Class A is confined to the middle ear (glomus tympanicum); Class B is "
            "limited to the tympanomastoid compartment without infralabyrinthine bone "
            "destruction; Class C is tympanojugular, extending beyond the tympanomastoid "
            "space toward the carotid canal/foramen lacerum (subclassified C1-C4 by "
            "carotid canal/ICA involvement); Class D has intracranial extension (De/Di, "
            "graded by dural displacement). Small Class A/B tumors are removed "
            "transcanal or via a transmastoid approach; Class C/D tumors need a lateral "
            "skull-base approach with proximal-to-distal vascular control and often a "
            "multidisciplinary neurotology/neurosurgery/vascular team, since jugular bulb "
            "and lower cranial nerve (IX-XII) preservation drive the approach as much as "
            "tumor removal does."
        ),
        "teach": (
            "Boards/chief framework: pulsatile tinnitus plus a reddish, blanching middle-"
            "ear mass is a paraganglioma until proven otherwise -- do not biopsy a "
            "suspected glomus tumor in clinic. Classify (Fisch A-D) before deciding "
            "treatment, since class drives both approach and morbidity risk. Preoperative "
            "embolization meaningfully reduces blood loss in vascular tumors. Always "
            "screen for a hereditary paraganglioma syndrome (SDHB/SDHD/SDHC) -- it changes "
            "counseling, surveillance, and the threshold for looking for synchronous or "
            "metastatic disease."
        ),
        "tags": ["glomus tumor", "paraganglioma", "jugulotympanic", "Fisch classification", "pulsatile tinnitus", "Brown sign", "SDHB SDHD"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — temporal bone paraganglioma anatomy, classification, workup, and management.",
            "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022), Neurotology/lateral skull base chapter.",
            "K.J. Lee's Essential Otolaryngology, 12e (2019), otology/neurotology chapters.",
        ],
        "source_metadata_v408": {
            "canonical_domain": "Otology / Neurotology",
            "canonical_topic": "Glomus Tumor / Paraganglioma",
            "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
            "locator_level": "domain-foundational",
            "reviewed_after": "v44.1",
        },
    },
    {
        "topic": "Laryngeal Electromyography (LEMG)",
        "primary_domain": "Laryngology / Voice / Swallowing",
        "recognize": (
            "A motionless or hypomobile vocal fold of uncertain cause -- true neurogenic "
            "paralysis versus mechanical fixation (cricoarytenoid joint fixation, "
            "posterior glottic scar) -- is the classic indication for laryngeal EMG."
        ),
        "localize": (
            "LEMG samples the thyroarytenoid-lateral cricoarytenoid (TA-LCA) complex, "
            "usually via a percutaneous approach through the cricothyroid membrane, and "
            "can separately sample the cricothyroid muscle to assess external branch of "
            "the superior laryngeal nerve (EBSLN) function."
        ),
        "workup": (
            "Normal motor unit recruitment despite fixed-appearing motion points toward a "
            "mechanical cause (confirm with laryngeal exam/palpation of the "
            "cricoarytenoid joint under anesthesia) rather than denervation. Fibrillation "
            "potentials with reduced or absent voluntary recruitment indicate active "
            "denervation. Polyphasic, synkinetic reinnervation potentials indicate "
            "ongoing but disorganized reinnervation -- a pattern associated with a worse "
            "chance of normal, purposeful motion returning, even though it may still "
            "eventually stabilize the airway (adductor synkinesis). A 2016 multidisciplinary "
            "consensus statement (neurolaryngology/AAO-HNS) supports LEMG for diagnosis, "
            "prognosis, and timing of intervention. Because fibrillation potentials take "
            "time to develop, testing performed very early after injury can be falsely "
            "reassuring; many practices favor obtaining LEMG only after several weeks "
            "have passed so the study is not misread as normal."
        ),
        "manage": (
            "LEMG findings help decide timing and choice of intervention: a favorable "
            "prognosis on LEMG may support observation or early reinnervation surgery, "
            "while a poor-prognosis pattern (or a patient who cannot wait for possible "
            "recovery) may favor proceeding directly to injection augmentation or "
            "framework medialization rather than deferring treatment on the chance of "
            "spontaneous recovery."
        ),
        "operate": (
            "LEMG results can guide selection and timing among injection laryngoplasty, "
            "framework (type I) medialization thyroplasty, and laryngeal reinnervation "
            "(e.g., ansa cervicalis-to-recurrent laryngeal nerve transfer) when recovery "
            "potential and timeline are uncertain from clinical exam alone."
        ),
        "teach": (
            "Boards/chief framework: a motionless fold is not automatically a "
            "\"paralyzed\" fold. LEMG's job is to separate neurogenic from mechanical "
            "causes of immobility and to time-stamp prognosis -- do not over-read a study "
            "performed too soon after injury, since a falsely normal-looking early exam "
            "can mislead both diagnosis and counseling."
        ),
        "tags": ["laryngeal EMG", "LEMG", "vocal fold immobility", "neurogenic vs mechanical", "synkinesis", "denervation"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — laryngeal electrodiagnosis, vocal fold immobility evaluation.",
            "Pasha & Golub, 6e (2022), Laryngology chapter — vocal fold paralysis workup.",
            "K.J. Lee's Essential Otolaryngology, 12e (2019), laryngology chapters.",
        ],
        "source_metadata_v408": {
            "canonical_domain": "Laryngology / Voice / Swallowing",
            "canonical_topic": "Laryngeal Electromyography (LEMG)",
            "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
            "locator_level": "domain-foundational",
            "reviewed_after": "v44.1",
        },
    },
    {
        "topic": "Laryngocele",
        "primary_domain": "Laryngology / Voice / Swallowing",
        "recognize": (
            "A neck or laryngeal mass that enlarges with Valsalva, straining, coughing, "
            "or playing a wind instrument -- sometimes with hoarseness, cough, globus, or "
            "airway symptoms -- suggests a laryngocele rather than a simple lymph node or "
            "lipoma."
        ),
        "localize": (
            "A laryngocele is an abnormal air-filled dilation of the laryngeal saccule "
            "(the appendix of the laryngeal ventricle, between the false and true vocal "
            "folds). An internal laryngocele stays confined within the thyrohyoid "
            "membrane in the paraglottic space; an external laryngocele herniates through "
            "the thyrohyoid membrane (typically via the superior laryngeal neurovascular "
            "hiatus) into the neck; a combined (mixed) laryngocele has both components."
        ),
        "workup": (
            "CT of the neck/larynx is essential and should be obtained before treating "
            "the mass as benign: laryngoceles coexist with an obstructing glottic or "
            "supraglottic squamous cell carcinoma at the saccule outlet in a clinically "
            "meaningful minority of cases, so imaging (and direct laryngoscopy with "
            "mucosal assessment) must actively exclude an underlying tumor rather than "
            "assume the mass is purely a laryngocele."
        ),
        "manage": (
            "Small, asymptomatic internal laryngoceles can be observed; symptomatic, "
            "enlarging, or airway-threatening laryngoceles warrant intervention, and any "
            "laryngocele found in association with a laryngeal malignancy is treated "
            "according to the cancer."
        ),
        "operate": (
            "Endoscopic marsupialization (unroofing the saccule endoscopically, often "
            "with a laser) is standard for internal laryngoceles. External and combined "
            "laryngoceles typically require open excision through the thyrohyoid "
            "membrane via a lateral neck approach, since the external component is not "
            "reliably addressed endoscopically."
        ),
        "teach": (
            "Boards/chief framework: never work up a laryngocele in isolation from the "
            "cancer question. A laryngocele can be the presenting sign of an obstructing "
            "glottic/supraglottic tumor, so imaging plus laryngoscopy to exclude "
            "malignancy comes before marsupialization or excision, not after."
        ),
        "tags": ["laryngocele", "saccule", "internal external combined", "Valsalva neck mass", "laryngeal cancer association"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — laryngeal saccular disorders, laryngocele classification and management.",
            "Pasha & Golub, 6e (2022), Laryngology chapter.",
            "K.J. Lee's Essential Otolaryngology, 12e (2019), laryngology chapters.",
        ],
        "source_metadata_v408": {
            "canonical_domain": "Laryngology / Voice / Swallowing",
            "canonical_topic": "Laryngocele",
            "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
            "locator_level": "domain-foundational",
            "reviewed_after": "v44.1",
        },
    },
    {
        "topic": "Lip Cancer",
        "primary_domain": "Head & Neck Oncology",
        "recognize": (
            "A non-healing ulcer, crusted lesion, or induration of the vermilion -- far "
            "more often the lower lip than the upper lip -- in a patient with chronic UV "
            "exposure, smoking, fair skin, or immunosuppression should raise concern for "
            "lip squamous cell carcinoma."
        ),
        "localize": (
            "Most lesions arise on the vermilion of the lower lip; upper lip and "
            "commissure involvement are less common but carry distinct implications. "
            "Commissure lesions are reconstructively challenging because there is less "
            "redundant tissue and the commissure is functionally critical for oral "
            "competence and speech."
        ),
        "workup": (
            "Full-thickness examination and palpation for induration, plus assessment for "
            "mental/inferior alveolar nerve involvement (perineural spread can present as "
            "chin/lip numbness) and regional nodal disease. Biopsy establishes histology "
            "and depth of invasion, which -- as in oral cavity SCC -- helps estimate "
            "occult nodal risk. Cross-sectional imaging is reserved for deep, advanced, "
            "or perineural-spread-suspicious lesions."
        ),
        "manage": (
            "Most lip cancers are treated surgically; radiation therapy is an option for "
            "patients who are not surgical candidates or for advanced/perineural disease."
        ),
        "operate": (
            "Surgical excision with adequate margins is standard; reconstruction depends "
            "on defect size and lip subunit, with options ranging from primary closure "
            "and wedge excision for small defects to Abbe, Estlander, or Karapandzic "
            "flaps for larger defects, particularly when the commissure is involved. "
            "Elective neck treatment is guided by depth-of-invasion thresholds that "
            "mirror oral cavity practice -- deeper lesions carry higher occult nodal risk "
            "and a lower threshold for elective neck dissection."
        ),
        "teach": (
            "Boards/chief framework: lip is its own AJCC primary site distinct from oral "
            "cavity, even though it is staged with similar T-category principles and "
            "managed with overlapping surgical logic. Lip SCC generally carries a more "
            "favorable prognosis than most other oral cavity subsites, but perineural "
            "spread along the mental/inferior alveolar nerve is a distinct risk that "
            "should change both imaging and margin planning when suspected."
        ),
        "tags": ["lip cancer", "lip SCC", "vermilion", "commissure", "Abbe Estlander Karapandzic flap", "perineural spread", "depth of invasion"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — lip and oral cavity cancer, reconstructive flap selection.",
            "Pasha & Golub, 6e (2022), Head & Neck Oncology chapter.",
            "K.J. Lee's Essential Otolaryngology, 12e (2019), head and neck oncology chapters.",
        ],
        "source_metadata_v408": {
            "canonical_domain": "Head & Neck Oncology",
            "canonical_topic": "Lip Cancer",
            "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
            "locator_level": "domain-foundational",
            "reviewed_after": "v44.1",
        },
    },
    {
        "topic": "Nasal Surgery as a CPAP-Adherence Adjunct",
        "primary_domain": "Sleep Surgery",
        "recognize": (
            "A patient with OSA and nasal obstruction (septal deviation, inferior "
            "turbinate hypertrophy, or nasal valve collapse) who reports CPAP intolerance, "
            "a high required pressure, mouth leak, or dry mouth/mask discomfort is a "
            "candidate to consider nasal airway optimization alongside PAP therapy."
        ),
        "localize": (
            "Elevated nasal resistance increases the work of breathing against a CPAP "
            "circuit and promotes mouth leak and pressure intolerance; the specific site "
            "of obstruction (internal/external nasal valve, septum, or turbinates) "
            "determines which corrective procedure is indicated."
        ),
        "workup": (
            "Nasal endoscopy to assess the valve, septum, and turbinates; a Cottle "
            "maneuver to screen for valve collapse; and correlation with the patient's "
            "own CPAP titration data (therapeutic pressure required, residual leak, and "
            "nightly usage hours) to confirm nasal obstruction is plausibly limiting "
            "adherence rather than another cause (mask fit, claustrophobia, pressure "
            "intolerance unrelated to the nose)."
        ),
        "manage": (
            "Set expectations explicitly: septoplasty, turbinate reduction, and/or "
            "functional nasal valve surgery do not cure OSA on their own and rarely "
            "normalize the AHI by themselves, but they can meaningfully lower the "
            "required therapeutic CPAP pressure and improve subjective tolerance and "
            "night-to-night adherence -- the outcome that matters most for a patient who "
            "was otherwise abandoning PAP therapy."
        ),
        "operate": (
            "Standard septoplasty and inferior turbinate reduction techniques apply; add "
            "a functional nasal valve procedure when a positive Cottle maneuver or "
            "endoscopic collapse identifies the valve as a contributing site."
        ),
        "teach": (
            "Boards/chief framework: this is an adherence adjunct, not a stand-alone OSA "
            "treatment. Measure success in CPAP usage hours per night and tolerated "
            "pressure, not in AHI reduction from the nasal surgery alone -- conflating "
            "the two is the classic teaching error."
        ),
        "tags": ["nasal surgery", "CPAP adherence", "septoplasty", "turbinate reduction", "nasal valve", "CPAP tolerance"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — nasal airway and OSA/CPAP interaction.",
            "Pasha & Golub, 6e (2022), Sleep Surgery chapter.",
            "K.J. Lee's Essential Otolaryngology, 12e (2019), rhinology and sleep chapters.",
        ],
        "source_metadata_v408": {
            "canonical_domain": "Sleep Surgery",
            "canonical_topic": "Nasal Surgery as a CPAP-Adherence Adjunct",
            "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
            "locator_level": "domain-foundational",
            "reviewed_after": "v44.1",
        },
    },
    {
        "topic": "Adult Epiglottic Collapse / Epiglottopexy",
        "primary_domain": "Sleep Surgery",
        "recognize": (
            "Drug-induced sleep endoscopy (DISE) revealing posterior prolapse of the "
            "epiglottis against the posterior pharyngeal wall identifies epiglottic "
            "collapse as an obstruction site -- one that is easy to miss on awake exam "
            "and often overlooked in patients labeled as \"CPAP failures\" or "
            "\"surgery-refractory\" without DISE."
        ),
        "localize": (
            "During sleep, negative inspiratory pressure can cause the epiglottis itself "
            "to fold posteriorly, obstructing the laryngeal inlet independent of (or in "
            "combination with) velar, oropharyngeal, or tongue-base collapse -- the "
            "epiglottis component of the VOTE (velum, oropharynx, tongue base, "
            "epiglottis) DISE classification."
        ),
        "workup": (
            "DISE is the key diagnostic tool for identifying epiglottic collapse as a "
            "distinct or contributing obstruction site, since it is a dynamic, "
            "sleep-state-dependent finding not reliably reproduced on awake flexible "
            "laryngoscopy."
        ),
        "manage": (
            "When epiglottic collapse is a major or sole contributor and PAP therapy or "
            "other measures fail or are not tolerated, surgical correction targeting the "
            "epiglottis is considered, usually alongside treatment of any other "
            "DISE-identified obstruction sites for best results."
        ),
        "operate": (
            "Epiglottopexy (suturing the epiglottis anteriorly to the tongue base or "
            "vallecula to prevent posterior prolapse) and partial epiglottectomy are the "
            "established surgical options for epiglottis-driven obstruction."
        ),
        "teach": (
            "Boards/chief framework: do not assume palate or tongue-base collapse "
            "explains every case of surgical or CPAP failure. DISE-confirmed epiglottic "
            "collapse is a distinct, correctable obstruction pattern that changes the "
            "operative plan."
        ),
        "tags": ["epiglottic collapse", "epiglottopexy", "DISE", "VOTE classification", "partial epiglottectomy"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — DISE, VOTE classification, epiglottic collapse management.",
            "Pasha & Golub, 6e (2022), Sleep Surgery chapter.",
            "K.J. Lee's Essential Otolaryngology, 12e (2019), sleep medicine/surgery chapters.",
        ],
        "source_metadata_v408": {
            "canonical_domain": "Sleep Surgery",
            "canonical_topic": "Adult Epiglottic Collapse / Epiglottopexy",
            "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
            "locator_level": "domain-foundational",
            "reviewed_after": "v44.1",
        },
    },
    {
        "topic": "Tracheostomy as Definitive OSA Therapy",
        "primary_domain": "Sleep Surgery",
        "recognize": (
            "A patient with severe OSA and life-threatening cardiopulmonary complications "
            "(severe hypoxemia, cor pulmonale, refractory arrhythmia) who has failed or "
            "cannot tolerate CPAP/BiPAP and other surgical options is a candidate for "
            "tracheostomy as definitive therapy."
        ),
        "localize": (
            "Tracheostomy bypasses the entire upper airway obstruction -- nasal, palatal, "
            "tongue-base, and supraglottic/laryngeal -- below the level of collapse, "
            "unlike any site-specific OSA surgery."
        ),
        "workup": (
            "Confirm OSA severity with polysomnography, document failure or intolerance "
            "of PAP therapy and of other surgical options, and assess candidacy for stoma "
            "creation and long-term tracheostomy care (neck anatomy, obesity, caregiver "
            "support, and the patient's or family's capacity for ongoing stoma "
            "management)."
        ),
        "manage": (
            "Historically, tracheostomy was the original definitive OSA treatment before "
            "CPAP existed and remains, mechanistically, the single most reliably "
            "effective intervention because it bypasses the obstruction entirely rather "
            "than treating one collapse site. It is reserved today as a last resort given "
            "the quality-of-life burden and stoma-care demands, but remains a genuinely "
            "appropriate option in select severe, refractory, high-risk patients -- not "
            "merely of historical interest."
        ),
        "operate": (
            "Standard tracheostomy technique is used. A fenestrated or capped tube worn "
            "during the day with nocturnal deflation/opening is a common strategy that "
            "preserves daytime speech and swallowing function while still resolving "
            "nocturnal obstruction."
        ),
        "teach": (
            "Boards/chief framework: know tracheostomy as the historical benchmark of "
            "\"cure\" against which every other OSA intervention is measured (near-"
            "complete resolution of obstructive events when the obstruction is bypassed), "
            "and know its narrow but real modern indication in severe, refractory, "
            "high-risk disease."
        ),
        "tags": ["tracheostomy", "OSA definitive therapy", "severe OSA", "cor pulmonale", "PAP failure"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — tracheostomy for OSA, historical and modern indications.",
            "Pasha & Golub, 6e (2022), Sleep Surgery chapter.",
            "K.J. Lee's Essential Otolaryngology, 12e (2019), sleep medicine/surgery chapters.",
        ],
        "source_metadata_v408": {
            "canonical_domain": "Sleep Surgery",
            "canonical_topic": "Tracheostomy as Definitive OSA Therapy",
            "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
            "locator_level": "domain-foundational",
            "reviewed_after": "v44.1",
        },
    },
]

# (domain, topic, field) -> (marker substring guarding idempotency, text to append)
GRADING_SCALE_APPENDS_V441 = {
    ("Otology / Neurotology", "Ménière Disease", "workup"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: stage disease severity with the AAO-HNS 1995 "
        "Committee on Hearing and Equilibrium four-tone (0.5, 1, 2, 3 kHz) pure-tone-"
        "average system, using the worst audiogram obtained during the 6-month interval "
        "before treatment: Stage I ≤25 dB, Stage II 26-40 dB, Stage III 41-70 dB, Stage "
        "IV >70 dB. Staging is for reporting/comparing outcomes and counseling, not a "
        "substitute for the clinical diagnostic criteria themselves."
    ),
    ("Otology / Neurotology", "Vestibular Schwannoma", "workup"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: the Gardner-Robertson hearing classification "
        "is the standard scale for reporting hearing in vestibular schwannoma (distinct "
        "from, but conceptually related to, the AAO-HNS class already used above): Class "
        "I (good) PTA 0-30 dB with speech discrimination 70-100%; Class II (serviceable) "
        "PTA 31-50 dB with 50-69% discrimination; Class III (non-serviceable) PTA 51-90 "
        "dB with 5-49% discrimination; Class IV (poor) PTA 90-100 dB with 1-4% "
        "discrimination; Class V (deaf), no measurable hearing. Classes I-II are "
        "considered serviceable hearing; III-V are not -- this distinction drives "
        "hearing-preservation candidacy discussions."
    ),
    ("Otology / Neurotology", "Facial Paralysis", "workup"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: the Sunnybrook Facial Grading System is a "
        "complementary, more granular alternative to House-Brackmann, scoring resting "
        "symmetry, voluntary movement of five facial actions, and synkinesis separately "
        "to produce a composite score out of 100 (100 = normal). It is especially useful "
        "when synkinesis needs to be tracked over time, which House-Brackmann does not "
        "capture well."
    ),
    ("Thyroid / Parathyroid / Salivary", "External Branch of the Superior Laryngeal Nerve Injury", "workup"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: the Cernea classification describes the "
        "EBSLN's course relative to the superior thyroid pole/vessels and predicts "
        "injury risk during thyroidectomy: Type 1 crosses the vessels more than 1 cm "
        "above the superior pole (lowest risk); Type 2a crosses less than 1 cm above the "
        "pole (moderate risk); Type 2b crosses at or below the upper edge of the "
        "superior pole, often within the ligation field of the superior pedicle (highest "
        "injury risk, and more common in large glands/goiters). Knowing the likely "
        "Cernea type before ligating the superior pedicle is part of deliberate nerve "
        "preservation, not just careful dissection in general."
    ),
    ("Facial Plastics / Trauma", "Auricular Reconstruction", "operate"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: named staged costal-cartilage techniques "
        "differ mainly in stage count and timing. Brent's technique uses 4 stages "
        "roughly 3 months apart (framework carving/placement; lobule transposition; "
        "elevation with sulcus creation and skin grafting; tragus construction/conchal "
        "excavation). Nagata's technique compresses this into 2 stages spaced further "
        "apart (a single framework incorporating tragus and lobule at once, followed by "
        "elevation with a cartilage wedge, flap, and skin graft) and is typically "
        "performed later, when more costal cartilage is available. Tanzer's original "
        "technique, historically described as a multi-stage approach (lobule "
        "transposition, framework construction/placement, elevation, tragus "
        "construction, conchal definition), was the predecessor that Brent's method "
        "refined; its exact original stage count is reported inconsistently across "
        "secondary sources and is not restated here as a specific number."
    ),
    ("Facial Plastics / Trauma", "ZMC / Orbital Trauma", "manage"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: Manson's work on orbital floor fractures "
        "established that a floor defect greater than roughly 2 cm² (or involving more "
        "than about 50% of the floor) is the threshold commonly used to flag "
        "\"extensive\" bony loss that carries meaningful enophthalmos risk and favors "
        "repair, even without acute entrapment; a lower pediatric-specific threshold "
        "(around 1.8 cm²) has been proposed given children's more elastic, "
        "greenstick-prone orbital bone. Use this alongside clinical findings "
        "(entrapment, diplopia, measured enophthalmos), not as a stand-alone trigger for "
        "surgery."
    ),
    ("Facial Plastics / Trauma", "Facial Synkinesis / Static-Dynamic Rehabilitation", "workup"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: the Sunnybrook Facial Grading System's "
        "synkinesis subscore is the standard way to quantify synkinesis severity "
        "specifically (scored across several voluntary movements and combined with the "
        "resting-symmetry and voluntary-movement subscores into the composite Sunnybrook "
        "total), and is preferred over House-Brackmann for tracking synkinesis over the "
        "course of neuromuscular retraining or botulinum toxin treatment."
    ),
    ("Sleep Surgery", "Hypoglossal Nerve Stimulation", "workup"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: standard candidacy criteria (as used in the "
        "STAR trial and current payer policy) exclude patients whose central and mixed "
        "apnea events make up 25% or more of the total AHI, since conventional unilateral "
        "hypoglossal nerve stimulation targets obstructive, not central, events. Know "
        "this threshold explicitly rather than as a vague \"mostly obstructive\" "
        "requirement."
    ),
    ("Sleep Surgery", "Hypoglossal Nerve Stimulation", "manage"): (
        "v44.1 evidence addition",
        "\n\nv44.1 evidence addition: the pivotal STAR trial (Strollo et al., NEJM 2014) "
        "reported a median AHI reduction from 29.3 to 9.0 at 12 months (mean 32.0 to "
        "15.3), a 66% responder rate (≥50% AHI reduction and AHI <20/hr), and a mean "
        "Epworth Sleepiness Scale improvement of 4.7 points (11.6 to 7.0) -- know these "
        "as the benchmark outcome numbers for counseling and for board questions about "
        "expected HNS efficacy."
    ),
    ("Laryngology / Voice / Swallowing", "Stroboscopy Interpretation", "workup"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: pair stroboscopic findings with standardized "
        "voice-assessment tools rather than treating the strobe image alone as the full "
        "evaluation. GRBAS is a clinician-rated auditory-perceptual scale (Grade, "
        "Roughness, Breathiness, Asthenia, Strain, each 0-3). CAPE-V has the clinician "
        "rate overall severity, roughness, breathiness, strain, pitch, and loudness on "
        "100 mm visual analog scales. VHI-10 is a 10-item patient-reported handicap "
        "questionnaire (each item 0-4, maximum score 40) capturing the functional, "
        "physical, and emotional impact of a voice disorder. This content, and much of "
        "this topic's approach to dysphonia workup, draws on the AAO-HNSF Clinical "
        "Practice Guideline: Hoarseness (Dysphonia), 2018 update."
    ),
    ("Laryngology / Voice / Swallowing", "Dysphagia / Aspiration", "workup"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: describe swallowing safety and diet texture "
        "using standardized scales rather than free text alone. The International "
        "Dysphagia Diet Standardisation Initiative (IDDSI) framework spans levels 0-7 "
        "across a single continuum covering both drinks (thinner levels) and foods "
        "(thicker/more textured levels), replacing older inconsistent facility-specific "
        "diet terminology. The Penetration-Aspiration Scale (Rosenbek et al., 1996) is an "
        "8-point scale describing how far material enters the airway and whether/how it "
        "is cleared: 1 = no airway entry, up through 8 = material passes below the "
        "vocal folds with no effort to eject it (silent aspiration) -- the finding of "
        "greatest concern on FEES/MBS."
    ),
    ("Pediatric Otolaryngology", "Microtia / Aural Atresia", "workup"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: the Jahrsdoerfer grading scale is the standard "
        "tool for assessing atresiaplasty candidacy from temporal bone CT, scored out of "
        "10 points with the presence of the stapes weighted most heavily (2 points, "
        "since a mobile, present stapes is the single strongest predictor of surgical "
        "hearing outcome) and the remaining criteria (which include oval window, round "
        "window, middle ear space aeration, facial nerve course, malleus-incus complex, "
        "mastoid pneumatization, and external ear appearance) each contributing further "
        "points. A score of roughly 7/10 or higher is the threshold commonly cited for a "
        "good surgical candidate; this curriculum states that threshold as commonly "
        "cited rather than as a single universally fixed cutoff, since sources vary "
        "slightly on the exact per-item breakdown and boundary score -- confirm against "
        "the original Jahrsdoerfer criteria when precision matters for a specific case."
    ),
    ("Sleep Surgery", "Palatal Surgery", "workup"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: the Friedman tongue position (FTP) and "
        "Friedman staging system predict palatal-surgery (UPPP) success and belong in "
        "the preoperative anatomic assessment, not just tonsil size. FTP grades "
        "oropharyngeal crowding with the tongue at rest and mouth open (not a true "
        "Mallampati, which uses phonation): FTP I = uvula and tonsils/pillars fully "
        "visible; FTP II = uvula visible but tonsils/pillars obscured by the tongue "
        "base; FTP III = only the soft palate and base of the uvula visible; FTP IV = "
        "only the hard palate visible. Combining FTP with tonsil size and BMI yields "
        "Friedman Stage I (FTP I-II with large tonsils, generally BMI-favorable), Stage "
        "II (intermediate combinations), and Stage III (FTP III-IV with small tonsils, "
        "or BMI ≥40 which overrides other findings to Stage III). Reported single-level "
        "UPPP success rates fall sharply across stages (roughly 80% in Stage I, 38% in "
        "Stage II, 8% in Stage III), which is why site/stage selection -- not technique "
        "alone -- drives outcome counseling."
    ),
    ("Sleep Surgery", "Palatal Surgery", "manage"): (
        "v44.1 grading-scale addition",
        "\n\nv44.1 grading-scale addition: define surgical success explicitly using the "
        "Sher criteria (Sher et al., 1996): a ≥50% reduction in AHI from baseline AND a "
        "postoperative AHI below 20 events/hour. Counsel patients using this definition "
        "rather than an informal sense of \"better\" -- it is the standard reported "
        "outcome measure across the sleep-surgery literature and the one board questions "
        "will reference."
    ),
}

NEW_CONCEPT_CHECKS_V441 = [
    {
        "id": "cc-v112-rec-otology-neurotology-glomus-tumor-paraganglioma",
        "domain": "Otology / Neurotology",
        "topic": "Glomus Tumor / Paraganglioma",
        "choices": [],
        "answer": None,
        "explanation": "This check tests recognition and initial workup of jugulotympanic paraganglioma.",
        "board_pearl": "Pulsatile tinnitus plus a reddish, blanching middle-ear mass (positive Brown sign) is a paraganglioma until proven otherwise; do not biopsy it in clinic.",
        "curveball": "Up to roughly a third to half of these tumors are hereditary (SDHB/SDHD/SDHC paraganglioma-pheochromocytoma syndromes), which changes counseling and surveillance.",
        "tier": "Concept check",
        "mode": "Recognize",
        "concept_id": "v6-otology-neurotology-glomus-tumor-paraganglioma",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "prompt": (
            "A patient presents with pulsatile tinnitus and a reddish, pulsatile-appearing "
            "mass visible behind an intact tympanic membrane, with mild conductive hearing "
            "loss. Pneumatic otoscopy causes the mass to blanch. What is the diagnosis, how "
            "should it be worked up, and what genetic consideration should not be skipped?"
        ),
        "answer_text": (
            "This presentation (pulsatile tinnitus, blanching vascular middle-ear mass, "
            "positive Brown sign) is classic for a jugulotympanic paraganglioma (glomus "
            "tympanicum or glomus jugulare). Do not biopsy it in clinic. Workup starts with "
            "CT temporal bone to characterize the bone-erosion pattern and MRI to assess "
            "soft-tissue/dural extent (classic salt-and-pepper enhancement); large vascular "
            "tumors are often embolized preoperatively via catheter angiography to reduce "
            "blood loss. Because a meaningful fraction of these tumors are hereditary "
            "(SDHB/SDHD/SDHC paraganglioma-pheochromocytoma syndromes), family history, "
            "biochemical screening for catecholamine secretion, and genetic "
            "counseling/testing should be pursued rather than treating this as a purely "
            "sporadic lesion."
        ),
        "recall_source": "Deep Curriculum",
        "curveball_answer": (
            "Classify extent with the Modified Fisch system (A middle ear only; B "
            "tympanomastoid without infralabyrinthine erosion; C tympanojugular extension "
            "toward the carotid canal, C1-C4 by ICA involvement; D intracranial extension) "
            "before choosing observation, stereotactic radiosurgery, or microsurgical "
            "resection -- higher-class tumors and older/frailer patients favor observation "
            "or SRS over resection given lower cranial nerve risk."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-mgt-otology-neurotology-glomus-tumor-paraganglioma",
        "domain": "Otology / Neurotology",
        "topic": "Glomus Tumor / Paraganglioma",
        "stem": "A patient has a Fisch Class C tympanojugular paraganglioma. Which management principle is most appropriate?",
        "choices": [
            "Biopsy the mass transcanally in clinic to confirm histology before any imaging.",
            "Obtain CT temporal bone and MRI to define extent, consider preoperative embolization for a vascular tumor, and plan a lateral skull-base approach with a multidisciplinary team given the class and extent.",
            "Start empiric oral corticosteroids and reassess with an audiogram in six weeks.",
            "Proceed directly to stereotactic radiosurgery without imaging characterization, since all glomus tumors respond equally regardless of class.",
        ],
        "answer": 1,
        "explanation": "Class C/D tumors require full extent-defining imaging, consideration of preoperative embolization for vascular lesions, and a multidisciplinary lateral skull-base approach given proximity to the carotid canal, jugular bulb, and lower cranial nerves.",
        "why_wrong": [
            "Biopsying a suspected vascular paraganglioma in clinic risks serious hemorrhage and is never appropriate before imaging.",
            "Correct.",
            "Corticosteroids and a delayed audiogram do not address a vascular skull-base tumor and delay appropriate imaging/staging.",
            "Treatment choice (observation, SRS, or surgery) depends on class and patient factors, not a uniform default; imaging-based staging always comes first.",
        ],
        "board_pearl": "Pulsatile tinnitus plus a reddish, blanching middle-ear mass (positive Brown sign) is a paraganglioma until proven otherwise; do not biopsy it in clinic.",
        "curveball": "Up to roughly a third to half of these tumors are hereditary (SDHB/SDHD/SDHC paraganglioma-pheochromocytoma syndromes), which changes counseling and surveillance.",
        "tier": "Concept check",
        "mode": "Manage",
        "concept_id": "v6-otology-neurotology-glomus-tumor-paraganglioma",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "curveball_answer": (
            "Screen for hereditary paraganglioma syndrome (SDHB/SDHD/SDHC) with family "
            "history, biochemical testing, and genetic counseling/testing -- SDHB in "
            "particular carries higher malignant/metastatic potential and should raise "
            "the threshold for broader staging."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-rec-laryngology-voice-swallowing-laryngeal-electromyography-lemg",
        "domain": "Laryngology / Voice / Swallowing",
        "topic": "Laryngeal Electromyography (LEMG)",
        "choices": [],
        "answer": None,
        "explanation": "This check tests LEMG's role in distinguishing neurogenic from mechanical vocal fold immobility.",
        "board_pearl": "A motionless fold is not automatically a paralyzed fold -- LEMG separates neurogenic immobility from mechanical fixation (e.g., cricoarytenoid joint fixation).",
        "curveball": "LEMG performed very early after injury can be falsely reassuring, since fibrillation potentials take time to develop.",
        "tier": "Concept check",
        "mode": "Recognize",
        "concept_id": "v6-laryngology-voice-swallowing-laryngeal-electromyography-lemg",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "prompt": (
            "A patient has a hypomobile vocal fold after thyroid surgery. The surgeon is "
            "unsure whether this represents recurrent laryngeal nerve injury or mechanical "
            "fixation from posterior glottic scar/joint injury. How does laryngeal EMG help, "
            "and what timing consideration matters?"
        ),
        "answer_text": (
            "Laryngeal EMG samples the thyroarytenoid-lateral cricoarytenoid complex "
            "(percutaneously through the cricothyroid membrane) and can separate causes: "
            "normal motor unit recruitment despite immobility suggests a mechanical cause "
            "(confirm with direct laryngoscopy/palpation of the cricoarytenoid joint under "
            "anesthesia), while fibrillation potentials with reduced or absent recruitment "
            "indicate active denervation, and polyphasic synkinetic reinnervation potentials "
            "indicate disorganized reinnervation with a worse prognosis for normal motion. "
            "Timing matters: fibrillation potentials take time to develop, so testing too "
            "early after injury can be falsely reassuring and should generally be deferred "
            "several weeks when possible."
        ),
        "recall_source": "Deep Curriculum",
        "curveball_answer": (
            "LEMG findings guide timing and choice of intervention -- a favorable "
            "prognosis may support observation or early reinnervation surgery, while a "
            "poor-prognosis pattern may favor proceeding directly to injection "
            "augmentation or framework medialization rather than waiting for uncertain "
            "spontaneous recovery."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-mgt-laryngology-voice-swallowing-laryngeal-electromyography-lemg",
        "domain": "Laryngology / Voice / Swallowing",
        "topic": "Laryngeal Electromyography (LEMG)",
        "stem": "LEMG on a hypomobile vocal fold shows normal motor unit recruitment despite the immobility. What does this most strongly suggest, and what should follow?",
        "choices": [
            "Active denervation of the recurrent laryngeal nerve; proceed to observation for 12 months awaiting reinnervation.",
            "A mechanical cause of immobility, such as cricoarytenoid joint fixation; confirm with direct laryngoscopy and palpation of the joint under anesthesia.",
            "Bilateral vocal fold paralysis requiring urgent tracheostomy regardless of exam findings.",
            "A technical error in electrode placement that should be repeated with no further workup.",
        ],
        "answer": 1,
        "explanation": "Normal recruitment despite fixed-appearing motion points away from denervation and toward a mechanical cause; joint palpation under anesthesia confirms fixation versus true paralysis.",
        "why_wrong": [
            "Denervation would be expected to show fibrillation potentials with reduced/absent recruitment, not normal recruitment.",
            "Correct.",
            "Airway management decisions depend on the full clinical picture (bilaterality, airway symptoms), not on this single EMG finding alone, and normal recruitment argues against a neurogenic bilateral paralysis picture here.",
            "Normal recruitment is a meaningful, expected finding pattern for a mechanical cause, not evidence of a technical artifact.",
        ],
        "board_pearl": "A motionless fold is not automatically a paralyzed fold -- LEMG separates neurogenic immobility from mechanical fixation (e.g., cricoarytenoid joint fixation).",
        "curveball": "LEMG performed very early after injury can be falsely reassuring, since fibrillation potentials take time to develop.",
        "tier": "Concept check",
        "mode": "Manage",
        "concept_id": "v6-laryngology-voice-swallowing-laryngeal-electromyography-lemg",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "curveball_answer": (
            "Because fibrillation potentials take time to appear, a normal-appearing early "
            "study does not fully exclude denervation; when timing is early after injury, "
            "correlate carefully with the clinical picture and consider the possibility of "
            "repeat testing later if the diagnosis remains uncertain."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-rec-laryngology-voice-swallowing-laryngocele",
        "domain": "Laryngology / Voice / Swallowing",
        "topic": "Laryngocele",
        "choices": [],
        "answer": None,
        "explanation": "This check tests recognition and mandatory cancer-exclusion workup for laryngocele.",
        "board_pearl": "Never work up a laryngocele in isolation from the cancer question -- it can be the presenting sign of an obstructing glottic/supraglottic tumor.",
        "curveball": "An internal laryngocele stays within the thyrohyoid membrane; an external laryngocele herniates through it into the neck; a combined laryngocele has both components.",
        "tier": "Concept check",
        "mode": "Recognize",
        "concept_id": "v6-laryngology-voice-swallowing-laryngocele",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "prompt": (
            "A patient reports a neck mass that enlarges when he plays the trumpet, along "
            "with mild hoarseness. What is the likely diagnosis, what must be excluded "
            "before treatment, and how is it managed?"
        ),
        "answer_text": (
            "This is classic for a laryngocele -- an abnormal air-filled dilation of the "
            "laryngeal saccule that enlarges with Valsalva/positive intrathoracic pressure "
            "maneuvers such as playing a wind instrument. Before treating it as benign, CT "
            "of the neck/larynx (plus direct laryngoscopy) must exclude an obstructing "
            "glottic or supraglottic squamous cell carcinoma at the saccule outlet, since "
            "laryngoceles coexist with laryngeal cancer in a clinically meaningful minority "
            "of cases. Once malignancy is excluded, small asymptomatic internal "
            "laryngoceles can be observed; symptomatic or enlarging ones are treated with "
            "endoscopic marsupialization (internal) or open excision through the "
            "thyrohyoid membrane (external/combined)."
        ),
        "recall_source": "Deep Curriculum",
        "curveball_answer": (
            "An internal laryngocele is confined within the thyrohyoid membrane in the "
            "paraglottic space; an external laryngocele herniates through the thyrohyoid "
            "membrane (typically via the superior laryngeal neurovascular hiatus) into the "
            "neck; a combined/mixed laryngocele has both components, and external/combined "
            "disease generally needs open excision rather than endoscopic marsupialization "
            "alone."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-mgt-laryngology-voice-swallowing-laryngocele",
        "domain": "Laryngology / Voice / Swallowing",
        "topic": "Laryngocele",
        "stem": "A CT scan confirms an external laryngocele with no evidence of an underlying tumor. What is the most appropriate management?",
        "choices": [
            "Endoscopic marsupialization alone, since all laryngoceles respond equally well to this approach.",
            "Open excision through the thyrohyoid membrane via a lateral neck approach, since the external component is not reliably addressed endoscopically.",
            "Observation only, regardless of symptoms, since laryngoceles never require treatment once cancer is excluded.",
            "Radiation therapy, since laryngoceles are treated the same as laryngeal carcinoma once identified.",
        ],
        "answer": 1,
        "explanation": "External and combined laryngoceles typically require open excision through the thyrohyoid membrane, unlike internal laryngoceles, which can often be marsupialized endoscopically.",
        "why_wrong": [
            "Endoscopic marsupialization is standard for internal laryngoceles, not for external disease, which extends beyond endoscopic reach.",
            "Correct.",
            "Symptomatic or enlarging laryngoceles warrant intervention even after cancer is excluded; observation is reserved for small asymptomatic internal laryngoceles.",
            "Radiation therapy treats laryngeal carcinoma, not a benign laryngocele; conflating the two is a key testing pitfall this topic is designed to catch.",
        ],
        "board_pearl": "Never work up a laryngocele in isolation from the cancer question -- it can be the presenting sign of an obstructing glottic/supraglottic tumor.",
        "curveball": "An internal laryngocele stays within the thyrohyoid membrane; an external laryngocele herniates through it into the neck; a combined laryngocele has both components.",
        "tier": "Concept check",
        "mode": "Manage",
        "concept_id": "v6-laryngology-voice-swallowing-laryngocele",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "curveball_answer": (
            "Internal laryngoceles are generally managed with endoscopic marsupialization; "
            "reserve open excision for external or combined disease, and always confirm "
            "the absence of an obstructing tumor before either approach."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-rec-head-neck-oncology-lip-cancer",
        "domain": "Head & Neck Oncology",
        "topic": "Lip Cancer",
        "choices": [],
        "answer": None,
        "explanation": "This check tests recognition, workup, and management principles for lip squamous cell carcinoma.",
        "board_pearl": "Lip is its own AJCC primary site distinct from oral cavity, though staged with similar T-category principles.",
        "curveball": "Perineural spread along the mental/inferior alveolar nerve can present as chin/lip numbness and should change imaging and margin planning.",
        "tier": "Concept check",
        "mode": "Recognize",
        "concept_id": "v6-head-neck-oncology-lip-cancer",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "prompt": (
            "An older patient with significant sun exposure presents with a non-healing, "
            "crusted ulcer on the vermilion of the lower lip. What is the likely diagnosis, "
            "what should the workup specifically assess, and what determines the need for "
            "elective neck treatment?"
        ),
        "answer_text": (
            "This presentation is classic for lip squamous cell carcinoma, most common on "
            "the sun-exposed lower lip vermilion. Workup includes full-thickness "
            "examination and palpation for induration, assessment for mental/inferior "
            "alveolar nerve involvement (perineural spread can present as chin/lip "
            "numbness), and a regional nodal exam, with biopsy to establish histology and "
            "depth of invasion. As in oral cavity SCC, depth of invasion helps estimate "
            "occult nodal risk and guides the threshold for elective neck dissection -- "
            "deeper lesions carry higher occult nodal risk and a lower threshold for "
            "treating the neck electively."
        ),
        "recall_source": "Deep Curriculum",
        "curveball_answer": (
            "Reconstruction depends on defect size and lip subunit: small defects allow "
            "primary closure or wedge excision, while larger defects (especially "
            "involving the commissure) require Abbe, Estlander, or Karapandzic flaps to "
            "preserve oral competence and speech."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-mgt-head-neck-oncology-lip-cancer",
        "domain": "Head & Neck Oncology",
        "topic": "Lip Cancer",
        "stem": "A patient with lip SCC has new chin numbness. What does this finding most specifically suggest, and how should it change management?",
        "choices": [
            "It suggests unrelated trigeminal neuralgia and should not affect the cancer workup.",
            "It suggests perineural spread along the mental/inferior alveolar nerve, which should prompt targeted imaging and may change margin planning.",
            "It suggests distant metastasis to the brain and warrants immediate palliative referral.",
            "It is an expected postoperative finding only and is not relevant preoperatively.",
        ],
        "answer": 1,
        "explanation": "New sensory change in the distribution of the mental/inferior alveolar nerve in a patient with lip SCC should raise concern for perineural spread, which changes imaging and margin planning.",
        "why_wrong": [
            "In a patient with known lip SCC, new numbness in the nerve's distribution should not be dismissed as an unrelated diagnosis without evaluation.",
            "Correct.",
            "Chin numbness reflects local perineural spread along a named nerve, not a typical presentation of distant brain metastasis.",
            "This finding is relevant preoperatively and should prompt further workup, not be deferred to the postoperative period.",
        ],
        "board_pearl": "Lip is its own AJCC primary site distinct from oral cavity, though staged with similar T-category principles.",
        "curveball": "Perineural spread along the mental/inferior alveolar nerve can present as chin/lip numbness and should change imaging and margin planning.",
        "tier": "Concept check",
        "mode": "Manage",
        "concept_id": "v6-head-neck-oncology-lip-cancer",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "curveball_answer": (
            "Most lip cancers are treated surgically with margin-based excision; "
            "radiation is reserved for patients who are not surgical candidates or for "
            "advanced/perineural disease."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-rec-sleep-surgery-nasal-surgery-as-a-cpap-adherence-adjunct",
        "domain": "Sleep Surgery",
        "topic": "Nasal Surgery as a CPAP-Adherence Adjunct",
        "choices": [],
        "answer": None,
        "explanation": "This check tests the correct framing of nasal surgery's role relative to CPAP therapy in OSA.",
        "board_pearl": "Measure success in CPAP usage hours and tolerated pressure, not AHI reduction from the nasal surgery alone.",
        "curveball": "A positive Cottle maneuver identifies nasal valve collapse as a contributing site that may need its own procedure, not just septoplasty/turbinate reduction.",
        "tier": "Concept check",
        "mode": "Recognize",
        "concept_id": "v6-sleep-surgery-nasal-surgery-as-a-cpap-adherence-adjunct",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "prompt": (
            "A patient with OSA and septal deviation reports he cannot tolerate his "
            "prescribed CPAP pressure due to significant mouth leak and nasal congestion. "
            "How should nasal surgery be framed in this discussion, and what should be used "
            "to judge whether it helped?"
        ),
        "answer_text": (
            "Nasal surgery (septoplasty, turbinate reduction, and/or nasal valve surgery "
            "when indicated) should be framed explicitly as a CPAP-adherence adjunct, not "
            "as a stand-alone OSA cure -- it does not reliably normalize the AHI by "
            "itself. The correct outcome measures are the required therapeutic CPAP "
            "pressure, residual mask leak, and nightly usage hours, since the goal is "
            "improving tolerance and adherence to PAP therapy that the patient was "
            "otherwise abandoning."
        ),
        "recall_source": "Deep Curriculum",
        "curveball_answer": (
            "Workup should include nasal endoscopy and a Cottle maneuver to identify "
            "which specific site (valve, septum, or turbinates) is contributing, since "
            "that determines which procedure is indicated."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-mgt-sleep-surgery-nasal-surgery-as-a-cpap-adherence-adjunct",
        "domain": "Sleep Surgery",
        "topic": "Nasal Surgery as a CPAP-Adherence Adjunct",
        "stem": "After septoplasty and turbinate reduction, a patient's AHI on a repeat unrelated study is essentially unchanged. Was the surgery a failure?",
        "choices": [
            "Yes, since nasal surgery is expected to normalize the AHI on its own.",
            "Not necessarily -- the relevant outcome measures are CPAP tolerance, required pressure, and nightly usage hours, which the AHI alone does not capture.",
            "Yes, and the patient should be referred directly for tracheostomy.",
            "The result is uninterpretable and no further sleep-related outcome measures should be tracked.",
        ],
        "answer": 1,
        "explanation": "Nasal surgery is an adherence adjunct, not an AHI-normalizing procedure; success should be judged by CPAP tolerance, pressure requirement, and adherence, not AHI alone.",
        "why_wrong": [
            "Conflating nasal surgery with a stand-alone AHI-normalizing treatment is the classic teaching error for this topic.",
            "Correct.",
            "An unchanged AHI after nasal surgery alone is an expected, not catastrophic, finding and does not itself justify escalating straight to tracheostomy.",
            "The correct outcome measures (CPAP pressure, leak, adherence) remain fully interpretable even when AHI on its own is unchanged.",
        ],
        "board_pearl": "Measure success in CPAP usage hours and tolerated pressure, not AHI reduction from the nasal surgery alone.",
        "curveball": "A positive Cottle maneuver identifies nasal valve collapse as a contributing site that may need its own procedure, not just septoplasty/turbinate reduction.",
        "tier": "Concept check",
        "mode": "Manage",
        "concept_id": "v6-sleep-surgery-nasal-surgery-as-a-cpap-adherence-adjunct",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "curveball_answer": (
            "If tolerance still has not improved, re-examine for an undertreated site "
            "(such as valve collapse on Cottle maneuver) before concluding the nasal "
            "airway is optimized."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-rec-sleep-surgery-adult-epiglottic-collapse-epiglottopexy",
        "domain": "Sleep Surgery",
        "topic": "Adult Epiglottic Collapse / Epiglottopexy",
        "choices": [],
        "answer": None,
        "explanation": "This check tests recognition of epiglottic collapse on DISE and its surgical management.",
        "board_pearl": "Do not assume palate or tongue-base collapse explains every surgical or CPAP failure -- DISE-confirmed epiglottic collapse is a distinct, correctable pattern.",
        "curveball": "Epiglottic collapse is the epiglottis component of the VOTE (velum, oropharynx, tongue base, epiglottis) DISE classification.",
        "tier": "Concept check",
        "mode": "Recognize",
        "concept_id": "v6-sleep-surgery-adult-epiglottic-collapse-epiglottopexy",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "prompt": (
            "A patient with OSA has failed CPAP and a prior palate procedure. Drug-induced "
            "sleep endoscopy shows the epiglottis prolapsing posteriorly against the "
            "pharyngeal wall. What does this finding mean, and what surgical options exist?"
        ),
        "answer_text": (
            "This is epiglottic collapse -- a distinct obstruction site identified on DISE "
            "(the epiglottis component of the VOTE classification) that is easy to miss "
            "on awake exam and often overlooked in patients labeled surgery- or "
            "CPAP-refractory. When it is a major contributor and other measures have "
            "failed or are not tolerated, epiglottopexy (suturing the epiglottis "
            "anteriorly to the tongue base/vallecula to prevent posterior prolapse) or "
            "partial epiglottectomy are established surgical options, usually combined "
            "with treatment of any other DISE-identified obstruction sites."
        ),
        "recall_source": "Deep Curriculum",
        "curveball_answer": (
            "DISE is the key diagnostic tool here because epiglottic collapse is a "
            "dynamic, sleep-state-dependent finding not reliably reproduced on awake "
            "flexible laryngoscopy."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-mgt-sleep-surgery-adult-epiglottic-collapse-epiglottopexy",
        "domain": "Sleep Surgery",
        "topic": "Adult Epiglottic Collapse / Epiglottopexy",
        "stem": "A patient's OSA persists after palatal surgery. What is the most appropriate next diagnostic step before assuming the palate operation simply failed?",
        "choices": [
            "Repeat the same palatal procedure with more aggressive tissue resection.",
            "Perform drug-induced sleep endoscopy to look for other or additional obstruction sites, including epiglottic collapse.",
            "Proceed directly to tracheostomy without further evaluation.",
            "Assume the diagnosis of OSA was incorrect and stop all further workup.",
        ],
        "answer": 1,
        "explanation": "Persistent OSA after palatal surgery should prompt DISE to look for additional or alternative obstruction sites, including epiglottic collapse, rather than assuming simple technical failure.",
        "why_wrong": [
            "Repeating the same procedure without re-evaluating the collapse pattern risks operating on the wrong site again.",
            "Correct.",
            "Tracheostomy is a last resort reserved for severe, refractory disease after appropriate site-directed evaluation, not a default next step.",
            "Persistent OSA after treatment does not mean the original diagnosis was wrong; it means the obstruction pattern needs re-evaluation.",
        ],
        "board_pearl": "Do not assume palate or tongue-base collapse explains every surgical or CPAP failure -- DISE-confirmed epiglottic collapse is a distinct, correctable pattern.",
        "curveball": "Epiglottic collapse is the epiglottis component of the VOTE (velum, oropharynx, tongue base, epiglottis) DISE classification.",
        "tier": "Concept check",
        "mode": "Manage",
        "concept_id": "v6-sleep-surgery-adult-epiglottic-collapse-epiglottopexy",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "curveball_answer": (
            "If epiglottic collapse is confirmed and significant, epiglottopexy or "
            "partial epiglottectomy are the established surgical options, generally "
            "paired with treatment of any other identified obstruction sites."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-rec-sleep-surgery-tracheostomy-as-definitive-osa-therapy",
        "domain": "Sleep Surgery",
        "topic": "Tracheostomy as Definitive OSA Therapy",
        "choices": [],
        "answer": None,
        "explanation": "This check tests the modern indication for and mechanism of tracheostomy in severe OSA.",
        "board_pearl": "Tracheostomy bypasses the entire upper airway obstruction below the level of collapse, unlike any site-specific OSA surgery.",
        "curveball": "A fenestrated or capped tube used during the day with nocturnal deflation/opening can preserve daytime speech/swallowing while still resolving nocturnal obstruction.",
        "tier": "Concept check",
        "mode": "Recognize",
        "concept_id": "v6-sleep-surgery-tracheostomy-as-definitive-osa-therapy",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "prompt": (
            "A patient has severe OSA complicated by cor pulmonale and has failed or "
            "cannot tolerate CPAP, BiPAP, and other surgical options. Why is tracheostomy "
            "considered in this scenario, and what makes it mechanistically different from "
            "other OSA surgeries?"
        ),
        "answer_text": (
            "Tracheostomy is considered here because it is reserved for severe OSA with "
            "life-threatening cardiopulmonary complications after failure or intolerance "
            "of PAP therapy and other surgical options. Mechanistically it differs from "
            "every site-specific OSA operation because it bypasses the entire upper "
            "airway obstruction (nasal, palatal, tongue-base, and laryngeal) below the "
            "level of collapse, rather than correcting one anatomic site -- which is why "
            "it was historically the original definitive OSA treatment before CPAP "
            "existed and remains the most reliably effective single intervention "
            "mechanistically."
        ),
        "recall_source": "Deep Curriculum",
        "curveball_answer": (
            "Workup should confirm severity by polysomnography, document failure/"
            "intolerance of PAP and other surgical options, and assess candidacy for "
            "stoma creation and long-term tracheostomy care."
        ),
        "gapfill_v441": True,
    },
    {
        "id": "cc-v112-mgt-sleep-surgery-tracheostomy-as-definitive-osa-therapy",
        "domain": "Sleep Surgery",
        "topic": "Tracheostomy as Definitive OSA Therapy",
        "stem": "A patient undergoing tracheostomy for severe refractory OSA wants to preserve some daytime speech and swallowing function. What strategy addresses this?",
        "choices": [
            "Permanently cap the tube at all times, day and night.",
            "Use a fenestrated or capped tube during the day with nocturnal deflation/opening to resolve obstruction only during sleep.",
            "Remove the tracheostomy entirely once symptoms improve, since OSA does not recur.",
            "Switch to CPAP alone once the tracheostomy is placed, making tube management irrelevant.",
        ],
        "answer": 1,
        "explanation": "A fenestrated or capped tube used during the day with nocturnal deflation/opening is a standard strategy to preserve daytime function while still resolving nocturnal obstruction.",
        "why_wrong": [
            "Permanent capping at all times would defeat the purpose of bypassing obstruction during sleep, when it matters most.",
            "Correct.",
            "OSA is caused by the underlying anatomic obstruction, which does not resolve on its own; removing the tracheostomy would restore the obstruction risk.",
            "The tracheostomy itself is the definitive therapy in this scenario; CPAP is not a substitute once tracheostomy has been chosen for this indication.",
        ],
        "board_pearl": "Tracheostomy bypasses the entire upper airway obstruction below the level of collapse, unlike any site-specific OSA surgery.",
        "curveball": "A fenestrated or capped tube used during the day with nocturnal deflation/opening can preserve daytime speech/swallowing while still resolving nocturnal obstruction.",
        "tier": "Concept check",
        "mode": "Manage",
        "concept_id": "v6-sleep-surgery-tracheostomy-as-definitive-osa-therapy",
        "assessment_class": "recall",
        "graded_discrimination": False,
        "curveball_answer": (
            "This approach is reserved for select severe, refractory, high-risk patients "
            "today given the quality-of-life and stoma-care burden, not used broadly "
            "across the OSA population."
        ),
        "gapfill_v441": True,
    },
]


def apply_missing_topics_gradingscales_v441(data_module, app_module=None):
    result = {"topics_added": 0, "grading_scales_added": 0, "concept_checks_added": 0}

    deep = data_module.DEEP_MODULES_V6
    existing_pairs = {(row.get("primary_domain"), row.get("topic")) for domain_rows in deep.values() for row in domain_rows}
    for entry in NEW_TOPICS_V441:
        key = (entry["primary_domain"], entry["topic"])
        if key in existing_pairs:
            continue
        deep.setdefault(entry["primary_domain"], []).append(dict(entry))
        existing_pairs.add(key)
        result["topics_added"] += 1
    data_module.DEEP_MODULES_V6 = deep
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = deep

    for (domain, topic, field), (marker, addition) in GRADING_SCALE_APPENDS_V441.items():
        for row in deep.get(domain, []):
            if row.get("topic") == topic:
                current = row.get(field, "") or ""
                if marker not in current:
                    row[field] = current + addition
                    result["grading_scales_added"] += 1
                break

    checks = data_module.CONCEPT_CHECKS_V112
    existing_ids = {q.get("id") for q in checks}
    manage_index = 0
    for entry in NEW_CONCEPT_CHECKS_V441:
        if entry["id"] not in existing_ids:
            check = dict(entry)
            if check.get("mode") == "Manage":
                # Rotate choices and their explanations together so the correct
                # position does not become a predictable cue across this batch.
                target = (0, 2, 3, 1, 0, 2, 3)[manage_index]
                manage_index += 1
                shift = (target - check["answer"]) % len(check["choices"])
                check["choices"] = check["choices"][-shift:] + check["choices"][:-shift] if shift else list(check["choices"])
                check["why_wrong"] = check["why_wrong"][-shift:] + check["why_wrong"][:-shift] if shift else list(check["why_wrong"])
                check["answer"] = target
            checks.append(check)
            existing_ids.add(entry["id"])
            result["concept_checks_added"] += 1
    data_module.CONCEPT_CHECK_BY_ID_V112 = {q["id"]: q for q in checks if q.get("id")}
    if app_module is not None:
        app_module.CONCEPT_CHECKS_V112 = checks
        app_module.CONCEPT_CHECK_BY_ID_V112 = data_module.CONCEPT_CHECK_BY_ID_V112

    return result
