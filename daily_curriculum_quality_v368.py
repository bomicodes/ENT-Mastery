"""Daily Curriculum question/label repair and curveball answer completion.

The six mastery levels describe cognitive depth; they must not force every topic
through the same literal wording.  This final-boundary patch classifies each
canonical topic, supplies a natural question progression, gives blinded clinical
cases a presentation label, and guarantees that every Attending Curveball has a
revealable teaching answer.
"""

import re


STAGES = ("recognize", "localize", "workup", "manage", "operate", "teach")

REINKE_ANSWERS = {
    "recognize": (
        "This is Reinke edema: typically bilateral, diffuse polypoid expansion of the "
        "superficial lamina propria in a smoker, producing a progressively low, rough voice."
    ),
    "localize": (
        "Reinke space is the superficial lamina propria beneath the vocal-fold epithelium. "
        "Diffuse fluid and myxoid expansion increases fold mass, lowering pitch and disrupting "
        "mucosal-wave propagation; marked disease can narrow the glottic airway. Reinke edema "
        "is usually broad and bilateral, unlike a focal polyp, while an irregular, stiff, or "
        "unilateral epithelial lesion deserves separate evaluation for dysplasia or malignancy."
    ),
    "workup": (
        "Office laryngoscopy defines whether the swelling is bilateral and diffuse and checks "
        "mobility and airway caliber. Stroboscopy assesses mucosal wave, pliability, and other "
        "phonotraumatic lesions. Irregular leukoplakia, ulceration, a focal unilateral mass, "
        "impaired mobility, or disproportionate stiffness should lower the threshold for biopsy."
    ),
    "manage": (
        "Start with smoking cessation, irritant and reflux control when clinically relevant, "
        "and voice-behavior counseling. Surgery is reasonable for unacceptable voice burden, "
        "significant airway compromise, diagnostic concern, or persistent disease after risk-factor "
        "management; expectations should include that continued smoking increases recurrence risk."
    ),
    "operate": (
        "Reduce excess superficial material while preserving epithelium, the vocal ligament, and "
        "as much viable superficial lamina propria as possible. A limited microflap or equivalent "
        "tissue-preserving technique maintains vibratory cover. Aggressive stripping, deep injury, "
        "or over-resection replaces pliable cover with scar and can permanently worsen voice."
    ),
    "teach": (
        "Reinke edema is a smoking-associated, usually bilateral expansion of the superficial "
        "lamina propria: added mass lowers pitch; laryngoscopy and stroboscopy confirm the diffuse "
        "pliable pattern and screen for suspicious focal disease; risk-factor control comes first; "
        "symptomatic voice or airway burden may justify tissue-preserving reduction. The key error "
        "is treating it by stripping the vocal fold and creating scar."
    ),
}

HNS_PROGRAMMING_ANSWERS = {
    "recognize": (
        "Implantation creates the treatment platform; activation and programming determine whether stimulation is "
        "comfortable, consistently used, and translated into useful tongue motion and airway opening. Initial settings "
        "are a starting point, not proof of efficacy."
    ),
    "localize": (
        "Programming should recruit useful tongue protrusion without painful, weak, strongly lateral, or retrusive motion. "
        "Amplitude and other device parameters, electrode configuration, and respiratory timing can change comfort and "
        "the movement pattern; an off-target pattern should prompt reprogramming before simply increasing intensity."
    ),
    "workup": (
        "Confirm wound healing and a normal postoperative tongue examination, interrogate the device, document usage and "
        "tolerance, and observe tongue motion across tested settings. Symptoms and download data guide early adjustment; "
        "objective sleep testing is used to determine residual disease and refine settings rather than relying on incision healing."
    ),
    "manage": (
        "Activate after appropriate healing, establish a comfortable functional range, and use gradual home acclimation with "
        "scheduled follow-up. Address discomfort, awakenings, poor adherence, or ineffective tongue motion before escalation, "
        "then use formal titration or efficacy testing to optimize residual obstructive events."
    ),
    "operate": (
        "For persistent nonresponse, first verify nightly use, settings, respiratory sensing, and tongue recruitment; then reassess "
        "residual collapse and competing sleep phenotypes. Reprogram before considering revision. Suspect a lead, cuff, generator, "
        "or anatomic problem when interrogation, waveforms, examination, or imaging localize a hardware or surgical failure."
    ),
    "teach": (
        "Teach HNS as a longitudinal pathway: implant, heal, activate, acclimate, measure efficacy, and troubleshoot. Success depends "
        "on comfortable selective recruitment, adherence, correct timing, and treatment of residual multilevel or nonobstructive "
        "sleep disease—not on an intact incision or one acceptable tongue movement in clinic."
    ),
}


def _clean(value):
    return re.sub(r"\s+", " ", str(value or "")).strip()


FOUNDATION_TOPICS = {
    "Temporal Bone Anatomy", "Auditory Neuroanatomy / Cochlear Physiology",
    "Nasal Anatomy for Endoscopy", "Laryngeal Anatomy",
    "Open Rhinoplasty Fundamentals", "Hair Restoration Fundamentals",
    "ENT Imaging Fundamentals", "Wound Healing / Scar Biology in Head & Neck Surgery",
    "Grafts / Implants / Biomaterials in ENT", "Laser / Energy Safety in Otolaryngology",
    "Cleft Lip / Palate — ENT Surgical Fundamentals",
}

TEST_TOPICS = {
    "Audiogram Interpretation", "Tympanometry / Acoustic Reflexes",
    "Vestibular Test Battery", "Audiologic Electrophysiology / ABR-OAE-ECoG",
    "Neurotologic Intraoperative Cranial-Nerve Monitoring",
    "Objective Assessment of Nasal Function", "Allergy Testing & Interpretation",
    "Indeterminate Thyroid Cytology / Molecular Testing", "Stroboscopy Interpretation",
    "FEES", "Modified Barium Swallow", "Adult PSG Interpretation",
    "Pediatric PSG Interpretation", "DISE", "Evidence Interpretation / Outcomes Research",
}

THERAPY_TOPICS = {
    "Hearing Aids and Bone-Conduction Devices", "Vestibular Rehabilitation",
    "Allergen Immunotherapy — SCIT / SLIT", "Adverse Pathology and Adjuvant Therapy",
    "Radiation Therapy Principles for Head & Neck Surgeons",
    "Systemic Therapy Foundations in Head & Neck Cancer", "Scar Management",
    "Facial Synkinesis / Static-Dynamic Rehabilitation", "PAP Troubleshooting",
    "Oral Appliance Therapy", "Hemostasis / Coagulopathy / Antithrombotic Management in ENT",
    "Pain Management in the Head & Neck Patient", "HNS Activation / Programming",
}

PROCEDURE_TOPICS = {
    "Cochlear Implant Surgery", "Endoscopic Maxillary Antrostomy", "Ethmoidectomy",
    "Sphenoidotomy", "Epistaxis Surgical Control", "Revision FESS",
    "Frontal Sinusotomy / Draf Procedures", "Endoscopic CSF Leak Repair / Nasoseptal Flap",
    "Neck Dissection", "Total Laryngectomy", "Open Partial / Conservation Laryngectomy",
    "Transoral Laser Microsurgery for Laryngeal Cancer",
    "Salvage Surgery After Radiation / Chemoradiation", "Central Neck Dissection",
    "Reoperative Thyroid Surgery", "Four-Gland Parathyroid Exploration",
    "Sialendoscopy", "Submandibular Gland Excision", "Reoperative Hyperparathyroidism",
    "Completion Thyroidectomy", "Supraglottoplasty", "Laryngotracheal Reconstruction",
    "Pediatric Tracheostomy / Decannulation", "Microtia Reconstruction",
    "Medialization Thyroplasty", "Microlaryngoscopy", "Injection Laryngoplasty",
    "Arytenoid Adduction / Reinnervation", "Posterior Cordotomy / Arytenoidectomy",
    "Aspiration-Prevention Surgery", "Transnasal Esophagoscopy",
    "Tracheobronchial Endoscopy Principles", "Local Flap Reconstruction",
    "Mohs Defect Reconstruction", "Functional Septorhinoplasty", "Otoplasty",
    "Forehead Flap / Nasal Reconstruction", "Bilobed Flap", "Cervicofacial Flap",
    "Skin Graft Selection", "Periocular Reconstruction", "Auricular Reconstruction",
    "Facial Nerve Reanimation", "Hypoglossal Nerve Stimulation",
    "Palatal Surgery", "Tongue Base Surgery", "Maxillomandibular Advancement",
    "Deep Neck Abscess Drainage",
}

COMPLICATION_TOPICS = {
    "Cochlear Implant Failure / Revision", "Orbital Complications of Sinusitis",
    "Intracranial Complications of Sinusitis", "Free-Flap Monitoring / Compromise / Salvage",
    "Complications of Neck Surgery", "Carotid Blowout Syndrome", "Frey Syndrome",
    "First-Bite Syndrome", "Recurrent Laryngeal Nerve Injury During Thyroidectomy",
    "Post-Tonsillectomy Hemorrhage", "Tracheostomy Emergency",
    "Postoperative Neck Hematoma", "Chyle Leak",
    "Esophageal Perforation / Cervical Mediastinitis", "Septal Hematoma",
}

