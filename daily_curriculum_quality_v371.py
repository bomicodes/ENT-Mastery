"""Focused question-answer alignment and curveball repairs for Daily Curriculum v37.1.

The broad v36.8/v37.0 rewrite made every prompt readable and restored answer
controls.  This layer fixes a subtler learner-experience failure: several broad
prompts asked for an entire pathway while the source answer supplied only one
teaching pearl, and several curveball fallbacks answered the parent topic rather
than the actual escalation in the question.
"""


DAILY_OVERRIDES = {
    ("MEN2 / RET", "teach"): (
        "In a patient with MEN2 who is preparing for thyroidectomy, which associated tumor must be excluded first, and why does the order matter?",
        "Exclude pheochromocytoma before thyroid surgery. An unrecognized catecholamine-secreting tumor can cause a life-threatening hypertensive crisis during anesthesia or manipulation, so biochemical evaluation and treatment of pheochromocytoma precede thyroidectomy.",
    ),
    ("Laryngeal Anatomy", "teach"): (
        "Which motor nerves supply the cricothyroid and the remaining intrinsic laryngeal muscles, and what examination change can follow injury to each?",
        "The external branch of the superior laryngeal nerve supplies the cricothyroid; injury impairs pitch elevation and vocal projection. The recurrent laryngeal nerve supplies the other intrinsic laryngeal muscles; injury causes vocal-fold motion impairment with voice, swallowing, or airway consequences depending on side and position.",
    ),
    ("Modified Barium Swallow", "teach"): (
        "Why should a modified barium swallow be interpreted as a functional experiment rather than a single aspiration score or static image?",
        "MBS samples swallowing across bolus volumes, viscosities, delivery methods, and compensatory strategies. The useful report identifies the physiologic impairment, when airway invasion or residue occurs, and whether a tested intervention changes it; one frame or PAS value cannot represent the whole study.",
    ),
    ("Presbyphonia", "workup"): (
        "Which voice assessments establish age-related glottic insufficiency, and what asymmetric finding should reopen the diagnosis?",
        "Use perceptual and patient-reported voice assessment plus laryngoscopy with stroboscopy to document bowing, atrophy, closure pattern, and vibratory function. Asymmetric motion, focal stiffness, a mass, or disproportionate unilateral atrophy should prompt evaluation for paresis or another structural or neurologic cause rather than attribution to age alone.",
    ),
    ("Presbyphonia", "teach"): (
        "How would you explain why treatment for presbyphonia is based on functional burden rather than age or the appearance of bowing alone?",
        "Age-related bowing is common and does not itself require treatment. Match voice therapy and, when needed, temporary or durable augmentation to the patient's communication demands, symptoms, glottic gap, pulmonary support, and response to therapy after excluding focal lesions and paresis.",
    ),
    ("Floor of Mouth SCC", "teach"): (
        "A floor-of-mouth cancer abuts the mandible on imaging. Why is proximity not the same as invasion, and what findings determine the mandibular resection plan?",
        "Thin floor-of-mouth soft tissue can place tumor close to the mandible without cortical or medullary invasion. Combine bimanual fixation, inferior-alveolar or mental-nerve symptoms, dental findings, and cross-sectional imaging to determine whether periosteal clearance, marginal mandibulectomy, or segmental resection is required.",
    ),
    ("Tracheomalacia / Bronchomalacia", "teach"): (
        "Why can a normal static airway image fail to exclude tracheomalacia or bronchomalacia, and what assessment demonstrates the relevant physiology?",
        "Malacia is excessive dynamic expiratory collapse, so a quiet static image can look normal. Correlate symptoms with dynamic bronchoscopy and/or appropriately performed dynamic expiratory imaging, describe the affected segment and severity, and assess vascular compression or other causes before choosing treatment.",
    ),
    ("Airway Foreign Body", "teach"): (
        "Why should a classic choking event with persistent focal respiratory findings outweigh a normal chest radiograph?",
        "Many aspirated objects are radiolucent, and inspiratory/expiratory films can be normal. A convincing witnessed event, unilateral wheeze or diminished breath sounds, persistent cough, or recurrent focal pneumonia sustains the diagnosis and can justify rigid bronchoscopy despite nondiagnostic imaging.",
    ),
    ("FEES", "workup"): (
        "What must a complete FEES interpretation describe beyond a penetration-aspiration score?",
        "Describe secretion management, anatomy and movement, premature spillage, residue location and amount, penetration or aspiration before and after the white-out, sensory response, fatigue, and the effect of tested postures, maneuvers, and consistencies. State the white-out limitation and recommend MBS when oral-phase, hyolaryngeal, or UES mechanics require fluoroscopic assessment.",
    ),
    ("FEES", "teach"): (
        "What is the most useful way to teach FEES reporting so the result changes care rather than merely naming a PAS score?",
        "Report the physiologic problem, its consequence, and the response to intervention: what material enters the airway or remains as residue, when it happens, whether the patient senses and clears it, and which tested strategy improves safety or efficiency. The PAS score supports that narrative but does not replace it.",
    ),
    ("Epistaxis", "teach"): (
        "How would you teach a junior to triage epistaxis by patient stability and likely bleeding source rather than by the amount of blood visible at one moment?",
        "Begin with airway and hemodynamics, anticoagulant or bleeding risk, and resuscitation needs; then clear clot, use vasoconstriction and directed examination to distinguish an accessible anterior source from persistent posterior or unidentified bleeding. Escalate recurrent or significant bleeding to packing, endoscopic arterial control, or embolization according to stability and source.",
    ),
    ("Pediatric Hearing Loss Workup", "teach"): (
        "Why is timely language access—not simply improving an audiogram—the organizing goal of a pediatric hearing-loss workup?",
        "Hearing supports speech, language, learning, and social development during time-sensitive developmental windows. Confirm type and severity with age-appropriate testing, address reversible conductive disease, provide amplification or implant evaluation without avoidable delay, and integrate early intervention, communication goals, and etiologic assessment.",
    ),
    ("Juvenile Nasopharyngeal Angiofibroma", "teach"): (
        "Why should an adolescent boy with recurrent epistaxis and a hypervascular nasopharyngeal mass be characterized radiographically before office biopsy?",
        "The classic clinical and imaging pattern can establish a presumptive diagnosis, while office instrumentation can cause severe hemorrhage. Contrast CT and MRI define nasal, pterygopalatine, infratemporal, orbital, skull-base, and intracranial extent and vascular relationships before angiography, embolization, or resection planning.",
    ),
    ("Posterior Cordotomy / Arytenoidectomy", "teach"): (
        "What functional tradeoff must be explained before posterior cordotomy or arytenoidectomy for bilateral vocal-fold immobility?",
        "Enlarging the posterior glottic airway reduces resistance but also sacrifices glottic closure, so greater airway gain can worsen breathy voice and sometimes swallowing protection. Confirm stable bilateral immobility or fixation, choose the least destructive adequate enlargement, and counsel that revision or contralateral treatment may be needed.",
    ),
    ("Tongue Base Surgery", "teach"): (
        "Which perioperative complications deserve explicit planning before tongue-base surgery for OSA?",
        "Postoperative edema and hemorrhage can threaten the airway, while pain and tongue-base dysfunction can worsen swallowing and oral intake. Plan exposure and hemostasis, postoperative airway monitoring by risk, analgesia that limits respiratory depression, hydration/nutrition, and a clear response to delayed bleeding or progressive obstruction.",
    ),
    ("Ethmoidectomy", "manage"): (
        "When does ethmoidectomy enter the CRS treatment pathway, and how should disease extent determine the operation?",
        "Offer surgery for appropriately selected objective ethmoid disease that remains burdensome despite suitable medical therapy or when a complication demands source control. Match the dissection to disease and access needs, preserve mucosa and reliable landmarks, and discuss continued postoperative topical therapy rather than presenting surgery as a cure for the inflammatory phenotype.",
    ),
    ("Microtia / Aural Atresia", "teach"): (
        "Why must hearing rehabilitation begin before cosmetic auricular reconstruction planning in a child with microtia or aural atresia?",
        "Language access is time-sensitive, especially with bilateral loss. Obtain early audiology and provide appropriate bone-conduction or other hearing support while later coordinating auricular reconstruction, prosthetic options, and atresiaplasty candidacy so one pathway does not compromise the timing or anatomy of another.",
    ),
    ("Vocal Fold Polyp / Cyst", "teach"): (
        "Why can complete removal of a benign vocal-fold polyp or cyst still produce a worse voice?",
        "The vibratory cover depends on pliable epithelium and superficial lamina propria. Excessive dissection, epithelial loss, or injury to the vocal ligament can replace a focal lesion with broad scar and persistent mucosal-wave loss, so surgery must be lesion-specific and tissue-preserving after voice behavior and expectations are addressed.",
    ),
    ("Submandibular Gland Excision", "teach"): (
        "Which three nerve relationships should be rehearsed before submandibular gland excision, and what deficit follows injury to each?",
        "Protect the marginal mandibular branch along the lower facial border, the lingual nerve as it loops around the submandibular duct, and the hypoglossal nerve deep to the gland. Injury causes lower-lip weakness, tongue numbness/taste disturbance, and ipsilateral tongue weakness, respectively.",
    ),
    ("Parathyroid Carcinoma", "teach"): (
        "Why is the first operation especially important when parathyroid carcinoma is suspected preoperatively?",
        "The best chance for durable control is an intact en-bloc initial resection without capsular rupture or tumor spillage, with removal of directly invaded adjacent tissue when appropriate. Piecemeal excision or violation can seed recurrent disease, which is difficult to eradicate and may cause severe recurrent hypercalcemia.",
    ),
}


