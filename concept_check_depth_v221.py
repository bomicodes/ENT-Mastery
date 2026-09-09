"""v20.21 — deepen exact-live Le Fort / Panfacial Trauma after validated v20.20 production."""
from concept_check_board_repair_v177 import _find_module

QIDS = ("cc-v112-rec-facial-plastics-trauma-le-fort-panfacial-trauma",)
CID = "v6-facial-plastics-trauma-le-fort-panfacial-trauma"
TOPIC = "Le Fort / Panfacial Trauma"

SOURCE_REFS_V221 = [
    {"type":"textbook","citation":"Cummings Otolaryngology: Head and Neck Surgery, 7th ed. (2021), connected Google Drive corpus, Drive id 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t; craniomaxillofacial trauma, orbital fracture, facial buttress, occlusion and skull-base principles cross-referenced 2026-09-09.","role":"durable foundation: facial buttresses, occlusion, midface/skull-base relationships, orbital/NOE danger zones and fixation principles"},
    {"type":"textbook","citation":"Pasha R, Golub JS. Otolaryngology-Head and Neck Surgery: Clinical Reference Guide, 6th ed. (2022), connected Google Drive copy Drive id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52; facial trauma and reconstructive framework cross-referenced 2026-09-09.","role":"resident/board framework: trauma assessment, fracture patterns, occlusion, orbit and midface management"},
    {"type":"textbook","citation":"K.J. Lee's Essential Otolaryngology: Head & Neck Surgery, 12th ed. (2019), connected Google Drive copy Drive id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR; Chapter 56 Craniomaxillofacial Trauma and Chapter 57 Orbital Fractures cross-referenced 2026-09-09.","role":"operative cross-check: Le Fort patterns, craniofacial relationships, airway/bleeding hazards and reconstruction goals"},
    {"type":"expert_reference","citation":"AO Surgery Reference CMF, Panfacial fractures (sequencing of repair), current page reviewed 2026-09-09.","role":"current expert operative reference: reliable-reference sequencing, restoration of three-dimensional facial frame, occlusion and buttress fixation"},
    {"type":"current_review","citation":"Menard C, Pierce S, deTar TR. Difficult airway management in trauma: a review of current guidelines. Emerg Med Pract. 2025;27(Suppl 3):1-40. PMID: 40498582.","role":"current difficult-airway and emergency front-of-neck rescue framework in trauma"},
    {"type":"current_evidence","citation":"Kuhrau C, Easton J, Woodyard De Brito K, Dembinski D, Gobble R. Safety of Intubation Methods in Patients With LeFort Pattern Facial Trauma. J Craniofac Surg. 2025. PMID: 40728925.","role":"evidence boundary: Le Fort label alone is not an evidence-based absolute prohibition on every controlled nasotracheal approach; route remains anatomy- and context-dependent"},
    {"type":"society_guidance","citation":"Difficult Airway Society 2025 tracheal intubation guidelines, published 2025; current update cross-checked 2026-09-09.","role":"current airway safety emphasis on first-attempt success, structured rescue and emergency front-of-neck access"},
]

PROMPT = """A polytrauma patient arrives after a high-speed collision with a mobile midface, malocclusion, bilateral periorbital edema, brisk naso-oropharyngeal bleeding and CT evidence of mixed Le Fort-pattern, NOE, ZMC, orbital and palatal fractures. As the senior ENT resident, explain the immediate airway, hemorrhage, vision, cervical-spine and skull-base priorities; how Le Fort patterns guide but do not replace CT injury mapping; how you establish true preinjury occlusion and choose top-down versus bottom-up sequencing; and how you restore facial width, height and projection. Include explicit danger zones, the modern airway-route disagreement, orbital/optic and CSF-leak emergencies, and concrete stop/stage or rescue decisions when bleeding, swelling, unstable physiology or fragmented reference points make definitive reconstruction unsafe."""

