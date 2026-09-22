"""v42.1: add 17 sourced, board-relevant Deep Curriculum topics."""

from copy import deepcopy


DOMAIN_SOURCES = {
    "Otology / Neurotology": ("Pasha & Golub, 6e (2022), Ch 7 Otology and Neurotology, pp 333-436.", "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 2, Ch 13-23, pp 234-478."),
    "Rhinology / Allergy / Skull Base": ("Pasha & Golub, 6e (2022), Ch 1 Allergy and Rhinology, pp 1-74.", "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 3, Ch 26-34, pp 479-611."),
    "Head & Neck Oncology": ("Pasha & Golub, 6e (2022), Ch 6 Head and Neck Cancer, pp 249-332.", "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 4, Ch 35-49, pp 612-878."),
    "Thyroid / Parathyroid / Salivary": ("Pasha & Golub, 6e (2022), Ch 3 Endocrinology and Ch 5 Salivary Glands.", "K.J. Lee's Essential Otolaryngology, 12e (2019), thyroid, parathyroid, and salivary chapters."),
    "Pediatric Otolaryngology": ("Pasha & Golub, 6e (2022), Ch 9 Pediatric Otolaryngology, pp 527-628.", "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 6, Ch 51-53, pp 921-1025."),
    "Laryngology / Voice / Swallowing": ("Pasha & Golub, 6e (2022), Ch 2 Laryngology, pp 75-126.", "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 5, Ch 50, pp 879-920."),
    "Facial Plastics / Trauma": ("Pasha & Golub, 6e (2022), Ch 8 Facial Plastic Surgery and Ch 10 Trauma.", "K.J. Lee's Essential Otolaryngology, 12e (2019), Part 7, Ch 54-58, pp 1026-1112."),
    "General ENT / Emergencies": ("Pasha & Golub, 6e (2022), Ch 5 General Otolaryngology and Ch 10 Trauma.", "K.J. Lee's Essential Otolaryngology, 12e (2019), general otolaryngology and emergency sections."),
}


def _card(topic, domain, recognize, localize, workup, manage, operate, teach, tags, claim_source):
    return {
        "topic": topic, "primary_domain": domain, "recognize": recognize,
        "localize": localize, "workup": workup, "manage": manage,
        "operate": operate, "teach": teach, "tags": tags,
        "source_basis": [
            claim_source,
            "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021), relevant domain chapter and index.",
            *DOMAIN_SOURCES[domain],
        ],
        "evidence_calibrated": "v42.1-review-2026",
        "source_metadata_v408": {
            "canonical_domain": domain, "canonical_topic": topic,
            "scope": "verified domain/chapter textbook locator; not a claim-level citation. Time-sensitive or numeric claims require the attached topic-specific guideline/source.",
            "locator_level": "domain-foundational", "reviewed_after": "v42.1",
        },
    }


