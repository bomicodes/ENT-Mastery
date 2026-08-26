"""v20.2/v20.8 final exact matcher-gap closures for the 93-case OR registry."""

EXACT = {
    "direct-laryngoscopy-bronchoscopy": [
        "Coordinate the ventilation plan with anesthesia and obtain atraumatic direct-laryngoscopic exposure of the supraglottis and true vocal folds before passing a telescope or bronchoscope.",
        "Document the supraglottis, vocal-fold mobility/appearance, posterior commissure, and glottic aperture before instrumenting the subglottis.",
        "Pass the telescope through the cords under direct vision and inspect the subglottis circumferentially, recording stenosis, scar, edema, or structural abnormality relative to the vocal folds and cricoid.",
        "Advance through the trachea to the carina and inspect both mainstem bronchi when bronchoscopy is indicated, maintaining orientation to the posterior membranous wall.",
        "Measure any airway lesion by level, length, diameter/grade, and distance from fixed landmarks; perform calibrated leak-pressure sizing only when it changes management.",
        "Complete planned biopsy, scar division, dilation, granulation removal, or foreign-body work only after the diagnostic airway has been fully documented.",
        "Reinspect the entire treated airway for bleeding, edema, mucosal injury, loose tissue, and the actual lumen gained after intervention.",
        "Define extubation versus postoperative airway support before leaving the OR and document rescue-airway concerns for the recovery team.",
    ],
    "orbital-abscess": [
        "Review contrast CT to localize the subperiosteal/orbital collection and its sinus source, then document baseline vision, pupils, color vision, and extraocular movement before drainage.",
        "Establish endoscopic access through the diseased ethmoid/maxillary/frontal pathway needed to reach the collection while defining the skull base and lamina papyracea.",
        "Skeletonize the lamina over the abscess and remove a controlled segment of bone, keeping the periorbita intact until the intended drainage site is clearly identified.",
        "Open or elevate the periorbita at the collection, drain purulence under direct visualization, and obtain cultures before irrigation when feasible.",
        "Decompress the full subperiosteal pocket without blindly instrumenting orbital fat or injuring the medial rectus and other extraocular structures.",
        "Open the causative sinus drainage pathways adequately so persistent infected sinus disease cannot immediately re-seed the orbit.",
        "Reinspect the orbit/sinus interface for decompression and hemostasis and avoid tight nasal packing that transmits pressure to the orbit.",
        "Repeat and document postoperative vision, pupils, color vision, and extraocular movement immediately; any deterioration triggers urgent orbital-compartment reassessment.",
    ],
    "bilobed-flap": [
        "Measure the defect and design the first and second lobes around a pivot point that recruits lax adjacent skin while respecting nasal aesthetic subunits.",
        "Incise the flap and elevate it in a plane thick enough to preserve the subdermal vascular plexus throughout both lobes and the common base.",
        "Undermine the surrounding recipient and donor skin sufficiently to distribute tension and reduce pincushioning or alar distortion after rotation.",
        "Rotate the first lobe into the primary defect and the second lobe into the first-lobe donor defect without excessive torsion or narrowing at the pivot.",
        "Trim standing cutaneous deformities conservatively only after the flap is seated and perfusion is confirmed, preserving enough tissue to avoid overcorrection.",
        "Place deep dermal sutures to offload skin tension, align the nasal contour, and prevent the flap from retracting away from the defect.",
        "Close the epidermis with precise edge eversion while avoiding strangulation of the flap base or excessive tension across the alar margin.",
        "Recheck flap color, capillary refill, inset tension, standing deformity, and final nasal contour before applying a noncompressive dressing.",
    ],
}


def apply_or_procedure_sequences_v202(registry):
    applied = []
    missing = []
    for slug, seq in EXACT.items():
        op = (registry or {}).get(slug)
        if not op:
            missing.append(slug)
            continue
        op["steps"] = list(seq)
        op["sequence_status_v200"] = "procedure-specific"
        op["sequence_status_v202"] = "exact-procedure-reviewed"
        applied.append(slug)
    return {"applied": applied, "count": len(applied), "missing_registry_slugs": missing}
