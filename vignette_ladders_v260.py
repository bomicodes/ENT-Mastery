"""v26.0 — Facial Plastics / Trauma deliberate ladder pass 4.

Adds five exact canonical nasal-function/rhinoplasty topics with complete
foundation -> application -> senior-decision ladders emphasizing diagnosis,
structural mechanics, operative planning, graft selection, complication rescue,
and preservation of airway function.
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


VIGNETTES_V260 = [
    _q("v260_fpt_obstruction_fnd", "Functional Nasal Obstruction", "foundation",
       "A patient has chronic unilateral nasal obstruction after prior trauma. Anterior rhinoscopy shows septal deviation, but symptoms improve markedly when the lateral cheek is gently pulled laterally. What additional mechanism should be suspected?",
       ["Nasal valve narrowing or dynamic lateral-wall insufficiency in addition to septal obstruction", "Isolated allergic rhinitis because the maneuver is diagnostic for allergy", "A CSF leak", "Normal nasal physiology because septal deviation never causes symptoms"], 0,
       "Functional nasal obstruction is often multilevel. Improvement with lateralization of the cheek or sidewall suggests clinically relevant nasal-valve compromise and should prompt assessment of static narrowing and dynamic collapse rather than attributing all symptoms to the septum.",
       ["Correct. The valve and lateral wall can materially contribute even when septal deviation is obvious.", "Allergic disease may coexist, but mechanical improvement with lateralization points toward a structural component.", "CSF rhinorrhea presents with drainage rather than maneuver-dependent inspiratory obstruction.", "Septal deviation can be symptomatic and may coexist with valve dysfunction."],
       "Do not stop the nasal-airway exam when you find the first abnormality; obstruction is frequently multilevel.",
       "What is the difference between static internal-valve narrowing and dynamic lateral-wall collapse?"),
    _q("v260_fpt_obstruction_app", "Functional Nasal Obstruction", "application",
       "A patient with persistent obstruction after technically adequate septoplasty has inspiratory sidewall collapse, a narrow middle vault, and improvement with modified Cottle support. What is the most appropriate next step?",
       ["Define the specific valve deficit and plan structural lateral-wall/middle-vault support rather than repeating septoplasty alone", "Repeat septoplasty without reassessing the valve", "Perform turbinate ablation until the lateral wall no longer collapses", "Treat only with antibiotics"], 0,
       "Failure after septoplasty should trigger re-localization of the obstructing segment. Dynamic sidewall collapse and middle-vault narrowing require targeted structural treatment; repeating a procedure that corrected a different anatomic level is unlikely to solve the problem.",
       ["Correct. Reconstruct the level that actually fails during inspiration.", "A repeat septoplasty ignores the demonstrated lateral-wall/middle-vault mechanism.", "Inferior-turbinate treatment does not provide structural support to a collapsing lateral wall.", "There is no infectious syndrome in this presentation."],
       "Persistent obstruction after septoplasty is a localization problem before it is a revision-septoplasty problem.",
       "Which examination findings help distinguish internal-valve narrowing from external-valve collapse?", "OR_prep"),
    _q("v260_fpt_obstruction_snr", "Functional Nasal Obstruction", "senior_decision",
       "A patient requests aggressive cosmetic narrowing of an already narrow middle vault but also has borderline internal-valve angles and exertional obstruction. What is the best senior-level counseling and planning principle?",
       ["Prioritize preservation or augmentation of valve cross-sectional area and explain that aesthetic narrowing must not create or worsen functional obstruction", "Promise maximal narrowing because cosmetic goals always supersede airway function", "Remove the upper lateral cartilages to increase definition", "Ignore baseline exertional symptoms because postoperative edema is the only cause of rhinoplasty obstruction"], 0,
       "Rhinoplasty changes airflow as well as appearance. Narrowing an already compromised middle vault can worsen internal-valve resistance; senior planning integrates aesthetic goals with preservation or reconstruction of the structural airway.",
       ["Correct. Aesthetic and functional objectives must be reconciled before surgery.", "Creating iatrogenic obstruction is not an acceptable tradeoff for cosmetic narrowing.", "Upper lateral cartilage destabilization can worsen middle-vault collapse.", "Preexisting symptoms and anatomy predict postoperative functional risk."],
       "A beautiful nose that cannot breathe is a reconstructive failure.",
       "Which grafting strategies can widen or stabilize a narrow middle vault?", "senior_management"),

    _q("v260_fpt_fsr_fnd", "Functional Septorhinoplasty", "foundation",
       "What distinguishes functional septorhinoplasty from an isolated septoplasty in a patient with nasal obstruction?",
       ["It addresses external and internal nasal framework problems—such as valve stenosis, sidewall weakness, or traumatic deformity—in addition to septal pathology", "It is simply a cosmetic rhinoplasty performed without airway goals", "It treats only inferior turbinate hypertrophy", "It never requires cartilage grafting"], 0,
       "Functional septorhinoplasty is chosen when obstruction arises from the nasal framework beyond the septum. It may combine septal correction with reconstruction of the middle vault, lateral wall, tip/caudal septum, or external valve.",
       ["Correct. The operation is defined by the obstructing anatomy, not by a cosmetic-versus-functional label alone.", "Functional surgery has an explicit airway objective.", "Turbinates may contribute but do not define septorhinoplasty.", "Structural grafting is often central when native support is deficient."],
       "The indication for functional septorhinoplasty is a structural airway problem that septoplasty alone cannot reliably correct.",
       "Which traumatic deformities commonly require correction of both septal and external framework components?"),
    _q("v260_fpt_fsr_app", "Functional Septorhinoplasty", "application",
       "During functional septorhinoplasty for a crooked traumatic nose, straightening the dorsal septum would leave the middle vault narrow and unstable after hump reduction. What adjunct best addresses this risk?",
       ["Reconstruct the middle vault with appropriate spreader-type support while restoring a stable straight septal platform", "Resect more upper lateral cartilage to make the dorsum narrower", "Ignore the middle vault because it cannot affect airflow", "Perform only alar-base excision"], 0,
       "Hump reduction or traumatic separation can destabilize the upper lateral cartilage-septal relationship and narrow the internal valve. Spreader grafts or equivalent structural techniques restore dorsal aesthetic lines while maintaining valve geometry.",
       ["Correct. Middle-vault reconstruction is both an aesthetic and functional step.", "Further narrowing or destabilization increases valve compromise.", "The middle vault is a major determinant of the internal nasal valve.", "Alar-base surgery does not correct a narrowed middle vault."],
       "After changing the dorsum, actively ask what happened to the internal valve.",
       "When might autospreader flaps be reasonable, and when is separate grafting preferable?", "OR_prep"),
    _q("v260_fpt_fsr_snr", "Functional Septorhinoplasty", "senior_decision",
       "A revision patient has severe caudal septal deviation, weak tip support, external-valve collapse, and little usable septal cartilage. What is the best operative strategy?",
       ["Plan a structural reconstruction that restores a stable caudal septal/tip foundation and valve support, using an alternative cartilage donor when septum is inadequate", "Perform additional weakening excisions because less cartilage means less obstruction", "Use soft-tissue filler as the sole treatment for collapse", "Avoid discussing rib or auricular cartilage because donor selection is unrelated to structural needs"], 0,
       "Complex revision functional rhinoplasty often requires rebuilding rather than further reduction. A deficient caudal framework and valve need stable structural support; donor choice follows required strength, shape, volume, and prior cartilage availability.",
       ["Correct. Reconstruction should restore the load-bearing framework before fine aesthetic adjustments.", "Further resection can worsen collapse and tip instability.", "Filler cannot replace a missing load-bearing framework in severe valve dysfunction.", "Alternative donor cartilage may be essential when septum is depleted."],
       "Revision obstruction after over-resection is usually a rebuilding problem, not another reduction problem.",
       "What tradeoffs distinguish auricular from costal cartilage in major nasal reconstruction?", "senior_management"),

    _q("v260_fpt_open_fnd", "Open Rhinoplasty Fundamentals", "foundation",
       "What is the principal exposure advantage of an open rhinoplasty approach?",
       ["Direct bilateral visualization of the cartilaginous framework, tip relationships, and dorsal anatomy for precise diagnosis and reconstruction", "It eliminates postoperative edema", "It guarantees no columellar scar", "It avoids all disruption of tip-support mechanisms"], 0,
       "The open approach provides broad symmetric exposure of the lower lateral cartilages, septum, and dorsum, facilitating complex reconstruction and teaching of three-dimensional relationships. Exposure does not eliminate edema, scarring, or the need to preserve support.",
       ["Correct. The major advantage is visualization and access.", "Open approaches can produce substantial edema, especially in the tip.", "A transcolumellar incision creates a scar, usually inconspicuous when designed and closed well.", "Dissection can weaken support if key structures are not deliberately preserved or reconstructed."],
       "Open exposure improves what you can see; it does not absolve you from understanding what your dissection destabilizes.",
       "Which tip-support structures are vulnerable during rhinoplasty dissection?"),
    _q("v260_fpt_open_app", "Open Rhinoplasty Fundamentals", "application",
       "During open rhinoplasty, the surgeon has completed framework exposure and is planning several reductive maneuvers. What principle best prevents postoperative deformity?",
       ["Sequence changes deliberately and reassess dorsal width, tip support, valve function, and symmetry after each structural maneuver", "Perform every planned resection before reassessing the nose", "Judge only the profile view because frontal symmetry is unrelated", "Assume the skin-soft-tissue envelope will compensate for any framework asymmetry"], 0,
       "Rhinoplasty is iterative structural surgery. Each maneuver changes forces and relationships elsewhere; frequent reassessment prevents cumulative over-resection, asymmetry, valve compromise, or loss of tip support.",
       ["Correct. Sequential reassessment converts a list of maneuvers into controlled structural surgery.", "Stacking reductions without reassessment magnifies unintended changes.", "Frontal, basal, oblique, and profile views all reveal different structural problems.", "The envelope often reveals rather than hides framework asymmetry as edema resolves."],
       "Rhinoplasty is not a checklist of resections; every maneuver changes the mechanical system.",
       "Why should the surgeon recheck the airway after dorsal and tip maneuvers?", "OR_prep"),
    _q("v260_fpt_open_snr", "Open Rhinoplasty Fundamentals", "senior_decision",
       "Near the end of open rhinoplasty, the nose looks narrower but inspiration now produces new lateral-wall collapse that was absent preoperatively. What is the best decision?",
       ["Correct the newly created structural deficit before closure rather than accepting iatrogenic valve collapse for a narrower appearance", "Close immediately because airway changes cannot be assessed intraoperatively", "Resect more lateral cartilage to improve airflow", "Pack the nose tightly and assume the collapse will resolve"], 0,
       "An intraoperative functional deficit created by framework modification should be corrected when recognized. Valve compromise can result from excessive narrowing or weakening and may require restoration of support before closure.",
       ["Correct. Recognized iatrogenic instability should be repaired at the index operation when feasible.", "The structural cause is already visible and should not be ignored.", "Additional weakening commonly worsens dynamic collapse.", "Packing cannot substitute for durable lateral-wall support."],
       "The final rhinoplasty check includes breathing mechanics, not just photographs of the contour.",
       "Which structural grafts can rescue internal versus external valve collapse?", "senior_management"),

    _q("v260_fpt_tip_fnd", "Rhinoplasty Tip Mechanics", "foundation",
       "Which concept best describes nasal tip projection and rotation?",
       ["They reflect the interaction of lower lateral cartilage shape/support, septal relationships, ligamentous attachments, and the skin-soft-tissue envelope", "They are determined only by nasal bone length", "They cannot be changed surgically", "They are independent of the caudal septum"], 0,
       "Tip position is a three-dimensional mechanical result of cartilage geometry and support. The medial and lateral crura, domes, caudal septum, attachments, and soft-tissue envelope all influence projection, rotation, and stability.",
       ["Correct. Tip mechanics arise from multiple interacting structural elements.", "Nasal bones primarily define the upper third, not tip position by themselves.", "Tip position is routinely modified surgically.", "The caudal septum is a major anchor and can strongly affect projection and rotation."],
       "Before changing the tip, identify what currently provides projection, rotation, and resistance to deformation.",
       "How can a caudal septal deformity alter both tip position and nasal airflow?"),
    _q("v260_fpt_tip_app", "Rhinoplasty Tip Mechanics", "application",
       "A patient has excessive tip projection and a strong, tension-bearing medial-crural/caudal-septal support complex. What is the safest planning concept?",
       ["Reduce projection in a controlled way while preserving or reconstructing enough support to prevent long-term tip ptosis and valve compromise", "Sever all support mechanisms and allow the tip to settle unpredictably", "Excise the entire lateral crus", "Assume projection reduction cannot affect the external nasal valve"], 0,
       "Deprojection is not simply tissue removal. Weakening support without a replacement plan can create loss of rotation, tip ptosis, asymmetry, or external-valve dysfunction as scar forces mature.",
       ["Correct. Controlled modification preserves predictable mechanics.", "Uncontrolled support release produces unpredictable long-term position.", "Excessive lateral-crural resection can cause alar retraction and valve collapse.", "Tip and alar mechanics directly affect the external nasal valve."],
       "Every tip-reduction maneuver should answer a second question: what will support the tip afterward?",
       "Which maneuvers can deproject the nose while maintaining a stable tip-lip relationship?", "OR_prep"),
    _q("v260_fpt_tip_snr", "Rhinoplasty Tip Mechanics", "senior_decision",
       "A thick-skinned patient seeks a dramatically pinched, highly defined tip. Intraoperatively, further cartilage narrowing would weaken the lateral crura and external valve. What is the best senior decision?",
       ["Set a realistic definition target and preserve structural strength rather than over-resecting cartilage to chase an envelope-limited aesthetic result", "Continue resection until the bare cartilage looks maximally narrow", "Remove both lateral crura because thick skin supplies adequate support", "Ignore the external valve because tip definition is unrelated to breathing"], 0,
       "The skin-soft-tissue envelope limits visible definition. Excessively weakening the framework to obtain an unrealistic intraoperative cartilage shape can produce delayed alar collapse, retraction, and an operated appearance without achieving the desired skin contour.",
       ["Correct. Senior judgment recognizes when tissue biology limits the safely achievable aesthetic endpoint.", "The framework must remain strong enough to resist healing forces and inspiration.", "Skin does not replace the structural role of the lower lateral cartilages.", "Tip and lateral-crural changes can directly compromise external-valve function."],
       "Do not destroy a functional framework to pursue definition the soft-tissue envelope cannot display.",
       "How does skin thickness change counseling, graft visibility, and expected time to final tip definition?", "senior_management"),

    _q("v260_fpt_grafts_fnd", "Rhinoplasty Graft Selection", "foundation",
       "What should primarily determine cartilage donor and graft choice in rhinoplasty?",
       ["The structural job required—strength, shape, volume, curvature, and recipient-site mechanics—balanced against donor availability and morbidity", "A rule that septum is always superior for every graft", "A rule that auricular cartilage is always strong enough for major dorsal reconstruction", "Cosmetic preference without regard to mechanical function"], 0,
       "Graft selection is task-specific. Septal cartilage is straight and convenient but finite; auricular cartilage offers natural curvature but less rigidity; costal cartilage provides abundant strong material but adds donor morbidity and warping considerations.",
       ["Correct. Match material properties to the mechanical problem.", "Septum is often ideal but may be inadequate or unavailable in revision surgery.", "Auricular cartilage is useful for many contours but may lack the rigidity or volume required for major structural rebuilding.", "A graft that looks appropriate but cannot perform its load-bearing task will fail functionally."],
       "Choose the graft by the force it must resist, not by habit.",
       "Which donor is especially useful when a curved alar contour is desired?"),
    _q("v260_fpt_grafts_app", "Rhinoplasty Graft Selection", "application",
       "A patient with external-valve collapse has weak, concave lateral crura but otherwise adequate tip position. Which grafting concept most directly addresses the mechanical problem?",
       ["Reinforce or replace the weak lateral-crural segment with appropriately shaped structural cartilage rather than simply removing more cartilage", "Perform additional cephalic trim until the ala is thinner", "Place a dorsal onlay graft only", "Use septal mucosal cautery to stiffen the ala"], 0,
       "Dynamic external-valve collapse caused by weak or malformed lateral crura requires structural support. Lateral-crural strut, batten, or replacement-type techniques are selected according to the precise deformity and desired vector.",
       ["Correct. The graft should oppose the collapse at its anatomic source.", "Additional resection can further weaken the lateral wall.", "A dorsal onlay does not directly stabilize a collapsing alar sidewall.", "Mucosal cautery is not a structural reconstruction and risks injury."],
       "Place support where the wall fails; do not expect a remote graft to fix a local mechanical deficit.",
       "How do alar batten and lateral-crural strut concepts differ in position and mechanical effect?", "OR_prep"),
    _q("v260_fpt_grafts_snr", "Rhinoplasty Graft Selection", "senior_decision",
       "A multiply operated nose requires major dorsal and caudal reconstruction, but septal cartilage is depleted and auricular cartilage cannot provide adequate straight load-bearing material. Which option is most appropriate?",
       ["Use costal cartilage when the required volume and rigidity justify it, with techniques that account for warping and donor-site morbidity", "Continue harvesting scarred residual septum regardless of quantity", "Use only injectable filler for load-bearing caudal reconstruction", "Abandon structural support and rely on the skin envelope"], 0,
       "Costal cartilage is valuable for major revision reconstruction because it provides abundant strong material. Its benefits must be balanced against donor morbidity, calcification, and warping; careful carving and construct design reduce these risks.",
       ["Correct. Donor escalation should follow the mechanical requirements of the reconstruction.", "Inadequate residual septum cannot supply the necessary structural volume.", "Filler cannot substitute for a stable load-bearing caudal framework.", "Soft tissue cannot reliably maintain major dorsal or caudal structure without support."],
       "In revision rhinoplasty, donor choice is part of the reconstructive plan—not an afterthought after septum runs out.",
       "What strategies are used to reduce clinically significant costal-cartilage warping?", "senior_management"),
]


def apply_learning_ladders_v260(challenges, concept_id_fn):
    """Append only missing v26.0 cases and attach exact canonical concept IDs."""
    existing = {str(q.get("id")) for q in challenges}
    added = 0
    for source in VIGNETTES_V260:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["concept_id"] = concept_id_fn(DOMAIN, q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1
    return added