ANSWER = """Foundation — panfacial trauma is not primarily a classification exercise. Le Fort I, II and III describe recurring planes of midface separation, but high-energy injuries are commonly asymmetric and mixed with mandibular, palatal, NOE, zygomaticomaxillary complex, orbital, frontal-sinus and skull-base fractures. The senior resident uses the classification as a communication scaffold, then builds a patient-specific three-dimensional map from examination and thin-cut CT. The operative objectives are first survival and preservation of critical function, then restoration of true preinjury occlusion and the facial frame in width, height and projection.

Immediate priorities — trauma resuscitation outranks facial fixation. A mobile midface, blood, secretions, loose teeth, dentures, posterior tongue displacement and progressive edema can produce a rapidly worsening difficult airway. Suction aggressively, oxygenate, protect the cervical spine as indicated and formulate the airway before repeated attempts create more bleeding and swelling. The airway plan must account for the need to manipulate occlusion during repair. Orotracheal intubation may obstruct maxillomandibular fixation; a nasal route may be inappropriate in selected central skull-base/NOE injuries; submental routing or tracheostomy may be appropriate in selected operative courses. If intubation or oxygenation fails, transition through a structured rescue algorithm and emergency front-of-neck access rather than persisting with traumatic attempts.

Airway-route disagreement — older teaching often converts 'Le Fort II/III' or 'skull-base fracture' into an absolute prohibition on all nasotracheal intubation. The feared intracranial passage from blind instrumentation is real enough that an uncertain/disrupted central skull base, severe NOE/nasal comminution, active CSF leak or a blind route should make the resident stop. But contemporary evidence does not justify treating the Le Fort label alone as an absolute contraindication to every controlled, visualized nasotracheal technique. The decision belongs to CT-defined anatomy, airway expertise, visualization, operative occlusal needs and available alternatives. Never instrument an incompletely characterized skull base blindly merely to simplify fixation.

Hemorrhage — brisk midface bleeding can be diffuse or arterial, including branches of the internal maxillary, sphenopalatine and facial systems. Start with suction, direct pressure and appropriate packing while resuscitating. Correct coagulopathy and activate massive-transfusion pathways when physiology demands it. Persistent major bleeding requires early escalation to controlled operative exposure/ligation or interventional embolization according to source and stability. Do not blindly clamp deep posterior nasal or pterygopalatine tissue: uncontrolled visualization places vascular and skull-base structures at risk. Ongoing shock is a reason to defer definitive reconstruction.

Vision and orbit — document acuity, pupils, afferent pupillary function, globe position and extraocular movements as early as feasible because edema and anesthesia may erase the baseline examination. Protect a suspected open globe and involve ophthalmology urgently. A tense orbit with proptosis, falling vision and a relative afferent pupillary defect is orbital compartment syndrome; when the clinical diagnosis is compelling, decompression is time critical and should not wait for a perfect CT or definitive fracture repair. Entrapment with oculocardiac symptoms is a different urgent orbital problem. Fracture reduction without first understanding globe and optic status can turn an occult injury into permanent blindness.

Skull base and CSF — inspect CT for cribriform/ethmoid roof, frontal sinus posterior-table and sphenoid involvement, pneumocephalus and trajectories near the carotid canal or optic pathway. Look clinically for CSF rhinorrhea/otorrhea and cranial neuropathy. Suspected CSF leak is a reason to avoid unnecessary blind nasal instrumentation, not a reason to probe the defect. Persistent or complex leaks require coordinated skull-base/neurosurgical decision-making. Durable anatomy principles still apply even as current evidence changes the route and timing of selected interventions.

Le Fort anatomy — Le Fort I separates the tooth-bearing maxilla/palate from the upper midface; Le Fort II is pyramidal and crosses the nasal bridge/medial orbital region toward the infraorbital rims and pterygoid attachments; Le Fort III represents craniofacial dysjunction through nasofrontal, orbital and zygomatic interfaces. Real fractures often cross these idealized planes. Map pterygoid plates, palate, nasomaxillary and zygomaticomaxillary buttresses, frontozygomatic region, NOE complex, orbital walls and mandibular components directly rather than inferring the entire injury from one label.

Occlusion — true preinjury occlusion is the functional reference, but it must be earned rather than assumed. Use intact dentition, wear facets, dental records or photographs when available, arch form and fracture geometry. A sagittal or comminuted palatal fracture can widen the maxillary arch; a displaced mandibular fracture can rotate the lower arch. Applying maxillomandibular fixation to two malreduced arches creates a false occlusal platform and locks deformity into every subsequent plate. Reconstruct/stabilize the palate and mandible sufficiently to create a trustworthy maxillomandibular unit before using the bite as a reference.

Three-dimensional facial frame — restore the vertical and horizontal buttresses that transmit load and define facial form. The reconstruction must re-establish facial width through accurate zygomatic positioning, vertical facial height and anterior projection. The zygoma must be positioned in three dimensions, not simply aligned at one easy-to-see rim. A small error at an early reference propagates across the face; plates hold a reduction, but they cannot rescue a wrong skeletal framework.

Sequencing — there is no universal top-down or bottom-up dogma. AO's current panfacial framework explicitly describes bottom-up reconstruction from the maxillomandibular unit, top-down reconstruction from the calvarium/frontal frame, and strategies that create upper and lower facial units and link them at the Le Fort I level. Start from the patient's most reliable reference structures and the side with the least comminution. If the mandible and dental arch are trustworthy while the frontal frame is fragmented, bottom-up may be logical. If the lower face is severely comminuted but the frontal/upper facial frame is reliable, top-down may be safer. The sequence is a reasoning tool, not a slogan.

NOE and medial canthus — assess medial canthal tendon attachment and central-fragment stability. If the NOE framework is not anatomically restored, an apparently straight nasal bridge can still heal with traumatic telecanthus and loss of nasal projection. Preserve lacrimal structures when feasible and obtain specialized repair when required. Intercanthal distance and central facial projection must be checked as structural endpoints.

ZMC and orbital framework — reconstruct the zygomatic complex from multiple reliable interfaces so orbital volume is built on the correct skeleton. Restoring the orbital floor before the zygoma and surrounding framework are correctly reduced can create the wrong orbital volume and lead to enophthalmos or diplopia. Before closure, reassess globe position and pupils, perform forced ductions when indicated, and ensure hardware or reconstructed walls are not impinging the globe, extraocular muscles or orbital apex.

Fixation and iterative verification — expose enough stable bone to identify reduction while limiting unnecessary soft-tissue injury. Fixation strength depends on load, comminution, bone quality and fracture pattern. Recheck occlusion after major units are linked. If the bite changes after fixation, stop adding plates and find the upstream malreduction. Similarly, a change in globe findings, uncontrolled hemorrhage or unexpected instability is a cue to reassess the framework rather than continue the planned sequence mechanically.

Senior bailout — when every landmark is mobile, do not choose an arbitrary corner and plate outward. Re-establish one trustworthy reference: the mandibular/dental arch, reconstructed palate, frontal bar or accurately reduced zygoma depending on the injury. Stop or stage if physiology is unstable, hemorrhage remains uncontrolled, swelling prevents meaningful ocular assessment, contaminated tissue requires serial debridement, or the available landmarks cannot support a reliable definitive reduction. Temporary stabilization followed by delayed definitive fixation is preferable to locking in malocclusion, telecanthus, orbital-volume error or facial-width deformity in an unsafe patient.

Complication rescue — new visual loss, a new afferent pupillary defect or tense proptosis intraoperatively or postoperatively is an emergency: release external compression and pursue orbital-compartment rescue rather than waiting for routine imaging. Major recurrent epistaxis requires controlled hemostatic evaluation rather than repeated blind posterior instrumentation. Severe postoperative malocclusion means reduction must be reassessed before consolidation. CSF leak, hardware infection/exposure, malunion, diplopia, enophthalmos, telecanthus and nasal obstruction should be traced back to the failed structural or soft-tissue problem instead of being treated as isolated cosmetic complications.

Senior synthesis — before definitive ORIF, answer six questions explicitly: Is the airway secure for the operation and postoperative swelling? Is hemorrhage controlled? Has vision been documented and every time-critical orbital emergency addressed? Is the skull base mapped? Is the occlusal platform truly preinjury rather than widened or rotated? What is the most reliable reference from which to rebuild width, height and projection? The dangerous resident error is mistaking a memorized Le Fort label or sequencing preference for an operative plan. Expert management repeatedly verifies airway, physiology, vision, occlusion and stable anatomy and is willing to stop or stage when those prerequisites are not trustworthy."""