# These are decision tools, symptom frameworks, or cross-cutting clinical maps.
# Treating them as diseases created diagnosis-reveal cards such as "What is the
# most likely diagnosis?" for antimicrobial stewardship or an airway plan.
FRAMEWORK_TOPICS = {
    "Cochlear Implant Candidacy",
    "Cochlear Implant Failure / Revision",
    "Cortical Neuroplasticity in Hearing Loss",
    "Otologic Manifestations of Systemic Disease",
    "Lateral Skull-Base Tumor Framework",
    "Central Vestibular Disorders",
    "Facial Paralysis",
    "Ototoxic / Noise-Induced Hearing Loss",
    "Hyperacusis / Decreased Sound Tolerance",
    "CRS Phenotyping",
    "Frontal Recess / Frontal Sinus",
    "Olfactory Dysfunction",
    "Systemic Disease of the Nose / Sinuses",
    "Unilateral Sinonasal Disease",
    "Facial Pain / Headache vs Rhinogenic Disease",
    "Benign Sinonasal Tumor Framework",
    "Laryngeal Preservation Decision",
    "Head & Neck Radiation Toxicity / Survivorship",
    "TEP and Alaryngeal Speech",
    "Tumor Immunology / Immunotherapy in HNSCC",
    "Neck Management by Primary Site",
    "Reconstruction Selection After Head & Neck Ablation",
    "Head & Neck Cancer Surveillance / Second Primaries",
    "Palliative / Goals-of-Care Decision-Making in Head & Neck Cancer",
    "Hungry Bone / Post-Thyroid Calcium Management",
    "Radioactive Iodine and TSH Suppression in DTC",
    "Pediatric Hearing Loss Workup",
    "Tympanostomy Tube Indications",
    "Congenital Neck Masses",
    "Congenital Hearing Loss Genetics",
    "Pediatric Aspiration",
    "Pediatric Head & Neck Tumors",
    "Pediatric Vestibular Disorders",
    "Croup vs Epiglottitis",
    "Pediatric Reflux / Eosinophilic Esophagitis",
    "Recurrent Tonsillitis Decision-Making",
    "Pediatric Speech Disorders",
    "Nonobstructive Pediatric Sleep Disorders",
    "Esophageal Disease for the Otolaryngologist",
    "Benign Vocal Fold Lesions",
    "Professional Voice",
    "Dysphagia / Aspiration",
    "Acute / Chronic Laryngopharyngitis",
    "Structured Facial Trauma Examination",
    "Mandibular Biomechanics and Occlusion",
    "Rhinoplasty Tip Mechanics",
    "Rhinoplasty Graft Selection",
    "Aesthetic Facial Analysis",
    "Aging Face / Injectables / Resurfacing",
    "Functional Nasal Obstruction",
    "HNS Troubleshooting / Nonresponse",
    "Down Syndrome Pediatric HNS",
    "Central Events / Hypoventilation",
    "ENT Perioperative Anesthesia / Difficult Airway Planning",
    "Antimicrobial Stewardship in Otolaryngology",
    "Cranial Nerve Examination / Skull Base Localization",
    "Common ENT Consult Triage / Disposition",
    "Petrous Apex Lesions",
    "Congenital Inner-Ear Malformations",
    "Complications of Neck Surgery",
    "AOM / OME / Tympanostomy Decisions",
    "Cleft / Craniofacial Otologic-Airway Care",
    "Ankyloglossia / Maxillary Frenulum",
    "Le Fort / Panfacial Trauma",
    "Facial Soft-Tissue Lacerations / Burns",
    "ENT Fluids / Electrolytes / Nutrition",
    "Epistaxis",
    "Systemic / Granulomatous Disease Manifestations in ENT",
    "Immunocompromised Host in Otolaryngology",
    "Oral Manifestations of Systemic Disease",
    "Geriatric Otolaryngology / Frailty",
}

# Exact exceptions for topics whose names contain oncology terms although the
# learning task is a benign or functional condition, not cancer staging.
CONDITION_TOPICS = {
    "Pleomorphic Adenoma / Warthin Tumor",
    "Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy",
}

ONCOLOGY_TOPICS = {
    "Unknown Primary with Cervical Metastasis",
}


# Keyword-only labels can be diverted by incidental prose (for example,
# "recurrent swallowing" in hemorrhage or "scar" in posterior glottic stenosis).
# These exact, diagnosis-neutral labels describe what the learner actually sees.
TOPIC_CASE_LABELS = {
    "Vestibular Neuritis": "Acute vestibular syndrome",
    "Post-Tonsillectomy Hemorrhage": "Postoperative oral bleeding",
    "Posterior Glottic Stenosis / Arytenoid Fixation": "Bilateral vocal-fold immobility",
    "Tracheomalacia / Bronchomalacia": "Dynamic pediatric airway symptoms",
    "Carotid Blowout Syndrome": "Sentinel or major neck bleeding",
    "Septal Hematoma": "Post-traumatic nasal obstruction",
}


def _topic_kind(topic, module):
    """Classify the named concept, never incidental words in its teaching prose.

    The former classifier searched the whole module.  Thus a condition mentioning
    a steroid became a therapy and a routine infection mentioning erosion became
    an emergency complication.  Exact concept overrides keep prompt grammar tied
    to what the learner is studying; only unambiguous tumor words use a fallback.
    """
    if topic in FOUNDATION_TOPICS:
        return "foundation"
    if topic in TEST_TOPICS:
        return "test"
    if topic in THERAPY_TOPICS:
        return "therapy"
    if topic in PROCEDURE_TOPICS:
        return "procedure"
    if topic in FRAMEWORK_TOPICS:
        return "framework"
    if topic in COMPLICATION_TOPICS:
        return "complication"
    if topic in CONDITION_TOPICS:
        return "condition"
    if topic in ONCOLOGY_TOPICS:
        return "oncology"
    text = topic.lower()
    if any(x in text for x in (
        "carcinoma", " cancer", "malign", "melanoma", "lymphoma", "sarcoma",
        "tumor", "neoplasm", "metastatic", "hnscc", " scc",
    )):
        return "oncology"
    return "condition"


def _case_label(topic, module, domain):
    """Return a useful, diagnosis-neutral label for blinded recognition cards."""
    if topic in TOPIC_CASE_LABELS:
        return TOPIC_CASE_LABELS[topic]
    text = " ".join([topic] + [_clean(module.get(k)) for k in ("recognize", "localize", "workup")]).lower()
    patterns = (
        (("stridor", "airway obstruction", "respiratory distress"), "Airway symptoms"),
        (("dysphonia", "hoarse", "voice", "vocal fold"), "Voice change"),
        (("dysphagia", "aspiration", "swallow"), "Swallowing symptoms"),
        (("otalgia", "otorrhea", "ear canal", "tympanic"), "Ear symptoms"),
        (("hearing loss", "hearing", "audiogram"), "Hearing complaint"),
        (("vertigo", "nystagmus", "dizziness", "imbalance"), "Dizziness / imbalance"),
        (("epistaxis", "nasal bleeding"), "Nasal bleeding"),
        (("rhinorrhea", "nasal drainage", "csf"), "Nasal drainage"),
        (("nasal obstruction", "sinonasal", "sinus"), "Sinonasal symptoms"),
        (("facial paralysis", "facial weakness"), "Facial weakness"),
        (("vision", "diplopia", "orbit", "proptosis"), "Orbital / visual symptoms"),
        (("neck mass", "cervical mass", "adenopathy"), "Neck mass"),
        (("thyroid", "goiter"), "Thyroid presentation"),
        (("salivary", "parotid", "submandibular"), "Salivary presentation"),
        (("snoring", "sleep apnea", "sleep-disordered"), "Sleep-breathing symptoms"),
        (("trauma", "fracture", "laceration"), "Trauma presentation"),
        (("scar", "aging face", "rhytid", "cosmetic"), "Facial appearance / scar concern"),
        (("foreign body", "ingestion"), "Foreign-body presentation"),
        (("infection", "abscess", "fever", "septic"), "Infectious presentation"),
        (("sound tolerance", "hyperacusis", "tinnitus"), "Sound-perception symptoms"),
        (("pediatric", "child", "infant", "neonate"), "Pediatric presentation"),
    )
    for needles, label in patterns:
        if any(n in text for n in needles):
            return label
    domain_labels = {
        "Otology / Neurotology / Audiology": "Ear / vestibular presentation",
        "Otology / Neurotology": "Ear / vestibular presentation",
        "Rhinology / Allergy / Skull Base": "Nasal / skull-base presentation",
        "Head & Neck Oncology": "Head and neck presentation",
        "Thyroid / Parathyroid / Salivary": "Endocrine / salivary presentation",
        "Pediatric Otolaryngology": "Pediatric ENT presentation",
        "Laryngology / Voice / Swallowing": "Voice / airway presentation",
        "Facial Plastics / Trauma / Reconstruction": "Facial / reconstructive presentation",
        "Facial Plastics / Trauma": "Facial / reconstructive presentation",
        "Sleep Medicine / Surgery": "Sleep-breathing presentation",
        "Sleep Surgery": "Sleep-breathing presentation",
        "General ENT / Perioperative / Emergencies": "Acute ENT presentation",
        "General ENT / Emergencies": "Acute ENT presentation",
    }
    return domain_labels.get(domain, "Clinical presentation")


