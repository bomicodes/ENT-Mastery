"""
v13.5 - Cross-domain vignette depth pass.

Adds high-yield, management-discriminating cases across all nine domains using
only canonical topic names already known to the live curriculum. The runtime
validator in recognize_stage_v127.py refuses any orphaned target.
"""

VIGNETTES_V135 = [
    # Otology / Neurotology
    {
        "id": "v135_oto_01", "domain": "Otology / Neurotology", "topic": "Sudden Sensorineural Hearing Loss",
        "stem": "A 58-year-old wakes with sudden unilateral hearing loss and tinnitus. Otoscopy is normal and bedside tuning-fork testing suggests sensorineural loss. What is the best next step?",
        "choices": ["Observe for 2 weeks before obtaining an audiogram", "Urgent audiometry and prompt corticosteroid treatment when appropriate while evaluating for retrocochlear disease", "Empiric oral antibiotics only", "Immediate tympanomastoidectomy"],
        "answer": 1,
        "explanation": "SSNHL is an otologic urgency. Confirm the sensorineural deficit quickly with audiometry, begin time-sensitive steroid therapy when not contraindicated, and evaluate for retrocochlear pathology rather than delaying treatment.",
        "why_wrong": ["Treatment benefit is time-sensitive; a long observation delay is inappropriate.", "Correct.", "Normal otoscopy plus sensorineural tuning-fork findings do not support otitis media as the primary problem.", "There is no indication for mastoid surgery in idiopathic SSNHL."],
        "board_pearl": "Do not let a normal ear exam create false reassurance in sudden hearing loss; distinguish conductive from sensorineural loss immediately.",
        "curveball": "The patient presents 3 weeks later with minimal recovery after oral steroids. What salvage option should be discussed?",
        "tier": "Curated board/call", "mode": "Vignette"
    },
    {
        "id": "v135_oto_02", "domain": "Otology / Neurotology", "topic": "Temporal Bone Fracture",
        "stem": "After blunt head trauma, a patient has hemotympanum and immediate complete facial paralysis. CT shows a temporal bone fracture. Which additional finding most strongly changes operative urgency?",
        "choices": ["Mild conductive hearing loss from hemotympanum", "Evidence of facial nerve transection or severe degeneration with a surgically accessible lesion", "Transient vertigo lasting seconds", "A small external auditory canal abrasion"],
        "answer": 1,
        "explanation": "Immediate complete paralysis raises concern for direct facial nerve injury. Surgical exploration/decompression is considered when testing and imaging support severe degeneration, transection, or impingement rather than simple edema.",
        "why_wrong": ["Conductive loss from hemotympanum is common and usually observed initially.", "Correct.", "Brief vertigo alone does not define a facial nerve surgical indication.", "A minor canal abrasion does not drive facial nerve management."],
        "board_pearl": "In temporal bone trauma, document facial nerve function early—before swelling, sedation, or delayed paralysis obscures whether the deficit was immediate or delayed.",
        "curveball": "How does delayed-onset incomplete facial weakness change the presumed mechanism and initial management?",
        "tier": "Curated board/OR", "mode": "Vignette"
    },
    {
        "id": "v135_oto_03", "domain": "Otology / Neurotology", "topic": "Chronic Otitis Media / Cholesteatoma",
        "stem": "A patient with chronic foul otorrhea has an attic retraction pocket containing keratin debris and progressive conductive hearing loss. CT shows scutum erosion. What management principle is most appropriate?",
        "choices": ["Long-term drops alone are definitive", "Surgical eradication of cholesteatoma with a plan tailored to extent, anatomy, hearing, and follow-up reliability", "Observe unless facial paralysis develops", "Treat with systemic steroids"],
        "answer": 1,
        "explanation": "Cholesteatoma is locally destructive keratinizing disease. Medical therapy can control infection temporarily but does not eradicate the matrix; surgery is generally required to create a safe ear.",
        "why_wrong": ["Drops can suppress infection but cannot remove the cholesteatoma matrix.", "Correct.", "Waiting for a complication sacrifices the goal of preventing labyrinthine, facial nerve, and intracranial injury.", "Steroids do not treat cholesteatoma."],
        "board_pearl": "The primary endpoint of cholesteatoma surgery is a safe, dry ear; hearing reconstruction is secondary to complete disease control.",
        "curveball": "The only-hearing ear is involved. How does that change counseling and operative planning?",
        "tier": "Curated board/OR", "mode": "Vignette"
    },

    # Rhinology / Allergy / Skull Base
    {
        "id": "v135_rhino_01", "domain": "Rhinology / Allergy / Skull Base", "topic": "Invasive Fungal Rhinosinusitis",
        "stem": "A neutropenic patient develops facial pain, fever, black nasal eschar, and new ophthalmoplegia. What is the best immediate management strategy?",
        "choices": ["Outpatient oral antibiotics and recheck in 48 hours", "Urgent biopsy/debridement, systemic antifungal therapy, reversal of immunosuppression when feasible, and multidisciplinary orbital/skull-base assessment", "Intranasal steroid escalation", "Observe until cultures finalize"],
        "answer": 1,
        "explanation": "Acute invasive fungal rhinosinusitis is rapidly angioinvasive and can progress to orbital and intracranial disease. Diagnosis and treatment must proceed in parallel with urgent tissue diagnosis, debridement, systemic antifungals, and optimization of immune status.",
        "why_wrong": ["Delay can be fatal.", "Correct.", "Steroids worsen the underlying risk context and do not treat angioinvasive fungal disease.", "Treatment should not wait for final cultures when the clinical syndrome is strongly suspicious."],
        "board_pearl": "In an immunocompromised patient, facial pain plus cranial neuropathy or devitalized mucosa is invasive fungal disease until proven otherwise.",
        "curveball": "Frozen section is negative but suspicion remains high. What should you do next?",
        "tier": "Curated board/call", "mode": "Vignette"
    },
    {
        "id": "v135_rhino_02", "domain": "Rhinology / Allergy / Skull Base", "topic": "Orbital Complications of Sinusitis",
        "stem": "A child with acute sinusitis develops proptosis, painful restricted extraocular movements, and decreased visual acuity. CT shows a medial subperiosteal orbital abscess. Which feature most strongly favors urgent surgical drainage?",
        "choices": ["Age under 10 alone", "Visual compromise or progressive ophthalmologic deficit despite medical therapy", "Mild eyelid edema only", "A normal afferent pupillary response"],
        "answer": 1,
        "explanation": "Vision-threatening findings and clinical progression are major indications for urgent drainage of orbital abscess in addition to intravenous antibiotics and sinus source control.",
        "why_wrong": ["Age influences pathogen profile and observation thresholds but is not by itself an operative indication.", "Correct.", "Preseptal edema alone is not enough to justify orbital surgery.", "A normal pupillary response is reassuring rather than an indication for urgent drainage."],
        "board_pearl": "In orbital sinus complications, serial vision exams matter as much as the CT. A deteriorating eye is an emergency even if imaging looks modest.",
        "curveball": "What bedside ophthalmologic findings should be documented repeatedly overnight?",
        "tier": "Curated board/call", "mode": "Vignette"
    },
    {
        "id": "v135_rhino_03", "domain": "Rhinology / Allergy / Skull Base", "topic": "Epistaxis Surgical Control",
        "stem": "A patient has persistent posterior epistaxis despite appropriate resuscitation, topical therapy, cautery attempts, and packing. Bleeding recurs immediately when packing is removed. What is the best next definitive strategy?",
        "choices": ["Repeated blind packing indefinitely", "Endoscopic surgical control of the sphenopalatine arterial territory, with embolization considered in selected cases", "Septoplasty alone", "Systemic steroids"],
        "answer": 1,
        "explanation": "Refractory posterior epistaxis should move toward definitive arterial control rather than repeated traumatic packing. Endoscopic sphenopalatine artery ligation/cauterization is a standard operative strategy; embolization is an alternative in selected patients.",
        "why_wrong": ["Repeated packing increases morbidity and delays definitive control.", "Correct.", "Septoplasty does not treat the arterial source unless required for access.", "Steroids are not definitive therapy for refractory posterior arterial bleeding."],
        "board_pearl": "When epistaxis keeps recurring after adequate packing, change the strategy—do not simply repeat the same temporizing maneuver.",
        "curveball": "The patient has severe carotid atherosclerosis and prior external carotid embolization. How does that affect the risk discussion?",
        "tier": "Curated board/OR", "mode": "Vignette"
    },

    # Head & Neck Oncology
    {
        "id": "v135_hn_01", "domain": "Head & Neck Oncology", "topic": "Unknown Primary with Cervical Metastasis",
        "stem": "A 52-year-old nonsmoker presents with a cystic level II neck node. FNA shows p16-positive squamous cell carcinoma and office examination does not reveal a primary. What is the best next diagnostic framework?",
        "choices": ["Assume branchial cleft cyst and observe", "Complete directed mucosal evaluation with appropriate imaging and operative examination, including attention to the palatine and lingual tonsils", "Immediate radical neck dissection without further workup", "Treat empirically as thyroid cancer"],
        "answer": 1,
        "explanation": "An adult cystic neck mass can represent HPV-associated oropharyngeal SCC. The workup seeks the occult primary with imaging and directed examination, often including tonsillar evaluation, before definitive treatment planning.",
        "why_wrong": ["Adult cystic neck masses must be considered malignant until proven otherwise.", "Correct.", "Definitive neck surgery before completing primary-site workup can compromise treatment planning.", "The pathology is squamous, not thyroid-derived."],
        "board_pearl": "A cystic level II node in an adult is metastatic HPV-associated OPSCC until proven otherwise—not a branchial cyst by default.",
        "curveball": "No primary is found after complete workup. What factors determine whether treatment fields can be safely narrowed?",
        "tier": "Curated board", "mode": "Vignette"
    },
    {
        "id": "v135_hn_02", "domain": "Head & Neck Oncology", "topic": "Salvage Surgery After Radiation / Chemoradiation",
        "stem": "A patient develops biopsy-proven isolated laryngeal recurrence 18 months after definitive chemoradiation. Imaging shows resectable disease and no distant metastases. What is the key management principle?",
        "choices": ["Re-irradiation is always preferred over surgery", "Evaluate for salvage surgery while counseling about higher wound, fistula, and swallowing complication risks in the irradiated field", "Observation until airway compromise occurs", "Systemic therapy is mandatory before considering local salvage"],
        "answer": 1,
        "explanation": "For resectable isolated locoregional recurrence after prior radiation, salvage surgery can offer the best chance of durable control but carries substantially increased wound and fistula morbidity.",
        "why_wrong": ["Re-irradiation can be appropriate in selected cases but is not automatically preferred to resection.", "Correct.", "Delay can sacrifice resectability.", "Systemic therapy is not mandatory before a potentially curative local salvage operation."],
        "board_pearl": "Salvage oncologic surgery is not merely the original operation done later; prior radiation fundamentally changes healing, vascularity, reconstruction, and complication risk.",
        "curveball": "The pharyngeal closure will be under tension in a heavily irradiated field. What reconstructive principle lowers fistula risk?",
        "tier": "Curated board/OR", "mode": "Vignette"
    },
    {
        "id": "v135_hn_03", "domain": "Head & Neck Oncology", "topic": "Cutaneous Squamous Cell Carcinoma of the Head & Neck",
        "stem": "A patient with a large recurrent temple cSCC has numbness in the V2 distribution and MRI shows enhancement tracking proximally along the infraorbital nerve. What finding most changes staging and treatment planning?",
        "choices": ["Tumor color", "Clinical/radiographic perineural spread along a named nerve toward the skull base", "Mild actinic damage nearby", "A remote history of basal cell carcinoma"],
        "answer": 1,
        "explanation": "Named-nerve perineural spread is a high-risk feature that changes imaging, surgical extent, skull-base considerations, and adjuvant radiation planning.",
        "why_wrong": ["Color is not a major staging determinant.", "Correct.", "Background actinic change does not carry the same prognostic impact.", "A remote unrelated skin cancer does not define the extent of the current lesion."],
        "board_pearl": "New cranial neuropathy in head-and-neck cSCC is perineural spread until proven otherwise; image the nerve to its central endpoint.",
        "curveball": "Symptoms extend to the foramen rotundum. How does proximal extent affect operability and adjuvant planning?",
        "tier": "Curated board/OR", "mode": "Vignette"
    },

    # Thyroid / Parathyroid / Salivary
    {
        "id": "v135_tps_01", "domain": "Thyroid / Parathyroid / Salivary", "topic": "Recurrent Laryngeal Nerve Injury During Thyroidectomy",
        "stem": "During total thyroidectomy, the nerve monitoring signal is lost on the first side after a difficult dissection. The contralateral lobe remains. What is the safest general principle?",
        "choices": ["Always complete the opposite side immediately", "Verify the loss of signal and strongly consider staging the contralateral surgery to avoid bilateral vocal fold paralysis", "Ignore monitoring because it never affects management", "Perform tracheotomy before evaluating the cause"],
        "answer": 1,
        "explanation": "A true loss of signal on the first side raises the stakes of proceeding to the opposite RLN. After troubleshooting the system and confirming the event, staged surgery may prevent bilateral vocal fold immobility.",
        "why_wrong": ["Proceeding automatically can convert a unilateral nerve injury into a bilateral airway problem.", "Correct.", "Monitoring does not replace visualization, but a verified loss can appropriately change the operative plan.", "Tracheotomy is not automatic before confirming the situation."],
        "board_pearl": "The value of nerve monitoring is not only identification; a verified first-side signal loss can change whether you safely proceed to the second side.",
        "curveball": "What technical checks should be performed before declaring a true loss of signal?",
        "tier": "Curated OR", "mode": "Vignette"
    },
    {
        "id": "v135_tps_02", "domain": "Thyroid / Parathyroid / Salivary", "topic": "First-Bite Syndrome",
        "stem": "Months after parapharyngeal space tumor resection, a patient reports severe ipsilateral parotid-region pain with the first bite of each meal that rapidly fades with continued chewing. What is the most likely diagnosis?",
        "choices": ["Sialolithiasis", "First-bite syndrome", "Frey syndrome", "Recurrent deep neck infection"],
        "answer": 1,
        "explanation": "The highly stereotyped first-bite pain that diminishes with subsequent bites after sympathetic-chain/parapharyngeal surgery is classic for first-bite syndrome.",
        "why_wrong": ["Obstruction causes meal-related swelling/pain throughout salivary stimulation rather than a first-bite-only pattern.", "Correct.", "Frey syndrome is gustatory sweating/flushing, not parotid-region pain.", "Infection would not produce this reproducible meal-triggered pattern."],
        "board_pearl": "First-bite syndrome and Frey syndrome are both gustatory postoperative syndromes, but one is pain and the other is sweating/flushing.",
        "curveball": "What nonoperative treatment can be considered if symptoms remain disabling?",
        "tier": "Curated board", "mode": "Vignette"
    },
    {
        "id": "v135_tps_03", "domain": "Thyroid / Parathyroid / Salivary", "topic": "Frey Syndrome",
        "stem": "A patient develops unilateral preauricular sweating and flushing whenever eating, one year after parotidectomy. What mechanism best explains the symptoms?",
        "choices": ["Parotid duct obstruction", "Aberrant parasympathetic reinnervation of cutaneous sweat glands and vessels", "Facial nerve neuroma", "Residual tumor secreting catecholamines"],
        "answer": 1,
        "explanation": "Frey syndrome results from aberrant regeneration of postganglionic parasympathetic fibers into cutaneous sympathetic targets after parotid surgery.",
        "why_wrong": ["Duct obstruction causes salivary pain/swelling, not gustatory sweating.", "Correct.", "A facial neuroma causes neural symptoms, not this autonomic pattern.", "The syndrome is postoperative aberrant reinnervation, not endocrine secretion."],
        "board_pearl": "Minor starch-iodine testing can map the symptomatic skin; botulinum toxin is highly effective when symptoms are bothersome.",
        "curveball": "What intraoperative reconstructive maneuver can reduce the incidence when planning parotidectomy?",
        "tier": "Curated board/OR", "mode": "Vignette"
    },

    # Pediatric Otolaryngology
    {
        "id": "v135_ped_01", "domain": "Pediatric Otolaryngology", "topic": "Pediatric Airway Foreign Body",
        "stem": "A previously healthy 2-year-old has sudden coughing and unilateral wheeze after eating peanuts. Chest radiograph is normal. What is the best next step?",
        "choices": ["Discharge because the radiograph is normal", "Proceed with airway foreign-body evaluation, typically rigid bronchoscopy when clinical suspicion is high", "Treat with inhaled steroids for presumed asthma", "Order only a neck ultrasound"],
        "answer": 1,
        "explanation": "A normal chest radiograph does not exclude an aspirated foreign body. A convincing choking history with focal findings warrants operative airway evaluation.",
        "why_wrong": ["Radiographs can be normal with radiolucent objects.", "Correct.", "Sudden onset after choking is not typical asthma.", "Ultrasound does not exclude a tracheobronchial foreign body."],
        "board_pearl": "History beats x-ray in pediatric aspiration. Sudden choking plus asymmetric breath sounds deserves bronchoscopy even with normal imaging.",
        "curveball": "The child becomes completely obstructed during induction. What is the immediate airway strategy?",
        "tier": "Curated board/call/OR", "mode": "Vignette"
    },
    {
        "id": "v135_ped_02", "domain": "Pediatric Otolaryngology", "topic": "Pediatric Deep Neck Infection",
        "stem": "A 4-year-old with fever, torticollis, muffled voice, and limited neck extension has CT evidence of a retropharyngeal collection. Which feature most strongly favors operative drainage rather than antibiotics alone?",
        "choices": ["Small phlegmon in a clinically improving child", "Airway compromise, toxicity, large organized abscess, or failure to improve with appropriate IV antibiotics", "Age under 5 alone", "Mild rhinorrhea"],
        "answer": 1,
        "explanation": "Pediatric deep-neck infection management depends on airway status, toxicity, abscess organization/size, and response to antibiotics. Airway compromise or clinical failure pushes toward drainage.",
        "why_wrong": ["An improving phlegmon may be managed medically with close observation.", "Correct.", "Age alone is not an operative indication.", "Rhinorrhea does not determine drainage need."],
        "board_pearl": "In deep-neck infection, the airway decision comes before the abscess-size debate.",
        "curveball": "The child has drooling and worsening stridor. Where should the airway be secured and who should be present?",
        "tier": "Curated board/call", "mode": "Vignette"
    },
    {
        "id": "v135_ped_03", "domain": "Pediatric Otolaryngology", "topic": "AOM / OME / Tympanostomy Decisions",
        "stem": "A child with bilateral otitis media with effusion for 4 months has documented conductive hearing loss and speech-language delay risk. What is the best management principle?",
        "choices": ["Continue indefinite observation regardless of hearing", "Discuss tympanostomy tubes because persistent bilateral effusion plus hearing difficulty/developmental risk increases benefit", "Start chronic systemic antibiotics", "Adenoidectomy is mandatory in every preschool child"],
        "answer": 1,
        "explanation": "Persistent OME becomes more intervention-worthy when hearing difficulty or developmental risk is present. Tympanostomy tubes can improve middle-ear ventilation and hearing during the effusion period.",
        "why_wrong": ["Developmental risk and documented hearing loss make indefinite observation less appropriate.", "Correct.", "Chronic systemic antibiotics are not standard definitive therapy for persistent OME.", "Adenoidectomy is not mandatory for every young child receiving first tubes."],
        "board_pearl": "OME decisions are not based on duration alone—hearing status and developmental vulnerability matter.",
        "curveball": "How does management change for recurrent AOM if no effusion is present at the candidacy visit?",
        "tier": "Curated board", "mode": "Vignette"
    },

    # Laryngology / Voice / Swallowing
    {
        "id": "v135_lary_01", "domain": "Laryngology / Voice / Swallowing", "topic": "Bilateral Vocal Fold Immobility",
        "stem": "A patient develops inspiratory stridor immediately after total thyroidectomy. Flexible laryngoscopy shows both vocal folds near the midline with minimal abduction. What is the immediate priority?",
        "choices": ["Voice therapy", "Secure and stabilize the airway while determining whether the immobility is transient or permanent", "Inject both vocal folds medially", "Observe at home"],
        "answer": 1,
        "explanation": "Bilateral vocal fold immobility can produce a critically narrowed glottic airway. Airway stabilization comes before definitive voice or glottic-widening decisions.",
        "why_wrong": ["Voice therapy does not address acute airway obstruction.", "Correct.", "Further medialization would worsen the airway.", "Stridor after bilateral immobility requires monitored airway management."],
        "board_pearl": "Unilateral paralysis is usually a voice problem; bilateral paralysis is first an airway problem.",
        "curveball": "If recovery does not occur, what is the trade-off of posterior cordotomy or arytenoidectomy?",
        "tier": "Curated board/call/OR", "mode": "Vignette"
    },
    {
        "id": "v135_lary_02", "domain": "Laryngology / Voice / Swallowing", "topic": "Inducible Laryngeal Obstruction / PVFM",
        "stem": "A young athlete has episodic inspiratory dyspnea and throat tightness during exertion. Pulmonary testing is unrevealing and laryngoscopy during symptoms shows paradoxical inspiratory adduction. What is first-line management?",
        "choices": ["Tracheotomy", "Laryngeal control/respiratory retraining with trigger management", "Long-term systemic steroids", "Arytenoidectomy"],
        "answer": 1,
        "explanation": "ILO/PVFM is a functional, trigger-associated laryngeal closure disorder. Behavioral respiratory retraining and management of contributing triggers are first-line.",
        "why_wrong": ["Tracheotomy is not first-line for a functional episodic disorder.", "Correct.", "Systemic steroids do not treat the core mechanism.", "Destructive airway surgery is inappropriate for a reversible functional closure pattern."],
        "board_pearl": "Inspiratory noise, rapid onset/offset, and poor response to asthma therapy should prompt consideration of ILO rather than escalating bronchodilators indefinitely.",
        "curveball": "Why can a normal office laryngoscopy fail to exclude exercise-induced ILO?",
        "tier": "Curated board", "mode": "Vignette"
    },
    {
        "id": "v135_lary_03", "domain": "Laryngology / Voice / Swallowing", "topic": "Posterior Glottic Stenosis / Arytenoid Fixation",
        "stem": "A patient has persistent bilateral vocal fold immobility after prolonged intubation. Laryngeal EMG suggests preserved neural input, and direct palpation shows restricted arytenoid motion. What diagnosis is most likely?",
        "choices": ["Bilateral RLN transection", "Posterior glottic stenosis with mechanical arytenoid fixation", "Spasmodic dysphonia", "Vocal fold nodules"],
        "answer": 1,
        "explanation": "Prolonged intubation can scar the posterior commissure and cricoarytenoid joints, producing mechanical fixation that mimics bilateral paralysis. Preserved neural input plus reduced passive mobility supports PGS.",
        "why_wrong": ["Preserved EMG activity and mechanical fixation argue against pure bilateral denervation.", "Correct.", "Spasmodic dysphonia is task-specific phonatory dystonia, not fixed bilateral immobility.", "Nodules do not immobilize the arytenoids."],
        "board_pearl": "Bilateral immobility is a phenotype, not a diagnosis—distinguish neurogenic paralysis from mechanical fixation before choosing surgery.",
        "curveball": "What operative maneuvers can improve airway, and what voice/swallow trade-offs should be discussed?",
        "tier": "Curated board/OR", "mode": "Vignette"
    },

    # Facial Plastics / Trauma
    {
        "id": "v135_fprs_01", "domain": "Facial Plastics / Trauma", "topic": "ZMC / Orbital Trauma",
        "stem": "After ZMC trauma, a patient has diplopia, enophthalmos, and CT evidence of a large orbital floor defect with herniated orbital contents. What is the major operative goal?",
        "choices": ["Cosmetic malar projection only", "Restore orbital volume/support and release entrapped or displaced tissue while reconstructing the midface as indicated", "Nasal packing only", "Observe indefinitely regardless of symptoms"],
        "answer": 1,
        "explanation": "Orbital reconstruction aims to restore orbital volume and anatomy, address entrapment, and prevent persistent diplopia/enophthalmos while coordinating fixation of the ZMC framework when unstable.",
        "why_wrong": ["Orbital function and volume matter in addition to cheek contour.", "Correct.", "Packing does not reconstruct orbital support.", "Persistent functional deficits and large defects can warrant repair."],
        "board_pearl": "Before orbital fracture surgery, document vision, pupils, motility, globe position, and sensation—then repeat them postoperatively.",
        "curveball": "The patient develops sudden visual loss and proptosis after repair. What diagnosis must be treated immediately?",
        "tier": "Curated board/OR", "mode": "Vignette"
    },
    {
        "id": "v135_fprs_02", "domain": "Facial Plastics / Trauma", "topic": "Functional Nasal Obstruction",
        "stem": "A patient has persistent nasal obstruction despite adequate septoplasty. Modified Cottle maneuver markedly improves breathing and inspiration causes lateral wall collapse. What is the key next principle?",
        "choices": ["Repeat septoplasty regardless of findings", "Treat structural nasal valve collapse with appropriate lateral wall/internal valve support", "Use antibiotics", "A normal CT excludes a structural cause"],
        "answer": 1,
        "explanation": "Persistent obstruction with dynamic lateral wall collapse and improvement with valve support points to nasal valve dysfunction. Structural support, not simply more septal resection, is needed.",
        "why_wrong": ["The septum may already be adequate; repeating the same operation misses the valve problem.", "Correct.", "Antibiotics do not correct valve mechanics.", "Valve collapse is primarily a functional physical-exam diagnosis and may not be captured by CT."],
        "board_pearl": "Septum, turbinates, internal valve, and external valve are separate potential bottlenecks—identify which one actually limits airflow before operating.",
        "curveball": "Which grafts or suture techniques can support dynamic lateral wall collapse?",
        "tier": "Curated board/OR", "mode": "Vignette"
    },
    {
        "id": "v135_fprs_03", "domain": "Facial Plastics / Trauma", "topic": "Facial Nerve Reanimation",
        "stem": "A patient has complete facial paralysis after nerve sacrifice, and direct repair is impossible. The distal facial musculature remains viable. What principle guides dynamic reanimation?",
        "choices": ["Wait until muscle is irreversibly atrophic before planning", "Provide a new motor source to the native facial musculature or transfer functional muscle before prolonged denervation makes reinnervation ineffective", "Use filler alone to restore smile", "Static slings restore spontaneous dynamic movement"],
        "answer": 1,
        "explanation": "Dynamic reanimation depends on viable target muscle and timely motor reinnervation or functional muscle transfer. The longer complete denervation persists, the less useful native facial muscle becomes.",
        "why_wrong": ["Delay can eliminate the window for meaningful native muscle reinnervation.", "Correct.", "Filler changes contour, not motor function.", "Static slings improve resting position but do not recreate active smile."],
        "board_pearl": "Facial reanimation begins with two clocks: time since denervation and whether the native mimetic muscles remain viable.",
        "curveball": "How would your options differ after several years of complete denervation with severe muscle atrophy?",
        "tier": "Curated board/OR", "mode": "Vignette"
    },

    # Sleep Surgery
    {
        "id": "v135_sleep_01", "domain": "Sleep Surgery", "topic": "DISE",
        "stem": "A patient with CPAP-intolerant OSA is being considered for sleep surgery. What is the main value of drug-induced sleep endoscopy?",
        "choices": ["It replaces polysomnography", "It characterizes dynamic level and pattern of upper-airway collapse to improve procedure selection", "It measures daytime pulmonary function", "It determines thyroid hormone dose"],
        "answer": 1,
        "explanation": "DISE is a phenotyping tool for dynamic airway collapse under sedated sleep-like conditions. It complements rather than replaces PSG and can identify patterns that alter surgical candidacy or procedure choice.",
        "why_wrong": ["PSG still defines sleep-disordered breathing severity and physiology.", "Correct.", "DISE is not pulmonary function testing.", "It has no role in thyroid dosing."],
        "board_pearl": "DISE is useful when the operative question is 'where and how does this airway collapse?' rather than simply 'does the patient have OSA?'.",
        "curveball": "What collapse pattern is particularly important when considering hypoglossal nerve stimulation candidacy?",
        "tier": "Curated board/OR", "mode": "Vignette"
    },
    {
        "id": "v135_sleep_02", "domain": "Sleep Surgery", "topic": "Central Sleep Apnea / Treatment-Emergent CSA",
        "stem": "A patient with OSA starts PAP and obstructive events improve, but repeated central apneas emerge during titration. What is the best initial interpretation?",
        "choices": ["The study proves the patient never had OSA", "Consider treatment-emergent central sleep apnea and reassess contributing factors and persistence before escalating therapy", "Perform tonsillectomy immediately", "Ignore central events regardless of severity"],
        "answer": 1,
        "explanation": "Central events can emerge after relief of obstruction and may resolve over time in some patients. Management requires distinguishing transient treatment-emergent CSA from persistent central disease and evaluating contributing conditions.",
        "why_wrong": ["OSA and treatment-emergent CSA can coexist sequentially during PAP treatment.", "Correct.", "Upper-airway surgery does not directly treat central respiratory-control instability.", "Clinically significant central events require interpretation and follow-up."],
        "board_pearl": "Not every apnea after PAP is obstructive. Read the event type, effort channels, and treatment response rather than treating AHI as a single undifferentiated number.",
        "curveball": "Which cardiac comorbidity changes the safety discussion for some advanced PAP modes?",
        "tier": "Curated board", "mode": "Vignette"
    },
    {
        "id": "v135_sleep_03", "domain": "Sleep Surgery", "topic": "Oral Appliance Therapy",
        "stem": "A patient with mild-to-moderate OSA cannot tolerate CPAP and has favorable dentition and mandibular anatomy. Which alternative is most appropriate to discuss?",
        "choices": ["Mandibular advancement oral appliance fitted and followed by a qualified dental/sleep team", "Chronic sedative use", "No therapy because CPAP failed", "Routine tracheotomy"],
        "answer": 0,
        "explanation": "Mandibular advancement devices are an established non-PAP option for selected patients, especially those with mild-to-moderate disease or PAP intolerance, with follow-up needed to assess efficacy and dental effects.",
        "why_wrong": ["Correct.", "Sedatives can worsen airway collapsibility and are not definitive OSA therapy.", "PAP intolerance does not eliminate other treatment options.", "Tracheotomy is not routine therapy for uncomplicated mild-to-moderate OSA."],
        "board_pearl": "For every OSA treatment, distinguish physiologic efficacy from real-world effectiveness—the best therapy is one the patient can actually use and that controls disease.",
        "curveball": "What follow-up test confirms that symptoms improving with the appliance actually corresponds to adequate OSA control?",
        "tier": "Curated board", "mode": "Vignette"
    },

    # General ENT / Emergencies
    {
        "id": "v135_gen_01", "domain": "General ENT / Emergencies", "topic": "Postoperative Neck Hematoma",
        "stem": "Two hours after thyroidectomy, a patient develops rapidly increasing neck pressure, swelling, stridor, and difficulty handling secretions. What is the immediate priority?",
        "choices": ["Wait for CT confirmation", "Release the wound/hematoma immediately if airway compromise is evolving while mobilizing the OR and airway team", "Give oral antibiotics and observe", "Place the patient flat and leave the room"],
        "answer": 1,
        "explanation": "A compressive postoperative neck hematoma can progress rapidly to complete airway obstruction. When airway compromise is evolving, bedside wound opening can be lifesaving and should not be delayed for imaging.",
        "why_wrong": ["Imaging can dangerously delay decompression.", "Correct.", "Antibiotics do not address mechanical airway compression.", "Supine positioning and delay can worsen the situation."],
        "board_pearl": "Post-thyroidectomy hematoma is a diagnosis you treat before you image when the airway is threatened.",
        "curveball": "After the incision is opened, stridor persists. What additional airway problem may coexist and how should it be evaluated?",
        "tier": "Curated board/call", "mode": "Vignette"
    },
    {
        "id": "v135_gen_02", "domain": "General ENT / Emergencies", "topic": "Esophageal Perforation / Cervical Mediastinitis",
        "stem": "After difficult endoscopic foreign-body removal, a patient develops severe neck/chest pain, fever, crepitus, and tachycardia. What is the best next step?",
        "choices": ["Routine discharge", "Urgent evaluation for esophageal perforation with broad-spectrum antibiotics, NPO status, imaging, and early surgical consultation/source control", "Treat as reflux only", "Wait several days before reassessment"],
        "answer": 1,
        "explanation": "Esophageal perforation is a time-sensitive source-control problem because contamination can rapidly produce deep-neck infection and mediastinitis. Resuscitation, broad-spectrum antibiotics, imaging, and multidisciplinary surgical planning should occur urgently.",
        "why_wrong": ["The symptom cluster is dangerous for perforation and sepsis.", "Correct.", "Reflux does not explain crepitus and systemic toxicity after instrumentation.", "Delay increases mediastinal contamination and mortality."],
        "board_pearl": "After upper aerodigestive instrumentation, pain out of proportion plus crepitus and fever is perforation until proven otherwise.",
        "curveball": "What factors favor nonoperative management versus drainage/repair?",
        "tier": "Curated board/call", "mode": "Vignette"
    },
    {
        "id": "v135_gen_03", "domain": "General ENT / Emergencies", "topic": "Epistaxis",
        "stem": "An anticoagulated patient presents with brisk epistaxis and borderline hypotension. What should happen before focusing on the exact bleeding vessel?",
        "choices": ["Immediate extensive cautery without stabilization", "Airway/hemodynamic assessment, resuscitation, medication review/reversal when appropriate, then stepwise local control", "Discharge with saline", "CT sinus before any treatment"],
        "answer": 1,
        "explanation": "Severe epistaxis is first an ABC/resuscitation problem. Stabilization and management of anticoagulation occur alongside escalating local control rather than after exhaustive attempts at bedside cautery.",
        "why_wrong": ["Local control without addressing shock and airway risk is unsafe.", "Correct.", "This patient is unstable and needs active management.", "CT is not the first priority in active severe bleeding."],
        "board_pearl": "In major epistaxis, treat the patient before the nose: airway, circulation, anticoagulation, then source control.",
        "curveball": "The patient continues to bleed around a well-positioned posterior pack. What escalation options should be considered?",
        "tier": "Curated board/call", "mode": "Vignette"
    },
]