NEW_TOPICS = [
    _card("Ramsay Hunt Syndrome (Herpes Zoster Oticus)", "Otology / Neurotology",
        "Acute unilateral facial weakness with severe otalgia and vesicles of the pinna, canal, or oropharynx suggests Ramsay Hunt syndrome; hearing loss, tinnitus, or vertigo may coexist, and rash may follow the palsy or be absent.",
        "Varicella-zoster reactivation in the geniculate ganglion inflames the facial nerve in the fallopian canal; adjacent vestibulocochlear involvement explains audiovestibular symptoms.",
        "The diagnosis is clinical. Examine the ear and oropharynx, document House-Brackmann grade and eye closure, and obtain audiometry when hearing symptoms are present; use MRI or electrodiagnostics for atypical, severe, or nonrecovering cases rather than routinely.",
        "Start meticulous corneal protection immediately. Early corticosteroid plus antiviral therapy is commonly recommended despite limited comparative evidence; provide analgesia and short-term vestibular symptom control followed by rehabilitation when needed.",
        "Facial nerve decompression is not routine because evidence is insufficient. Persistent deficits are managed later with exposure protection, rehabilitation, chemodenervation, or facial reanimation according to recovery and denervation duration.",
        "Ramsay Hunt generally has a worse facial recovery prognosis than Bell palsy. Ear pain plus palsy warrants a careful search for vesicles, but their absence does not exclude zoster sine herpete.",
        ["ramsay hunt", "zoster oticus", "facial nerve"], "Cummings 7e — herpes zoster oticus presentation, prognosis, eye care, and medical treatment."),
    _card("Facial Nerve Schwannoma", "Otology / Neurotology",
        "Think of facial nerve schwannoma with slowly progressive, recurrent, or fluctuating ipsilateral facial weakness, a middle-ear or internal-auditory-canal mass, or facial function discordant with tumor size.",
        "The tumor can arise along any facial-nerve segment; smooth fallopian-canal enlargement and multisegment enhancement help distinguish it from other temporal-bone and cerebellopontine-angle lesions.",
        "Contrast MRI maps neural and soft-tissue extent; temporal-bone CT defines fallopian-canal and ossicular involvement. Document serial facial grade, hearing, growth, and electrodiagnostic findings when useful.",
        "Observe small or slowly growing tumors with useful facial function using serial examination, audiometry, and MRI. Stereotactic radiation or surgery is individualized by growth, symptoms, hearing, location, age, and goals.",
        "Options include decompression, nerve-sparing debulking in selected anatomy, radiosurgery, or resection with primary repair, grafting, or nerve transfer. Resection often risks major facial deterioration, so intact function argues against reflexive excision.",
        "Recurrent same-side palsy or failure of presumed Bell palsy to recover warrants imaging. Counsel from the patient's present function, not tumor size alone, and explain the facial-function tradeoff of intervention.",
        ["facial nerve schwannoma", "facial paralysis", "temporal bone"], "Cummings 7e — facial nerve schwannoma diagnosis and function-preserving management."),
    _card("Auditory Neuropathy Spectrum Disorder", "Otology / Neurotology",
        "Suspect ANSD when speech understanding is disproportionately poor or fluctuating relative to behavioral thresholds, especially with prematurity, hyperbilirubinemia, neuropathy, or family history.",
        "Outer-hair-cell function is preserved while inner-hair-cell, synaptic, or auditory-nerve transmission is dys-synchronous; lesion site strongly affects rehabilitation prognosis.",
        "Confirm a present cochlear microphonic and/or otoacoustic emissions with absent or markedly abnormal ABR, recognizing that OAEs may disappear over time. Add behavioral audiology, speech perception, genetics, and MRI of the cochlear nerves.",
        "Provide early language access and individualized hearing-aid or remote-microphone trials with close functional monitoring; thresholds alone do not predict benefit.",
        "Consider cochlear implantation when appropriately fitted amplification fails to support speech and language. Confirm cochlear-nerve integrity because severe deficiency predicts limited CI benefit and may prompt auditory-brainstem-implant evaluation in selected centers.",
        "The signature is preserved cochlear receptor activity with disordered neural synchrony. Base escalation on functional speech-language progress, not a single audiogram.",
        ["auditory neuropathy", "ansd", "abr", "cochlear implant"], "Cummings 7e — ANSD physiology, diagnostic pattern, and rehabilitation."),
    _card("Empty Nose Syndrome", "Rhinology / Allergy / Skull Base",
        "Consider ENS after turbinate surgery when paradoxical obstruction, suffocation sensation, dryness, or crusting occurs despite a visibly open airway; anxiety and sleep disturbance are common comorbid burdens.",
        "Loss of turbinate mucosa and airflow sensation plus altered nasal aerodynamics are proposed contributors; it is a multifactorial neurosensory and airflow disorder rather than fixed stenosis.",
        "Use operative history, endoscopy, ENS6Q, mucosal assessment, and a carefully interpreted cotton test. Exclude inflammatory, structural, neurologic, sleep, and psychiatric contributors; no single test is definitive.",
        "Begin humidification, saline, emollients when appropriate, and coordinated treatment of sleep and mental-health comorbidity while validating symptoms and setting realistic expectations.",
        "Selected patients with consistent symptoms and temporary cotton-test improvement may consider turbinate or lateral-wall augmentation, but evidence and durability are variable and revision requires careful consent.",
        "Prevention favors mucosa-preserving turbinate surgery. A wide cavity does not prove adequate nasal function, and psychological comorbidity should be treated without dismissing the nasal symptoms.",
        ["empty nose syndrome", "turbinate", "paradoxical obstruction"], "Cummings 7e — empty nose syndrome assessment and conservative/augmentative treatment."),
    _card("Silent Sinus Syndrome", "Rhinology / Allergy / Skull Base",
        "Painless progressive unilateral enophthalmos or hypoglobus without trauma or prominent sinus symptoms should raise concern for silent sinus syndrome.",
        "Chronic maxillary outflow obstruction produces negative pressure, maxillary atelectasis, and inferior bowing of the orbital floor, increasing orbital volume.",
        "Sinus/orbital CT shows an opacified, contracted maxillary sinus, retracted uncinate, and depressed orbital floor. Distinguish volume loss from an expansile mucocele, neoplasm, and post-traumatic deformity.",
        "Medical therapy may address concurrent inflammation but does not reverse established atelectasis or orbital-volume change; coordinate rhinology and ophthalmic evaluation.",
        "Endoscopic uncinectomy and maxillary antrostomy restore ventilation. Orbital-floor reconstruction may be simultaneous or staged depending on deformity, diplopia, severity, and expected remodeling after re-aeration.",
        "Unexplained enophthalmos is sometimes a sinus diagnosis. Treat the obstructed, volume-losing sinus and individualize—not automatically mandate—orbital reconstruction.",
        ["silent sinus", "enophthalmos", "maxillary atelectasis"], "Cummings 7e — chronic maxillary atelectasis and orbital management."),
    _card("Endoscopic Pituitary / Anterior Skull Base Approach", "Rhinology / Allergy / Skull Base",
        "Sellar and selected midline skull-base lesions may present with endocrine excess or failure, visual-field loss, cranial neuropathy, headache, or incidental imaging findings; not every lesion requires surgery.",
        "The endonasal corridor crosses the sphenoid to the sella, bounded by carotids and cavernous sinuses laterally, optic apparatus superiorly, and clivus posteriorly; extended approaches reach planum, cribriform, and clival targets.",
        "Obtain dedicated MRI, CT for bony and sphenoid anatomy when operative planning requires it, complete pituitary testing, formal visual assessment when indicated, and multidisciplinary endocrinology-neurosurgery-rhinology review.",
        "Observe appropriate incidental/noncompressive lesions and use disease-specific medical therapy such as dopamine agonists for most prolactinomas; optimize endocrine deficits before surgery.",
        "The rhinologist creates the corridor and reconstruction while neurosurgery treats the lesion. Plan carotid localization and multilayer closure before dural entry; preserve or harvest a vascularized nasoseptal flap when a high-flow leak is plausible.",
        "This is a team operation whose success includes endocrine and visual outcomes, carotid safety, and durable CSF-leak prevention—not merely tumor removal.",
        ["pituitary", "endonasal", "skull base", "nasoseptal flap"], "Cummings 7e — endoscopic endonasal skull-base anatomy and reconstruction."),
    _card("Sentinel Lymph Node Biopsy in Oral Cavity Cancer", "Head & Neck Oncology",
        "SLNB is a staging option for selected early cT1-2 clinically node-negative oral-cavity SCC when performed within a validated multidisciplinary program; it is not used to stage an overtly node-positive neck.",
        "Peritumoral tracer identifies first-echelon lymphatic drainage, allowing intensive pathologic examination of representative nodes while recognizing that floor-of-mouth shine-through can complicate localization.",
        "Confirm primary-site pathology and cN0 status with examination and appropriate imaging. Perform protocol-based lymphoscintigraphy/SPECT-CT and intraoperative probe localization; step-sectioning and immunohistochemistry improve detection of small deposits.",
        "A negative technically adequate SLNB can permit surveillance. Positive findings trigger pathology- and protocol-directed neck treatment and adjuvant decision-making rather than one automatic response for every deposit.",
        "Excise all mapped sentinel nodes while protecting cranial nerves and vessels. Elective neck dissection remains a valid alternative and is preferred when mapping expertise, pathology support, or reliable follow-up is unavailable.",
        "SLNB is staging, not primary-tumor treatment. Its safety depends on selection, mapping quality, pathology processing, and an experienced team.",
        ["sentinel node", "oral cavity cancer", "neck staging"], "ASCO/NCCN-aligned early oral-cavity neck-staging principles; Cummings 7e oncology framework."),
    _card("Subacute (de Quervain) Thyroiditis", "Thyroid / Parathyroid / Salivary",
        "A painful tender thyroid after a viral-like illness, fever, and transient thyrotoxic symptoms suggests subacute granulomatous thyroiditis.",
        "Inflammatory follicular disruption releases stored hormone; this is destructive thyroiditis, not increased hormone synthesis.",
        "Check TSH/free hormones and ESR or CRP. Low radioactive-iodine uptake during thyrotoxicosis distinguishes destructive thyroiditis from Graves disease; ultrasound or biopsy is reserved for atypical or focal findings.",
        "Treat pain with NSAIDs and use corticosteroids for severe or refractory inflammation. Beta blockade treats adrenergic symptoms; antithyroid drugs do not help. Follow for the transient hypothyroid phase and uncommon permanent hypothyroidism.",
        "There is no routine surgical role. Failure to follow the expected course, a persistent focal lesion, abscess concern, or compressive progression should reopen the diagnosis.",
        "Pain, high inflammatory markers, thyrotoxicosis, and low uptake form the classic pattern; anticipate the thyrotoxic-to-hypothyroid-to-recovery sequence.",
        ["de quervain", "subacute thyroiditis", "low uptake"], "Cummings 7e — subacute granulomatous thyroiditis diagnosis and treatment."),
    _card("Hashimoto Thyroiditis", "Thyroid / Parathyroid / Salivary",
        "Hashimoto thyroiditis commonly presents with a painless firm diffuse gland, hypothyroid symptoms, or incidental biochemical/ultrasound abnormalities.",
        "Chronic autoimmune lymphocytic injury progressively destroys follicles and may produce goitrous or atrophic disease.",
        "TSH and free T4 define function; anti-TPO antibodies support the diagnosis. Ultrasound characterizes a gland or true nodule, but diffuse heterogeneity alone is not an FNA indication.",
        "Use levothyroxine for overt hypothyroidism and individualize subclinical disease treatment. Monitor clinically and evaluate new focal or rapid enlargement rather than repeatedly measuring antibodies.",
        "Surgery is reserved for selected compressive goiter or independently suspicious disease. Rapid enlargement warrants urgent lymphoma evaluation, often with core biopsy and flow/cytogenetic studies, because lymphoma is primarily treated nonsurgically.",
        "Do not dismiss a dominant nodule or rapidly growing mass as 'just Hashimoto.' Risk-stratify the focal finding on its own merits.",
        ["hashimoto", "hypothyroidism", "thyroid lymphoma"], "Cummings 7e — chronic lymphocytic thyroiditis and lymphoma association."),
    _card("External Branch of the Superior Laryngeal Nerve Injury", "Thyroid / Parathyroid / Salivary",
        "After thyroid or neck surgery, loss of high pitch, projection, and vocal endurance with preserved gross vocal-fold motion suggests EBSLN injury, especially in a professional voice user.",
        "The EBSLN powers cricothyroid tension and courses variably near the superior thyroid pedicle; injury changes pitch control without classic recurrent-laryngeal-nerve paralysis.",
        "Document pitch range and task-specific symptoms. Stroboscopy may show subtle asymmetry but is not diagnostic; cricothyroid laryngeal EMG is the most specific confirmatory test when the result will change counseling or treatment.",
        "Use observation and voice therapy for compensation, projection, and safe vocal loading; recovery and functional impact vary.",
        "No standard restorative operation exists for isolated injury. Prevention requires capsular upper-pole dissection, individual vessel control, and visual/monitoring-assisted nerve preservation when feasible.",
        "Normal vocal-fold motion does not exclude laryngeal nerve injury. Ask about high notes, projection, fatigue, and occupational voice demands.",
        ["ebsln", "cricothyroid", "thyroidectomy", "pitch"], "Cummings 7e — EBSLN anatomy, diagnosis, prevention, and voice effects."),
    _card("Pierre Robin Sequence", "Pediatric Otolaryngology",
        "Micrognathia, glossoptosis, and upper-airway obstruction—often with a U-shaped cleft palate—define Pierre Robin sequence; severity ranges from feeding difficulty to life-threatening obstruction.",
        "Mandibular hypoplasia displaces the tongue posteriorly and may impede palatal fusion, producing tongue-base rather than primary laryngeal obstruction; isolated and syndromic forms differ in prognosis.",
        "Assess breathing across sleep and feeding, growth, gas exchange/polysomnography when needed, swallowing, and airway level by endoscopy. Evaluate for associated syndromes such as Stickler based on phenotype and genetics.",
        "Use a multidisciplinary pathway: specialist-directed monitored positioning, feeding support, and nasopharyngeal airway or noninvasive support when appropriate. Home sleep plans must follow infant safe-sleep and specialty guidance rather than casual prone-position advice.",
        "Persistent significant obstruction may require mandibular distraction, tongue-lip adhesion, or tracheostomy selected by obstruction level, comorbidity, and institutional expertise; palate repair follows airway and growth stabilization.",
        "Treat airway and nutrition first. Quantify obstruction and identify multilevel/syndromic disease before choosing a tongue, mandible, or tracheostomy solution.",
        ["pierre robin", "micrognathia", "glossoptosis", "pediatric airway"], "Cummings 7e and contemporary pediatric airway pathways — evaluation and tiered PRS management."),
    _card("Nasal Dermoid Cyst", "Pediatric Otolaryngology",
        "A congenital midline nasal dorsal pit, tract, mass, hair, or recurrent sebaceous drainage suggests a nasal dermoid and possible intracranial extension.",
        "Trapped ectoderm along the embryologic prenasal/foramen-cecum pathway can leave a cutaneous tract that variably approaches or crosses the skull base.",
        "Image before biopsy. MRI best evaluates intracranial and dural extension; thin-cut CT adds bony detail when it changes operative planning. Use both selectively for complementary questions and distinguish encephalocele and nasal glial heterotopia.",
        "Treat acute infection before definitive surgery when clinically safe; observation does not eliminate recurrent infection or growth risk.",
        "Excise the complete cyst and tract using an approach matched to extent; suspected intracranial disease requires skull-base/neurosurgical planning. Avoid blind probing or office biopsy.",
        "The board-level safety rule is image before incision: a midline pediatric nasal mass may communicate with the skull base.",
        ["nasal dermoid", "midline nasal mass", "intracranial extension"], "Cummings 7e — congenital midline nasal masses, imaging, and complete excision."),
    _card("Infantile Hemangioma / PHACE Syndrome", "Pediatric Otolaryngology",
        "Infantile hemangiomas appear in early infancy, proliferate, then involute; large segmental face or scalp lesions raise concern for PHACE rather than representing only a cosmetic problem.",
        "These GLUT-1-positive vascular tumors differ from malformations present fully formed at birth. Segmental distribution can accompany posterior-fossa, arterial, cardiac, eye, and ventral developmental anomalies.",
        "Typical focal lesions are clinical diagnoses. For PHACE risk, obtain MRI/MRA of head and neck, echocardiography/aortic-arch assessment, ophthalmologic examination, and multidisciplinary review before treatment decisions.",
        "Observe uncomplicated lesions. Oral propranolol is first-line systemic therapy for high-risk hemangiomas; in PHACE, assess cerebrovascular/cardiac anatomy and use individualized cautious initiation and titration. Topical timolol suits selected thin superficial lesions.",
        "Surgery or laser has selected roles for urgent focal compromise, residual deformity, ulceration, or lesions unsuitable for medication; airway disease requires direct airway assessment and coordinated control.",
        "A large segmental facial hemangioma is a syndrome marker. Propranolol is highly effective, but PHACE arterial disease changes pretreatment evaluation and dosing precautions.",
        ["infantile hemangioma", "phace", "propranolol"], "AAP Clinical Practice Guideline for Management of Infantile Hemangiomas; Cummings 7e vascular-anomaly chapters."),
    _card("Laryngopharyngeal Reflux (LPR)", "Laryngology / Voice / Swallowing",
        "Chronic hoarseness, throat clearing, globus, cough, or irritation may be reflux-associated, but this symptom cluster is nonspecific and commonly overlaps allergy, voice-use, sensory neuropathy, and other laryngeal disorders.",
        "Proximal refluxate exposure may injure pharyngolaryngeal mucosa, but no symptom or laryngoscopic sign uniquely localizes symptoms to reflux.",
        "Perform laryngeal examination and assess competing causes and alarm features. Posterior erythema or edema alone cannot diagnose LPR. For isolated extraesophageal symptoms without typical GERD, favor objective ambulatory reflux testing before prolonged PPI therapy; tailor endoscopy to GI indications.",
        "Use meal timing, weight and trigger modification when relevant. A time-limited PPI trial is reasonable when typical GERD symptoms coexist, but response is not diagnostic; stop escalation and reconsider the phenotype when treatment fails.",
        "Antireflux surgery is reserved for objectively proven reflux with appropriate symptom correlation and foregut evaluation, not unexplained throat symptoms alone.",
        "Avoid turning nonspecific throat symptoms or erythema into a reflex diagnosis. Establish whether reflux is objectively or clinically plausible before committing to long-term acid suppression.",
        ["lpr", "extraesophageal reflux", "hoarseness", "pH impedance"], "ACG GERD guideline and AGA extraesophageal reflux update — testing and treatment limits; Cummings 7e laryngology framework."),
    _card("Blepharoplasty / Eyelid Malposition (Ptosis, Ectropion, Entropion)", "Facial Plastics / Trauma",
        "Separate dermatochalasis from true ptosis, outward lower-lid ectropion, and inward entropion; exposure, tearing, lash-globe contact, field loss, and dry-eye symptoms determine functional urgency.",
        "Skin excess, levator/aponeurotic dysfunction, horizontal laxity, and anterior/posterior lamellar imbalance are different defects requiring different repairs; neurogenic ptosis must not be mistaken for aging.",
        "Measure margin-reflex distance and levator function, test lower-lid distraction/snap-back, examine pupils and motility, assess ocular surface and dry eye, and obtain formal fields when documenting functional upper-lid obstruction.",
        "Lubrication and exposure protection can bridge mild malposition; botulinum toxin has selected temporary uses, but structural disease is corrected anatomically.",
        "Blepharoplasty conservatively removes or repositions tissue; ptosis repair targets levator/Müller mechanisms; lateral tarsal strip treats lax ectropion, and entropion repair corrects retractors and overriding. Prevent overresection, lagophthalmos, ectropion, and retrobulbar hematoma.",
        "'Droopy eyelid' is not one diagnosis. Identify the failing layer and vector, and assess ocular surface and lower-lid support before removing tissue.",
        ["blepharoplasty", "ptosis", "ectropion", "entropion"], "Cummings 7e — eyelid anatomy, assessment, blepharoplasty, and malposition repair."),
    _card("Cervical Necrotizing Fasciitis", "General ENT / Emergencies",
        "Rapidly progressive neck pain or swelling, systemic toxicity, pain out of proportion, skin duskiness, bullae, or crepitus after odontogenic/pharyngeal infection should trigger immediate concern.",
        "Polymicrobial infection spreads along fascial planes, thromboses small vessels, and causes necrosis; danger-space extension can produce descending necrotizing mediastinitis.",
        "This is a clinical diagnosis. Obtain contrast CT through the chest when the patient is stable and it will map extent without delaying source control; gas may be absent. Draw cultures and resuscitation labs while mobilizing the OR.",
        "Secure the threatened airway, resuscitate, start broad aerobic/anaerobic coverage with toxin-suppressing therapy when indicated, and provide ICU support; antibiotics cannot replace debridement.",
        "Perform immediate wide debridement to viable bleeding tissue, drain all involved spaces, and plan serial re-exploration. Thoracic extension requires early thoracic-surgery drainage strategy.",
        "Do not wait for a discrete abscess or reassuring scan. Rapid progression plus toxicity makes delay to operative source control lethal.",
        ["necrotizing fasciitis", "deep neck infection", "mediastinitis"], "Cummings 7e — cervical necrotizing infection, mediastinal spread, and serial debridement."),
    _card("Ear and Nasal Foreign Body Removal", "General ENT / Emergencies",
        "A witnessed insertion, unilateral foul rhinorrhea, canal pain, hearing loss, or a visible object suggests a nasal or aural foreign body. Button batteries and paired high-powered magnets are tissue-destructive emergencies.",
        "Risk depends on site and material: batteries generate alkaline electrical injury, paired magnets compress tissue, organic material swells, and live insects abrade the canal.",
        "Use excellent illumination, otoscopy/rhinoscopy or endoscopy, and assess object, depth, tympanic membrane, trauma, and cooperation. Imaging is selective and must not delay battery removal.",
        "Choose the tool by shape: forceps for graspable objects, hook/curette or balloon behind smooth objects, suction when suitable, and positive pressure for selected nasal cases. Immobilize an aural insect with an appropriate agent only when tympanic-membrane integrity and material safety permit it.",
        "Proceed to controlled microscopic/endoscopic removal with sedation or anesthesia for batteries, deep/impacted objects, poor cooperation, adjacent critical structures, or failed attempts. Avoid irrigation for batteries, swelling organic material, or suspected tympanic perforation, and limit traumatic retries.",
        "The safest first attempt is the best attempt. Remove batteries and dangerous magnets immediately, match technique to object geometry, and re-examine afterward for injury or retained fragments.",
        ["foreign body", "button battery", "ear", "nose"], "Cummings 7e — aural/nasal foreign-body technique, emergencies, and OR indications."),
]