TRAPS = [
    "Naming a Le Fort pattern from one fracture line and failing to map mixed NOE, ZMC, orbital, palatal, mandibular and skull-base components.",
    "Prioritizing fixation before securing an airway threatened by blood, secretions, loose teeth, edema or a mobile midface.",
    "Repeating traumatic intubation attempts instead of escalating to structured rescue and emergency front-of-neck access when oxygenation fails.",
    "Treating all nasotracheal intubation as automatically safe or automatically forbidden from the Le Fort label rather than the actual skull-base anatomy and technique.",
    "Blindly instrumenting the nose through an incompletely characterized central skull-base or NOE injury.",
    "Chasing posterior hemorrhage with blind clamps rather than resuscitation, controlled exposure or embolization.",
    "Failing to document vision before edema or anesthesia removes the baseline examination.",
    "Waiting for definitive ORIF or perfect imaging while clinically obvious orbital compartment syndrome threatens irreversible blindness.",
    "Using maxillomandibular fixation to lock a widened palate or malreduced mandible into a false occlusal platform.",
    "Treating top-down or bottom-up as dogma rather than beginning from the most reliable intact reference.",
    "Fixing one visible buttress while global facial width, height or projection remains wrong.",
    "Ignoring medial canthal tendon/NOE stability and producing persistent traumatic telecanthus.",
    "Reconstructing orbital volume before the zygomatic framework is accurately reduced.",
    "Continuing to add plates after the bite or globe findings change rather than locating the upstream error.",
    "Forcing one-stage definitive panfacial ORIF despite unstable physiology, uncontrolled bleeding, massive swelling or unreliable landmarks when staged stabilization is safer.",
]