def _blind_recognition_prompt(topic, module):
    """Turn the module's recognition layer into a diagnosis-blinded question."""
    stem = _clean(module.get("recognize"))
    if not stem:
        return (
            "A patient has a presentation consistent with an ENT disorder in this domain. "
            "What diagnosis best fits, and which finding would you use to confirm it?"
        )
    variants = {topic, topic.replace("&", "and")}
    variants.update(
        part.strip(" -") for part in re.split(r"\s*(?:/|—|\(|\)|\bof the\b|\bof\b)\s*", topic, flags=re.IGNORECASE)
        if len(part.strip(" -")) >= 6
    )
    leading = re.split(r"\s+(?:of|with|and|/)\s+", topic, maxsplit=1, flags=re.IGNORECASE)[0]
    acronyms = {
        "".join(word[0] for word in re.findall(r"[A-Za-z]+", value)
                if word.lower() not in {"and", "or", "of", "the", "with"})
        for value in variants | {leading}
    }
    for variant in sorted(variants, key=len, reverse=True):
        if variant:
            # Whole-term replacement prevents Labyrinthitis from corrupting
            # "labyrinthine" and similarly embedded anatomic words.
            stem = re.sub(
                r"(?<!\w)" + re.escape(variant) + r"(?!\w)",
                "the target diagnosis", stem, flags=re.IGNORECASE,
            )
    for acronym in sorted(acronyms, key=len, reverse=True):
        if len(acronym) >= 2:
            stem = re.sub(r"\b" + re.escape(acronym) + r"\b", "the condition", stem, flags=re.IGNORECASE)
    stem = re.sub(
        r"\b(?:foundation|advanced|senior|source-grounded)\s+refinement\s*[—:–-]+\s*",
        "", stem, flags=re.IGNORECASE,
    )
    stem = re.sub(r"\b[A-Z][A-Z /-]{2,}\s+REFINEMENT\s*[—:–-]+\s*", "", stem)
    stem = re.sub(
        r"^(recognize|suspect|consider)\s+(?:diffuse\s+)?(?:the target diagnosis|the condition)\s*(?:\([^)]*\))?\s*(?:as|by|when|if)\s+",
        "", stem, flags=re.IGNORECASE,
    )
    stem = re.sub(
        r"^(?:the target diagnosis|the condition)\s+(is|classically|typically|presents?\s+with)\s+",
        "", stem, flags=re.IGNORECASE,
    )
    stem = re.sub(r"^use this card for\s+(?:the target diagnosis|the condition)\.\s*", "", stem, flags=re.IGNORECASE)
    stem = re.sub(r"^acquired\s+(?:the target diagnosis|the condition)\s+is\s+", "", stem, flags=re.IGNORECASE)
    stem = re.sub(
        r"^recognize\s+.{0,140}?\s+(?:as|from)\s+", "", stem,
        flags=re.IGNORECASE,
    )
    stem = re.sub(r"\b(?:suggests?|supports?|represents?)\s+the target diagnosis\b", "is the characteristic pattern", stem, flags=re.IGNORECASE)
    stem = re.sub(r"\b(?:should\s+)?raise concern for the target diagnosis\b", "is concerning", stem, flags=re.IGNORECASE)
    stem = stem.replace("the target diagnosis", "this disorder")
    stem = re.sub(r"\bprimary acquired this disorder\b", "a primary acquired form", stem, flags=re.IGNORECASE)
    stem = re.sub(r"\ba simple this disorder\b", "a simple form", stem, flags=re.IGNORECASE)
    stem = re.sub(r"\bthis disorder\s*\((?:the condition|this disorder)\)", "this disorder", stem, flags=re.IGNORECASE)
    stem = re.sub(r"^the\s+TIME COURSE,\s+not from\s+", "Use the time course, not ", stem)
    stem = _excerpt(stem, 420).rstrip()
    if stem:
        stem = stem[0].upper() + stem[1:]
    if stem.endswith("?"):
        return stem
    return stem.rstrip(".") + ". What is the most likely diagnosis?"


def _usable_blind_prompt(prompt):
    """Reject synthetic case stems that read like edited curriculum prose."""
    low = prompt.lower()
    artifacts = (
        "this disorder", "the condition", "the target diagnosis", "use this card",
        "foundation —", "foundation:", "application —", "refinement —",
        "senior —", "boards —", "chief —", "can is ", "a this ",
        "recognize sialadenitis the", "umbrella the",
    )
    stem = prompt.rsplit("What is the most likely diagnosis?", 1)[0].strip()
    return len(stem) >= 70 and not any(token in low for token in artifacts)


def _named_recognition_prompt(topic):
    return (
        f"For {topic}, what presentation or pattern should a resident recognize, "
        "and which feature best distinguishes it from the closest mimic?"
    )


def _prompt(topic, stage, kind, module, original_prompt="", blind_recognition=True):
    """Build a coherent six-step progression without category-literal stems."""
    if topic == "HNS Activation / Programming":
        return {
            "recognize": "After HNS implantation, what does activation and programming accomplish, and why is the first setting not a final efficacy test?",
            "localize": "During HNS programming, how do tongue-motion pattern, comfort, stimulation settings, and respiratory timing reveal useful versus off-target recruitment?",
            "workup": "Before activation and during optimization, what healing, tongue examination, usage, device, symptom, and sleep-study data should be reviewed?",
            "manage": "How should HNS activation progress from a comfortable starting range through home acclimation and formal efficacy testing, and what problems require earlier adjustment?",
            "operate": "If HNS remains uncomfortable or ineffective despite use, how do you separate a programming problem, residual anatomic collapse, another sleep phenotype, and hardware failure before considering revision?",
            "teach": "How would you teach HNS activation and programming as a longitudinal pathway from healing through objective efficacy assessment and troubleshooting?",
        }[stage]
    if topic == "Reinke Edema":
        return {
            "recognize": (
                "A patient with a long smoking history develops gradually progressive "
                "deepening and roughness of the voice. Laryngoscopy shows bilateral, "
                "diffuse, floppy swelling of the membranous vocal folds. What is the "
                "most likely diagnosis?"
            ),
            "localize": (
                "In Reinke edema, which layer of the vocal fold is expanded, how does "
                "that change vibration and pitch, and what appearance distinguishes it "
                "from a focal polyp or a suspicious unilateral mass?"
            ),
            "workup": (
                "After recognizing Reinke edema, what should office laryngoscopy and "
                "stroboscopy establish before treatment, and which findings should "
                "prompt biopsy rather than routine edema reduction?"
            ),
            "manage": (
                "How do smoking and irritant control, voice care, symptom burden, and "
                "airway compromise determine conservative treatment versus surgery for "
                "Reinke edema?"
            ),
            "operate": (
                "During microlaryngeal reduction of Reinke edema, what tissue must be "
                "preserved, and why can aggressive epithelial stripping or over-resection "
                "produce a worse voice?"
            ),
            "teach": (
                "How would you teach a junior the complete Reinke edema pathway—from the typical "
                "presentation and involved layer through counseling and tissue-preserving "
                "surgery—and name the operative mistake most likely to cause scarring."
            ),
        }[stage]

    if stage == "recognize" and kind in {"condition", "oncology", "complication"}:
        if blind_recognition:
            return _blind_recognition_prompt(topic, module)
        return _named_recognition_prompt(topic)

    prompts = {
        "condition": {
            "recognize": f"What clinical pattern should make you suspect {topic}, and which finding makes that diagnosis more likely than its closest mimic?",
            "localize": f"For {topic}, what anatomic site or pathophysiologic process produces the characteristic findings, and how does that mechanism help distinguish the main mimics?",
            "workup": f"A patient is suspected of having {topic}. What focused examination or testing confirms the diagnosis, and which result would change the next step?",
            "manage": f"Once {topic} is established, what is the treatment sequence, and what symptom, examination finding, or failure of initial therapy should trigger escalation?",
            "operate": f"For {topic}, when is a procedure appropriate, what anatomy or technical principle determines success, and what is the rescue plan if the first approach fails?",
            "teach": f"How would you teach {topic} as one connected pathway from presentation and mechanism through confirmation, treatment, and escalation?",
        },
        "foundation": {
            "recognize": f"How would you build a practical map of {topic}: which structures or mechanisms belong on it, and what clinical problem does each help explain?",
            "localize": f"How would you use {topic} to trace the key spatial or physiologic relationships and explain the consequence of injuring, obstructing, or disrupting each one?",
            "workup": f"How is {topic} identified on examination, endoscopy, imaging, or testing, and which normal variant is most likely to be misread?",
            "manage": f"How would you apply {topic} to a real clinical decision, and how does the anatomy or physiology change counseling, treatment selection, or urgency?",
            "operate": f"How would you apply {topic} in the operating room to identify the landmarks, danger structures, safe sequence, and bailout route before the key step?",
            "teach": f"How would you teach {topic} from first principles and use one clinical or operative example to show why the relationships matter?",
        },
        "test": {
            "recognize": f"When is {topic} the right tool, what question does it answer, and what can it not establish by itself?",
            "localize": f"Which components of {topic} identify the site or mechanism of disease, and which finding is commonly overinterpreted?",
            "workup": f"How should {topic} be interpreted in sequence: what must be checked first for validity, what are the decisive findings, and what corroboration is needed before acting?",
            "manage": f"How would different results from {topic} lead to observation, further testing, or treatment rather than the same plan for every patient?",
            "operate": f"What is the highest-stakes technical or interpretive failure in {topic}, how do you recognize it, and what should you do before committing to an irreversible treatment?",
            "teach": f"How would you teach a junior to perform or read {topic} using a sequence, validity check, interpretation, limitation, and management consequence?",
        },
        "procedure": {
            "recognize": f"What problem is {topic} designed to solve, and what patient or anatomic feature makes it preferable to the main alternatives?",
            "localize": f"Before {topic}, map the target, exposure, critical landmarks, and danger structures. Which relationship most often changes the approach?",
            "workup": f"What preoperative history, examination, imaging, or functional testing is required before offering {topic}, and which result would make you defer or choose another plan?",
            "manage": f"Where does {topic} fit in the treatment pathway, and what conservative, endoscopic, open, or nonsurgical alternatives should be discussed first?",
            "operate": f"How would you perform {topic} as the primary surgeon, including setup, exposure, decisive steps, complication avoidance, bailout, and postoperative plan?",
            "teach": f"How would you teach {topic} around indication, anatomy, the commitment point, rescue, and early complication recognition rather than a memorized step list?",
        },
        "oncology": {
            "recognize": f"Which presentation should raise concern for {topic}, and what competing benign or malignant diagnosis must be separated before treatment?",
            "localize": f"For {topic}, how would you map local extent and regional or distant spread, and which involved structures change urgency, stage, or treatment modality?",
            "workup": f"How would you build the diagnostic and staging workup for {topic}: what tissue is needed, what should imaging define, and which result changes treatment?",
            "manage": f"How would you construct a stage- and patient-specific plan for {topic}, including the appropriate roles of surgery, radiation, systemic therapy, surveillance, or palliation?",
            "operate": f"At tumor board, what advanced treatment decision matters most for {topic}, when does surgery have a role, and which anatomy or functional tradeoff changes that decision?",
            "teach": f"How would you teach {topic} from diagnosis through surveillance, including histology, stage, treatment sequence, regional management, and functional consequences?",
        },
        "complication": {
            "recognize": f"What early pattern identifies {topic}, which apparently reassuring finding can mislead you, and what dangerous progression must be anticipated?",
            "localize": f"What structure or failure mechanism is responsible for {topic}, and how does the likely site determine the immediate risk?",
            "workup": f"For suspected {topic}, what must be assessed at the bedside first, what testing can safely follow, and what finding means you should stop testing and intervene?",
            "manage": f"What is the time-critical response to {topic}, including stabilization, source control or definitive treatment, consultation, and the threshold for escalation?",
            "operate": f"If {topic} requires operative rescue, describe exposure, control of the problem, protection of threatened structures, bailout options, and postoperative surveillance.",
            "teach": f"How would you teach {topic} as a rescue algorithm from recognition and immediate action through definitive control and early escalation?",
        },
        "therapy": {
            "recognize": f"What clinical indication makes {topic} appropriate, and what superficially similar problem will not benefit from it?",
            "localize": f"What target or mechanism does {topic} act on, and how does that explain both its expected benefit and its important adverse effects?",
            "workup": f"Before starting {topic}, what confirms candidacy, what baseline risks must be checked, and how will response or toxicity be measured?",
            "manage": f"How is {topic} initiated, monitored, adjusted, and stopped, and what finding should prompt a different treatment strategy?",
            "operate": f"When {topic} fails or causes a complication, what procedural or multidisciplinary alternative becomes appropriate, and what should not be delayed?",
            "teach": f"How would you teach {topic} through indication, mechanism, selection, monitoring, failure, and the counseling point patients most need to understand?",
        },
        "framework": {
            "recognize": f"For {topic}, what is the first clinically useful distinction, and how does it change the differential, urgency, or next step?",
            "localize": f"When evaluating {topic}, which anatomic, physiologic, or decision categories matter, and how does the plan change across them?",
            "workup": f"How would you apply {topic} to a patient: which history, examination, or data establish the relevant category, and which finding redirects the plan?",
            "manage": f"Using {topic}, how do you choose and sequence the available options, and what should trigger escalation or multidisciplinary input?",
            "operate": f"What procedural decision can arise in {topic}, which anatomy or commitment point governs it, and what bailout or safety stop must be planned?",
            "teach": f"How would you teach {topic} as a practical algorithm with a first distinction, decisive data, next step, and safety stop?",
        },
    }
    return prompts[kind][stage]


