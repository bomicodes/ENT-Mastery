"""v20.20 — deepen the exact-live Le Fort / Panfacial Trauma Concept Check on validated v20.19 production."""
from concept_check_board_repair_v177 import _find_module

QIDS = ("cc-v112-rec-facial-plastics-trauma-le-fort-panfacial-trauma",)
CID = "v6-facial-plastics-trauma-le-fort-panfacial-trauma"
TOPIC = "Le Fort / Panfacial Trauma"

SOURCE_REFS_V220 = [
    {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive corpus, full compressed copy Drive id 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t; Craniomaxillofacial Trauma chapter and facial-plastic trauma anatomy cross-referenced 2026-09-08.","role":"durable foundation: facial buttresses, occlusion, midface/skull-base relationships, orbital/NOE danger zones, exposure and fixation principles"},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive copy Drive id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52; reconstructive/facial-plastic trauma framework cross-referenced 2026-09-08.","role":"resident/board framework: initial trauma assessment, fracture patterns, occlusion, orbital and midface management"},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected Google Drive copy Drive id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR; facial trauma, maxillofacial anatomy and airway principles cross-referenced 2026-09-08.","role":"operative cross-check: Le Fort patterns, craniofacial relationships, airway/bleeding hazards and fixation goals"},
    {"type":"society_reference","citation":"AO Surgery Reference CMF, Midface second edition, published Aug 14 2025; Panfacial fractures—sequencing of repair and midfacial patient examination modules.","role":"current expert operative reference: airway/circulation first, visual/neurologic/cervical-spine assessment, restoration of occlusion and facial width/height/projection, unit-based sequencing and postoperative occlusion checks"},
    {"type":"current_review","citation":"Menard C, Pierce S, deTar TR. Difficult airway management in trauma: a review of current guidelines. Emerg Med Pract. 2025;27(Suppl 3):1-40. PMID: 40498582.","role":"current trauma airway algorithms including maxillofacial trauma and emergency front-of-neck rescue"},
    {"type":"current_evidence","citation":"Kuhrau C, et al. Safety of Intubation Methods in Patients With LeFort Pattern Facial Trauma. J Craniofac Surg. 2025. PMID: 40728925.","role":"evidence boundary: route of intubation is individualized; historical avoidance of nasotracheal intubation with skull-base injury is not a substitute for imaging, direct control and airway-team judgment"},
]

PROMPT = """A polytrauma patient arrives after a high-speed collision with mobile midface, malocclusion, bilateral periorbital edema, brisk naso-oropharyngeal bleeding and CT evidence of Le Fort-pattern fractures extending through NOE and zygomaticomaxillary buttresses. As the senior ENT resident, explain the immediate airway/hemorrhage/vision/skull-base priorities, how Le Fort patterns and panfacial anatomy guide but do not replace CT-based injury mapping, how you establish preinjury occlusion and choose top-down versus bottom-up sequencing, and how you restore facial width, height and projection. Include explicit danger zones, airway-route disagreements, orbital/optic and CSF-leak emergencies, and concrete rescue/bailout decisions when bleeding, swelling, unstable occlusion or fragmented reference points make the planned reconstruction unsafe."""

