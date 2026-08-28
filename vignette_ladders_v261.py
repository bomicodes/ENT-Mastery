"""v26.1 — Facial Plastics / Trauma deliberate ladder pass 5.

Adds five exact canonical topics with complete foundation -> application ->
senior-decision ladders focused on facial reanimation, synkinesis, scar biology,
periocular safety, and staged nasal reconstruction.
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


VIGNETTES_V261 = [
    _q("v261_fpt_reanimation_fnd", "Facial Nerve Reanimation", "foundation",
       "A patient has immediate complete facial paralysis after temporal-bone trauma. What is the key first principle before choosing a reanimation procedure?",
       ["Define lesion timing, continuity/prognosis of the native nerve, and whether viable facial musculature remains", "Proceed directly to free gracilis transfer in every complete paralysis", "Wait several years before any prognostic assessment", "Treat only the brow because lower-face function does not affect outcome"], 0,
       "Facial reanimation is time- and anatomy-dependent. Acute repair/grafting, nerve transfers, and muscle transfer address different problems; the decision starts with nerve continuity, expected recovery, denervation duration, and muscle viability.",
       ["Correct. Reanimation strategy follows lesion biology and elapsed denervation time.", "Free functional muscle transfer is generally reserved for long-standing paralysis or absent viable native muscle, not every acute injury.", "Delayed assessment can forfeit useful reconstructive windows.", "Eye protection, oral competence, smile, and symmetry all matter."],
       "Before naming an operation, decide whether you are trying to rescue the native nerve, reinnervate viable muscle, or replace muscle that can no longer recover.",
       "How does denervation duration change the usefulness of nerve transfer versus free functional muscle transfer?"),
    _q("v261_fpt_reanimation_app", "Facial Nerve Reanimation", "application",
       "Ten months after proximal facial-nerve sacrifice, a patient has no meaningful recovery but still has viable mimetic muscle. Which strategy best restores neural input while the native muscles remain usable?",
       ["Consider a nerve-transfer/reinnervation strategy rather than waiting until irreversible motor end-plate loss", "Perform only static suspension because dynamic recovery is impossible before one year", "Delay all intervention for five years", "Excise the zygomaticus muscles to reduce asymmetry"], 0,
       "When spontaneous recovery is unlikely but native muscles are still viable, timely reinnervation can preserve dynamic facial movement. Options depend on deficit pattern and donor availability and may include masseteric or hypoglossal-based transfer, sometimes combined with cross-face input.",
       ["Correct. The remaining viable motor units make timely reinnervation valuable.", "Static procedures can complement reanimation but do not replace a reasonable dynamic option in this setting.", "Prolonged denervation reduces the chance that native muscles can be successfully reinnervated.", "Removing viable smile musculature worsens the reconstructive substrate."],
       "A functioning donor nerve is not enough; the recipient muscle must still be capable of responding.",
       "What are the tradeoffs between masseteric transfer, hypoglossal-based transfer, and cross-face nerve grafting?", "OR_prep"),
    _q("v261_fpt_reanimation_snr", "Facial Nerve Reanimation", "senior_decision",
       "A patient presents four years after complete flaccid facial paralysis with severe smile asymmetry and marked hemifacial atrophy. EMG and examination suggest poor native muscle viability. What is the best senior reconstructive principle?",
       ["Plan dynamic muscle replacement, often with free functional muscle transfer, while separately addressing eye protection and static support as needed", "Attempt isolated distal nerve grafting and expect the atrophic native muscles to recover", "Correct the smile only and ignore corneal exposure", "Avoid counseling about staged or combined procedures"], 0,
       "Long-standing denervation can make native mimetic muscle an unreliable target. Dynamic muscle replacement becomes appropriate, but comprehensive facial rehabilitation also addresses ocular safety, resting symmetry, oral competence, and patient priorities.",
       ["Correct. Late paralysis is often a muscle-replacement problem plus regional rehabilitation.", "A nerve graft cannot restore useful motion if the recipient motor apparatus is no longer viable.", "Corneal protection can be vision-saving and must not be subordinated to smile goals.", "Complex reanimation frequently requires staged or combined interventions and explicit expectation setting."],
       "Late facial paralysis is not one operation; reconstruct the functions the patient has lost, in the order that protects safety and maximizes meaningful movement.",
       "When would a dual-innervation strategy be considered for free functional muscle transfer?", "senior_management"),

    _q("v261_fpt_synkinesis_fnd", "Facial Synkinesis / Static-Dynamic Rehabilitation", "foundation",
       "A patient recovering from Bell palsy closes the eye involuntarily when smiling and develops tightness around the mouth. What is the most likely mechanism?",
       ["Aberrant facial-nerve regeneration causing involuntary co-contraction, consistent with synkinesis", "Persistent complete flaccid paralysis", "Isolated trigeminal neuropathy", "Normal symmetric facial movement"], 0,
       "Synkinesis follows misdirected or poorly coordinated reinnervation after facial-nerve injury. Patients may have eye-mouth coupling, platysmal overactivity, stiffness, and reduced excursion despite apparent return of tone.",
       ["Correct. Coupled movements after recovery are classic for synkinesis.", "Flaccid paralysis lacks the unwanted co-contraction described.", "Trigeminal dysfunction does not produce this pattern of facial motor coupling.", "The described movement is pathologic and asymmetric."],
       "Recovery of facial tone is not the same as recovery of selective facial movement.",
       "Why can a patient with synkinesis look stronger at rest but still have a worse smile?"),
    _q("v261_fpt_synkinesis_app", "Facial Synkinesis / Static-Dynamic Rehabilitation", "application",
       "A patient with stable postparalytic synkinesis has bothersome periocular closure during smile and platysmal hyperactivity but useful voluntary facial movement. What is the best initial treatment framework?",
       ["Facial neuromuscular retraining plus targeted chemodenervation of maladaptive muscle groups, individualized to the movement pattern", "Ablate the entire facial nerve", "Perform free gracilis transfer immediately despite useful native movement", "Observe indefinitely because synkinesis is never treatable"], 0,
       "Selective rehabilitation aims to improve motor control while reducing pathologic co-contraction. Therapy and targeted botulinum toxin are first-line tools for many patients with stable synkinesis and preserved native movement.",
       ["Correct. Treatment should preserve useful movement while reducing maladaptive coupling.", "Global denervation would sacrifice useful facial function.", "Free muscle transfer is not first-line when native muscle function is present and the principal problem is coordination.", "Synkinesis can be meaningfully improved with structured therapy and selective interventions."],
       "Treat the abnormal vector, not the whole face; preserve useful native movement whenever possible.",
       "When might selective neurectomy or myectomy enter the treatment ladder?", "OR_prep"),
    _q("v261_fpt_synkinesis_snr", "Facial Synkinesis / Static-Dynamic Rehabilitation", "senior_decision",
       "After optimized therapy and repeated targeted toxin treatment, a patient still has severe disabling ocular-oral synkinesis and platysmal tethering. Which senior principle is most appropriate before surgery?",
       ["Map which muscles and nerve branches drive the unwanted movement, confirm a stable pattern, and choose selective procedures that preserve desired smile and eye function", "Perform indiscriminate broad neurectomy because more denervation always improves symmetry", "Ignore prior toxin response because it provides no functional information", "Treat resting asymmetry only and disregard dynamic complaints"], 0,
       "Surgical treatment for refractory synkinesis is highly selective. Prior examination, therapy response, and chemodenervation can help identify pathologic contributors and predict the consequences of weakening specific muscles or branches.",
       ["Correct. Surgical selectivity is essential to avoid trading synkinesis for new weakness.", "Overly broad denervation can create flaccidity and functional loss.", "Temporary chemodenervation can serve as a useful functional preview of selective weakening.", "The defining disability in synkinesis is often dynamic and task-specific."],
       "The goal is not maximal weakening; it is maximal useful excursion with minimal unwanted co-contraction.",
       "How can botulinum-toxin response function as a reversible trial before permanent selective surgery?", "senior_management"),

    _q("v261_fpt_scar_fnd", "Scar Management", "foundation",
       "Six weeks after a cheek laceration repair, a scar is pink, firm, and mildly raised but remains within the original wound boundaries. Which diagnosis and principle best fit?",
       ["An immature hypertrophic scar; begin evidence-based conservative scar care and follow maturation", "A keloid by definition", "Recurrent skin cancer", "A mature scar that can no longer change"], 0,
       "Hypertrophic scars remain confined to the wound and often evolve during early remodeling. Initial management may include sun protection, silicone-based therapy, massage when appropriate, and selective intralesional treatment for symptomatic or progressive thickening.",
       ["Correct. Early raised scars can still remodel substantially.", "Keloids extend beyond the original wound margins.", "Nothing in the vignette suggests recurrent malignancy.", "Scar maturation continues for months and sometimes longer."],
       "Do not revise an immature scar merely because it is conspicuous early in remodeling.",
       "Which clinical features distinguish hypertrophic scar from keloid behavior?"),
    _q("v261_fpt_scar_app", "Scar Management", "application",
       "A linear facial scar is mature but widened and depressed across a relaxed skin-tension line after prior traumatic closure. What is the best reconstructive concept?",
       ["Revise the scar only after analyzing tension, orientation, contour, and underlying support, then redistribute or reduce unfavorable forces", "Simply excise and close under the same high tension", "Use intralesional steroid as the sole treatment for a depressed atrophic scar", "Laser the wound immediately without correcting mechanical causes"], 0,
       "Scar revision succeeds when the cause of poor appearance is addressed. Orientation, tension, dead space, edge eversion, contour, and missing soft tissue can matter more than merely removing the visible scar.",
       ["Correct. Mechanical and geometric analysis should guide the revision plan.", "Repeating the same closure mechanics often recreates the same widened scar.", "Steroid is useful for hypertrophic biology, not as sole treatment for depressed tissue loss.", "Resurfacing cannot reliably correct an unaddressed deep contour or tension problem."],
       "A scar is the record of wound biology plus mechanical forces; revision must change at least one of those determinants.",
       "When are Z-plasty or geometric broken-line techniques useful, and when are they unnecessary?", "OR_prep"),
    _q("v261_fpt_scar_snr", "Scar Management", "senior_decision",
       "A patient requests immediate surgical revision of a three-month-old postoperative neck scar that is red and firm but not functionally tethered. What is the best senior counseling?",
       ["Explain that continued maturation and nonsurgical optimization are appropriate unless there is a compelling functional indication, because premature revision may recreate an active scar", "Revise every visible scar at three months", "Promise complete scar elimination", "Avoid discussing pigmentation and sun exposure"], 0,
       "Scar revision timing is individualized. Without contracture, distortion, or another urgent indication, allowing maturation can improve color and firmness and makes the final defect easier to judge; adjunctive therapy can be used during this interval.",
       ["Correct. Timing should reflect scar biology and functional urgency.", "Routine early re-excision can restart the same inflammatory remodeling process.", "No procedure can guarantee an invisible scar.", "Sun protection and pigment counseling are important components of facial scar management."],
       "The best scar revision is often the one performed after the scar has declared its final problem.",
       "Which functional problems justify earlier intervention despite an immature scar?", "senior_management"),

    _q("v261_fpt_periocular_fnd", "Periocular Reconstruction", "foundation",
       "After excision of a lower-eyelid lesion, which functional priorities must guide reconstruction before cosmetic refinement?",
       ["Protect the globe, preserve eyelid closure and blink, maintain lid-margin position, and provide stable anterior/posterior lamellar support", "Maximize vertical skin tension to sharpen the lid", "Ignore the posterior lamella in full-thickness defects", "Accept ectropion if the skin color match is good"], 0,
       "Periocular reconstruction is functional reconstruction around the eye. Defect depth, canthal support, lamellar involvement, and vectors of tension determine whether the cornea remains protected and the lid stays apposed to the globe.",
       ["Correct. Ocular protection and lid mechanics come first.", "Vertical downward tension increases the risk of lower-lid retraction and ectropion.", "Full-thickness defects require restoration of both lamellae.", "A good color match does not compensate for exposure keratopathy risk."],
       "Near the eye, a cosmetically acceptable reconstruction that exposes the cornea is a failure.",
       "What structures constitute the anterior and posterior lamellae of the eyelid?"),
    _q("v261_fpt_periocular_app", "Periocular Reconstruction", "application",
       "A large lower-eyelid/cheek defect is being advanced superiorly. Which maneuver best reduces postoperative ectropion risk?",
       ["Design vectors and fixation to minimize downward pull and restore lateral canthal/lid support when needed", "Close the cheek under maximal vertical tension", "Remove additional tarsus to make closure easier", "Leave the lid unsupported because scar contraction will elevate it"], 0,
       "Lower-lid reconstruction must resist gravitational and scar-contracture forces. Wide undermining, appropriate advancement vectors, periosteal or canthal support, and thoughtful lamellar reconstruction can reduce postoperative retraction.",
       ["Correct. Vector control and structural support are central to lower-lid safety.", "Vertical tension is a common driver of ectropion.", "Unnecessary tarsal loss weakens the lid.", "Scar contraction commonly pulls the lid away from the globe rather than reliably elevating it."],
       "When reconstructing the lower lid, ask where every gram of closure tension will be transmitted.",
       "When is canthopexy or canthoplasty added to a cheek or lower-lid reconstruction?", "OR_prep"),
    _q("v261_fpt_periocular_snr", "Periocular Reconstruction", "senior_decision",
       "Two days after lower-eyelid reconstruction, a patient develops increasing pain, proptosis, tense orbit, decreased vision, and an afferent pupillary defect. What is the best immediate response?",
       ["Treat as orbital compartment syndrome with emergent decompression rather than waiting for imaging", "Observe until routine clinic follow-up", "Remove only skin sutures and reassess tomorrow", "Start scar massage"], 0,
       "Vision loss with proptosis, tense orbit, and optic-nerve dysfunction is a time-critical orbital compartment syndrome. Decompression should not be delayed for imaging when the diagnosis is clinically apparent.",
       ["Correct. This is an ocular emergency requiring immediate pressure relief and definitive evaluation.", "Observation risks irreversible optic neuropathy.", "Superficial suture removal alone does not reliably decompress the orbit.", "Scar care is irrelevant during an acute vision-threatening compartment syndrome."],
       "Postoperative periocular pain plus vision change is an emergency until proven otherwise.",
       "What bedside findings support immediate lateral canthotomy/cantholysis?", "senior_management"),

    _q("v261_fpt_forehead_fnd", "Forehead Flap / Nasal Reconstruction", "foundation",
       "A large full-thickness distal nasal defect includes skin, cartilage, and internal lining. What reconstructive principle is most important?",
       ["Reconstruct lining, structural support, and external cover as separate required layers", "Replace only the external skin because the nose will maintain shape without support", "Use a skin graft alone for every full-thickness defect", "Ignore lining because mucosa always regenerates across any defect"], 0,
       "Major nasal reconstruction is a three-layer problem. Durable lining prevents contraction, cartilage or other support maintains contour and airway, and well-vascularized external cover restores the skin envelope.",
       ["Correct. Missing one layer jeopardizes both shape and function.", "Without structural support, contraction can produce collapse and stenosis.", "A skin graft cannot replace missing lining and load-bearing cartilage in a full-thickness defect.", "Large lining defects require deliberate reconstruction and can contract severely if neglected."],
       "Think lining, framework, cover—in that order of what the defect actually lacks.",
       "Why is the paramedian forehead flap particularly useful for large distal nasal skin defects?"),
    _q("v261_fpt_forehead_app", "Forehead Flap / Nasal Reconstruction", "application",
       "A subtotal nasal tip/ala defect requires a paramedian forehead flap and cartilage support. Why is reconstruction commonly staged rather than aggressively thinned and inset in one operation?",
       ["Staging preserves vascular reliability while allowing later contouring, support refinement, and pedicle division after neovascularization", "The forehead flap has no axial blood supply", "Cartilage cannot be placed beneath a forehead flap", "Staging is cosmetic only and has no perfusion implications"], 0,
       "The paramedian forehead flap is robust, but extensive immediate thinning or complex inset can threaten distal perfusion. Staged transfer allows safe tissue survival followed by secondary thinning/contouring and pedicle division.",
       ["Correct. Staging balances reliable perfusion with eventual three-dimensional refinement.", "The flap is based on the supratrochlear vascular system.", "Cartilage grafting is commonly paired with forehead-flap reconstruction when structural support is missing.", "Perfusion and tissue conditioning are major reasons for staging."],
       "Do not sacrifice flap reliability to obtain the final contour at the first stage.",
       "How does the timing of flap thinning differ between an intermediate stage and pedicle division?", "OR_prep"),
    _q("v261_fpt_forehead_snr", "Forehead Flap / Nasal Reconstruction", "senior_decision",
       "After successful forehead-flap coverage of a large alar defect, the patient has progressive nostril narrowing because internal lining and structural alar support were insufficient. What is the best senior interpretation?",
       ["This is a three-layer reconstructive failure; restore lining and structural support rather than repeatedly debulking external cover alone", "The problem is excess blood supply and should be treated by pedicle ligation only", "Further cartilage removal will open the nostril", "External scar laser alone will reverse vestibular collapse"], 0,
       "Nasal stenosis after major reconstruction often reflects scar contraction acting on inadequate lining or framework. Durable revision must correct the missing structural components rather than treating only external bulk.",
       ["Correct. Restoring a patent internal surface and resisting contractile forces addresses the mechanism.", "Pedicle management does not correct established lining/support deficiency.", "Removing support generally worsens alar collapse.", "Laser may improve scar characteristics but cannot replace missing lining or cartilage."],
       "If a reconstructed nose contracts closed, ask which layer was never adequately restored.",
       "Which lining options can be considered for major alar or columellar defects?", "senior_management"),
]


def apply_learning_ladders_v261(challenges, concept_id_fn):
    """Append only missing v26.1 cases and attach exact canonical concept IDs."""
    existing = {str(q.get("id")) for q in challenges}
    added = 0
    for source in VIGNETTES_V261:
        if source["id"] in existing:
            continue
        q = dict(source)
        q["concept_id"] = concept_id_fn(DOMAIN, q["topic"])
        challenges.append(q)
        existing.add(q["id"])
        added += 1
    return added
