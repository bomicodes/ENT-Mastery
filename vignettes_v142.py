"""v14.2 — balanced second-case depth pass for the six lowest-depth domains.

Adds a second decision-heavy vignette to 18 high-yield singleton topics.
Emphasis: boards, overnight call, and OR anatomy/decision making. Every target
is validated against the live canonical curriculum at import time.
"""


def Q(qid, domain, topic, stem, choices, answer, explanation, pearl, curveball, focus="boards"):
    return {
        "id": qid, "domain": domain, "topic": topic, "stem": stem,
        "choices": choices, "answer": answer, "explanation": explanation,
        "why_wrong": ["Use the mechanism, anatomy, and management priority in the explanation to distinguish this choice." for _ in choices],
        "board_pearl": pearl, "curveball": curveball, "focus": focus,
        "tier": "Curated chief/call/OR", "mode": "Vignette",
    }


VIGNETTES_V142 = [
    Q('v142_oto_01', 'Otology / Neurotology', 'Necrotizing Otitis Externa',
      'A 74-year-old with poorly controlled diabetes has severe nocturnal otalgia, persistent otorrhea, granulation tissue at the bony-cartilaginous junction, and new House-Brackmann IV facial weakness. What is the best next step?',
      ['Treat as invasive skull-base infection with urgent imaging, culture-directed antipseudomonal therapy, and evaluation of cranial neuropathy', 'Topical drops alone and routine follow-up', 'Immediate stapedectomy', 'Reassure because facial weakness is expected in uncomplicated otitis externa'], 0,
      'Cranial neuropathy in a high-risk patient with refractory otitis externa is a red flag for necrotizing otitis externa/skull-base osteomyelitis. Management requires systemic antipseudomonal therapy, microbiologic diagnosis, imaging to define extent, and close multidisciplinary follow-up.',
      'New cranial nerve dysfunction converts an ear-canal infection into a skull-base emergency until proven otherwise.',
      'If inflammatory markers improve but MRI marrow signal remains abnormal, which clinical and laboratory trends are more useful for judging response?', 'overnight_call'),

    Q('v142_oto_02', 'Otology / Neurotology', 'Otosclerosis / Stapes Fixation',
      'A patient with a classic conductive hearing loss, absent acoustic reflexes, normal tympanic membrane, and good cochlear reserve elects stapes surgery. During the operation the footplate is mobile rather than fixed. What is the best response?',
      ['Stop and reassess the diagnosis/ossicular chain rather than performing a routine stapedotomy', 'Create a fenestra anyway because the audiogram proves otosclerosis', 'Remove the incus', 'Perform labyrinthectomy'], 0,
      'Stapes surgery is predicated on stapes fixation. An unexpectedly mobile footplate should prompt reassessment for another cause of conductive loss such as ossicular discontinuity or congenital anomaly; proceeding reflexively risks inner-ear injury without treating the true mechanism.',
      'In otologic surgery, the intraoperative mechanical finding can overrule the preoperative label.',
      'What preoperative finding would make superior canal dehiscence an important alternative explanation for an air-bone gap?', 'OR_prep'),

    Q('v142_oto_04', 'Otology / Neurotology', 'Temporal Bone Anatomy',
      'During a transmastoid facial recess approach for cochlear implantation, which boundaries define the facial recess that must be respected to enter the middle ear safely?',
      ['Facial nerve medially/posteriorly, chorda tympani laterally, and fossa incudis superiorly', 'Sigmoid sinus, tegmen, and mastoid tip', 'Carotid artery, jugular bulb, and Eustachian tube', 'Superior semicircular canal, endolymphatic sac, and vestibular aqueduct'], 0,
      'The facial recess is opened between the mastoid segment of the facial nerve and chorda tympani, with the fossa incudis superiorly. Precise identification prevents facial nerve/chorda injury and gives access to the round-window niche.',
      'Know operative anatomy as three-dimensional boundaries, not isolated structure names.',
      'If the facial nerve is anomalously anterior and obscures the round window, what alternative cochlear access strategies can be considered?', 'OR_prep'),

    Q('v142_rhi_01', 'Rhinology / Allergy / Skull Base', 'Endoscopic CSF Leak Repair / Nasoseptal Flap',
      'A patient has a high-flow intraoperative CSF leak after expanded endonasal skull-base resection. Which reconstruction principle most directly lowers postoperative leak risk?',
      ['Use a vascularized pedicled nasoseptal flap as part of a multilayer closure when feasible', 'Pack the nose without defining the defect', 'Use only free mucosal graft regardless of flow', 'Leave the defect open for secondary healing'], 0,
      'High-flow skull-base defects generally need robust multilayer reconstruction, commonly incorporating a vascularized nasoseptal flap supplied by the posterior septal branch of the sphenopalatine artery.',
      'Plan the reconstructive flap before tumor exposure can injure its pedicle.',
      'What prior septal surgery or tumor involvement can compromise the nasoseptal flap and what alternatives remain?', 'OR_prep'),

    Q('v142_rhi_02', 'Rhinology / Allergy / Skull Base', 'Frontal Sinusotomy / Draf Procedures',
      'A patient has persistent frontal sinus disease after prior complete ethmoidectomy and standard frontal sinusotomy, with severe bilateral frontal recess scarring. Which operation creates a common drainage pathway by removing the superior nasal septum and frontal sinus floor between the orbits?',
      ['Draf III (modified endoscopic Lothrop)', 'Draf I', 'Simple maxillary antrostomy', 'Sphenoidotomy'], 0,
      'A Draf III creates a wide common frontal neo-ostium by removing the frontal sinus floor bilaterally and the superior septum. It is reserved for selected refractory or anatomically difficult frontal disease.',
      'Frontal surgery is escalation by anatomy: know exactly what bone each Draf procedure removes.',
      'Which structures set the lateral and posterior safety limits during a Draf III?', 'OR_prep'),

    Q('v142_rhi_04', 'Rhinology / Allergy / Skull Base', 'Revision FESS',
      'Before revision FESS in a patient with distorted landmarks and recurrent disease, what is the most important operative planning step?',
      ['Re-review thin-cut CT in all three planes and deliberately identify residual partitions, skull base, orbit, frontal drainage pathway, and prior surgical changes', 'Assume normal landmarks remain where expected', 'Rely only on navigation without understanding anatomy', 'Begin with blind posterior ethmoid dissection'], 0,
      'Revision surgery carries increased risk because landmarks may be absent or displaced. Systematic CT review and a landmark-based dissection plan are essential; navigation supplements but does not replace anatomy.',
      'Navigation tells you where the instrument is; it does not tell you what operation is safe.',
      'Which stable landmarks are especially useful when the middle turbinate has been partially resected?', 'OR_prep'),

    Q('v142_lar_01', 'Laryngology / Voice / Swallowing', 'Injection Laryngoplasty',
      'A patient has acute unilateral vocal fold paralysis after skull-base surgery with a large glottic gap, weak cough, and aspiration, but meaningful nerve recovery remains possible. What is a reasonable early intervention?',
      ['Temporary injection augmentation to improve closure while awaiting recovery', 'Immediate permanent bilateral cordotomy', 'Observe despite recurrent aspiration because intervention prevents nerve recovery', 'Total laryngectomy'], 0,
      'Temporary injection laryngoplasty can improve voice, cough, and swallowing during the recovery window without committing the patient to a permanent framework procedure.',
      'Early augmentation treats glottic insufficiency; it does not prevent neural recovery.',
      'How do injection material duration and expected recovery interval influence material choice?', 'OR_prep'),

    Q('v142_lar_02', 'Laryngology / Voice / Swallowing', 'Medialization Thyroplasty',
      'A patient has stable chronic unilateral vocal fold paralysis with persistent breathy dysphonia and a posterior glottic gap despite adequate medialization during trial injection. What additional procedure may improve closure?',
      ['Arytenoid adduction combined with type I thyroplasty in selected patients', 'Posterior cordotomy', 'Cricotracheal resection', 'Tonsillectomy'], 0,
      'Type I thyroplasty addresses membranous glottic insufficiency; arytenoid adduction can address vertical height mismatch and a persistent posterior gap in selected unilateral paralysis.',
      'Framework surgery should match the geometry of the insufficiency, not merely the diagnosis of paralysis.',
      'Why is intraoperative voice assessment useful during an awake/monitored thyroplasty?', 'OR_prep'),

    Q('v142_lar_04', 'Laryngology / Voice / Swallowing', 'Stroboscopy Interpretation',
      'Stroboscopy shows a persistent focal absence of mucosal wave over a unilateral lesion while the contralateral fold has normal wave. What does this finding most strongly suggest?',
      ['A lesion tethering or replacing the pliable superficial lamina propria, such as scar, cyst, or invasive pathology depending on context', 'Normal vibration', 'Isolated nasal obstruction', 'Bilateral recurrent laryngeal nerve paralysis'], 0,
      'A focal absent or markedly reduced mucosal wave suggests impaired pliability at that site. Interpretation must be integrated with lesion morphology, closure pattern, symmetry, periodicity, and oncologic risk.',
      'Stroboscopy is a tissue-mechanics exam: wave abnormalities tell you where the cover is no longer behaving normally.',
      'Why can severe aperiodicity make standard stroboscopy misleading and when is high-speed imaging useful?', 'boards'),

    Q('v142_fpt_01', 'Facial Plastics / Trauma', 'Open Rhinoplasty Fundamentals',
      'During an open rhinoplasty, which maneuver most directly improves exposure of the nasal tip cartilages while preserving vascularity and soft-tissue integrity?',
      ['Careful transcolumellar/marginal incisions with elevation in the proper avascular plane over the lower lateral cartilages', 'Random full-thickness tip excision', 'Circumferential devascularization of the columella', 'Subperiosteal dissection across the entire upper lip'], 0,
      'Open rhinoplasty provides broad exposure through transcolumellar and marginal incisions; meticulous plane selection and soft-tissue handling preserve vascularity and minimize scar/edema.',
      'Exposure is useful only if the dissection preserves the soft-tissue envelope you need for the final contour.',
      'What vascular or skin-risk factors make aggressive tip thinning especially hazardous?', 'OR_prep'),

    Q('v142_fpt_03', 'Facial Plastics / Trauma', 'Periocular Reconstruction',
      'After lower-eyelid Mohs surgery, a full-thickness defect involves more than half of the lid width. Which reconstructive principle is essential?',
      ['Reconstruct both anterior and posterior lamellae, providing vascularized support to at least one lamella', 'Use skin graft alone for every layer', 'Leave the tarsal defect unsupported', 'Tighten the upper lip instead'], 0,
      'Large full-thickness eyelid defects require restoration of both lamellae and stable lid support while minimizing vertical tension that can cause ectropion.',
      'Periocular reconstruction succeeds when the eyelid remains apposed to the globe, not merely when the hole is closed.',
      'How does a defect involving the medial canthus change concern for the lacrimal drainage system?', 'OR_prep'),

    Q('v142_fpt_04', 'Facial Plastics / Trauma', 'Septal Perforation',
      'A patient with a symptomatic anterior septal perforation has crusting, bleeding, and whistling despite humidification. Before considering surgical closure, what is most important?',
      ['Identify and control the underlying cause and optimize mucosal health before attempting bilateral mucosal flap closure', 'Immediately enlarge the perforation', 'Place a spreader graft without addressing mucosa', 'Ignore cocaine/vasculitis history because etiology does not affect repair'], 0,
      'Successful septal perforation repair depends on etiology, size/location, healthy vascularized mucosa, and tension-free multilayer closure. Ongoing trauma, vasculitis, cocaine exposure, or severe inflammation undermines repair.',
      'A perforation is a wound-healing problem before it is a hole-closing problem.',
      'Why are large posterior defects often less symptomatic yet technically harder to close?', 'OR_prep'),

    Q('v142_tps_01', 'Thyroid / Parathyroid / Salivary', 'Anaplastic Thyroid Cancer',
      'An older patient has a rapidly enlarging fixed thyroid mass, stridor, dysphagia, and bilateral vocal fold impairment. Biopsy is suspicious for anaplastic thyroid carcinoma. What is the immediate management priority?',
      ['Rapid multidisciplinary airway and oncologic assessment with urgent molecular testing and staging, avoiding a reflexive morbid resection before resectability/biology are defined', 'Routine outpatient observation', 'RAI as definitive first-line therapy', 'Elective lobectomy without airway planning'], 0,
      'Anaplastic thyroid cancer is an oncologic and airway emergency. Management requires rapid confirmation, airway strategy, staging/resectability assessment, and molecular testing because targeted therapy can be important in actionable disease.',
      'In ATC, an uncontrolled airway can become the first fatal complication; plan it before the patient crashes.',
      'Why can tracheostomy be technically difficult or harmful in a bulky invasive anterior neck tumor, and when is it nevertheless required?', 'overnight_call'),

    Q('v142_tps_02', 'Thyroid / Parathyroid / Salivary', 'Central Neck Dissection',
      'During thyroid cancer surgery, which boundaries best describe the central neck nodal compartment relevant to a level VI dissection?',
      ['Hyoid superiorly, innominate/brachiocephalic region inferiorly, and carotid sheaths laterally, with prelaryngeal, pretracheal and paratracheal nodes', 'Mandibular angle to clavicle lateral to SCM', 'Only the submental triangle', 'Retropharyngeal space only'], 0,
      'The central compartment contains prelaryngeal, pretracheal, and paratracheal nodes and lies between the carotid sheaths. Surgery requires deliberate protection of both recurrent laryngeal nerves and parathyroid blood supply.',
      'A central neck dissection is a defined compartment operation, not removal of whatever nodes are visible.',
      'How does a therapeutic dissection on the right differ anatomically near the recurrent laryngeal nerve and innominate artery?', 'OR_prep'),

    Q('v142_tps_04', 'Thyroid / Parathyroid / Salivary', 'Reoperative Hyperparathyroidism',
      'A patient has persistent hypercalcemia after prior bilateral neck exploration. Before reoperation, what is the most important principle?',
      ['Confirm the biochemical diagnosis and obtain concordant high-quality localization before a focused reoperative plan', 'Re-explore immediately without localization', 'Assume every case is parathyroid carcinoma', 'Remove the thyroid gland empirically'], 0,
      'Reoperative parathyroid surgery carries higher RLN and hypoparathyroidism risk. Biochemical reconfirmation, review of prior pathology/operative notes, and careful localization with complementary imaging are critical.',
      'In the reoperative neck, localization is not optional convenience—it is risk reduction.',
      'When localization remains negative despite unequivocal disease, how do expert-center referral and alternative imaging fit the plan?', 'OR_prep'),

    Q('v142_ped_01', 'Pediatric Otolaryngology', 'Laryngomalacia',
      'A 3-month-old has inspiratory stridor worse with feeding and supine positioning, poor weight gain, recurrent cyanotic spells, and significant supraglottic collapse on flexible laryngoscopy. What is the best management?',
      ['Supraglottoplasty is appropriate for severe laryngomalacia after assessing comorbid contributors', 'Reassurance alone regardless of growth or hypoxemia', 'Tonsillectomy', 'Chronic racemic epinephrine at home'], 0,
      'Most laryngomalacia is observed, but severe disease with failure to thrive, hypoxemia/apnea, significant feeding compromise, or cardiopulmonary consequences is an indication for operative treatment.',
      'Severity is defined by physiology and feeding/growth—not by how loud the stridor is.',
      'Which synchronous airway lesions or neurologic comorbidities increase the chance of persistent symptoms after supraglottoplasty?', 'OR_prep'),

    Q('v142_ped_02', 'Pediatric Otolaryngology', 'Pediatric Tracheostomy / Decannulation',
      'A tracheostomy-dependent child is being considered for decannulation. Which evaluation is most important before removing the tube?',
      ['Confirm that the original indication has resolved and assess airway patency, secretion burden, respiratory reserve, sleep/gas exchange, and ability to tolerate capping per protocol', 'Remove the tube solely because of age', 'Ignore suprastomal collapse', 'Decannulate during an acute respiratory infection'], 0,
      'Safe pediatric decannulation is multidisciplinary and protocol-driven. Airway endoscopy is often used to identify granulation, suprastomal collapse, stenosis, or persistent obstruction, while capping/sleep assessment evaluates physiologic readiness.',
      'Decannulation is an airway and respiratory-reserve decision, not simply a tube-size decision.',
      'What endoscopic finding would need correction before a capping trial despite otherwise good pulmonary status?', 'boards'),

    Q('v142_ped_03', 'Pediatric Otolaryngology', 'Subglottic Hemangioma',
      'A 2-month-old develops progressive biphasic stridor and has a segmental beard-distribution cutaneous hemangioma. Endoscopy shows a compressible subglottic vascular lesion. What is first-line disease-directed therapy in most cases?',
      ['Systemic propranolol after appropriate cardiovascular assessment', 'Repeated traumatic biopsy', 'Radiation therapy', 'Immediate total laryngectomy'], 0,
      'Infantile subglottic hemangioma typically proliferates in early infancy and responds dramatically to beta-blocker therapy such as propranolol. Airway severity still determines urgency and need for adjunctive intervention.',
      'A beard-distribution hemangioma plus progressive infant stridor should trigger an airway hemangioma evaluation.',
      'What clinical circumstances require securing the airway before waiting for propranolol response?', 'overnight_call'),
]
