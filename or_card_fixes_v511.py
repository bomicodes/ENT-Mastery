"""v51.1 OR Tomorrow card repairs found while writing the anatomy-by-case pages.

- tegmen-repair: its steps and landmarks had been copied from the endoscopic nasal CSF-leak card.
  Replaced with a transmastoid / middle-fossa tegmen repair sequence and temporal-bone landmarks.
- palatoplasty, tep, microflap, rrp-debridement: landmarks were a generic laryngeal list.
- lingual-tonsillectomy: steps described palatine tonsillectomy. Replaced with tongue-base steps.
- tep, microflap, rrp-debridement: an emergency-rescue paragraph (dislodged prosthesis / airway fire)
  had been inserted as step 1. It is kept, but moved to the end and labelled as a rescue step so the
  operative sequence reads in order.
"""

TEGMEN_STEPS = [
    "Confirm the diagnosis and map the defect before incision: beta-2 transferrin (or beta-trace) on the fluid, high-resolution temporal-bone CT for the tegmen tympani/mastoideum defect(s), and MRI when an encephalocele or meningoencephalocele is suspected. Look for multiple defects and for elevated intracranial pressure (obesity, empty sella, papilledema) that predisposes to spontaneous leaks and recurrence.",
    "Choose the approach from defect site and size: transmastoid for small, posterior or lateral tegmen mastoideum defects; middle-fossa craniotomy for large, multiple or anterior (tegmen tympani) defects and for encephaloceles; a combined transmastoid/middle-fossa approach when exposure from below alone is inadequate.",
    "Transmastoid: perform a cortical mastoidectomy, thin the tegmen to identify the defect and any herniated dura/brain, and protect the ossicular chain (incus body and short process in the attic) and the facial nerve. Avoid drilling on exposed dura.",
    "Middle fossa: through a temporal craniotomy above the zygomatic root, elevate the temporal lobe dura extradurally from posterior to anterior, identify the defect(s), and protect the greater superficial petrosal nerve and a possibly dehiscent geniculate ganglion anteromedially and the middle meningeal artery at the foramen spinosum.",
    "Manage herniated tissue: amputate non-functional herniated brain/gliotic tissue at the defect with bipolar cautery rather than forcing it back, and repair dural tears primarily or with graft.",
    "Reconstruct in layers with broad overlap: an intracranial (dural-side) fascia or dural-substitute layer, a rigid layer (bone, cartilage or calvarial graft) across the bony defect, and an extracranial fascia/temporalis or pedicled flap layer, with tissue sealant as an adjunct.",
    "Close and plan aftercare: restore the mastoid/middle-ear space as needed, consider lumbar drainage selectively, and evaluate and treat elevated intracranial pressure (weight loss, acetazolamide, neuro-ophthalmology) to lower recurrence risk.",
]
TEGMEN_LANDMARKS = ["tegmen tympani / tegmen mastoideum", "middle cranial fossa dura and temporal lobe",
                    "incus body and short process in the attic", "tympanic and mastoid facial nerve",
                    "arcuate eminence and greater superficial petrosal nerve (middle fossa)",
                    "middle meningeal artery at the foramen spinosum", "sigmoid sinus and sinodural angle"]

LINGUAL_STEPS = [
    "Confirm the indication and target: tongue-base or lingual-tonsil obstruction confirmed on exam and DISE (or recurrent lingual tonsillitis), with a plan that fits a multilevel OSA strategy; review imaging if the lingual artery or a vascular anomaly is a concern.",
    "Secure the airway with an anesthesia plan for a shared, potentially edematous airway (nasotracheal or oral intubation as agreed) and protect the teeth and lips.",
    "Expose the tongue base with suspension laryngoscopy, a tongue-base retractor or the TORS setup, using a 0- or 30-degree endoscope for visualization of the vallecula and lateral lingual tonsil.",
    "Remove lingual tonsil tissue from the midline outward with coblation, laser, microdebrider or TORS, staying superficial to the intrinsic tongue musculature and preserving the vallecular mucosa and epiglottis.",
    "Respect the lateral limit: the dorsal lingual and lingual arteries and the hypoglossal nerve lie deep and lateral, so limit depth and lateral extent and stop at the glossotonsillar sulcus.",
    "Achieve meticulous hemostasis and inspect the vallecula and epiglottis; avoid circumferential raw surfaces that predispose to scarring.",
    "Plan extubation and monitoring for airway edema and bleeding (steroids per protocol, monitored setting, multimodal analgesia), and reassess OSA outcome objectively after healing.",
]
LINGUAL_LANDMARKS = ["foramen cecum and circumvallate papillae (anterior limit)", "vallecula and lingual surface of the epiglottis",
                     "glossoepiglottic folds", "glossotonsillar sulcus (lateral limit)",
                     "dorsal lingual and lingual arteries (deep/lateral)", "hypoglossal nerve (deep/lateral)"]

LANDMARKS = {
    "palatoplasty": ["hard-palate cleft margin and vomer", "greater palatine foramen and neurovascular pedicle",
                     "levator veli palatini (abnormal insertion on the posterior hard palate)",
                     "tensor veli palatini tendon and hamulus", "nasal mucosa layer", "uvula and soft-palate layers"],
    "tep": ["tracheostoma mucocutaneous junction", "posterior tracheal wall (party wall) at 12 o'clock",
            "cervical esophagus behind the party wall", "cricopharyngeus / pharyngoesophageal segment",
            "pharyngeal plexus and constrictors (spasm risk)"],
}


def _move_rescue_step_last(card, marker):
    steps = list(card.get("steps") or [])
    if steps and marker.lower() in str(steps[0]).lower():
        first = steps.pop(0)
        steps.append("Rescue step (only if it occurs): " + first)
        card["steps"] = steps
        return True
    return False


def install_or_card_fixes_v511(data):
    reg = getattr(data, "OR_PREP_REGISTRY", None) or {}
    done = []
    if "tegmen-repair" in reg:
        reg["tegmen-repair"]["steps"] = list(TEGMEN_STEPS)
        reg["tegmen-repair"]["landmarks"] = list(TEGMEN_LANDMARKS)
        done.append("tegmen-repair")
    if "lingual-tonsillectomy" in reg:
        reg["lingual-tonsillectomy"]["steps"] = list(LINGUAL_STEPS)
        reg["lingual-tonsillectomy"]["landmarks"] = list(LINGUAL_LANDMARKS)
        done.append("lingual-tonsillectomy")
    for slug, lm in LANDMARKS.items():
        if slug in reg:
            reg[slug]["landmarks"] = list(lm)
            done.append(slug + ":landmarks")
    for slug, marker in (("tep", "dislodged prosthesis"), ("microflap", "airway fire"), ("rrp-debridement", "airway fire")):
        if slug in reg and _move_rescue_step_last(reg[slug], marker):
            done.append(slug + ":rescue-step-last")
    data.OR_CARD_FIXES_V511 = done
    return done