def _module_index(data_module):
    result = {}
    for domain, modules in data_module.DEEP_MODULES_V6.items():
        for module in modules:
            cid = data_module._v6_item_id(domain, module.get("topic"))
            result[cid] = module
    return result


def apply_daily_items_v368(items, data_module):
    modules = _module_index(data_module)
    stats = {"items": 0, "blinded_cases": 0, "labeled_cases": 0, "kinds": {}}
    for item in items:
        module = modules.get(item.get("concept_id")) or {}
        topic = _clean(item.get("topic"))
        stage = item.get("stage")
        if stage not in STAGES:
            continue
        kind = _topic_kind(topic, module)
        original_prompt = item.get("prompt") or ""
        blind_prompt = ""
        blind_recognition = False
        if stage == "recognize" and kind in {"condition", "oncology", "complication"}:
            blind_prompt = _blind_recognition_prompt(topic, module)
            blind_recognition = _usable_blind_prompt(blind_prompt)
        item["daily_topic_kind"] = kind
        item["daily_prompt"] = _prompt(
            topic, stage, kind, module, original_prompt, blind_recognition
        ).rstrip()
        if not item["daily_prompt"].endswith("?"):
            item["daily_prompt"] = item["daily_prompt"].rstrip(".") + "?"
        # The legacy template has a small number of prompt-text fallbacks. Keep
        # the canonical prompt itself synchronized so none of those branches can
        # resurrect category-driven wording.
        item["prompt"] = item["daily_prompt"]
        if topic == "Reinke Edema":
            item["answer"] = REINKE_ANSWERS[stage]
        if topic == "HNS Activation / Programming":
            item["answer"] = HNS_PROGRAMMING_ANSWERS[stage]
        if stage == "recognize":
            # Only diagnostic recognition is an unidentified case.  A test,
            # procedure, therapy, or anatomy framework should name the subject.
            if kind in {"condition", "oncology", "complication"} and blind_recognition:
                item["blind_reveal"] = True
                item["blind_case_label"] = _case_label(topic, module, item.get("domain"))
                stats["blinded_cases"] += 1
                if item["blind_case_label"]:
                    stats["labeled_cases"] += 1
            else:
                item["blind_reveal"] = False
                item.pop("blind_case_label", None)
        stats["items"] += 1
        stats["kinds"][kind] = stats["kinds"].get(kind, 0) + 1
    return stats


def _excerpt(text, limit=900):
    text = _clean(text)
    if len(text) <= limit:
        return text
    window = text[:limit]
    cut = ""
    # Prefer the last true sentence boundary within the limit.
    parts = window.rsplit(". ", 1)
    if len(parts) == 2 and parts[0]:
        cut = parts[0].rstrip(" .")
    if not cut:
        # No sentence boundary: many long recognize fields are one compound
        # sentence joined by " -- " or "; ". Cutting there keeps a complete
        # clause instead of stopping mid-thought partway into the next one.
        for joiner in (" -- ", "; ", ", "):
            clause_parts = window.rsplit(joiner, 1)
            if len(clause_parts) == 2 and len(clause_parts[0]) >= 120:
                cut = clause_parts[0].rstrip(" .,;:-")
                break
    if not cut:
        # Last resort: the nearest whitespace boundary, so the excerpt never
        # ends mid-word even when no clause boundary is available either.
        cut = window.rsplit(None, 1)[0].rstrip(" .,;:-")
    return (cut or window).rstrip() + "."


def _curveball_lead(question):
    q = question.lower()
    if any(x in q for x in ("stridor", "stridulous", "airway", "cannot lie flat")):
        return (
            "Treat this as a threatened airway, not as a biopsy-scheduling problem. "
            "Call anesthesia and the operating team, keep the patient upright with continuous "
            "monitoring and oxygen as needed, avoid sedation or an induction that could convert "
            "partial obstruction to complete obstruction, and secure the airway in a controlled "
            "setting with spontaneous ventilation and a surgical-airway backup when feasible. "
            "Diagnostic tissue comes after oxygenation and a safe airway."
        )
    if any(x in q for x in ("bleed", "hemorrhage", "hypotens", "transfusion")):
        return (
            "Resuscitation and definitive hemorrhage control now outrank the ideal elective sequence: "
            "protect the airway, obtain large-bore access and blood products, reverse correctable "
            "coagulopathy, identify the likely source, and involve the OR/interventional team early."
        )
    if any(x in q for x in ("vision", "afferent pupillary", "orbit", "proptosis")):
        return (
            "A new objective visual deficit is an organ-threatening escalation. Recheck acuity, pupils, "
            "color vision, motility and pressure as appropriate, obtain urgent specialty support, and "
            "move to decompression or source control when the clinical diagnosis is clear rather than "
            "delaying for a perfectly completed elective workup."
        )
    if any(x in q for x in ("facial weakness", "facial paralysis", "loses signal", "nerve")):
        return (
            "First determine whether this is progressive neural injury, compression, infection, or a "
            "technical monitoring problem; document function, remove reversible causes, and escalate "
            "imaging or exploration when the trajectory or operative findings suggest ongoing injury."
        )
    return ""