EXPECTED_NEW_DOMAIN_COUNTS = {
    "Otology / Neurotology": 51, "Rhinology / Allergy / Skull Base": 45,
    "Head & Neck Oncology": 42, "Thyroid / Parathyroid / Salivary": 35,
    "Pediatric Otolaryngology": 43, "Laryngology / Voice / Swallowing": 37,
    "Facial Plastics / Trauma": 34, "Sleep Surgery": 21,
    "General ENT / Emergencies": 35,
}


def apply_deep_curriculum_new_topic_gaps_v421(data_module, app_module=None):
    modules = deepcopy(data_module.DEEP_MODULES_V6)
    added, already_present = [], []
    for card in NEW_TOPICS:
        domain = card["primary_domain"]
        if domain not in modules:
            raise RuntimeError(f"v42.1: missing curriculum domain: {domain}")
        if any(x.get("topic") == card["topic"] for x in modules[domain]):
            already_present.append(card["topic"])
        else:
            modules[domain].append(deepcopy(card))
            added.append(card["topic"])
    counts = {domain: len(cards) for domain, cards in modules.items()}
    if counts != EXPECTED_NEW_DOMAIN_COUNTS:
        raise RuntimeError(f"v42.1: unexpected domain counts: {counts}")
    data_module.DEEP_MODULES_V6.clear()
    data_module.DEEP_MODULES_V6.update(modules)
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"topics_added": added, "already_present": already_present}
