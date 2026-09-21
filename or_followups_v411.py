"""ENT Mastery v41.1 -- procedure-specific OR-prep attending follow-ups.

Replaces the remaining copied three-pair templates identified in the 2026-09-20
review. Each replacement is grounded in the card's existing indications, danger,
and landmarks fields.
"""
from copy import deepcopy


FOLLOWUPS = {
    "stapedotomy": ("How do you avoid facial nerve injury during stapedotomy, and what do you do if the tympanic facial nerve is dehiscent and overhangs the oval window?", "Identify the tympanic facial nerve landmark above the oval window before working near the footplate. If it is dehiscent and low-lying, work carefully under it or convert to a more conservative approach rather than risk transecting or thermally injuring an exposed nerve."),
    "submandibular-gland": ("Which nerve is at greatest risk while raising the cervical flap over the gland, and how do you protect it?", "The marginal mandibular branch runs superficial to the submandibular fascia near the mandibular border. Stay deep to the platysma/fascia and retract inferiorly (or ligate and retract the facial vein) to keep dissection below the nerve's plane."),
    "sialendoscopy": ("What size stone is reliably retrievable endoscopically, and what do you do if the basket becomes impacted on a larger stone?", "Stones roughly ≤4 mm are usually retrievable endoscopically. If a basket impacts on a larger stone, do not force traction -- convert to a combined transoral/open approach or lithotripsy rather than risk duct avulsion or lingual nerve injury."),
    "DLB": ("Why is dental/lip protection specifically emphasized before suspension laryngoscopy, and what should you do if you feel excessive resistance seating the scope?", "Suspension transmits significant leverage through the upper incisors and lip; pad and protect them before suspending. If you feel excessive resistance, stop and reassess positioning/exposure rather than forcing the scope, which risks dental avulsion or lip laceration."),
    "airway-dilation": ("Why is posterior wall injury a specific concern during dilation of subglottic stenosis, and how do you avoid it?", "The posterior cricoid/subglottis is thin and sits directly anterior to the esophagus. Dilate under direct visualization with controlled, incremental pressure and stop if mucosal tearing extends beyond the anticipated fracture line, to avoid full-thickness posterior injury or perforation."),
    "medialization": ("How do you judge adequate medialization intraoperatively in an awake patient, and what suggests you have overmedialized?", "Have the patient phonate during implant sizing/placement and listen for voice strength and quality. Stridor, airway compromise, or a markedly strained/pressed voice suggests overmedialization, and the implant should be downsized or repositioned."),
    "zenker": ("What pouch-size threshold favors an endoscopic approach over open Zenker repair, and what is the danger if the septotomy is extended too far?", "Pouches of roughly ≥2-3 cm are generally favorable for endoscopic stapling/laser septotomy. Extending the septotomy beyond the confirmed common wall into healthy esophagus risks perforation and mediastinitis."),
    "adenoidectomy": ("Why is conservative tissue removal near the torus tubarius and Passavant ridge important, and what results from over-resection there?", "Excessive resection near the torus tubarius risks Eustachian tube injury and effusion; violating the velopharyngeal sphincter/Passavant ridge risks velopharyngeal insufficiency with hypernasal speech and nasal regurgitation, especially in a patient with an occult submucous cleft."),
    "thyroglossal": ("Why does the Sistrunk procedure remove the central hyoid segment, and which nerve is at risk during dissection toward the tongue base?", "Removing the central hyoid and a core of tissue up to the foramen cecum addresses the full embryologic tract, which is why Sistrunk lowers recurrence versus simple cyst excision; the hypoglossal nerve runs nearby as dissection continues toward the tongue base and should be identified and protected."),
    "branchial": ("Before excising a presumed branchial cleft cyst in an adult, what must you rule out first, and why does that change the workup?", "A cystic metastatic neck node -- particularly from HPV-associated oropharyngeal carcinoma -- can mimic a congenital branchial cleft cyst in an adult. Obtain FNA and appropriate imaging before excision so an oncologic diagnosis is not delayed by presuming a benign congenital lesion."),
    "orbital-floor": ("What exam finding makes a pediatric orbital floor fracture a same-day surgical emergency regardless of how the imaging looks?", "A 'trapdoor' fracture with the oculocardiac reflex -- bradycardia, nausea/vomiting, and restricted gaze from entrapped tissue -- is a surgical emergency independent of fracture size on CT, since delay risks ischemic injury to the entrapped muscle."),
    "mandible-orif": ("What must you confirm before leaving the OR regardless of fixation technique, and why?", "Confirm the patient's preinjury occlusion has been restored, using arch bars/MMF intraoperatively to check the bite, before finalizing fixation -- restoring an idealized 'normal' occlusion that is not the patient's own baseline is a common, avoidable error."),
    "zmc-orif": ("Why is CT obtained before choosing a fixation approach for a ZMC fracture, and what functional finding would push you toward operating rather than observing?", "CT defines displacement/comminution and which buttresses need fixation, guiding whether one-, two-, or three-point fixation is sufficient. Trismus from coronoid impingement or persistent diplopia from globe/muscle malposition supports operative repair over observation."),
    "microflap": ("What is the single most important microsurgical principle for preserving voice when removing a benign vocal-fold lesion, and why?", "Stay superficial to the vocal ligament and preserve the superficial lamina propria whenever possible -- violating the deeper layers scars the vibratory mucosal wave and can cause permanent dysphonia even after the lesion is fully removed."),
    "rrp-debridement": ("What is the single most important safety step before activating the laser near the airway, and why does anterior-commissure disease change the approach?", "Confirm a laser-safe airway technique (protected ETT or apneic/jet ventilation) with low FiO2 before firing the laser. Bilateral anterior-commissure disease treated in the same setting risks anterior glottic web formation, so bilateral anterior lesions are often staged."),
    "reconstructive-palate": ("What is the main long-term risk of overly aggressive palatal tissue removal for OSA, and how do you mitigate it?", "Removing too much palatal/pharyngeal tissue risks velopharyngeal insufficiency with nasal regurgitation and hypernasal speech; preserve adequate palatal length and sphincter function and counsel patients preoperatively about this tradeoff against OSA improvement."),
    "lingual-tonsillectomy": ("Which vessel is the feared source of delayed hemorrhage after tongue-base reduction, and what does that mean for the postoperative airway plan?", "The lingual artery runs near the tongue-base operative field and can cause major delayed bleeding; plan postoperative airway monitoring (often overnight observation) given the risk of sudden airway compromise from bleeding or edema in this confined space."),
    "hyoid-genioglossus": ("What limits the safe inferior extent of the genioglossus advancement osteotomy, and what happens if that limit is violated?", "The mandibular tooth roots and mental/inferior-alveolar neurovascular bundle limit how large the anterior mandibular window can be; violating that boundary risks tooth devitalization or mental nerve injury and can destabilize the mandible."),
    "closed-nasal-reduction": ("What must you exclude before or immediately after closed nasal reduction, and why is missing it dangerous?", "A septal hematoma must be excluded -- if missed, it can cause septal cartilage necrosis (saddle-nose deformity) or abscess. Also examine for signs of an associated NOE injury (telecanthus, widened intercanthal distance), which closed reduction alone will not address."),
    "noe-orif": ("What clinical test distinguishes a true NOE fracture with medial canthal tendon disruption from simple periorbital swelling, and why does it matter?", "The bowstring test -- lateral traction on the lower lid/canthus while palpating the tendon -- reveals canthal tendon mobility from a displaced central fragment. Missing true canthal disruption leads to permanent telecanthus and requires formal transnasal canthopexy, not just fracture reduction."),
    "bilobed-flap": ("Why does the Zitelli modification reduce trapdoor/pincushion deformity compared to the classic bilobed flap, and what arc of rotation does it use?", "The Zitelli modification reduces the total arc of rotation to roughly 45-50 degrees (versus about 90-100 degrees per lobe classically), distributing tension more evenly and reducing standing cutaneous deformities and pincushioning at the tip/ala."),
    "melolabial-flap": ("What is the main risk of designing this flap with too narrow a pedicle, and how do you avoid alar distortion on inset?", "A too-narrow pedicle risks distal flap ischemia by compromising the subdermal plexus. Keep the pedicle base adequately wide, and design/inset the flap to avoid tension that would pull on or blunt the alar rim or melolabial crease."),
    "cervicofacial-flap": ("Why is lower-lid ectropion a specific risk with this flap, and how do you minimize it intraoperatively?", "Wide undermining and tension during rotation/advancement over the cheek can pull the lower eyelid margin inferiorly. Anchor the flap to stable periosteum (e.g., a suspension suture to the lateral orbital rim) to offload tension from the eyelid margin."),
    "skin-graft-face": ("Why is a bolster/tie-over dressing important after a full-thickness skin graft on the face, and what does early graft failure usually indicate?", "A bolster immobilizes the graft against its bed and prevents shear or a hematoma/seroma from separating the graft from its vascular supply. Early graft loss usually reflects an inadequate vascular bed, an underlying hematoma/seroma, or graft movement rather than a suturing problem."),
    "facial-nerve-reanimation": ("Within what window after facial nerve injury is direct repair, cable grafting, or nerve transfer to native musculature favored, and why does a delayed presentation change the plan?", "Motor endplates typically remain viable for roughly 12-24 months after denervation; within that window, direct repair/cable grafting/nerve transfer to preserve native facial muscle is favored. Beyond it, the native muscle can no longer be reliably reinnervated, so free functional muscle transfer is usually needed instead."),
    "free-flap-basics": ("What intraoperative finding after anastomosis suggests venous congestion rather than arterial insufficiency, and how urgently should a compromised flap be managed?", "A congested flap looks dusky/blue with brisk, dark bleeding on pinprick, versus a pale flap with no bleeding in arterial insufficiency. Take a compromised flap back to the OR promptly to explore and revise the anastomosis or relieve a kink/compression -- salvage rates fall sharply the longer take-back is delayed."),
    "pharyngocutaneous-fistula": ("Why is a pharyngocutaneous fistula near the carotid sheath potentially an emergency, and what sign should prompt urgent vascular evaluation?", "Chronic salivary contamination near the carotid sheath -- especially in a previously irradiated or dissected neck -- can erode the vessel wall. A sentinel bleed from the fistula tract or wound should prompt urgent imaging/vascular evaluation for impending carotid blowout rather than being treated as routine wound drainage."),
    "laryngeal-fracture": ("What airway management principle applies to a patient with a suspected laryngeal fracture, and why is blind orotracheal intubation dangerous here?", "Avoid blind orotracheal intubation attempts -- they can convert a partial laryngeal injury into complete laryngotracheal separation. Secure the airway with awake fiberoptic intubation, or with an awake tracheostomy under local anesthesia if the patient is unstable."),
    "esophageal-fb": ("How does management differ for a coin lodged in the esophagus versus a sharp object or button battery, and why?", "A blunt object like a coin can sometimes be observed briefly for spontaneous passage, or removed semi-electively if the patient is stable and asymptomatic. A sharp object or button battery requires urgent/emergent removal because of the much higher risk of perforation or, for a battery, ongoing alkaline mucosal injury."),
}

