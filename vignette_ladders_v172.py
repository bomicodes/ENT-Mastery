"""v17.2 — Deliberate learning-ladder curation, Otology pass 4.

Reviews five v13.6 Otology foundations and adds only the missing application and
senior/chief decision layers. Generic foundation distractors remain intact; the
new layers carry individualized distractor teaching and explicit learning stage.
"""


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong,
       pearl, curveball, focus):
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


REVIEWED_FOUNDATION_IDS_V172 = {
    "v136_oto_01",  # Acute Otitis Externa
    "v136_oto_02",  # Age-Related Hearing Loss / Presbycusis
    "v136_oto_03",  # Audiologic Electrophysiology / ABR-OAE-ECoG
    "v136_oto_04",  # Auditory Neuroanatomy / Cochlear Physiology
    "v136_oto_05",  # Cochlear Implant Failure / Revision
}


VIGNETTES_V172 = [
    _q(
        "v172_oto_aoe_app", "Acute Otitis Externa", "application",
        "A 70-year-old with diabetes presents with severe otalgia and canal edema. After careful debridement, the canal is diffusely inflamed but there is no granulation tissue, cranial neuropathy, fever, or extension beyond the canal. What is the best treatment plan?",
        ["Topical antipseudomonal therapy with optimized delivery, analgesia, water precautions, and close reassessment", "Immediate skull-base surgery", "Systemic steroids alone", "No treatment because diabetes explains the pain"], 0,
        "Even in a high-risk host, uncomplicated acute otitis externa is primarily treated topically. The key is reliable drug delivery through an edematous canal, pain control, dry-ear precautions, and a low threshold to reassess for necrotizing disease if the course is atypical.",
        [
            "Correct. Host risk increases vigilance but does not automatically convert every canal infection into skull-base osteomyelitis.",
            "Skull-base surgery is not initial therapy for uncomplicated canal-limited infection.",
            "Steroids alone do not treat the bacterial infection and may worsen glycemic control.",
            "Diabetes raises concern for complications; it never makes severe otalgia a reason to withhold treatment."
        ],
        "For otitis externa, first decide whether disease is canal-limited or has crossed into necrotizing/skull-base infection.",
        "What failure-to-improve interval and exam findings would make you escalate the workup rather than simply changing ear drops?",
        "boards",
    ),
    _q(
        "v172_oto_aoe_snr", "Acute Otitis Externa", "senior_decision",
        "The same diabetic patient returns with deep nocturnal pain out of proportion to the canal exam, granulation tissue at the bony-cartilaginous junction, and new facial weakness. What is the safest next decision?",
        ["Continue the same topical drops alone for another month", "Treat this as suspected necrotizing otitis externa/skull-base osteomyelitis with urgent imaging, culture-directed systemic antipseudomonal therapy, metabolic optimization, and cranial-nerve assessment", "Perform an Epley maneuver", "Reassure because facial weakness is common in simple swimmer's ear"], 1,
        "Pain out of proportion, granulation tissue, a high-risk host, and cranial neuropathy should trigger an immediate shift from routine otitis externa to necrotizing external otitis/skull-base osteomyelitis. Management requires defining extent, obtaining cultures when feasible, systemic therapy, diabetes control, and close multidisciplinary follow-up.",
        [
            "Topical therapy alone is inadequate once invasive skull-base disease is suspected.",
            "Correct. The chief-level move is recognizing that the disease category has changed and escalating both diagnostic and therapeutic intensity.",
            "Canalith repositioning is unrelated to invasive external-ear infection.",
            "Cranial neuropathy is a red flag for skull-base extension, not an expected feature of uncomplicated otitis externa."
        ],
        "In a diabetic patient, new cranial neuropathy plus relentless otalgia is skull-base disease until proven otherwise.",
        "How would you use ESR/CRP and imaging over time when clinical symptoms improve more quickly than radiographic abnormalities?",
        "overnight_call",
    ),

    _q(
        "v172_oto_presby_app", "Age-Related Hearing Loss / Presbycusis", "application",
        "A 76-year-old has gradually progressive bilateral high-frequency sensorineural hearing loss, but the right ear now has substantially poorer word recognition than the left despite similar pure-tone thresholds. What is the best next step?",
        ["Attribute the asymmetry to age and fit identical hearing aids without further evaluation", "Evaluate the asymmetric speech performance for retrocochlear or other unilateral pathology while addressing hearing rehabilitation", "Treat with antibiotics", "Order tympanostomy tubes"], 1,
        "Typical presbycusis is broadly symmetric. Disproportionately poor unilateral word recognition or meaningful asymmetric SNHL should reopen the differential for retrocochlear disease rather than being dismissed as normal aging.",
        [
            "Age does not explain away a new asymmetric audiometric red flag.",
            "Correct. Rehabilitation and diagnostic evaluation can proceed in parallel.",
            "There is no infectious middle-ear syndrome here.",
            "Tubes do not treat sensorineural loss or asymmetric speech discrimination."
        ],
        "Presbycusis is common, but common diagnoses do not erase asymmetric or disproportionate speech findings.",
        "What audiometric asymmetry or associated symptoms would strengthen your threshold for MRI of the internal auditory canals?",
        "boards",
    ),
    _q(
        "v172_oto_presby_snr", "Age-Related Hearing Loss / Presbycusis", "senior_decision",
        "An 82-year-old with bilateral severe age-related SNHL uses well-fit hearing aids consistently but still has very poor aided sentence understanding and major communication disability. Cognition and medical status are adequate for rehabilitation. What is the best next decision?",
        ["Increase hearing-aid gain indefinitely regardless of aided speech performance", "Refer for formal cochlear-implant evaluation rather than assuming advanced age precludes implantation", "Stop amplification because speech testing is poor", "Perform stapedotomy"], 1,
        "When optimized amplification no longer provides useful speech understanding, the problem has moved beyond routine hearing-aid adjustment. Chronologic age alone is not a contraindication to cochlear implantation; functional aided performance, medical fitness, cognition, anatomy, and goals should drive evaluation.",
        [
            "More gain does not solve poor cochlear speech discrimination and may worsen comfort or distortion.",
            "Correct. Senior care recognizes when amplification has reached its functional ceiling and escalates appropriately.",
            "Poor aided performance is a reason to consider another rehabilitation strategy, not to abandon communication support.",
            "Stapes surgery treats conductive fixation, not severe sensorineural presbycusis."
        ],
        "The endpoint of hearing-aid management is useful communication, not simply device ownership.",
        "How would frailty, dementia severity, manual dexterity, and caregiver support influence candidacy counseling without using age as a blanket exclusion?",
        "boards",
    ),

    _q(
        "v172_oto_ephys_app", "Audiologic Electrophysiology / ABR-OAE-ECoG", "application",
        "An infant has absent or grossly abnormal ABR waveforms but preserved otoacoustic emissions and a present cochlear microphonic. Tympanometry is normal. Which interpretation best fits the physiology?",
        ["Auditory neuropathy spectrum disorder with preserved outer-hair-cell function but impaired neural synchrony", "Ossicular discontinuity", "Typical presbycusis", "Posterior canal BPPV"], 0,
        "Preserved OAEs/cochlear microphonic show functioning outer hair cells, while an abnormal ABR indicates failure of synchronous neural transmission. That dissociation is characteristic of auditory neuropathy spectrum disorder.",
        [
            "Correct. The pattern localizes the dysfunction beyond ordinary outer-hair-cell loss.",
            "A conductive lesion would alter sound transmission and does not create the classic preserved cochlear microphonic with neural desynchrony pattern.",
            "Presbycusis is an acquired age-related cochlear disorder, not an infant electrophysiologic dissociation.",
            "BPPV is vestibular and does not explain abnormal auditory evoked potentials."
        ],
        "Read electrophysiology by generator: OAE = outer hair cell; cochlear microphonic = cochlear receptor potential; ABR = synchronous auditory neural conduction.",
        "How can middle-ear effusion confound OAEs and ABR thresholds, and what test helps keep you from mislocalizing the problem?",
        "boards",
    ),
    _q(
        "v172_oto_ephys_snr", "Audiologic Electrophysiology / ABR-OAE-ECoG", "senior_decision",
        "A child with suspected auditory neuropathy has inconsistent behavioral responses, preserved OAEs, markedly abnormal ABR, and MRI showing severe bilateral cochlear nerve deficiency. The family asks whether cochlear implantation will predictably restore speech understanding. What is the best counseling principle?",
        ["Promise normal speech because the cochlea is structurally present", "Explain that cochlear nerve integrity is a major determinant of implant benefit and that severe nerve deficiency substantially limits predictability, requiring individualized habilitation and device counseling", "Recommend stapedotomy", "Ignore MRI because ABR is the only relevant test"], 1,
        "Cochlear implantation bypasses hair-cell transduction but still depends on an adequate cochlear nerve and central auditory pathway. Severe cochlear nerve deficiency therefore changes prognosis and may prompt discussion of limited benefit or alternative auditory rehabilitation strategies in specialized centers.",
        [
            "A structurally present cochlea does not guarantee an adequate neural substrate for implant benefit.",
            "Correct. Senior interpretation integrates electrophysiology, anatomy, behavioral testing, development, and family goals.",
            "Stapes surgery treats conductive fixation and is irrelevant here.",
            "MRI provides essential anatomic information about the neural substrate that ABR alone cannot supply."
        ],
        "Electrophysiology tells you how the pathway behaves; MRI can tell you whether the neural substrate needed for rehabilitation is actually present.",
        "When might an auditory brainstem implant enter discussion, and why is candidacy far narrower than for routine cochlear implantation?",
        "OR_prep",
    ),

    _q(
        "v172_oto_neuro_app", "Auditory Neuroanatomy / Cochlear Physiology", "application",
        "A patient with a unilateral pontine lesion has difficulty localizing sound but does not have complete deafness in either ear. Which neuroanatomic principle best explains this?",
        ["Auditory pathways have substantial bilateral projection above the cochlear nuclei", "Each auditory cortex receives input only from the ipsilateral cochlea", "The ossicles compensate for brainstem lesions", "The vestibular nuclei carry all auditory information"], 0,
        "After the cochlear nuclei, auditory information ascends through bilateral brainstem projections. Therefore unilateral central lesions usually impair localization, timing, and complex processing more than they cause complete monaural deafness.",
        [
            "Correct. Bilateral central representation is the key localization principle.",
            "Strict ipsilateral cortical representation would predict unilateral central deafness, which is not how the pathway is organized.",
            "Middle-ear mechanics cannot compensate for a central auditory lesion.",
            "Vestibular nuclei process balance-related signals rather than carrying the primary ascending auditory pathway."
        ],
        "Peripheral lesions can make one ear deaf; unilateral central lesions usually distort processing because central auditory representation is bilateral.",
        "Which lesions before the first major bilateral projections can still produce a predominantly ipsilateral peripheral hearing deficit?",
        "boards",
    ),
    _q(
        "v172_oto_neuro_snr", "Auditory Neuroanatomy / Cochlear Physiology", "senior_decision",
        "After skull-base surgery, a patient has normal pure-tone thresholds but suddenly struggles to understand rapid speech in noise and localize sound. Otoscopy and tympanometry are normal. What is the best next approach?",
        ["Assume the complaint is nonorganic because thresholds are normal", "Use targeted speech-in-noise/central auditory assessment and correlate the deficit with the surgical neuroanatomy rather than relying on pure-tone thresholds alone", "Place tympanostomy tubes", "Treat empirically for otosclerosis"], 1,
        "Pure-tone detection is only one auditory function. Central pathway injury can impair binaural timing, localization, and complex speech processing while leaving threshold audiometry relatively intact. Evaluation should match the functional complaint and lesion anatomy.",
        [
            "Normal thresholds do not prove normal central auditory processing.",
            "Correct. The senior decision is to select testing that interrogates the function actually lost.",
            "Normal middle-ear mechanics make tubes irrelevant.",
            "Otosclerosis produces a conductive pattern, not isolated postoperative central processing difficulty."
        ],
        "A normal audiogram can coexist with disabling central auditory dysfunction; test the pathway function that the patient says is failing.",
        "How would unilateral eighth-nerve injury, cochlear synaptopathy, or cortical disease produce different testing patterns?",
        "OR_prep",
    ),

    _q(
        "v172_oto_cirev_app", "Cochlear Implant Failure / Revision", "application",
        "A long-term cochlear-implant user has an abrupt performance drop after a fall. External hardware exchange does not restore function, and integrity testing shows abnormal electrode impedances. What is the best next step?",
        ["Increase map levels repeatedly without investigating hardware", "Obtain focused device integrity assessment and imaging for migration or hardware failure, with revision/reimplantation considered if failure is confirmed", "Treat as otitis media regardless of the ear exam", "Tell the patient internal devices cannot be revised"], 1,
        "Sudden loss of previously stable implant performance requires a structured failure evaluation: external components, programming, impedances/integrity testing, imaging, and medical causes. Confirmed internal device failure or electrode migration can require revision surgery.",
        [
            "Repeated programming cannot correct a mechanically displaced or electrically failed internal array.",
            "Correct. The mechanism of failure should be defined before revision planning.",
            "Infection should be treated when present, but it should not be invented to explain objective device abnormalities.",
            "Internal cochlear implants can be revised or reimplanted when indicated."
        ],
        "For implant performance loss, first classify the problem: external equipment, programming, medical, electrode position, soft failure, or hard failure.",
        "What imaging and operative considerations become important when trauma has displaced an otherwise intact electrode array?",
        "OR_prep",
    ),
    _q(
        "v172_oto_cirev_snr", "Cochlear Implant Failure / Revision", "senior_decision",
        "A cochlear-implant recipient develops progressive postauricular skin breakdown with exposed receiver hardware and recurrent drainage despite appropriate antibiotics. Device performance is declining. What is the best senior-level principle?",
        ["Continue indefinite suppressive antibiotics over exposed hardware", "Treat this as a threatened or established implant infection/extrusion problem and plan definitive surgical management, which may require explantation with staged or selected immediate reimplantation depending on infection and tissue conditions", "Cover the exposed device with a hearing-aid earmold", "Ignore the wound if some electrical function remains"], 1,
        "Exposed or chronically infected implanted hardware is difficult to sterilize medically because of biofilm and compromised soft-tissue coverage. Definitive management may require device removal, wound control, and later or selected immediate reimplantation based on infection severity, organism, anatomy, and tissue quality.",
        [
            "Suppressive antibiotics rarely solve exposed biofilm-bearing hardware with failing soft-tissue coverage.",
            "Correct. Senior planning balances infection control, auditory deprivation, tissue reconstruction, and the feasibility/timing of reimplantation.",
            "An earmold cannot provide vascularized coverage or eradicate implant infection.",
            "Residual electrical function does not make chronically exposed hardware safe."
        ],
        "CI revision is not only an electronics problem; infection, biofilm, skin viability, and preservation of future cochlear access can dominate the plan.",
        "How would meningitis risk, cochlear ossification, or an only-hearing implanted ear influence timing of reimplantation?",
        "OR_prep",
    ),
]


def apply_learning_ladders_v172(challenges, id_factory):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reviewed = 0
    for qid in REVIEWED_FOUNDATION_IDS_V172:
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v17.2: reviewed foundation missing from live registry: {qid}")
        q["learning_stage"] = "foundation"
        q["ladder_reviewed"] = True
        reviewed += 1

    existing = {q.get("id") for q in challenges if q.get("id")}
    added = 0
    for q in VIGNETTES_V172:
        item = dict(q)
        if item["id"] in existing:
            continue
        item["concept_id"] = id_factory(item["domain"], item["topic"])
        item["ladder_reviewed"] = True
        item["curation_version"] = "v17.2"
        challenges.append(item)
        existing.add(item["id"])
        added += 1

    return {
        "reviewed_foundations": reviewed,
        "added_questions": added,
        "topics": sorted({q["topic"] for q in VIGNETTES_V172}),
    }
