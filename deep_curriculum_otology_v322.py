"""v32.2 — source-grounded Temporal Bone Anatomy vs Temporal Bone Fracture rebuild.

The anatomy card owns the three-dimensional surgical map. The fracture card owns acute
trauma triage, complication-directed evaluation, modern otic-capsule classification, and
selective intervention. Keeping those jobs separate prevents an anatomy recall card from
becoming a shallow trauma card and prevents fracture management from degenerating into a
list of landmarks.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


TEMPORAL_BONE_REBUILD_V322 = {
    "temporal bone anatomy": {
        "recognize": (
            "Use this card to build the OPERATIVE/SPATIAL MAP of the temporal bone, not to manage trauma. Orient the squamous, mastoid, tympanic, petrous and styloid components around the external canal, middle ear, mastoid and otic capsule. The clinically useful map relates surface and air-cell landmarks to the tegmen superiorly, sigmoid sinus posteriorly, middle cranial fossa superior-medially, posterior fossa posterior-medially, temporomandibular joint anteriorly, jugular bulb inferiorly and petrous carotid anterior-medially."
        ),
        "localize": (
            "Localize structures in a reproducible lateral-to-medial sequence. From the mastoid cortex identify the temporal line/tegmen, spine of Henle and canal, then mastoid antrum and lateral semicircular canal. The FACIAL NERVE travels IAC -> labyrinthine segment -> geniculate ganglion -> tympanic (horizontal) segment above the oval window -> second genu -> mastoid (vertical) segment -> stylomastoid foramen. The chorda tympani branches from the mastoid segment and crosses the middle ear. The facial recess is bounded by facial nerve posteriorly, chorda tympani anteriorly and fossa incudis superiorly; the sigmoid sinus, tegmen and labyrinth define other critical mastoidectomy danger boundaries."
        ),
        "workup": (
            "Translate anatomy onto high-resolution temporal-bone CT rather than memorizing isolated names. On axial and coronal images identify the ossicular chain; cochlea, vestibule and semicircular canals; IAC; facial canal; carotid canal; jugular bulb; tegmen; sigmoid sinus; mastoid antrum/aditus; Eustachian tube and external canal. Then ask what surgical corridor a lesion occupies and what structure limits safe exposure. This card should answer 'where is it and what is next to it?'—not 'what do I do after a skull-base injury?'"
        ),
        "manage": (
            "Apply the map to clinical localization. Conductive loss can arise in the canal, tympanic membrane, ossicles or middle-ear space; sensorineural loss localizes more medially to cochlea/CN VIII pathways. Facial weakness can be localized along the intratemporal course by associated findings and imaging. Superior tegmen defects connect ear/mastoid to middle fossa; posterior defects approach sigmoid/posterior fossa; inferior disease approaches jugular bulb; anterior disease approaches TMJ/petrous carotid/Eustachian tube. Management belongs to the disease-specific card once the anatomic compartment is identified."
        ),
        "operate": (
            "Boards-to-OR landmarks: cortical mastoidectomy proceeds with the tegmen as the superior limit and sigmoid sinus as the posterior limit while the lateral semicircular canal and incus orient the antrum. Posterior tympanotomy enters through the facial recess while protecting the facial nerve and chorda tympani. Before drilling near the labyrinth, facial canal, carotid canal, jugular bulb or dura, know the expected three-dimensional relationship and recognize anatomic variation such as a high jugular bulb, anterior sigmoid sinus, low tegmen or aberrant facial nerve course. Anatomy is the safety system; the indication for surgery comes from the pathology card."
        ),
        "teach": (
            "Chief/boards framework: TEMPORAL BONE ANATOMY = CORRIDORS + BOUNDARIES + NEUROVASCULAR RELATIONSHIPS. Be able to trace CN VII from IAC to stylomastoid foramen, orient tegmen/sigmoid/labyrinth during mastoidectomy, define the facial recess, and read those relationships on CT. Do not contaminate this card with fracture treatment thresholds; the fracture card owns trauma decisions."
        ),
        "tags": ["temporal bone anatomy", "facial nerve", "facial recess", "mastoidectomy landmarks", "tegmen", "sigmoid sinus", "otic capsule", "temporal bone CT"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — temporal bone, middle-ear, facial-nerve and lateral skull-base anatomy framework",
            "K.J. Lee's Essential Otolaryngology, 12e — temporal bone/facial nerve anatomy and operative orientation",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — external ear, temporal bone, middle-ear and facial-nerve anatomy",
        ],
    },
    "temporal bone fracture": {
        "recognize": (
            "Use this card for ACUTE TEMPORAL-BONE TRAUMA after life-threatening head/cervical injuries have been stabilized. Look for hemotympanum or bloody otorrhea, tympanic-membrane/EAC injury, hearing loss, vertigo, facial weakness and CSF otorrhea/rhinorrhea. Document facial function EARLY with House-Brackmann grade and, whenever possible, whether weakness was immediate versus delayed and complete versus incomplete; that chronology materially changes prognosis and the facial-nerve workup."
        ),
        "localize": (
            "Classify modern fractures primarily as OTIC-CAPSULE SPARING versus OTIC-CAPSULE VIOLATING/DISRUPTING because this better predicts major neurotologic sequelae than the older longitudinal/transverse labels. Otic-capsule violation raises concern for severe SNHL/vestibular injury, CSF leak and facial-nerve injury. Separately localize complications: EAC/TM/ossicular injury -> conductive loss; cochlea/labyrinth -> SNHL/vertigo; fallopian canal -> facial palsy; tegmen/posterior-fossa plate -> CSF fistula; carotid canal involvement -> vascular injury concern. A fracture line is an anatomic description, not by itself an indication for surgery."
        ),
        "workup": (
            "After trauma stabilization, perform careful otoscopy without aggressive canal manipulation, bedside tuning forks when feasible, serial facial-nerve examination and formal audiometry once the patient can participate. Standard trauma CT may identify the injury; obtain thin-cut high-resolution temporal-bone CT when facial paralysis, suspected CSF fistula, significant hearing/vestibular injury or operative planning requires detailed anatomy. Add vascular imaging when the fracture trajectory or associated findings raise concern for carotid injury. If clear otorrhea is uncertain, beta-2 transferrin can confirm CSF. For complete traumatic facial paralysis, electrophysiologic testing is timed after Wallerian degeneration has evolved rather than performed reflexively on day 0; contemporary society guidance uses serial electrodiagnostics around the 10-14 day window in appropriate patients."
        ),
        "manage": (
            "Treat the COMPLICATION, not the fracture line. Most uncomplicated traumatic CSF leaks are initially managed conservatively with observation and measures that reduce intracranial-pressure strain; persistent/recurrent leakage, meningitis or a repairable high-risk defect warrants skull-base repair planning. Hemotympanum usually resolves; persistent conductive loss after the acute period suggests ossicular disruption and merits repeat audiometry/imaging. Persistent vestibular symptoms receive diagnosis-specific treatment and rehabilitation; suspected perilymphatic fistula is a separate surgical decision. Severe/profound SNHL requires hearing-rehabilitation counseling. Avoid teaching routine prophylactic antibiotics for every temporal-bone fracture as a universal rule; infection strategy depends on the specific wound/CSF scenario and local evidence-based practice."
        ),
        "operate": (
            "FACIAL NERVE is the key selective-operative branch. Delayed or incomplete traumatic weakness generally has a favorable spontaneous prognosis and is not an automatic decompression indication. Immediate complete paralysis warrants neurotology evaluation, high-resolution imaging and appropriately timed electrodiagnostics. Marked degeneration (often taught as >90% on ENoG in a complete palsy) may support decompression in a carefully selected patient when imaging/clinical localization is concordant, but the evidence is LOW QUALITY and the threshold is not an automatic operation. Suspected transection or penetrating injury changes the problem toward exploration/repair. Choose transmastoid, middle-fossa or combined exposure according to the suspected injured segment and hearing status. Persistent CSF fistula and delayed ossicular disruption are separate complication-directed operations."
        ),
        "teach": (
            "Chief/boards sequence: STABILIZE -> DOCUMENT FACE/HEARING/VESTIBULAR/CSF -> CLASSIFY OTIC CAPSULE -> IMAGE THE COMPLICATION -> TREAT THE COMPLICATION. Modern discriminator: otic-capsule sparing versus violating predicts clinically relevant morbidity better than simply longitudinal versus transverse. Immediate complete facial palsy triggers imaging + delayed/serial electrodiagnostics; delayed/incomplete palsy usually does not equal decompression. Do not overstate ENoG or decompression evidence: society recommendations are weak/low-quality, so integrate timing, completeness, CT localization and trajectory."
        ),
        "tags": ["temporal bone fracture", "otic capsule sparing", "otic capsule violating", "facial paralysis", "ENoG", "CSF otorrhea", "ossicular disruption", "traumatic hearing loss"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — temporal-bone trauma, facial-nerve injury, CSF leak and hearing-loss framework",
            "K.J. Lee's Essential Otolaryngology, 12e — temporal-bone fracture sequelae and modern classification context",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — trauma to the ear/temporal bone and facial-nerve evaluation",
            "Brazilian Society of Otology Task Force, 2024 — traumatic peripheral facial palsy imaging/electrodiagnostic/decompression recommendations and evidence grading",
        ],
    },
}


def apply_temporal_bone_rebuild_v322(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules:
            payload = TEMPORAL_BONE_REBUILD_V322.get(_norm(module.get("topic")))
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v322"] = True
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
