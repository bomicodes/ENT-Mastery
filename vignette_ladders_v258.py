"""v25.8 — Facial Plastics / Trauma deliberate ladder pass 2.

Adds five exact canonical trauma topics with foundation -> application ->
senior-decision ladders emphasizing anatomy, functional priorities, sequencing,
and complications rather than isolated fracture-label recall.
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

VIGNETTES_V258 = [
    _q("v258_fpt_noe_fnd","NOE Fracture","foundation",
       "A patient with central midface trauma has a widened nasal bridge, telecanthus, and loss of nasal projection. Which structure is most important to assess because its disruption drives the characteristic medial canthal deformity?",
       ["Medial canthal tendon and its attachment to the central NOE fragment","Lateral canthal tendon only","Masseter insertion on the mandibular angle","Temporalis tendon on the coronoid"],0,
       "NOE fractures disrupt the central nasal-orbital-ethmoid skeleton. The medial canthal tendon attachment and the stability of the bone carrying it are central to classification, telecanthus, and reconstruction.",
       ["Correct. MCT integrity and the quality of its bony attachment determine whether stable fixation alone is enough or tendon reconstruction is required.","The lateral canthus does not explain traumatic telecanthus from central midface disruption.","The masseter affects mandibular biomechanics, not medial canthal position.","The temporalis insertion does not govern intercanthal width."],
       "In NOE trauma, do not just ask whether the nasal bones are broken—ask whether the medial canthal tendon still has a stable home.",
       "What bedside finding or maneuver can suggest medial canthal tendon instability?"),
    _q("v258_fpt_noe_app","NOE Fracture","application",
       "CT shows a comminuted NOE fracture with mobile central fragments and clinically obvious telecanthus. What operative principle best prevents a persistent post-traumatic widened intercanthal distance?",
       ["Restore stable central skeletal support and anatomically secure the medial canthal tendon when its native bony attachment is not reliable","Reduce only the nasal dorsum and ignore the medial orbit","Place cosmetic filler at the nasal root instead of skeletal repair","Wait for the tendon to scar in a widened position"],0,
       "NOE repair depends on accurate reduction of the central facial skeleton and restoration of medial canthal position. When the tendon remains attached to a stable fragment, that fragment can be fixed; when the attachment is avulsed or the fragment is too comminuted, tendon fixation becomes necessary.",
       ["Correct. Skeletal width and tendon position must both be restored.","Dorsal contour alone does not correct medial orbital widening or tendon displacement.","Filler cannot restore fracture stability or tendon attachment.","Delayed scarring in malposition makes secondary correction much harder."],
       "Telecanthus after NOE trauma is usually a fixation problem, not a camouflage problem.",
       "How does severe comminution change your confidence in a tendon-bearing central fragment?", "OR_prep"),
    _q("v258_fpt_noe_snr","NOE Fracture","senior_decision",
       "A patient has NOE, frontal sinus, and orbital fractures with CSF rhinorrhea. Which senior-level approach best organizes definitive reconstruction?",
       ["Coordinate skull-base/CSF-leak management first, then re-establish stable craniofacial reference points and restore central facial width, medial canthal position, nasal projection, and orbital geometry in a planned sequence","Fix isolated small fragments opportunistically without defining stable reference points","Perform nasal cosmetic reconstruction before addressing the skull base","Ignore the medial canthi until a later cosmetic procedure"],0,
       "Complex central facial trauma crosses skull base, orbit, and facial skeleton. Definitive repair should prioritize intracranial/skull-base safety and then rebuild from reliable references so that width, projection, canthal position, and orbital volume are not fixed inconsistently.",
       ["Correct. This avoids locking in a central facial deformity while higher-priority injuries remain unresolved.","Fragment-by-fragment fixation without a global frame can encode malposition.","Cosmetic nasal work is secondary to CSF/skull-base and structural reconstruction.","Delayed canthal correction is more difficult after fibrosis and malunited central fragments."],
       "NOE injuries punish poor sequencing: establish the safe skull base and a reliable facial frame before fine contour.",
       "Which late deformities suggest inadequate primary NOE reduction?", "senior_management"),

    _q("v258_fpt_frontal_fnd","Frontal Sinus Fracture","foundation",
       "A CT after forehead trauma shows a frontal sinus fracture. Which three anatomic questions most directly determine management?",
       ["Anterior table contour, posterior table/dural injury, and frontal sinus outflow tract function","Only the size of the skin laceration","Only whether the patient has frontal headache","Only whether both frontal sinuses are pneumatized"],0,
       "Frontal sinus fracture planning separates the cosmetic anterior table, the posterior table/skull-base interface, and the frontal sinus outflow tract. Each component changes observation, repair, sinus-preservation, or cranialization decisions.",
       ["Correct. These are the core management axes.","Skin injury affects approach and wound care but does not define sinus safety.","Headache is nonspecific and cannot characterize table or outflow injury.","Pneumatization matters anatomically but does not replace injury assessment."],
       "Think of frontal sinus trauma as three linked problems: forehead contour, brain separation, and sinus drainage.",
       "What clinical finding should raise immediate concern for posterior table/dural violation?"),
    _q("v258_fpt_frontal_app","Frontal Sinus Fracture","application",
       "A patient has a minimally displaced anterior-table frontal sinus fracture, intact posterior table, no CSF leak, and no convincing outflow obstruction. What is the most appropriate management principle?",
       ["Observation with clinical and radiographic follow-up is reasonable when contour and sinus drainage are preserved","Cranialize every frontal sinus fracture","Obliterate the sinus solely because any anterior-table fracture exists","Perform emergent bicoronal exposure despite preserved contour and drainage"],0,
       "Modern frontal sinus management is increasingly selective. A stable anterior-table injury without posterior-table danger or outflow obstruction can often be observed, provided follow-up can detect ventilation failure, sinusitis, or late mucocele.",
       ["Correct. Management should match the injured subsite and functional risk.","Cranialization is reserved for substantially more severe posterior-table/skull-base patterns.","Obliteration is not required for every isolated anterior-table injury.","An extensive approach adds morbidity without correcting a demonstrated problem."],
       "A frontal sinus fracture is not automatically an operation; treat the component that is actually unsafe.",
       "What follow-up problem can present years later if frontal sinus drainage becomes chronically obstructed?", "senior_management"),
    _q("v258_fpt_frontal_snr","Frontal Sinus Fracture","senior_decision",
       "CT demonstrates a severely comminuted displaced posterior-table fracture with pneumocephalus, a persistent CSF leak, and major disruption of the sinus-skull-base barrier. What definitive principle is most appropriate?",
       ["Treat this as a skull-base injury requiring multidisciplinary repair, with cranialization considered when posterior-table disruption is severe and sinus preservation is unsafe","Repair only the forehead contour and leave the posterior injury untouched","Use closed nasal reduction to seal the CSF leak","Observe indefinitely because CSF leaks never require operative management"],0,
       "Severe posterior-table disruption with persistent CSF communication moves the problem beyond cosmetic frontal sinus repair. Management may require dural repair and cranialization, removing unsafe posterior sinus boundaries and isolating the sinonasal tract from the intracranial space.",
       ["Correct. The operation must restore a durable brain-sinus barrier and address the unsafe posterior table.","Anterior contour repair alone does not control intracranial contamination or CSF leakage.","Closed nasal reduction does not address the frontal posterior table or dura.","Some traumatic leaks may resolve, but severe displaced comminution with persistent leakage requires active definitive planning."],
       "The more the posterior table stops behaving like a wall, the more the case becomes skull-base surgery rather than simple facial fracture repair.",
       "Which factors would make sinus-preserving endoscopic strategies more reasonable than open cranialization?", "senior_management"),

    _q("v258_fpt_lefort_fnd","Le Fort / Panfacial Trauma","foundation",
       "A patient has mobile maxilla, malocclusion, facial elongation, and midface instability after high-energy trauma. What functional relationship should be documented and restored during panfacial reconstruction?",
       ["Premorbid dental occlusion and facial width-height-projection relationships","Only forehead skin symmetry","Only external nasal color","Only the size of each fracture gap on CT"],0,
       "Le Fort and panfacial trauma are three-dimensional alignment injuries. Occlusion gives a functional reference, while facial width, vertical height, and projection determine global skeletal form.",
       ["Correct. These relationships guide reconstruction of multiple connected segments.","Forehead skin symmetry does not define maxillomandibular alignment.","Nasal skin color is not a skeletal reference.","Individual fracture gaps can look reduced while the global face remains malpositioned."],
       "In panfacial trauma, the goal is not to make every fracture line look pretty—it is to rebuild one coherent face.",
       "Which airway concern can complicate maxillomandibular fixation in severe facial trauma?"),
    _q("v258_fpt_lefort_app","Le Fort / Panfacial Trauma","application",
       "A dentate patient with panfacial fractures has an intact mandible that can be reproducibly placed into premorbid occlusion. What sequencing concept is most useful?",
       ["Use the reliable mandibular arch and occlusion as a lower facial reference, then rebuild the midface systematically while repeatedly checking width, height, projection, and orbital relationships","Plate the most comminuted midface fragment first because it is visually dramatic","Finalize the orbits before establishing any facial skeletal reference","Ignore the bite until skin closure"],0,
       "When the mandible is trustworthy, bottom-up reconstruction can provide a stable platform for maxillary and midface reduction. The larger principle is to choose the most reliable reference, not to follow one universal order in every pattern.",
       ["Correct. Stable occlusion and arch form can anchor the reconstruction.","Starting with the least reliable fragment can propagate error.","Orbital geometry depends on the surrounding facial frame.","Late occlusal discovery may reveal that multiple already-fixed segments are wrong."],
       "Choose a trustworthy reference first; sequencing is anatomy-driven, not ritual-driven.",
       "When would a top-down approach be preferable?", "OR_prep"),
    _q("v258_fpt_lefort_snr","Le Fort / Panfacial Trauma","senior_decision",
       "After panfacial fixation, the plates appear satisfactory on individual buttresses but the patient has widened facial width and persistent malocclusion. What is the best interpretation?",
       ["The global reconstruction is wrong despite locally acceptable fixation; reassess the reference segment and release/reduce fixation as needed before accepting closure","Leave everything because each plate is technically seated","Correct the bite later with orthodontics regardless of skeletal malposition","Camouflage facial width with soft-tissue filler"],0,
       "Panfacial success is measured by integrated three-dimensional relationships, not plate appearance. If occlusion or facial width is wrong, the construct may need to be revised before union makes correction more difficult.",
       ["Correct. Global form and function outrank local hardware neatness.","A well-seated plate can rigidly fix a malreduction.","Orthodontics cannot reliably compensate for major skeletal malposition.","Soft-tissue camouflage does not restore facial skeletal geometry."],
       "A rigidly fixed wrong face is harder to fix than an unfixed wrong face.",
       "Which intraoperative checks should be repeated before final tightening of the construct?", "senior_management"),

    _q("v258_fpt_biomech_fnd","Mandibular Biomechanics and Occlusion","foundation",
       "Why can a mandibular fracture displace even when the fracture line itself looks small?",
       ["Muscle forces and the tension-compression behavior of the mandibular arch can separate or rotate fragments depending on fracture orientation","The mandible has no meaningful muscular attachments","All mandibular fractures are mechanically identical","Dental occlusion does not transmit force across the mandible"],0,
       "Mandibular displacement reflects fracture geometry plus muscular pull and functional loading. Understanding tension and compression zones explains why fixation strategy differs by site and fracture favorability.",
       ["Correct. Biomechanics, not just fracture size, determine stability.","Masseter, temporalis, pterygoids, suprahyoids, and other forces strongly influence fragments.","Angle, body, symphysis, condyle, and atrophic fractures behave differently.","The dental arch is a major functional reference and load pathway."],
       "Mandible questions become easier when you stop memorizing plates and start thinking about force vectors.",
       "How can the direction of an angle fracture make it favorable or unfavorable?"),
    _q("v258_fpt_biomech_app","Mandibular Biomechanics and Occlusion","application",
       "A patient with bilateral mandibular fractures has a reconstructed lower border that looks symmetric, but the premorbid bite cannot be reproduced. What should happen before definitive fixation is accepted?",
       ["Reassess reduction, arch width, condylar seating, and occlusal reference because skeletal continuity without correct occlusion is not an adequate functional repair","Ignore the bite because lower-border symmetry proves correct reduction","Remove healthy teeth until the bite closes","Accept the result and plan routine soft-tissue revision"],0,
       "Occlusion is an integrated readout of mandibular arch form, vertical height, and condylar position. A symmetric border can coexist with an incorrect arch or condylar relationship.",
       ["Correct. Functional alignment must be restored, not just contour.","External symmetry does not prove the dental and condylar system is correct.","Healthy teeth should not be sacrificed to fit a malreduced skeleton.","Soft-tissue revision cannot correct skeletal malocclusion."],
       "If the bite is wrong, assume the reduction is wrong until you prove otherwise.",
       "What factors make premorbid occlusion an unreliable reference?", "OR_prep"),
    _q("v258_fpt_biomech_snr","Mandibular Biomechanics and Occlusion","senior_decision",
       "An edentulous older patient has a markedly atrophic mandibular-body fracture with poor bone stock. Which fixation concept becomes especially important?",
       ["Use a load-bearing construct capable of bridging weak bone rather than relying on dentition-dependent stabilization or minimal load-sharing fixation","Use dental arch bars as the sole treatment despite absent dentition","Use the smallest plate possible because atrophic bone carries load well","Ignore inferior alveolar nerve and soft-tissue vascularity when increasing fixation"],0,
       "Atrophic edentulous fractures have limited bone stock, reduced contact area, and no reliable dental occlusion for fixation. They often require more robust load-bearing reconstruction while preserving soft-tissue blood supply and accounting for nerve position.",
       ["Correct. The hardware must carry more of the functional load when the bone cannot.","Arch bars cannot provide conventional dental fixation without usable dentition.","Atrophic bone is less able to share load.","Robust fixation still requires careful dissection and respect for vascularity and nerve anatomy."],
       "Weak bone shifts the construct from load sharing toward load bearing.",
       "How does severe atrophy alter screw purchase and plate position planning?", "senior_management"),

    _q("v258_fpt_soft_fnd","Facial Soft-Tissue Lacerations / Burns","foundation",
       "A deep cheek laceration crosses the course of the parotid duct and buccal branches of the facial nerve. What is the key principle before routine layered closure?",
       ["Identify and document injury to critical structures such as facial nerve, parotid duct, eyelid/canaliculus, major vessels, and cartilage before they are buried by closure","Close the skin immediately without deeper examination","Assume intact facial movement excludes parotid duct injury","Delay all wound irrigation because facial wounds are highly vascular"],0,
       "Facial wounds demand structure-specific examination before closure. Nerve, duct, canalicular, cartilage, and vascular injuries are easier to identify and repair before swelling and wound closure obscure them.",
       ["Correct. Functional structures must be assessed before they disappear beneath a cosmetically neat closure.","Immediate superficial closure can conceal injuries that require repair.","Facial movement says nothing about salivary duct continuity.","Irrigation and contamination control are core wound-care steps."],
       "A beautiful skin closure over a missed nerve or duct injury is still a bad facial repair.",
       "How can you assess parotid duct continuity in a suspicious cheek wound?"),
    _q("v258_fpt_soft_app","Facial Soft-Tissue Lacerations / Burns","application",
       "A patient has a jagged contaminated facial laceration with viable but irregular skin edges and no tissue loss. Which repair principle best preserves long-term function and cosmesis?",
       ["Irrigate thoroughly, debride only clearly nonviable tissue, align key landmarks precisely, close in appropriate layers without excessive tension, and preserve viable facial tissue whenever possible","Excise a wide margin of healthy tissue to create a simple geometric wound","Place maximal tension on the epidermal sutures to flatten the wound","Ignore vermilion, brow, alar, or eyelid landmarks until later scar revision"],0,
       "Facial vascularity supports conservative tissue preservation. Meticulous landmark alignment, layered tension distribution, and contamination control usually matter more than converting every irregular wound into a large clean ellipse.",
       ["Correct. This preserves tissue and reduces distortion of high-visibility landmarks.","Unnecessary tissue sacrifice can create a larger reconstructive problem.","Epidermal tension increases track marks, ischemia, and scar widening.","Small landmark mismatches are conspicuous and may be difficult to correct secondarily."],
       "On the face, preserve tissue and spend precision on landmarks.",
       "Which facial landmarks tolerate even a 1-2 mm alignment error poorly?", "overnight_call"),
    _q("v258_fpt_soft_snr","Facial Soft-Tissue Lacerations / Burns","senior_decision",
       "A patient with a deep facial burn has evolving edema, eyelid involvement, and circumferential neck burns after an enclosed-space fire. What should the senior plan prioritize?",
       ["Airway/inhalation-injury assessment and ocular protection first, then staged burn debridement/reconstruction based on tissue viability and functional units rather than immediate cosmetic resurfacing","Immediate elective scar revision before airway assessment","Delay ocular examination until contracture develops","Treat all burned facial tissue as definitively nonviable on first inspection"],0,
       "Major facial burns are dynamic injuries. Airway edema and inhalation injury can progress rapidly, while ocular exposure threatens vision. Tissue viability evolves, so reconstruction is staged around function, wound depth, and later contracture risk.",
       ["Correct. Life- and vision-threatening priorities precede definitive aesthetic reconstruction.","Airway compromise can become difficult to rescue after edema progresses.","Early ocular protection prevents exposure injury and missed globe damage.","Burn depth can evolve; indiscriminate early excision of potentially viable facial tissue may worsen the defect."],
       "Burn reconstruction starts with airway, eyes, and viable tissue—not scar aesthetics.",
       "What later contractures around the mouth, eyelids, and neck may require functional release and reconstruction?", "senior_management"),
]

def apply_learning_ladders_v258(challenges, concept_id_fn):
    """Append only missing v25.8 cases and attach exact canonical concept IDs."""
    existing={str(q.get("id")) for q in challenges}
    added=0
    for source in VIGNETTES_V258:
        if source["id"] in existing: continue
        q=dict(source)
        q["choices"]=list(source.get("choices") or [])
        q["why_wrong"]=list(source.get("why_wrong") or [])
        q["concept_id"]=concept_id_fn(DOMAIN,q["topic"])
        challenges.append(q); existing.add(q["id"]); added+=1
    return added