_TEMPLATE_A = (
    ("What should you know before incision?", "The exact indication, disease extent, relevant imaging/testing, alternatives, anatomy and rescue plan."),
    ("What makes this operation unsafe?", "Losing orientation to the named danger structures or proceeding without a defined functional/oncologic endpoint."),
    ("How do you judge success?", "By disease-specific control plus preservation/restoration of the relevant airway, hearing, voice, swallowing, sleep or oncologic function."),
)
_TEMPLATE_B = (
    ("What determines whether this is the right operation?", "The operation should solve a defined anatomic/physiologic/oncologic problem and offer a better risk-benefit tradeoff than observation, medical therapy, or another procedure."),
    ("What are the danger structures?", "Name the procedure-specific structures above and state how the exposure, dissection plane, or fixation vector keeps them safe."),
    ("What is the rescue plan?", "Know what finding should make you stop, how you would regain airway/hemostasis/anatomic orientation, and which complication requires urgent reoperation or specialty help."),
)
_GENERIC_TEMPLATES = {_TEMPLATE_A, _TEMPLATE_B}


def _normalize_qa(value):
    if not isinstance(value, (list, tuple)):
        return None
    rows = []
    for pair in value:
        if not (isinstance(pair, (list, tuple)) and len(pair) == 2 and all(isinstance(x, str) for x in pair)):
            return None
        rows.append((pair[0].strip(), pair[1].strip()))
    return tuple(rows)


def apply_or_followups_v411(data_module, app_module=None):
    ops_source = getattr(data_module, "OR_PREP_REGISTRY", None)
    if not isinstance(ops_source, dict):
        raise RuntimeError("v41.1: OR_PREP_REGISTRY unavailable")
    ops = deepcopy(ops_source)

    replaced, preserved = [], []
    for slug, pair in FOLLOWUPS.items():
        if slug not in ops:
            preserved.append(slug + ":missing")
            continue
        normalized = _normalize_qa(ops[slug].get("attending_followup"))
        if normalized == (pair,):
            replaced.append(slug)
            continue
        if normalized in _GENERIC_TEMPLATES:
            ops[slug]["attending_followup"] = [list(pair)]
            replaced.append(slug)
        else:
            preserved.append(slug + ":individualized-or-unrecognized")

    data_module.OR_PREP_REGISTRY.clear()
    data_module.OR_PREP_REGISTRY.update(ops)
    if app_module is not None:
        app_module.OR_PREP_REGISTRY = data_module.OR_PREP_REGISTRY
    return {"followups_replaced": replaced, "followups_preserved": preserved}
