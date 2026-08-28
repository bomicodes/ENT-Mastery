"""v25.5 — Laryngology / Voice / Swallowing deliberate ladder pass 6.

Adds five complete foundation -> application -> senior-decision ladders spanning
laryngeal dystonia/tremor, unilateral-paralysis reconstruction, irreversible airway
widening, and chronic cough/laryngeal hypersensitivity. Senior decisions emphasize
phenotype localization, reversibility, airway/voice/swallow tradeoffs, and avoiding
irreversible treatment before the mechanism is established.
"""
DOMAIN = "Laryngology / Voice / Swallowing"


def _q(qid, topic, stage, stem, choices, answer, explanation, reasons, pearl,
       curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic, "learning_stage": stage,
        "stem": stem, "choices": choices, "answer": answer,
        "explanation": explanation, "why_wrong": reasons,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette", "focus": focus,
        "ladder_reviewed": True, "_coverage_reviewed_v211": True,
    }


VIGNETTES_V255 = [
    _q("v255_lar_sd_fnd", "Spasmodic Dysphonia", "foundation",
       "A 46-year-old has a task-specific strained, strangled voice with intermittent breaks that are most prominent during voiced speech. Flexible examination shows no mass and normal vocal-fold mobility between phonatory breaks. What is the most likely diagnosis?",
       ["Adductor spasmodic dysphonia (laryngeal dystonia)", "Unilateral vocal fold paralysis", "Vocal fold polyp", "Acute bacterial laryngitis"], 0,
       "Adductor spasmodic dysphonia is a focal laryngeal dystonia characterized by involuntary hyperadductory voice breaks during susceptible speech tasks. The larynx can look structurally normal and move normally outside the dystonic task.",
       ["Correct. Task-specific strained breaks with otherwise preserved structure and mobility are classic for adductor laryngeal dystonia.", "Unilateral paralysis causes persistent motion impairment and glottic insufficiency rather than intermittent task-specific hyperadductory breaks.", "A polyp produces a structural vibratory abnormality and typically persistent dysphonia rather than stereotyped dystonic breaks.", "Acute laryngitis produces inflammatory dysphonia, not a chronic task-specific pattern with normal interval examination."],
       "Spasmodic dysphonia is a task-specific motor disorder; listening across different phonetic tasks is part of localization, not an optional flourish.",
       "How would predominantly voiceless-loaded sentence breaks change the dystonia phenotype you suspect?"),
    _q("v255_lar_sd_app", "Spasmodic Dysphonia", "application",
       "A patient with well-characterized adductor spasmodic dysphonia remains significantly limited despite behavioral strategies. Which treatment is the standard targeted procedural therapy?",
       ["Botulinum toxin injection into the overactive adductor complex, typically the thyroarytenoid/lateral cricoarytenoid system", "Permanent bilateral vocal fold stripping", "Empiric antibiotics", "Immediate total laryngectomy"], 0,
       "Botulinum toxin chemodenervation of the hyperactive adductor musculature is the established targeted treatment for adductor spasmodic dysphonia. Dosing is individualized to voice response, duration, breathiness, and swallowing side effects.",
       ["Correct. Targeted botulinum toxin reduces dystonic adductor overactivity while allowing dose adjustment over repeated treatment cycles.", "Stripping normal vocal-fold cover does not treat the neurologic mechanism and risks permanent scar.", "Antibiotics have no role in a focal dystonia without infection.", "Total laryngectomy is grossly disproportionate and destroys normal laryngeal function for a treatable focal motor disorder."],
       "Counsel before injection about the expected tradeoff: transient breathiness and sometimes mild liquid dysphagia may precede the best voice interval.",
       "How would poor pulmonary reserve or baseline aspiration risk change your initial dose strategy?", "senior_management"),
    _q("v255_lar_sd_snr", "Spasmodic Dysphonia", "senior_decision",
       "A patient labeled as having spasmodic dysphonia reports progressively poorer benefit despite escalating botulinum toxin doses. Examination now shows rhythmic laryngeal oscillation during sustained vowels in addition to irregular speech-task breaks. What is the best next senior-level step?",
       ["Re-phenotype the disorder for coexisting vocal tremor or another diagnosis before further dose escalation and tailor treatment to the observed motor pattern", "Continue increasing the same bilateral dose indefinitely without reassessment", "Excise both true vocal folds", "Assume every treatment failure is psychogenic"], 0,
       "Dystonia and tremor can coexist, and their treatment targets are not identical. When the response changes, the correct move is to revisit perceptual and endoscopic localization rather than reflexively escalating a treatment aimed at only one motor pattern.",
       ["Correct. Re-localizing the motor phenotype prevents unnecessary toxicity and allows treatment to address a tremor component or alternate diagnosis.", "Blind dose escalation can worsen breathiness or dysphagia without treating an unrecognized tremor component.", "Removing normal vocal folds does not address the neurologic mechanism and would cause severe irreversible morbidity.", "A changing treatment response should prompt diagnostic reassessment; it should not be dismissed as psychogenic without evidence."],
       "When botulinum toxin 'stops working,' first ask whether the target, phenotype, dose, or diagnosis has changed before assuming pharmacologic failure.",
       "Which perceptual tasks and anatomic levels would you deliberately examine to distinguish dystonic breaks from tremor?", "senior_management"),

    _q("v255_lar_tremor_fnd", "Vocal Tremor", "foundation",
       "A 68-year-old has rhythmic oscillation of pitch and loudness during sustained phonation. Flexible examination demonstrates regular oscillation involving the larynx and mild rhythmic motion of the palate. Which diagnosis best fits?",
       ["Vocal tremor", "Adductor spasmodic dysphonia alone", "Unilateral recurrent laryngeal nerve paralysis", "Vocal fold cyst"], 0,
       "Vocal tremor produces rhythmic, relatively regular oscillation and may involve multiple upper-airway subsites. Spasmodic dysphonia more often produces irregular task-specific breaks rather than a regular oscillatory pattern.",
       ["Correct. Regular rhythmic oscillation across sustained phonation and more than one anatomic level is characteristic of vocal tremor.", "Adductor spasmodic dysphonia produces irregular dystonic breaks and may coexist with tremor, but does not by itself explain the regular multilevel oscillation.", "RLN paralysis causes fixed or paretic motion asymmetry rather than rhythmic oscillation.", "A cyst is a focal structural lesion and does not create rhythmic palate-larynx movement."],
       "Rhythmicity and distribution are high-yield discriminators: tremor may extend beyond the true folds, whereas dystonia is more task-specific and irregular.",
       "What examination finding would make an isolated laryngeal injection less likely to control the patient's entire symptom burden?"),
    _q("v255_lar_tremor_app", "Vocal Tremor", "application",
       "A patient has disabling predominantly horizontal laryngeal vocal tremor with little baseline dysphagia. Which management principle is most appropriate?",
       ["Match therapy to tremor distribution; selected laryngeal-predominant tremor can be treated with targeted botulinum toxin while broader essential tremor may warrant neurologic/systemic management", "Treat every tremor with identical bilateral cordectomy", "Use antibiotics until the oscillation resolves", "Assume voice therapy alone eliminates all neurologic tremor"], 0,
       "Treatment depends on where the tremor is expressed and the patient's comorbidities. Targeted botulinum toxin can reduce selected laryngeal tremor patterns, while generalized essential tremor may require neurologic evaluation and systemic treatment options.",
       ["Correct. Phenotype and anatomic distribution should drive treatment rather than a one-size-fits-all laryngeal procedure.", "Cordectomy is destructive, does not treat the neurologic generator, and creates major voice/airway morbidity.", "Tremor is not an infectious process and does not respond to antibiotics.", "Behavioral therapy can improve compensatory technique but does not reliably abolish the underlying neurologic oscillation."],
       "Do not treat the word 'tremor'; treat the patient's dominant tremor axis, distribution, disability, and tolerance for treatment side effects.",
       "How would prominent vertical global-laryngeal movement alter your expectations for thyroarytenoid-directed botulinum toxin?", "senior_management"),
    _q("v255_lar_tremor_snr", "Vocal Tremor", "senior_decision",
       "An older patient with multilevel vocal tremor also has baseline liquid dysphagia and frailty. The patient requests aggressive botulinum toxin because the voice is socially disabling. What is the best senior-level approach?",
       ["Map the tremor distribution, establish functional priorities, and use conservative targeted treatment or multidisciplinary alternatives that explicitly account for swallowing reserve", "Give the largest bilateral laryngeal dose immediately because voice is the only relevant endpoint", "Perform irreversible airway-widening surgery", "Withhold all treatment solely because the patient is older"], 0,
       "Botulinum toxin can trade stronger tremor suppression for breathiness and dysphagia. In a patient with limited swallowing reserve, treatment should be anatomically targeted and conservatively titrated, with neurology and voice/swallow expertise used when multilevel disease is present.",
       ["Correct. Senior management balances voice benefit against aspiration risk and treats the observed distribution rather than maximizing dose.", "Large empiric bilateral dosing can worsen glottic competence and swallowing without guaranteeing control of multilevel tremor.", "Airway-widening surgery treats bilateral immobility, not vocal tremor.", "Chronologic age alone is not a reason to deny treatment; physiologic reserve and patient goals should guide selection."],
       "The best tremor response is not automatically the best patient outcome if the price is clinically important dysphagia.",
       "How would you define a successful first treatment cycle when complete tremor elimination is unrealistic?", "senior_management"),

    _q("v255_lar_aa_reinn_fnd", "Arytenoid Adduction / Reinnervation", "foundation",
       "A patient with chronic unilateral vocal fold paralysis has a large posterior glottic gap and vertical height mismatch despite otherwise favorable vocal-fold bulk. Which operation most directly addresses arytenoid position and posterior closure?",
       ["Arytenoid adduction", "Cricopharyngeal myotomy", "Posterior cordotomy", "Septoplasty"], 0,
       "Arytenoid adduction rotates the arytenoid to improve vocal-process position, posterior glottic closure, and vertical alignment. It is often considered with medialization thyroplasty when posterior gap or height mismatch is a major component of insufficiency.",
       ["Correct. Arytenoid adduction specifically targets posterior arytenoid geometry that simple anterior medialization may not fully correct.", "Cricopharyngeal myotomy treats selected upper-esophageal sphincter dysfunction and does not correct arytenoid position.", "Posterior cordotomy enlarges the glottic airway and would worsen insufficiency in unilateral paralysis.", "Septoplasty has no effect on laryngeal closure."],
       "Think geometry: thyroplasty medializes the fold; arytenoid adduction is especially useful when the posterior gap or vertical level remains wrong.",
       "What intraoperative voice or endoscopic finding would suggest that medialization alone has not corrected the relevant glottic geometry?"),
    _q("v255_lar_aa_reinn_app", "Arytenoid Adduction / Reinnervation", "application",
       "A young adult has permanent unilateral recurrent laryngeal nerve paralysis, good overall health, and a strong desire for durable restoration of vocal-fold tone. Which statement about ansa cervicalis-to-RLN reinnervation is most accurate?",
       ["It can restore tone and bulk over months but does not reliably restore normal purposeful abduction, so temporary augmentation may be used while waiting for reinnervation", "It produces immediate normal vocal-fold motion in the recovery room", "It is designed to enlarge the posterior airway in bilateral immobility", "It requires removal of the arytenoid cartilage"], 0,
       "Ansa-to-RLN reinnervation provides neural input that can improve long-term tone, bulk, and position, but clinical benefit develops over months and normal coordinated mobility is not expected. Temporary injection can bridge the delayed effect in selected patients.",
       ["Correct. Reinnervation is a delayed, durable tone-restoration strategy rather than an immediate motion-restoration procedure.", "Axonal regeneration takes time; immediate normal motion is not the expected mechanism or endpoint.", "Posterior airway enlargement is the purpose of procedures such as cordotomy/arytenoidectomy, not unilateral reinnervation.", "Arytenoid removal is not required for ansa-to-RLN reinnervation."],
       "Reinnervation changes the muscle's long-term biologic state; it is not an instant mechanical medialization.",
       "How would the need for immediate aspiration control influence whether you add temporary injection or framework surgery?", "OR_prep"),
    _q("v255_lar_aa_reinn_snr", "Arytenoid Adduction / Reinnervation", "senior_decision",
       "A 32-year-old with established unilateral paralysis has severe dysphonia, a large posterior gap with vertical height mismatch, and no realistic expectation of spontaneous neural recovery. The patient needs near-term voice improvement but also values durable long-term tone. What is the best planning principle?",
       ["Choose and combine procedures based on glottic geometry and timing: arytenoid adduction/framework medialization can provide immediate mechanical correction, while reinnervation may add delayed durable tone in an appropriate patient", "Use reinnervation alone and promise immediate normal motion", "Perform posterior cordotomy to widen the glottis", "Delay all treatment indefinitely because no single operation solves every dimension"], 0,
       "Permanent unilateral paralysis may require more than one mechanism of correction. Framework/arytenoid procedures address immediate position and closure, whereas reinnervation provides delayed biologic tone; procedure selection should reflect age, chronicity, posterior gap, height mismatch, aspiration, and urgency of functional recovery.",
       ["Correct. Senior planning separates immediate mechanical goals from delayed reinnervation goals and matches each procedure to the actual glottic deficit.", "Reinnervation does not provide immediate benefit or reliably restore purposeful normal motion.", "Posterior cordotomy worsens glottic insufficiency and is used for airway compromise from bilateral immobility.", "The presence of tradeoffs calls for individualized planning, not therapeutic paralysis when the deficit is functionally severe."],
       "Do not ask which unilateral-paralysis operation is 'best' in isolation; ask which deficit—bulk, position, posterior gap, height, timing, aspiration—still needs correction.",
       "How would advanced age, poor donor-nerve quality, or a small anterior gap change the relative value of reinnervation versus framework surgery?", "senior_management"),

    _q("v255_lar_cordotomy_fnd", "Posterior Cordotomy / Arytenoidectomy", "foundation",
       "A patient with chronic bilateral vocal fold immobility has exertional stridor but acceptable swallowing. Before an irreversible posterior cordotomy or arytenoidectomy, which distinction is essential?",
       ["Determine whether the immobility is neurogenic paralysis or mechanical posterior glottic fixation, using the history and appropriate laryngeal evaluation including operative palpation when needed", "Assume all bilateral immobility is recurrent laryngeal nerve paralysis", "Skip airway assessment because voice is the only outcome that matters", "Perform bilateral complete cordectomy as the diagnostic test"], 0,
       "Bilateral immobility can result from neurogenic paralysis or mechanical fixation such as posterior glottic stenosis/cricoarytenoid ankylosis. The etiology affects counseling and treatment, and irreversible tissue sacrifice should not precede adequate localization.",
       ["Correct. Mechanical fixation and neurogenic paralysis can look similar on office examination but may require different treatment strategies.", "Assuming a neural cause can miss posterior glottic scar or joint fixation.", "Airway adequacy is the central indication for glottic-widening surgery and must be assessed alongside voice and swallow.", "Destructive surgery should not be used as a diagnostic maneuver when the mechanism can be evaluated more safely."],
       "Never trade away voice and glottic competence for airway until you know why the folds are immobile and what reversible options remain.",
       "What does direct arytenoid palpation under anesthesia add when office motion examination cannot distinguish paralysis from fixation?"),
    _q("v255_lar_cordotomy_app", "Posterior Cordotomy / Arytenoidectomy", "application",
       "A patient with confirmed chronic bilateral neurogenic vocal fold paralysis wishes to avoid long-term tracheostomy and accepts a weaker voice in exchange for a larger airway. What is the core principle of posterior cordotomy/arytenoidectomy?",
       ["Enlarge the posterior glottic airway by removing or lateralizing selected tissue, while deliberately balancing airway gain against irreversible voice and swallowing costs", "Restore normal bilateral abduction by regenerating both recurrent laryngeal nerves immediately", "Tighten the posterior glottis to improve airway", "Treat the disorder solely with reflux medication"], 0,
       "Posterior cordotomy and partial arytenoidectomy are static airway-enlarging procedures. They can improve ventilation and facilitate decannulation in selected patients, but the larger glottic aperture can worsen voice and sometimes swallowing; restenosis from scar or granulation can also occur.",
       ["Correct. These procedures intentionally exchange some phonatory closure for airway caliber and require explicit functional counseling.", "They do not immediately restore neural abduction or normal dynamic motion.", "Tightening the posterior glottis would reduce airway caliber and worsen the indication being treated.", "Reflux treatment does not reverse fixed bilateral neurogenic immobility with clinically important airway limitation."],
       "For bilateral immobility, airway improvement, voice preservation, and aspiration protection pull in different directions; there is no free enlargement of the glottis.",
       "Why might a staged unilateral procedure be preferable to aggressive bilateral tissue removal?", "OR_prep"),
    _q("v255_lar_cordotomy_snr", "Posterior Cordotomy / Arytenoidectomy", "senior_decision",
       "A patient presents with severe stridor from newly recognized bilateral vocal fold immobility. The cause and likelihood of recovery are not yet established. What is the best senior-level strategy regarding irreversible glottic-widening surgery?",
       ["Secure the airway with the least destructive appropriate strategy and complete etiologic/recovery assessment before committing to irreversible posterior glottic tissue loss unless circumstances clearly require otherwise", "Perform maximal bilateral cordotomy and arytenoidectomy immediately before defining the cause", "Observe severe stridor at home until spontaneous recovery occurs", "Perform medialization thyroplasty on both sides"], 0,
       "When recovery potential and mechanism are uncertain, emergency airway safety comes first, but definitive irreversible widening can often wait until localization and prognosis are clearer. Tracheostomy or other temporizing airway management may preserve future options when clinically appropriate.",
       ["Correct. A reversible airway bridge preserves voice and reconstructive options while the cause and neural recovery potential are established.", "Maximal irreversible tissue sacrifice can create avoidable permanent voice/swallow morbidity if recovery later occurs or the mechanism proves mechanically correctable.", "Severe stridor is an airway emergency and is unsafe for outpatient observation without stabilization.", "Bilateral medialization narrows the airway and is the opposite of what severe bilateral immobility requires."],
       "In an unstable airway, 'do something now' does not mean 'do the most irreversible thing now.' Stabilize first, then make the definitive tradeoff with better information.",
       "Which clinical factors would make you move from a temporary airway strategy to definitive posterior glottic widening?", "senior_management"),

    _q("v255_lar_cough_fnd", "Chronic Cough / Laryngeal Hypersensitivity", "foundation",
       "A patient has cough for many months despite an appropriate evaluation and treatment of common pulmonary, medication-related, nasal, and reflux-related contributors. Laryngoscopy shows no concerning structural lesion. The cough is triggered by talking, odors, and temperature change and is preceded by a throat tickle. Which concept best fits this phenotype?",
       ["Chronic refractory cough with laryngeal hypersensitivity", "Acute bacterial epiglottitis", "Fixed bilateral vocal fold paralysis", "Untreated invasive laryngeal cancer by definition"], 0,
       "A sensory-hypersensitivity/neurogenic cough phenotype often features stereotyped non-tussive triggers, an urge-to-cough sensation, and persistence after appropriate evaluation and treatment of common causes. It remains a diagnosis made in context rather than a shortcut around red-flag evaluation.",
       ["Correct. Triggered cough with a sensory prodrome after appropriate exclusion/treatment of common causes is typical of laryngeal hypersensitivity/chronic refractory cough.", "Epiglottitis is an acute toxic airway illness rather than a months-long trigger-sensitive cough syndrome.", "Bilateral paralysis produces airway/voice findings and visible motion impairment, not this isolated sensory-triggered pattern.", "Cancer must be considered when red flags or lesions are present, but chronic cough without a lesion is not cancer by definition."],
       "Do not label chronic cough 'neurogenic' before doing enough evaluation to know what you are calling refractory.",
       "Which red flags—hemoptysis, weight loss, progressive dysphagia, smoking history, abnormal imaging, or focal laryngeal findings—would reopen the structural workup?"),
    _q("v255_lar_cough_app", "Chronic Cough / Laryngeal Hypersensitivity", "application",
       "A patient has chronic refractory cough with a convincing laryngeal hypersensitivity phenotype and no untreated red-flag cause. Which treatment strategy is appropriate?",
       ["Behavioral cough-suppression/laryngeal control therapy with speech-language pathology, with selected neuromodulator therapy when needed and appropriate", "Repeated antibiotics despite no infection", "Permanent total voice rest", "Immediate laryngectomy"], 0,
       "Behavioral cough suppression and laryngeal control therapy are evidence-based components of management for refractory cough. Selected patients may also benefit from neuromodulatory treatment after individualized discussion of adverse effects and comorbidities.",
       ["Correct. Therapy targets the hypersensitive cough reflex and maladaptive laryngeal responses without assuming an infectious or structural mechanism.", "Antibiotics should not be repeated when there is no evidence of bacterial infection.", "Permanent voice rest does not treat the sensory-reflex mechanism and is functionally harmful.", "Laryngectomy is not a treatment for an otherwise structurally normal hypersensitivity syndrome."],
       "Cough suppression therapy is active retraining—not reassurance alone—and works best when the patient understands the trigger/urge/response cycle.",
       "How would sedation risk, fall risk, renal function, or concurrent neuropathic medications affect neuromodulator selection?", "senior_management"),
    _q("v255_lar_cough_snr", "Chronic Cough / Laryngeal Hypersensitivity", "senior_decision",
       "A patient referred for 'neurogenic cough' has failed empiric proton-pump inhibitor therapy and asks for a procedural treatment immediately. Review reveals new hemoptysis and a 30-pack-year smoking history, and the prior laryngeal examination was limited. What is the best next step?",
       ["Reopen the diagnostic evaluation and obtain adequate airway/laryngeal assessment for structural disease before escalating hypersensitivity-directed therapy", "Assume failed reflux therapy proves a neurogenic mechanism", "Start indefinite antibiotics without examination", "Proceed directly to an irreversible laryngeal operation"], 0,
       "Chronic refractory cough is a diagnosis reached after appropriate assessment, not after failure of one empiric therapy. New hemoptysis and substantial tobacco exposure are red flags that should redirect attention to structural pulmonary and upper-airway disease before symptom-directed neuromodulatory or procedural treatment.",
       ["Correct. New red flags supersede the prior working label and require renewed diagnostic evaluation.", "Failure of proton-pump inhibition does not establish a sensory neuropathy and cannot exclude malignancy or pulmonary disease.", "Antibiotics without evidence of infection neither evaluate hemoptysis nor address the relevant cancer risk.", "Irreversible treatment before adequate structural evaluation risks delaying diagnosis and causing unnecessary morbidity."],
       "A senior clinician must be willing to discard a convenient prior label when the phenotype changes or a red flag appears.",
       "If the renewed workup is reassuring, how would you sequence behavioral therapy, medication trials, and any specialist procedural options while defining measurable response?", "senior_management"),
]


def apply_learning_ladders_v255(challenges, concept_id_fn):
    """Append only missing v25.5 cases and attach exact canonical concept IDs."""
    existing = {str(q.get("id")) for q in challenges}
    added = 0
    for source in VIGNETTES_V255:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["choices"] = list(source.get("choices") or [])
        q["why_wrong"] = list(source.get("why_wrong") or [])
        q["concept_id"] = concept_id_fn(DOMAIN, q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1
    return added
