"""ENT Mastery v46.4 -- Learning-ladder gapfill: Facial Plastics / Trauma.

Adds foundation/application/senior_decision Clinical Challenge vignettes for
the 2 Facial Plastics / Trauma topics flagged by audit_domain_ladder_inventory_v217.py
as having no deliberately-reviewed ladder row (recently-added topics that never
got this pass). Grounded in each topic's existing Deep Curriculum content --
no new clinical facts or numbers introduced beyond what that content already
states.
"""
from copy import deepcopy

DOMAIN = "Facial Plastics / Trauma"

NEW_QUESTIONS = [
    # ---------------------------------------------------------------
    # Laryngeal Fracture / External Laryngeal Trauma
    # ---------------------------------------------------------------
    {
        "id": "v464_fp_laryngealfx_fnd",
        "domain": DOMAIN,
        "topic": "Laryngeal Fracture / External Laryngeal Trauma",
        "stem": "A young man arrests his motorcycle into a fixed clothesline at speed. He arrives with neck tenderness, subcutaneous emphysema over the anterior neck, a flattened thyroid prominence, and mild dysphonia, but he is speaking in full sentences without stridor. What is the most important next step?",
        "choices": [
            "Reassure the patient and discharge home since he can speak normally",
            "Obtain CT neck with contrast before any airway evaluation, since he is not in obvious distress",
            "Assess airway/breathing/circulation with cervical-spine precautions and involve senior ENT/anesthesia/trauma support immediately, recognizing that a calm voice does not exclude serious injury",
            "Perform blind nasotracheal intubation at the bedside to secure the airway proactively"
        ],
        "answer": 2,
        "explanation": "Anterior-neck blunt trauma with tenderness, subcutaneous emphysema, and a flattened thyroid prominence are red flags for laryngeal fracture. Symptom severity does not reliably grade structural injury -- a patient who is speaking calmly can still develop airway-threatening edema over hours. The correct next step is coordinated ABCs with cervical-spine precautions and senior ENT/anesthesia/trauma involvement, not reassurance, not imaging before airway assessment, and not blind intubation.",
        "why_wrong": [
            "Speaking calmly does not reliably reflect the severity of the underlying structural injury; this patient has multiple red-flag findings and needs urgent evaluation, not discharge.",
            "Airway/breathing assessment with senior support must occur before or alongside imaging in a patient with signs concerning for laryngeal injury; imaging should not be pursued at the expense of airway assessment.",
            "Correct.",
            "Blind attempts at intubation across a suspected laryngeal injury can create a false passage or convert a partial injury into complete separation; this is specifically to be avoided."
        ],
        "board_pearl": "Do not let a calm voice provide false reassurance after anterior neck trauma -- neck tenderness, emphysema, and a flattened thyroid prominence are the red flags that drive urgent multidisciplinary evaluation, and symptom severity does not reliably grade structural injury.",
        "curveball": "Which additional injuries should be assessed for as part of the same multidisciplinary trauma evaluation?",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-facial-plastics-trauma-laryngeal-fracture-external-laryngeal-trauma",
        "learning_stage": "foundation",
        "ladder_reviewed": True,
        "focus": "boards",
        "curveball_answer": "Along with airway assessment, the trauma team should evaluate for cervical spine injury, carotid/jugular vascular trauma, and pharyngoesophageal perforation as part of coordinated multidisciplinary trauma care."
    },
    {
        "id": "v464_fp_laryngealfx_app",
        "domain": DOMAIN,
        "topic": "Laryngeal Fracture / External Laryngeal Trauma",
        "stem": "After anterior neck trauma, flexible nasolaryngoscopy in a stable, cooperative patient shows mild mucosal edema and a small hematoma without exposed cartilage. The exam is otherwise reassuring. Which statement correctly guides the next step?",
        "choices": [
            "A reassuring scope exam alone means the workup is complete and no further imaging is needed",
            "CT neck with thin cuts and multiplanar laryngeal reconstruction should still be obtained once safe, because a seemingly mild scope exam can still miss a framework fracture",
            "The patient should be sent home with voice rest instructions and no monitoring",
            "Because the exam looks mild, direct laryngoscopy and bronchoscopy should be scheduled electively in several weeks"
        ],
        "answer": 1,
        "explanation": "A seemingly mild flexible scope exam can still miss an underlying framework fracture. CT neck with thin cuts and multiplanar laryngeal reconstruction is used to define displaced or nondisplaced thyroid/cricoid fractures once it is safe to image, and grading (Schaefer-Fuhrman) requires both endoscopy and CT findings -- not radiology or endoscopy alone.",
        "why_wrong": [
            "Endoscopy alone is insufficient; framework injury can be present despite a reassuring mucosal exam, so imaging is still indicated once safe.",
            "Correct.",
            "Even patients treated conservatively (Group I / selected Group II) require monitored admission with serial airway and endoscopic checks, typically for at least 24 hours, rather than immediate discharge.",
            "Direct laryngoscopy/bronchoscopy is used after airway control to delineate the full extent of injury for repair planning in patients who need operative evaluation; an asymptomatic, reassuring exam does not by itself mean this must be deferred electively for weeks, and decisions about further endoscopic evaluation should not simply be pushed out because the initial exam looked mild."
        ],
        "board_pearl": "Grade laryngeal trauma using BOTH endoscopy and CT findings together -- a mild-appearing mucosal exam does not rule out an underlying framework fracture.",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-facial-plastics-trauma-laryngeal-fracture-external-laryngeal-trauma",
        "learning_stage": "application",
        "ladder_reviewed": True,
        "focus": "OR_prep",
        "curveball": "If CT subsequently shows a nondisplaced thyroid cartilage fracture with intact mucosa and no airway compromise, how would this patient most likely be managed?",
        "curveball_answer": "This would generally correspond to Schaefer-Fuhrman Group I or selected stable Group II injury (intact mucosa, no significant displacement or airway compromise), managed with monitored admission, head elevation, humidification, voice rest, analgesia, a swallowing assessment, and serial endoscopy rather than immediate operative repair."
    },
    {
        "id": "v464_fp_laryngealfx_snr",
        "domain": DOMAIN,
        "topic": "Laryngeal Fracture / External Laryngeal Trauma",
        "stem": "A patient with a clearly unstable laryngeal framework disruption after blunt neck trauma has stridor and worsening dyspnea in the trauma bay. Which airway strategy is most appropriate?",
        "choices": [
            "Routine rapid-sequence intubation using standard blind technique to save time",
            "Wait for CT neck to fully characterize the fracture before making any airway decision",
            "A controlled, coordinated airway approach favoring an awake tracheostomy below the injury (or controlled fiberoptic intubation with immediate surgical backup) chosen by the senior team based on anatomy, stability, and expertise",
            "Immediate operative cartilage reduction and fixation before any airway is secured"
        ],
        "answer": 2,
        "explanation": "With a clearly unstable framework or major disruption, a controlled airway approach is required, and routine blind rapid-sequence intubation should be avoided because it can create a false passage or complete separation. The choice among controlled fiberoptic intubation with immediate surgical backup versus awake/local tracheostomy depends on anatomy, stability, expertise, and associated injuries; with clearly unstable framework or major separation, a surgical airway below the injury is favored when feasible. This decision should not be delayed for imaging, and operative repair follows airway security, not the reverse.",
        "why_wrong": [
            "Blind rapid-sequence intubation across a suspected severe disruption is explicitly discouraged because it risks creating a false passage or completing a separation.",
            "An unstable or rapidly deteriorating airway must be secured before imaging, not after a CT is obtained.",
            "Correct.",
            "The airway must be secured first; operative cartilage repair is planned and performed after the airway (often below the level of disruption) is controlled."
        ],
        "board_pearl": "For a clearly unstable laryngeal framework, expert controlled airway management -- often a surgical airway below the disruption -- comes before imaging and before definitive cartilage repair; complete laryngotracheal separation is an airway catastrophe requiring identification of the distal trachea for secure ventilation first.",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-facial-plastics-trauma-laryngeal-fracture-external-laryngeal-trauma",
        "learning_stage": "senior_decision",
        "ladder_reviewed": True,
        "focus": "overnight_call",
        "curveball": "Once the airway is secure and the patient stabilizes, what is the appropriate timing philosophy for operative repair of a displaced fracture, and what common teaching error should be avoided?",
        "curveball_answer": "Expeditious repair is preferred when clinically feasible: exploration is recommended within about 24-48 hours in one major reference and ideally within 2-3 days after stabilization in another, after immediately life-threatening injuries are addressed first. A commonly misread statistic -- a published mean repair time of 5.6 days (range 3-10) -- describes real-world practice, not a required or optimal delay, and should not be taught as the target timing."
    },
    # ---------------------------------------------------------------
    # Blepharoplasty / Eyelid Malposition (Ptosis, Ectropion, Entropion)
    # ---------------------------------------------------------------
    {
        "id": "v464_fp_bleph_fnd",
        "domain": DOMAIN,
        "topic": "Blepharoplasty / Eyelid Malposition (Ptosis, Ectropion, Entropion)",
        "stem": "An older patient complains of heavy, sagging upper eyelids that intermittently obstruct the superior visual field, worse by end of day. Examination shows redundant upper-lid skin overlying the lash line, but the lid margin position and levator function appear normal once the skin is lifted. Which condition does this best represent?",
        "choices": [
            "True blepharoptosis from levator dehiscence",
            "Dermatochalasis (skin excess) rather than true ptosis",
            "Entropion",
            "Ectropion"
        ],
        "answer": 1,
        "explanation": "'Droopy eyelid' is not one diagnosis. Dermatochalasis is skin excess that can mechanically obstruct the visual field, and it must be separated from true ptosis (a levator/aponeurotic problem), outward lower-lid ectropion, and inward entropion -- each is a different defect requiring a different repair.",
        "why_wrong": [
            "True ptosis reflects levator/aponeurotic dysfunction with an abnormal margin position independent of skin excess; here the margin position is normal once the excess skin is accounted for.",
            "Correct.",
            "Entropion is inward turning of the lid margin, not simply excess upper-lid skin.",
            "Ectropion is outward turning of the lid margin (classically lower lid), not upper-lid skin excess."
        ],
        "board_pearl": "Separate dermatochalasis from true ptosis, ectropion, and entropion before planning any surgery -- identify the failing layer and vector rather than treating every 'droopy eyelid' the same way.",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-facial-plastics-trauma-blepharoplasty-eyelid-malposition-ptosis-ectropion-entropion",
        "learning_stage": "foundation",
        "ladder_reviewed": True,
        "focus": "boards",
        "curveball": "What measurements should be obtained before assuming this is purely dermatochalasis and proceeding straight to skin excision?",
        "curveball_answer": "Margin-reflex distance and levator function should be measured, along with lower-lid distraction/snap-back testing, pupil and motility exam, and assessment of the ocular surface and dry-eye symptoms; formal visual fields should be obtained when documenting functional upper-lid obstruction."
    },
    {
        "id": "v464_fp_bleph_app",
        "domain": DOMAIN,
        "topic": "Blepharoplasty / Eyelid Malposition (Ptosis, Ectropion, Entropion)",
        "stem": "A patient presents with new-onset unilateral upper-eyelid droop. On exam the margin-reflex distance is reduced and levator function is diminished on that side, without any prior eyelid surgery or obvious age-related skin change. Which principle should guide the evaluation before this is treated as ordinary age-related ptosis?",
        "choices": [
            "Proceed directly to standard aponeurotic ptosis repair without further workup, since droopy eyelid is always aging-related",
            "Recognize that neurogenic ptosis must not be mistaken for aging-related aponeurotic ptosis, and evaluate pupils and motility as part of localizing the cause",
            "Assume this is dermatochalasis and plan skin-only blepharoplasty",
            "Treat empirically with lubricating drops only, since structural disease rarely needs correction"
        ],
        "answer": 1,
        "explanation": "Skin excess, levator/aponeurotic dysfunction, horizontal laxity, and anterior/posterior lamellar imbalance are different defects requiring different repairs, and neurogenic ptosis specifically must not be mistaken for aging. Pupils and motility should be examined as part of localizing the responsible layer before committing to a particular structural repair.",
        "why_wrong": [
            "Jumping to a standard aponeurotic repair without excluding a neurogenic cause risks missing a different (and potentially more significant) underlying process.",
            "Correct.",
            "Reduced margin-reflex distance and levator function indicate a true ptosis problem, not simple skin excess, so skin-only blepharoplasty is not the appropriate plan here.",
            "Lubrication/exposure protection is described as a bridge for mild malposition, not a substitute for correcting structural disease once identified; it is not the primary answer when a new, asymmetric, levator-function-abnormal ptosis needs to be characterized first."
        ],
        "board_pearl": "New or asymmetric ptosis with abnormal levator function is not automatically aging-related -- pupil and motility exam help exclude a neurogenic cause before structural repair is planned.",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-facial-plastics-trauma-blepharoplasty-eyelid-malposition-ptosis-ectropion-entropion",
        "learning_stage": "application",
        "ladder_reviewed": True,
        "focus": "boards",
        "curveball": "If the workup instead confirms straightforward aponeurotic ptosis with normal pupils and motility, what does the operative approach specifically target?",
        "curveball_answer": "Ptosis repair targets the levator/Müller mechanisms specifically, as distinct from blepharoplasty (which conservatively removes or repositions tissue) or lateral tarsal strip/entropion repair (which address lower-lid laxity or retractor/override problems)."
    },
    {
        "id": "v464_fp_bleph_snr",
        "domain": DOMAIN,
        "topic": "Blepharoplasty / Eyelid Malposition (Ptosis, Ectropion, Entropion)",
        "stem": "A patient has chronic lower-lid horizontal laxity with the lid margin turning outward, tearing, and mild ocular surface irritation. A positive lower-lid distraction/snap-back test confirms significant laxity, and the ocular surface is otherwise healthy. Which operative decision is most appropriate?",
        "choices": [
            "Perform a lateral tarsal strip procedure to address the horizontal laxity causing the ectropion",
            "Perform entropion repair targeting the retractors and lid override",
            "Perform standard upper-lid blepharoplasty since all eyelid malposition is corrected the same way",
            "Rely on botulinum toxin as the definitive, permanent correction of the lid malposition"
        ],
        "answer": 0,
        "explanation": "Lax ectropion (outward turning with confirmed horizontal laxity on distraction/snap-back testing) is treated with a lateral tarsal strip procedure targeting the horizontal laxity. This is distinct from entropion repair, which corrects retractors and overriding for inward-turning lids, and from blepharoplasty, which addresses skin excess/upper-lid tissue rather than lower-lid horizontal laxity.",
        "why_wrong": [
            "Correct.",
            "Entropion repair addresses inward turning and retractor/override problems -- the opposite mechanism from this patient's outward-turning, lax ectropion.",
            "Blepharoplasty conservatively removes or repositions upper-lid tissue; it does not correct lower-lid horizontal laxity causing ectropion, since different defects require different repairs.",
            "Botulinum toxin has selected temporary uses only; structural disease such as lax ectropion is corrected anatomically, not with a temporizing agent as the definitive treatment."
        ],
        "board_pearl": "Match the repair to the mechanism: horizontal lid laxity with ectropion calls for a lateral tarsal strip, while entropion repair corrects retractors and lid override -- treating structural malposition anatomically rather than with temporizing measures.",
        "tier": "Curated learning ladder",
        "mode": "Vignette",
        "concept_id": "v6-facial-plastics-trauma-blepharoplasty-eyelid-malposition-ptosis-ectropion-entropion",
        "learning_stage": "senior_decision",
        "ladder_reviewed": True,
        "focus": "OR_prep",
        "curveball": "During any of these eyelid procedures, what complications must specifically be prevented, and why does surgical candidacy require assessing the ocular surface and lower-lid support beforehand?",
        "curveball_answer": "Overresection, lagophthalmos, ectropion, and retrobulbar hematoma must be prevented during these procedures. Assessing the ocular surface (dry eye, exposure symptoms) and lower-lid support before removing tissue matters because inadequate assessment can lead to iatrogenic exposure, lagophthalmos, or ectropion after otherwise well-intentioned tissue removal or repositioning."
    },
]


def apply_deep_curriculum_ladder_facial_plastics_v464(data_module, app_module=None):
    existing = getattr(data_module, "CLINICAL_CHALLENGES_V119", None)
    if not isinstance(existing, list):
        raise RuntimeError("v46.4: CLINICAL_CHALLENGES_V119 unavailable")
    existing_ids = {q.get("id") for q in existing}
    added = 0
    cases = list(existing)
    for q in NEW_QUESTIONS:
        if q["id"] in existing_ids:
            raise RuntimeError(f"v46.4: duplicate id {q['id']!r}")
        cases.append(q)
        added += 1
    data_module.CLINICAL_CHALLENGES_V119 = cases
    if app_module is not None:
        app_module.CLINICAL_CHALLENGES_V119 = data_module.CLINICAL_CHALLENGES_V119
    return {"questions_added": added}
