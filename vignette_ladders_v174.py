"""v17.4 — Deliberate learning-ladder curation, Otology pass 6.

Reviews the next five v13.6 Otology foundations and adds only missing
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


REVIEWED_FOUNDATION_IDS_V174 = {
    "v136_oto_11",  # Hyperacusis / Decreased Sound Tolerance
    "v136_oto_12",  # Lateral Skull-Base Tumor Framework
    "v136_oto_13",  # Neurotologic Intraoperative Cranial-Nerve Monitoring
    "v136_oto_14",  # Otologic Manifestations of Systemic Disease
    "v136_oto_15",  # Otosclerosis / Stapes Fixation
}


VIGNETTES_V174 = [
    _q(
        "v174_oto_hyper_app", "Hyperacusis / Decreased Sound Tolerance", "application",
        "A patient with a normal audiogram reports that ordinary dishes clinking and traffic noise are painfully loud. The patient has begun wearing maximum-attenuation earplugs all day and symptoms are worsening. What is the best management principle?",
        ["Encourage even more continuous sound avoidance", "Confirm the decreased-sound-tolerance phenotype, address migraine/anxiety or other contributors, and use counseling with gradual sound exposure rather than reinforcing excessive avoidance", "Perform stapedotomy", "Diagnose malingering because thresholds are normal"], 1,
        "Hyperacusis can be disabling despite normal thresholds. Excessive sound avoidance may increase vigilance and central gain, so treatment generally emphasizes education, controlled sound exposure, and management of relevant comorbid contributors rather than universal earplug dependence.",
        ["Continuous overprotection can reinforce sound intolerance outside genuinely hazardous noise environments.", "Correct. The treatment target is functional sound tolerance, not maximal acoustic isolation.", "Stapes surgery treats fixation, not primary hyperacusis.", "Normal pure-tone thresholds do not invalidate decreased sound tolerance."],
        "Hyperacusis is a loudness-tolerance problem, not necessarily a hearing-threshold problem.",
        "How would misophonia and loudness recruitment differ clinically from hyperacusis?",
        "boards",
    ),
    _q(
        "v174_oto_hyper_snr", "Hyperacusis / Decreased Sound Tolerance", "senior_decision",
        "A patient labeled with hyperacusis reports autophony, hears eye movements, develops vertigo with loud sound and pressure, and has an apparent low-frequency conductive gap despite normal tympanometry. What is the best next decision?",
        ["Continue sound therapy alone because all sound intolerance is functional", "Evaluate for a third-window disorder such as superior semicircular canal dehiscence before treating this as isolated hyperacusis", "Place tympanostomy tubes", "Start systemic antibiotics"], 1,
        "Autophony, sound/pressure-induced vestibular symptoms, and a low-frequency air-bone gap with normal middle-ear mechanics suggest a third-window physiology rather than isolated decreased sound tolerance. The diagnostic frame should shift accordingly.",
        ["The associated vestibular and conductive-appearing findings are not explained by simple hyperacusis.", "Correct. Senior reasoning asks whether sound intolerance is a symptom of another otologic disorder.", "Normal tympanometry and third-window clues make tubes inappropriate.", "There is no infectious syndrome."],
        "When hyperacusis comes with autophony, Tullio phenomenon, or pressure-induced vertigo, look for a third window before labeling it primary.",
        "Which audiometric, VEMP, and CT findings would strengthen the diagnosis while avoiding overcalling incidental radiographic dehiscence?",
        "boards",
    ),

    _q(
        "v174_oto_sbtumor_app", "Lateral Skull-Base Tumor Framework", "application",
        "A patient has pulsatile tinnitus, lower cranial neuropathies, and a highly vascular enhancing jugular-foramen mass with a salt-and-pepper MRI appearance. What is the most useful next management framework?",
        ["Biopsy transcanally before vascular assessment", "Define cranial-nerve function, vascular supply, growth, catecholamine status when relevant, patient age/comorbidity, and goals before choosing observation, radiation, or surgery", "Assume vestibular schwannoma and schedule translabyrinthine resection", "Ignore hearing and swallowing function because tumor control is the only endpoint"], 1,
        "Jugular-foramen paraganglioma management is individualized. The decision depends on biology, vascularity, cranial-nerve function, growth, patient factors, and treatment morbidity; indiscriminate biopsy of a vascular skull-base lesion can be hazardous.",
        ["Highly vascular skull-base lesions should not be casually biopsied without defining the vascular diagnosis and risk.", "Correct. Skull-base treatment starts with localization, biology, function, and patient goals.", "The compartment and imaging phenotype do not fit a routine vestibular schwannoma framework.", "Lower cranial-nerve, hearing, swallowing, and quality-of-life outcomes are central to management."],
        "At the lateral skull base, the correct treatment is determined by compartment, biology, and functional cost—not by size alone.",
        "When would angiography or preoperative embolization meaningfully alter planning?",
        "OR_prep",
    ),
    _q(
        "v174_oto_sbtumor_snr", "Lateral Skull-Base Tumor Framework", "senior_decision",
        "A 78-year-old with mild dysphonia but otherwise intact lower cranial-nerve function has a slowly growing jugular paraganglioma. Definitive resection would likely require sacrifice of multiple lower cranial nerves. What is the best senior-level principle?",
        ["Operate because complete resection is always superior to preserving function", "Balance tumor control against expected cranial-nerve morbidity; observation or radiation may be preferable when surgical cure would impose disproportionate functional loss", "Biopsy repeatedly until the tumor shrinks", "Delay discussion of swallowing and aspiration until after treatment"], 1,
        "For many benign or indolent lateral skull-base tumors, treatment morbidity can exceed disease morbidity. Older age, slow growth, and preserved function may shift management toward surveillance or radiation rather than aggressive resection with predictable lower cranial-nerve deficits.",
        ["Oncologic completeness is not automatically the best endpoint for indolent benign disease when functional cost is high.", "Correct. Chief-level judgment explicitly weighs natural history against treatment morbidity.", "Repeated biopsy is not a treatment and may be dangerous in a vascular tumor.", "Swallowing, aspiration, voice, and airway consequences should be anticipated before treatment selection."],
        "For benign skull-base disease, preserving function may be more important than achieving an anatomic cure at any cost.",
        "How would documented rapid growth, brainstem compression, or catecholamine secretion change the balance?",
        "boards",
    ),

    _q(
        "v174_oto_monitor_app", "Neurotologic Intraoperative Cranial-Nerve Monitoring", "application",
        "During cerebellopontine-angle surgery, free-run facial EMG becomes suddenly sustained during tumor traction. What is the best immediate response?",
        ["Increase traction to finish the dissection quickly", "Stop the provoking maneuver, irrigate and reassess the field, allow recovery, and modify the dissection before proceeding", "Ignore the activity because only direct stimulation matters", "Intentionally divide the nerve to eliminate the signal"], 1,
        "Sustained neurotonic EMG can reflect mechanical, thermal, or ischemic facial-nerve stress. Monitoring is useful only if a concerning change alters surgical behavior before irreversible injury occurs.",
        ["More traction increases the suspected mechanism of injury.", "Correct. A warning signal should trigger a change in operative maneuver.", "Free-run activity supplies information distinct from direct stimulation thresholds.", "The purpose of monitoring is nerve preservation, not elimination of the monitored structure."],
        "Monitoring is not a scoreboard; it is a real-time feedback system whose value depends on changing the operation when the nerve is stressed.",
        "How do free-run EMG, direct stimulation threshold, and motor-evoked potentials answer different questions?",
        "OR_prep",
    ),
    _q(
        "v174_oto_monitor_snr", "Neurotologic Intraoperative Cranial-Nerve Monitoring", "senior_decision",
        "Near the end of vestibular schwannoma resection, the facial nerve is anatomically intact but the proximal stimulation threshold has risen substantially and the response amplitude has fallen. A thin layer of adherent tumor remains on the nerve. What is the best senior-level principle?",
        ["Pursue gross-total resection regardless of worsening nerve physiology", "Consider leaving a small adherent remnant if further dissection is likely to convert a functioning nerve into a permanent palsy, then manage the remnant with surveillance or adjunctive treatment as appropriate", "Cut the nerve and graft it immediately because the threshold changed", "Ignore monitoring if the nerve looks continuous"], 1,
        "When facial-nerve physiology deteriorates during removal of densely adherent benign tumor, the marginal oncologic benefit of complete removal may be outweighed by permanent facial dysfunction. Intentional near-total or subtotal resection can be appropriate in selected cases.",
        ["Gross-total resection is not an absolute goal when the functional price is disproportionate.", "Correct. Senior skull-base judgment integrates tumor biology, remnant control options, and facial-nerve function.", "An anatomically intact nerve with residual response should not be sacrificed solely because thresholds worsened.", "Visual continuity does not guarantee physiologic integrity; monitoring adds important functional information."],
        "In benign CPA surgery, a tiny controllable remnant can be a better outcome than a perfectly clean MRI with a permanently paralyzed face.",
        "How would the decision differ for an aggressive malignant lesion encasing the facial nerve?",
        "OR_prep",
    ),

    _q(
        "v174_oto_systemic_app", "Otologic Manifestations of Systemic Disease", "application",
        "A patient with granulomatosis with polyangiitis has persistent otitis media, mixed hearing loss, and new facial weakness despite ventilation tubes and repeated antibiotics. What is the best interpretation?",
        ["This is routine recurrent otitis media and should be managed only with more tubes", "The ear findings may represent active systemic inflammatory disease and require coordination of systemic evaluation and immunosuppressive management in addition to local ear care", "The hearing loss proves otosclerosis", "Facial weakness excludes autoimmune disease"], 1,
        "Granulomatous and autoimmune disease can involve the middle ear, cochlea, and facial nerve. Persistent atypical disease despite appropriate local treatment should prompt assessment of systemic activity rather than endless treatment of the ear as an isolated infection.",
        ["Repeated local procedures may treat consequences but not the inflammatory driver.", "Correct. Ear disease can be a manifestation of systemic vasculitis.", "Mixed loss and inflammatory ear disease do not establish stapes fixation.", "Facial neuropathy can occur with inflammatory or granulomatous temporal-bone disease."],
        "When ear disease behaves unlike ordinary ear disease, widen the frame beyond the temporal bone.",
        "Which laboratory, imaging, and biopsy findings would help distinguish infection from granulomatous inflammation?",
        "boards",
    ),
    _q(
        "v174_oto_systemic_snr", "Otologic Manifestations of Systemic Disease", "senior_decision",
        "A patient receiving immunosuppression for systemic vasculitis develops worsening otalgia, granulation tissue, and cranial neuropathy. Inflammatory markers are elevated. What is the safest next decision?",
        ["Assume every new ear symptom is autoimmune and immediately escalate immunosuppression", "Urgently evaluate for invasive infection such as skull-base osteomyelitis before attributing deterioration to autoimmune flare, because immunosuppression changes both risk and presentation", "Stop all diagnostic testing because inflammatory markers cannot help", "Treat with topical anesthetic alone"], 1,
        "Immunosuppressed patients can develop dangerous infection that mimics inflammatory disease. Escalating immunosuppression without excluding invasive infection may be catastrophic; the senior approach reassesses the differential and obtains cultures/imaging as appropriate.",
        ["Anchoring on the known autoimmune diagnosis can miss a superimposed infection.", "Correct. Immunosuppression raises the stakes of distinguishing flare from infection.", "Inflammatory markers are nonspecific but can be useful in context and longitudinally.", "Cranial neuropathy with invasive-appearing ear disease requires far more than symptomatic therapy."],
        "A known systemic diagnosis should widen—not narrow—the differential when the clinical pattern changes.",
        "How would you coordinate biopsy or culture timing if both infection and inflammatory disease remain plausible?",
        "overnight_call",
    ),

    _q(
        "v174_oto_otoscl_app", "Otosclerosis / Stapes Fixation", "application",
        "A 34-year-old has progressive conductive hearing loss, normal tympanic membranes, absent acoustic reflexes, and a Carhart notch. Speech discrimination is excellent. Which management options are most appropriate?",
        ["Discuss amplification versus stapes surgery based on hearing goals, anatomy, and risk tolerance", "Treat with prolonged antibiotics", "Perform labyrinthectomy", "Place tympanostomy tubes as definitive therapy"], 0,
        "Classic stapes fixation can be treated with appropriately fitted hearing amplification or stapedotomy/stapedectomy in suitable candidates. Selection depends on functional goals, audiometry, anatomy, and informed acceptance of surgical risks.",
        ["Correct. Both amplification and surgery are legitimate pathways for bothersome conductive loss from otosclerosis.", "Otosclerosis is not an infectious process.", "Labyrinthectomy destroys vestibular function and hearing and is unrelated to stapes fixation.", "Tubes do not correct a fixed stapes footplate."],
        "The diagnosis may be classic, but treatment is preference-sensitive: hearing aid and stapes surgery are both real options.",
        "What audiometric or examination features would make you question the diagnosis before operating?",
        "boards",
    ),
    _q(
        "v174_oto_otoscl_snr", "Otosclerosis / Stapes Fixation", "senior_decision",
        "A patient referred for stapes surgery has a low-frequency air-bone gap, normal tympanometry, present acoustic reflexes, prominent autophony, and sound-induced vertigo. What is the best next decision?",
        ["Proceed with stapedotomy because every conductive gap with a normal drum is otosclerosis", "Stop and evaluate for a third-window disorder before stapes surgery", "Place a tympanostomy tube", "Treat with systemic steroids"], 1,
        "A conductive-appearing gap with preserved reflexes plus autophony and Tullio-type symptoms is not a typical stapes-fixation phenotype. Third-window disorders can mimic otosclerosis, and stapes surgery in the wrong diagnosis can fail to help or worsen vestibular symptoms.",
        ["The physiologic and symptom pattern conflicts with classic stapes fixation.", "Correct. Senior operative judgment includes knowing when not to operate on an apparently straightforward audiogram.", "A tube does not treat third-window physiology.", "Steroids do not correct the suspected mechanical inner-ear shunt."],
        "Before stapes surgery, prove the conductive mechanism; a third-window mimic is a classic setup for the wrong operation.",
        "How would an only-hearing ear change your counseling even when the diagnosis truly is otosclerosis?",
        "OR_prep",
    ),
]


def apply_learning_ladders_v174(challenges, id_factory):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reviewed = 0
    for qid in REVIEWED_FOUNDATION_IDS_V174:
        q = by_id.get(qid)
        if q is None:
            raise RuntimeError(f"v17.4: reviewed foundation missing from live registry: {qid}")
        q["learning_stage"] = "foundation"
        q["ladder_reviewed"] = True
        reviewed += 1

    existing = {q.get("id") for q in challenges if q.get("id")}
    added = 0
    for q in VIGNETTES_V174:
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
        "topics": sorted({q["topic"] for q in VIGNETTES_V174}),
    }