RECOGNITION_PROMPTS = {
    "Chronic Otitis Media / Cholesteatoma": "A patient has chronic foul otorrhea and conductive hearing loss. Otoscopy shows a pars-flaccida retraction pocket containing keratin debris with adjacent granulation. What is the most likely diagnosis?",
    "Septal Deviation": "A patient has persistent unilateral nasal obstruction despite decongestion. Examination shows a fixed septal spur narrowing the symptomatic side, without a mass or dynamic lateral-wall collapse. What is the most likely diagnosis?",
    "Secondary / Tertiary Hyperparathyroidism": "A patient with advanced chronic kidney disease has persistently elevated PTH, phosphate retention, altered vitamin-D physiology, and multigland parathyroid hyperplasia; hypercalcemia later develops despite medical therapy. What pathophysiologic diagnosis best explains this pattern?",
    "Submandibular Sialolithiasis": "A patient has recurrent unilateral submandibular swelling and colicky pain that begins with meals. Floor-of-mouth palpation finds a firm focus along Wharton duct with reduced salivary flow. What is the most likely diagnosis?",
    "Supraglottic Cancer": "A patient develops progressive dysphagia, odynophagia, referred otalgia, and a level II neck mass before major voice change. Laryngoscopy shows an irregular lesion of the epiglottis extending toward the aryepiglottic fold. What is the most likely diagnosis?",
    "Floor of Mouth SCC": "An adult has a persistent indurated ulcer of the floor of mouth with pain, reduced tongue mobility, and a new ipsilateral neck node. What diagnosis must be presumed until biopsy proves otherwise?",
    "Mandible Fracture": "After facial trauma, a patient has new malocclusion, trismus, sublingual ecchymosis, segment mobility, and numbness of the lower lip. What is the most likely diagnosis?",
    "Frontal Sinus Fracture": "After high-energy forehead trauma, a patient has a brow laceration and contour depression with pneumocephalus and clear rhinorrhea on evaluation. What injury must be defined on thin-cut CT?",
    "Septal Hematoma": "After nasal trauma, a child develops progressive bilateral obstruction. Examination shows soft, boggy, fluctuant swelling on both sides of the septum that does not shrink with decongestion. What is the most likely diagnosis?",
}


