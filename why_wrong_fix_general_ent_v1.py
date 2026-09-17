"""
why_wrong_fix_general_ent_v1.py

Replaces the generic/duplicate `why_wrong` text for the 25 General ENT /
Emergencies items flagged by audit_question_quality.py (GENERIC_WHY_WRONG).
Each wrong choice now gets its own specific clinical reasoning instead of a
shared, copy-pasted sentence. The correct choice's own slot is left as
"Correct." to match the existing schema.

Usage
-----
Wire this into runtime_entry_pasha.py the same way other repair patches are
wired in (after all other curriculum/vignette assembly), e.g.:

    from why_wrong_fix_general_ent_v1 import apply_why_wrong_fix_general_ent_v1
    WHY_WRONG_FIX_GENERAL_ENT_V1 = apply_why_wrong_fix_general_ent_v1(runtime_entry.data)

Or run standalone against a loaded `data` module for a dry check:

    import data
    from why_wrong_fix_general_ent_v1 import apply_why_wrong_fix_general_ent_v1
    apply_why_wrong_fix_general_ent_v1(data)
"""

# Keyed by question id. Each list has one entry per choice index, in the same
# order as `choices`. The correct choice's own entry is "Correct." and is not
# displayed as a "why wrong" explanation by the existing render logic, but is
# kept present so list length always matches len(choices).

