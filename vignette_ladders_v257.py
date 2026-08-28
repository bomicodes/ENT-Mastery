"""v25.7 — Facial Plastics / Trauma deliberate ladder pass 1.

Begins the next incomplete canonical domain with five high-yield trauma/call topics.
Each topic receives a foundation -> application -> senior-decision ladder centered
on examination priorities, airway/vision/occlusion threats, operative timing, and
avoiding irreversible functional loss.
"""
DOMAIN = "Facial Plastics / Trauma"


def _q(qid, topic, stage, stem, choices, answer, explanation, reasons, pearl,
       curveball, focus="boards"):
    return {
        "id": qid, "domain": DOMAIN, "topic": topic, "learning_stage": stage,
        "stem": stem, "choices": choices, "answer": answer,
        "explanation": explanation, "why_wrong": reasons,
        "board_pearl": pearl, "curveball": curveball,
        "tier": "Curated learning ladder", "mode": "Vignette", "focus": focus,
        "ladder_reviewed": True, "_coverage_reviewed_v211": True,
    }


VIGNETTES_V257 = [
    _q("v257_fpt_exam_fnd", "Structured Facial Trauma Examination", "foundation",
       "A patient arrives after high-speed blunt facial trauma. After primary trauma stabilization, which focused examination should be documented before swelling and sedation obscure findings?",
       ["Visual acuity and pupils, extraocular movements, facial sensation and motor function, occlusion, trismus, bony step-offs/mobility, nasal septum, oral cavity, and soft-tissue injuries", "Only external photographs because palpation may worsen fractures", "Only a dental examination because facial fractures do not threaten vision", "Delay all cranial-nerve and ocular assessment until after definitive fracture repair"], 0,
       "Once airway, breathing, circulation, and cervical-spine priorities are addressed, a structured facial examination establishes critical preoperative baselines. Vision, pupils, motility, occlusion, cranial-nerve function, septum, and skeletal stability can change or become difficult to interpret as edema progresses.",
       ["Correct. These findings localize injury, identify time-sensitive threats, and provide a baseline for operative counseling and postoperative comparison.", "Photography is useful but cannot replace examination for vision, occlusion, nerve deficits, septal hematoma, or unstable skeletal segments.", "Facial trauma can threaten the globe, optic nerve, airway, and cranial nerves in addition to dentition.", "Waiting until after repair loses the preoperative neurologic, ocular, and occlusal baseline needed to distinguish injury from treatment-related change."],
       "In facial trauma, document what the patient could see, feel, move, and bite like before you operate.",
       "Which finding on the initial eye examination requires action before routine CT review or fracture planning?"),
    _q("v257_fpt_exam_app", "Structured Facial Trauma Examination", "application",
       "A patient with midface trauma has normal oxygenation but new decreased visual acuity, a relative afferent pupillary defect, proptosis, and a tense orbit. What should dominate the next decision?",
       ["Treat suspected orbital compartment syndrome as a vision-threatening emergency and decompress promptly when the clinical diagnosis is present rather than waiting for routine fracture planning", "Observe until facial swelling resolves", "Prioritize dental impressions before addressing the eye", "Schedule elective orbital-floor repair several weeks later without acute intervention"], 0,
       "Decreased vision, RAPD, proptosis, tense orbit, and compatible mechanism suggest orbital compartment syndrome. Vision can be permanently lost from pressure-related optic ischemia; emergent lateral canthotomy/cantholysis is a clinical rescue procedure when indicated and should not be delayed for routine fracture sequencing.",
       ["Correct. The threatened organ—vision—sets the priority before elective skeletal reconstruction.", "Observation risks irreversible optic-nerve and retinal ischemic injury.", "Occlusion matters, but it does not supersede an acute vision-threatening compartment syndrome.", "Elective floor repair addresses fracture anatomy, not the immediate orbital-pressure emergency."],
       "Not every dramatic CT fracture is emergent, but a threatened eye is.",
       "How would an open globe concern alter bedside orbital manipulation and the sequence of ophthalmologic care?", "overnight_call"),
    _q("v257_fpt_exam_snr", "Structured Facial Trauma Examination", "senior_decision",
       "A polytrauma patient has panfacial fractures, heavy edema, an unreliable initial history, and planned fixation. Which senior-level preparation best reduces avoidable postoperative diagnostic confusion?",
       ["Reconcile preoperative CT with a repeatable documented functional examination, explicitly noting baseline vision, pupils, motility, facial nerve/trigeminal findings, occlusion, hearing, nasal/septal findings, and any exam limitation before fixation", "Rely on the CT alone because function can be inferred from fracture lines", "Omit examination elements that cannot be completed perfectly", "Assume every postoperative deficit was present before surgery unless the patient proves otherwise"], 0,
       "Complex trauma requires an explicit baseline and acknowledgment of what could not be assessed. Imaging maps bone but does not substitute for visual function, nerve function, globe examination, occlusion, or dynamic mobility; documenting uncertainty is safer than inventing a normal baseline.",
       ["Correct. A structured baseline improves operative planning, handoffs, informed consent, and recognition of new postoperative deficits.", "CT cannot establish visual acuity, RAPD, facial movement, dental occlusion, or many sensory deficits.", "Limitations should be documented and reassessed, not silently omitted.", "Assuming a deficit was preexisting can miss a surgical complication and undermines safe postoperative surveillance."],
       "A good trauma note is part of the operation: it defines the functional starting point and what still needs reassessment.",
       "Which deficits should trigger immediate postoperative re-examination before attributing them to expected edema?", "senior_management"),

    _q("v257_fpt_zmc_fnd", "ZMC / Orbital Trauma", "foundation",
       "A patient struck in the cheek has malar flattening, infraorbital numbness, palpable infraorbital-rim step-off, and diplopia. Which injury pattern best fits?",
       ["Zygomaticomaxillary complex fracture with associated orbital involvement", "Isolated mandibular condyle fracture", "Septal perforation", "Temporal-bone longitudinal fracture"], 0,
       "The zygoma contributes to malar projection, orbital rim/floor, and facial width. ZMC disruption can produce flattening, infraorbital-nerve dysfunction, trismus from arch impingement, orbital-volume change, and diplopia.",
       ["Correct. The combination of malar contour change, infraorbital sensory loss, rim step-off, and ocular symptoms is classic for ZMC/orbital trauma.", "Condyle fractures primarily affect occlusion, preauricular pain, and mandibular motion rather than the malar eminence and orbital rim.", "Septal perforation causes nasal symptoms and does not explain malar flattening or orbital findings.", "Temporal-bone fractures can affect hearing and facial nerve function but do not produce this characteristic midface pattern."],
       "ZMC is not a single fracture line; think malar projection, orbital volume, facial width, and the infraorbital nerve together.",
       "What mechanism can cause trismus in a displaced zygomatic-arch component?"),
    _q("v257_fpt_zmc_app", "ZMC / Orbital Trauma", "application",
       "A child with orbital trauma has nausea, bradycardia, marked pain with attempted upgaze, and limited vertical eye movement despite relatively little external bruising. What is the best interpretation?",
       ["Suspect a trapdoor orbital fracture with extraocular muscle/soft-tissue entrapment and oculocardiac reflex, prompting urgent specialty evaluation and release rather than routine delayed observation", "Minimal bruising excludes significant orbital injury", "Treat only the nausea and reassess in several weeks", "Assume the motility deficit is voluntary guarding"], 0,
       "Children can develop elastic trapdoor fractures that entrap orbital tissue while the bony segment recoils. Painful motility restriction with nausea, vomiting, or bradycardia reflects the oculocardiac reflex and can indicate true entrapment requiring urgent release.",
       ["Correct. The physiologic reflex and restricted motility make this more urgent than a typical uncomplicated floor fracture.", "The 'white-eye' appearance is precisely why significant pediatric entrapment can be underestimated externally.", "Symptom treatment without addressing entrapment risks persistent ischemic muscle injury and motility dysfunction.", "A reproducible deficit with vagal symptoms after trauma should not be dismissed as poor effort."],
       "In pediatric orbital trauma, a quiet-looking eye with nausea/bradycardia can be more dangerous than a dramatic black eye.",
       "What examination and imaging features distinguish muscle entrapment from diplopia caused only by edema?", "overnight_call"),
    _q("v257_fpt_zmc_snr", "ZMC / Orbital Trauma", "senior_decision",
       "An adult has a displaced ZMC fracture with malar flattening, increased orbital volume, and a large floor defect. There is no orbital compartment syndrome or open globe. What principle should guide definitive repair?",
       ["Restore three-dimensional zygomatic position and stable facial buttresses first, then reconstruct the orbital defect on reliable bony ledges while protecting the infraorbital nerve, periorbita, extraocular muscles, and posterior orbit", "Place an orbital implant before reducing the displaced zygoma", "Reduce only the most visible anterior rim and ignore facial width and rotation", "Extend dissection blindly toward the orbital apex to maximize implant size"], 0,
       "Orbital volume and floor geometry depend on correct zygomatic position. Definitive repair therefore requires accurate three-dimensional reduction and stable fixation of the ZMC before judging the residual orbital defect; reconstruction then uses supported ledges while avoiding muscle entrapment and posterior optic structures.",
       ["Correct. Restoring the skeletal frame first prevents reconstructing an orbit around a malpositioned zygoma.", "An implant sized before zygomatic reduction can encode the wrong orbital volume and position.", "A cosmetically aligned anterior rim can hide persistent rotation, width, or posterior displacement.", "Blind posterior dissection risks the orbital apex and optic nerve and is not required for sound reconstruction."],
       "Reduce the frame before you rebuild the floor; orbital reconstruction is only as accurate as the zygoma beneath it.",
       "After fixation, what intraoperative findings would make you revise the reduction or implant before closure?", "OR_prep"),

    _q("v257_fpt_mandible_fnd", "Mandible Fracture", "foundation",
       "After a punch to the jaw, a patient has new malocclusion, lower-lip numbness, and tenderness with a palpable mandibular step-off. What is the most useful functional clue that the mandibular ring has been disrupted?",
       ["A new change in dental occlusion", "Isolated nasal congestion", "Normal tympanic membranes", "Loss of smell without dental symptoms"], 0,
       "Occlusion is a sensitive functional marker of mandibular alignment. Fractures may also cause pain, mobility, trismus, gingival laceration, step-offs, and inferior alveolar/mental nerve sensory change.",
       ["Correct. A patient often notices even small changes in the relationship of the dental arches, making new malocclusion highly informative.", "Nasal congestion localizes poorly to mandibular alignment.", "Normal ear examination does not exclude a mandibular fracture.", "Anosmia suggests a different injury pattern and does not explain the occlusal change."],
       "In mandibular trauma, ask the patient whether the bite feels normal before you decide the bones are aligned.",
       "Why can a unilateral condylar fracture produce an apparently distant change in anterior occlusion?"),
    _q("v257_fpt_mandible_app", "Mandible Fracture", "application",
       "A dentate adult has a displaced mandibular-body fracture through the tooth-bearing segment with gross malocclusion. Airway is stable. What principle best guides definitive treatment?",
       ["Re-establish the patient's premorbid occlusion and stable mandibular continuity, using maxillomandibular fixation and/or open reduction internal fixation according to fracture pattern, displacement, dentition, and associated injuries", "Align the inferior border cosmetically while ignoring the bite", "Extract every tooth adjacent to any fracture automatically", "Delay all oral hygiene and perioperative infection precautions because oral fractures are sterile"], 0,
       "Functional restoration centers on premorbid occlusion and stable bone healing. Technique varies by location and biomechanics; teeth in the fracture line are not automatically removed unless they are infected, fractured, nonrestorable, obstruct reduction, or otherwise compromise treatment.",
       ["Correct. Occlusion and stable continuity are the endpoints; fixation strategy follows the mechanics and patient context.", "A smooth lower border with persistent malocclusion is not an adequate functional reduction.", "Routine extraction can sacrifice useful dentition and is unnecessary when a tooth is healthy and does not interfere with reduction.", "Tooth-bearing fractures communicate with oral flora and require appropriate perioperative infection prevention and meticulous oral care rather than being treated as sterile injuries."],
       "Fix the bite, not just the X-ray.",
       "How would an edentulous atrophic mandible change fixation strategy and the importance of load-bearing reconstruction?", "OR_prep"),
    _q("v257_fpt_mandible_snr", "Mandible Fracture", "senior_decision",
       "A patient with a mandibular angle fracture also has bilateral midface fractures and loss of reliable facial width/height landmarks. What is the best senior-level sequencing principle?",
       ["Use reproducible occlusion and mandibular arch form as a foundational reference when feasible, then restore midface width, projection, and vertical relationships in a planned panfacial sequence", "Fix whichever small plate is easiest to reach first without a global plan", "Ignore occlusion until all midface plates are final", "Set facial width by soft-tissue appearance alone while the patient is anesthetized"], 0,
       "Panfacial reconstruction requires a stable reference. In many patterns, restoring mandibular continuity and premorbid occlusion creates a lower facial framework against which the midface can be rebuilt, although exact top-down versus bottom-up sequencing is individualized to which landmarks remain trustworthy.",
       ["Correct. The principle is to establish a reliable skeletal reference and progress systematically rather than accumulating locally acceptable but globally incompatible reductions.", "Unplanned fixation can lock in width, projection, or occlusal errors that become harder to correct later.", "Finalizing the midface without a dependable occlusal reference risks facial-height and bite discrepancies.", "Edema and draping make soft tissue an unreliable sole guide to bony width during complex fixation."],
       "Panfacial trauma is a sequencing problem: establish one trustworthy frame before asking the next segment to match it.",
       "When might a top-down sequence be preferable because the cranial or frontal reference is more reliable than the mandible?", "senior_management"),

    _q("v257_fpt_nasal_fnd", "Nasal Fracture", "foundation",
       "A patient presents after nasal trauma with swelling, epistaxis, and a visibly deviated nasal dorsum. Which examination must be performed before simply arranging delayed fracture reduction?",
       ["Intranasal examination specifically looking for a septal hematoma and mucosal injury", "Only external profile photographs", "Routine diagnostic nasal bone radiographs in every uncomplicated case", "No examination until swelling has completely resolved"], 0,
       "Nasal fracture diagnosis is usually clinical, but the intranasal examination is essential because a septal hematoma is an urgent complication that can destroy septal cartilage if missed.",
       ["Correct. Septal hematoma is the time-sensitive finding that changes management immediately.", "External photographs do not evaluate the septal mucoperichondrial space.", "Plain films rarely change management for an isolated uncomplicated nasal fracture and do not exclude septal hematoma.", "Waiting for swelling to subside before inspecting the septum risks cartilage necrosis and abscess."],
       "Every nasal-trauma examination includes the septum; the emergency is often inside the nose, not the crooked nasal bones.",
       "What intranasal appearance and palpation distinguish a septal hematoma from a simple deviated septum?"),
    _q("v257_fpt_nasal_app", "Nasal Fracture", "application",
       "An adult with an isolated displaced nasal fracture has no septal hematoma, CSF leak, uncontrolled epistaxis, or other facial fracture. Swelling makes immediate contour assessment unreliable. What timing principle is appropriate?",
       ["Reassess after edema subsides and perform closed reduction within the early healing window before the bones become fixed, with timing individualized to swelling and patient factors", "Wait several months until the fracture has fully united before attempting closed reduction", "Perform emergent open rhinoplasty on every displaced fracture", "Do nothing because traumatic nasal obstruction and deformity cannot be improved after injury"], 0,
       "When swelling obscures deformity, a short interval for edema reduction improves assessment. Closed reduction is then performed before substantial bony healing makes manipulation difficult; exact timing varies with age, swelling, and local practice.",
       ["Correct. The goal is enough time for assessment but not so much time that early union prevents effective closed manipulation.", "Once the bones have healed in malposition, closed reduction is less effective and later formal septorhinoplasty may be required.", "Most isolated fractures do not need acute open rhinoplasty; treatment should match complexity and associated septal injury.", "Many acute deformities and obstruction patterns improve with appropriate reduction; nihilism is inappropriate."],
       "Nasal-fracture timing balances two clocks: swelling must fall, but bone healing must not advance too far.",
       "What associated injuries would make this an immediate operative or broader facial-trauma problem rather than a routine delayed closed reduction?", "senior_management"),
    _q("v257_fpt_nasal_snr", "Nasal Fracture", "senior_decision",
       "A patient returns months after inadequately treated nasal trauma with persistent obstruction, dorsal deviation, septal deformity, and internal/external valve compromise. What is the best planning principle?",
       ["Treat the healed problem as a functional structural deformity: define septal, bony-vault, and valve contributors and plan definitive septorhinoplasty rather than repeating an acute-fracture maneuver", "Repeat office closed reduction indefinitely despite healed bone", "Treat only with decongestants because trauma cannot alter nasal valves", "Correct the dorsal appearance while deliberately ignoring airflow"], 0,
       "Late post-traumatic obstruction may reflect healed septal deviation, bony-vault displacement, narrowing, and valve dysfunction. Once acute reduction is no longer appropriate, reconstruction should address the specific structural causes of both obstruction and deformity.",
       ["Correct. Chronic post-traumatic nasal dysfunction requires a new structural analysis rather than pretending the injury is still an acute mobile fracture.", "Healed bone and scar do not reliably respond to repeated closed reduction.", "Decongestants cannot correct fixed skeletal and valve collapse.", "Cosmetic-only correction can leave the patient's principal functional complaint unresolved."],
       "Acute fracture reduction and delayed functional septorhinoplasty solve different problems on different timelines.",
       "How would prior septal cartilage loss alter your graft-source planning for delayed reconstruction?", "senior_management"),

    _q("v257_fpt_sept_hema_fnd", "Septal Hematoma", "foundation",
       "After nasal trauma, a child has worsening bilateral nasal obstruction. Examination shows a soft, fluctuant, violaceous swelling bulging from both sides of the septum. What is the diagnosis?",
       ["Septal hematoma", "Simple fixed septal deviation", "Inferior turbinate hypertrophy", "Choanal atresia"], 0,
       "A septal hematoma is blood trapped between septal cartilage and its mucoperichondrium, often producing soft bilateral fluctuant swelling after trauma. It compromises diffusion-dependent cartilage nutrition and can rapidly progress to necrosis or abscess.",
       ["Correct. The post-traumatic fluctuant bilateral septal swelling is classic and requires urgent treatment.", "A deviated septum is firm structural cartilage/bone rather than a new fluctuant mucosal collection.", "Turbinate hypertrophy arises from the lateral nasal wall, not the septal mucoperichondrial plane.", "Choanal atresia is congenital posterior obstruction and does not present as an acute fluctuant septal mass after trauma."],
       "Septal cartilage has no direct blood supply; separating it from mucoperichondrium threatens the cartilage itself.",
       "Why is the risk of later saddle-nose deformity especially important in a growing child?"),
    _q("v257_fpt_sept_hema_app", "Septal Hematoma", "application",
       "A traumatic septal hematoma is confirmed. What is the correct management?",
       ["Urgent drainage with evacuation of clot, measures to prevent reaccumulation, appropriate antimicrobial coverage, and close re-examination", "Observe for spontaneous resolution over several weeks", "Treat with topical decongestant alone", "Perform cosmetic dorsal filler injection over the collection"], 0,
       "Prompt drainage restores mucoperichondrial contact and limits cartilage necrosis. Incision/aspiration technique depends on size and patient factors, but the key principles are complete evacuation, prevention of reaccumulation, infection treatment/prevention, and early follow-up.",
       ["Correct. Septal hematoma is an urgent drainage problem because delay risks abscess and structural cartilage loss.", "Observation permits ongoing ischemia and infection and can lead to saddle deformity or more serious complications.", "Decongestants do not evacuate blood from the mucoperichondrial plane.", "Filler neither treats the collection nor prevents cartilage necrosis and could worsen infection risk."],
       "Drain it, keep it drained, and look again soon—the operation is incomplete without surveillance for reaccumulation.",
       "What findings would suggest the hematoma has already evolved into a septal abscess?", "overnight_call"),
    _q("v257_fpt_sept_hema_snr", "Septal Hematoma", "senior_decision",
       "A patient presents late with fever, purulent septal drainage, loss of cartilaginous support, and early saddle deformity after missed nasal trauma. What is the best senior-level approach?",
       ["Control the septal infection urgently with drainage/culture-directed therapy and preserve viable tissue; defer definitive structural reconstruction until infection and tissue viability are stabilized", "Place definitive cartilage grafts into the infected field immediately for cosmetic correction", "Ignore the infection and schedule routine closed nasal fracture reduction", "Treat only with oral decongestants because the deformity is already permanent"], 0,
       "A septal abscess with cartilage necrosis is first an infection and tissue-viability emergency. Definitive reconstruction is usually planned after the infection has resolved and the remaining support/scar pattern is clear, rather than implanting graft material into uncontrolled infection.",
       ["Correct. Source control and preservation of remaining viable support come before elective reconstruction.", "Immediate grafting into an infected field risks graft loss and persistent infection.", "Closed reduction does not address abscess, necrotic cartilage, or a mature support deficit.", "The infection still requires urgent treatment, and later reconstruction can address functional and structural sequelae."],
       "When septal hematoma is missed, the priority sequence becomes infection control first, reconstruction second.",
       "Which autologous graft sources might be considered later if septal cartilage is no longer available for structural reconstruction?", "senior_management"),
]


def apply_learning_ladders_v257(challenges, concept_id_fn):
    """Append only missing v25.7 cases and attach exact canonical concept IDs."""
    existing = {str(q.get("id")) for q in challenges}
    added = 0
    for source in VIGNETTES_V257:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["choices"] = list(source.get("choices") or [])
        q["why_wrong"] = list(source.get("why_wrong") or [])
        q["concept_id"] = concept_id_fn(DOMAIN, q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1
    return added