CURVEBALL_OVERRIDES = {
    "v264_sleep_tongue_snr": "New dental pain or malocclusion after genioglossus advancement is not routine throat pain. Recheck the occlusion and dentition, examine for infection or wound dehiscence, and obtain appropriate mandibular imaging to evaluate screw or osteotomy displacement, dental-root injury, fracture, nonunion or malunion. Early maxillofacial reassessment is warranted when the bite has changed.",
    "v248_ped_reflux_eoe_fnd": "Eosinophilic esophagitis is an esophageal clinicopathologic diagnosis. Laryngeal erythema or edema is nonspecific, and a normal larynx does not inspect the esophageal mucosa or exclude patchy eosinophilic inflammation. A compatible symptom history requires GI evaluation with upper endoscopy and biopsies from multiple esophageal levels.",
    "v175_oto_ototox_snr": "Aminoglycoside vestibulotoxicity may present with oscillopsia during head movement, imbalance that is worse in darkness or on uneven ground, and gait unsteadiness without a new pure-tone threshold shift. Examine dynamic visual acuity and head impulses and obtain vestibular testing appropriate to suspected bilateral hypofunction; stable hearing does not exclude vestibular injury.",
    "v241_ped_choanal_snr": "Syndromic craniofacial, cardiac, neurologic and feeding problems change airway timing, anesthesia risk and the likelihood that choanal repair alone will normalize breathing. Reflux or secretion burden can complicate healing but should not become a catch-all explanation for restenosis. Repeated narrowing warrants endoscopic definition of scar, bony restenosis and contributing anatomy, followed by individualized revision and postoperative surveillance counseling.",
    "v143_gen_02": "Suspected descending mediastinitis expands imaging to contrast-enhanced neck and chest when the patient is stable and triggers immediate thoracic-surgery involvement in addition to ENT, critical care and infectious disease. Broad IV antibiotics and resuscitation begin promptly; drainage must address every involved cervical and mediastinal compartment rather than stopping at the original neck abscess.",
    "v175_oto_tmperf_snr": "An anterior perforation can limit visualization and graft support and may require a different exposure or stabilization technique. Active otorrhea and uncontrolled middle-ear or Eustachian-tube disease should be treated and characterized before elective closure when possible, because persistent inflammation reduces success; the timing and graft plan should match location, edge, middle-ear status and hearing goals.",
    "v269_gen_deep_snr": "Suspected septic internal-jugular thrombophlebitis requires contrast imaging that evaluates the neck veins and deep spaces, blood cultures, and chest imaging for septic pulmonary emboli. Start IV therapy with reliable anaerobic and oropharyngeal coverage and drain any source. Anticoagulation is individualized with multidisciplinary input rather than automatic for every case.",
    "v146_tps_09": "Document both vocal folds before reoperation. A preexisting unilateral paralysis makes injury to the functioning contralateral nerve a potential bilateral-airway catastrophe, so confirm that contralateral dissection is truly necessary, use meticulous nerve identification with monitoring as an adjunct, and consider staging or an alternative plan when oncologically and biochemically acceptable. Plan postoperative airway observation.",
    "v251_lar_micro_app": "Stage treatment when bilateral lesions require broad opposing free-edge dissection or when complete treatment would create excessive bilateral mucosal injury. Preserving at least one stable vibratory edge and avoiding opposing raw surfaces reduces web and scar risk; prioritize the dominant lesion, allow healing, reassess voice and stroboscopy, then address the other side if still necessary.",
    "v221_hn_npc_app": "Where validated, pretreatment plasma EBV DNA adds prognostic information and can help establish a baseline disease burden in EBV-associated nonkeratinizing nasopharyngeal carcinoma. Post-treatment kinetics or re-emergence can support response and surveillance assessment, but results must be interpreted with imaging and examination and are not a stand-alone screening or recurrence diagnosis.",
    "v137_fpt_15": "A true keloid extends beyond the original wound and has a higher recurrence risk than a hypertrophic scar. Counsel that excision alone commonly recurs; use multimodal control such as serial intralesional corticosteroid with or without 5-FU, pressure or silicone where feasible, and selected postoperative radiation for difficult recurrent lesions after weighing site- and patient-specific risks.",
    "v243_ped_vfi_app": "Brain and brainstem imaging is particularly important for unexplained bilateral vocal-fold immobility, associated central neurologic findings, other cranial neuropathies, abnormal development or tone, or no plausible peripheral/iatrogenic cause. Imaging should follow the suspected vagal pathway; direct laryngoscopy with palpation is still needed when mechanical fixation remains possible.",
    "v143_ped_04": "When continuous secretion aspiration causes life-threatening pulmonary disease despite optimized feeding, therapy and correction of reversible lesions, discuss procedures that separate or close the laryngeal airway, such as laryngotracheal separation or selected closure/diversion operations. The choice depends on reversibility, communication goals, tracheostomy status and caregiver priorities; these operations trade native voice and airway continuity for pulmonary protection.",
    "v142_fpt_01": "Thin or scarred skin, prior rhinoplasty, smoking or vasculopathy, prior radiation, active inflammation, and an already overprojected or tightly tensioned tip increase ischemia and contour-visibility risk. Avoid aggressive defatting and wide undermining, preserve the subdermal vascular plexus, minimize tension, and counsel that thick and thin envelopes create different limits rather than simply requiring more thinning.",
    "v222_hn_cbp_app": "Preexisting contralateral vagal dysfunction raises the cost of any new ipsilateral vagal deficit: bilateral dysfunction can produce severe dysphagia, aspiration and laryngeal dysfunction. Favor observation or radiotherapy when oncologically reasonable, establish baseline lower-cranial-nerve and swallow function, and if intervention is necessary sequence treatment to preserve the only functioning side and plan swallowing/airway rehabilitation.",
    "v145_hn_07": "Recurrent aspiration pneumonia requires urgent instrumental swallowing assessment with FEES and/or MBS, pulmonary and nutrition review, and endoscopic evaluation for recurrence, stenosis and laryngeal dysfunction. Decide whether compensatory strategies, diet change, rehabilitation, dilation or augmentation can restore safety; feeding-tube support or aspiration-prevention surgery enters the discussion when pulmonary injury continues despite maximal restorative treatment.",
    "v144_oto_05": "Early diffusion-weighted MRI can miss small posterior-fossa infarcts, especially in the brainstem and during the first day. A central HINTS pattern, severe truncal ataxia, focal deficits or a high-risk trajectory should outweigh an early negative scan and prompt stroke-pathway management, vascular imaging and repeat MRI rather than reassurance from one study.",
    "v145_lar_07": "FEES adds direct bedside assessment of secretions, laryngeal sensation and response, fatigue over a meal, repeat examinations without radiation, and trials of real foods or positioning. It complements rather than replaces MBS because the oral phase, hyolaryngeal excursion and UES opening are obscured or not measured during the endoscopic white-out.",
    "v222_hn_lym_app": "If an excisional biopsy would require hazardous dissection beside major vessels, obtain image-guided core samples with enough tissue for histology, immunophenotyping, flow cytometry and molecular studies after coordinating with pathology. Excision remains useful when architecture is essential and can be obtained safely; a nondiagnostic FNA should not lead to repeated inadequate sampling.",
    "v222_hn_rts_app": "Aspiration-prevention surgery enters the discussion when chronic aspiration causes recurrent pneumonia, hospitalization or feeding dependence despite rehabilitation and correction of treatable stenosis, glottic insufficiency or reflux-related contributors, especially when the larynx is profoundly insensate or nonfunctional. Confirm absence of recurrent cancer and counsel explicitly about permanent airway, swallowing and voice consequences.",
}