def _best_curveball_support(question, module, challenge):
    stop = {
        "what", "which", "when", "where", "would", "should", "could", "this",
        "that", "with", "from", "into", "your", "does", "have", "been", "than",
        "before", "after", "patient", "change", "become", "becomes", "instead",
    }
    qwords = {
        word for word in re.findall(r"[a-z0-9]+", question.lower())
        if len(word) >= 4 and word not in stop
    }
    candidates = []
    for field in STAGES:
        value = _clean(module.get(field))
        if value:
            candidates.append((field, value))
    for field in ("explanation", "board_pearl"):
        value = _clean(challenge.get(field))
        if value:
            candidates.append((field, value))
    if not candidates:
        return ""

    q = question.lower()
    priors = set()
    if any(x in q for x in ("diagnosis", "differential", "red flag", "finding", "alternative")):
        priors.update(("recognize", "localize", "workup"))
    if any(x in q for x in ("test", "imaging", "evaluate", "workup", "laboratory", "biopsy")):
        priors.add("workup")
    if any(x in q for x in ("manage", "treat", "therapy", "counsel", "follow", "surveillance")):
        priors.add("manage")
    if any(x in q for x in ("surgery", "operative", "approach", "resection", "drain", "fixation", "reconstruct")):
        priors.add("operate")
    if q.startswith("why"):
        priors.update(("localize", "teach"))

    scored = []
    for order, (field, value) in enumerate(candidates):
        words = set(re.findall(r"[a-z0-9]+", value.lower()))
        overlap = sum(3 if len(word) >= 7 else 2 for word in qwords & words)
        prior = 4 if field in priors else 0
        # Prefer the canonical concept layer over the primary vignette explanation
        # when lexical relevance is otherwise tied.
        canonical = 1 if field in STAGES else 0
        scored.append((overlap + prior + canonical, -order, value))
    scored.sort(reverse=True)
    return _excerpt(scored[0][2])