ANSWER = """Foundation — panfacial trauma is not an exercise in naming Le Fort I, II or III. The classification is useful shorthand for recurring fracture patterns, but modern injuries are frequently asymmetric, comminuted and mixed with mandibular, palatal, NOE, ZMC, orbital, frontal-sinus and skull-base fractures. The senior resident must build a three-dimensional injury map from examination and thin-cut CT, then restore function and facial form around reliable reference points. The goals are a secure airway, hemostasis, preservation of vision and brain/cervical-spine safety, followed by restoration of preinjury occlusion, facial width, height and projection with stable fixation.

Immediate priorities — follow trauma resuscitation before facial reconstruction. A mobile bleeding midface, posterior tongue displacement, loose teeth, dentures, blood and secretions can rapidly obstruct the airway. Suction aggressively, provide oxygenation/ventilation and secure the airway before swelling and repeated attempts make it harder. Anticipate cervical-spine precautions and a difficult airway. If oral intubation blocks the occlusal work and a nasal route is unsafe or impractical, options can include controlled tube exchange, submental routing in selected cases, or tracheostomy when a durable unobstructed airway is required. If oxygenation or intubation fails, move through the established difficult-airway rescue pathway to emergency front-of-neck access rather than persisting with traumatic attempts.

Airway-route nuance — residents are often taught that nasotracheal intubation is absolutely forbidden in every Le Fort II/III or skull-base fracture because of feared intracranial passage. That historical hazard still matters, especially with disrupted central skull base/NOE anatomy, active CSF leak, severe nasal comminution or when the route is blind. However, contemporary literature does not support treating the label 'Le Fort' alone as an absolute route prohibition. The decision should use CT-defined skull-base anatomy, need for maxillomandibular fixation, airway expertise, visualization and alternatives. Never pass a nasal tube blindly through an incompletely characterized central skull-base injury merely to simplify fixation.

Hemorrhage — brisk midface bleeding can be diffuse or arise from branches of the internal maxillary, sphenopalatine, facial or other systems. Begin with suction, direct pressure and packing where appropriate while resuscitating. Correct coagulopathy and activate trauma/massive-transfusion pathways when indicated. If bleeding remains uncontrolled, escalate early to operative exposure, vessel control or interventional embolization depending on anatomy and physiology. Do not blindly clamp deep posterior nasal or pterygopalatine tissue where the maxillary artery and cranial-nerve/skull-base structures are not defined. Persistent shock outranks definitive fracture fixation.

Vision and orbit — document visual acuity, pupils, color vision when feasible, extraocular movements, globe position and afferent pupillary function early because edema soon obscures examination. Suspected globe rupture is protected and managed urgently with ophthalmology. A tense orbit with rapidly decreasing vision, proptosis and an afferent pupillary defect is a time-critical orbital compartment syndrome; do not wait for a perfect CT or for definitive fracture repair before decompression when the diagnosis is clinically compelling. Entrapment, especially with oculocardiac symptoms in a trapdoor pattern, is a different urgent problem. Blindly reducing an orbital fracture without knowing globe/optic status can convert an occult injury into irreversible visual loss.

Skull base and CSF — look for CSF rhinorrhea/otorrhea, pneumocephalus, cranial neuropathy and fractures traversing the cribriform, ethmoid roof, frontal sinus posterior table or sphenoid. Clear fluid alone is not a reason to instrument the nose. Avoid blind nasal instrumentation when skull-base integrity is uncertain. Coordinate persistent or complex CSF leaks with skull-base/neurosurgical expertise. Fever or meningitis is not a therapeutic mechanism for dural healing; the goal is recognition, protection from ascending contamination and definitive management when indicated.

Le Fort anatomy — Le Fort I separates the tooth-bearing maxilla/palate from the upper midface; Le Fort II is pyramidal and crosses the nasal bridge/medial orbit toward the infraorbital rim and pterygoid region; Le Fort III represents craniofacial dysjunction through nasofrontal, orbital and zygomatic arch-related interfaces. Real trauma rarely respects textbook lines. Confirm pterygoid plate, palatal, zygomaticomaxillary, nasomaxillary, frontozygomatic, NOE and orbital components on CT rather than inferring the whole injury from one fracture line.

Occlusion is the functional reference — establish the patient's preinjury bite from wear facets, dental records/photos when available, intact teeth and fracture geometry. Remove grossly unstable nonrestorable obstacles as clinically necessary but preserve useful dentition and bone. Palatal widening and mandibular fractures can create a false occlusal platform; stabilizing the mandible against a widened maxilla simply locks deformity into the reconstruction. Reduce palatal and mandibular components enough to create a trustworthy lower facial unit before relying on maxillomandibular fixation as a template.

Buttresses and three-dimensional reconstruction — the vertical nasomaxillary, zygomaticomaxillary and pterygomaxillary regions and horizontal frontal, infraorbital/zygomatic and maxillary/alveolar supports transmit facial loads and define projection. Panfacial reduction must recreate facial width at the zygomas, vertical height between cranial and dental units, and anterior projection. One accurately restored reference can guide the next; one malreduced reference propagates error throughout the face.

Sequencing — there is no single mandatory 'top-down' or 'bottom-up' sequence. Bottom-up commonly begins by establishing the mandible as a stable arch, restoring occlusion/palate, then linking the midface upward. Top-down begins from stable frontal/cranial reference points, reconstructs upper facial width/NOE/ZMC relationships, then connects the lower midface and occlusion. AO's current panfacial framework explicitly allows either direction: create stable upper and lower facial units and ultimately link them at the Le Fort I level. Choose the direction that starts from the patient's least disrupted, most reproducible reference. If the frontal bar is comminuted but the mandible is intact, bottom-up may be logical; if the mandible/palate is destroyed but the cranial frame is reliable, top-down may be safer.

NOE and medial canthus — identify medial canthal tendon integrity and central-fragment stability. Failure to restore intercanthal distance and nasal projection produces traumatic telecanthus and a flattened central face that is difficult to correct later. Preserve lacrimal anatomy when possible and coordinate injuries requiring specialized repair. Do not accept apparent nasal alignment before the NOE framework is actually stable.

ZMC and orbital framework — restore the zygomatic width/projection and verify alignment across reliable interfaces, not one visible rim alone. Orbital volume depends on accurate reconstruction of the zygoma, floor and medial/lateral walls. Over-widening or posterior malposition changes globe projection. Before closing, reassess globe position, pupils, forced ductions when indicated, and make sure hardware or reconstructed walls are not impinging the orbit.

Fixation strategy — expose enough stable bone to identify the fracture and confirm reduction without creating unnecessary soft-tissue injury. Fixation strength depends on fracture pattern, comminution, bone quality and load. Plates are tools for holding an anatomically reconstructed skeleton, not a substitute for reduction. Recheck occlusion repeatedly as major units are linked. If the bite changes after fixation, stop and identify which reference was wrong rather than tightening additional plates around a malreduction.

Senior bailout — when every landmark is mobile, do not 'pick a corner' and keep plating. Re-establish a reliable reference: dentition/mandible, frontal bar, one correctly reduced zygoma, or a reconstructed palate depending on the injury. If swelling prevents meaningful globe assessment, bleeding remains uncontrolled, physiology is unstable, contaminated soft tissue needs serial debridement, or definitive landmarks cannot yet be trusted, staged treatment can be safer than forcing one marathon reconstruction. Temporary stabilization and delayed definitive fixation are acceptable when the alternative is locking in malocclusion, blindness risk or an unstable patient.

Complication rescue — postoperative or intraoperative new vision loss, afferent pupillary defect or tense proptosis is an emergency; release compressive dressings/packing and pursue immediate orbital-compartment rescue rather than waiting for routine imaging. New severe malocclusion after fixation means reduction must be reassessed before healing consolidates the error. Persistent major epistaxis after reconstruction requires controlled hemostatic evaluation, not repeated blind posterior instrumentation. Hardware exposure/infection, malunion, enophthalmos, diplopia, telecanthus, nasal obstruction and CSF leak should be traced back to the failed structural or soft-tissue problem rather than treated as cosmetic afterthoughts.

Senior synthesis — before definitive fixation, be able to answer: Is the airway secure for the entire operation and postoperative swelling? Is hemorrhage controlled? Has vision been documented and every orbital emergency excluded or treated? Is skull-base injury mapped? What is the most reliable starting reference? Is the occlusal platform truly preinjury rather than a widened or rotated construct? Which sequence best restores width, height and projection in this patient? The dangerous resident error is mistaking a memorized Le Fort label or sequencing slogan for a reconstruction plan. The expert plan is individualized, repeatedly checked against occlusion and stable anatomy, and willing to stop or stage when physiology, bleeding, vision or unreliable reference points make definitive fixation unsafe."""

