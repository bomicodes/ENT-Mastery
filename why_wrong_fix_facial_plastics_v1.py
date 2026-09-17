"""
why_wrong_fix_facial_plastics_v1.py

Replaces the generic/duplicate `why_wrong` text for the 31 Facial Plastics /
Trauma items flagged by audit_question_quality.py (GENERIC_WHY_WRONG). Each
wrong choice gets its own specific clinical reasoning. The correct choice's
own slot is "Correct." to match schema.

Usage: same pattern as why_wrong_fix_general_ent_v1.py.

    from why_wrong_fix_facial_plastics_v1 import apply_why_wrong_fix_facial_plastics_v1
    WHY_WRONG_FIX_FACIAL_PLASTICS_V1 = apply_why_wrong_fix_facial_plastics_v1(runtime_entry.data)
"""

WHY_WRONG_FIXES = {
    "v141_fpt_01": [
        "Restoring occlusion is the primary functional goal of mandible fracture "
        "repair; plating without first confirming correct occlusal relationship risks "
        "fixing the fracture in a malaligned position.",
        "Correct.",
        "Not every tooth in a fracture line needs removal; extraction decisions are "
        "individualized based on infection, mobility, and whether the tooth interferes "
        "with stable reduction, not applied universally.",
        "A displaced fracture with malocclusion and infection will not resolve "
        "without intervention; observation would leave the patient with persistent "
        "malocclusion and untreated infection.",
    ],
    "v141_fpt_02": [
        "Once nasal bones have consolidated, closed reduction becomes unreliable "
        "because the bones can no longer be manually repositioned without "
        "refracturing; it is not equally effective weeks later as it would be "
        "acutely.",
        "Correct.",
        "Effective treatment options exist, including delayed septorhinoplasty with "
        "osteotomies; stating no treatment is possible is inaccurate.",
        "Turbinate reduction addresses a different structure (the turbinates) and "
        "does not correct the fixed bony deformity of the nasal fracture itself.",
    ],
    "v141_fpt_03": [
        "The paramedian forehead flap is specifically based on a named vascular "
        "pedicle (the supratrochlear vessels); stating it has no pedicle is factually "
        "incorrect and contradicts the premise of the question.",
        "Cartilage grafts used in nasal reconstruction require vascularized "
        "soft-tissue coverage to survive and integrate; this statement ignores a "
        "fundamental principle of reconstructive surgery.",
        "Correct.",
        "Staging exists specifically to protect neovascularization and manage the "
        "tissue transition from pedicled flap to healed reconstruction; there is a "
        "clear biologic rationale.",
    ],
    "v141_fpt_04": [
        "Waiting years allows distal muscle to atrophy and lose reinnervation "
        "potential; timely nerve repair, while the distal branches and muscle are "
        "still viable, offers the best chance of restoring native movement.",
        "A static sling only provides passive symmetry at rest and does not restore "
        "active, dynamic facial movement, which nerve grafting can achieve here since "
        "distal branches remain viable.",
        "Correct.",
        "Botulinum toxin further weakens muscle activity and is used to manage "
        "overactivity or synkinesis, not to address an acute nerve transection needing "
        "repair; it would not restore function to the paralyzed side.",
    ],
    "v141_fpt_05": [
        "Removing more cartilage from an already narrowed middle vault would further "
        "reduce internal valve support and worsen the collapse, the opposite of the "
        "needed correction.",
        "Turbinate reduction addresses a different structure (the inferior "
        "turbinate) and does not address the structural middle-vault collapse causing "
        "internal valve narrowing.",
        "Nasal steroids treat mucosal inflammation and have no effect on a fixed "
        "structural cartilage deficiency causing valve collapse.",
        "Correct.",
    ],
    "v141_fpt_06": [
        "BPPV is an inner-ear positional vertigo disorder entirely unrelated to "
        "frontal sinus outflow obstruction.",
        "Otosclerosis is a middle-ear conductive hearing loss condition from stapes "
        "fixation, unrelated to frontal sinus drainage or trapped mucosa.",
        "Correct.",
        "A parotid fistula involves salivary leakage from the parotid gland, an "
        "entirely different anatomic structure and mechanism unrelated to obstructed "
        "frontal sinus outflow.",
    ],
    "v142_fpt_01": [
        "Random full-thickness excision of tip tissue is destructive and imprecise; "
        "it does not represent the careful, planned dissection that provides safe "
        "exposure while preserving structure.",
        "Circumferential devascularization of the columella would compromise blood "
        "supply to the very tissue being elevated, risking necrosis rather than "
        "preserving vascularity.",
        "Extensive subperiosteal dissection across the entire upper lip is "
        "unnecessary for tip exposure and would cause excessive, unrelated "
        "soft-tissue disruption beyond what open rhinoplasty requires.",
        "Correct.",
    ],
    "v142_fpt_03": [
        "A skin graft alone lacks the structural rigidity needed to support the "
        "eyelid margin and posterior lamella; it cannot replace the tarsoconjunctival "
        "support required for a large full-thickness defect.",
        "Correct.",
        "Leaving the tarsal (structural support) defect unaddressed risks lid "
        "instability, malposition, and corneal exposure; posterior lamellar support "
        "must be restored.",
        "Tightening the upper lip does not address a lower eyelid defect and would "
        "not restore missing tissue or structural support to the affected lid.",
    ],
    "v142_fpt_04": [
        "Enlarging the perforation would worsen the defect and symptoms; this is the "
        "opposite of what is needed before considering closure.",
        "A spreader graft addresses internal nasal valve support, an entirely "
        "different structural problem from a septal perforation; it does not address "
        "the mucosal defect or its cause.",
        "Ongoing causes like cocaine use or vasculitis actively undermine tissue "
        "healing and graft/flap survival; ignoring them would set up any attempted "
        "repair to fail, since the underlying destructive process would continue.",
        "Correct.",
    ],
    "v143_fpt_01": [
        "Correct.",
        "Closing the skin without assessing for duct or nerve injury may permanently "
        "miss a repairable injury, since function testing and clear anatomic "
        "identification become much harder once swelling and healing progress.",
        "Ligating every facial nerve branch would create permanent, iatrogenic "
        "facial paralysis; this is the opposite of the goal, which is to identify and "
        "repair any injured nerve, not sacrifice healthy ones.",
        "Excising the parotid gland is a major, disfiguring operation entirely "
        "disproportionate to a laceration; the appropriate approach is to evaluate and "
        "repair the duct if injured, not remove the whole gland.",
    ],
    "v143_fpt_02": [
        "Cranialization is reserved for more severe injuries (typically involving "
        "posterior table/dural injury), not an isolated anterior-table fracture with "
        "intact posterior table and patent outflow tract; it is disproportionately "
        "aggressive here.",
        "Correct.",
        "The anterior-table displacement is causing a visible contour deformity that "
        "affects the patient's appearance; ignoring it fails to address the primary "
        "problem this fracture pattern presents.",
        "Obliteration is reserved for situations with outflow tract compromise or "
        "other specific indications; sacrificing a patent, functioning sinus "
        "unnecessarily removes the option to preserve normal sinus function.",
    ],
    "v143_fpt_03": [
        "Correct.",
        "Fixing fragments opportunistically without a global sequencing plan risks "
        "losing the overall facial width, height, and projection relationships needed "
        "for a correct final result, since each segment's position depends on the "
        "others.",
        "Occlusion is a key reference point that should guide reduction throughout "
        "the case; waiting until all plates are placed to check it risks discovering a "
        "malocclusion only after fixation is already complete.",
        "The nasal bones alone do not provide a reliable reference for overall "
        "facial width, height, or mandibular position in panfacial trauma; multiple "
        "stable buttresses and dental occlusion are needed as reference points.",
    ],
    "v143_fpt_04": [
        "Correct.",
        "Ignoring the canthal-bearing fragment leaves the medial canthal tendon "
        "unsupported in an unstable position, which will result in telecanthus and a "
        "widened intercanthal distance regardless of how well the nasal bones "
        "themselves are reduced.",
        "Resecting the medial canthal tendons removes the very structure needed for "
        "normal eyelid position and intercanthal distance; this would create, not "
        "correct, the deformity this reconstruction aims to prevent.",
        "Isolated orbital floor grafting addresses a different structural problem "
        "(orbital volume/floor support) and does not address the unstable "
        "canthal-bearing bone fragment, which is the critical issue in this NOE "
        "pattern.",
    ],
    "v143_fpt_05": [
        "A columellar strut supports tip projection and stability, not the internal "
        "nasal valve or middle vault width; it does not address this specific "
        "structural problem.",
        "Correct.",
        "An auricular composite graft to the lobule addresses alar rim or lobule "
        "contour issues, an entirely different anatomic region and problem from "
        "internal valve narrowing at the middle vault.",
        "Temporalis fascia is typically used for camouflage or soft-tissue coverage, "
        "not for providing rigid structural support to widen the internal nasal "
        "valve.",
    ],
    "v147_fp_01": [
        "Nasal appearance is influenced by its relationship to surrounding facial "
        "features (chin, facial thirds, profile), not length alone; focusing on a "
        "single linear measurement misses the relational nature of facial aesthetics.",
        "Promising a specific look based on another person's features ignores the "
        "patient's own unique facial anatomy, skin quality, and what is actually "
        "surgically achievable for them.",
        "Standardized photography is an essential tool for objective preoperative "
        "analysis and surgical planning; ignoring it removes valuable documentation "
        "and planning information.",
        "Correct.",
    ],
    "v147_fp_02": [
        "Correct.",
        "Overfilling the nasolabial crease without addressing the underlying volume "
        "loss elsewhere in the midface can create an unnatural contour and does not "
        "correct the actual mechanism (skeletal/fat volume loss) causing the deep "
        "fold.",
        "Filler injection carries real risk of vascular occlusion and tissue "
        "necrosis if injected without respecting vascular anatomy; ignoring this is a "
        "significant safety hazard, not an acceptable treatment principle.",
        "Resurfacing treats skin surface quality (texture, fine lines) but does not "
        "restore lost facial volume, which is a separate problem requiring volumizing "
        "treatment.",
    ],
    "v147_fp_03": [
        "Removing more cartilage would further weaken structural support, worsening "
        "rather than correcting the retraction and collapse caused by insufficient "
        "support after the prior surgery.",
        "Correct.",
        "Cauterizing the vestibule would create additional scarring and tissue "
        "damage, worsening contracture and stenosis rather than restoring normal "
        "lining and support.",
        "Severe fixed stenosis will not resolve without correcting the underlying "
        "structural and lining deficiency; indefinite observation leaves the patient "
        "with ongoing functional obstruction.",
    ],
    "v147_fp_04": [
        "Closing under excessive tension without addressing the cartilage framework "
        "loss risks wound breakdown, distortion, and failure to restore normal ear "
        "contour and projection.",
        "Correct.",
        "Removing the remaining healthy ear is a drastic, unnecessary step when a "
        "defined defect with a healthy surrounding sulcus can be reconstructed; this "
        "would create a much larger problem than needed.",
        "A thick muscle flap would create a bulky, poorly contoured result over the "
        "delicate helical framework; thin, pliable tissue is needed to reveal the "
        "underlying cartilage contour, not bulky muscle.",
    ],
    "v147_fp_05": [
        "The bilobed flap specifically requires careful geometric planning (pivot "
        "point, arc of rotation, lobe sizing) to work well; poor planning is a known "
        "cause of complications like trapdoor deformity.",
        "The bilobed flap is specifically useful for small-to-moderate nasal "
        "defects; it is not universally ideal for every cheek defect, which may be "
        "better served by other reconstructive options depending on size and "
        "location.",
        "Pincushioning (trapdoor deformity) is a recognized risk of the bilobed "
        "flap, particularly with oversizing or poor design; the flap does not "
        "eliminate this risk.",
        "Correct.",
    ],
    "v147_fp_06": [
        "The cervicofacial flap is itself a local/regional advancement flap, an "
        "alternative to free tissue transfer, not something that requires it; this "
        "statement misdescribes the technique.",
        "Correct.",
        "The cervicofacial flap is a soft-tissue (skin/subcutaneous) flap; it does "
        "not provide vascularized bone, which would require a different type of flap "
        "such as a free osseous flap.",
        "Larger defects place more tension on flap closure, and factors like "
        "lower-lid position and distal perfusion become more significant; tension is "
        "not automatically eliminated regardless of defect size.",
    ],
    "v147_fp_07": [
        "Synkinesis results from aberrant nerve regeneration after the acute injury "
        "has already resolved; steroids treat acute inflammation and have no "
        "mechanism to correct this chronic aberrant reinnervation pattern.",
        "A static sling addresses resting symmetry and does not correct the "
        "dynamic, aberrant co-contraction pattern (eye closing with smiling) that "
        "defines synkinesis.",
        "Correct.",
        "Effective treatments exist, including neuromuscular retraining and "
        "targeted botulinum toxin; stating no treatment exists is inaccurate and "
        "denies the patient beneficial options.",
    ],
    "v147_fp_08": [
        "Correct.",
        "Placing a low, juvenile hairline in a patient with ongoing androgenetic "
        "alopecia risks an unnatural appearance as the native hairline continues to "
        "recede around the transplanted zone over time.",
        "Because androgenetic alopecia is progressive, failing to anticipate future "
        "native hair loss risks a result that looks increasingly unnatural or patchy "
        "as untreated areas continue to thin.",
        "Harvesting beyond the safe donor zone risks visible scarring and a "
        "depleted donor area, since donor hair is a finite, non-renewable resource "
        "that must be planned conservatively.",
    ],
    "v147_fp_09": [
        "Tension direction, not incision length alone, determines whether a flap "
        "will distort a nearby free margin like the eyelid; prioritizing the shortest "
        "incision while ignoring tension vector risks causing ectropion.",
        "This is an overstatement -- local flaps from adjacent facial skin generally "
        "provide superior color and texture match compared to skin grafts, which is "
        "why local tissue is often preferred when feasible.",
        "Correct.",
        "Ignoring relaxed skin tension lines produces scars that are more visible "
        "and can create unfavorable tension vectors; respecting these lines is a "
        "basic principle of favorable flap design and scar camouflage.",
    ],
    "v147_fp_10": [
        "Correct.",
        "The maxilla is not involved in bilateral subcondylar fracture mechanics; it "
        "does not acutely lengthen as a consequence of mandibular condylar injury.",
        "Subcondylar fractures do not cause tongue paralysis; the tongue's motor "
        "innervation (hypoglossal nerve) is unrelated to the temporomandibular joint "
        "or condylar height.",
        "Teeth do not erupt acutely in response to trauma; this is not a "
        "physiologically plausible mechanism for a rapidly developing open bite after "
        "facial injury.",
    ],
    "v147_fp_11": [
        "Correct.",
        "A pre-Mohs photo shows the original lesion but not the actual final defect "
        "after resection; the reconstructive surgeon needs to verify the true "
        "post-resection defect, not rely solely on a photo taken before surgery.",
        "Assuming margins are positive without confirmation could lead to either "
        "premature reconstruction before clearance is verified or unnecessarily "
        "delayed reconstruction if margins are actually clear.",
        "Nasal defects often involve multiple layers (lining, cartilage support, "
        "external cover); ignoring lining and cartilage loss risks an incomplete "
        "reconstruction plan that fails to restore full nasal structure and function.",
    ],
    "v147_fp_12": [
        "This patient's deformity is specifically an underdeveloped antihelical "
        "fold with normal conchal depth; addressing the concha alone would not "
        "correct the actual anatomic cause of the prominent ear in this case.",
        "Lobule prominence is a separate, distinct deformity from an underdeveloped "
        "antihelical fold; removing the lobule would not address this patient's "
        "actual anatomic problem and would create an unrelated change.",
        "Correct.",
        "Mastoidectomy is an entirely unrelated middle-ear/mastoid surgical "
        "procedure with no role in cosmetic ear-shape correction.",
    ],
    "v147_fp_13": [
        "Blind cartilage resection without understanding the interconnected tip "
        "support mechanism risks unpredictable, uncontrolled changes to both rotation "
        "and projection, potentially worsening the very problem being treated.",
        "Correct.",
        "Rotation and projection are mechanically linked through the tip support "
        "system, not independent; many maneuvers affect both simultaneously, "
        "sometimes in opposing directions, which is exactly why understanding this "
        "relationship matters.",
        "Maximally shortening the caudal septum in every case can over-rotate the "
        "tip and cause unwanted loss of septal support; this is not appropriate as a "
        "universal maneuver for every patient's individual anatomy and goals.",
    ],
    "v147_fp_14": [
        "Hypertrophic scars can improve with time and conservative management; "
        "immediate wide excision in every case is overly aggressive and skips less "
        "invasive, effective first-line options.",
        "Correct.",
        "Radiation is not routine first-line therapy for a benign hypertrophic scar "
        "and carries risks disproportionate to this generally self-limited, "
        "improvable condition.",
        "Symptomatic hypertrophic scars often respond to conservative measures "
        "(silicone, pressure, steroid injection); ignoring them permanently forgoes "
        "effective treatment options that could meaningfully improve the scar's "
        "appearance and symptoms.",
    ],
    "v147_fp_15": [
        "All skin grafts, including full-thickness grafts, require a vascularized "
        "recipient bed to survive via imbibition and subsequent revascularization; a "
        "graft cannot survive without one.",
        "Correct.",
        "Bare cortical bone without periosteum lacks the vascularity needed to "
        "support a skin graft; grafts require a vascularized bed, which exposed bone "
        "without periosteum does not provide.",
        "Bolster (tie-over) dressings are commonly used to immobilize full-thickness "
        "skin grafts and promote adherence to the recipient bed during the critical "
        "early healing period; grafts do often need this fixation.",
    ],
    "v147_fp_16": [
        "Masseteric nerve transfer is a dynamic reanimation technique aimed at "
        "restoring active movement, which requires functional muscle and nerve "
        "regeneration time; it does not address this frail patient's need for a "
        "static solution, and dynamic procedures were specifically excluded here.",
        "Tongue-base reduction addresses airway obstruction from tongue base "
        "tissue, an entirely unrelated procedure with no role in correcting eyelid "
        "malposition.",
        "Correct.",
        "Septoplasty corrects nasal septal deviation and has no relationship to "
        "eyelid position or facial paralysis-related ectropion.",
    ],
    "v147_fp_17": [
        "Hair color has no clinical relevance to facial trauma assessment or any "
        "functional/neurologic status that needs documentation before sedation.",
        "Correct.",
        "Nasal airflow alone does not capture critical baseline findings like "
        "vision, eye movements, facial nerve function, or occlusion that could be "
        "permanently lost or impossible to assess once the patient is intubated and "
        "sedated.",
        "Blood pressure alone is a vital sign relevant to overall stabilization but "
        "does not substitute for the specific baseline neurologic, ocular, and facial "
        "function exam findings that must be documented before sedation obscures "
        "them.",
    ],
}


def apply_why_wrong_fix_facial_plastics_v1(data_module):
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
        print(f"why_wrong_fix_facial_plastics_v1: {len(missing)} ids not found: {missing}")
    return updated
