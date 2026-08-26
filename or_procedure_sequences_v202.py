"""v20.2 final exact matcher-gap closures for the 93-case OR registry."""

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