TRAPS = [
    "Naming a Le Fort pattern from one CT line and failing to map asymmetric NOE, ZMC, orbital, palatal, mandibular and skull-base components.",
    "Prioritizing fracture classification or fixation before securing an airway obstructed by blood, secretions, teeth or a mobile midface.",
    "Repeating traumatic intubation attempts instead of escalating through a difficult-airway algorithm and front-of-neck rescue when oxygenation fails.",
    "Treating nasotracheal intubation as automatically safe or automatically forbidden from the words 'Le Fort' alone rather than evaluating skull-base anatomy, visualization and alternatives.",
    "Blindly passing a nasal tube through an incompletely characterized central skull-base or NOE injury.",
    "Chasing deep posterior midface hemorrhage with blind clamps rather than pressure/packing, resuscitation and controlled operative or endovascular hemostasis.",
    "Failing to document vision before edema or anesthesia removes the baseline examination.",
    "Waiting for definitive fracture repair or perfect imaging while a clinically obvious orbital compartment syndrome destroys vision.",
    "Using maxillomandibular fixation to lock a widened palate or malreduced mandibular arch into a false occlusion.",
    "Believing top-down or bottom-up is a dogma instead of starting from the most reliable intact reference in that patient's fracture pattern.",
    "Fixing one easily visible buttress perfectly while facial width, height or projection remains wrong globally.",
    "Ignoring medial canthal tendon/NOE stability and creating persistent traumatic telecanthus despite an apparently straight nasal bridge.",
    "Reconstructing the orbital floor before the zygomatic framework is correctly reduced and thereby building orbital volume on the wrong skeleton.",
    "Continuing to add plates after occlusion changes instead of stopping to identify the upstream malreduction.",
    "Forcing definitive panfacial ORIF in an unstable, actively bleeding, massively swollen patient when staged stabilization is safer.",
]

