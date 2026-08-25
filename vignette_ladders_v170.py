"""v17.0 — Deliberate learning-ladder curation, Otology pass 2.

Reviews the next five canonical Otology concepts and preserves their v12.4
foundation cases while adding application and senior/chief decision layers.
"""


def _q(qid, topic, stage, stem, choices, answer, explanation, why_wrong, pearl, curveball, focus):
    return {
        "id": qid, "domain": "Otology / Neurotology", "topic": topic,
        "learning_stage": stage, "stem": stem, "choices": choices, "answer": answer,
        "explanation": explanation, "why_wrong": why_wrong, "board_pearl": pearl,
        "curveball": curveball, "tier": "Curated learning ladder", "mode": "Vignette",
        "focus": focus,
    }


REVIEWED_FOUNDATION_IDS_V170 = {
    "v124_oto_07",  # Vestibular Neuritis
    "v124_oto_08",  # CSF Otorrhea / Temporal Encephalocele
    "v124_oto_09",  # Acute Mastoiditis / Petrous Apicitis
    "v124_oto_10",  # Patulous Eustachian Tube Dysfunction
    "v124_oto_11",  # Perilymph Fistula / Inner-Ear Window Leak
}


VIGNETTES_V170 = [
    _q(
        "v170_oto_vn_app", "Vestibular Neuritis", "application",
        "A 44-year-old has 36 hours of continuous vertigo, nausea, and spontaneous unidirectional horizontal-torsional nystagmus. Hearing is unchanged. Head impulse is abnormal to the left, there is no skew, and gait is impaired but independent. After stroke red flags are excluded, which treatment plan is most appropriate?",
        ["Weeks of scheduled meclizine to prevent recurrent vertigo", "A short course of symptomatic medication followed by early mobilization and vestibular rehabilitation", "Immediate intratympanic gentamicin", "Epley maneuvers every four hours"], 1,
        "Once a peripheral acute vestibular syndrome is established, vestibular suppressants are useful only briefly for severe acute symptoms. Early activity and vestibular rehabilitation promote central compensation; prolonged suppressants can delay it.",
        ["Prolonged vestibular suppression can impede compensation and creates sedation/fall risk.", "Correct. Acute symptom control should transition quickly to compensation-focused rehabilitation.", "Gentamicin intentionally ablates vestibular function and is not routine treatment for vestibular neuritis.", "Epley treats canalithiasis causing brief positional attacks, not continuous neuritis."],
        "Treat the miserable acute phase, then get the vestibular system moving; chronic suppressants work against compensation.",
        "If new unilateral hearing loss accompanies the acute vestibular syndrome, how does the localization and urgency change?", "boards"),
    _q(
        "v170_oto_vn_snr", "Vestibular Neuritis", "senior_decision",
        "A 69-year-old with vascular risk factors presents with a first episode of continuous vertigo and vomiting. Nystagmus is direction-changing with gaze, head impulse is normal, and the patient cannot stand without support. An early diffusion-weighted MRI is reported negative. What is the safest next decision?",
        ["Discharge with vestibular neuritis because MRI excludes posterior circulation stroke", "Treat the bedside pattern as central and pursue urgent stroke-level evaluation despite the early negative MRI", "Perform canalith repositioning and discharge", "Start chronic vestibular suppressants and reassess in one month"], 1,
        "In a true acute vestibular syndrome, central ocular-motor findings and profound truncal/gait instability can outweigh an early negative MRI because small posterior-fossa infarcts may be missed early. The senior error is false reassurance from imaging that conflicts with the bedside localization.",
        ["Early MRI is not perfectly sensitive for small posterior-circulation infarction, especially when the bedside pattern is central.", "Correct. Discordant central bedside findings require escalation, not diagnostic closure.", "BPPV produces brief triggered attacks and does not explain this continuous central pattern.", "Suppressants do not address a possible stroke and can obscure serial examination."],
        "HINTS is a localization tool for continuous acute vestibular syndrome in appropriately selected patients—not a generic dizziness checklist.",
        "Which patients are poor candidates for HINTS interpretation because they do not actually have an acute vestibular syndrome?", "overnight_call"),

    _q(
        "v170_oto_csf_app", "CSF Otorrhea / Temporal Encephalocele", "application",
        "An adult with recurrent unilateral middle-ear effusion develops persistent clear drainage after tympanostomy. Beta-2 transferrin is positive. High-resolution CT shows a tegmen tympani defect and MRI suggests a small temporal encephalocele. What is the best management principle?",
        ["Treat recurrently with topical drops because the tube is the source", "Refer for definitive skull-base repair after defining the defect and evaluating factors that may drive recurrence", "Remove the tube and observe indefinitely", "Perform stapedotomy"], 1,
        "A confirmed lateral skull-base CSF leak carries meningitis risk and generally warrants definitive repair in an appropriate surgical candidate. CT defines bony anatomy, MRI helps characterize herniated soft tissue, and spontaneous leaks should prompt attention to recurrence drivers such as elevated intracranial pressure.",
        ["Drops do not close a tegmen defect or eliminate intracranial infectious risk.", "Correct. Confirmation, localization, repair planning, and recurrence-risk assessment belong together.", "Tube removal may hide the drainage but does not correct the skull-base communication.", "Stapedotomy does not treat a tegmen defect or CSF leak."],
        "Persistent clear otorrhea after a tube can reveal—not cause—a pre-existing skull-base CSF leak.",
        "What clinical and imaging clues would make idiopathic intracranial hypertension part of the recurrence workup?", "boards"),
    _q(
        "v170_oto_csf_snr", "CSF Otorrhea / Temporal Encephalocele", "senior_decision",
        "A patient has a spontaneous lateral temporal-bone CSF leak with multiple tegmen defects, a sizable encephalocele, and preserved hearing. Which operative planning principle is most appropriate?",
        ["Choose an approach only from the patient's age", "Select transmastoid, middle-fossa, or combined repair based on defect number/location/size, encephalocele extent, hearing, and need for durable multilayer closure", "A lumbar drain alone is definitive treatment", "Obliterate the cochlea routinely to prevent recurrence"], 1,
        "Approach selection is anatomy-driven. Limited accessible defects may be repaired transmastoid, whereas broad/multiple anterior tegmen defects or substantial encephaloceles may favor middle-fossa or combined exposure. Durable closure and management of elevated intracranial pressure when present matter as much as simply plugging visible holes.",
        ["Chronologic age alone does not define the surgical corridor.", "Correct. Chief-level planning integrates the map of disease, hearing preservation, exposure, and recurrence biology.", "CSF diversion can be adjunctive in selected cases but does not reliably repair a structural skull-base defect by itself.", "Routine cochlear obliteration would sacrifice hearing without addressing the tegmen pathology."],
        "For spontaneous tegmen leaks, repair the anatomy and ask why the dura failed there in the first place.",
        "How would a single posterior tegmen mastoideum defect differ from broad anterior tegmen tympani disease in your preferred exposure?", "OR_prep"),

    _q(
        "v170_oto_mast_app", "Acute Mastoiditis / Petrous Apicitis", "application",
        "A child with acute coalescent mastoiditis has fever, postauricular swelling, and a subperiosteal abscess on CT but no intracranial complication. What is the most appropriate escalation?",
        ["Oral antibiotics alone at home", "Hospital admission for IV antibiotics with drainage/source control, including mastoid surgery when indicated by the abscess and coalescent disease", "Observation because mastoid opacification is always incidental", "Vestibular suppressants only"], 1,
        "A subperiosteal abscess plus coalescent bony disease represents complicated mastoiditis and requires inpatient antimicrobial therapy and source-control planning rather than treatment as uncomplicated otitis media.",
        ["Oral outpatient therapy is inadequate for a deep complication with bony destruction.", "Correct. The abscess and coalescence are the management-changing findings.", "Simple mastoid opacification can be nonspecific, but cortical destruction and a subperiosteal collection are not incidental.", "Vestibular suppressants do not treat invasive infection."],
        "Do not operate on the word 'opacification'; operate/escalate for the complication pattern—coalescence, abscess, neurologic spread, or failure of therapy.",
        "How would sigmoid sinus thrombosis or an epidural abscess change the team, imaging, and operative plan?", "overnight_call"),
    _q(
        "v170_oto_mast_snr", "Acute Mastoiditis / Petrous Apicitis", "senior_decision",
        "A patient treated for otitis media develops persistent deep facial/retro-orbital pain, otorrhea, and new abducens palsy. Imaging shows petrous-apex inflammatory disease. What is the best senior-level interpretation and plan?",
        ["This is uncomplicated otitis media; continue the same outpatient regimen", "Recognize petrous apicitis/Gradenigo-pattern disease and escalate to IV antimicrobial therapy, targeted imaging, and drainage when medical therapy or anatomy requires it", "Treat as isolated sixth-nerve palsy with an eye patch only", "Perform Epley maneuver"], 1,
        "Deep pain plus otorrhea and sixth-nerve dysfunction is the classic warning constellation for petrous-apex infection. Management requires aggressive antimicrobial treatment and assessment for surgical drainage based on clinical response, abscess, osteitis, and accessible disease.",
        ["A cranial neuropathy and petrous-apex disease make this a complication, not routine AOM.", "Correct. The key is recognizing skull-base extension and escalating before further neurologic or intracranial spread.", "An eye patch may palliate diplopia but ignores the infectious cause.", "Canalith repositioning has no role in petrous apicitis."],
        "New cranial neuropathy in otomastoid infection is a localization clue to skull-base spread until proven otherwise.",
        "Which venous and intracranial complications should be actively sought when petrous-apex infection is extensive?", "overnight_call"),

    _q(
        "v170_oto_pet_app", "Patulous Eustachian Tube Dysfunction", "application",
        "A patient reports hearing her own breathing loudly after substantial weight loss; symptoms worsen with exercise and improve supine. Otoscopy is normal at rest. Which office maneuver best helps support the suspected diagnosis?",
        ["Observe the tympanic membrane while the patient performs forceful nasal breathing with one nostril occluded", "Dix-Hallpike testing only", "Carotid compression", "Pneumatic otoscopy after topical phenylephrine as the sole diagnostic test"], 0,
        "Patulous Eustachian tube symptoms can be intermittent. Provoking respiration while directly observing the tympanic membrane or using long time-base tympanometry can demonstrate respiration-synchronous pressure transmission even when the resting exam is normal.",
        ["Correct. Dynamic testing can reveal respiration-synchronous tympanic-membrane movement.", "Dix-Hallpike evaluates posterior-canal BPPV, not respiratory autophony.", "Jugular/carotid maneuvers are used in selected pulsatile-tinnitus evaluations and do not diagnose patulous ETD.", "A single static otoscopic maneuver is less useful than reproducing the characteristic dynamic physiology."],
        "A normal resting ear exam does not exclude patulous ETD; reproduce the symptom and look for respiration-synchronous mechanics.",
        "How would autophony from superior canal dehiscence differ when you ask exactly which internal sounds the patient hears?", "boards"),
    _q(
        "v170_oto_pet_snr", "Patulous Eustachian Tube Dysfunction", "senior_decision",
        "A patient with disabling patulous Eustachian tube symptoms has failed hydration, weight stabilization, and conservative measures. Before an irreversible procedure, what is the most important senior-level step?",
        ["Assume all autophony is patulous ETD and permanently occlude the tube", "Objectively confirm symptom-mechanism concordance and exclude mimics such as superior canal dehiscence before selecting a targeted intervention", "Place a ventilation tube in every patient regardless of physiology", "Perform stapedectomy"], 1,
        "Patulous ETD treatments can trade autophony for obstructive middle-ear problems and outcomes vary. Before procedural escalation, the diagnosis should be physiologically supported and third-window or other autophony mimics excluded; treatment is then individualized and preferably reversible when possible.",
        ["Irreversible closure based on symptoms alone risks treating the wrong mechanism and causing chronic obstruction.", "Correct. Diagnostic certainty matters most when the proposed intervention can create a new mechanical problem.", "Tympanostomy may help selected patients but is neither universally effective nor diagnostic proof.", "Stapes surgery does not treat an abnormally patent Eustachian tube."],
        "The more irreversible the ET intervention, the higher the bar for proving that the tube—not a third window—is causing the symptom.",
        "What postoperative problems would you counsel about if an intervention intentionally narrows or occludes the Eustachian tube?", "OR_prep"),

    _q(
        "v170_oto_plf_app", "Perilymph Fistula / Inner-Ear Window Leak", "application",
        "After barotrauma, a patient has abrupt unilateral sensorineural hearing loss and vertigo that worsen with coughing and lifting. Otoscopy is normal. What is the most appropriate initial framework?",
        ["Treat as routine BPPV because all post-traumatic vertigo is positional", "Recognize a possible inner-ear window injury, institute pressure-avoidance measures, obtain urgent audiovestibular assessment, and follow hearing closely", "Reassure because a normal tympanic membrane excludes inner-ear trauma", "Start chronic aminoglycoside drops"], 1,
        "Pressure-linked cochleovestibular symptoms after barotrauma raise concern for an oval- or round-window injury. Initial management emphasizes avoiding further pressure stress, documenting hearing, excluding other urgent causes, and watching for deterioration that may justify exploration.",
        ["BPPV can follow trauma but does not explain abrupt SNHL or pressure-sensitive cochlear symptoms.", "Correct. The combination of trauma, hearing loss, vertigo, and pressure sensitivity changes the pathway.", "The tympanic membrane can be normal despite inner-ear window injury.", "Aminoglycosides can be ototoxic and do not repair a suspected fistula."],
        "Post-traumatic vertigo plus new SNHL is not 'just BPPV' until the cochlear injury is explained.",
        "Which alternative diagnoses—including third-window disease and inner-ear decompression injury—must be considered from the exposure history?", "boards"),
    _q(
        "v170_oto_plf_snr", "Perilymph Fistula / Inner-Ear Window Leak", "senior_decision",
        "A diver with a convincing pressure injury has progressive sensorineural hearing loss and disabling pressure-provoked vertigo despite strict conservative management. Imaging excludes an obvious third-window lesion. What is the best next decision?",
        ["Continue observation indefinitely even as hearing deteriorates", "Discuss timely middle-ear exploration with reinforcement of the oval/round windows because progressive cochleovestibular loss lowers the threshold for operative treatment", "Perform vestibular nerve section", "Place a cochlear implant immediately without evaluating the suspected leak"], 1,
        "Perilymph fistula is often a clinical diagnosis and no single test is perfectly definitive. In a compelling traumatic setting, progressive hearing loss or persistent disabling vestibular symptoms despite conservative therapy can justify exploration and window reinforcement after competing diagnoses are addressed.",
        ["Ongoing deterioration changes the risk-benefit balance against indefinite observation.", "Correct. The operative threshold depends on exposure mechanism, trajectory, functional severity, and exclusion of mimics rather than one laboratory test.", "Vestibular nerve section is disproportionately destructive and does not address the suspected window injury.", "Implantation is not the first response to an active, potentially repairable traumatic process."],
        "For suspected traumatic fistula, trajectory matters: worsening hearing is more management-changing than a static nonspecific dizziness complaint.",
        "If exploration finds no visible leak, why might surgeons still reinforce the windows in a highly convincing traumatic case?", "OR_prep"),
]


def apply_learning_ladders_v170(challenges, id_factory):
    by_id = {q.get("id"): q for q in challenges if q.get("id")}
    reviewed = 0
    for qid in REVIEWED_FOUNDATION_IDS_V170:
        q = by_id.get(qid)
        if q:
            q["learning_stage"] = "foundation"
            q["ladder_reviewed"] = True
            reviewed += 1

    existing = {q.get("id") for q in challenges}
    added = 0
    for item in VIGNETTES_V170:
        if item["id"] in existing:
            continue
        q = dict(item)
        q["concept_id"] = id_factory(q.get("domain", ""), q.get("topic", ""))
        q["ladder_reviewed"] = True
        challenges.append(q)
        existing.add(q["id"])
        added += 1
    return {"reviewed_foundations": reviewed, "added": added, "topics": 5}
