"""Second-order learner-experience repairs for the live Daily Curriculum.

V36.8 removed the rigid six-sentence generator.  This pass repairs subtler
problems visible only after reviewing the rendered registry: alias-revealing
"blinded" cards, labels selected from incidental module words, mid-word excerpt
truncation, and advanced prompts that ask for an operation when the correct
senior decision is explicitly nonoperative.
"""

import re

from daily_curriculum_quality_v368 import _clean, _named_recognition_prompt


# These labels describe the presentation without giving away the diagnosis.
# Exact mappings take precedence over keyword inference from the rest of a module.
CASE_LABEL_OVERRIDES = {
    "Pediatric Chronic Rhinosinusitis": "Chronic pediatric nasal symptoms",
    "Floor of Mouth SCC": "Persistent floor-of-mouth lesion",
    "Base of Tongue SCC": "Oropharyngeal symptoms or neck mass",
    "Supraglottic Cancer": "Progressive swallowing or airway symptoms",
    "Tonsil SCC": "Oropharyngeal lesion or cystic neck mass",
    "Parapharyngeal Space Tumor": "Deep neck-space mass",
    "Carotid Body Paraganglioma": "Pulsatile lateral neck mass",
    "Basal Cell Carcinoma of the Head & Neck": "Suspicious cutaneous lesion",
    "Anaplastic Thyroid Cancer": "Rapidly enlarging thyroid mass",
    "Thyroglossal Duct Cyst": "Midline neck mass",
    "Lymphatic Malformation": "Compressible trans-spatial mass",
    "Pediatric Deep Neck Infection": "Febrile child with neck stiffness or drooling",
    "Residual OSA After Surgery": "Persistent sleep-breathing symptoms",
    "Restless Legs / Periodic Limb Movement Disorders": "Nocturnal limb discomfort or movement",
    "Peritonsillar Abscess": "Unilateral severe throat symptoms",
    "Frontal Sinus Fracture": "Forehead or brow contour injury after craniofacial trauma with possible CSF leak concern",
    "Chyle Leak": "Postoperative drain-output change",
    "Recurrent Laryngeal Nerve Injury During Thyroidectomy": "New postoperative voice or airway symptoms",
    "Nonfunctional Larynx / Chronic Aspiration After Cancer Therapy": "Late swallowing and pulmonary dysfunction",
    "Pediatric OSA / Adenotonsillar Disease": "Pediatric sleep-breathing symptoms",
}


# The source recognition prose for these topics contains the diagnosis (or an
# unmistakable abbreviation) verbatim.  Such cards are teaching summaries, not
# honest unidentified cases, so name the topic instead of pretending to blind it.
NAMED_RECOGNITION_TOPICS = {
    "Sinonasal Inverted Papilloma",
    "CRSwNP",
    "HPV-Associated Oropharyngeal SCC",
    "Glottic Cancer",
    "Medullary Thyroid Cancer",
    "Radioiodine-Refractory Differentiated Thyroid Cancer",
    "Pediatric Deep Neck Infection",
    "Recurrent Laryngeal Nerve Injury During Thyroidectomy",
    "Residual OSA After Surgery",
    "Deep Neck Space Infection",
    "Button Battery Ingestion",
}


PROMPT_ONLY_OVERRIDES = {
    ("Epiglottitis", "recognize"): (
        "A febrile child has severe odynophagia, drooling, a muffled voice, tripod positioning, anxiety and progressive stridor, and refuses to lie flat. What is the most likely diagnosis?"
    ),
}


