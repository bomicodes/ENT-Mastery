"""Fifth-order Daily Curriculum semantic and curveball cleanup.

This layer removes residual generic operative prompts from interpretation and
nonoperative topics, and replaces inherited boilerplate in curveball answers
with direct answers to the clinical question asked.
"""


DAILY_OVERRIDES = {
    ("Tympanometry / Acoustic Reflexes", "operate"): (
        "Before using tympanometry or acoustic reflexes to justify an irreversible ear treatment, which validity checks and discordant findings must be resolved?",
        "Confirm an adequate probe seal, appropriate ear-canal volume, a repeatable tracing, and agreement with otoscopy and the audiogram. A flat tracing with low volume suggests occlusion or probe error, normal volume may fit effusion, and high volume may reflect a perforation or patent tube. Recheck technique and reconcile unexpected reflex patterns before localizing disease or recommending surgery.",
    ),
    ("Vestibular Test Battery", "operate"): (
        "What must vestibular testing establish before an ablative ear procedure, and which discordance should stop the plan?",
        "Confirm the symptomatic and physiologically weaker ear, quantify usable function on both sides, and reconcile caloric, vHIT, VEMP, positional, ocular-motor, hearing, and bedside findings with the history. Stop if laterality is inconsistent, compensation or medication confounds testing, or the contralateral ear lacks sufficient reserve; repeat targeted testing before creating a permanent bilateral deficit.",
    ),
    ("Audiologic Electrophysiology / ABR-OAE-ECoG", "operate"): (
        "When an intraoperative auditory waveform changes, how do you distinguish technical or anesthetic artifact from possible neural injury before altering the operation?",
        "Announce the change and pause the provoking maneuver. Verify electrodes, impedance, stimulus delivery, masking and noise; review blood pressure, temperature, anesthetic changes and irrigation; then repeat the signal and compare morphology, latency and amplitude with baseline. A persistent reproducible change after reversible causes are corrected should drive surgical decompression or repositioning and explicit postoperative hearing assessment.",
    ),
    ("Neurotologic Intraoperative Cranial-Nerve Monitoring", "operate"): (
        "What is the immediate response to loss of a previously reliable cranial-nerve monitoring signal during skull-base surgery?",
        "Stop the maneuver, notify the team, and first exclude equipment, electrode, stimulation, neuromuscular-blockade, anesthetic, blood-pressure and temperature causes. Inspect the operative field for traction, compression, heat or vascular compromise, release reversible stress and retest proximally and distally when feasible. Monitoring is an adjunct: interpret recovery or persistent loss with direct anatomy and document the event and postoperative examination.",
    ),
    ("Objective Assessment of Nasal Function", "operate"): (
        "How should rhinomanometry, acoustic rhinometry, or symptom scores influence nasal surgery without allowing a single number to choose the operation?",
        "Use objective testing to corroborate obstruction, compare sides or decongested states, and measure outcome, but map the treatable structure with history, endoscopy and dynamic valve examination. Discordance should prompt reassessment for nasal-cycle effects, technique, mucosal disease, sensory complaints or multilevel obstruction; it should not trigger progressively larger septal, turbinate or valve surgery to normalize a number.",
    ),
    ("Allergy Testing & Interpretation", "operate"): (
        "What finding on allergy testing can change perioperative medical planning, and why does it not by itself create an indication for nasal surgery?",
        "A clinically relevant sensitization can guide avoidance, pharmacotherapy or immunotherapy and improve control of mucosal inflammation around surgery. A positive skin or serum test does not identify a septal, turbinate, valve or sinus target and may represent sensitization without symptomatic allergy. Operate only for independently demonstrated structural disease, objective CRS or another accepted indication after correlating the result with exposure and symptoms.",
    ),
    ("Indeterminate Thyroid Cytology / Molecular Testing", "operate"): (
        "How should an indeterminate cytology and molecular result change the choice among surveillance, diagnostic lobectomy, and a more extensive initial thyroid operation?",
        "Integrate Bethesda category, ultrasound pattern, size, nodal or invasive findings, clinical risk, contralateral disease, assay purpose and local predictive values. A reassuring classifier may support surveillance in an otherwise low-risk nodule; a rule-in alteration may justify diagnostic surgery or influence extent when it predicts a specific cancer biology. Discordant high-risk clinical findings outrank false reassurance, and molecular testing should not replace a required diagnostic or oncologic operation.",
    ),
    ("Stroboscopy Interpretation", "operate"): (
        "Which stroboscopic finding should change or defer a planned benign vocal-fold procedure, and what must be clarified first?",
        "Diffuse or unexplained focal stiffness, absent wave beyond a presumed lesion, irregular epithelium, abnormal vascularity, impaired motion or a mismatch between the visible lesion and vibratory deficit should reopen the diagnosis. Clarify scar, sulcus, deep cyst, paresis, dysplasia or malignancy and obtain appropriate tissue or further evaluation before performing a routine excision that could remove healthy cover without treating the true problem.",
    ),
    ("FEES", "operate"): (
        "Which FEES findings can change the safety or timing of an airway, voice, or swallowing procedure?",
        "Severe secretion burden, silent aspiration, ineffective clearance, profound sensory loss, fatigue, or aspiration that does not improve with tested strategies may require pulmonary and nutritional stabilization and can make glottic-widening or aspiration-worsening surgery unsafe. Conversely, aspiration that improves when glottic closure is simulated can support augmentation. State the white-out limitation and obtain MBS when oral, hyolaryngeal or UES mechanics will change the plan.",
    ),
    ("Modified Barium Swallow", "operate"): (
        "How can an MBS distinguish a surgically correctable swallowing problem from one unlikely to improve with an ENT procedure?",
        "Identify the timing and mechanism of airway invasion, hyolaryngeal excursion, pharyngeal driving force, residue, UES opening and response to maneuvers or bolus modification. A focal obstruction, selected glottic insufficiency or defined structural lesion may support a targeted procedure; diffuse weakness, poor sensation or aspiration from multiple phases requires rehabilitation, nutrition and medical planning rather than an anatomy-only operation.",
    ),
    ("Adult PSG Interpretation", "operate"): (
        "Which PSG findings determine perioperative risk yet still cannot identify the anatomic target for adult OSA surgery?",
        "Review event type, AHI or RDI, oxygen nadir and burden, hypoventilation, sleep stage and position dependence, arousals, rhythm findings and study adequacy. Severe hypoxemia, central events or hypoventilation alter optimization and monitoring, but PSG does not show whether collapse is palatal, lateral-wall, tongue-base or epiglottic. Choose anatomy-directed treatment only after awake examination and selected sleep-state phenotyping such as DISE.",
    ),
    ("Pediatric PSG Interpretation", "operate"): (
        "How should a pediatric PSG change the indication and postoperative monitoring plan for adenotonsillectomy without being treated as a stand-alone operative map?",
        "Confirm obstructive rather than central physiology and integrate event burden, gas-exchange abnormalities, age, obesity, craniofacial or neuromuscular disease, cardiopulmonary risk and examination. Severe OSA or major comorbidity increases the need for monitored postoperative care and a residual-disease plan. PSG measures physiology but does not prove that adenotonsillar tissue is the only obstructing level.",
    ),
    ("Evidence Interpretation / Outcomes Research", "operate"): (
        "Before changing an operative practice from a published study, which threats to applicability and causal inference must be checked?",
        "Check whether the population, indication, comparator, surgeon experience, technique and follow-up match the intended patient. Look for selection bias, confounding by indication, learning-curve effects, missing outcomes, crossover, multiplicity and clinically meaningful absolute effects—not only statistical significance. A retrospective surgical series can establish feasibility or associations but rarely proves superiority without a credible comparator and adjustment strategy.",
    ),
    ("Narcolepsy / Central Hypersomnolence Recognition", "operate"): (
        "What finding should stop an upper-airway operation from being offered as treatment for persistent sleepiness?",
        "Sleepiness that persists despite adequate sleep opportunity and effective treatment of any documented obstruction requires a central-hypersomnolence, circadian, medication, psychiatric or medical evaluation rather than more airway surgery. Validate overnight PSG and MSLT conditions and interpret them with cataplexy and REM-intrusion symptoms. An anatomic procedure is appropriate only for independently demonstrated obstructive disease, not for narcolepsy itself.",
    ),
}