COHORT = {QIDS[0]: {
    "concept_id": CID,
    "canonical_topic": TOPIC,
    "prompt": PROMPT,
    "answer_text": ANSWER,
    "explanation": "Panfacial trauma is rebuilt from physiology and reliable references: secure airway/hemostasis/vision first, map the actual CT injury, establish true occlusion, then restore facial width, height and projection using the most reliable anatomy rather than a memorized sequencing slogan.",
    "board_pearl": "Do not plate chaos: create a trustworthy reference and real occlusal platform; if airway, bleeding, vision, physiology or landmarks are uncontrolled, stop or stage rather than lock in catastrophe.",
    "depth_layers_v221": {
        "foundation":"Trauma priorities, Le Fort pattern anatomy, facial buttresses, orbit/NOE/skull base and occlusion as the functional reference.",
        "application":"Airway-route selection, hemorrhage control, CT injury mapping, palate/mandible stabilization, top-down versus bottom-up sequencing and three-dimensional fixation.",
        "senior_decision":"Rescue vision/airway/bleeding before fixation; choose the most reliable starting reference; stop or stage when physiology or fragmented landmarks make definitive reconstruction unsafe."
    },
    "common_traps_v221": TRAPS,
    "deliberate_review_v221": "Selected from the exact successful v20.20 production backlog. It ranked low lexically, but its prior 14-word answer left major resident/board/OR hazards unaddressed: difficult airway, hemorrhage, blindness, skull-base injury, false occlusal references and sequencing failure.",
    "source_refs_v221": SOURCE_REFS_V221,
    "evidence_distinction_v221": "Durable Cummings/Pasha/K.J. Lee anatomy, buttress, occlusion and fixation principles are preserved. Current AO Surgery Reference guides reliable-reference sequencing. Contemporary 2025 airway evidence is used to avoid two false absolutes: blind nasal instrumentation across an uncertain skull base remains hazardous, but a Le Fort label alone does not prove every controlled nasotracheal approach is contraindicated. Current difficult-airway guidance emphasizes first-attempt success, structured rescue and emergency front-of-neck access.",
    "audit_profile_v221": "le_fort_panfacial_trauma",
}}

def apply_concept_check_task_alignment_v221(checks, deep_modules, v6_item_id):
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
        q["task_alignment_v221"] = True
        repaired.append(qid)
    return {"repaired": repaired, "missing": missing, "link_mismatch": link_mismatch}