CURVEBALL_OVERRIDES = {
    "v252_lar_mtd_snr": (
        "Laryngeal EMG is useful when subtle vagal or recurrent-laryngeal neuropathy remains plausible despite an "
        "equivocal motion or stroboscopic examination, particularly when prognosis would change observation, temporary "
        "augmentation, or definitive framework surgery. Interpret recruitment and spontaneous activity in the context "
        "of timing; a normal or technically limited study does not exclude every mild neuropathy."
    ),
    "v220_hn_fom_fnd": (
        "Loss of a clean plane or fixation to the mandible, lower-lip/chin sensory change, and imaging evidence of "
        "cortical or medullary invasion raise concern for mandibular involvement. Deep submucosal induration, impaired "
        "tongue mobility, or extension toward the extrinsic tongue musculature suggests a deeper floor-of-mouth process."
    ),
    "v262_fpt_otoplasty_fnd": (
        "Isolated antihelical underfolding can be corrected by creating or reinforcing the fold, commonly with Mustarde-"
        "type sutures. Conchal hypertrophy or excessive conchomastoid angle requires a separate conchal strategy—often "
        "Furnas-type setback sutures and, selectively, cartilage reduction—so fold sutures are not overtightened to hide it."
    ),
    "v254_lar_polycyst_fnd": (
        "A deeper intracordal cyst is tethered within the vibratory cover and typically produces focal marked reduction "
        "or absence of mucosal wave. A superficial polyp more often remains pliable, with wave visible around or over it, "
        "although hemorrhage or fibrosis can also stiffen a polyp."
    ),
    "v254_lar_polycyst_snr": (
        "Persistent stiffness without recurrent focal mass suggests scar, sulcus, or residual lamina-propria injury rather "
        "than simple lesion recurrence. Allow healing, repeat stroboscopy, optimize voice therapy, and address scar-related "
        "vibratory failure cautiously; a true recurrent mass instead requires lesion-specific reassessment before re-excision."
    ),
    "v11_fprs_05": (
        "Treat the modified Cottle as a localization clue, not proof of a single lesion. Inspect static internal-valve "
        "narrowing and dynamic lateral-wall collapse independently, decongest the turbinates, assess septal contribution, "
        "and use endoscopy to identify posterior obstruction so the plan addresses each demonstrated bottleneck."
    ),
    "v254_lar_nodule_fnd": (
        "Soft, early nodules are more edematous and often regress with reduced collision dose and effective voice therapy. "
        "Mature fibrotic nodules are stiffer and less reversible, but therapy remains first-line; surgery is reserved for "
        "carefully selected persistent functional limitation after behavior and diagnosis are optimized."
    ),
    "v254_lar_nodule_app": (
        "Reduce collision dose with scheduled voice breaks, amplification, quieter-room or microphone access, limits on "
        "shouting and prolonged speaking, and temporary workload modification. Pair accommodations with hydration, recovery "
        "time, and task-specific voice therapy rather than prescribing impractical total silence."
    ),
    "v143_rhi_03": (
        "The nasolacrimal duct descends anterior to the natural maxillary ostium in the lacrimal/maxillary bone. Anterior "
        "enlargement should remain under direct landmark control; blind or overly aggressive anterior dissection risks duct "
        "injury, whereas posterior and inferior enlargement usually provides safer access when clinically appropriate."
    ),
    "v207_rhi_frontal_snr": (
        "Maintain a usable frontal corridor with saline irrigation, topical anti-inflammatory therapy, and targeted "
        "debridement of obstructive crust, clot, or early scar without repeatedly traumatizing healthy mucosa. Treat ongoing "
        "inflammation and synechiae early; persistent narrowing warrants endoscopic reassessment rather than blind instrumentation."
    ),
    "v137_tps_05": (
        "Suspected multigland disease lowers the reliability of a focused single-gland operation. Plan systematic bilateral "
        "identification and assessment of all glands, use intraoperative PTH as an adjunct rather than a substitute for anatomy, "
        "and anticipate ectopic or supernumerary glands if the biochemical response is inadequate."
    ),
    "v220_hn_tonsil_snr": (
        "Positive microscopic margin and pathologic extranodal extension are both major postoperative high-risk findings and "
        "commonly support concurrent chemoradiation when the patient can tolerate it. Other adverse features can support radiation, "
        "but they do not automatically carry the same chemotherapy implication as margin positivity or ENE."
    ),
    "v243_ped_sgh_snr": (
        "Escalate beyond propranolol when airway compromise is immediately unstable, the drug is contraindicated or not tolerated, "
        "or an adequate course fails to control a focal obstructing lesion. Endoscopic debulking can provide selected rapid relief; "
        "tracheostomy is a rescue or bridge for otherwise unmanageable obstruction rather than routine first-line treatment."
    ),
    "v267_sleep_ds_snr": (
        "HNS treats obstructive collapse, not central apnea or primary gas-exchange failure. New central events, hypoventilation, "
        "or important pulmonary disease should trigger repeat phenotype assessment, CO2/oxygen evaluation, and medical or "
        "ventilatory management before proceeding with or intensifying upper-airway stimulation."
    ),
    "v235_tps_indet_fnd": (
        "Predictive values are prevalence-dependent. With the same sensitivity and specificity, a higher pretest malignancy "
        "prevalence raises positive predictive value and lowers the reassurance of a negative result; a lower prevalence does "
        "the reverse. Interpret the molecular result together with ultrasound, cytology, and the local tested population."
    ),
    "v147_fp_14": (
        "A keloid extends beyond the original wound margins, may continue enlarging, and has a stronger tendency to recur after "
        "excision alone. A hypertrophic scar remains confined to the incision and often flattens with maturation, although both "
        "can be raised, symptomatic, and erythematous early."
    ),
    "v222_hn_tep_snr": (
        "Inability to use finger occlusion should prompt assessment of vision, dexterity, reach, stoma geometry, pulmonary support, "
        "and peristomal seal. A hands-free valve may help only if the housing seals and expiratory pressure is adequate; otherwise "
        "adapt the occlusion aid or prioritize another communication method with speech-language pathology."
    ),
    "v246_ped_cranio_fnd": (
        "Palatal muscle dysfunction can sustain Eustachian-tube dysfunction throughout childhood, so middle-ear disease may "
        "recur after a tube extrudes even when the first set restored hearing. Longitudinal audiology detects recurrent conductive "
        "loss during speech-language development and guides whether additional ventilation or hearing support is needed."
    ),
    "v269_gen_afb_app": (
        "Reinspect both lungs and distal bronchi because more than one foreign body may be present, fragments can break off, and "
        "the object can migrate during extraction. A systematic final survey also identifies retained secretions, mucosal injury, "
        "bleeding, or another obstruction that would otherwise be mistaken for uncomplicated recovery."
    ),
    "v124_ped_04": (
        "Prolonged neonatal jaundice plus hearing loss and abnormal neurologic findings should widen "
        "the differential beyond isolated congenital deafness. Revisit congenital infection, especially "
        "CMV; bilirubin neurotoxicity/auditory neuropathy; genetic or syndromic disease; and metabolic or "
        "neurodegenerative disorders. Confirm the auditory phenotype with ABR/OAE and coordinate targeted evaluation."
    ),
    "v124_ped_06": (
        "A tract coursing between the internal and external carotid arteries is classic for a second "
        "branchial cleft anomaly. That predicts a deep course toward the tonsillar fossa and places the "
        "carotids and nearby hypoglossal and glossopharyngeal nerves at risk; define the tract before excision."
    ),
    "v128_lar_01": (
        "A true intracordal cyst usually causes focal marked reduction or absence of mucosal wave because "
        "it is tethered within the superficial lamina propria. A polyp is often more superficial and retains "
        "wave around or over it, although a large or fibrotic polyp can also reduce wave."
    ),
    "v137_tps_08": (
        "Recurrent or metastatic parathyroid carcinoma is often dominated by severe PTH-mediated "
        "hypercalcemia rather than tumor bulk alone. Control calcium urgently while assessing whether "
        "resection or another tumor-directed treatment can reduce the hormone-producing burden."
    ),
    "v137_fpt_10": (
        "Bare cartilage without perichondrium is a poorly vascularized recipient bed, so a skin graft is at "
        "high risk of loss. Preserve perichondrium when possible; otherwise provide a vascularized bed or "
        "choose a local flap rather than expecting reliable graft take on avascular cartilage."
    ),
    "v137_fpt_12": (
        "Overtight permanent otoplasty sutures can create an unnaturally sharp antihelical fold, contour "
        "distortion or telephone-ear deformity, and may erode or extrude with inflammation or chondritis."
    ),
    "v138_hn_24": (
        "Positive margins and pathologic extranodal extension are the major findings that intensify "
        "adjuvant therapy after transoral resection, commonly toward postoperative chemoradiation when "
        "tolerated. Multiple nodes, pT3-4 disease, perineural invasion, and lymphovascular invasion can also support radiation."
    ),
    "v138_lar_09": (
        "High-grade dysplasia warrants complete, adequately oriented tissue assessment and closer endoscopic "
        "surveillance because occult invasion and progression are more concerning. Treat visible disease with "
        "a voice-preserving excisional or ablative strategy and shorten follow-up for recurrence or worrisome margins."
    ),
    "v140_ped_06": (
        "Neurologic impairment, hypotonia, developmental delay, craniofacial or genetic syndromes, prematurity, "
        "and pre-existing dysphagia increase the chance that aspiration will persist after supraglottoplasty. "
        "Define baseline swallowing and counsel that correcting collapse does not correct neuromotor disease."
    ),
    "v143_lar_04": (
        "If meaningful neural recovery remains possible, defer irreversible glottic widening or use a reversible "
        "temporizing airway strategy. Cricoarytenoid fixation is mechanical; confirm it by palpation and address "
        "scar or joint fixation when feasible rather than assuming cordotomy alone treats the cause."
    ),
    "v144_oto_04": (
        "Repeated steroid-responsive relapse supports an immune-mediated phenotype but creates cumulative toxicity. "
        "Reconfirm audiometric response and mimics, involve rheumatology for steroid-sparing therapy, monitor toxicity, "
        "and preserve hearing-aid or cochlear-implant rehabilitation if hearing declines."
    ),
    "v145_hn_08": (
        "Total laryngopharyngectomy becomes more compelling with a nonfunctional aspirating larynx, extensive "
        "cartilage destruction, bulky T4 disease, circumferential hypopharyngeal involvement, or low likelihood "
        "of completing organ-preservation therapy. Swallow, pulmonary reserve, resectability, and goals remain decisive."
    ),
    "v145_lar_16": (
        "Horizontal glottic tremor is often targeted at the thyroarytenoid-lateral cricoarytenoid complex; vertical "
        "laryngeal tremor may require carefully selected strap-muscle treatment. Multilevel palate/pharynx/larynx "
        "tremor predicts less complete benefit from a focal injection."
    ),
    "v147_fp_07": (
        "Complete flaccid paralysis without recovery potential is not synkinesis and will not be corrected by "
        "chemodenervation. Prioritize eye protection and resting symmetry, then choose static support or dynamic "
        "reanimation according to denervation duration, viable motor targets, goals, and comorbidity."
    ),
    "v147_fp_12": (
        "Overtight Mustarde sutures can create a sharp antihelical fold, overcorrection or telephone-ear contour, "
        "and permanent sutures can extrude or cause inflammation/chondritis. Balance the fold rather than using "
        "suture tension to compensate for unaddressed conchal excess."
    ),
    "v152_ped_01": (
        "Dominant anterior vascular compression shifts treatment toward relieving that relationship—often "
        "aortopexy and/or anterior tracheopexy—rather than posterior tracheopexy alone. Define the vascular anatomy "
        "with dynamic airway evaluation and cross-sectional or cardiac imaging before choosing the operation."
    ),
    "v154_hn_app": (
        "A laryngectomy patient has no upper-airway connection to the lungs, so all oxygenation and intubation occur "
        "through the stoma. A tracheostomy patient usually retains an intact upper airway; ventilate through the tube "
        "first, but oral ventilation or intubation may remain possible if that airway is patent."
    ),
    "v206_rhi_max_app": (
        "A Haller cell can narrow and elevate the infundibulum near the orbital floor, while a lateralized uncinate "
        "can lie against the lamina and obscure the corridor. The natural maxillary ostium remains medial to the "
        "uncinate; identify it directly and avoid an isolated accessory opening or orbital injury while searching laterally."
    ),
    "v222_hn_tep_fnd": (
        "TEP speech diverts pulmonary air through a one-way prosthesis into the pharyngoesophageal segment and usually "
        "provides longer, more fluent speech. Esophageal speech uses a small injected air bolus without a prosthesis. "
        "An electrolarynx supplies an external vibration source, is easier to establish, but sounds mechanical."
    ),
    "v236_tps_men2_app": (
        "RET genotype stratifies medullary-thyroid-cancer aggressiveness and therefore timing of surveillance and "
        "risk-reducing thyroidectomy. Highest-risk variants require surgery in infancy; other variants allow timing "
        "to incorporate age, calcitonin trend, ultrasound, and family phenotype using current ATA guidance."
    ),
    "v236_tps_men2_snr": (
        "Elevated or rising calcitonin and suspicious cervical nodes convert a prophylactic operation into therapeutic "
        "cancer surgery. Stage the neck and plan total thyroidectomy with compartment-oriented nodal dissection where "
        "disease is demonstrated or indicated; do not perform prophylactic lateral-neck dissection."
    ),
    "v236_tps_ptca_fnd": (
        "Needle biopsy of suspected parathyroid carcinoma can seed tumor, rupture the capsule, cause hemorrhage or "
        "fibrosis, and rarely distinguishes adenoma from carcinoma because invasion is the key diagnosis. Use the "
        "biochemical phenotype and imaging to plan an intact oncologic resection."
    ),
    "v243_ped_tm_fnd": (
        "Deep anesthesia changes respiratory effort, and positive-pressure ventilation can stent the airway, masking "
        "the spontaneous-expiratory collapse that defines malacia. Dynamic bronchoscopy should assess appropriately "
        "preserved spontaneous breathing across the respiratory cycle."
    ),
    "v245_ped_hl_app": (
        "Auditory neuropathy can preserve OAEs or cochlear microphonic while disrupting ABR synchrony, so thresholds "
        "may fluctuate and speech understanding can be much worse than the audiogram predicts. Counsel around functional "
        "language access and consider implantation for persistently poor benefit rather than from threshold alone."
    ),
    "v113-oto-02": (
        "Use submillimeter temporal-bone CT reformatted in the plane of the superior canal "
        "(Pöschl) and orthogonal to it (Stenvers), plus VEMP testing. A low cVEMP threshold "
        "and/or increased oVEMP amplitude supports third-window physiology; symptoms, physiology, "
        "and dedicated CT should agree before repair is offered."
    ),
    "v128_lar_03": (
        "A cyst may be adherent within the superficial lamina propria, so aggressive dissection can "
        "remove or scar the pliable vibratory cover. The lesion can be gone yet the mucosal wave and "
        "voice become worse; use a tissue-preserving microflap and accept judicious residual wall when "
        "complete removal would require destructive stripping."
    ),
    "v135_oto_03": (
        "Serviceable hearing makes labyrinth preservation the priority. Define the fistula, leave its "
        "matrix until the end, avoid suction or direct instrumentation over the open labyrinth, use "
        "copious irrigation and meticulous low-trauma dissection, then seal the defect. A large fistula, "
        "only-hearing ear, or adherent matrix justifies an explicitly individualized matrix-removal plan."
    ),
    "v136_oto_13": (
        "Free-run EMG is a continuous warning channel: bursts or trains signal mechanical, thermal, or "
        "electrical irritation but do not quantify function. Stimulated EMG confirms the mapped nerve "
        "and trends the current needed to evoke a response; a rising threshold or lost response can "
        "indicate impaired conduction after technical causes are excluded."
    ),
    "v136_rhi_04": (
        "Situs inversus or dextrocardia may accompany primary ciliary dyskinesia; the combination with "
        "chronic sinopulmonary disease is the classic Kartagener phenotype. Normal laterality does not "
        "exclude PCD."
    ),
    "v136_rhi_17": (
        "The sphenopalatine artery is the major vessel at risk near the sphenopalatine foramen. Its "
        "posterior lateral nasal and septal branches should be anticipated during posterior nasal and "
        "sphenoid-region dissection."
    ),
    "v137_slp_01": (
        "Chronic opioids raise central sleep apnea and sleep-related hypoventilation, including ataxic "
        "breathing, rather than simply worsening pharyngeal collapse. Review dose and co-sedatives, "
        "assess ventilation as well as event type, and prioritize medication/ventilatory management over "
        "upper-airway surgery."
    ),
    "v137_slp_13": (
        "Severe retrognathia suggests a skeletal restriction rather than an isolated soft-tissue tongue-"
        "base problem. It should raise consideration of maxillomandibular advancement because MMA "
        "enlarges and tensions the retrolingual and retropalatal airway more comprehensively than focal "
        "tongue-base reduction."
    ),
    "v138_hn_11": (
        "Primary laryngopharyngectomy is favored when durable function-preserving treatment is unlikely: "
        "a nonfunctional larynx with major aspiration, extensive cartilage or laryngeal framework invasion, "
        "bulky disease unlikely to respond, or inability to tolerate/complete chemoradiation. Resectability, "
        "pre-treatment swallowing, pulmonary reserve, and patient goals all matter."
    ),
    "v138_lar_17": (
        "Stop blind extraction, maintain ventilation and visualization, and re-survey the airway. Retrieve "
        "fragments under direct control with the appropriate telescope/forceps; use flexible bronchoscopy "
        "for distal localization when needed and obtain thoracic support if a fragment is inaccessible or "
        "airway injury is suspected."
    ),
    "v138_lar_19": (
        "Reconsider nodules when the lesion is unilateral, irregular, ulcerated or leukoplakic, has focal "
        "mucosal-wave loss, enlarges despite voice therapy, or occurs with concerning exposure/history. "
        "Those findings warrant direct evaluation and often biopsy rather than assuming benign bilateral "
        "phonotrauma."
    ),
    "v139_gen_06": (
        "Look for inflammatory fluid or gas tracking from the cervical spaces below the thoracic inlet "
        "into the mediastinum, especially multiple mediastinal compartments, with fascial thickening, "
        "collections, or pleural/pericardial involvement. Image through the chest and involve thoracic "
        "surgery early."
    ),
    "v139_gen_10": (
        "Recurrent food impaction should prompt evaluation for eosinophilic esophagitis, including "
        "esophageal biopsies even when the mucosa is not dramatically abnormal. A stricture, ring, or "
        "other structural and motility disorder also remains in the differential."
    ),
    "v139_ped_20": (
        "The innominate artery is a common anterior compressor of the trachea. A double aortic arch, "
        "right arch with aberrant left subclavian artery, pulmonary artery sling, or other vascular ring "
        "can also compress the tracheobronchial tree and must be defined before airway surgery."
    ),
    "v140_gen_10": (
        "For an expanding postoperative neck hematoma, call for help and oxygen while immediately opening "
        "the skin closure, then divide the platysma/deep sutures and evacuate clot until the airway is "
        "decompressed; do not wait for transport or imaging. Secure the airway with anesthesia and return "
        "to the OR for definitive hemostasis."
    ),
    "v140_hn_03": (
        "Confirm chyle clinically and trend output. Maintain closed drainage, institute a low-fat diet with "
        "medium-chain triglycerides for a low-output leak, optimize fluids/electrolytes/nutrition, and apply "
        "selective pressure cautiously. Escalate persistent or rising output to operative ligation and/or "
        "interventional lymphatic management rather than prolonging ineffective diet alone."
    ),
    "v141_slp_06": (
        "Avoid adaptive servo-ventilation for predominant central sleep apnea in symptomatic chronic heart "
        "failure with reduced left-ventricular ejection fraction (classically LVEF 45% or less) because of "
        "the mortality signal in that population. Confirm the current cardiac phenotype and use an "
        "appropriate alternative strategy."
    ),
    "v144_oto_22": (
        "Do not biopsy or instrument a retrotympanic red mass in the office; a paraganglioma or aberrant "
        "vascular structure could hemorrhage catastrophically. Obtain dedicated imaging and vascular "
        "characterization first."
    ),
    "v154_gen_fnd": (
        "A malnourished patient may be thiamine depleted, and carbohydrate refeeding can abruptly increase "
        "thiamine demand. Give thiamine before or with calories to prevent Wernicke encephalopathy and "
        "cardiac complications while monitoring phosphate, potassium, magnesium, glucose, and volume status."
    ),
    "v154_hn_fnd": (
        "After total laryngectomy the mouth and nose no longer connect to the lungs. Oxygenation and "
        "ventilation must be delivered through the neck stoma; face-mask oxygen or oral intubation will not "
        "ventilate the patient. Remove a removable obstruction and place a cuffed tube through the stoma if "
        "positive-pressure ventilation is required."
    ),
    "v147_gen_01": (
        "Use the diagnosis, source, illness severity, host risk, local resistance, cultures when they will "
        "change care, and the narrowest effective site-penetrating agent. Reassess at 48–72 hours to stop, "
        "narrow, or redirect therapy; repeated empiric antibiotics cannot substitute for drainage or other "
        "source control."
    ),
    "v143_gen_05": (
        'At the bedside, opening the neck incision (removing skin staples/sutures and manually evacuating the underlying hematoma) can immediately relieve airway-compressing pressure while preparing for emergent return to the OR; this should not be delayed for imaging or transport if the airway is acutely threatened.'
    ),
    "v136_rhi_24": (
        'A concurrent internal-valve problem needs its own correction, such as spreader or batten grafts to widen or support the valve angle, because septoplasty alone will not fix valve collapse and addressing only the septum leaves the obstruction unresolved.'
    ),
    "v137_tps_12": (
        'A pre-existing contralateral vocal fold palsy raises the stakes of any new injury to the remaining functional nerve, since bilateral palsy risks airway obstruction requiring tracheostomy; document current voice/airway status with laryngoscopy before and after surgery, and discuss this bilateral-injury risk explicitly during consent.'
    ),
    "v138_hn_25": (
        'Neck erythema, swelling, fever, and saliva or foul-smelling drainage from the wound or drain, especially around the time of first oral intake, suggest a pharyngocutaneous fistula; suspicion should prompt holding oral intake, wound inspection, and imaging or a fluoroscopic swallow study as needed.'
    ),
    "v139_ped_07": (
        'Single-stage reconstruction with tracheostomy removal/closure and temporary endotracheal tube stenting during healing suits a stable child without significant reflux, aspiration risk, or comorbid pulmonary disease and with straightforward grafting; double-stage reconstruction with staged decannulation is preferred for severe or combined glottic/subglottic stenosis or a less optimized medical/pulmonary status.'
    ),
    "v139_ped_08": (
        'Airway-threatening floor-of-mouth or tongue-base involvement escalates urgency: securing the airway (early intubation or a defined airway plan) takes priority over elective sclerotherapy, and urgent debulking or sclerotherapy under controlled airway conditions may be needed rather than routine staged treatment.'
    ),
    "v143_rhi_04": (
        'Stop dissecting immediately, avoid grasping or resecting the prolapsed fat (mistaking it for polyp risks extraocular muscle or nerve injury), and check for periorbital ecchymosis/proptosis and extraocular movements to exclude a lamina papyracea breach with orbital injury before deciding whether to proceed, repair, or abort.'
    ),
    "v143_hno_05": (
        'Carotid encasement or skull-base extension raises the risk of vascular injury and may warrant preoperative vascular imaging or balloon-occlusion testing, a combined or staged approach with vascular or skull-base surgery, and explicit counseling about stroke risk, possible carotid sacrifice or reconstruction, and lower cranial nerve injury.'
    ),
    "v143_ped_01": (
        'A first branchial cleft anomaly (Work type I or II) courses near or through the parotid gland and can be intimately associated with the facial nerve, so dissection requires facial nerve identification and monitoring, unlike a second branchial cleft tract, which travels between the carotid vessels away from the facial nerve.'
    ),
    "v144_oto_23": (
        'Persistent perforation at 4 months without spontaneous healing supports considering tympanoplasty (myringoplasty with graft material such as temporalis fascia or perichondrium), rather than automatically requiring surgery; individualize timing based on hearing, infections, examination, water exposure, and patient preferences; ossicular chain assessment and possible ossiculoplasty should be discussed if the air-bone gap suggests ossicular involvement beyond the perforation alone.'
    ),
    "v144_rh_19": (
        'A caudal deviation requires stabilizing the caudal septum at the anterior nasal spine/maxillary crest, such as with suture fixation, batten or spreader grafting, or an extracorporeal technique for severe deformity, to prevent recurrence, whereas a simple mid-septal spur can often be corrected with straightforward cartilage/bone removal alone.'
    ),
    "v145_hn_03": (
        'In a large Shamblin III tumor encasing the carotid, preoperative planning should address the possibility of carotid sacrifice or reconstruction, including vascular surgery involvement, assessment of collateral cerebral circulation, and possible balloon test occlusion, along with counseling about stroke risk and lower cranial nerve injury.'
    ),
    "v146_ped_07": (
        'An airway-threatening lymphatic malformation shifts management from elective sclerotherapy to urgent airway securement (intubation or, if needed, tracheostomy) plus urgent debulking or sclerotherapy performed under controlled airway conditions, rather than routine staged outpatient treatment.'
    ),
    "v147_fp_11": (
        'Full-thickness alar loss requires reconstructing all three layers: internal lining (a mucosal, septal hinge, or folded composite flap), a cartilage framework graft to restore support and prevent notching or collapse, and external skin cover such as a paramedian forehead flap for larger defects, rather than a single-layer skin-only repair.'
    ),
    "v209_rhi_sphenoid_snr": (
        'Suspected internal carotid injury requires immediate firm packing of the sphenoid with hemostatic material to tamponade bleeding, maintaining the airway and hemodynamic stability, and urgent conversion to endovascular or open vascular control with neurosurgical/vascular surgery involvement, rather than continued attempts at endoscopic control alone.'
    ),
    "v220_hn_fom_snr": (
        'A segmental mandibular defect requires vascularized bone reconstruction, typically a fibula free flap, to restore both contour and dental rehabilitation potential, in contrast to a marginal mandibulectomy defect, which usually needs only soft-tissue coverage; osseointegrated implant planning should be considered at the time of bony reconstruction.'
    ),
    "v220_hn_tonsil_app": (
        'Delayed, brisk oropharyngeal bleeding after TORS, especially bleeding that recurs after initial control or is associated with airway compromise, requires immediate airway securement and urgent return to the operating room for surgical control, since the lingual or external carotid branches can be the source of a life-threatening post-TORS hemorrhage.'
    ),
    "v221_hn_tl_app": (
        'A large, high-output, or expanding fistula, evidence of exposed or threatened carotid vessels, uncontrolled infection or necrosis, or failure of conservative wound care to allow the tract to heal should prompt operative debridement and vascularized flap reconstruction, such as a pectoralis major flap, rather than continued conservative management.'
    ),
    "v221_hn_pps_snr": (
        'A vagal schwannoma typically splays the carotid artery anteriorly and the jugular vein posteriorly, and resection risks vocal fold paralysis/aspiration; a sympathetic-chain schwannoma instead displaces the carotid sheath as a unit anteriorly, and resection risks Horner syndrome, so preoperative counseling should differ based on which structure of origin is suspected.'
    ),
    "v222_hn_cbp_snr": (
        'Preoperative embolization can be considered for large, highly vascular Shamblin II/III tumors to reduce intraoperative blood loss, but it carries risk of stroke from inadvertent embolization of the internal carotid or its branches, cranial nerve injury from ischemia to adjacent structures, and post-embolization inflammation that can make dissection planes more difficult.'
    ),
    "v234_tps_reopthy_fnd": (
        'Review of the prior operative note for which side and how much thyroid/parathyroid tissue was removed, whether the RLN and parathyroid glands were identified with their status documented, and the pathology report for extent of disease and margins helps anticipate scarring, altered anatomy, and the structures at highest risk during re-entry.'
    ),
    "v234_tps_4g_fnd": (
        'Ectopic superior glands are most often found posteriorly, tracking toward the tracheoesophageal groove, retropharyngeal or retroesophageal space, or descending into the posterior mediastinum; ectopic inferior glands more often reflect incomplete descent, located high in the neck near the carotid bifurcation/thyrothymic tract, or descended too far into the anterior mediastinum/thymus.'
    ),
    "v235_tps_smgex_app": (
        'Hypoglossal nerve injury causes ipsilateral tongue weakness with deviation toward the injured side on protrusion and dysarthria/difficulty with bolus control, whereas lingual nerve injury causes numbness and taste loss over the anterior two-thirds of the tongue without motor tongue weakness; the motor-versus-sensory pattern distinguishes the two.'
    ),
    "v241_ped_supra_app": (
        'Treat the posterior interarytenoid mucosa conservatively and avoid symmetric, aggressive bilateral resection in the same setting, since over-resection there is the classic cause of supraglottic (interarytenoid) stenosis; staged, asymmetric, or limited unilateral surgery reduces this risk.'
    ),
    "v241_ped_supra_snr": (
        'If work of breathing and oxygen dependence persist despite a technically adequate supraglottoplasty, evaluate for a missed synchronous airway lesion (such as subglottic stenosis, tracheomalacia, or a second area of supraglottic collapse) with repeat endoscopy; noninvasive support can bridge a child who is improving, revision surgery suits an identified correctable lesion, and tracheostomy is reserved for failure of these measures or an unsafe airway.'
    ),
    "v241_ped_ltr_fnd": (
        'Cricotracheal resection removes the stenotic cricoid/upper tracheal segment and re-anastomoses healthy airway, so it does not depend on cartilage graft take and suits severe, circumferential, or previously-grafted stenosis; expansion (graft) reconstruction instead enlarges the airway lumen in place using cartilage grafts, preserving native tissue but depending on graft healing and mucosalization.'
    ),
    "v241_ped_ltr_app": (
        'Impaired vocal fold mobility or significant aspiration risk favors a double-stage approach with a longer period of stenting/protection and more cautious decannulation, since single-stage surgery closes the tracheostomy but retains an endotracheal tube temporarily during healing; subsequent extubation depends on adequate airway patency and protection that a mobility-impaired or aspirating larynx may not reliably provide.'
    ),
    "v244_ped_bca_fnd": (
        'A second-cleft tract classically passes between the internal and external carotid arteries en route to the tonsillar fossa, while third- and fourth-pouch anomalies communicate with the pyriform sinus and are distinguished by their relationship to the superior laryngeal nerve: third above, fourth below. They may present with recurrent suppurative thyroiditis or a left-sided neck abscess; delineate the individual tract and protect nearby vessels and laryngeal nerves during treatment.'
    ),
    "v244_ped_bca_snr": (
        'First-cleft anomalies risk the facial nerve; second-cleft tracts risk the hypoglossal and glossopharyngeal nerves near their course between the carotid vessels; third- and fourth-cleft tracts, which relate to the pyriform sinus, risk the recurrent laryngeal and superior laryngeal nerves during dissection near the thyroid and larynx.'
    ),
    "v251_lar_micro_snr": (
        'Limited neck extension or cervical spine immobility, temporomandibular joint dysfunction or trismus, retrognathia/micrognathia, prominent or fragile incisors, a short thyromental distance, and prior radiation-induced fibrosis of the neck and pharynx all predict difficult laryngoscope suspension and should be anticipated preoperatively.'
    ),
    "v254_lar_nodule_snr": (
        'Begin with a period of relative voice rest, then progress through structured vocal rehabilitation, gentle semi-occluded vocal tract exercises, and gradually increasing vocal loading, confirming mucosal wave/healing on stroboscopy before advancing from conversational voice to rehearsal-level singing and only later to full unrestricted performance voice, typically over several weeks under close therapy/laryngology follow-up.'
    ),
    "v254_lar_polycyst_app": (
        'Features favoring earlier surgery include a large or hemorrhagic polyp causing marked dysphonia, a professional voice user with functional/occupational urgency, failure of an adequate trial of voice therapy, or a lesion such as a true cyst that is unlikely to resolve with therapy alone; these shift the balance away from prolonged conservative management.'
    ),
}