CURVEBALL_OVERRIDES = {
    "v128_lar_04": "Massive bilateral Reinke edema can leave a narrow, compliant glottic aperture and make both intubation and postoperative swelling hazardous. Review the airway endoscopically, coordinate an awake or spontaneous-ventilation strategy with anesthesia when obstruction is significant, have smaller tubes and surgical-airway rescue available, avoid traumatic repeated attempts, and consider staged tissue-preserving reduction rather than aggressive bilateral stripping.",
    "v128_lar_06": "Treat the unilateral paresis as the driver rather than labeling all supraglottic squeeze as primary muscle-tension dysphonia. Document motion, tone, glottic gap and recovery prognosis with stroboscopy and selective LEMG; use voice therapy to reduce maladaptive compensation, but add temporary augmentation or a durable medialization/reinnervation plan when persistent insufficiency, aspiration or vocal demand warrants it.",
    "v132_fprs_01": "Clear rhinorrhea raises concern for an anterior skull-base CSF leak. Before fixation, obtain thin-cut facial and skull-base CT with appropriate brain imaging, assess for pneumocephalus and intracranial injury, and involve neurosurgery or skull-base expertise. Avoid blind nasal instrumentation when cribriform injury is possible, coordinate airway and fracture sequencing, and repair a persistent or operative-field leak with a planned vascularized or multilayer closure.",
    "v136_rhi_08": "The classic Hadad-Bassagasteguy nasoseptal flap is supplied by the posterior septal branch of the sphenopalatine artery, a terminal branch of the internal maxillary artery. Preserve the pedicle at the posterior septum and sphenoid face during the initial approach; injury can eliminate the preferred vascularized option for a large or high-flow skull-base defect.",
    "v138_lar_07": "For atrophy, augmentation is commonly bilateral and distributed in the deep lateral vocal fold to restore bowed volume while preserving the superficial vibratory cover. For unilateral paralysis, place material in the deep paraglottic compartment to medialize the fold and, when needed, support the vocal process/posterior gap. Inject incrementally under visualization and avoid superficial lamina-propria placement in either setting.",
    "v142_rhi_02": "During a Draf III, the orbits and laminae papyraceae define the lateral safety limits, while the anterior cranial base—particularly the first olfactory fibers and posterior table—defines the posterior limit. The nasal beak is anterior. Preoperative CT and constant identification of these boundaries prevent orbital entry, CSF leak and unsafe lateral or posterior drilling.",
    "v145_hn_10": "When excision behind the carotid sheath would add major neurovascular morbidity, coordinate with pathology and obtain image-guided core biopsies through a safe route, allocating fresh tissue for flow cytometry and additional cores for histology, immunophenotyping and molecular studies. Reserve open excision for persistently nondiagnostic sampling when architecture remains essential and the exposure can be justified safely.",
    "v146_ped_19": "Demonstrated anterior vascular compression changes treatment from generic airway stenting or posterior wall support to correction of the vascular-airway relationship. Depending on the vessel and dynamic pattern, options include aortopexy or innominate arteriopexy, sometimes combined with anterior or posterior tracheopexy. Define the compression with dynamic bronchoscopy and cross-sectional vascular imaging and address associated esophageal or posterior intrusion rather than assuming one operation fits every malacia pattern.",
    "v207_rhi_draf_snr": "Neo-osteogenesis narrows the neo-ostium with new bone; exposed drill bone promotes crusting, granulation and later stenosis; severe type-2 inflammation drives recurrent edema and polyposis; and inadequate debridement or topical access permits scar bridges and inflammation to mature. Reduce unnecessary mucosal stripping and thermal injury, create an appropriately sized drainage pathway, control the inflammatory phenotype, and provide planned postoperative saline, topical therapy and endoscopic care.",
    "v213_rhi_odont_found": "Posterior maxillary dental extraction, implant placement or removal, sinus augmentation, apicoectomy, cyst surgery and other dentoalveolar procedures near the sinus floor can create an oroantral communication. Define defect size, duration, infection and foreign material; coordinate dental source control and closure of a persistent fistula with sinus drainage when needed rather than treating only the nasal cavity.",
    "v213_rhi_odont_snr": "A displaced implant or dental foreign body is a persistent mechanical and infectious source. Localize it on CT, determine whether transnasal endoscopic, transoral or combined retrieval provides the safest access, restore maxillary drainage, culture or biopsy discordant disease, and coordinate definitive dental rehabilitation. Antibiotics or antrostomy without retrieval may leave the cause in place.",
    "v236_tps_men2_fnd": "An occult pheochromocytoma can release catecholamines during induction or thyroid manipulation and cause hypertensive crisis, arrhythmia, myocardial injury or death. Biochemically screen according to the patient's MEN2 genotype and age-related risk, localize a positive tumor, and achieve appropriate alpha blockade and adrenal treatment before elective thyroidectomy.",
    "v236_tps_ptca_app": "If the recurrent laryngeal nerve is functioning and the tumor can be separated without violating the capsule or leaving gross disease, preservation may be reasonable. True gross nerve invasion may require en-bloc sacrifice to maximize initial disease control after confirming contralateral function and counseling about voice, airway and swallowing consequences. Plan immediate repair or reinnervation when feasible; avoid peeling tumor or rupturing the parathyroid capsule merely to preserve motion.",
    "v241_ped_asp_fnd": "Children with neurologic impairment, prematurity, hypotonia, cranial neuropathy, laryngeal sensory loss, prior airway reconstruction or tracheostomy, and some syndromic or medically complex conditions may aspirate without cough. Recurrent pneumonia, wet breathing or voice, unexplained oxygen events, prolonged feeding and poor growth should prompt instrumental assessment even when caregivers never witness choking.",
    "v243_ped_vfi_snr": "Severe baseline aspiration lowers the tolerance for posterior cordotomy or arytenoidectomy because additional loss of glottic closure can worsen pulmonary injury. Confirm neurogenic versus mechanical immobility and recovery potential, optimize swallowing and pulmonary status, and favor observation, tracheostomy or another reversible airway strategy when feasible. If widening is unavoidable, use the least destructive adequate procedure with explicit postoperative swallow surveillance.",
    "v251_lar_inj_snr": "New stridor or dyspnea after injection is an airway complication until proved otherwise. Assess oxygenation and obtain urgent flexible laryngoscopy while mobilizing anesthesia and surgical-airway backup; look for overmedialization, hematoma, edema, laryngospasm or bilateral motion impairment. Keep the patient monitored, treat reversible edema or spasm, and secure the airway or remove excess material when obstruction is clinically significant rather than observing a deteriorating patient remotely.",
    "v255_lar_aa_reinn_app": "Reinnervation restores tone only after axonal ingrowth, so it cannot provide immediate aspiration control. Add a temporary injection when recovery or long-term geometry remains uncertain, or framework medialization with or without arytenoid adduction when a durable immediate closure is needed. Choose the bridge from gap shape, posterior level mismatch, pulmonary consequences and expected recovery while allowing reinnervation to mature.",
    "v255_lar_aa_reinn_snr": "Advanced age or poor donor-nerve quality reduces the speed and reliability of reinnervation, while a small anterior gap may be corrected predictably with injection or thyroplasty and may not justify arytenoid adduction. Favor an immediate framework or injectable solution when timely closure is the priority; reserve reinnervation for patients with viable targets, durable tone goals and enough time for delayed benefit.",
    "v258_fpt_lefort_fnd": "Maxillomandibular fixation removes immediate oral access and can turn postoperative bleeding, edema or emesis into an airway emergency. Establish a secure airway route that does not traverse a suspected skull-base fracture, confirm that rescue access remains possible after draping, keep release tools immediately available, and consider submental intubation or tracheostomy when prolonged fixation or severe panfacial swelling makes extubation unsafe.",
    "v258_fpt_lefort_app": "A top-down sequence is useful when the frontal bar, skull base or another upper facial reference is stable and the lower face or occlusion is too comminuted or unreliable to serve as the starting template. Rebuild the upper width and projection, then connect the midface and mandible while repeatedly checking occlusion and orbital relationships; the sequence should follow the most trustworthy remaining reference, not a rigid rule.",
    "v258_fpt_lefort_snr": "Before final tightening, seat both condyles, release and reproduce the planned occlusion, and check facial width, height and projection, zygomatic symmetry, orbital volume and globe position, canthal relationships, midline and mandibular continuity. Reconfirm airway access and inspect imaging or navigation when used; loosen and correct a construct that only appears aligned while fixation is forcing the bite.",
    "v262_fpt_otoplasty_app": "Disproportionate or escalating pain, tense swelling, new asymmetry, bleeding through the dressing, dusky skin, delayed capillary refill or cartilage exposure suggests hematoma or skin-perichondrial compromise. Remove the constrictive dressing, inspect promptly, evacuate a hematoma and secure hemostasis with a protective bolster; do not wait for routine follow-up when cartilage viability and infection risk are at stake.",
    "v263_sleep_hnsprog_fnd": "Before activation, document tongue protrusion, deviation and strength, lower-cranial-nerve function, speech and swallowing, and inspect the neck and chest wounds for hematoma, infection or lead migration. Significant new weakness or dysphagia warrants surgeon review and often delayed activation with imaging or device interrogation as indicated; programming should not mask a surgical neuropraxia or mechanical complication.",
}


