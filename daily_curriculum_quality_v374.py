"""Sixth-order Daily Curriculum clinical-task and curveball cleanup.

This layer replaces the last repeated ``build a map`` and ``what structure or
failure mechanism`` prompts with concrete anatomy, interpretation, or rescue
tasks.  It also removes the final shared procedural curveball fallback so every
live Attending Curveball answers the question actually displayed to the learner.
"""


DAILY_OVERRIDES = {
    ("Temporal Bone Anatomy", "recognize"): (
        "During a cortical mastoidectomy, which fixed boundaries orient the surgeon before deeper dissection, and which critical structures lie beyond them?",
        "Orient the squamous, mastoid, tympanic, petrous and styloid temporal-bone components around the external canal, middle ear, mastoid and otic capsule. The tegmen bounds the field superiorly, the sigmoid sinus posteriorly, the posterior canal wall and facial recess anteriorly, and the digastric ridge inferiorly. Deeper relationships include the middle cranial fossa above, posterior fossa behind, jugular bulb below, petrous carotid anteromedially, labyrinth medially and facial nerve along its labyrinthine, tympanic and mastoid segments.",
    ),
    ("Auditory Neuroanatomy / Cochlear Physiology", "recognize"): (
        "How does sound travel from the tympanic membrane to auditory cortex, and where do mechanical transmission, frequency analysis, transduction, neural synchrony, and binaural processing occur?",
        "The tympanic membrane and ossicles transmit and impedance-match sound into cochlear fluid. A basilar-membrane traveling wave produces tonotopic frequency analysis; inner-hair-cell transduction drives spiral-ganglion neurons, while outer hair cells provide active amplification and sharpening. Auditory-nerve fibers project through cochlear nuclei, superior olivary complexes, lateral lemniscus, inferior colliculi and medial geniculate bodies to auditory cortex. Bilateral central projections explain why a unilateral central lesion rarely causes complete unilateral deafness.",
    ),
    ("Nasal Anatomy for Endoscopy", "recognize"): (
        "During diagnostic nasal endoscopy, what sequence of landmarks keeps the examination oriented from the nasal floor to the middle meatus, sphenoethmoidal recess, and choana?",
        "Begin with the vestibule, septum, nasal floor and inferior turbinate, then identify the middle turbinate as the principal endoscopic landmark. Inspect the middle meatus and uncinate-bulla region, follow the basal lamella toward the superior meatus, and examine the sphenoethmoidal recess above and medial to the superior turbinate before reaching the choana and nasopharynx. Maintain awareness of the lamina papyracea laterally and skull base superiorly rather than advancing through an unrecognized recess.",
    ),
    ("Cleft Lip / Palate — ENT Surgical Fundamentals", "recognize"): (
        "In a child with cleft palate, which linked anatomic problems account for feeding difficulty, velopharyngeal speech, and chronic middle-ear disease?",
        "The visible cleft reflects abnormal separation and orientation of the palatal shelves and levator sling, so the child may lack effective oral-nasal separation for feeding and velopharyngeal closure for speech. Abnormal tensor veli palatini mechanics impair Eustachian-tube ventilation and predispose to persistent effusion and conductive hearing loss. Assessment must therefore integrate palate anatomy, feeding, speech/resonance, hearing and ear disease rather than treating only the mucosal gap.",
    ),
    ("Laryngeal Anatomy", "recognize"): (
        "How do the laryngeal framework, joints, intrinsic muscles, mucosal spaces, and superior versus recurrent laryngeal nerves work together to produce airway protection and phonation?",
        "The thyroid, cricoid and arytenoid cartilages form a mobile framework linked by cricoarytenoid and cricothyroid joints. Intrinsic muscles abduct, adduct and tension the folds; the superficial lamina propria permits vibration, while paraglottic and pre-epiglottic spaces guide tumor spread. The recurrent laryngeal nerve supplies all intrinsic muscles except cricothyroid and carries sensation below the glottis; the superior laryngeal nerve provides supraglottic sensation through its internal branch and cricothyroid motor supply through its external branch.",
    ),
    ("Open Rhinoplasty Fundamentals", "recognize"): (
        "What exposure does an open rhinoplasty approach add, and which support and soft-tissue relationships must remain visible throughout tip, dorsum, and valve work?",
        "A transcolumellar incision joined to marginal incisions elevates the skin-soft-tissue envelope for broad visualization of the lower lateral cartilages, septum, dorsum and nasal valves. The exposure helps diagnose asymmetry and perform precise grafting or suturing, but it does not remove the need to preserve dorsal and caudal septal support, protect the internal and external valves, maintain vascularized soft-tissue coverage and avoid excessive thinning or devascularization of the envelope.",
    ),
    ("Hair Restoration Fundamentals", "recognize"): (
        "Before planning hair transplantation, which history and scalp findings distinguish stable patterned androgenetic loss from active scarring, inflammatory, or diffuse shedding disorders?",
        "Map the distribution and tempo of loss, miniaturization, donor density and hair caliber, and examine for erythema, scale, perifollicular change, loss of follicular openings, patchiness or diffuse shedding. Stable patterned miniaturization with an adequate permanent donor zone can support transplantation; active scarring alopecia, inflammatory disease, alopecia areata, telogen effluvium or an unstable youthful pattern requires diagnosis and medical stabilization first because grafting does not stop the underlying process.",
    ),
    ("ENT Imaging Fundamentals", "recognize"): (
        "For an ENT problem, when does CT answer the key question better than MRI, and when should MRI be added instead of simply repeating CT?",
        "CT is strongest for cortical bone, fractures, ossicles, air spaces, calcification and rapid assessment of acute sinonasal or temporal-bone anatomy. MRI better characterizes soft tissue, marrow, dura and brain, perineural spread, vascular-flow relationships and many skull-base lesions; diffusion and contrast sequences can answer specific infection or tumor questions. Choose the study from the suspected compartment and decision, review it in multiplanar planes, and add angiographic imaging when vessel injury or vascular tumor is plausible.",
    ),
    ("Wound Healing / Scar Biology in Head & Neck Surgery", "recognize"): (
        "A head-and-neck wound is separating or healing poorly: which local and systemic mechanisms should be identified before calling it simply a bad scar?",
        "Separate acute wound failure from later excessive scarring. Early dehiscence or fistula may reflect tension, hematoma or seroma, infection, salivary contamination, ischemia, radiation injury, malnutrition, diabetes, nicotine exposure or immunosuppression. Hypertrophic scars remain within the wound boundary and may regress, whereas keloids extend beyond it. Management starts by correcting the active mechanical, perfusion, infectious or nutritional cause rather than treating surface appearance alone.",
    ),
    ("Grafts / Implants / Biomaterials in ENT", "recognize"): (
        "When choosing an autograft, allograft, or synthetic implant in ENT reconstruction, which mechanical and biologic demands determine whether the material is suitable?",
        "Match the material to the job: rigid or semirigid support, pliable lining, volume replacement, sound conduction or long-term device function. Consider infection and extrusion risk, vascularized coverage, resorption, warping, donor morbidity, radiation, wound contamination, imaging needs and reversibility. Autologous tissue is often favored in contaminated or poorly vascularized fields, while allografts and synthetics can avoid donor morbidity when their predictable mechanics and complication profile fit the site.",
    ),
    ("Laser / Energy Safety in Otolaryngology", "recognize"): (
        "Before activating a laser or electrosurgical device in the airway, what elements complete the fire triangle and what team controls interrupt each one?",
        "An airway fire requires an ignition source, an oxidizer and fuel. Control ignition with the lowest effective settings, standby mode and safe aiming; reduce oxidizer concentration and avoid nitrous oxide through explicit anesthesia communication; manage fuel with an appropriate laser-resistant tube, protected cuff, wet pledgets and dry-time confirmation for alcohol preparations. Announce activation, protect eyes and skin, evacuate plume, keep saline immediately available and rehearse tube removal, oxygen cessation and airway-fire rescue.",
    ),
    ("Orbital Complications of Sinusitis", "localize"): (
        "In a patient with sinusitis and eyelid swelling, which examination and imaging findings distinguish preseptal disease, subperiosteal abscess, orbital cellulitis or abscess, and orbital-apex or cavernous-sinus involvement?",
        "Localize disease relative to the orbital septum, lamina papyracea, extraocular muscles, optic nerve, orbital apex and cavernous sinus. Painful or restricted motility, proptosis, reduced acuity or color vision, RAPD and optic-disc change indicate postseptal or optic-pathway risk. CT with contrast usually defines sinus and orbital compartments; MRI is useful for apex, intracranial or cavernous-sinus concern. Serial visual examinations matter because deterioration—not collection size alone—can mandate urgent drainage.",
    ),
    ("Intracranial Complications of Sinusitis", "localize"): (
        "When sinusitis is accompanied by severe headache, focal deficit, seizure, meningismus, or altered mental status, which routes and intracranial compartments must imaging define urgently?",
        "Frontal sinus infection can extend through posterior-table osteitis or valveless diploic veins, while ethmoid and sphenoid disease can reach the cavernous sinus, skull base, meninges or adjacent brain. Contrast MRI and CT should distinguish epidural or subdural empyema, cerebritis or parenchymal abscess, meningitis, venous-sinus thrombosis, osteomyelitis and Pott puffy tumor. The involved compartment determines neurosurgical urgency and whether sinus source control alone is insufficient.",
    ),
    ("Free-Flap Monitoring / Compromise / Salvage", "localize"): (
        "A free flap becomes pale or congested after head-and-neck reconstruction: how do appearance, bleeding, Doppler findings, and the pedicle examination localize arterial, venous, or extrinsic compromise?",
        "Pallor, slow or absent dark bleeding and loss of arterial Doppler suggest inflow failure; a blue, swollen flap with brisk dark bleeding and a persisting arterial signal suggests venous obstruction. Trace the circuit from arterial inflow through both anastomoses and microcirculation to venous outflow, while immediately checking hematoma, tight closure or dressing, dependent positioning, and pedicle kink or twist. A strong arterial Doppler does not exclude venous compromise, and suspected vascular failure requires prompt exploration rather than prolonged observation.",
    ),
    ("Carotid Blowout Syndrome", "localize"): (
        "In an irradiated or infected neck with sentinel bleeding, which exposed vessel segments and wound features make carotid blowout imminent rather than routine mucosal bleeding?",
        "Threatened or ruptured common or internal carotid segments may be exposed by recurrent tumor, radiation necrosis, infection, pharyngocutaneous fistula or wound breakdown; major external-carotid branches can also produce life-threatening hemorrhage. A visible vessel, pseudoaneurysm, contrast extravasation, recurrent sentinel bleed or infected tissue separating the artery from skin or pharynx marks escalating risk. Localize with urgent vascular imaging only if the patient is stable enough; uncontrolled hemorrhage requires simultaneous airway, resuscitation and definitive endovascular or operative control.",
    ),
    ("First-Bite Syndrome", "localize"): (
        "After deep-lobe parotid or parapharyngeal surgery, why does severe pain peak with the first bite and fade during the meal, and what anatomy was likely disrupted?",
        "The syndrome localizes to disrupted sympathetic input to parotid myoepithelial cells, often after deep-lobe, parapharyngeal, carotid-space or sympathetic-chain surgery. Relatively unopposed parasympathetic stimulation at the onset of salivation produces intense first-stimulus pain that diminishes with continued eating. That pattern separates it from TMJ or dental pain, trigeminal neuralgia and recurrent suppurative sialadenitis.",
    ),
    ("Frey Syndrome", "localize"): (
        "Why does eating cause focal flushing and sweating over a healed parotid bed, and how does that mechanism differ from first-bite syndrome?",
        "Postganglionic parasympathetic fibers that formerly stimulated the parotid can regenerate aberrantly into denervated cutaneous sweat glands and superficial vessels. Salivatory stimulation is then misdirected into sweating and vasodilation over the operative bed, demonstrable with a Minor starch-iodine test when needed. First-bite syndrome is instead a pain syndrome associated with loss of sympathetic input and unopposed salivary stimulation, not aberrant cutaneous reinnervation.",
    ),
    ("Recurrent Laryngeal Nerve Injury During Thyroidectomy", "localize"): (
        "Where is the recurrent laryngeal nerve most vulnerable during thyroidectomy, and which anatomic variants or separate nerve injuries can mimic or alter the deficit?",
        "The nerve is especially vulnerable near the ligament of Berry and laryngeal entry point, at crossings with branches of the inferior thyroid artery, and where tumor, scar or traction distorts its course. The left nerve usually ascends in the tracheoesophageal groove, the right is more oblique, and a nonrecurrent right nerve should be suspected with the corresponding vascular anomaly. External superior laryngeal nerve injury impairs cricothyroid function and pitch projection without causing the same vocal-fold immobility.",
    ),
    ("Septal Hematoma", "localize"): (
        "After nasal trauma, what does bilateral fluctuant septal swelling represent, and why can a localized subperichondrial collection rapidly threaten the whole cartilaginous framework?",
        "Blood has separated septal perichondrium from cartilage, interrupting diffusion-dependent cartilage nutrition. The collection may become infected and cartilage can necrose, producing septal abscess, perforation, saddle deformity and impaired midface growth in a child. This is not routine edema or a fixed deviation: it requires prompt drainage, irrigation, appropriate antimicrobial coverage and reapposition of mucoperichondrial flaps while associated trauma is assessed.",
    ),
    ("Post-Tonsillectomy Hemorrhage", "localize"): (
        "In post-tonsillectomy bleeding, why do a small visible fossa clot, repeated swallowing, or hematemesis still represent both a circulatory and airway emergency?",
        "Bleeding usually arises from the tonsillar fossae, with secondary hemorrhage often occurring as eschar separates during healing. The visible oral finding can underestimate swallowed blood and ongoing fossa bleeding. Hypovolemia, a full stomach, aspiration and airway contamination can coexist, especially in children, so resuscitation, suction, IV access, blood preparation and controlled operative evaluation must proceed together rather than waiting to identify a named vessel at bedside.",
    ),
    ("Tracheostomy Emergency", "localize"): (
        "When a patient with a neck stoma acutely cannot ventilate, how do tract maturity and total-laryngectomy anatomy determine where oxygenation and recannulation attempts must occur?",
        "First determine whether the patient has a tracheostomy with upper-airway continuity or a total-laryngectomy stoma with none. A fresh tracheostomy tract can close or false-pass, so blind forceful replacement is dangerous; oxygenate from above and at the stoma when anatomy permits while using endoscopic guidance and surgical help. A mature tract is generally safer to recannulate. After total laryngectomy, oral or nasal ventilation cannot reach the lungs: oxygenation and intubation must occur through the stoma.",
    ),
    ("Postoperative Neck Hematoma", "localize"): (
        "Why can a postoperative neck hematoma cause progressive airway obstruction even before the trachea appears markedly compressed, and why may intubation remain difficult after the incision is opened?",
        "Rising pressure in a relatively noncompliant neck obstructs venous and lymphatic drainage, producing rapidly progressive pharyngeal and laryngeal edema in addition to direct compression and displacement. That edema can persist after clot release, so waiting for hypoxemia or attempting repeated routine intubation is unsafe. With airway symptoms or a tense expanding wound, open the incision and evacuate clot immediately while mobilizing definitive airway and operative hemostasis.",
    ),
    ("Chyle Leak", "localize"): (
        "After low-neck surgery, which anatomy explains a new milky or feeding-responsive drain output, and what findings suggest a high-output leak with systemic consequences?",
        "The thoracic duct usually enters the venous system near the left internal-jugular/subclavian junction after an anatomically variable arch, so left level IV and root-of-neck dissection carry greatest risk, although right-sided lymphatic injury can occur. Confirm the feeding relationship and triglyceride-rich output when uncertain, quantify output and monitor volume, electrolytes, nutrition and immune loss. Persistent high output, wound compromise or respiratory consequences should prompt early procedural or operative escalation rather than diet changes alone.",
    ),
    ("Esophageal Perforation / Cervical Mediastinitis", "localize"): (
        "After difficult endoscopy or dilation, how do pain, crepitus, fever, and imaging distinguish a contained cervical perforation from contamination tracking into the mediastinum?",
        "The cervical esophagus lies behind the trachea and communicates with retropharyngeal and danger-space pathways into the mediastinum. Contrast-enhanced CT of neck and chest, often with a carefully selected water-soluble swallow study, should define air, fluid, extravasation, pleural involvement and whether the leak is contained. Size, location, delay, sepsis, obstruction, tissue quality and prior radiation determine whether strict nonoperative management is reasonable or urgent drainage, repair, diversion and thoracic source control are required.",
    ),
}


