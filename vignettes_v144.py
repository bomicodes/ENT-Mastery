"""
v14.4 - Second-case depth closure for Otology/Neurotology and
Rhinology/Allergy/Skull Base singleton topics.

These are deliberately decision-centered: each asks what finding, test, or
management choice changes care rather than merely asking for a label.
"""


def _case(qid, domain, topic, stem, choices, answer, explanation, pearl, curveball, focus="boards"):
    why_wrong = []
    for i, choice in enumerate(choices):
        if i == answer:
            why_wrong.append("Correct.")
        else:
            why_wrong.append(
                f"{choice} does not best address the management discriminator in this scenario; "
                "use the mechanism and decision point described in the explanation."
            )
    return {
        "id": qid, "domain": domain, "topic": topic, "stem": stem,
        "choices": choices, "answer": answer, "explanation": explanation,
        "why_wrong": why_wrong, "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated second-pass depth", "mode": "Vignette", "focus": focus,
    }


O = "Otology / Neurotology"
R = "Rhinology / Allergy / Skull Base"

VIGNETTES_V144 = [
    # ---------------- Otology / Neurotology ----------------
    _case("v144_oto_01", O, "Age-Related Hearing Loss / Presbycusis",
          "A 74-year-old reports gradually worsening speech understanding, especially in noise. Audiometry shows symmetric high-frequency SNHL with good but reduced word recognition and no asymmetry. What is the best next management step?",
          ["Reassure that this is normal aging and needs no treatment", "Offer hearing rehabilitation and communication strategies while screening for red flags that would require additional workup", "Order temporal-bone CT before discussing amplification", "Treat empirically with systemic steroids"], 1,
          "Age-related hearing loss is common but functionally important. Symmetric, gradual high-frequency SNHL without red flags is managed with hearing rehabilitation, counseling, and communication optimization; imaging is not routine solely for presbycusis.",
          "'Expected for age' is not a management plan—treat the communication disability and look for asymmetry or other red flags.",
          "Word recognition is unexpectedly poor in one ear. What additional evaluation becomes appropriate?", "boards"),

    _case("v144_oto_02", O, "Audiologic Electrophysiology / ABR-OAE-ECoG",
          "A newborn fails screening. OAEs are present, but ABR responses are absent or severely abnormal. Which disorder should this pattern raise concern for?",
          ["Auditory neuropathy spectrum disorder", "Simple cerumen impaction", "Classic conductive otitis media only", "Otosclerosis"], 0,
          "Preserved OAEs suggest functioning outer hair cells, while an absent/abnormal ABR suggests disordered neural synchrony along the auditory nerve/brainstem pathway—an auditory neuropathy pattern.",
          "OAE asks whether outer hair cells work; ABR asks whether the neural signal is transmitted synchronously.",
          "How does this pattern change counseling about hearing aids versus cochlear implantation?", "boards"),

    _case("v144_oto_03", O, "Auditory Neuroanatomy / Cochlear Physiology",
          "A patient has a cochlear lesion selectively affecting the basal turn. Which hearing deficit is most expected?",
          ["Preferential low-frequency loss", "Preferential high-frequency loss", "Isolated vestibular loss", "Only speech-production difficulty with normal hearing"], 1,
          "The cochlea is tonotopically organized: the stiff, narrow basal turn encodes high frequencies, whereas the more compliant apex encodes low frequencies.",
          "Base = high frequency; apex = low frequency—this spatial map persists centrally.",
          "Why can a patient with normal pure-tone thresholds still have difficulty understanding speech in noise?", "boards"),

    _case("v144_oto_04", O, "Autoimmune Inner Ear Disease",
          "A patient develops rapidly progressive, fluctuating bilateral SNHL over weeks with intermittent vestibular symptoms. There is no conductive pathology. Which feature most supports an autoimmune inner-ear process?",
          ["A slowly stable loss over decades", "Bilateral or sequential rapidly progressive SNHL with steroid responsiveness in the appropriate clinical context", "A single brief positional vertigo episode", "A normal audiogram"], 1,
          "AIED is a clinical diagnosis of exclusion characterized by relatively rapid, often bilateral or sequential SNHL that may fluctuate and can respond to corticosteroids; systemic autoimmune disease may coexist.",
          "Think tempo and bilaterality: weeks to months is very different from presbycusis.",
          "The patient improves on steroids but relapses repeatedly. What multidisciplinary considerations should enter long-term treatment?", "boards"),

    _case("v144_oto_05", O, "Central Vestibular Disorders",
          "A dizzy patient has direction-changing gaze-evoked nystagmus, severe truncal ataxia, and a normal head-impulse test during continuous acute vertigo. What is the safest interpretation?",
          ["Typical peripheral vestibular neuritis", "Central pathology such as posterior circulation stroke must be excluded urgently", "Simple BPPV", "Ménière disease is proven"], 1,
          "In the acute vestibular syndrome, central ocular-motor findings, inability to sit or walk, and a normal head impulse can signal stroke. A reassuring ear history does not override dangerous neurologic signs.",
          "Continuous vertigo plus central eye findings is a stroke problem until proven otherwise.",
          "Why can an early posterior-fossa MRI be falsely reassuring in selected cases?", "overnight_call"),

    _case("v144_oto_06", O, "Cochlear Implant Failure / Revision",
          "A long-term cochlear implant user develops abrupt performance decline and intermittent device function. Integrity testing is abnormal. What is the best next principle?",
          ["Assume central auditory decline and observe indefinitely", "Differentiate soft failure, hard device failure, electrode migration, infection, and medical causes; revise when objective/device evidence and clinical failure support it", "Remove the implant without planning reimplantation", "Treat with ear drops only"], 1,
          "CI performance decline requires a structured device and medical workup. Hard failure, migration, infection, or persistent suspected soft failure may require explantation/reimplantation after counseling about anatomy and hearing goals.",
          "Revision CI begins by deciding whether the problem is the device, electrode position, ear, or auditory system.",
          "CT shows electrode migration. What operative risks and counseling points change in a revision cochlear implant?", "OR_prep"),

    _case("v144_oto_07", O, "Congenital Inner-Ear Malformations",
          "A child with severe SNHL has CT showing incomplete partition anatomy and a widened cochlear aperture. Which operative issue is most important before cochlear implantation?",
          ["There is no added surgical concern", "Anticipate abnormal facial-nerve anatomy and possible CSF/perilymph gusher depending on the malformation", "The child cannot receive any hearing implant", "Only the mastoid cortex matters"], 1,
          "Congenital cochleovestibular malformations can alter the facial nerve course and increase the risk of CSF/perilymph gusher; preoperative CT/MRI anatomy directly informs electrode choice and surgical strategy.",
          "In congenital ear surgery, the scan is an operative map—not just a diagnostic label.",
          "MRI also shows cochlear nerve aplasia. How does that change hearing-rehabilitation options?", "OR_prep"),

    _case("v144_oto_08", O, "Cortical Neuroplasticity in Hearing Loss",
          "Why is early auditory access important in a young child with severe congenital hearing loss?",
          ["Because cochlear anatomy stops growing at 6 months", "Prolonged auditory deprivation can alter central auditory development, so timely effective auditory input supports language and cortical organization", "Because hearing aids permanently cure SNHL", "Because speech therapy is ineffective after infancy"], 1,
          "Auditory pathways are experience dependent. Prolonged deprivation during sensitive developmental periods can limit later speech/language outcomes even after peripheral hearing is restored.",
          "The ear is only the input device; language outcome also depends on what the developing brain receives and when.",
          "How does this concept influence timing discussions for pediatric cochlear implantation?", "boards"),

    _case("v144_oto_09", O, "Eustachian Tube Dysfunction",
          "An adult has persistent aural pressure and a retracted tympanic membrane with negative middle-ear pressure after an upper respiratory illness. Which finding best supports obstructive Eustachian tube dysfunction rather than a nonspecific pressure complaint?",
          ["Normal otoscopy and normal tympanometry during symptoms", "Objective evidence such as TM retraction or negative-pressure tympanogram that fits the symptoms", "Only a history of migraine", "Autophony that improves when lying down"], 1,
          "Obstructive ETD should connect symptoms to objective middle-ear pressure dysfunction. Normal examination requires reconsideration of alternatives such as migraine, TMJ, or patulous ETD.",
          "Do not label every pressure complaint ETD—look for objective pressure consequences.",
          "Symptoms occur only with descent during flights and the office exam is normal. How does that change the phenotype?", "boards"),

    _case("v144_oto_10", O, "Hearing Aids and Bone-Conduction Devices",
          "A patient has unilateral chronic conductive hearing loss from an ear that cannot reliably tolerate a conventional earmold because of recurrent canal disease. Bone-conduction thresholds are good. What rehabilitation principle is most appropriate?",
          ["No rehabilitation is possible", "Consider bone-conduction hearing technology because it bypasses the external/middle-ear conductive pathway", "Cochlear implantation is always first-line", "Systemic steroids restore the conductive mechanism"], 1,
          "Bone-conduction devices transmit sound through the skull to a functioning cochlea and are useful when the external/middle ear cannot efficiently or safely use conventional air-conduction amplification.",
          "Match the device to the failed part of the auditory pathway.",
          "How does single-sided deafness change the goal of bone-conduction technology compared with conductive loss?", "boards"),

    _case("v144_oto_11", O, "Hyperacusis / Decreased Sound Tolerance",
          "A patient with normal hearing thresholds reports ordinary environmental sounds as painfully loud and has begun wearing earplugs all day. What is the best counseling principle?",
          ["Encourage constant overprotection to eliminate all sound", "Exclude dangerous causes, then use education and gradual sound exposure/behavioral strategies rather than reinforcing broad sound avoidance", "Perform stapedectomy", "Treat as Ménière disease without further evaluation"], 1,
          "Hyperacusis management commonly combines reassurance, treatment of associated migraine/anxiety or other contributors, and controlled sound desensitization. Excessive sound avoidance can increase central gain and worsen tolerance.",
          "Protection is for genuinely hazardous sound, not normal daily acoustic life.",
          "The complaint is specifically triggered by certain human sounds with anger rather than loudness discomfort. What related diagnosis should be considered?", "boards"),

    _case("v144_oto_12", O, "Labyrinthitis / Infections of the Labyrinth",
          "A patient with acute otitis media develops severe continuous vertigo plus new sensorineural hearing loss. Which feature distinguishes labyrinthitis from isolated vestibular neuritis?",
          ["The presence of auditory loss", "Nausea", "Continuous vertigo", "Head-motion intolerance"], 0,
          "Both can cause an acute vestibular syndrome, but labyrinthitis includes cochlear involvement with hearing loss and/or tinnitus; vestibular neuritis classically spares hearing.",
          "Acute vertigo plus hearing loss widens the differential beyond vestibular neuritis and raises urgency.",
          "What infectious and central causes must be considered when hearing loss accompanies acute vertigo?", "overnight_call"),

    _case("v144_oto_13", O, "Lateral Skull-Base Tumor Framework",
          "A patient has progressive unilateral hearing loss, multiple lower cranial neuropathies, and a skull-base mass. What is the most important planning principle before biopsy or surgery?",
          ["Biopsy any visible portion immediately", "Define the lesion's vascularity, cranial-nerve relationships, carotid/jugular involvement, intracranial extent, and likely diagnosis before choosing a tissue or operative strategy", "Assume all skull-base tumors are vestibular schwannomas", "Use symptoms alone to choose the approach"], 1,
          "Lateral skull-base tumors sit among critical neurovascular structures. Imaging phenotype and compartment of origin determine whether biopsy is safe, whether embolization is relevant, and which surgical corridor or nonsurgical treatment is appropriate.",
          "At the skull base, diagnosis and route-to-tissue are inseparable from vascular and cranial-nerve anatomy.",
          "Imaging suggests a hypervascular paraganglioma. What additional preoperative questions become important?", "OR_prep"),

    _case("v144_oto_14", O, "Neurotologic Intraoperative Cranial-Nerve Monitoring",
          "During vestibular schwannoma surgery, facial EMG activity suddenly increases during tumor dissection. What is the best interpretation?",
          ["Monitoring proves the nerve is intact and no change is needed", "Treat the change as a warning signal: stop or alter the maneuver, irrigate/reassess, and correlate with stimulation thresholds and anatomy", "Monitoring replaces direct nerve identification", "Immediately sacrifice the facial nerve"], 1,
          "Intraoperative monitoring is an adjunct that detects physiologic stress and helps map nerves. A significant change should influence technique, but must be interpreted with equipment, anesthesia, stimulation, and direct anatomy.",
          "Monitoring is a feedback system, not permission to ignore anatomy.",
          "What technical causes can mimic a true loss of facial-nerve signal?", "OR_prep"),

    _case("v144_oto_15", O, "Ossicular Discontinuity",
          "After head trauma, a patient has persistent 35-dB conductive hearing loss despite a healed tympanic membrane and aerated middle ear. Tympanometry is hypercompliant. What diagnosis should be suspected?",
          ["Ossicular discontinuity", "Sudden SNHL", "Ménière disease", "Vestibular neuritis"], 0,
          "A persistent large air-bone gap with an intact TM and hypercompliant tympanogram after trauma suggests ossicular-chain discontinuity, commonly at the incudostapedial joint.",
          "A healed eardrum does not guarantee an intact conductive chain.",
          "What factors determine observation, hearing aid use, or exploratory tympanoplasty/ossiculoplasty?", "OR_prep"),

    _case("v144_oto_16", O, "Otologic Manifestations of Systemic Disease",
          "A patient with granulomatosis with polyangiitis has refractory middle-ear effusions, mixed hearing loss, nasal crusting, and systemic inflammatory symptoms. What principle should guide management?",
          ["Treat each ear episode as isolated uncomplicated otitis media", "Recognize the ear findings as possible systemic inflammatory disease and coordinate disease control while treating local complications", "Perform routine tympanoplasty immediately regardless of activity", "Avoid laboratory or rheumatologic evaluation"], 1,
          "Systemic autoimmune and granulomatous disorders can involve the Eustachian tube, middle ear, cochlea, and facial nerve. Durable otologic control may depend on controlling the systemic disease rather than repeatedly treating local manifestations alone.",
          "When an ear problem is unusually refractory, ask whether the ear is the organ announcing systemic disease.",
          "What otologic findings can occur in relapsing polychondritis or Cogan syndrome?", "boards"),

    _case("v144_oto_17", O, "Otosclerosis",
          "A young adult has slowly progressive conductive hearing loss, normal otoscopy, absent acoustic reflexes, and a Carhart-like dip around 2 kHz. Which management choice is reasonable?",
          ["Only systemic steroids", "Hearing aid amplification or stapes surgery depending on hearing goals, anatomy, and patient preference", "Canal-wall-down mastoidectomy", "Observation is mandatory regardless of disability"], 1,
          "Otosclerosis commonly fixes the stapes footplate. Both amplification and stapedotomy/stapedectomy can provide effective rehabilitation in appropriately selected patients.",
          "The board question is not just 'what is it?' but 'does this patient want amplification or mechanical restoration?'.",
          "The opposite ear is the patient's only hearing ear. How does that change operative counseling?", "OR_prep"),

    _case("v144_oto_18", O, "Ototoxic / Noise-Induced Hearing Loss",
          "A patient receiving cisplatin develops new bilateral high-frequency SNHL. What is the best prevention/monitoring principle?",
          ["Wait until conversational hearing is severely impaired before testing", "Use baseline and serial audiologic monitoring and coordinate treatment decisions when threshold shifts emerge", "Noise protection has no role during ototoxic therapy", "The loss is always reversible after chemotherapy"], 1,
          "Ototoxic injury often begins in the high frequencies before patients notice conversational deficits. Baseline/serial testing enables early detection and shared oncology decisions about dose, alternatives, and hearing rehabilitation.",
          "Monitor before symptoms become the audiogram.",
          "What audiometric pattern is classic for chronic noise exposure and how does it differ from presbycusis?", "boards"),

    _case("v144_oto_19", O, "Patulous Eustachian Tube Dysfunction",
          "A patient hears their own voice and breathing unusually loudly. Symptoms worsen with exercise and improve when lying supine. Otoscopy shows TM movement with respiration. What is the best diagnosis?",
          ["Obstructive ETD", "Patulous Eustachian tube", "Otosclerosis", "Acute labyrinthitis"], 1,
          "Autophony of voice/breathing, positional improvement, and TM excursion with respiration are characteristic of patulous ETD, which is physiologically opposite to obstructive ETD.",
          "Obstructive ETD is too closed; patulous ETD is too open—do not treat them as the same problem.",
          "Why can routine balloon dilation worsen this patient's symptoms?", "boards"),

    _case("v144_oto_20", O, "Persistent Postural-Perceptual Dizziness (PPPD)",
          "Months after a resolved vestibular neuritis, a patient has daily nonspinning dizziness worsened by upright posture, supermarkets, scrolling, and visually complex environments. Vestibular testing is otherwise reassuring. What is the best management framework?",
          ["Repeated vestibular suppressants indefinitely", "Explain PPPD and use vestibular rehabilitation plus behavioral/psychological and pharmacologic strategies when appropriate", "Canal plugging surgery", "Strict bed rest"], 1,
          "PPPD is a chronic functional vestibular disorder often triggered by a prior vestibular event. Treatment aims to recalibrate maladaptive visual/postural dependence through vestibular therapy, education, and selected CBT/SSRI/SNRI strategies.",
          "Persistent dizziness after the peripheral lesion heals may reflect maladaptive sensory weighting, not ongoing labyrinth destruction.",
          "Why can chronic meclizine use interfere with compensation?", "boards"),

    _case("v144_oto_21", O, "Petrous Apex Lesions",
          "MRI shows a T1-hyperintense, expansile petrous apex lesion with a history of deep retro-orbital pain and diplopia. What principle most determines whether to observe or drain/resect?",
          ["All petrous apex lesions require surgery", "Use imaging phenotype, symptoms, growth, infection risk, cranial-neural effects, and relationship to carotid/cochlea to determine diagnosis and corridor", "Biopsy through the carotid canal", "Treat every lesion as acute mastoiditis"], 1,
          "Petrous apex lesions include cholesterol granuloma, cholesteatoma, effusion, infection, and neoplasm. Characteristic CT/MRI features plus symptoms and anatomy guide observation versus drainage or resection.",
          "Petrous apex surgery is a corridor problem: the diagnosis tells you whether you need access; anatomy tells you whether a safe corridor exists.",
          "What imaging features help distinguish cholesterol granuloma from cholesteatoma?", "OR_prep"),

    _case("v144_oto_22", O, "Tinnitus",
          "A patient reports new unilateral pulse-synchronous tinnitus. Otoscopy is normal. Which next step is most appropriate?",
          ["Reassure without further evaluation", "Evaluate for vascular and structural causes with targeted history/exam, audiometry, and appropriate imaging", "Treat empirically with oral steroids only", "Schedule stapedectomy"], 1,
          "Pulsatile tinnitus has a different differential from nonpulsatile subjective tinnitus and can reflect arterial, venous, middle-ear, or intracranial pathology. Unilateral pulse-synchronous symptoms warrant directed evaluation.",
          "First divide tinnitus into pulsatile versus nonpulsatile; that branch changes the workup.",
          "A retrotympanic red mass is now visible. What dangerous office maneuver should be avoided?", "overnight_call"),

    _case("v144_oto_23", O, "Tympanic Membrane Perforation",
          "A patient has a clean traumatic TM perforation after a slap injury, mild conductive hearing loss, and no vertigo or facial weakness. What is the best initial management?",
          ["Immediate tympanoplasty in every case", "Keep the ear dry, avoid traumatic instrumentation/ototoxic drops, and observe for spontaneous healing with follow-up hearing assessment", "Daily hydrogen peroxide irrigation", "Systemic steroids are mandatory"], 1,
          "Most uncomplicated traumatic TM perforations heal spontaneously. Initial care is dry-ear protection and follow-up; surgery is reserved for persistent perforation or associated ossicular/inner-ear injury.",
          "Traumatic perforation is usually an observation problem unless hearing, vestibular, facial-nerve, or contamination findings say otherwise.",
          "The perforation persists at 4 months with an air-bone gap. What operative options should be discussed?", "boards"),

    _case("v144_oto_24", O, "Tympanometry / Acoustic Reflexes",
          "An audiogram shows a conductive air-bone gap. Tympanometry is type As with absent acoustic reflexes. Which pathology is most compatible?",
          ["Stapes fixation such as otosclerosis", "Normal middle-ear mechanics", "Isolated vestibular neuritis", "Pure cochlear presbycusis only"], 0,
          "A shallow type As tympanogram reflects a stiff middle-ear system; absent reflexes with conductive loss can support ossicular/stapes fixation such as otosclerosis.",
          "Tympanometry measures middle-ear mechanics; reflex patterns help localize the conductive or neural pathway problem.",
          "How would ossicular discontinuity tend to change tympanometric compliance?", "boards"),

    _case("v144_oto_25", O, "Vestibular Neuritis",
          "A patient has 36 hours of continuous severe vertigo, nausea, unidirectional horizontal-torsional nystagmus, abnormal head impulse to the right, no hearing loss, and no focal neurologic deficits. What is the most likely diagnosis and management principle?",
          ["Right vestibular neuritis; short-term symptom control followed by early mobilization/vestibular rehabilitation", "BPPV; Epley maneuver alone", "Ménière disease; salt restriction proves the diagnosis", "Acoustic neuroma requiring emergency surgery"], 0,
          "The continuous acute vestibular syndrome with unilateral vestibular hypofunction and preserved hearing fits vestibular neuritis. Vestibular suppressants should be brief so central compensation can begin, followed by mobilization and rehab.",
          "Vestibular neuritis is hours-to-days of continuous vertigo, not seconds of positional vertigo.",
          "Which HINTS feature would make you abandon the peripheral diagnosis and evaluate urgently for stroke?", "overnight_call"),

    _case("v144_oto_26", O, "Vestibular Rehabilitation",
          "A patient with compensated unilateral vestibular hypofunction still avoids head movement because it provokes brief disequilibrium. What therapy best promotes recovery?",
          ["Long-term vestibular suppressants and activity restriction", "Gaze-stability, habituation, balance training, and progressive activity through vestibular rehabilitation", "Strict cervical immobilization", "Middle-ear surgery"], 1,
          "Vestibular rehabilitation uses adaptation, substitution, and habituation to improve gaze stability and balance. Chronic suppression and avoidance can slow central compensation.",
          "Recovery requires the brain to experience controlled error signals, not avoid them forever.",
          "How would bilateral vestibular loss change the rehabilitation emphasis?", "boards"),

    _case("v144_oto_27", O, "Vestibular Test Battery",
          "A patient has chronic imbalance with suspected superior vestibular nerve dysfunction. Which pairing correctly links a vestibular test to the structure/function it emphasizes?",
          ["vHIT—high-frequency semicircular canal vestibulo-ocular reflex", "Pure-tone audiometry—otolith function", "Tympanometry—saccular function", "OAE—horizontal canal function"], 0,
          "The vestibular battery is complementary: vHIT probes high-frequency canal VOR, calorics emphasize low-frequency horizontal-canal function, and VEMPs assess otolith pathways. No single test is a complete vestibular examination.",
          "Choose vestibular tests by the frequency range and end organ you are trying to interrogate.",
          "Why can calorics be abnormal while vHIT remains normal in the same patient?", "boards"),

    # ---------------- Rhinology / Allergy / Skull Base ----------------
    _case("v144_rh_01", R, "Allergy Testing & Interpretation",
          "A patient has perennial rhinitis symptoms and positive skin-prick testing to dust mite. What determines whether the result is clinically meaningful?",
          ["Any positive wheal proves the allergen causes symptoms", "The sensitization must match the exposure history and symptom pattern; testing supports but does not replace clinical correlation", "Total IgE alone establishes the culprit allergen", "CT sinus opacity proves allergic rhinitis"], 1,
          "Skin or serum specific-IgE testing demonstrates sensitization, not necessarily symptomatic allergy. Management depends on whether the exposure and history fit the test result.",
          "A positive allergy test without a matching history is sensitization, not automatically disease.",
          "When would allergen immunotherapy be considered after testing?", "boards"),

    _case("v144_rh_02", R, "Benign Sinonasal Tumor Framework",
          "An adult has unilateral obstruction and recurrent epistaxis. Endoscopy shows a unilateral vascular-appearing nasal mass. What is the safest next step before biopsy?",
          ["Blind office biopsy immediately", "Define attachment, vascularity, skull-base/orbital extension, and likely diagnosis with endoscopy and appropriate imaging before choosing a biopsy route", "Treat as allergic polyposis", "Ignore unilateral symptoms"], 1,
          "Unilateral sinonasal masses require a neoplasm-focused workup. Vascular lesions and skull-base processes can make unplanned office biopsy dangerous; imaging guides whether and how to obtain tissue.",
          "Unilateral disease earns respect: image the anatomy before you casually biopsy a vascular-looking mass.",
          "Imaging shows cerebriform enhancement from the lateral nasal wall. Which benign tumor becomes more likely and why does its attachment matter surgically?", "OR_prep"),

    _case("v144_rh_03", R, "CF / Primary Ciliary Dyskinesia Sinonasal Disease",
          "A young adult with bronchiectasis, chronic wet cough, and lifelong refractory pansinusitis has unusually thick secretions. What principle should guide sinonasal management?",
          ["Treat as isolated routine CRS only", "Coordinate evaluation for mucociliary disease and use long-term airway-focused care; surgery may improve drainage/access but does not correct the underlying clearance defect", "Avoid saline irrigation", "Assume symptoms are psychogenic"], 1,
          "CF and primary ciliary dyskinesia produce systemic mucociliary-clearance failure. ENT treatment should integrate pulmonary care, cultures when appropriate, topical clearance strategies, and selective surgery for access/disease burden.",
          "ESS can improve the plumbing; it cannot repair abnormal mucus or cilia.",
          "What associated otologic findings would support primary ciliary dyskinesia in a child?", "boards"),

    _case("v144_rh_04", R, "CRS Phenotyping",
          "Two patients both meet criteria for CRS; one has bilateral polyps, asthma, and anosmia, while the other has purulent drainage without polyps. Why does phenotyping matter?",
          ["It does not; all CRS is treated identically", "Phenotype/endotype affects expected recurrence, comorbidity evaluation, topical/systemic therapy, biologic candidacy, and surgical planning", "Only CT score matters", "Antibiotics are mandatory indefinitely in both"], 1,
          "CRS is heterogeneous. CRSwNP, CRSsNP, AERD, AFRS, immunodeficiency-associated disease, and other phenotypes differ in inflammatory biology and longitudinal treatment needs.",
          "The diagnosis 'CRS' starts the treatment framework; phenotype determines much of what comes next.",
          "What features would make you specifically screen for AERD?", "boards"),

    _case("v144_rh_05", R, "CRSsNP",
          "A patient has >12 weeks of obstruction and mucopurulent drainage with objective endoscopic inflammation but no polyps. Symptoms persist despite appropriate medical therapy. What is a reasonable next management principle?",
          ["Biologic therapy is automatically first-line", "Confirm phenotype and contributing factors, optimize medical therapy, and consider ESS when persistent objective disease and quality-of-life burden justify it", "Operate based only on a mildly abnormal CT", "No further treatment is possible"], 1,
          "CRSsNP management combines objective confirmation, medical therapy, evaluation for dental/immunologic/anatomic contributors, and selective surgery when symptoms and disease remain significant.",
          "ESS is not a CT treatment; it is a treatment for appropriately selected symptomatic inflammatory disease.",
          "Unilateral maxillary disease is present with a diseased molar. How does that change the differential and plan?", "boards"),

    _case("v144_rh_06", R, "Facial Pain / Headache vs Rhinogenic Disease",
          "A patient has severe 'sinus headaches' but normal nasal endoscopy, normal sinus CT, photophobia, nausea, and episodic throbbing pain. What is the best next step?",
          ["FESS despite normal objective sinonasal evaluation", "Reconsider migraine or another headache disorder rather than attributing symptoms to sinus disease", "Long-term antibiotics", "Frontal sinus obliteration"], 1,
          "Facial pressure is nonspecific. Migraine commonly masquerades as 'sinus headache'; normal endoscopy/CT plus migrainous features argues strongly against rhinogenic pain and prevents unnecessary sinus surgery.",
          "Pressure is a symptom, not proof of sinus inflammation.",
          "What rare anatomic situations can produce truly rhinogenic contact-point pain, and why must other causes still be excluded?", "boards"),

    _case("v144_rh_07", R, "Frontal Recess / Frontal Sinus",
          "During frontal sinus surgery, why is preoperative multiplanar CT review especially important?",
          ["The frontal recess has uniform anatomy in all patients", "Variable frontal cells, skull-base slope, anterior ethmoid artery, orbit, and drainage pathway can make blind superior dissection dangerous", "CT cannot show relevant anatomy", "Only the nasal septum matters"], 1,
          "Frontal drainage anatomy is highly variable and bounded by orbit and skull base. CT-based mapping of cells and drainage pathway is essential to choose a safe dissection corridor and preserve mucosa.",
          "In the frontal recess, orientation errors become skull-base or orbital injuries quickly.",
          "A postoperative patient develops a laterally based frontal mucocele. What does that suggest about access and drainage strategy?", "OR_prep"),

    _case("v144_rh_08", R, "Fungal Ball",
          "An immunocompetent adult has unilateral maxillary opacification with hyperdense concretions and foul drainage. Endoscopy shows thick debris but no tissue necrosis. What is the best management?",
          ["Systemic amphotericin for months", "Endoscopic removal and restoration of sinus drainage; systemic antifungal therapy is usually unnecessary for a noninvasive fungal ball", "No treatment even if symptomatic", "Chemoradiation"], 1,
          "A fungal ball is noninvasive colonization of a sinus lumen, usually managed surgically by removing concretions and opening the sinus. It is biologically distinct from invasive fungal rhinosinusitis.",
          "Fungus in the sinus does not automatically mean invasive fungal disease.",
          "Histology unexpectedly shows tissue invasion. How does management change immediately?", "OR_prep"),

    _case("v144_rh_09", R, "Immunodeficiency-Associated Chronic Rhinosinusitis",
          "A patient has refractory CRS plus recurrent pneumonias and unusually frequent bacterial infections despite technically adequate sinus surgery. What is the next important step?",
          ["Repeat sinus surgery indefinitely without broader evaluation", "Evaluate for humoral or other immune deficiency and coordinate treatment of the underlying host problem", "Assume all symptoms are allergy", "Stop all topical therapy"], 1,
          "Refractory or unusually recurrent sinopulmonary infection should prompt consideration of quantitative immunoglobulins and functional antibody responses in the appropriate context; durable control may require immune-directed therapy.",
          "When infection burden is disproportionate, audit the host—not just the sinuses.",
          "How can poor pneumococcal antibody response change management even when total IgG is normal?", "boards"),

    _case("v144_rh_10", R, "Inferior Turbinate Hypertrophy",
          "A patient has persistent bilateral nasal obstruction from enlarged inferior turbinates despite appropriate treatment of allergic rhinitis. Which operative principle is preferred?",
          ["Aggressively resect the entire inferior turbinate", "Reduce obstructive tissue while preserving mucosa and turbinate function", "Remove the middle turbinate instead", "Ablate the septum"], 1,
          "Turbinate surgery should improve airflow while preserving mucosal humidification and sensation. Excessive resection risks crusting, dryness, and empty-nose-type symptoms.",
          "The goal is a smaller functioning turbinate, not absence of a turbinate.",
          "How does concomitant septal deviation affect surgical planning for nasal obstruction?", "OR_prep"),

    _case("v144_rh_11", R, "Local Allergic Rhinitis",
          "A patient has classic seasonal nasal itching, sneezing, and watery rhinorrhea, but repeated skin and serum specific-IgE tests are negative. What concept may explain the symptoms?",
          ["Local allergic rhinitis with nasal mucosal IgE-mediated reactivity", "Allergy is impossible", "Invasive fungal disease", "CSF leak"], 0,
          "Some patients have localized nasal allergic responses despite negative systemic testing. Diagnosis remains specialized and clinical correlation is essential, but negative systemic testing does not make every allergic phenotype impossible.",
          "Systemic sensitization tests do not capture every mucosal immune phenotype.",
          "How would you distinguish this from nonallergic vasomotor rhinitis clinically?", "boards"),

    _case("v144_rh_12", R, "Mucocele",
          "Years after frontal sinus surgery, a patient develops slowly progressive proptosis and frontal pressure. CT shows an expansile, smoothly marginated frontal sinus lesion with bony remodeling. What is the best management principle?",
          ["Treat as acute invasive fungal disease", "Drain/marsupialize the obstructed mucocele and re-establish durable sinus ventilation while protecting orbit and skull base", "Observe all symptomatic mucoceles indefinitely", "Radiation therapy"], 1,
          "Mucoceles are expansile mucus-filled lesions caused by obstructed sinus drainage and can erode/remodel bone. Symptomatic or complicated lesions are treated by establishing drainage, usually endoscopically when anatomy permits.",
          "A mucocele is a ventilation failure that becomes a space-occupying lesion.",
          "What features would push you toward a combined or external approach rather than purely endoscopic drainage?", "OR_prep"),

    _case("v144_rh_13", R, "Nasal Anatomy for Endoscopy",
          "During diagnostic nasal endoscopy, which landmark most reliably leads you to the natural maxillary ostium region?",
          ["The uncinate process and middle meatus", "The inferior meatus alone", "The nasal vestibule", "The posterior choana only"], 0,
          "The maxillary natural ostium lies in the middle meatus/ethmoid infundibulum behind the uncinate. Understanding this relationship prevents mistaking an accessory ostium for the natural drainage pathway.",
          "Endoscopic sinus anatomy is learned as drainage pathways bounded by stable landmarks, not isolated holes.",
          "Why can connecting a natural and accessory maxillary ostium matter in recirculation?", "OR_prep"),

    _case("v144_rh_14", R, "Nonallergic Rhinitis / Rhinitis Medicamentosa",
          "A patient has severe rebound nasal obstruction after using oxymetazoline every few hours for 3 months. What is the best treatment principle?",
          ["Increase decongestant frequency", "Stop the topical vasoconstrictor and use supportive anti-inflammatory therapy while counseling that rebound may temporarily worsen", "Start systemic antifungal therapy", "Immediate skull-base surgery"], 1,
          "Rhinitis medicamentosa is rebound congestion from chronic topical alpha-agonist use. Management requires withdrawal and often intranasal corticosteroid/supportive therapy during recovery.",
          "The medication causing relief can become the mechanism maintaining obstruction.",
          "How does vasomotor/nonallergic rhinitis differ when the dominant symptom is watery rhinorrhea triggered by temperature or eating?", "boards"),

    _case("v144_rh_15", R, "Objective Assessment of Nasal Function",
          "A patient reports severe nasal obstruction, but the structural examination is equivocal. What is the best use of objective nasal testing?",
          ["It replaces the history and physical examination", "It can quantify airflow/resistance or geometry and complement symptom scores, but results must be interpreted with the clinical picture", "It proves allergy", "It determines cancer stage"], 1,
          "Rhinomanometry and acoustic rhinometry can provide objective physiologic/anatomic information, but nasal obstruction perception is multidimensional and no single measurement replaces clinical assessment.",
          "Objective airflow data are adjuncts, not an automatic indication for surgery.",
          "Why can the Cottle maneuver overpredict benefit from nasal-valve surgery?", "boards"),

    _case("v144_rh_16", R, "Olfactory Dysfunction",
          "A patient has persistent anosmia after a viral illness, normal endoscopy, and no obstructing mass. What is a reasonable first-line rehabilitation strategy?",
          ["Olfactory training with repeated structured odor exposure", "Routine sinus surgery", "Long-term antibiotics", "No counseling because recovery is impossible"], 0,
          "Postviral olfactory loss often has no surgically correctable obstruction. Olfactory training is low risk and supported as a rehabilitation strategy while red flags and reversible nasal inflammation are assessed.",
          "First decide conductive versus sensorineural/central smell loss; treatment follows the mechanism.",
          "Which unilateral smell-loss or neurologic features should trigger imaging or broader evaluation?", "boards"),

    _case("v144_rh_17", R, "Pediatric Chronic Rhinosinusitis",
          "A 6-year-old has chronic nasal obstruction and purulent drainage despite appropriate medical treatment. Adenoid hypertrophy is present, with no concerning orbital or intracranial findings. What operative step is often considered before full adult-style ESS?",
          ["Adenoidectomy in an appropriately selected child", "Total rhinectomy", "Frontal sinus obliteration", "No surgery can ever be used in children"], 0,
          "The adenoid can serve as a bacterial reservoir and obstruct the nasopharynx; adenoidectomy is commonly an early surgical step for medically refractory pediatric CRS before more extensive ESS in selected children.",
          "Pediatric CRS is not simply adult CRS in a smaller nose—adenoid disease matters.",
          "What comorbidities should lower your threshold to evaluate for CF, PCD, or immune deficiency?", "boards"),

    _case("v144_rh_18", R, "Recurrent Acute Rhinosinusitis",
          "An adult reports four distinct episodes per year of acute bacterial-type sinusitis with complete symptom resolution between episodes. Endoscopy between attacks is normal. What diagnosis best fits?",
          ["Recurrent acute rhinosinusitis", "Chronic rhinosinusitis", "Invasive fungal sinusitis", "CSF rhinorrhea"], 0,
          "RARS consists of discrete acute episodes separated by symptom-free intervals; CRS requires persistent symptoms and objective inflammation over a chronic duration.",
          "The key distinction is what happens between episodes: normal intervals point away from CRS.",
          "When is CT most informative in RARS—during an episode or after symptoms have fully resolved?", "boards"),

    _case("v144_rh_19", R, "Septal Deviation",
          "A patient has fixed unilateral nasal obstruction from a severe caudal septal deviation that does not improve with decongestion. Medical therapy has failed. What is the operative goal of septoplasty?",
          ["Remove as much cartilage as possible", "Correct the obstructing deformity while preserving adequate structural support, especially dorsal and caudal support", "Ablate the inferior turbinate completely", "Open the frontal sinus"], 1,
          "Septoplasty balances airway improvement with preservation of the structural L-strut and support mechanisms. Overresection can cause saddle deformity or tip support problems.",
          "A straight septum that collapses the nose is not a successful septoplasty.",
          "How does a caudal deviation change fixation and reconstruction compared with a simple mid-septal spur?", "OR_prep"),

    _case("v144_rh_20", R, "Sinonasal Malignancy",
          "A patient has unilateral obstruction, epistaxis, facial numbness, and an irregular sinonasal mass with skull-base erosion. What is the best initial oncologic principle?",
          ["Treat empirically as CRS for months", "Obtain staging-quality imaging and tissue diagnosis with attention to orbit, skull base, cranial nerves, neck, and distant disease before definitive multidisciplinary planning", "Perform blind debulking without pathology", "Assume all sinonasal cancers receive the same operation"], 1,
          "Sinonasal malignancies are histologically diverse and anatomically complex. Histology and extent determine whether treatment is endoscopic/open surgery, radiation, systemic therapy, or combinations.",
          "For sinonasal cancer, histology is as important as geography.",
          "MRI shows perineural spread toward the cavernous sinus. How does that change resectability and radiation planning?", "boards"),

    _case("v144_rh_21", R, "Sphenoidotomy",
          "During endoscopic sphenoidotomy, what is the most important preoperative imaging habit?",
          ["Ignore the sphenoid because anatomy is constant", "Identify carotid and optic-nerve relationships, Onodi cells, septal insertions, pneumatization pattern, and skull-base anatomy before entering", "Use only a lateral plain film", "Enter through the most lateral wall"], 1,
          "The sphenoid can expose or dehisce the optic nerve and carotid canal, and intersinus septa may insert onto these structures. CT review is essential before widening the ostium.",
          "A sphenoid septum attached to the carotid prominence is a warning, not a handle.",
          "Where is the natural sphenoid ostium relative to the superior turbinate?", "OR_prep"),

    _case("v144_rh_22", R, "Systemic Disease of the Nose / Sinuses",
          "A patient has persistent nasal crusting, septal perforation, pulmonary symptoms, and renal abnormalities. What is the best next conceptual step?",
          ["Treat as uncomplicated allergic rhinitis", "Consider systemic vasculitis such as granulomatosis with polyangiitis and coordinate systemic evaluation rather than treating the nose in isolation", "Perform cosmetic rhinoplasty first", "Use topical decongestants indefinitely"], 1,
          "Destructive or unusually inflammatory sinonasal disease can be a manifestation of systemic vasculitis, autoimmune disease, sarcoid, relapsing polychondritis, or cocaine-related injury. The pattern should trigger systemic evaluation.",
          "A septal perforation is a finding; the cause may live far outside the nose.",
          "Which biopsy site is often most useful when sinonasal tissue is nonspecific but systemic GPA is suspected?", "boards"),

    _case("v144_rh_23", R, "Unilateral Sinonasal Disease",
          "An adult has persistent unilateral maxillary opacification and unilateral polyploid tissue. Why should this be approached differently from typical bilateral inflammatory polyposis?",
          ["Unilateral disease has no special significance", "It broadens the differential to odontogenic disease, fungal ball, inverted papilloma, malignancy, and anatomic obstruction, so targeted imaging/endoscopy and often tissue diagnosis are needed", "It proves allergic rhinitis", "It should never be biopsied"], 1,
          "Unilateral disease is a pattern that demands explanation. The differential includes inflammatory, dental, fungal, benign neoplastic, and malignant causes, so the workup should not assume routine diffuse CRS.",
          "Bilateral polyps are usually inflammatory; a unilateral mass has to earn that assumption.",
          "CT shows focal hyperostosis at one attachment site. Which diagnosis becomes more likely and how does that guide surgery?", "OR_prep"),
]
