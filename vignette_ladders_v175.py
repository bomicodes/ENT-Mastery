"""v17.5 — Deliberate learning-ladder curation, Otology pass 7.

Reviews five additional v13.6 Otology foundations and adds missing application
and senior/chief decision layers without replacing strong foundation material.
"""


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong, pearl, curveball, focus):
    return {
        "id": qid,
        "domain": "Otology / Neurotology",
        "topic": topic,
        "learning_stage": stage,
        "stem": stem,
        "choices": choices,
        "answer": answer,
        "explanation": explanation,
        "why_wrong": why_wrong,
        "board_pearl": pearl,
        "curveball": curveball,
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "focus": focus,
    }


REVIEWED_FOUNDATION_IDS_V175 = {
    "v136_oto_16",  # Ototoxic / Noise-Induced Hearing Loss
    "v136_oto_17",  # Persistent Postural-Perceptual Dizziness (PPPD)
    "v136_oto_18",  # Petrous Apex Lesions
    "v136_oto_19",  # Temporal Bone Anatomy
    "v136_oto_20",  # Tympanic Membrane Perforation
}


VIGNETTES_V175 = [
    _q(
        "v175_oto_ototox_app", "Ototoxic / Noise-Induced Hearing Loss", "application",
        "A patient receiving cisplatin develops new bilateral high-frequency tinnitus and a measurable threshold shift on serial audiometry while cancer therapy is ongoing. What is the best next step?",
        ["Wait until conversational-frequency hearing is severely impaired", "Document the change promptly, communicate it to oncology, continue structured ototoxicity monitoring, and begin rehabilitation counseling while treatment risk-benefit is reassessed", "Place tympanostomy tubes", "Assume the change is temporary because otoscopy is normal"], 1,
        "Ototoxic monitoring is valuable only when early threshold shifts trigger communication and management. High-frequency change can precede major conversational-frequency loss, allowing oncologic risk-benefit discussion, prevention of additional exposure where possible, and earlier rehabilitation planning.",
        ["Waiting for severe disability defeats the purpose of surveillance.", "Correct. Monitoring should change care before hearing loss becomes advanced.", "Tubes do not treat cochlear hair-cell injury.", "Normal otoscopy is expected in sensorineural ototoxicity and does not make the loss transient."],
        "Ototoxicity programs are decision systems, not just serial audiograms.",
        "How would renal dysfunction, cumulative dose, or concurrent aminoglycoside exposure change risk assessment?",
        "boards",
    ),
    _q(
        "v175_oto_ototox_snr", "Ototoxic / Noise-Induced Hearing Loss", "senior_decision",
        "A critically ill patient requires an aminoglycoside for a resistant infection and already has baseline sensorineural hearing loss. What is the best senior-level principle?",
        ["Refuse the antibiotic regardless of infection severity", "Balance life-saving antimicrobial need against ototoxic risk, minimize avoidable exposure, optimize dosing and renal function, monitor hearing/vestibular symptoms when feasible, and use less-ototoxic alternatives when clinically equivalent", "Use two aminoglycosides to shorten treatment", "Assume preexisting hearing loss eliminates the value of monitoring"], 1,
        "Ototoxic risk must be integrated with the indication for the drug. When the medication is necessary, risk reduction includes appropriate dosing, renal monitoring, avoidance of synergistic ototoxins, baseline/serial assessment when feasible, and substitution only when an effective safer option exists.",
        ["Untreated severe infection may pose greater immediate harm than ototoxic risk.", "Correct. Senior care balances competing harms rather than treating ototoxicity in isolation.", "Stacking ototoxic agents increases risk without a general protective rationale.", "Preexisting loss increases the consequence of further injury and makes thoughtful monitoring more important, not less."],
        "The correct question is not 'Is this drug ototoxic?' but 'Is the exposure necessary, and how can harm be minimized without compromising the primary disease treatment?'",
        "What vestibular symptoms should prompt concern for aminoglycoside vestibulotoxicity even if pure-tone thresholds remain stable?",
        "overnight_call",
    ),

    _q(
        "v175_oto_pppd_app", "Persistent Postural-Perceptual Dizziness (PPPD)", "application",
        "Five months after compensated vestibular neuritis, a patient has daily nonspinning dizziness that worsens when upright, walking through grocery aisles, or viewing busy visual scenes. Neurologic examination is normal. Which diagnosis best fits?",
        ["Persistent postural-perceptual dizziness", "Posterior canal BPPV", "Acute cerebellar stroke", "Perilymphatic fistula"], 0,
        "PPPD is characterized by persistent nonspinning dizziness or unsteadiness on most days for at least several months, worsened by upright posture, motion, and complex visual stimuli, often after a vestibular precipitant has otherwise compensated.",
        ["Correct. The chronic visual-motion/postural pattern is classic.", "BPPV produces brief position-triggered attacks with characteristic positional nystagmus rather than continuous visual dependence.", "A stable five-month syndrome with normal neurologic exam and a typical trigger pattern is not an acute stroke presentation.", "A fistula is more associated with pressure/strain-related vestibular symptoms and relevant ear history."],
        "PPPD is diagnosed by the pattern of symptoms and triggers—not by requiring abnormal vestibular testing.",
        "How would frequent spontaneous episodes with photophobia or headache suggest vestibular migraine as a coexisting driver?",
        "boards",
    ),
    _q(
        "v175_oto_pppd_snr", "Persistent Postural-Perceptual Dizziness (PPPD)", "senior_decision",
        "A patient with PPPD has stopped driving, exercising, and entering stores because symptoms worsen with motion and visual complexity. The patient takes meclizine daily despite no acute spinning vertigo. What is the best management strategy?",
        ["Continue chronic vestibular suppressants and strict activity avoidance", "Use education, vestibular rehabilitation with graded exposure, treatment of migraine/anxiety contributors, and consider SSRI/SNRI therapy in selected patients while reducing chronic vestibular-suppressant dependence", "Perform labyrinthectomy", "Repeat Epley maneuvers indefinitely"], 1,
        "PPPD is maintained in part by maladaptive visual/postural dependence and avoidance. Treatment aims to restore movement tolerance and reduce threat responses using vestibular rehabilitation, graded exposure, and management of relevant psychiatric or migraine comorbidity; chronic suppressants can impede compensation.",
        ["Avoidance and long-term suppressants tend to reinforce disability rather than restore compensation.", "Correct. Treatment is active rehabilitation, not chronic suppression.", "A destructive vestibular operation is inappropriate for a functional persistent dizziness syndrome.", "Canalith maneuvers treat BPPV, not PPPD without positional nystagmus."],
        "For PPPD, the treatment target is reintegration with motion and visual environments—not elimination of every transient symptom before activity resumes.",
        "What exam or historical red flags would make you reopen the search for an uncompensated peripheral or central lesion?",
        "boards",
    ),

    _q(
        "v175_oto_petrous_app", "Petrous Apex Lesions", "application",
        "MRI shows an expansile petrous-apex lesion that is hyperintense on both T1- and T2-weighted sequences and does not demonstrate the marked diffusion restriction expected for cholesteatoma. What diagnosis is most likely?",
        ["Cholesterol granuloma", "Acute otitis externa", "Vestibular schwannoma", "Tympanosclerosis"], 0,
        "Petrous-apex cholesterol granuloma classically shows high T1 and high T2 signal from blood-breakdown products. Cholesteatoma/epidermoid-type lesions are typically characterized by diffusion restriction rather than intrinsic T1 hyperintensity.",
        ["Correct. The MRI phenotype is the key discriminator.", "External-canal infection does not produce this petrous-apex imaging pattern.", "Vestibular schwannoma arises from the vestibular nerve/CPA-IAC complex and has a different imaging phenotype.", "Tympanosclerosis is a middle-ear process, not an expansile T1-bright petrous-apex lesion."],
        "Petrous-apex diagnosis is often an MRI-sequence problem before it becomes a surgical-approach problem.",
        "Which CT and MRI features would instead favor petrous-apex cholesteatoma?",
        "boards",
    ),
    _q(
        "v175_oto_petrous_snr", "Petrous Apex Lesions", "senior_decision",
        "A symptomatic petrous-apex cholesterol granuloma causes sixth-nerve palsy. Imaging shows a favorable drainage corridor to the sphenoid sinus, while the carotid artery and cochlea make a lateral route higher risk. What is the best senior-level operative principle?",
        ["Use the same transmastoid route for every petrous-apex lesion", "Choose the safest durable drainage corridor based on lesion position and relationships to the carotid artery, cochlea, labyrinth, dura, and sphenoid sinus; an endonasal route may be preferable when anatomy is favorable", "Resect the cochlea routinely to improve access", "Observe despite progressive cranial neuropathy because all cholesterol granulomas are asymptomatic"], 1,
        "Petrous-apex route selection is anatomy-specific. The best approach reaches or drains the lesion while minimizing risk to the carotid artery, cochlea, labyrinth, cranial nerves, and dura. Endoscopic endonasal drainage can be attractive when the lesion abuts a safe sphenoid corridor.",
        ["No single corridor is universally safest.", "Correct. Senior planning chooses the route from the patient's anatomy, not from surgeon habit.", "Sacrificing normal hearing structures is not routine when a safer corridor exists.", "Progressive sixth-nerve dysfunction makes simple observation less attractive in a symptomatic expanding lesion."],
        "For petrous-apex surgery, approach selection is a geometry problem bounded by critical structures.",
        "What anatomic relationship would make an infracochlear or infralabyrinthine approach more attractive than an endonasal route?",
        "OR_prep",
    ),

    _q(
        "v175_oto_tbanat_app", "Temporal Bone Anatomy", "application",
        "During a facial recess approach, which structures define the surgical corridor?",
        ["Facial nerve medially, chorda tympani laterally, and fossa incudis/short process of the incus superiorly", "Carotid artery medially, sigmoid sinus laterally, and jugular bulb superiorly", "Tegmen medially, labyrinth laterally, and Eustachian tube superiorly", "Cochlea medially, external auditory canal laterally, and vestibule inferiorly"], 0,
        "The facial recess is bounded by the facial nerve medially, chorda tympani laterally, and the incus buttress/fossa incudis region superiorly. Understanding the corridor spatially is essential for posterior tympanotomy and cochlear-implant access.",
        ["Correct. These are the practical operative boundaries of the facial recess.", "Those structures describe other temporal-bone relationships, not the facial recess.", "The tegmen and labyrinth are important mastoid landmarks but do not define this corridor.", "These structures do not form the posterior tympanotomy boundaries."],
        "Temporal-bone anatomy should be learned as corridors and danger boundaries, not as isolated labels.",
        "What landmark helps locate the mastoid segment of the facial nerve before it is fully skeletonized?",
        "OR_prep",
    ),
    _q(
        "v175_oto_tbanat_snr", "Temporal Bone Anatomy", "senior_decision",
        "During mastoidectomy, the surgeon loses orientation in a poorly pneumatized temporal bone. The tegmen is low, the sigmoid sinus is anterior, and the lateral semicircular canal has not yet been confidently identified. What is the safest next step?",
        ["Continue drilling deeply until the middle ear appears", "Re-establish known landmarks and safe cortical boundaries before proceeding deeper, using preoperative imaging and anatomic relationships rather than blind depth", "Drill directly medial to the presumed canal wall", "Use the facial nerve monitor as a substitute for anatomic orientation"], 1,
        "When orientation is uncertain, the safe response is to stop and rebuild the three-dimensional map from trusted landmarks. Variant anatomy and contracted mastoids narrow safe corridors, and monitoring does not replace knowledge of the tegmen, sigmoid, canal wall, labyrinth, and facial nerve relationships.",
        ["Blind deeper drilling converts uncertainty into injury risk.", "Correct. Senior temporal-bone surgery prioritizes orientation before progress.", "A presumed landmark is not a safe basis for medial drilling.", "Monitoring can warn about neural proximity but cannot identify all critical temporal-bone structures or replace anatomy."],
        "When you are lost in the temporal bone, the solution is not more drilling—it is reorientation.",
        "Which CT features should make you anticipate a narrow facial recess or unusually anterior sigmoid sinus preoperatively?",
        "OR_prep",
    ),

    _q(
        "v175_oto_tmperf_app", "Tympanic Membrane Perforation", "application",
        "A patient has a small dry traumatic central tympanic-membrane perforation with mild conductive hearing loss one week after a slap injury. There is no vertigo, facial weakness, or infection. What is the best initial management?",
        ["Dry-ear precautions and observation with follow-up because many traumatic perforations close spontaneously", "Immediate tympanomastoidectomy", "Routine aminoglycoside drops despite no infection", "Repeated water irrigation to prevent crusting"], 0,
        "Most uncomplicated traumatic perforations heal spontaneously. Initial management is protection from water and contamination, documentation of hearing, and follow-up; surgery is reserved for persistent defects or associated injuries.",
        ["Correct. Observation is appropriate for an uncomplicated early traumatic perforation.", "There is no mastoid disease or other indication for immediate mastoidectomy.", "Unnecessary potentially ototoxic topical therapy should be avoided when the middle ear is exposed.", "Water exposure increases contamination risk and does not promote closure."],
        "Traumatic TM perforation is usually a protect-and-reassess problem unless the associated findings say otherwise.",
        "Which symptoms or audiometric findings would make ossicular or inner-ear injury more likely?",
        "boards",
    ),
    _q(
        "v175_oto_tmperf_snr", "Tympanic Membrane Perforation", "senior_decision",
        "Four months after trauma, a dry 40% tympanic-membrane perforation remains unchanged and the patient has persistent conductive hearing loss. What is the best next step?",
        ["Continue indefinite observation because traumatic perforations always close eventually", "Discuss definitive repair such as tympanoplasty after confirming middle-ear status and evaluating whether the hearing loss is explained by the perforation alone", "Perform labyrinthectomy", "Treat with chronic systemic antibiotics"], 1,
        "A persistent dry perforation beyond the expected healing interval warrants consideration of tympanoplasty, especially with functional hearing loss or water-exposure limitations. The preoperative evaluation should ensure that ossicular injury or other middle-ear pathology is not being missed.",
        ["Persistent stable defects may not close spontaneously after several months.", "Correct. The decision now shifts from observation to repair planning and mechanism assessment.", "Labyrinthectomy is destructive and unrelated to a conductive deficit from a TM defect.", "There is no active infection requiring chronic antibiotics."],
        "Before repairing a chronic traumatic perforation, make sure the conductive loss is proportional to the membrane defect; a larger gap can signal ossicular injury.",
        "How would anterior location, Eustachian-tube dysfunction, or active otorrhea alter technique or timing?",
        "OR_prep",
    ),
]


def apply_learning_ladders_v175(challenges, id_factory):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reviewed = 0
    for qid in REVIEWED_FOUNDATION_IDS_V175:
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v17.5: reviewed foundation missing from live registry: {qid}")
        q["learning_stage"] = "foundation"
        q["ladder_reviewed"] = True
        reviewed += 1

    existing = {q.get("id") for q in challenges if q.get("id")}
    added = 0
    for q in VIGNETTES_V175:
        item = dict(q)
        if item["id"] in existing:
            continue
        item["concept_id"] = id_factory(item["domain"], item["topic"])
        item["ladder_reviewed"] = True
        challenges.append(item)
        existing.add(item["id"])
        added += 1

    return {
        "reviewed_foundations": reviewed,
        "added_questions": added,
        "topics": sorted({q["topic"] for q in VIGNETTES_V175}),
    }
