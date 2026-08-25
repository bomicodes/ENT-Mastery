"""v17.3 — Deliberate learning-ladder curation, Otology pass 5.

Reviews five additional v13.6 Otology foundations and adds only missing
application and senior/chief decision layers.
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


REVIEWED_FOUNDATION_IDS_V173 = {
    "v136_oto_06",  # Cochlear Implant Surgery
    "v136_oto_07",  # Congenital Inner-Ear Malformations
    "v136_oto_08",  # Cortical Neuroplasticity in Hearing Loss
    "v136_oto_09",  # Eustachian Tube Dysfunction
    "v136_oto_10",  # Hearing Aids and Bone-Conduction Devices
}


VIGNETTES_V173 = [
    _q(
        "v173_oto_cisurg_app", "Cochlear Implant Surgery", "application",
        "During routine cochlear implantation through a facial recess approach, the surgeon has excellent round-window exposure and useful residual low-frequency hearing. Which insertion strategy best supports hearing preservation?",
        ["Perform a generous promontory cochleostomy and rapidly advance the array", "Use a slow atraumatic scala-tympani insertion through the round window or closely adjacent opening while minimizing suction, drilling trauma, and force", "Disarticulate the ossicular chain to improve electrode mobility", "Enter the vestibule if the first few electrodes meet resistance"], 1,
        "Residual-hearing preservation depends on minimizing mechanical and acoustic trauma, maintaining scala-tympani placement, avoiding forceful advancement, and limiting unnecessary drilling or suction near the cochlea. The round window is often favorable when anatomy permits.",
        ["A larger cochleostomy and rapid insertion increase trauma rather than reduce it.", "Correct. Atraumatic technique and scala-tympani placement are the key physiologic goals.", "Ossicular disarticulation does not facilitate cochlear electrode insertion and sacrifices conductive function.", "The vestibule is not an alternative route for a routine cochlear electrode and risks major inner-ear injury."],
        "In CI surgery, the technical endpoint is not merely 'electrode in cochlea'—it is atraumatic, appropriately positioned insertion with durable fixation.",
        "What intraoperative or postoperative findings would make you suspect scalar translocation or tip fold-over?",
        "OR_prep",
    ),
    _q(
        "v173_oto_cisurg_snr", "Cochlear Implant Surgery", "senior_decision",
        "A child with profound SNHL has a very contracted mastoid, an anteriorly displaced facial nerve, and limited safe access to the round window on preoperative imaging. What is the best senior-level planning principle?",
        ["Use the standard posterior tympanotomy regardless of anatomy", "Plan the operative corridor around the aberrant facial-nerve and middle-ear anatomy, considering alternative approaches or modified exposure rather than forcing a routine facial recess", "Abandon implantation because every malformed temporal bone is contraindicated", "Drill through the facial nerve if it blocks the shortest route"], 1,
        "Cochlear implantation is an anatomy-dependent operation. Aberrant facial-nerve position and limited round-window access may require modified exposure or alternative approaches. The goal is safe cochlear access without treating the standard facial recess as mandatory.",
        ["A standard approach is useful only when the anatomy makes it safe.", "Correct. Senior planning adapts the operation to the temporal-bone anatomy rather than the reverse.", "Many challenging congenital anatomies remain implantable in experienced centers.", "Sacrificing an intact facial nerve for routine electrode access is inappropriate."],
        "Preoperative CT is an operative map, not a documentation exercise; variant facial-nerve anatomy can completely change the route.",
        "How would a prior canal-wall-down mastoid cavity change receiver placement, electrode routing, and infection counseling?",
        "OR_prep",
    ),

    _q(
        "v173_oto_malf_app", "Congenital Inner-Ear Malformations", "application",
        "A child with profound congenital SNHL has incomplete partition anatomy, a widened cochlear aperture, and a present but small cochlear nerve. Which issue should be emphasized before cochlear implantation?",
        ["The operation carries no additional risks once hearing loss is profound", "There may be increased risk of CSF/perilymph gusher and atypical facial-nerve anatomy, and auditory outcome may be less predictable when the cochlear nerve is hypoplastic", "Stapedectomy is required before implantation", "MRI is unnecessary if CT already shows the cochlea"], 1,
        "Inner-ear malformations alter both surgical risk and expected auditory benefit. Widened communications can predispose to gusher, facial-nerve anatomy may be abnormal, and cochlear-nerve hypoplasia can limit performance even when electrode insertion is technically successful.",
        ["Profound loss does not erase anatomy-specific surgical or outcome risk.", "Correct. Counseling must cover both operative hazards and neural substrate.", "Stapes surgery does not correct congenital profound SNHL in this setting.", "MRI is important for evaluating the cochlear nerve and other soft-tissue anatomy not adequately characterized by CT."],
        "For congenital SNHL, ask two separate questions: can I safely place an electrode, and is there enough neural substrate to benefit from it?",
        "Which malformation patterns are most associated with a large intraoperative gusher?",
        "OR_prep",
    ),
    _q(
        "v173_oto_malf_snr", "Congenital Inner-Ear Malformations", "senior_decision",
        "A child with profound bilateral SNHL has cochlear aplasia on CT and absent cochlear nerves on high-resolution MRI. The family asks for cochlear implantation because hearing aids provide no benefit. What is the best next counseling step?",
        ["Proceed with standard cochlear implantation because profound loss alone defines candidacy", "Explain that cochlear implantation requires an implantable cochlea and functional cochlear nerve; refer to a specialized implant center to discuss whether an auditory brainstem implant or non-auditory communication strategy is appropriate", "Offer bilateral stapedotomy", "Delay all language intervention until school age"], 1,
        "A cochlear implant requires both an anatomic cochlear target and a neural pathway to stimulate. Cochlear aplasia with absent cochlear nerves makes conventional CI ineffective, so counseling must shift toward specialized alternatives and immediate language access rather than repeated routine CI evaluation.",
        ["Audiometric severity alone cannot overcome absent target anatomy.", "Correct. This is a candidacy boundary, not merely a difficult insertion.", "Stapes surgery is irrelevant to absent cochlear anatomy and nerve.", "Early communication access is crucial; delaying language intervention compounds auditory deprivation."],
        "Not every profound congenital hearing loss is a cochlear-implant problem; anatomy can move the patient into an entirely different rehabilitation pathway.",
        "What additional developmental and family factors should be discussed when counseling about auditory brainstem implantation?",
        "boards",
    ),

    _q(
        "v173_oto_plastic_app", "Cortical Neuroplasticity in Hearing Loss", "application",
        "A toddler with congenital profound bilateral SNHL has had minimal auditory access despite appropriately fit hearing aids. Why does prolonged delay in effective auditory stimulation matter?",
        ["The ossicles progressively fuse without sound", "Sensitive-period auditory cortical development can be altered by deprivation, reducing later speech and language potential even if sound is restored", "The tympanic membrane becomes permanently atrophic", "Hearing aids prevent cortical development"], 1,
        "Early auditory experience shapes cortical organization during sensitive developmental periods. Prolonged deprivation can lead to cross-modal and maladaptive reorganization, so later access to sound may not fully recover the speech-language potential available with earlier effective stimulation.",
        ["Ossicular fixation is not the mechanism of developmental auditory deprivation.", "Correct. The key biologic issue is time-sensitive cortical development.", "Tympanic-membrane change is not the central determinant of language outcome here.", "Appropriately fitted amplification supports rather than blocks auditory development."],
        "Early hearing intervention is a neurodevelopmental treatment, not just a device-fitting decision.",
        "Why is the effect of delayed implantation different in an adult who had normal hearing through childhood and then became deaf?",
        "boards",
    ),
    _q(
        "v173_oto_plastic_snr", "Cortical Neuroplasticity in Hearing Loss", "senior_decision",
        "A 17-year-old with congenital profound bilateral deafness has never used amplification consistently and communicates fluently with sign language. The family asks whether cochlear implantation will predictably provide open-set speech understanding. What is the best counseling principle?",
        ["Promise the same outcome expected in a recently deafened postlingual adult", "Explain that long-standing congenital auditory deprivation substantially limits predictability of speech-perception benefit, while respecting the patient's established communication mode and goals", "Decline evaluation solely because sign language is used", "Recommend implantation only if the patient agrees to stop signing"], 1,
        "Duration and timing of auditory deprivation strongly affect cortical readiness for spoken-language processing. Late implantation after congenital profound deafness can provide sound awareness and variable benefit, but open-set speech outcomes are much less predictable than in postlingually deafened patients.",
        ["Postlingual auditory pathways have prior language organization that this patient never developed through hearing.", "Correct. Counseling should be realistic, individualized, and goal-based.", "Use of sign language is not itself a contraindication to respectful implant evaluation.", "Communication identity and access should not be made conditional on abandoning sign language."],
        "The same audiogram can carry very different implant prognoses depending on when auditory deprivation began and how long it lasted.",
        "How would evidence of prior meaningful spoken-language development change prognosis?",
        "boards",
    ),

    _q(
        "v173_oto_etd_app", "Eustachian Tube Dysfunction", "application",
        "An adult reports chronic ear pressure and intermittent muffled hearing. Otoscopy shows mild tympanic-membrane retraction and tympanometry repeatedly demonstrates negative middle-ear pressure. Which finding would most support obstructive rather than patulous Eustachian tube dysfunction?",
        ["Autophony of breathing that improves when supine", "Respiratory movement of the tympanic membrane", "Persistent negative middle-ear pressure with retraction", "Symptoms triggered only by exercise and dehydration"], 2,
        "Obstructive ETD produces inadequate middle-ear ventilation, negative pressure, and retraction. Patulous ETD instead produces abnormal openness with autophony of voice/breathing and may show tympanic-membrane movement with respiration.",
        ["Positional relief of breathing autophony is classic for patulous ETD.", "Respiratory tympanic-membrane movement supports a patulous tube.", "Correct. Objective negative pressure is a key obstructive phenotype.", "Exercise and dehydration more often exacerbate patulous symptoms."],
        "Do not equate 'ear fullness' with obstructive ETD; establish the physiologic phenotype before treating the tube.",
        "What common disorders can mimic obstructive ETD despite a normal tympanogram and normal drum?",
        "boards",
    ),
    _q(
        "v173_oto_etd_snr", "Eustachian Tube Dysfunction", "senior_decision",
        "A 56-year-old develops a new unilateral persistent middle-ear effusion without a recent URI. What is the most important next management principle?",
        ["Proceed directly to balloon dilation without examining the nasopharynx", "Evaluate the nasopharynx and skull-base region for an obstructing lesion while also managing the effusion", "Assume age-related ETD and observe indefinitely", "Treat with vestibular suppressants"], 1,
        "New persistent unilateral adult effusion requires evaluation for a mechanical obstructive cause, including nasopharyngeal pathology. Treating the ear alone can miss the disease responsible for the Eustachian-tube dysfunction.",
        ["Balloon dilation should not precede evaluation for an obstructing lesion.", "Correct. The senior move is to identify why one adult Eustachian tube suddenly stopped functioning.", "Indefinite observation risks delayed diagnosis of an obstructing mass.", "Vestibular suppressants do not treat middle-ear effusion or Eustachian-tube obstruction."],
        "Adult unilateral effusion is a diagnostic sign, not merely a tube-placement indication.",
        "How would epistaxis, cranial neuropathy, or cervical adenopathy change the urgency and imaging plan?",
        "overnight_call",
    ),

    _q(
        "v173_oto_bcd_app", "Hearing Aids and Bone-Conduction Devices", "application",
        "A patient with congenital unilateral canal atresia has a normal cochlea and cannot wear a conventional air-conduction aid on the affected side. Which rehabilitation strategy most directly bypasses the external and middle ear?",
        ["Bone-conduction device", "Cochlear implant", "Systemic corticosteroids", "Vestibular implant"], 0,
        "Bone-conduction devices transmit acoustic information through skull vibration to a functioning cochlea, bypassing an unusable external canal and conductive apparatus.",
        ["Correct. This matches the site of deficit while preserving use of the normal cochlea.", "A cochlear implant bypasses hair-cell transduction and is not the first-line solution for an intact cochlea with purely conductive obstruction.", "Steroids do not correct congenital canal atresia.", "Vestibular implants address balance pathways, not conductive hearing loss."],
        "Match the rehabilitation device to the lesion: air-conduction aid uses the canal, bone conduction bypasses it, CI bypasses damaged cochlear transduction.",
        "What factors determine whether a nonsurgical headband/adhesive device or implanted bone-conduction system is preferable?",
        "boards",
    ),
    _q(
        "v173_oto_bcd_snr", "Hearing Aids and Bone-Conduction Devices", "senior_decision",
        "An adult with single-sided deafness asks whether a bone-conduction implant will restore normal binaural hearing and sound localization. What is the best counseling response?",
        ["Yes; routing sound to the better cochlea recreates normal binaural processing", "Explain that bone-conduction routing can improve awareness of sound from the deaf side and reduce head-shadow effects, but it does not restore true binaural input to the deaf ear", "No device can improve any functional deficit from single-sided deafness", "The device works by regenerating the cochlear nerve"], 1,
        "In single-sided deafness, a bone-conduction routing system sends sound from the deaf side to the functioning cochlea. That can improve access to sound but does not recreate two independently stimulated auditory pathways, so localization and binaural cues remain limited.",
        ["Routing to one cochlea cannot reproduce interaural timing and level differences processed from two ears.", "Correct. Device counseling should distinguish improved access from restoration of binaural hearing.", "Routing devices can meaningfully improve head-shadow-related listening even if they do not restore binaural physiology.", "Bone-conduction systems transmit sound; they do not regenerate neural tissue."],
        "For single-sided deafness, ask whether the device routes sound to one good cochlea or actually stimulates the deaf auditory pathway—those are not equivalent goals.",
        "How does this counseling differ when discussing cochlear implantation for selected single-sided deafness patients?",
        "boards",
    ),
]


def apply_learning_ladders_v173(challenges, id_factory):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reviewed = 0
    for qid in REVIEWED_FOUNDATION_IDS_V173:
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v17.3: reviewed foundation missing from live registry: {qid}")
        q["learning_stage"] = "foundation"
        q["ladder_reviewed"] = True
        reviewed += 1

    existing = {q.get("id") for q in challenges if q.get("id")}
    added = 0
    for q in VIGNETTES_V173:
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
        "topics": sorted({q["topic"] for q in VIGNETTES_V173}),
    }