DAILY_OVERRIDES = {
    ("Tympanic Membrane Perforation", "recognize"): (
        "After trauma or infection, otoscopy shows a true defect in the tympanic membrane. What features determine whether the perforation is uncomplicated or a clue to ossicular, inner-ear, or chronic middle-ear disease?",
        "Confirm the defect and describe acuity, size, site, edge, contamination or infection, hearing change, and vertigo. Marked conductive loss suggests ossicular injury; sensorineural loss or vertigo raises inner-ear concern; keratin, retraction, or chronic drainage suggests underlying chronic ear disease.",
    ),
    ("Tympanic Membrane Perforation", "localize"): (
        "How do perforation location, mechanism, and associated hearing or vestibular findings localize injury beyond the tympanic membrane?",
        "The membrane defect may be traumatic, infectious, iatrogenic, or secondary to chronic middle-ear disease. A large air-bone gap can indicate ossicular disruption, while sensorineural loss or vertigo suggests labyrinthine injury. Marginal keratin or a retraction pocket redirects attention to cholesteatoma rather than an isolated hole.",
    ),
    ("Tympanic Membrane Perforation", "operate"): (
        "When should a persistent tympanic-membrane perforation be repaired, and what must be excluded or corrected for tympanoplasty to succeed?",
        "Offer repair for a persistent symptomatic perforation, recurrent contamination or infection, or functionally important conductive loss after the ear is medically optimized. Define ossicular status, Eustachian-tube and middle-ear disease, perforation edge and remaining membrane; treat cholesteatoma or other deeper pathology rather than closing the surface defect alone.",
    ),
    ("Tympanic Membrane Perforation", "teach"): (
        "How would you teach a junior to separate an uncomplicated tympanic-membrane perforation from one that signals deeper middle- or inner-ear injury?",
        "Start with mechanism and time course, then describe the entire membrane and middle ear, quantify hearing, and ask about vertigo. Most clean acute perforations heal with dry-ear precautions, but disproportionate loss, vertigo, marginal keratin, chronic drainage, or failure to heal requires evaluation of the ossicles, labyrinth, and chronic ear disease before repair.",
    ),
    ("Inferior Turbinate Hypertrophy", "recognize"): (
        "A patient has chronic nasal obstruction with enlarged inferior turbinates. How do decongestion response and examination distinguish reversible mucosal congestion, fixed turbinate enlargement, septal narrowing, and nasal-valve collapse?",
        "Compare the airway before and after topical decongestion and inspect the septum and internal/external valves at rest and with inspiration. Substantial shrinkage supports a reversible mucosal component; persistent bulky tissue or bone suggests fixed hypertrophy, while an unchanged focal bottleneck or dynamic wall collapse identifies another contributor.",
    ),
    ("Inferior Turbinate Hypertrophy", "operate"): (
        "When is turbinate reduction appropriate, what function should the operation preserve, and what finding means the septum or nasal valve also needs attention?",
        "Consider reduction only for persistent symptomatic turbinate enlargement after appropriate medical treatment. Reduce obstructing submucosal tissue or bone while preserving functional mucosa and avoiding excessive resection; a fixed septal bottleneck or dynamic valve collapse requires its own plan rather than progressively removing turbinate tissue.",
    ),
    ("Restless Legs / Periodic Limb Movement Disorders", "recognize"): (
        "A patient reports an evening urge to move the legs with unpleasant sensations that begin at rest and improve with movement; a bed partner also notices repetitive sleep movements. Which features distinguish restless legs syndrome from periodic limb movements and from obstructive sleep apnea?",
        "Restless legs syndrome is a clinical sensorimotor urge that begins or worsens at rest, is relieved by movement, and is worse in the evening or night. Periodic limb movements are stereotyped movements measured during sleep and do not by themselves establish RLS. Neither pattern is evidence of pharyngeal obstruction.",
    ),
    ("Restless Legs / Periodic Limb Movement Disorders", "localize"): (
        "Why should restless legs symptoms be localized to sensorimotor and sleep physiology rather than the upper airway, and which mimics should be separated?",
        "The defining relationship to rest, movement, and circadian timing points to a sensorimotor disorder. Separate nocturnal cramps, positional discomfort, neuropathy, akathisia, habitual movement, and sleep-related breathing arousals before attributing every restless night to RLS or OSA.",
    ),
    ("Restless Legs / Periodic Limb Movement Disorders", "operate"): (
        "What is the correct senior-level decision when restless legs or periodic limb movements—not demonstrable obstruction—are disrupting sleep?",
        "Do not offer an ENT airway operation for RLS or PLMD. Review iron status and reversible contributors, address exacerbating medications when appropriate, and coordinate sleep-medicine or neurology treatment; investigate and treat OSA separately only when independent evidence supports it.",
    ),
    ("Restless Legs / Periodic Limb Movement Disorders", "teach"): (
        "How would you teach why a restless sleeper does not automatically need an OSA operation?",
        "Name the phenotype before choosing treatment: RLS is an awake sensorimotor urge, PLMS are measured sleep movements, and OSA is recurrent upper-airway obstruction. Correct contributors and refer for sleep or neurologic management; airway surgery treats only proven obstructive anatomy.",
    ),
    ("Circadian Rhythm Sleep-Wake Disorders", "operate"): (
        "What is the appropriate advanced decision when sleep is normal at the patient's preferred clock time but misaligned with work or school demands?",
        "ENT surgery does not correct circadian misalignment. Establish the phase pattern with history and sleep logs or actigraphy, then use appropriately timed schedule change, light exposure, melatonin when suitable, and sleep-medicine guidance rather than an upper-airway procedure.",
    ),
}


