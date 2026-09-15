"""Fourth-order Daily Curriculum question/answer and curveball alignment repairs.

The earlier broad rewrite made every live item readable, but a residual group of
questions still asked for a complete pathway while revealing only a short pearl.
This layer narrows those prompts to the clinical decision actually supported by
the answer and replaces generic parent-topic curveball fallbacks with direct,
actionable answers to the question asked.
"""


DAILY_OVERRIDES = {
    ("Audiogram Interpretation", "workup"): (
        "When an audiogram appears internally inconsistent, which reliability checks should be reconciled before using it to localize hearing loss?",
        "Confirm that pure-tone responses are repeatable, speech-reception threshold agrees reasonably with the pure-tone average, and word-recognition testing used an appropriate presentation level and list. Reconcile air and bone thresholds with masking, tympanometry, otoscopy, and prior tests before labeling a conductive, sensorineural, mixed, or asymmetric loss.",
    ),
    ("Audiogram Interpretation", "operate"): (
        "Which audiometric inconsistency should stop you before recommending an irreversible ear operation, and what should be repeated or corroborated?",
        "Stop when the proposed operation does not fit reliable masked thresholds, speech testing, tympanometry, or the examination—for example, an unexplained air-bone gap or unexpectedly poor word recognition. Repeat or obtain expert audiometry, correct masking or transducer problems, and investigate retrocochlear or functional explanations before operating.",
    ),
    ("Audiogram Interpretation", "teach"): (
        "How should a resident read an audiogram in sequence so that the result localizes disease and changes management?",
        "First verify reliability; then classify type, degree, configuration, symmetry, and change from baseline. Reconcile speech reception and word recognition with pure tones, add tympanometry and the ear examination, and state the management consequence. Never make an irreversible decision from one isolated threshold or an unmasked apparent air-bone gap.",
    ),
    ("Narcolepsy / Central Hypersomnolence Recognition", "teach"): (
        "What distinction prevents a patient with excessive daytime sleepiness from being mislabeled as having OSA or narcolepsy before the workup is valid?",
        "Sleepiness is a symptom, not a diagnosis. First document adequate sleep opportunity and address circadian misalignment, sedating substances, medical or psychiatric contributors, and clinically important sleep-disordered breathing. Only then interpret overnight PSG followed by a properly performed MSLT in the context of cataplexy and other REM-intrusion symptoms.",
    ),
    ("Vocal Fold Polyp / Cyst", "workup"): (
        "What should stroboscopy establish before treating a suspected vocal-fold polyp or cyst, and which finding should reopen the diagnosis?",
        "Define lesion depth, epithelial integrity, mucosal-wave amplitude, closure pattern, stiffness, and contralateral reactive change while assessing voice use. A cyst often causes focal tethering and marked wave reduction; an irregular surface, leukoplakia, ulceration, impaired motion, or stiffness extending beyond the lesion should prompt evaluation for scar, sulcus, dysplasia, or malignancy rather than routine benign-lesion surgery.",
    ),
    ("Arytenoid Adduction / Reinnervation", "workup"): (
        "Which findings distinguish a posterior glottic gap or vertical-level mismatch suited to arytenoid adduction from denervation better addressed by reinnervation or augmentation?",
        "Use flexible laryngoscopy and stroboscopy to define side, gap geometry, vocal-process position, vertical mismatch, tone, and compensatory behavior; assess swallowing and recovery prognosis, with LEMG selectively. Arytenoid adduction targets posterior gap and level mismatch, reinnervation restores long-term tone but not immediate motion, and augmentation treats volume and closure.",
    ),
    ("Arytenoid Adduction / Reinnervation", "teach"): (
        "Why are injection, framework medialization, arytenoid adduction, and reinnervation not interchangeable treatments for unilateral vocal-fold paralysis?",
        "They solve different physiologic problems. Injection or thyroplasty adds bulk and medializes the edge; arytenoid adduction rotates the vocal process to address posterior gap and vertical mismatch; reinnervation restores tone over time without normal motion. Choose and combine them according to gap geometry, expected recovery, age, swallowing risk, and the need for immediate versus durable benefit.",
    ),
    ("Tongue Base Surgery", "workup"): (
        "Before tongue-base surgery for OSA, what must demonstrate that the tongue base is a meaningful treatment target rather than an incidental finding?",
        "Confirm clinically important OSA and review prior treatment, anatomy, BMI, dentition, tongue and lingual-tonsil volume, skeletal position, and multilevel collapse. Awake examination, imaging when relevant, and especially DISE can distinguish hypertrophic tissue, dynamic tongue-base collapse, epiglottic interaction, and palatal or lateral-wall disease that would require a different or combined plan.",
    ),
    ("Injection Laryngoplasty", "teach"): (
        "Which two technical errors during injection laryngoplasty can worsen voice or threaten the airway, and how are they prevented?",
        "Superficial injection into the vibratory cover can create stiffness, while excessive or poorly positioned augmentation can over-medialize the fold and impair voice or airway. Keep the needle and material in the intended deep paraglottic compartment, inject incrementally under visualization, reassess closure and voice, and stop before chasing perfect symmetry with excess volume.",
    ),
    ("Nasopharyngeal Carcinoma", "teach"): (
        "Why should a new unilateral middle-ear effusion in an adult trigger nasopharyngeal evaluation rather than repeated empiric ear treatment?",
        "A nasopharyngeal lesion can obstruct the Eustachian-tube orifice and present first as unilateral conductive hearing loss or effusion. Examine the nasopharynx and neck, obtain appropriate imaging for a suspicious or unexplained finding, and biopsy the primary lesion safely; do not let temporary improvement after myringotomy or antibiotics end the etiologic workup.",
    ),
    ("Leukoplakia / Laryngeal Dysplasia", "teach"): (
        "Why is vocal-fold leukoplakia a descriptive finding rather than a final diagnosis, and what determines surveillance versus biopsy or excision?",
        "Leukoplakia describes a white epithelial plaque whose histology can range from benign keratosis to invasive carcinoma. Risk factors, surface irregularity, vascular or ulcerative change, focal stiffness or impaired mucosal wave, growth, recurrence, and prior pathology determine the need and timing of tissue diagnosis while treatment preserves as much functional vibratory cover as oncologically safe.",
    ),
    ("Tonsil SCC", "workup"): (
        "What tissue and imaging are needed to stage a suspected tonsil squamous-cell carcinoma, and why must HPV status and the contralateral neck be addressed explicitly?",
        "Obtain diagnostic tissue with p16 testing as the accepted surrogate in oropharyngeal SCC, define mucosal and deep extent, and image both necks plus distant sites as stage and symptoms warrant. HPV-mediated and HPV-independent cancers use different staging frameworks, and tonsillar lymphatic drainage can be bilateral when disease approaches midline or involves adjacent tongue base or palate.",
    ),
    ("Vocal Fold Nodules", "workup"): (
        "Which voice and stroboscopic findings support vocal-fold nodules, and what asymmetric feature should redirect the diagnosis?",
        "Typical nodules are bilateral, fairly symmetric mid-membranous lesions associated with phonotraumatic behavior and often an hourglass closure pattern. Document mucosal wave, stiffness, occupational demand, and technique. A unilateral, irregular, markedly stiff, subepithelial, or vascular lesion should prompt consideration of polyp, cyst, scar, sulcus, dysplasia, or another focal process.",
    ),
    ("Supraglottoplasty", "teach"): (
        "What operative principle prevents supraglottoplasty from trading laryngomalacia for iatrogenic supraglottic stenosis?",
        "Tailor treatment to the demonstrated collapse—commonly dividing shortened aryepiglottic folds and selectively reducing redundant tissue—while preserving protective mucosa. Avoid deep injury, excessive arytenoid resection, interarytenoid injury, and broad opposing bilateral raw surfaces; reassess the airway and swallowing rather than maximizing tissue removal.",
    ),
    ("Head & Neck Radiation Toxicity / Survivorship", "teach"): (
        "Which late radiation effects require active longitudinal surveillance even after cancer control is established?",
        "Surveillance must address recurrence and second primaries while actively screening swallowing and aspiration, nutrition, dentition and osteoradionecrosis risk, xerostomia, fibrosis and trismus, thyroid dysfunction, hearing, carotid disease, pain, psychosocial health, and communication. Toxicities can emerge or progress years later, so survivorship is part of cancer treatment rather than an afterthought.",
    ),
    ("Posterior Cordotomy / Arytenoidectomy", "workup"): (
        "What must be established before an irreversible posterior glottic-widening procedure, and which finding should favor observation or a reversible airway strategy?",
        "Confirm whether immobility is neurogenic or mechanical with laryngoscopy and direct palpation when needed, define airway and swallow burden, review onset and cause, and estimate recovery with serial examination and selective LEMG. Recent potentially recoverable paresis should favor time, tracheostomy, or another reversible strategy when the airway permits rather than immediate destructive widening.",
    ),
    ("Audiologic Electrophysiology / ABR-OAE-ECoG", "teach"): (
        "How does identifying the generator and limitation of each electrophysiologic test prevent a false hearing or site-of-lesion diagnosis?",
        "OAEs assess cochlear outer-hair-cell function but depend on a usable conductive pathway; ABR samples synchronous neural conduction from auditory nerve through brainstem and estimates, rather than directly measures, behavioral threshold; electrocochleography samples cochlear and distal nerve potentials. Check stimulus, electrodes, noise, middle-ear status, age, and sedation before interpreting an absent or delayed waveform.",
    ),
    ("Hypopharyngeal Cancer", "workup"): (
        "What must the initial workup of hypopharyngeal cancer define before a treatment pathway is chosen?",
        "Obtain endoscopic tissue diagnosis and map subsite, longitudinal and deep spread, laryngeal function, cartilage or prevertebral involvement, cervical nodes, and distant or synchronous disease with appropriate cross-sectional and systemic staging. Document airway, pulmonary reserve, nutrition, dentition, baseline voice and swallowing because these findings can change both oncologic modality and reconstructive feasibility.",
    ),
    ("Hypopharyngeal Cancer", "manage"): (
        "Which tumor and patient factors determine organ-preservation therapy versus primary surgery for hypopharyngeal cancer?",
        "Balance stage and resectability with laryngeal function, cartilage or prevertebral invasion, aspiration, airway compromise, nutrition, pulmonary reserve, likelihood of completing chemoradiation, and salvage options. A preserved anatomic larynx is not a success if it remains unsafe or nonfunctional; surgery requires a deliberate neck, reconstruction, speech, and swallowing plan.",
    ),
    ("Hypopharyngeal Cancer", "teach"): (
        "Why must baseline nutrition, pulmonary reserve, and swallowing function be treated as oncologic variables in hypopharyngeal cancer?",
        "These cancers often present late with nodal disease, weight loss, aspiration, and synchronous tobacco-related disease. Baseline reserve determines treatment tolerance and whether organ preservation is functionally meaningful, while reconstruction and rehabilitation influence pulmonary complications, feeding dependence, and the ability to complete curative therapy.",
    ),
    ("Indeterminate Thyroid Cytology / Molecular Testing", "workup"): (
        "Before using a molecular result from an indeterminate thyroid nodule, which variables determine whether it can safely change management?",
        "Verify the Bethesda category and specimen adequacy, then integrate ultrasound phenotype, nodule size, compressive or invasive features, nodal findings, radiation and family history, patient preferences, and the assay's intended use and local cancer prevalence. Predictive values are context-dependent; a molecular result refines rather than replaces clinical and sonographic risk.",
    ),
    ("Floor of Mouth SCC", "workup"): (
        "What should examination, biopsy, and imaging establish before planning treatment for floor-of-mouth squamous-cell carcinoma?",
        "Use careful oral and bimanual examination to define mucosal extent, depth and fixation, tongue mobility, sublingual or submandibular involvement, mandibular relationship, and cranial-nerve symptoms. Obtain representative tissue and image deep soft tissue, mandible, cervical nodes, and distant disease as appropriate; distinguish proximity to bone from true cortical or medullary invasion.",
    ),
    ("Floor of Mouth SCC", "manage"): (
        "Which findings determine the primary, mandibular, and neck components of a floor-of-mouth cancer operation?",
        "Plan primary resection to obtain oncologic margins while preserving tongue and swallowing function when possible. Periosteal contact alone may permit clearance or marginal mandibulectomy, whereas gross medullary invasion usually requires segmental resection. Depth, midline proximity, nodal status, and drainage pattern determine ipsilateral or bilateral neck management and adjuvant therapy follows final pathology.",
    ),
    ("Parapharyngeal Space Tumor", "workup"): (
        "How do prestyloid versus poststyloid displacement and vascular imaging determine the biopsy and operative plan for a parapharyngeal-space mass?",
        "MRI and contrast CT define compartment, skull-base extent, fat planes, carotid and jugular displacement, neural relationships, and salivary continuity; add CTA or MRA when vascularity is possible. Prestyloid masses more often arise from deep-lobe salivary tissue, whereas poststyloid lesions favor neurogenic or paraganglionic origins. Avoid transoral or needle biopsy of a suspected vascular lesion.",
    ),
    ("Parapharyngeal Space Tumor", "teach"): (
        "What imaging clue should stop routine needle biopsy of a parapharyngeal-space mass?",
        "Marked enhancement, flow voids, vessel splaying or displacement, a salt-and-pepper appearance, or continuity with the carotid sheath should raise concern for paraganglioma or another vascular lesion. Complete vascular characterization and multidisciplinary planning first; uncontrolled biopsy can cause major hemorrhage and may not be needed when imaging is classic.",
    ),
    ("TEP and Alaryngeal Speech", "workup"): (
        "Which patient and anatomic findings determine whether tracheoesophageal speech is feasible after laryngectomy?",
        "Assess motivation, cognition, vision and hand dexterity, caregiver support, pulmonary reserve and secretion burden, stoma access, pharyngoesophageal-segment function, stricture or reconstruction, prior radiation, and ability to manage leakage and prosthesis changes. Speech-language pathology assessment and insufflation or other targeted testing can identify spasm or obstruction before puncture or revision.",
    ),
    ("TEP and Alaryngeal Speech", "teach"): (
        "Why is communication rehabilitation part of the laryngectomy treatment plan rather than an optional postoperative add-on?",
        "Total laryngectomy permanently separates the airway and removes laryngeal voice. Preoperative counseling should compare TEP speech, electrolarynx, and esophageal speech; set expectations for pulmonary and prosthesis care; and account for cognition, dexterity, anatomy, radiation, and patient goals. A technically successful cancer operation remains functionally incomplete without an accessible communication plan.",
    ),
}


