"""v16.9 — Deliberate learning-ladder curation, Otology pass 1.

This pass reviews five canonical Otology concepts whose existing v12.4 cases are
strong foundations but do not deliberately span application and senior/chief
reasoning. We preserve those foundations, explicitly tag them, and add only the
missing layers. New cases use stable IDs, individualized distractor teaching,
and concept IDs are assigned by the live merge layer.
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


# Existing v12.4 questions deliberately reviewed and retained as foundations.
REVIEWED_FOUNDATION_IDS_V169 = {
    "v124_oto_02",  # Tympanometry / Acoustic Reflexes
    "v124_oto_03",  # Temporal Bone Fracture
    "v124_oto_04",  # Cochlear Implant Candidacy
    "v124_oto_05",  # Facial Paralysis
    "v124_oto_06",  # Vestibular Migraine
}


VIGNETTES_V169 = [
    # Tympanometry / Acoustic Reflexes
    _q(
        "v169_oto_tymp_app", "Tympanometry / Acoustic Reflexes", "application",
        "A patient has a 25-dB conductive hearing loss, a type As tympanogram, and absent ipsilateral and contralateral acoustic reflexes when the affected ear is stimulated. Otoscopy is normal. Which diagnosis best integrates these findings?",
        ["Ossicular discontinuity", "Superior canal dehiscence", "Stapes fixation from otosclerosis", "Auditory neuropathy"], 2,
        "Reduced middle-ear compliance with a conductive gap and absent reflexes is a classic physiologic pattern for stapes fixation. Tympanometry and reflexes should be used to localize the mechanism rather than interpreted as isolated test labels.",
        [
            "Ossicular discontinuity more often produces a hypercompliant type Ad pattern rather than a stiff type As tracing.",
            "A third-window lesion can create a pseudoconductive gap, but middle-ear mechanics are typically normal and acoustic reflexes may remain present.",
            "Correct. Stapes fixation reduces compliance and prevents the impedance change required for a measurable acoustic reflex.",
            "Auditory neuropathy is a neural synchrony disorder and does not explain a conductive air-bone gap with stiff middle-ear mechanics."
        ],
        "Use tympanometry and reflexes to ask whether the conductive-looking loss is truly a middle-ear mechanics problem.",
        "If the reflexes were present despite the same air-bone gap and tympanogram were normal, what inner-ear 'third-window' diagnoses would move up your list?",
        "boards",
    ),
    _q(
        "v169_oto_tymp_snr", "Tympanometry / Acoustic Reflexes", "senior_decision",
        "A patient is referred for stapes surgery because of an apparent conductive loss. Repeat testing shows normal tympanometry, present acoustic reflexes, low-frequency air-bone gaps, autophony, and pressure-induced vertigo. What is the best next decision?",
        ["Proceed with stapedotomy because any air-bone gap implies stapes fixation", "Repeat hearing aids only and ignore the vestibular symptoms", "Order temporal-bone CT/VEMP evaluation for a third-window lesion before middle-ear surgery", "Explore the middle ear and decide after inspecting the ossicles"], 2,
        "Normal middle-ear mechanics and preserved reflexes argue against ordinary stapes fixation. Autophony and pressure/sound-induced vestibular symptoms make a third-window disorder such as superior canal dehiscence a critical alternative before irreversible middle-ear surgery.",
        [
            "An air-bone gap can be pseudoconductive; operating on the stapes without reconciling discordant physiology risks treating the wrong mechanism.",
            "Amplification may address hearing but does not explain or evaluate the pressure-induced vestibular syndrome.",
            "Correct. Senior interpretation means stopping a planned operation when the physiologic pattern points outside the middle ear.",
            "Exploration is not a diagnostic substitute for noninvasive physiologic and imaging evidence when a third-window lesion is suspected."
        ],
        "Before stapes surgery, make sure the audiogram, tympanogram, reflexes, symptoms, and imaging all tell the same mechanical story.",
        "What CT plane and VEMP pattern would strengthen a diagnosis of superior canal dehiscence, and what imaging pitfall can overcall dehiscence?",
        "OR_prep",
    ),

    # Temporal Bone Fracture
    _q(
        "v169_oto_tbf_app", "Temporal Bone Fracture", "application",
        "After a temporal-bone fracture, a patient has delayed-onset complete facial paralysis that developed over 48 hours. CT shows no obvious nerve transection. What is the best initial management approach?",
        ["Immediate facial-nerve transection and grafting", "High-dose corticosteroid therapy with close facial-function follow-up", "No treatment because delayed paralysis is always permanent", "Routine cochlear implantation"], 1,
        "Delayed facial paralysis after temporal-bone trauma is more consistent with edema/inflammation than immediate transection and generally has a substantially better prognosis. Steroids and serial facial assessment are appropriate when there is no evidence requiring decompression or repair.",
        [
            "Surgical transection would create a permanent injury and is not a treatment for delayed traumatic neuropraxia.",
            "Correct. Delayed onset usually supports an intact but edematous nerve and favors medical management initially.",
            "Delayed paralysis often recovers well; assuming irreversibility would lead to unnecessary intervention.",
            "Cochlear implantation treats severe hearing loss and has no role in isolated traumatic facial paresis."
        ],
        "In temporal-bone trauma, timing of facial paralysis is a major prognostic and management discriminator.",
        "What findings on electroneurography or EMG would make you reconsider observation?",
        "boards",
    ),
    _q(
        "v169_oto_tbf_snr", "Temporal Bone Fracture", "senior_decision",
        "A patient with an otic-capsule-violating fracture has immediate complete facial paralysis. Serial electroneurography shows greater than 90% degeneration within the accepted testing window, and high-resolution CT localizes injury near the geniculate/labyrinthine segment. What is the most appropriate senior-level decision?",
        ["Continue observation indefinitely because all traumatic palsies recover", "Decompress the facial nerve only if hearing is normal", "Discuss timely facial-nerve exploration/decompression using an approach tailored to hearing status and injury location", "Perform routine parotidectomy"], 2,
        "Immediate complete paralysis plus severe electrodiagnostic degeneration suggests major neural injury and is the classic setting in which exploration/decompression may be considered. The operative corridor depends on lesion location and whether useful hearing remains.",
        [
            "The combination of immediate complete paralysis and severe degeneration is precisely what makes indefinite observation inappropriate.",
            "Hearing status influences the surgical approach, not whether a severe traumatic nerve injury deserves consideration for intervention.",
            "Correct. The chief-level decision integrates onset, electrodiagnostics, fracture anatomy, hearing, and timing rather than using CT alone.",
            "Parotidectomy does not address an intratemporal facial-nerve injury."
        ],
        "Traumatic facial-nerve management is not 'fracture equals surgery'; it is onset + severity + degeneration + localization + hearing status.",
        "How would a serviceable-hearing patient change your choice among middle-fossa, transmastoid, and translabyrinthine corridors?",
        "OR_prep",
    ),

    # Cochlear Implant Candidacy
    _q(
        "v169_oto_ci_app", "Cochlear Implant Candidacy", "application",
        "A 63-year-old has bilateral severe sensorineural hearing loss and poor aided sentence recognition despite optimized hearing aids. MRI is normal and cognition is adequate. What additional information is most important before finalizing cochlear-implant candidacy and ear selection?",
        ["Only unaided pure-tone thresholds", "Aided speech testing, duration/asymmetry of deafness, imaging, and patient communication goals", "Whether the patient has tinnitus", "Whether the tympanic membrane is perfectly translucent"], 1,
        "Modern cochlear-implant decisions are driven by aided functional speech performance plus ear-specific history, anatomy, rehabilitation potential, and goals. Pure-tone thresholds alone do not capture useful hearing or predict which ear offers the best strategy.",
        [
            "Unaided thresholds help characterize hearing but are insufficient without aided speech performance and ear-specific context.",
            "Correct. Candidacy and ear choice are functional and individualized, not threshold-only decisions.",
            "Tinnitus can improve after implantation but is not the central determinant of candidacy or ear selection.",
            "A normal-appearing tympanic membrane does not establish cochlear reserve or aided speech benefit."
        ],
        "Refer for CI evaluation when optimized hearing aids no longer provide adequate speech understanding; do not wait for total deafness.",
        "How would asymmetric hearing, residual low-frequency hearing, and hearing-aid benefit influence single-sided versus bilateral strategy?",
        "boards",
    ),
    _q(
        "v169_oto_ci_snr", "Cochlear Implant Candidacy", "senior_decision",
        "A child with post-meningitic profound hearing loss is being evaluated for cochlear implantation. CT/MRI suggests early cochlear ossification. What should change in the plan?",
        ["Delay implantation for several years to see if the cochlea reopens", "Implantation is contraindicated once any ossification appears", "Expedite implant planning because progressive ossification can make electrode insertion more difficult, with counseling about modified surgical technique or incomplete insertion", "Perform stapedotomy first"], 2,
        "Post-meningitic labyrinthitis ossificans can progress and compromise scala patency. This is a timing-sensitive candidacy problem: prompt implantation evaluation and operative planning may preserve access before ossification becomes more extensive.",
        [
            "Delay risks losing cochlear patency and making later insertion more difficult or incomplete.",
            "Ossification complicates implantation but does not automatically preclude it; surgical technique and expected insertion may need modification.",
            "Correct. The senior decision is to recognize urgency and plan for altered anatomy rather than treating candidacy as routine.",
            "Stapes surgery treats conductive mechanics and does not address post-meningitic profound SNHL."
        ],
        "Meningitis is one of the settings where CI timing can be anatomically urgent because the cochlea may ossify.",
        "What imaging features and intraoperative findings would change your electrode strategy, and when might bilateral implantation be favored?",
        "OR_prep",
    ),

    # Facial Paralysis
    _q(
        "v169_oto_fp_app", "Facial Paralysis", "application",
        "A patient with presumed Bell palsy returns 4 months later with progressive complete weakness, facial pain, and no recovery. Which next step is most appropriate?",
        ["Repeat oral steroids indefinitely", "Reassure because Bell palsy commonly worsens for months", "Obtain targeted imaging along the facial-nerve course and evaluate for neoplasm or other secondary cause", "Perform vestibular rehabilitation only"], 2,
        "Progressive weakness, pain, recurrence, other cranial neuropathies, or failure to recover on the expected Bell-palsy trajectory are red flags for a secondary facial neuropathy. Imaging should cover the relevant intratemporal and extratemporal nerve course and be guided by examination.",
        [
            "Repeated steroids without reassessing the diagnosis can delay recognition of a structural lesion.",
            "Bell palsy typically reaches nadir quickly and then improves; progressive months-long decline is not reassuring.",
            "Correct. The clinical course has broken the Bell-palsy pattern and the diagnosis must be reopened.",
            "Vestibular rehabilitation does not evaluate a progressive facial neuropathy."
        ],
        "Bell palsy is a diagnosis with an expected tempo; when the tempo is wrong, reopen the differential.",
        "What imaging coverage would you choose if the exam suggests a high intratemporal lesion versus a parotid-region lesion?",
        "boards",
    ),
    _q(
        "v169_oto_fp_snr", "Facial Paralysis", "senior_decision",
        "During parotid malignancy resection, the main facial-nerve trunk is grossly encased by tumor and preoperative function was already poor. A negative margin cannot be achieved while preserving the involved segment. What is the best oncologic and reconstructive principle?",
        ["Preserve the nerve regardless of margin because facial function always outranks cancer control", "Sacrifice the involved segment when required for oncologic clearance and plan immediate nerve reconstruction/reanimation when feasible", "Abort the cancer operation and observe", "Remove only the overlying parotid tissue and leave gross tumor on the nerve"], 1,
        "When a facial-nerve segment is directly invaded and preservation would leave gross disease, oncologic clearance takes priority. When feasible, immediate cable grafting, nerve transfer, or other reanimation planning should be integrated into the same operation rather than deferred as an afterthought.",
        [
            "Preserving a grossly invaded nerve at the cost of an inadequate cancer resection is not an acceptable universal rule.",
            "Correct. Senior surgery balances margin control with planned functional reconstruction.",
            "Observation does not address a resectable malignancy with known nerve invasion.",
            "Leaving gross tumor behind on the nerve sacrifices oncologic control without preserving meaningful function."
        ],
        "Facial-nerve preservation is the goal when oncologically safe; direct tumor invasion changes the priority and should trigger immediate reanimation planning.",
        "How does the expected gap length and availability of proximal/distal nerve ends influence cable grafting versus masseteric or hypoglossal transfer?",
        "OR_prep",
    ),

    # Vestibular Migraine
    _q(
        "v169_oto_vm_app", "Vestibular Migraine", "application",
        "A patient has recurrent 3-hour vertigo episodes with photophobia and migraine headache but no fluctuating hearing loss. Neurologic examination is normal between attacks. What is the best management framework?",
        ["Treat every episode as Meniere disease with ablative therapy", "Use migraine trigger/lifestyle management and appropriate acute/preventive migraine therapy while excluding competing vestibular diagnoses", "Perform vestibular-nerve section", "Prescribe chronic vestibular suppressants as the only therapy"], 1,
        "Vestibular migraine is managed as a migraine-spectrum disorder after the episodic pattern and competing vestibular diagnoses are assessed. Lifestyle/trigger control, acute therapy, and preventive medication are individualized; chronic vestibular suppressants can impede compensation and do not address the underlying migraine biology.",
        [
            "Ablative Meniere treatment is inappropriate without the characteristic fluctuating cochlear syndrome and would create irreversible vestibular injury.",
            "Correct. Management follows migraine principles while preserving diagnostic discipline about other vestibular disorders.",
            "Vestibular-nerve section is destructive treatment for selected refractory peripheral vestibular disease, not routine vestibular migraine.",
            "Vestibular suppressants may help selected acute attacks but are not an adequate chronic disease strategy."
        ],
        "Vestibular migraine is diagnosed by syndrome and time course, not by one vestibular test.",
        "What features would make you obtain MRI or pursue a central-neurologic workup despite an otherwise migrainous history?",
        "boards",
    ),
    _q(
        "v169_oto_vm_snr", "Vestibular Migraine", "senior_decision",
        "A patient labeled with vestibular migraine now has a new continuous acute vestibular syndrome, severe gait ataxia, direction-changing gaze-evoked nystagmus, and a normal head impulse. What should happen next?",
        ["Increase migraine prophylaxis and discharge", "Perform an Epley maneuver", "Treat this as possible posterior-circulation stroke and obtain urgent stroke-level evaluation rather than anchoring on the prior migraine diagnosis", "Start diuretics for Meniere disease"], 2,
        "A prior vestibular-migraine diagnosis does not protect a patient from stroke. A new acute vestibular syndrome with central bedside signs requires urgent evaluation for posterior-circulation ischemia; diagnostic anchoring is the danger being tested.",
        [
            "New central signs and severe gait dysfunction are not safely explained by simply escalating migraine therapy.",
            "Epley treats brief positional BPPV and does not address a continuous syndrome with central oculomotor findings.",
            "Correct. Chief-level reasoning means recognizing when the current syndrome is different from the patient's prior benign pattern.",
            "Meniere disease requires an episodic cochleovestibular syndrome and does not explain these central findings."
        ],
        "Do not let an established benign vestibular diagnosis override a new syndrome with central red flags.",
        "Which HINTS-family findings are most concerning for a central lesion, and when is HINTS inappropriate to apply?",
        "overnight_call",
    ),
]


def apply_learning_ladders_v169(challenges, item_id_fn):
    """Tag reviewed foundations and merge the missing Otology ladder layers."""
    by_id = {q.get("id"): q for q in challenges}
    tagged = []
    for qid in REVIEWED_FOUNDATION_IDS_V169:
        q = by_id.get(qid)
        if not q:
            raise RuntimeError(f"v16.9 expected reviewed foundation missing: {qid}")
        q["learning_stage"] = "foundation"
        q["review_status"] = "deliberately_reviewed_v169"
        tagged.append(qid)

    canonical = {
        (q.get("domain"), q.get("topic"))
        for q in challenges
        if q.get("domain") and q.get("topic")
    }
    existing = set(by_id)
    added = []
    for source in VIGNETTES_V169:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["concept_id"] = item_id_fn(q["domain"], q["topic"])
        q["review_status"] = "deliberately_reviewed_v169"
        challenges.append(q)
        existing.add(q["id"])
        added.append(q["id"])
    return {"tagged_foundations": tagged, "added": added}