CURVEBALL_OVERRIDES = {
    "v113-rhi-03": "Map the internal maxillary artery supply—especially distal sphenopalatine branches—and any ascending pharyngeal or internal-carotid contribution before embolization. Define extension through the sphenopalatine foramen/pterygopalatine fossa, vidian canal, foramen rotundum, infratemporal fossa, orbit and skull base because vascular supply and intracranial or carotid relationships determine embolization safety and the resection corridor.",
    "v113-lar-01": "Closed reduction is most useful early, before capsular fibrosis fixes the cricoarytenoid joint. If intubation-related mechanical dislocation is strongly suspected, confirm the distinction from neurogenic paralysis with laryngoscopy, joint palpation under anesthesia and selective LEMG, then pursue prompt reduction rather than waiting through a prolonged paralysis-observation interval.",
    "v116-gen-03": "Favor endoscopic sphenopalatine-artery control when significant posterior bleeding persists or recurs despite initial stabilization, especially when prolonged packing would add airway, pressure-necrosis, aspiration or monitoring burden. Embolization is useful when endoscopic control fails, the source is inaccessible or broader arterial mapping is needed, but stroke, cranial-nerve and tissue-necrosis risks must be weighed.",
    "v124_oto_08": "Multiple tegmen defects and markers of elevated intracranial pressure increase the chance of another leak after technically successful closure. Repair all clinically relevant defects, counsel that the skull-base problem may be multifocal, and coordinate neuro-ophthalmology or neurology evaluation and longitudinal intracranial-pressure management rather than treating the ear defect as an isolated event.",
    "v124_oto_12": "Autoimmune inner-ear disease has no single exclusionary serologic test, so negative systemic markers do not rule out a clinically compatible, serially documented phenotype. Still exclude more common and consequential mimics—sudden idiopathic loss, Ménière disease, ototoxicity, infection, retrocochlear disease, genetic loss and other inflammatory disorders—before committing to prolonged immunosuppression.",
    "v124_ped_09": "Systemic propranolol transformed treatment of clinically important infantile subglottic hemangioma and is first-line for appropriate patients after cardiac and airway assessment. Secure or support a threatened airway first; reserve endoscopic debulking, open surgery or tracheostomy for severe obstruction, diagnostic uncertainty, contraindication or inadequate response.",
    "v136_oto_11": "Autophony, internal body-sound amplification, sound- or pressure-induced vertigo/oscillopsia, pulsatile tinnitus and an apparent low-frequency conductive gap with an intact middle ear suggest a third-window syndrome rather than primary hyperacusis. Confirm concordant physiology with VEMP testing and dedicated temporal-bone CT rather than diagnosing dehiscence from sound intolerance alone.",
    "v136_rhi_10": "A low or asymmetric skull base shortens the vertical margin for error and can be mistaken for an ethmoid partition. Review coronal and sagittal CT side-by-side, identify the lateral lamella and anterior ethmoid artery, stay oriented to lamina papyracea and known cells, and avoid assuming the opposite side predicts a safe superior limit.",
    "v136_rhi_12": "Circumferential mucosal stripping exposes bone and promotes inflammation, osteitis, granulation and concentric scar, which can restenose the narrow frontal outflow tract. Preserve mucosa wherever possible, use atraumatic instrumentation and ensure postoperative topical access, debridement and surveillance.",
    "v137_slp_02": "For delayed sleep-wake phase, appropriately timed bright light soon after the desired wake time generally advances the circadian phase; evening light tends to delay it further. Timing is the treatment, so pair light with a consistent wake schedule and avoid indiscriminate exposure without confirming the phase pattern.",
    "v138_hn_06": "Clinically positive cervical disease requires therapeutic, compartment-oriented neck management rather than an elective-neck calculation. Define levels, laterality, fixation and extranodal-extension concern on examination and imaging, then integrate ipsilateral or bilateral dissection and adjuvant therapy with primary resection according to the floor-of-mouth drainage pattern and final pathology.",
    "v138_lar_08": "The paraglottic space lies lateral to the ventricle and laryngeal saccule, while the pre-epiglottic space communicates with it superiorly around the quadrangular-membrane region. Involvement enables transglottic and extralaryngeal spread and can change T category and conservation options, so describe space invasion rather than merely naming a surface subsite.",
    "v138_lar_12": "Reduced upper-esophageal-sphincter opening appears as restricted distention and duration at the pharyngoesophageal segment with upstream pyriform residue; a posterior impression or bar may be present. Do not call primary cricopharyngeal dysfunction from that image alone—weak hyolaryngeal excursion or pharyngeal propulsion can create the same consequence.",
    "v139_ped_12": "A type I laryngeal cleft may appear as an abnormally deep interarytenoid notch extending to or just below the vocal processes, but flexible examination and swallow testing show consequences rather than reliably defining the defect. Diagnosis requires careful palpation of the posterior glottis during direct laryngoscopy/bronchoscopy.",
    "v139_ped_18": "Supraglottoplasty is tailored to the demonstrated collapse: commonly divide shortened aryepiglottic folds and selectively reduce redundant arytenoid/supraglottic mucosa. Preserve protective tissue, avoid injury to the interarytenoid mucosa and do not create opposing bilateral raw surfaces that can scar into supraglottic stenosis.",
    "v140_gen_06": "Rigid bronchoscopy can use controlled ventilation through the side port, spontaneous ventilation, intermittent apnea or jet ventilation depending on age, obstruction and team expertise. The surgeon and anesthesiologist must agree on ventilation and extraction pauses in advance, maintain visualization of the object and be prepared for complete obstruction if it migrates.",
    "v140_gen_07": "After button-battery or sharp-object removal, deep circumferential necrosis, bleeding, prolonged impaction, posterior wall injury or proximity to the aorta warrants continued admission, NPO management, multidisciplinary surveillance and cross-sectional vascular imaging when an aorto-esophageal injury is plausible. Delayed hemorrhage or fistula can occur after the object is gone.",
    "v145_hn_20": "Positive microscopic margins and pathologic extranodal extension are the strongest classic findings that escalate postoperative treatment toward concurrent chemoradiation when the patient can tolerate it. Other adverse features may justify radiation, but a TORS strategy should be reconsidered when the likely result is trimodality therapy without a functional or oncologic advantage.",
    "v251_lar_micro_fnd": "Reinke space is the superficial lamina propria immediately beneath the vocal-fold epithelium. Its pliability permits the mucosal wave; edema, cyst, scar or surgical stripping in this layer changes vibration, so phonomicrosurgery must preserve viable epithelium and superficial lamina propria whenever possible.",
    "v262_fpt_otoplasty_snr": "An acute auricular hematoma is a fluctuant blood collection after trauma and needs prompt drainage plus compression to prevent cartilage deformity. Perichondritis is painful erythema, edema and infection—often after piercing or surgery—and needs antipseudomonal therapy with drainage of abscess or devitalized tissue when present; compression alone is not adequate treatment.",
}


