"""v25.9 — Facial Plastics / Trauma deliberate ladder pass 3.

Adds five exact canonical reconstructive topics with foundation -> application ->
senior-decision ladders emphasizing defect analysis, aesthetic-unit planning,
vascular reliability, tissue match, distortion risk, and rescue decisions.
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


VIGNETTES_V259 = [
    _q("v259_fpt_local_fnd", "Local Flap Reconstruction", "foundation",
       "A small facial defect cannot be closed primarily without distorting a nearby free margin. What is the central reconstructive advantage of a local flap over a distant graft?",
       ["It recruits adjacent vascularized tissue with similar color, thickness, and texture while redirecting closure tension", "It has no blood-supply requirements", "It always creates less scar than primary closure", "It can ignore relaxed skin-tension lines and facial subunits"], 0,
       "Local flaps borrow neighboring vascularized tissue and redistribute tension through advancement, rotation, or transposition. Their major strength is tissue match plus the ability to position tension away from vulnerable landmarks.",
       ["Correct. Adjacent vascularized tissue often gives the best match while allowing deliberate control of tension vectors.", "Local flaps still depend on a reliable random-pattern or named vascular supply.", "A flap creates additional incisions and is not automatically less scar-producing than a good primary closure.", "Incision placement and aesthetic-unit boundaries remain central to facial reconstruction."],
       "Choose a flap because its movement and tension vectors solve the defect—not because the word 'flap' sounds more reconstructive.",
       "Which nearby free margins are most vulnerable to distortion from poorly directed closure tension?"),
    _q("v259_fpt_local_app", "Local Flap Reconstruction", "application",
       "A cheek defect lies just inferior to the lower eyelid. Direct superior-inferior closure would pull the lid downward. What planning principle best reduces postoperative ectropion risk?",
       ["Design the flap so the dominant closure vector is horizontal or superolateral and avoid vertical tension on the lower lid", "Place maximal tension directly on the lid margin", "Undermine only the eyelid and leave the cheek fixed", "Accept early ectropion because all flap tension resolves"], 0,
       "Periocular reconstruction requires active management of vector forces. Supportive horizontal or superolateral tension and adequate cheek mobilization reduce downward traction on the lower eyelid.",
       ["Correct. Vector planning is as important as defect coverage near a mobile free margin.", "Direct downward tension is a classic setup for lid malposition.", "Limited mobilization can concentrate force on the eyelid rather than distribute it through the cheek.", "Scar contraction can worsen, not reliably correct, an initially poor vector."],
       "Near a free margin, think in vectors before you think in flap names.",
       "What adjunctive support might be considered when a large cheek flap still places the lower lid at risk?", "OR_prep"),
    _q("v259_fpt_local_snr", "Local Flap Reconstruction", "senior_decision",
       "A rotation flap remains tight despite reasonable undermining, and advancing it further would blanch the distal tip and distort the adjacent ala. What is the best senior-level decision?",
       ["Stop forcing the flap, reassess design and defect size, and add a second reconstructive component or choose another option rather than accepting ischemia and landmark distortion", "Increase closure tension until the defect disappears", "Thin the distal flap aggressively until it advances", "Ignore blanching if the skin edges can be sutured"], 0,
       "A reconstructive plan that only works under excessive tension is the wrong plan. Distal ischemia and free-margin distortion predict necrosis and deformity; senior judgment is recognizing when to redesign rather than forcing closure.",
       ["Correct. A second flap, graft, staged reconstruction, or revised design is preferable to a vascularly compromised, deforming closure.", "Excess tension worsens perfusion and distortion.", "Aggressive thinning can further injure the subdermal vascular plexus.", "Blanching under tension is a warning sign, not a cosmetic detail."],
       "The endpoint is a healthy, well-positioned reconstruction—not simply a closed wound.",
       "What early postoperative findings suggest venous congestion versus arterial insufficiency?", "senior_management"),

    _q("v259_fpt_mohs_fnd", "Mohs Defect Reconstruction", "foundation",
       "After Mohs surgery, what should the reconstructive surgeon determine before selecting a closure?",
       ["Defect depth, involved aesthetic subunits, exposed critical structures, free-margin risk, and whether oncologic margins are definitively clear", "Only the longest skin dimension", "Only the patient's age", "Only which flap is quickest to draw"], 0,
       "Mohs defects are reconstructive problems defined by depth, subunit location, exposed cartilage/bone/nerve, and nearby functional landmarks. Margin status and the possibility of further excision must also be understood before definitive reconstruction.",
       ["Correct. Defect analysis comes before flap selection.", "A single surface measurement does not capture depth or functional risk.", "Age affects planning but cannot define the defect.", "Technique should follow the defect, not convenience."],
       "Do not name the flap until you can describe the defect in three dimensions.",
       "Why can a seemingly small alar or eyelid Mohs defect be more demanding than a larger convex cheek defect?"),
    _q("v259_fpt_mohs_app", "Mohs Defect Reconstruction", "application",
       "A full-thickness alar Mohs defect includes skin, cartilage support, and internal lining. Which reconstructive concept is most important?",
       ["Replace each missing layer—lining, structural support, and external cover—rather than resurfacing skin alone", "Use a thin skin graft alone because alar support will regenerate", "Close the nostril partially to reduce defect size", "Delay structural support until collapse develops"], 0,
       "Full-thickness nasal defects require layered reconstruction. Failure to restore lining or cartilage support can produce contraction, alar retraction, vestibular stenosis, and external valve collapse even if the skin initially looks acceptable.",
       ["Correct. Three-layer nasal reconstruction preserves both airway and contour.", "Skin alone cannot restore the structural framework of the ala.", "Intentional nostril narrowing sacrifices function rather than reconstructing it.", "Secondary support after scar contraction is more difficult than restoring framework during primary reconstruction."],
       "A nasal reconstruction can look closed and still be functionally incomplete.",
       "Which cartilage donor sites are commonly considered for alar structural grafting?", "OR_prep"),
    _q("v259_fpt_mohs_snr", "Mohs Defect Reconstruction", "senior_decision",
       "A large central nasal Mohs defect spans most of one aesthetic subunit but leaves a narrow strip of distorted residual skin. What principle may improve the final contour and scar placement?",
       ["Consider completing the aesthetic subunit when appropriate so scars fall at subunit borders and reconstruction restores a coherent contour", "Always preserve every millimeter of residual skin regardless of distortion", "Place the final scar across the most convex visible surface", "Use maximal tension to keep the reconstruction single-stage"], 0,
       "For selected large nasal defects, the subunit principle can justify excising a small amount of compromised residual skin so the entire subunit is reconstructed with scars hidden at natural boundaries. It is a planning principle, not a mandate for every defect.",
       ["Correct. In the right defect, replacing the subunit can produce a more natural contour than patching an irregular remnant.", "Preservation is valuable, but a tiny malpositioned remnant can worsen contour and scar visibility.", "Convex central scars are usually more conspicuous than scars at natural borders.", "Forcing a one-stage high-tension closure can sacrifice perfusion and shape."],
       "Aesthetic-subunit reconstruction is selective: use it when it improves contour and scar camouflage, not as dogma.",
       "When would preserving residual subunit skin be preferable to completing the subunit?", "senior_management"),

    _q("v259_fpt_bilobed_fnd", "Bilobed Flap", "foundation",
       "Why is a bilobed flap useful for selected small-to-moderate distal nasal defects?",
       ["It transfers nearby nasal skin through two sequential transposition lobes, distributing tension into more mobile adjacent tissue", "It provides internal nasal lining and cartilage automatically", "It has no risk of pincushioning or trapdoor deformity", "It is designed without regard to the relaxed skin-tension lines or nasal subunits"], 0,
       "The bilobed flap recruits adjacent dorsal/sidewall skin for distal nasal defects. Two lobes allow the primary defect to borrow tissue from a progressively more mobile area while spreading closure tension.",
       ["Correct. The second lobe helps close the donor defect created by movement of the first.", "A bilobed flap is cutaneous coverage; full-thickness defects may still need lining and support.", "Pincushioning, standing-cone deformity, and distortion remain recognized risks.", "Orientation and tissue laxity strongly influence the result."],
       "Bilobed means two-step tissue recruitment, not two independent flaps.",
       "Which nasal regions usually provide more recruitable skin than the rigid lower third?"),
    _q("v259_fpt_bilobed_app", "Bilobed Flap", "application",
       "A bilobed flap for an alar-adjacent defect is designed with excessive total rotation and the primary lobe under tension. Which complication becomes more likely?",
       ["Alar displacement plus pincushioning/trapdoor deformity from poorly distributed tension and scar contraction", "Spontaneous cartilage regeneration", "Improved external nasal valve support", "Elimination of all donor-site scars"], 0,
       "Bilobed design is sensitive to lobe size, arc of rotation, tissue thickness, and vector. Excess rotation or tension can distort the ala and exaggerate trapdoor/pincushion contour.",
       ["Correct. The flap can successfully cover the defect while still producing an unacceptable nasal shape.", "Cutaneous transposition does not regenerate missing cartilage.", "A poorly directed cutaneous flap can worsen, not reliably strengthen, the external valve.", "The technique necessarily creates additional incisions."],
       "A bilobed flap fails cosmetically when the geometry solves coverage but ignores contour and vector.",
       "How can wide undermining and thoughtful lobe sizing reduce tension and pincushioning?", "OR_prep"),
    _q("v259_fpt_bilobed_snr", "Bilobed Flap", "senior_decision",
       "A distal nasal defect is too large and deep for a bilobed flap without major alar distortion and flattening of the nasal tip. What is the best senior decision?",
       ["Choose a reconstruction that better matches the defect—such as a staged interpolated flap or other regional option with structural support as needed—rather than stretching the bilobed indication", "Make both lobes progressively smaller and close under extreme tension", "Excise additional normal ala until the bilobed flap fits", "Accept valve collapse because scar revision is easier later"], 0,
       "Bilobed flaps have a useful but finite indication. Large or deep distal nasal defects may require more tissue, better vascular reliability, staged transfer, and separate structural grafting.",
       ["Correct. Technique selection should escalate with defect size, depth, and subunit loss.", "Undersized lobes increase tension and necrosis/distortion risk.", "Unnecessary alar sacrifice worsens the functional defect.", "Preventing airway collapse is preferable to reconstructing scarred collapse later."],
       "Do not let a familiar flap become a solution looking for a defect.",
       "Which defect characteristics push you toward a paramedian forehead flap instead of a bilobed flap?", "senior_management"),

    _q("v259_fpt_cervico_fnd", "Cervicofacial Flap", "foundation",
       "A large lateral cheek cutaneous defect requires regional tissue recruitment. What makes a cervicofacial advancement/rotation flap attractive?",
       ["It mobilizes broad adjacent cheek and neck skin with good color/texture match to resurface a large defect", "It provides rigid mandibular reconstruction", "It is a free flap requiring microvascular anastomosis", "It eliminates risk to the lower eyelid and facial nerve"], 0,
       "Cervicofacial flaps recruit a wide skin-soft tissue reservoir from the cheek and neck. They can cover large lateral facial defects with favorable tissue match while avoiding a distant donor site.",
       ["Correct. The broad regional reservoir is the principal reconstructive advantage.", "The flap supplies soft-tissue coverage, not load-bearing mandibular bone.", "It is a regional flap and does not inherently require microvascular transfer.", "Ectropion, distal ischemia, hematoma, and nerve-related complications still require careful planning."],
       "The cervicofacial flap is powerful because it recruits a region, not because it ignores regional anatomy.",
       "Which cheek and neck tissue planes can be used for elevation, and how do they affect vascularity and nerve risk?"),
    _q("v259_fpt_cervico_app", "Cervicofacial Flap", "application",
       "After a large infraorbital cheek defect, a cervicofacial flap would place substantial inferior pull on the lower eyelid. What modification is most important?",
       ["Mobilize sufficiently to minimize vertical tension and provide lateral/superior fixation or eyelid support when needed", "Anchor the flap to the lower lid margin under tension", "Avoid undermining so the flap remains tight", "Resect the lower lid to prevent ectropion"], 0,
       "Large cheek advancement can transmit downward force to the lower lid. Wide mobilization plus fixation/support to stable lateral or superior structures helps redirect the vector and reduce ectropion.",
       ["Correct. The reconstruction must protect lid position while closing the cheek.", "Direct traction on the lid margin increases malposition risk.", "Insufficient mobilization concentrates tension at the eyelid.", "Removing normal eyelid tissue worsens the functional defect."],
       "A successful cheek flap that produces ectropion is not a successful reconstruction.",
       "Which patient factors—such as baseline lid laxity—should lower your threshold for prophylactic lid support?", "OR_prep"),
    _q("v259_fpt_cervico_snr", "Cervicofacial Flap", "senior_decision",
       "On postoperative day 1, the distal cervicofacial flap is dusky and swollen with brisk dark bleeding on pinprick, while the pedicle is compressed by a tense hematoma. What is the priority?",
       ["Urgently relieve the mechanical cause—evacuate the hematoma and restore unobstructed perfusion—rather than observing progressive congestion", "Apply tighter dressings to reduce swelling", "Wait several days because all venous congestion resolves", "Debride the entire flap immediately without assessing reversible causes"], 0,
       "Early flap compromise may be reversible when caused by hematoma, pedicle kinking, or excessive tension. Venous congestion with a tense collection requires prompt source control before microvascular thrombosis and tissue loss become irreversible.",
       ["Correct. Time-sensitive correction of a reversible mechanical problem can salvage regional tissue.", "More compression can further impair venous outflow and arterial inflow.", "Persistent congestion can progress to thrombosis and necrosis.", "Immediate total debridement is premature when a correctable cause is evident."],
       "A threatened flap is an anatomic problem until proven otherwise: look for tension, twist, compression, and hematoma.",
       "How do the bedside appearances of venous congestion and arterial insufficiency differ?", "senior_management"),

    _q("v259_fpt_graft_fnd", "Skin Graft Selection", "foundation",
       "What is the main tradeoff between split-thickness and full-thickness skin grafts in facial reconstruction?",
       ["Split-thickness grafts take more readily on marginal beds but contract and mismatch more; full-thickness grafts often match face better and contract less but require a well-vascularized bed", "Full-thickness grafts survive on avascular bone without periosteum", "Split-thickness grafts never contract", "Donor-site characteristics do not affect facial graft appearance"], 0,
       "Graft thickness changes metabolic demand, contraction, durability, donor-site healing, and color/texture match. Facial defects often favor full-thickness grafts when the recipient bed can support them.",
       ["Correct. Thickness selection is a balance between take and long-term aesthetic/contracture behavior.", "Bare cortical bone without periosteum is a poor graft bed.", "Secondary contraction is a recognized limitation of thinner grafts.", "Donor-site color, thickness, adnexal quality, and sun exposure influence the final match."],
       "Skin-graft choice is a recipient-bed decision and an aesthetic-match decision at the same time.",
       "Which facial donor sites commonly provide useful full-thickness skin with favorable color and thickness match?"),
    _q("v259_fpt_graft_app", "Skin Graft Selection", "application",
       "A nasal sidewall defect has exposed healthy perichondrium and is too superficial to justify a flap. Which option is often reasonable when contour is acceptable and tissue match is prioritized?",
       ["A carefully selected full-thickness skin graft with meticulous bed contact and bolster/immobilization", "A split-thickness graft placed over active hematoma", "A skin graft suspended above the bed so fluid can drain underneath", "A graft over bare avascular cartilage after removing all perichondrium"], 0,
       "A full-thickness graft can be effective on a well-vascularized nasal bed when three-dimensional contour does not require bulk or structural support. Close graft-bed contact and prevention of hematoma/seroma are critical for plasmatic imbibition and inosculation.",
       ["Correct. Appropriate bed, tissue match, and immobilization make a graft a strong option for selected superficial defects.", "Hematoma separates the graft from its nutrient bed and threatens take.", "Dead space under a graft impairs revascularization.", "Removing vascularized perichondrium creates a worse recipient bed."],
       "A graft survives by contact; blood or dead space between graft and bed is the enemy.",
       "What are the early phases of graft take before mature neovascularization?", "OR_prep"),
    _q("v259_fpt_graft_snr", "Skin Graft Selection", "senior_decision",
       "A patient has a deep alar defect with exposed unsupported cartilage and a high risk of nostril retraction. Why is a skin graft alone a poor definitive choice?",
       ["It may resurface the wound but cannot replace missing structural support, and secondary contraction can worsen alar retraction or vestibular stenosis", "Skin grafts are contraindicated anywhere on the nose", "Full-thickness grafts always become infected on cartilage", "A graft provides more structural rigidity than cartilage"], 0,
       "Reconstruction must replace what is missing. When structural support is absent or contracture would deform a free margin, cartilage grafting and/or flap reconstruction may be required in addition to skin coverage.",
       ["Correct. Coverage without framework can trade an open wound for a functional nasal deformity.", "Skin grafts are useful for many appropriately selected nasal defects.", "Infection is not inevitable; the core issue here is support and contraction.", "Skin provides coverage, not cartilage-like rigidity."],
       "Do not confuse resurfacing with reconstruction when a defect has lost support.",
       "Which nasal subunits are least forgiving of secondary contraction because they border the external nasal valve?", "senior_management"),
]


def apply_learning_ladders_v259(challenges, concept_id_fn):
    """Append only missing v25.9 cases and attach exact canonical concept IDs."""
    existing = {str(q.get("id")) for q in challenges}
    added = 0
    for source in VIGNETTES_V259:
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