def apply_curveball_answers_v368(challenges, data_module):
    modules = _module_index(data_module)
    filled = 0
    for q in challenges:
        question = _clean(q.get("curveball"))
        if q.get("id") == "v147_gen_01" and question.lower() == "boards":
            q["curveball"] = (
                "How should culture data, source control, host risk, and early clinical response "
                "be used to narrow or stop empiric antibiotics?"
            )
            question = q["curveball"]
        if q.get("id") in CURVEBALL_OVERRIDES:
            q["curveball_answer"] = CURVEBALL_OVERRIDES[q["id"]]
            filled += 1
            continue
        if not question or _clean(q.get("curveball_answer")):
            continue
        module = modules.get(q.get("concept_id")) or {}
        lead = _curveball_lead(question)
        support = _best_curveball_support(question, module, q)
        q["curveball_answer"] = (lead + ((" " + support) if lead and support else support)).strip()
        if not q["curveball_answer"]:
            q["curveball_answer"] = (
                "Reassess the new finding first, identify whether it changes airway, bleeding, "
                "neurologic, visual, or oncologic risk, and revise the next diagnostic or treatment "
                "step before returning to the original sequence."
            )
        filled += 1
    return filled


def install_daily_curriculum_quality_v368(data_module, app_module):
    original_get_items = data_module.get_adaptive_items_v120

    def get_adaptive_items_v368():
        items = original_get_items()
        apply_daily_items_v368(items, data_module)
        return items

    data_module.get_adaptive_items_v120 = get_adaptive_items_v368

    def adaptive_question_v368(item):
        return item.get("daily_prompt") or _prompt(
            _clean(item.get("topic")), item.get("stage"),
            item.get("daily_topic_kind") or "condition", {}, item.get("prompt") or "",
        )

    app_module._adaptive_question = adaptive_question_v368
    curveballs_filled = apply_curveball_answers_v368(
        data_module.CLINICAL_CHALLENGES_V119, data_module
    )
    # Keep both route lookup locations synchronized after mutation.
    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {
        q["id"]: q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get("id")
    }
    app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119

    sample = get_adaptive_items_v368()
    item_stats = apply_daily_items_v368(sample, data_module)
    return {"item_stats": item_stats, "curveballs_filled": curveballs_filled}