def _finish_at_word_boundary(prompt, limit=520):
    """Keep a useful stem without producing fragments such as ``H.`` or ``ne.``."""
    prompt = _clean(prompt)
    suffix = " What is the most likely diagnosis?"
    if not prompt.endswith(suffix):
        return prompt
    stem = prompt[:-len(suffix)].rstrip(" .")
    if len(stem) <= limit:
        return stem + "." + suffix
    candidate = stem[:limit]
    sentence = candidate.rsplit(". ", 1)[0].rstrip(" .")
    if len(sentence) >= 120:
        candidate = sentence
    else:
        candidate = re.sub(r"\s+\S*$", "", candidate).rstrip(" ,;:-")
    return candidate + "." + suffix


def apply_daily_curriculum_quality_v370(items, app_module):
    stats = {"items": 0, "labels": 0, "named_recognition": 0, "daily_overrides": 0}
    for item in items:
        topic = _clean(item.get("topic"))
        stage = item.get("stage")
        key = (topic, stage)
        if key in PROMPT_ONLY_OVERRIDES:
            prompt = PROMPT_ONLY_OVERRIDES[key]
            item["daily_prompt"] = prompt
            item["prompt"] = prompt
        if key in DAILY_OVERRIDES:
            prompt, answer = DAILY_OVERRIDES[key]
            item["daily_prompt"] = prompt
            item["prompt"] = prompt
            item["answer"] = answer
            stats["daily_overrides"] += 1
        if stage == "recognize":
            if key in DAILY_OVERRIDES:
                # A curated comparison/application question names or presupposes
                # the topic and is not an unidentified diagnostic vignette.
                item["blind_reveal"] = False
                item.pop("blind_case_label", None)
                stats["named_recognition"] += 1
            elif topic in NAMED_RECOGNITION_TOPICS:
                prompt = _named_recognition_prompt(topic)
                item["daily_prompt"] = prompt
                item["prompt"] = prompt
                item["blind_reveal"] = False
                item.pop("blind_case_label", None)
                stats["named_recognition"] += 1
            elif item.get("blind_reveal"):
                if topic in CASE_LABEL_OVERRIDES:
                    item["blind_case_label"] = CASE_LABEL_OVERRIDES[topic]
                    stats["labels"] += 1
                prompt = _finish_at_word_boundary(app_module._adaptive_question(item))
                item["daily_prompt"] = prompt
                item["prompt"] = prompt
        stats["items"] += 1
    return stats


def install_daily_curriculum_quality_v370(data_module, app_module):
    original_get_items = data_module.get_adaptive_items_v120

    def get_adaptive_items_v370():
        items = original_get_items()
        apply_daily_curriculum_quality_v370(items, app_module)
        return items

    data_module.get_adaptive_items_v120 = get_adaptive_items_v370

    def adaptive_question_v370(item):
        return item.get("daily_prompt") or item.get("prompt") or ""

    app_module._adaptive_question = adaptive_question_v370

    changed_curveballs = 0
    for challenge in data_module.CLINICAL_CHALLENGES_V119:
        answer = CURVEBALL_OVERRIDES.get(challenge.get("id"))
        if answer:
            challenge["curveball_answer"] = answer
            changed_curveballs += 1

    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {
        q["id"]: q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get("id")
    }
    app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119

    sample = get_adaptive_items_v370()
    return {
        "item_stats": apply_daily_curriculum_quality_v370(sample, app_module),
        "curveball_answers_repaired": changed_curveballs,
    }