CURVEBALL_OVERRIDES = {
    "v146_slp_06": "Complete concentric collapse at the velum is a contraindicating collapse pattern for conventional unilateral hypoglossal-nerve stimulation candidacy. It should redirect treatment toward weight and PAP optimization, palatal or multilevel strategies, skeletal options, or another individualized pathway rather than proceeding as though isolated anteroposterior palatal collapse were present.",
    "v255_lar_tremor_fnd": "Tremor involving the palate, pharyngeal walls, tongue base, vertical laryngeal motion, or multiple intrinsic laryngeal vectors suggests a distributed tremor that one focal thyroarytenoid injection will not fully control. Examine across sustained vowels, connected speech, quiet breathing, and pitch changes, and coordinate neurologic and voice assessment before setting expectations for botulinum toxin.",
    "v264_sleep_tongue_fnd": "Lingual-tonsil hypertrophy is visible lymphoid bulk that can be reduced directly. Skeletal retroposition is a fixed craniofacial relationship better addressed by advancement when clinically important, whereas dynamic tongue-base collapse is defined by sleep-state behavior, often on DISE, and may require stabilization, stimulation, suspension, or multilevel treatment. Name the mechanism before choosing the operation.",
    "v264_sleep_tongue_app": "Retrognathia, reduced posterior airway space from skeletal position, multilevel lateral-wall collapse, or persistent tongue-base collapse without substantial lingual-tonsil bulk argues against tissue removal alone. Favor maxillomandibular advancement for a meaningful skeletal deficiency and consider hyoid-based or other stabilization as part of a phenotype-specific multilevel plan rather than using lingual tonsillectomy as a generic tongue-base operation.",
    "v137_tps_06": "RET codon and risk category, the earliest reported age of medullary thyroid carcinoma in the family, calcitonin trend, examination and imaging findings, and the child's ability to undergo safe surgery determine timing. Higher-risk genotypes prompt earlier thyroidectomy, but pheochromocytoma must be excluded and treated first whenever age and phenotype make it plausible.",
    "v138_hn_18": "Anterior displacement of the internal carotid artery localizes a mass to the poststyloid carotid space and favors a vagal or sympathetic-chain schwannoma, paraganglioma, or other neurovascular lesion rather than a typical prestyloid deep-lobe parotid tumor. The relationship between carotid artery and jugular vein and any carotid splaying further refine the nerve or paraganglionic origin.",
    "v138_lar_20": "Treatment is matched to tremor distribution and disability: education and voice therapy can improve compensatory technique; neurology-directed medication may help a broader essential tremor phenotype; and botulinum toxin can reduce selected horizontal or vertical laryngeal tremor. Injection target and dose must balance benefit against transient breathiness, dysphagia, and the fact that extralaryngeal tremor may persist.",
    "v143_lar_03": "Severe dysplasia or carcinoma in situ carries substantially greater progression and recurrence concern than benign keratosis. Obtain complete, well-oriented tissue sufficient to exclude invasion, use oncologically adequate but voice-preserving excision or ablation when appropriate, shorten endoscopic surveillance, and re-biopsy new growth, ulceration, vascular change, or increasing stiffness rather than repeatedly observing an unchanged white-plaque label.",
    "v144_oto_18": "Chronic noise injury classically produces a bilateral high-frequency sensorineural notch, often greatest around 3–6 kHz with relative recovery at 8 kHz, whereas presbycusis more often slopes progressively through the highest frequencies without a discrete recovery. Real patients can have both, so interpret the pattern with exposure history, age, asymmetry, speech scores, and serial change.",
    "v145_lar_13": "Unilateral, irregular, or markedly stiff lesions are not typical paired vocal nodules. Reopen the differential to polyp, cyst, scar or sulcus, papilloma, dysplasia, and malignancy; review risk factors and use stroboscopy to define focal wave loss, with tissue diagnosis when epithelial or oncologic features warrant it rather than prescribing nodule therapy by location alone.",
    "v235_tps_indet_app": "A highly suspicious ultrasound pattern raises pretest malignancy risk and lowers the reassurance provided by a negative classifier. Reconcile the exact sonographic features, cytology, sampling adequacy, assay performance in that risk setting, nodal findings, and patient preferences; repeat sampling or diagnostic surgery may remain appropriate when clinical and molecular results are discordant.",
    "v251_lar_inj_app": "Recurrent aspiration pneumonia, inability to protect the airway or clear secretions, a large glottic gap with ineffective cough, progressive weight loss or feeding-tube dependence, and instrumental evidence that improved closure is likely to help favor earlier temporary augmentation while neural recovery remains uncertain. Augmentation complements, rather than replaces, swallowing therapy and evaluation of sensory or pharyngeal deficits.",
    "v254_lar_leuko_app": "Suspected invasion requires a biopsy that includes the epithelial basement membrane and adequate underlying stroma, oriented to the suspicious depth, rather than a tangential superficial shaving. Target the most irregular, ulcerated, vascular, or stiff area, preserve uninvolved vibratory cover when oncologically safe, and ensure the specimen allows pathology to distinguish severe dysplasia or in situ disease from invasive carcinoma.",
    "v254_lar_leuko_snr": "Progression to severe dysplasia, carcinoma in situ, or invasion; recurrent or enlarging disease despite adequate treatment; increasing focal stiffness; ulceration; abnormal vascularity; impaired motion; or deep extension makes simple office surveillance insufficient. Escalate to definitive tissue diagnosis, oncologic staging when invasion is found, and appropriately complete treatment while preserving function where safe.",
    "v255_lar_tremor_snr": "Define success by a patient-prioritized functional gain—such as easier conversation, improved intelligibility or reduced effort—plus a tolerable adverse-effect window, not by complete visual abolition of tremor. Document baseline and post-treatment perceptual or patient-reported measures, duration of benefit, breathiness and dysphagia, then adjust target, dose, laterality, and interval for the next cycle.",
    "v261_fpt_scar_fnd": "A hypertrophic scar remains confined to the original wound and may regress with maturation; a keloid grows beyond the wound boundaries, often continues to enlarge, and has greater recurrence risk. Distinguish both from a widened, depressed, contracted, infected, or recurrent-tumor scar before selecting pressure, silicone, injection, laser, excision, or multimodal therapy.",
    "v261_fpt_scar_snr": "Threatened eyelid closure or ectropion, nasal-valve or oral-commissure distortion, airway or feeding limitation, restricted neck or joint motion, neuropathic pain, recurrent ulceration, or rapidly progressive contracture can justify earlier intervention. Protect function first with therapy, splinting, injection, release, or reconstruction as appropriate rather than waiting for cosmetic maturation while deformity becomes fixed.",
    "v128_lar_02": "Confirm the lesion and vibratory effect with laryngoscopy and stroboscopy, then begin voice-behavior modification and lesion-specific voice therapy while addressing smoking, irritants, and vocal demand. Nodules commonly improve without surgery; selected persistent polyps or cysts with ongoing functional limitation may require tissue-preserving phonomicrosurgery after diagnosis and expectations are clear.",
    "v138_hn_10": "Before dentoalveolar surgery in a heavily irradiated mandible, review radiation dose and field, time since treatment, dental and periodontal status, healing history, smoking, nutrition, and current evidence of osteoradionecrosis. Coordinate with dental oncology and the treating head-and-neck team, favor prevention and the least traumatic feasible approach, obtain informed consent about impaired healing, and use adjuncts selectively rather than assuming one prophylactic regimen eliminates risk.",
    "v142_lar_01": "Choose a temporary material when meaningful neural recovery is plausible or the diagnosis and long-term closure need remain uncertain; its duration should bridge the expected recovery and reassessment interval. A longer-lasting injectable is more reasonable for low recovery potential or when a durable trial is intended, but permanent framework or reinnervation decisions still depend on gap geometry, prognosis, age, and patient goals.",
    "v143_lar_02": "Discuss dental or mucosal injury, tongue numbness or taste change, jaw and neck discomfort, and the possibility that limited oral opening, dentition, mandibular anatomy, cervical mobility, body habitus, or lesion position may prevent ideal line-of-sight exposure. The anesthesia plan must preserve ventilation and airway rescue while sharing access; inability to expose safely may require a different instrument, staged biopsy, or alternative approach.",
    "v171_oto_aied_app": "A reproducible steroid-responsive decline supports an immune-mediated phenotype but is not pathognomonic. Document serial thresholds and speech scores, exclude fluctuating Ménière, infection and other mimics, minimize repeated unstructured steroid exposure, and involve rheumatology or otology when toxicity or dependence prompts a steroid-sparing discussion while maintaining hearing rehabilitation.",
    "v234_tps_4g_app": "Before mediastinal escalation, systematically revisit the tracheoesophageal grooves, retroesophageal space, carotid sheaths, intrathyroidal sites, thyrothymic ligaments and cervical thymus, and undescended superior-gland locations near the posterior pharynx or high carotid sheath. Reconcile operative findings with imaging and intraoperative PTH, and use targeted re-localization rather than blind mediastinal exploration.",
    "v251_lar_inj_fnd": "When recovery is uncertain, use a temporary injectable whose expected resorption spans the observation and reinnervation interval, preserving options for repeat injection, framework surgery, or reinnervation. Longer-lasting material can be reasonable when recovery is unlikely or repeated procedures are undesirable, but avoid making an irreversible correction from an uncertain early prognosis.",
    "v269_gen_deep_fnd": "The danger space can transmit infection from skull base to diaphragm, while the retropharyngeal space descends into the upper mediastinum and communicates with the danger space; the pretracheal visceral space can also track into the anterior mediastinum. Clinical toxicity, chest symptoms, crepitus, or inferior neck extension should prompt contrast imaging of both neck and chest and early thoracic involvement.",
}


def apply_daily_curriculum_quality_v372(items):
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


def install_daily_curriculum_quality_v372(data_module, app_module):
    original_get_items = data_module.get_adaptive_items_v120

    def get_adaptive_items_v372():
        items = original_get_items()
        apply_daily_curriculum_quality_v372(items)
        return items

    data_module.get_adaptive_items_v120 = get_adaptive_items_v372

    def adaptive_question_v372(item):
        return item.get("daily_prompt") or item.get("prompt") or ""

    app_module._adaptive_question = adaptive_question_v372

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