def apply_daily_curriculum_quality_v371(items):
    stats = {"daily_pairs": 0, "recognition_prompts": 0}
    for item in items:
        key = (item.get("topic"), item.get("stage"))
        override = DAILY_OVERRIDES.get(key)
        if override:
            prompt, answer = override
            item["daily_prompt"] = prompt
            item["prompt"] = prompt
            item["answer"] = answer
            stats["daily_pairs"] += 1
        if item.get("stage") == "recognize" and item.get("topic") in RECOGNITION_PROMPTS:
            prompt = RECOGNITION_PROMPTS[item["topic"]]
            item["daily_prompt"] = prompt
            item["prompt"] = prompt
            stats["recognition_prompts"] += 1
    return stats


def install_daily_curriculum_quality_v371(data_module, app_module):
    original_get_items = data_module.get_adaptive_items_v120

    def get_adaptive_items_v371():
        items = original_get_items()
        apply_daily_curriculum_quality_v371(items)
        return items

    data_module.get_adaptive_items_v120 = get_adaptive_items_v371

    def adaptive_question_v371(item):
        return item.get("daily_prompt") or item.get("prompt") or ""

    app_module._adaptive_question = adaptive_question_v371

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

    sample = get_adaptive_items_v371()
    return {
        "item_stats": apply_daily_curriculum_quality_v371(sample),
        "curveball_answers_repaired": changed_curveballs,
    }