WHY_WRONG_FIXES = {
    "v140_gen_01": [
        "Bleeding has stopped only because a clot has formed over the vessel; secondary "
        "tonsillar bleeds are notoriously prone to recurring suddenly and severely once "
        "that clot dislodges, so early discharge risks a life-threatening rebleed outside "
        "the hospital.",
        "Disturbing or removing the clot at the bedside can dislodge it and precipitate "
        "immediate, uncontrolled hemorrhage in a fossa without direct pressure or suction "
        "control; clot manipulation should happen in a monitored setting with airway and "
        "OR backup ready.",
        "Correct.",
        "Oral intake and unmonitored observation ignore the real risk of a repeat bleed "
        "and would delay recognition and resuscitation if hemorrhage recurs; a convincing "
        "sentinel bleed warrants inpatient monitoring, not routine reassurance.",
    ],
    "v140_gen_02": [
        "Correct.",
        "In an immature (2-day-old) tract, forceful blind reinsertion attempts can create "
        "a false passage in the pretracheal soft tissue, converting a recoverable situation "
        "into mediastinal injury or complete loss of the airway.",
        "Occluding the mouth and nose assumes the natural airway is the route to ventilate, "
        "but many tracheostomy-dependent patients have no natural airway at all, or this "
        "wastes critical time without addressing the actual obstruction at the stoma.",
        "A desaturating patient cannot wait; the tract does not mature acutely, and delaying "
        "action while hypoxia progresses causes harm.",
    ],
    "v140_gen_03": [
        "Correct.",
        "Stridor is a late sign of near-complete obstruction; waiting for it means "
        "intervening only once safe intubation options have already narrowed, so airway "
        "teams should be involved before that point, not after.",
        "ACE-inhibitor angioedema is bradykinin-mediated, not infectious, so antibiotics "
        "(and antihistamines/epinephrine, for that matter) do not reliably address the "
        "underlying swelling.",
        "Repeated oral exams add nothing therapeutic and can provoke gagging or trauma "
        "that worsens airway edema and distress; the priority is planning safe airway "
        "access, not repeated inspection.",
    ],
    "v140_gen_04": [
        "A negative CT for a drainable collection does not exclude Ludwig angina, a diffuse "
        "cellulitis that can obstruct the airway through tissue swelling and tongue "
        "elevation alone, without ever forming a discrete abscess.",
        "Blind needling of a woody, edematous floor of mouth risks injuring the lingual "
        "artery, nerve, or tongue musculature and rarely yields useful drainage when the "
        "process is a diffuse cellulitis rather than a loculated collection.",
        "Correct.",
        "Ludwig angina classically does not fluctuate because it is a spreading cellulitis, "
        "not an abscess; waiting for a sign that may never appear delays airway-protective "
        "management while risk continues to build.",
    ],
    "v140_gen_05": [
        "Correct.",
        "Mucositis causes diffuse mucosal oozing, not a discrete pulsatile bleed in a "
        "patient whose imaging shows tumor encasing an exposed, irregular carotid segment; "
        "mislabeling this as mucositis would miss a potentially fatal sentinel event.",
        "Calling pulsatile oral bleeding in this context \"routine\" epistaxis ignores the "
        "vascular imaging findings and the well-described phenomenon of self-limited "
        "sentinel bleeds preceding carotid rupture.",
        "Dental sources do not explain pulsatile bleeding correlating with an eroded "
        "carotid segment on CTA; anchoring on a dental cause would delay the urgent "
        "vascular workup this presentation demands.",
    ],
    "v140_gen_06": [
        "Correct.",
        "Sending an acutely obstructed patient to CT abandons airway control during "
        "transport and imaging, when the priority is restoring ventilation immediately, "
        "not further diagnostic delay.",
        "Extubating a patient with a foreign body now obstructing the glottis removes the "
        "operator's only means of controlling and clearing the airway, worsening rather "
        "than resolving the emergency.",
        "An object impacted at the glottis causing complete obstruction will not pass "
        "spontaneously in a useful timeframe; waiting risks hypoxic injury or arrest.",
    ],
    "v140_gen_07": [
        "Correct.",
        "Button batteries generate current and hydroxide ions against adjacent mucosa, "
        "causing liquefactive necrosis that can perforate the esophagus within hours; "
        "overnight observation allows exactly the delay that turns a straightforward "
        "retrieval into a catastrophic injury.",
        "Esophageal button batteries can cause severe tissue injury before any symptoms "
        "develop, so waiting for symptoms as a trigger forfeits the narrow window in which "
        "removal prevents perforation or fistula.",
        "Blindly advancing a battery without endoscopic visualization risks further mucosal "
        "injury en route and does not shorten the ongoing esophageal contact time already "
        "causing damage; endoscopic removal is the standard of care.",
    ],
    "v140_gen_08": [
        "Persistent high-output leak despite maximal conservative therapy (fat restriction, "
        "pressure, octreotide) means that approach has already failed; continuing it "
        "unchanged only prolongs the nutritional, electrolyte, and immunologic losses "
        "chylous drainage causes.",
        "Removing the drain without controlling the leak simply redirects chyle into the "
        "soft tissues or mediastinum, risking a chyloma, wound breakdown, or respiratory "
        "compromise rather than resolving the underlying problem.",
        "Chyle leaks are a mechanical/lymphatic drainage problem, not a clotting disorder; "
        "anticoagulation has no role in controlling lymphatic outflow and would not be "
        "expected to reduce chyle volume.",
        "Correct.",
    ],
    "v140_gen_09": [
        "Awake flexible intubation preserves spontaneous ventilation and the patient's own "
        "airway tone throughout the attempt, which is why it is a recommended strategy in a "
        "predicted difficult airway rather than the dangerous option.",
        "Awake tracheostomy under local anesthesia bypasses the obstructed upper airway "
        "entirely while preserving spontaneous respiration, making it a reasonable rescue "
        "plan in selected anatomy rather than a hazard.",
        "A structured multidisciplinary briefing before attempting the airway is a safety "
        "practice that improves coordination and readiness; it does not itself create risk.",
        "Correct.",
    ],
    "v140_gen_10": [
        "Waiting for lab results delays decompression of a mechanically expanding hematoma "
        "that is already compromising the airway; in a true compressive emergency, opening "
        "the wound cannot wait for coagulation studies to return.",
        "Ultrasound adds diagnostic delay without providing therapeutic benefit in a patient "
        "whose airway is being actively compromised by an expanding hematoma; this is a "
        "clinical, bedside emergency, not an imaging-driven one.",
        "Correct.",
        "Voice change is a late and inconsistent sign; relying on it to trigger action "
        "ignores the more immediate and reliable signs already present (neck pressure, "
        "dysphagia, expanding swelling) that mandate action now.",
    ],
    "v143_gen_03": [
        "This is a septic thrombophlebitis with metastatic pulmonary emboli, not an allergic "
        "or inflammatory nasal process; topical nasal steroids do nothing for the underlying "
        "infection or septic emboli.",
        "Lemierre syndrome affects the internal jugular vein, not the carotid artery, and "
        "the disease is infectious/thrombotic rather than atherosclerotic; carotid "
        "endarterectomy does not address the septic source.",
        "Correct.",
        "Internal jugular vein thrombosis after pharyngitis is not an expected, benign "
        "finding -- it is the hallmark of Lemierre syndrome, a serious and potentially "
        "fatal condition that requires prompt antibiotic treatment, not observation.",
    ],
    "v143_gen_05": [
        "Chronic, stable tinnitus without acute change is a nonurgent outpatient issue and "
        "poses no immediate threat to airway, vision, or life, unlike a postoperative "
        "patient with evolving stridor.",
        "An asymptomatic septal deviation found incidentally requires no acute action at "
        "all and can be addressed electively, in clear contrast to a rapidly progressing "
        "airway emergency.",
        "Cerumen impaction is a routine, non-urgent complaint that can be managed on a "
        "standard outpatient basis and carries no risk of acute deterioration.",
        "Correct.",
    ],
    "v147_gen_01": [
        "Mild erythema without purulence, fever, or systemic signs is more consistent with "
        "inflammation than infection; reflexive broad-spectrum antibiotics for any redness "
        "drives resistance and adverse effects without proven benefit.",
        "Empirically double-covering organisms that have not been shown to be present or "
        "likely ignores the actual clinical picture and local resistance patterns, which is "
        "precisely what stewardship principles caution against.",
        "Cultures from a true abscess can identify the causative organism and guide "
        "narrowing of therapy; withholding them when they would change management runs "
        "counter to good antimicrobial stewardship.",
        "Correct.",
    ],
    "v147_gen_02": [
        "An optic chiasm lesion would cause visual field deficits (such as bitemporal "
        "hemianopia), not hoarseness, dysphagia, shoulder weakness, and tongue deviation, "
        "so it does not explain this constellation of findings.",
        "An isolated V1 (ophthalmic division of trigeminal) lesion would cause facial "
        "sensory loss in the forehead/eye region, not the combination of vagal, accessory, "
        "and hypoglossal deficits described here.",
        "Correct.",
        "Middle ear ossicle pathology causes conductive hearing loss, not the lower cranial "
        "neuropathies (voice, swallowing, shoulder, tongue) seen in this patient; it does "
        "not localize to the described findings at all.",
    ],
    "v147_gen_03": [
        "Correct.",
        "Simple dehydration does not explain hypophosphatemia, weakness, and arrhythmia "
        "developing specifically after aggressive refeeding in a severely malnourished "
        "patient; this pattern is the electrolyte-shift syndrome of refeeding, not volume "
        "depletion.",
        "Acute otitis media is a middle-ear infection with no connection to electrolyte "
        "shifts, weakness, or arrhythmia following nutritional repletion.",
        "BPPV is a positional vestibular disorder and has no relationship to nutritional "
        "status, phosphate levels, or cardiac arrhythmia.",
    ],
    "v147_gen_04": [
        "Plain sinus radiographs have poor soft-tissue resolution and cannot define a "
        "deep-neck abscess, its extent, or its relationship to major vessels -- they are "
        "essentially obsolete for this indication.",
        "Chest ultrasound evaluates thoracic structures, not the deep neck spaces where "
        "this abscess is suspected, and offers no useful information about a neck "
        "collection or its relationship to the carotid sheath.",
        "Correct.",
        "DEXA measures bone mineral density for osteoporosis screening and has no role in "
        "evaluating an acute soft-tissue infection.",
    ],
    "v147_gen_05": [
        "This is a retrospective observational study, so there is no randomization process "
        "to be biased -- the problem is that treatment assignment was never random in the "
        "first place, which is the separate issue of confounding by indication.",
        "Blinding addresses measurement or assessment bias, not the underlying confounding "
        "created when healthier patients preferentially received one treatment; it does "
        "nothing to correct for who was selected for surgery in a retrospective study.",
        "Correct.",
        "When a study was published has no bearing on whether sicker or healthier patients "
        "were selectively directed toward one treatment; publication date is irrelevant to "
        "this specific threat to validity.",
    ],
    "v147_gen_06": [
        "Chronologic age alone is a poor predictor of surgical outcome and should not by "
        "itself exclude a patient from potentially beneficial treatment; frailty and "
        "functional status matter far more than years lived.",
        "Correct.",
        "Being technically resectable does not mean an operation is safe or beneficial for "
        "this specific patient; major surgery in a severely frail patient can cause net "
        "harm even when the tumor itself could be removed.",
        "Cognitive impairment directly affects a patient's ability to participate in "
        "recovery, follow postoperative instructions, and tolerate treatment burden, so "
        "ignoring it omits a critical factor in decision-making.",
    ],
    "v147_gen_07": [
        "Covering exposed hardware with nonvascular, scarred tissue does not restore a "
        "healthy blood supply to the wound bed and is likely to fail again, since the "
        "underlying problem -- poor vascularity -- is unaddressed.",
        "Antibiotics can treat superficial infection but cannot overcome biofilm on an "
        "exposed implant or restore a compromised soft-tissue envelope; exposure often "
        "persists or recurs despite antibiotic therapy alone.",
        "Radiation damages microvasculature and impairs, rather than improves, tissue "
        "integration and healing around an implant -- the opposite of what this option "
        "states.",
        "Correct.",
    ],
    "v147_gen_08": [
        "Correct.",
        "Black eschar is a late finding in acute invasive fungal rhinosinusitis; "
        "neutropenic patients may have blunted inflammatory signs, so waiting for this "
        "classic but late sign risks missing the window for effective debridement and "
        "antifungal therapy.",
        "Facial pain and fever with dusky mucosa in a neutropenic patient should raise "
        "concern for a life-threatening invasive infection, not be managed as routine "
        "allergic disease in an outpatient setting.",
        "Culture results can take days, during which invasive fungal disease can progress "
        "rapidly and become unresectable or fatal; clinical suspicion alone should prompt "
        "urgent biopsy and empiric therapy rather than waiting.",
    ],
    "v147_gen_09": [
        "High oxidizer concentration is one of the three elements required for an airway "
        "fire (with fuel and ignition source); maximizing FiO2 during laser activation "
        "increases, rather than decreases, fire risk.",
        "Wet pledgets/sponges protect adjacent tissue and reduce ignition risk from stray "
        "laser energy; disregarding them removes a safeguard rather than improving safety.",
        "Standard adhesive tapes and some tube materials are flammable and can ignite from "
        "laser energy; using non-laser-safe materials near an active laser field increases "
        "fire risk rather than mitigating it.",
        "Correct.",
    ],
    "v147_gen_10": [
        "Simple aphthous ulcers are typically isolated to the mouth and do not explain "
        "concurrent genital ulcers and uveitis; the multisystem pattern here points to a "
        "systemic disease, not an isolated local process.",
        "Ménière disease causes vertigo, fluctuating hearing loss, and aural fullness -- it "
        "has no association with oral ulcers, genital ulcers, or uveitis, and does not fit "
        "this presentation.",
        "Otosclerosis causes progressive conductive hearing loss from stapes fixation; it "
        "has no relationship to mucocutaneous ulceration or ocular inflammation and does "
        "not explain any of the findings described.",
        "Correct.",
    ],
    "v147_gen_11": [
        "High-dose opioids in an opioid-naive patient with OSA carry a significant risk of "
        "respiratory depression during sleep, making monotherapy at high doses a "
        "particularly hazardous approach in this specific patient.",
        "Correct.",
        "Avoiding all nonopioid options removes agents (acetaminophen, NSAIDs where "
        "appropriate, regional techniques) that reduce total opioid requirement and "
        "therefore respiratory risk in a patient who already has OSA.",
        "Sedating a patient with untreated OSA until pain resolves increases the risk of "
        "airway obstruction and hypoventilation during sleep, compounding rather than "
        "solving the safety problem posed by opioid-naive status and OSA.",
    ],
    "v147_gen_12": [
        "Allergic rhinitis does not cause subglottic stenosis, pulmonary nodules, or renal "
        "dysfunction; it cannot account for the multisystem pattern described here.",
        "BPPV is a peripheral vestibular disorder causing brief positional vertigo; it has "
        "no connection to nasal crusting, airway stenosis, lung, or kidney disease.",
        "Correct.",
        "Otosclerosis causes isolated conductive hearing loss from stapes fixation and has "
        "no relationship to the sinonasal, airway, pulmonary, or renal findings described "
        "in this multisystem presentation.",
    ],
    "v147_gen_13": [
        "Radiation actually damages the microvasculature over time, reducing rather than "
        "increasing blood supply to irradiated tissue -- the opposite of what this option "
        "states.",
        "Correct.",
        "Irradiated, fibrotic, poorly vascularized tissue is generally more, not less, "
        "susceptible to infection because of impaired local immune delivery and healing "
        "capacity.",
        "Radiation-damaged tissue is characteristically hypovascular and hypoxic, not "
        "richly oxygenated; this is precisely why healing is impaired and reconstruction "
        "may require importing a new blood supply via vascularized tissue transfer.",
    ],
}


def apply_why_wrong_fix_general_ent_v1(data_module):
    """Overwrite why_wrong for the fixed ids. Returns count actually updated."""
    byid = {q.get("id"): q for q in data_module.CLINICAL_CHALLENGES_V119 if q.get("id")}
    updated = 0
    missing = []
    for qid, new_why_wrong in WHY_WRONG_FIXES.items():
        q = byid.get(qid)
        if q is None:
            missing.append(qid)
            continue
        if len(new_why_wrong) != len(q.get("choices") or []):
            raise ValueError(
                f"{qid}: fix has {len(new_why_wrong)} entries but question has "
                f"{len(q.get('choices') or [])} choices"
            )
        q["why_wrong"] = new_why_wrong
        updated += 1
    if missing:
        print(f"why_wrong_fix_general_ent_v1: {len(missing)} ids not found: {missing}")
    return updated
