"""
v13.2 - Facial Plastics / Trauma vignette batch, targeting the weakest-
coverage domain (23% before this batch). Prioritized by board yield and
overnight-call/OR relevance over raw topic-count.
"""

VIGNETTES_V132 = [
{
"id": "v132_fprs_01", "domain": "Facial Plastics / Trauma", "topic": "Le Fort / Panfacial Trauma",
"stem": "A patient after high-speed MVC has midface mobility on manual manipulation of the maxillary alveolus, with the entire midface moving as a unit relative to the skull base but the nasofrontal junction remaining stable. Which Le Fort pattern is most consistent with this exam?",
"choices": ["Le Fort I", "Le Fort II", "Le Fort III", "Isolated zygomaticomaxillary complex fracture"],
"answer": 2,
"explanation": "Le Fort III (craniofacial dysjunction) separates the entire midface from the skull base at the level of the zygomaticofrontal sutures, nasofrontal junction, and orbits, so the whole midface moves as one unit on exam. If the nasofrontal junction itself were mobile with the maxilla, that would suggest an even higher/combined pattern.",
"why_wrong": ["Le Fort I involves only the maxillary alveolus/palate moving separately from the upper midface, not the entire midface as a block.","Le Fort II is a pyramidal fracture through the nasal bones and medial orbits; the nasal complex typically moves with the maxilla, unlike the isolated-alveolus pattern of Le Fort I.","Correct.","An isolated ZMC fracture produces mobility localized to the cheek/zygoma, not the entire midface."],
"board_pearl": "Le Fort patterns are rarely pure or symmetric in real trauma - describe what actually moves on exam rather than forcing the injury into one textbook category.",
"curveball": "The patient also has clear rhinorrhea. How does that change your preoperative workup before fixation?",
"tier": "Curated board-style", "mode": "Vignette"
},
{
"id": "v132_fprs_02", "domain": "Facial Plastics / Trauma", "topic": "NOE Fracture Mechanics",
"stem": "After facial trauma, a patient has traumatic telecanthus and a rounded, ill-defined medial canthal angle. Bimanual palpation with one instrument on the caruncle and one on the lateral orbital rim demonstrates bone mobility. What does this confirm?",
"choices": ["An isolated nasal bone fracture", "A nasoorbitoethmoid (NOE) fracture with a mobile medial canthal tendon-bearing bone fragment", "A pure orbital floor blowout fracture", "A zygomatic arch fracture"],
"answer": 1,
"explanation": "The bimanual exam (bowstring test) specifically assesses whether the bone fragment bearing the medial canthal tendon is mobile, which confirms an unstable NOE fracture requiring precise tendon-bearing fragment fixation rather than simple reduction.",
"why_wrong": ["An isolated nasal fracture does not typically produce telecanthus or medial canthal tendon instability.","Correct.","An orbital floor blowout fracture affects globe position and extraocular motion, not medial canthal tendon stability.","A zygomatic arch fracture affects the lateral midface and does not produce medial canthal telecanthus."],
"board_pearl": "Traumatic telecanthus with a positive bowstring test defines an unstable NOE fracture - the surgical goal is precise repositioning and fixation of the canthal-bearing fragment, not just general facial reduction.",
"curveball": "Fixation is delayed 3 weeks due to other injuries. How does that change the difficulty and approach to canthal reduction?",
"tier": "Curated board-style", "mode": "Vignette"
},
{
"id": "v132_fprs_03", "domain": "Facial Plastics / Trauma", "topic": "Nasal Fracture",
"stem": "A patient presents 5 days after a nasal fracture with persistent deviation but resolving edema. What is the most appropriate next step?",
"choices": ["Immediate open septorhinoplasty", "Closed reduction, since it remains feasible within the first 1-2 weeks before the bones set", "Observation only, since nasal fractures do not benefit from reduction after 72 hours", "CT is mandatory before any intervention can be considered"],
"answer": 1,
"explanation": "Closed reduction is typically still effective within about 1-2 weeks of injury (sometimes longer in children, shorter in adults) before the fracture fragments become fixed; waiting for edema to resolve for accurate assessment is reasonable as long as reduction still occurs within this window.",
"why_wrong": ["Open septorhinoplasty is reserved for cases with septal fracture-dislocation, prior closed reduction failure, or complex/delayed presentations, not the routine first step.","Correct.","This ignores the real, time-limited window during which closed reduction remains effective.","CT is not mandatory for an isolated, uncomplicated nasal fracture; the diagnosis and reduction decision are primarily clinical."],
"board_pearl": "The closed-reduction window for nasal fractures is time-limited, not indefinite - always document the day of injury and act before the fragments fixate.",
"curveball": "On closer exam, the septum is also dislocated off the maxillary crest. Does that change the plan from closed to open reduction?",
"tier": "Curated board-style", "mode": "Vignette"
},
{
"id": "v132_fprs_04", "domain": "Facial Plastics / Trauma", "topic": "Frontal Sinus Fracture",
"stem": "CT after frontal trauma shows a displaced posterior table fracture with a small amount of pneumocephalus but no obvious CSF leak. What principle most influences management here?",
"choices": ["Posterior table involvement raises concern for dural injury and CSF leak, requiring close evaluation and often neurosurgical involvement regardless of an obvious leak on initial exam", "Only anterior table fractures matter clinically", "Pneumocephalus is a normal incidental finding requiring no further workup", "The frontal sinus should always be cranialized regardless of duct or posterior table status"],
"answer": 0,
"explanation": "Posterior table fractures risk dural tear and CSF leak, intracranial contamination, and long-term mucocele formation even when a leak isn't obvious immediately, so these injuries generally warrant close monitoring, appropriate imaging follow-up, and multidisciplinary (often neurosurgical) involvement.",
"why_wrong": ["Correct.","Anterior table-only fractures are important for contour but carry much lower risk of intracranial complications than posterior table involvement.","Pneumocephalus in this context reflects a breach of the intracranial compartment and should prompt further evaluation, not be dismissed as incidental.","Cranialization is one option for specific patterns (e.g., significantly displaced/comminuted posterior table or duct-involving injury), not a default for every frontal sinus fracture."],
"board_pearl": "Frontal sinus fracture management decisions hinge on posterior table displacement and nasofrontal duct/outflow tract status, not just whether the sinus contour looks abnormal on exam.",
"curveball": "Follow-up imaging months later shows an opacified frontal sinus with a normal-appearing outflow tract. What complication must be excluded?",
"tier": "Curated board-style", "mode": "Vignette"
},
{
"id": "v132_fprs_05", "domain": "Facial Plastics / Trauma", "topic": "Structured Facial Trauma Examination",
"stem": "A trauma patient has multiple facial fractures. Before any imaging is reviewed, which two exam components are most important to document early and specifically because they can be obscured or forgotten once swelling progresses or the patient is sedated?",
"choices": ["Skin color and hair distribution", "Visual acuity/globe exam and cranial nerve (especially facial nerve) function", "Dental occlusion only", "Nasal airflow symmetry only"],
"answer": 1,
"explanation": "Vision-threatening injury and facial nerve function are time-sensitive findings that can be lost to assessment once eyelid swelling progresses or the patient requires sedation/intubation; documenting them early is both clinically important and medicolegally protective.",
"why_wrong": ["Skin and hair findings are not the priority baseline exam elements in facial trauma.","Correct.","Occlusion matters but is not as time-sensitive to document before swelling/sedation as vision and facial nerve function.","Nasal airflow assessment is useful but not the most urgent baseline documentation priority in multi-system facial trauma."],
"board_pearl": "In facial trauma, document visual acuity and facial nerve function before swelling or sedation makes reliable assessment impossible - these findings, once lost, cannot be recovered later.",
"curveball": "The patient is intubated on arrival and cannot cooperate with a vision exam. What alternative assessment can still screen for a vision-threatening injury?",
"tier": "Curated board-style", "mode": "Vignette"
},
{
"id": "v132_fprs_06", "domain": "Facial Plastics / Trauma", "topic": "Mandibular Biomechanics and Occlusion",
"stem": "A patient has a mandible fracture and a new anterior open bite on exam. Which fracture pattern classically produces this occlusal finding?",
"choices": ["Isolated unilateral body fracture with normal condyles", "Bilateral condylar/subcondylar fractures with loss of posterior vertical ramus height", "Isolated symphyseal fracture without displacement", "Isolated coronoid process fracture"],
"answer": 1,
"explanation": "Bilateral condylar/subcondylar fractures cause bilateral loss of posterior mandibular ramus height, allowing the posterior teeth to over-approximate and the anterior mandible to rotate open, producing an anterior open bite.",
"why_wrong": ["A unilateral body fracture more typically produces a step-off or crossbite pattern rather than a symmetric anterior open bite.","Correct.","An isolated nondisplaced symphyseal fracture does not typically alter posterior ramus height or produce an open bite.","An isolated coronoid fracture affects temporalis attachment and jaw excursion, not vertical ramus height or occlusion in this pattern."],
"board_pearl": "An anterior open bite after facial trauma should make you specifically look for bilateral condylar/subcondylar fractures - the occlusion is a direct readout of posterior ramus height.",
"curveball": "The patient also has a chin laceration. Why does a chin laceration raise your suspicion for a specific mandible fracture pattern even before imaging?",
"tier": "Curated board-style", "mode": "Vignette"
},
{
"id": "v132_fprs_07", "domain": "Facial Plastics / Trauma", "topic": "Facial Soft-Tissue Lacerations / Burns",
"stem": "A patient has a deep cheek laceration medial to a line drawn from the lateral canthus to the oral commissure, with clear fluid draining from the wound when asked to bite down. What structure is most likely injured, and why does the fluid matter?",
"choices": ["Facial nerve buccal branch; the fluid suggests nerve sheath fluid", "Parotid duct (Stensen duct); the fluid may represent saliva, and duct injury requires specific repair over a stent", "Facial artery; the fluid represents lymphatic drainage", "Marginal mandibular nerve; the fluid is irrelevant"],
"answer": 1,
"explanation": "Lacerations along a line from the tragus to the midpoint of the upper lip (over the buccinator/duct course) that produce clear drainage, especially increasing with chewing/salivary stimulation, should raise concern for parotid (Stensen) duct injury, which requires identification and repair over a stent to prevent sialocele or fistula.",
"why_wrong": ["Facial nerve injury would produce a motor deficit, not primarily fluid drainage, and nerve sheath fluid is not a real clinical finding to test for this way.","Correct.","Facial artery injury would present with active bleeding, not clear fluid, and is not associated with lymphatic drainage in this context.","The marginal mandibular nerve produces a motor deficit if injured; it is not associated with fluid drainage, and dismissing the finding as irrelevant is wrong regardless of which nerve is considered."],
"board_pearl": "Clear fluid from a cheek laceration overlying the parotid duct's expected course is a duct injury until proven otherwise - test for it by looking for increased flow with gustatory stimulation and repair over a stent when confirmed.",
"curveball": "Cannulation of Stensen duct from the buccal papilla confirms the injury is proximal to the papilla but distal to the gland. How does injury location change repair feasibility?",
"tier": "Curated board-style", "mode": "Vignette"
},
{
"id": "v132_fprs_08", "domain": "Facial Plastics / Trauma", "topic": "Static Facial Reanimation",
"stem": "A patient has permanent, complete facial paralysis after resection of a large vestibular schwannoma with nerve sacrifice, and is not a candidate for further nerve grafting or free functional muscle transfer due to comorbidities. Which goal best describes static facial reanimation in this patient?",
"choices": ["Restoring voluntary, symmetric smile with dynamic movement", "Improving facial symmetry at rest and protecting the eye, without restoring active movement", "Restoring normal blink and tearing physiology", "Reversing atrophy of the paralyzed facial musculature"],
"answer": 1,
"explanation": "Static procedures (such as fascial slings, brow lifts, or lower-lid tightening) improve resting symmetry and provide functional support, particularly for eye protection, without providing active/dynamic movement - appropriate when dynamic reanimation is not feasible or desired.",
"why_wrong": ["Restoring dynamic, voluntary movement is the goal of dynamic reanimation techniques (e.g., nerve transfer, free functional muscle transfer), not static procedures.","Correct.","Static procedures do not restore normal blink dynamics, though they can help with lagophthalmos-related exposure risk through mechanical support.","Static procedures address position and symmetry, not muscle physiology/atrophy itself."],
"board_pearl": "Choosing static versus dynamic facial reanimation is about patient candidacy and goals, not a strict hierarchy - eye protection is often the single most urgent functional priority regardless of which approach is chosen.",
"curveball": "The patient's main complaint is actually poor eye closure with exposure keratitis, not the smile asymmetry. Which specific static intervention most directly addresses this?",
"tier": "Curated board-style", "mode": "Vignette"
},
{
"id": "v132_fprs_09", "domain": "Facial Plastics / Trauma", "topic": "Auricular Reconstruction",
"stem": "A child with unilateral microtia is being evaluated for staged autologous ear reconstruction using costal cartilage. Which factor most influences the recommended timing of surgery?",
"choices": ["Adequate costal cartilage size/framework material, generally reached by around age 8-10", "The procedure must be completed before age 2 regardless of cartilage availability", "Timing does not matter since cartilage graft size is unrelated to patient growth", "Reconstruction should always wait until after age 18"],
"answer": 0,
"explanation": "Autologous costal cartilage reconstruction is typically timed to when the chest wall has grown enough to provide adequate cartilage for framework carving, generally around age 8-10, balancing sufficient donor material against the psychosocial benefit of earlier reconstruction.",
"why_wrong": ["Reconstruction that early would precede adequate costal cartilage development in most children.","Correct.","Cartilage graft adequacy is directly related to chest wall/rib growth, so timing is very much tied to patient growth.","Waiting until adulthood is not standard when adequate cartilage is available earlier and psychosocial timing favors earlier reconstruction."],
"board_pearl": "Autologous microtia reconstruction timing balances two competing goals: enough costal cartilage to build a durable, detailed framework, and reconstructing early enough for psychosocial benefit during childhood.",
"curveball": "The family asks about a synthetic (porous polyethylene) framework instead. What is the key trade-off compared with autologous cartilage?",
"tier": "Curated board-style", "mode": "Vignette"
},
{
"id": "v132_fprs_10", "domain": "Facial Plastics / Trauma", "topic": "Local Flap Reconstruction",
"stem": "A 1.5 cm full-thickness cheek defect after Mohs excision has adequate surrounding skin laxity. Which principle should guide flap selection over a skin graft for this defect?",
"choices": ["Skin grafts always provide superior color and texture match on the cheek", "Local flaps generally provide better color/texture match and contour for cheek defects when adjacent tissue laxity allows tension-free closure", "Local flaps are contraindicated on the cheek due to facial nerve risk in all cases", "Defect size is irrelevant to the flap-versus-graft decision"],
"answer": 1,
"explanation": "The reconstructive ladder favors using adjacent, similar tissue (local flaps) when laxity allows, since this typically provides superior color, texture, and contour match compared with a skin graft, which often looks patched and can contract unpredictably.",
"why_wrong": ["Skin grafts are more prone to color/texture mismatch and contraction than well-designed local tissue, particularly on the cheek.","Correct.","Local cheek flaps are commonly and safely performed with attention to facial nerve branch anatomy, not categorically contraindicated.","Defect size, location, and adjacent tissue laxity are central to the flap-versus-graft decision, not irrelevant."],
"board_pearl": "The reconstructive ladder is a starting framework, not a strict hierarchy - for facial costhetic subunits like the cheek, a well-designed local flap often outperforms a skin graft even when a graft would technically 'work.'",
"curveball": "The defect actually extends close to the marginal mandibular nerve's expected course. How does that change flap design and dissection plane?",
"tier": "Curated board-style", "mode": "Vignette"
},
{
"id": "v132_fprs_11", "domain": "Facial Plastics / Trauma", "topic": "Skin Graft Selection",
"stem": "A large scalp defect after tumor resection, with exposed periosteum but no exposed bone, requires temporary or definitive coverage. Which graft type is generally preferred, and why?",
"choices": ["Full-thickness skin graft, for maximal durability", "Split-thickness skin graft, because it has a higher take rate on a well-vascularized bed and larger donor-site availability for a large defect", "No graft is needed since periosteum will epithelialize spontaneously within days", "Composite graft, to restore hair-bearing tissue"],
"answer": 1,
"explanation": "Split-thickness skin grafts generally have a higher take rate than full-thickness grafts because they require less vascular ingrowth to survive, and can be harvested in larger quantities, making them well suited to large defects with a vascularized bed such as intact periosteum.",
"why_wrong": ["Full-thickness grafts have lower take rates on marginal beds and are typically reserved for smaller, cosmetically sensitive areas rather than large scalp defects.","Correct.","Spontaneous epithelialization over bare periosteum without a dermal element is far too slow and unreliable for a large defect; grafting is appropriate.","A composite graft is used for small, structurally complex defects (e.g., alar rim), not to resurface a large scalp wound, and hair restoration is a separate later consideration."],
"board_pearl": "Graft take depends on the vascularity of the recipient bed and the metabolic demand of the graft - thinner grafts survive on more marginal beds, which is why exposed bone without periosteum usually needs a flap, not a graft.",
"curveball": "On closer inspection, a small area of bare calvarial bone without periosteum is also present within the defect. Does a skin graft remain adequate for that specific area?",
"tier": "Curated board-style", "mode": "Vignette"
},
{
"id": "v132_fprs_12", "domain": "Facial Plastics / Trauma", "topic": "Functional Septorhinoplasty",
"stem": "A patient with nasal airway obstruction has a caudal septal deviation and collapse of the internal nasal valve on inspiration (positive modified Cottle test). Which combination of techniques most directly addresses both findings?",
"choices": ["Turbinate reduction alone", "Septoplasty to correct caudal deviation plus spreader grafts or a similar technique to support the internal nasal valve", "Rhinoplasty tip work only, without addressing the septum or valve", "Topical decongestant therapy alone is definitive treatment"],
"answer": 1,
"explanation": "Caudal septal deviation requires septoplasty (sometimes extended/caudal septal techniques) for correction, while internal nasal valve collapse - confirmed by symptomatic improvement with lateral wall support on modified Cottle testing - is classically addressed with spreader grafts or similar structural support to widen and stabilize the valve angle.",
"why_wrong": ["Turbinate reduction addresses a different (mucosal/nonstructural) contributor to obstruction and does not fix caudal septal deviation or valve collapse.","Correct.","Isolated tip work does not address either the septal deviation or the internal valve, which are both structural contributors described here.","Topical decongestants provide temporary mucosal decongestion, not correction of the underlying structural collapse and deviation."],
"board_pearl": "A positive modified Cottle test (symptomatic improvement with gentle lateral cheek traction opening the internal valve) supports structural valve collapse as a real contributor to obstruction, not just septal deviation - both may need to be addressed for a functional result.",
"curveball": "After surgery, the patient still reports obstruction on the same side, and exam shows a normal-appearing internal valve but new external valve collapse with deep inspiration. What structural cause should you now consider?",
"tier": "Curated board-style", "mode": "Vignette"
},
]