CURVEBALL_OVERRIDES = {
    "v136_rhi_24": "An internal nasal-valve problem requires treatment of the narrow lateral-wall–septal angle and dynamic sidewall support, not septoplasty or turbinate reduction alone. Identify static narrowing versus inspiratory collapse and choose targeted support such as spreader grafting, flaring sutures, lateral-wall reinforcement or another valve procedure while preserving dorsal and caudal septal support. Counsel that an untreated valve can leave persistent obstruction despite a straight septum.",
    "v137_tps_12": "Existing unilateral RLN paralysis makes the contralateral functioning nerve the patient's only mobile-fold motor supply; injury could create bilateral immobility and an immediate airway emergency. Confirm and document laryngoscopy, explain the possibility of tracheostomy and staged surgery, optimize localization and experienced nerve-preserving dissection, and reconsider the extent or timing of a nonurgent operation. If the contralateral signal is lost, stop before additional bilateral risk unless oncologic necessity clearly outweighs airway harm.",
    "v138_hn_25": "Suspect pharyngocutaneous fistula with fever, neck erythema or tenderness, increasing pain, salivary or foul drain output, wound edema, dehiscence, subcutaneous air, unexplained leukocytosis, or oral intake appearing in the wound. A sentinel neck bleed is especially ominous because saliva and infection can expose major vessels. Stop oral intake, assess the wound and neopharynx, protect the laryngectomy airway, obtain imaging when it changes drainage planning, and escalate early for debridement or vascularized coverage when conservative care is unsafe.",
    "v139_ped_07": "Single-stage reconstruction is favored when the child has a stable pulmonary course, manageable comorbidity, adequate airway above and below the stenosis, favorable vocal-fold function and swallowing, and can tolerate postoperative intubation without a tracheostomy safety valve. Double-stage reconstruction is favored with severe or multilevel disease, poor pulmonary reserve, significant aspiration, uncertain graft stability, prior failures or a need to retain the tracheostomy while healing. The choice is individualized around safe decannulation, not stenosis grade alone.",
    "v143_hno_05": "Internal-carotid encasement or skull-base extension changes a routine parapharyngeal resection into a vascular and cranial-nerve problem. Obtain high-resolution cross-sectional and angiographic imaging, define collateral cerebral circulation and involve skull-base, vascular and endovascular teams; selected cases may require balloon-occlusion assessment, reconstruction planning, subtotal treatment or nonsurgical therapy. Counsel explicitly about stroke, major hemorrhage, lower-cranial-nerve deficits, dysphagia, dysphonia, Horner syndrome, incomplete resection and the possibility that morbidity outweighs resection benefit.",
    "v144_oto_23": "At four months, correlate the persistent perforation with hearing, infection, Eustachian-tube function and ossicular status. Discuss continued observation when healing remains plausible and the ear is safe, versus office patching in selected small defects or myringoplasty/tympanoplasty using fat, fascia, perichondrium or cartilage according to size, location and risk. A meaningful air-bone gap also requires evaluation for ossicular injury or middle-ear disease, with ossiculoplasty added only when demonstrated rather than assuming closure alone will normalize hearing.",
    "v144_rh_19": "A caudal deviation involves the support and valve-bearing segment, so simple excision of the convex spur risks tip ptosis, columellar retraction and persistent obstruction. Mobilize and straighten the caudal septum with conservative scoring, suturing, batten grafting, repositioning on the nasal spine or extracorporeal reconstruction when necessary, then secure midline fixation while preserving an adequate L-strut. Reassess the internal and external valves because caudal correction may require simultaneous support rather than more cartilage removal.",
    "v145_hn_03": "A large Shamblin III carotid-body tumor encasing the ICA requires explicit planning for vascular control, stroke risk and possible arterial reconstruction or sacrifice. Obtain detailed angiographic imaging, assess skull-base extent and contralateral circulation, and coordinate vascular or endovascular expertise; selective embolization may be considered but does not eliminate cranial-nerve or stroke risk. Counsel about lower-cranial-nerve deficits, dysphagia, dysphonia, Horner syndrome, major blood loss, stroke and the possibility that observation or radiation offers a better morbidity tradeoff.",
    "v147_fp_11": "Full-thickness alar loss requires three-layer reconstruction: vascularized internal lining, structural support that recreates the alar rim and external valve, and skin cover matched in color and contour. A composite graft may work only for small, well-vascularized defects; larger losses often need staged local or regional lining and a cartilage graft plus a nasolabial or paramedian forehead flap. Reconstruct subunit boundaries and airway support, not merely surface skin, and avoid opposing poorly vascularized graft layers.",
    "v220_hn_fom_snr": "A segmental mandibular defect requires restoration of bony continuity, lower-face height and projection, occlusion, tongue support and a durable soft-tissue seal. Plan virtual or conventional osteotomies and a vascularized osseous flap—often fibula—around the resection and recipient vessels, with immediate implants only when oncologic, dental, radiation and patient factors support them. Coordinate prosthodontics early because plate position, bone height and skin-paddle design determine whether later dental rehabilitation is feasible.",
    "v221_hn_tl_app": "Conservative fistula care is unsafe with sepsis, an enlarging or uncontained leak, necrotic tissue, failure of drainage, exposed great vessels, sentinel bleeding, major wound breakdown, mediastinal extension, persistent high output, or failure to improve despite nutrition and wound care. These findings require operative exploration, debridement, drainage, closure when possible and introduction of well-vascularized tissue such as a pectoralis or free flap. Protect the laryngectomy stoma and secure vascular control urgently if the carotid is threatened.",
    "v221_hn_pps_snr": "A vagal schwannoma typically separates the internal jugular vein from the carotid artery and risks postoperative vocal-fold paralysis, dysphagia and other vagal deficits. A sympathetic-chain schwannoma more often displaces the carotid artery and jugular vein together without separating them and risks Horner syndrome. Imaging patterns are suggestive rather than absolute, so counsel from the nerve most likely at origin, document preoperative lower-cranial-nerve and sympathetic function, and discuss observation or nerve-sparing/subtotal strategies when preservation outweighs complete excision.",
    "v222_hn_cbp_snr": "Preoperative embolization may be considered for selected large, hypervascular carotid-body tumors when it is expected to reduce blood loss or facilitate safe dissection and experienced endovascular and surgical teams are available. It is not routine or risk-free: discuss embolic stroke, cranial-nerve ischemia, carotid injury or dissection, nontarget embolization, access complications and postembolization inflammation. Timing and target vessels must be coordinated with the operation, and embolization does not remove the need for proximal/distal vascular-control planning.",
    "v234_tps_reopthy_fnd": "Review the original indication, side and extent of resection, operative description of both RLNs and parathyroids, nerve-monitoring events, anatomic difficulty, complications and any implanted or autotransplanted tissue. Pathology should clarify diagnosis, tumor size and subtype, margins, extrathyroidal or vascular invasion, nodes removed and involved, and molecular findings. Combine that record with current laryngoscopy, imaging, biochemistry and the precise reoperative target so the plan avoids blind scar dissection and unnecessary bilateral risk.",
    "v234_tps_4g_fnd": "Superior glands arise from the fourth pouch and are usually posterior near the upper or mid thyroid and RLN entry region; ectopic superior glands often fall posteriorly into the tracheoesophageal groove, retroesophageal space or posterior mediastinum. Inferior glands descend with thymus from the third pouch and may lie near the lower pole, within the thyrothymic ligament or thymus, or in the anterior mediastinum; they can also be intrathyroidal. Search embryologically and confirm tissue rather than performing progressively hazardous random dissection.",
    "v241_ped_supra_app": "Preserve interarytenoid mucosa and avoid broad opposing raw surfaces across both arytenoids or aryepiglottic folds. Limit treatment to the structures actually collapsing, using controlled division of shortened folds and conservative reduction of redundant mucosa while protecting the true vocal folds and laryngeal inlet. Excess bilateral arytenoid or interarytenoid injury promotes scar bridging and supraglottic stenosis and may worsen swallowing; staged treatment is safer when the amount of tissue required is uncertain.",
    "v241_ped_ltr_fnd": "Expansion laryngotracheal reconstruction enlarges a narrowed framework by splitting the cricoid or laryngeal skeleton and inserting cartilage grafts, preserving the stenotic segment while increasing caliber. Cricotracheal resection removes the diseased subglottic or upper-tracheal segment and reanastomoses healthy airway, offering stronger correction for selected severe mature stenoses but adding anastomotic tension and recurrent-nerve risk. Length, level, grade, framework quality, comorbidity and prior reconstruction—not grade alone—determine candidacy.",
    "v241_ped_ltr_app": "Impaired vocal-fold abduction can leave a glottic bottleneck after an otherwise adequate subglottic reconstruction, while poor closure or baseline aspiration makes aggressive posterior expansion or glottic widening more hazardous. Define mobility, cricoarytenoid fixation, sensation, swallowing and pulmonary reserve before choosing graft direction, stenting and staging. Severe aspiration or uncertain bilateral motion may favor a staged reconstruction that retains the tracheostomy, a smaller expansion, or separate treatment of the glottic problem before decannulation.",
    "v251_lar_micro_snr": "Limited neck extension, cervical fusion or instability, prominent maxillary incisors, reduced oral opening, micrognathia or retrognathia, mandibular hardware, macroglossia, obesity, prior radiation and trismus predict difficult suspension. Document dentition and cervical precautions, review prior exposure notes and have alternative laryngoscopes, angled telescopes, flexible approaches and nonsuspension options ready. Protect teeth and stop escalating force when the target cannot be exposed safely; poor exposure should change the plan, not justify dental or pharyngeal injury.",
    "v254_lar_nodule_snr": "Return should be individualized to wound appearance, procedure extent, voice demand and the treating surgeon/voice therapist's protocol. Use an initial period of prescribed voice conservation, then gradual reintroduction of easy resonant phonation with hydration, reflux or irritant control when relevant, and correction of the phonotraumatic behavior that caused the lesions. Increase duration, loudness, pitch range and performance load stepwise; pain, rising effort, loss of range or deteriorating quality should trigger reassessment rather than pushing through a fixed calendar.",
    "v254_lar_polycyst_app": "Earlier surgery is more reasonable for a true subepithelial cyst with persistent focal stiffness and major occupational limitation, a pedunculated or hemorrhagic polyp unlikely to resolve, airway symptoms, diagnostic uncertainty, suspicious epithelial or vascular features, or failure of appropriate voice therapy and irritant control. Operative urgency is lower for a classic benign lesion with usable voice and modifiable phonotrauma. The procedure should use tissue-preserving microflap principles and address the contralateral reactive lesion conservatively.",
}


def apply_daily_curriculum_quality_v374(items):
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


def install_daily_curriculum_quality_v374(data_module, app_module):
    original_get_items = data_module.get_adaptive_items_v120

    def get_adaptive_items_v374():
        items = original_get_items()
        apply_daily_curriculum_quality_v374(items)
        return items

    data_module.get_adaptive_items_v120 = get_adaptive_items_v374

    def adaptive_question_v374(item):
        return item.get("daily_prompt") or item.get("prompt") or ""

    app_module._adaptive_question = adaptive_question_v374

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