def apply_daily_curriculum_quality_v373(items):
    changed = 0
    for item in items:
        override = DAILY_OVERRIDES.get((item.get("topic"), item.get("stage")))
        if not override:
            continue
        prompt, answer = override
        item["daily_prompt"] = prompt
        item["prompt"] = prompt
        item["answer"] = answer
        changed += 1
    return changed


def install_daily_curriculum_quality_v373(data_module, app_module):
    original_get_items = data_module.get_adaptive_items_v120

    def get_adaptive_items_v373():
        items = original_get_items()
        apply_daily_curriculum_quality_v373(items)
        return items

    data_module.get_adaptive_items_v120 = get_adaptive_items_v373

    def adaptive_question_v373(item):
        return item.get("daily_prompt") or item.get("prompt") or ""

    app_module._adaptive_question = adaptive_question_v373

    repaired = 0
    for challenge in data_module.CLINICAL_CHALLENGES_V119:
        answer = CURVEBALL_OVERRIDES.get(challenge.get("id"))
        if answer:
            challenge["curveball_answer"] = answer
            repaired += 1

    data_module.CLINICAL_CHALLENGE_BY_ID_V119 = {
        q["id"]: q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get("id")
    }
    app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    app_module.CLINICAL_CHALLENGE_BY_ID_V119 = data_module.CLINICAL_CHALLENGE_BY_ID_V119

    return {
        "daily_pairs_repaired": len(DAILY_OVERRIDES),
        "curveball_answers_repaired": repaired,
    }