COHORT = {QIDS[0]: {
    "concept_id": CID,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "answer_text": ANSWER,
    "explanation": "Panfacial trauma is rebuilt from physiology and reliable references: secure airway/hemostasis/vision first, map the actual CT injury, establish true occlusion, then restore facial width, height and projection with a sequence chosen from stable anatomy rather than a memorized slogan.",
    "board_pearl": "In panfacial trauma, do not plate chaos: first create one trustworthy reference and a real occlusal platform; if vision, hemorrhage, airway or landmarks are uncontrolled, stop and stage rather than lock in catastrophe.",
    "depth_layers_v220": {
        "foundation":"Trauma priorities, Le Fort pattern anatomy, buttresses, orbit/NOE/skull base and occlusion as the functional reference.",
        "application":"Airway-route selection, hemorrhage control, CT injury mapping, palate/mandible stabilization, top-down versus bottom-up sequencing and three-dimensional fixation.",
        "senior_decision":"Rescue vision/airway/bleeding before fixation; select the most reliable starting reference; stop or stage when physiology or fragmented landmarks make definitive reconstruction unsafe."
    },
    "common_traps_v220": TRAPS,
    "deliberate_review_v220": "Selected from the exact successful v20.19 production backlog. It ranked fifth lexically, but its prior 14-word answer left major resident/board/OR hazards unaddressed: difficult airway, hemorrhage, blindness, skull-base injury, false occlusal references and sequencing failure.",
    "source_refs_v220": SOURCE_REFS_V220,
    "evidence_distinction_v220": "Durable Cummings/Pasha/K.J. Lee anatomy, buttress, occlusion and fixation principles are preserved. AO Surgery Reference's Aug 14 2025 midface revision updates current expert sequencing and assessment. Contemporary airway literature is used to avoid two false absolutes: blind nasal instrumentation across an uncertain skull base remains hazardous, but a Le Fort label alone does not prove every controlled nasotracheal approach is contraindicated. Emergency airway and orbital-compartment rescue remain time-critical safety priorities.",
    "audit_profile_v220": "le_fort_panfacial_trauma",
}}

def apply_concept_check_task_alignment_v220(checks, deep_modules, v6_item_id):
    by = {str(q.get("id") or ""): q for q in checks or []}
    repaired, missing, link_mismatch = [], [], []
    for qid, payload in COHORT.items():
        q = by.get(qid)
        if q is None:
            missing.append(qid); continue
        module = _find_module(q, deep_modules, v6_item_id)
        topic = str(module.get("topic") or "") if module else ""
        cid = v6_item_id(q.get("domain"), topic) if module and q.get("domain") else None
        if topic != payload["canonical_topic"] or cid != payload["concept_id"]:
            link_mismatch.append(qid); continue
        for key, value in payload.items():
            if key != "canonical_topic": q[key] = value
        q["topic"] = payload["canonical_topic"]
        q["concept_id"] = payload["concept_id"]
        q["choices"] = []
        q["answer"] = None
        q["task_alignment_v220"] = True
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}
