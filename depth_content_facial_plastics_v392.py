"""v39.2 -- Facial Plastics / Trauma depth repair (content-staleness sweep, batch 3/9).

Same two defects as v39.0/v39.1. See thyroglossal_duct_cyst_depth_v389 for
the pattern and rationale.
"""

DOMAIN = "Facial Plastics / Trauma"

DEPTH_V392 = {
    "Mohs Defect Reconstruction": {
        "recognize": (
            "Reconstruction planning starts only after Mohs margins are confirmed clear; the defect "
            "must be assessed for which aesthetic subunit(s) it crosses, whether it involves a free "
            "margin (eyelid, alar rim, lip), and its depth (skin only vs. exposed cartilage, bone, or "
            "underlying muscle/nerve)."
        ),
        "localize": (
            "Location relative to facial subunit boundaries and free margins -- not defect size -- "
            "determines reconstructive difficulty and options: a small defect at the alar rim or "
            "eyelid margin has little tissue laxity to recruit and a high risk of notching or "
            "retraction, while a similarly sized defect on a convex, non-margin surface like the "
            "cheek or forehead tolerates a wider range of closures."
        ),
        "operate": (
            "Indication: any Mohs defect once margins are histologically clear; the reconstructive "
            "ladder runs from secondary intention and skin grafting up through local flaps and staged "
            "regional/interpolated flaps. Setup: examine tissue laxity, vascularity, and involvement "
            "of deep structures (cartilage, bone, nerve, duct) before choosing a technique. Key steps: "
            "respect subunit boundaries by placing incisions along natural junction lines when "
            "possible, recruit skin along, not across, relaxed skin tension lines, and reconstruct "
            "missing structural support (cartilage graft for alar defects, for example) rather than "
            "relying on skin closure alone to prevent free-margin distortion. Danger structures: "
            "facial nerve branches (especially temporal/marginal mandibular) in cheek and jawline "
            "defects, the nasolacrimal system near medial canthal defects, and the parotid duct in "
            "mid-cheek defects. Failure mode: choosing the reconstructive option that looks most "
            "impressive rather than the simplest one that respects free margins and subunit "
            "aesthetics -- overly aggressive flap reconstruction of a small free-margin defect can "
            "cause more distortion than a staged or simpler approach. Postoperative plan: monitor "
            "flap/graft viability, protect free margins from tension during healing, and plan any "
            "secondary revision only after the tissue has matured."
        ),
    },
    "Scar Management": {
        "recognize": (
            "Recognize which scar phenotype you are treating before intervening: hypertrophic scars "
            "stay within the original wound borders and often improve over time, keloids extend "
            "beyond the original margins and can recur aggressively after excision, and widened, "
            "depressed, or contracted scars reflect tension, poor apposition, or free-margin traction "
            "rather than an inflammatory scar process."
        ),
        "localize": (
            "Scar quality is driven by wound tension and orientation relative to relaxed skin tension "
            "lines, depth of injury, degree and duration of inflammation, and patient-specific biology "
            "(skin type, prior keloid history, anatomic location -- sternum, deltoid, and jawline are "
            "higher-risk sites for hypertrophic/keloid scarring than eyelid or upper lip)."
        ),
        "operate": (
            "Indication for procedural intervention: a scar causing functional distortion (free-"
            "margin retraction, contracture limiting motion) or one that has failed nonsurgical "
            "measures and is mature enough to revise. Setup/key steps: nonsurgical management "
            "(silicone sheeting, pressure, sun protection, intralesional steroid or 5-fluorouracil, "
            "pulsed-dye or fractional laser) is first-line and should be given adequate time before "
            "considering revision; when revision is indicated, techniques are matched to the scar's "
            "geometry -- straight-line scars crossing tension lines benefit from Z-plasty or W-plasty "
            "to reorient them, while depressed/widened scars may need re-excision with layered "
            "closure and eversion. Danger structures: depend on location (facial nerve branches near "
            "cheek/temple scars, for example); the more general hazard is operating in the wrong "
            "phase of scar maturation. Failure mode: revising an immature scar (typically before "
            "12-18 months, or before hypertrophic changes have had a chance to soften) unless "
            "function specifically demands earlier intervention -- early revision on an actively "
            "remodeling scar has a higher recurrence/re-widening rate. Postoperative plan: continued "
            "sun protection and silicone/pressure therapy after revision, with reassessment of the "
            "revised scar over the following year before considering any further procedure."
        ),
    },
    "Open Rhinoplasty Fundamentals": {
        "recognize": (
            "The open (external) approach adds a transcolumellar incision to bilateral marginal "
            "incisions, giving binocular exposure of the entire nasal framework at the cost of "
            "additional dissection, a visible (though usually inconspicuous) scar, and typically "
            "more tip edema/longer recovery than a closed approach; it is chosen when the planned "
            "work needs direct visualization rather than being achievable by feel."
        ),
        "localize": (
            "Exposure obtained is of the full framework simultaneously -- both lower lateral "
            "cartilages, the septum, and the bony-cartilaginous vault -- which is why the open "
            "approach is favored for complex tip asymmetry, revision cases with distorted anatomy, "
            "major structural grafting, or significant valve reconstruction, where precise, "
            "side-by-side comparison of the two sides under direct vision changes the operation."
        ),
        "operate": (
            "Indication: complex or revision tip work, significant structural grafting needs, "
            "internal/external valve reconstruction, or any case where accurate bilateral comparison "
            "under direct vision is expected to change the result. Setup: preoperative standardized "
            "photography and functional (nasal valve, septal deviation) plus aesthetic analysis to "
            "define what needs correcting and what septal cartilage is available for grafting. Key "
            "steps: transcolumellar inverted-V incision joined to marginal incisions, elevate skin-"
            "soft tissue envelope in a consistent subperichondrial/subperiosteal plane to preserve "
            "vascularity, address septum first if harvesting graft material, then perform planned "
            "dorsal, tip, and valve modifications with the framework fully visualized, and close in "
            "layers checking symmetry before leaving the OR. Danger structures: the medial crura and "
            "columellar vessels at the incision, the keystone area (osseocartilaginous junction) "
            "where over-aggressive dorsal work destabilizes support, and the internal/external "
            "valves, which are easily narrowed by careless cartilage removal. Failure mode: "
            "over-resection of dorsal or tip cartilage, which is far harder to correct secondarily "
            "than a mild under-correction -- when in doubt, conservative resection with structural "
            "grafting to build the desired shape is safer than aggressive reduction. Postoperative "
            "plan: splinting, edema control, and staged reassessment of the result over months, since "
            "final shape is not apparent until postoperative edema resolves."
        ),
    },
    "Otoplasty": {
        "recognize": (
            "Prominent ear (typically flagged by parents/patients as ears that 'stick out') most "
            "often results from one or both of two anatomic defects: an underdeveloped or absent "
            "antihelical fold (loss of the normal antihelical curve, so the helix sits more anterior "
            "and lateral) and/or excess conchal bowl depth/height pushing the ear away from the "
            "scalp; the two frequently coexist and produce different degrees of prominence at "
            "different points along the ear."
        ),
        "localize": (
            "Assess prominence at three reference points -- superior helix, mid-ear, and lobule -- "
            "since antihelical underdevelopment mainly affects the upper ear while conchal excess "
            "affects the mid/lower ear; measuring the conchoscaphal angle and helix-to-mastoid "
            "distance at each level localizes which component (or both) is driving the deformity in "
            "a given patient before choosing a technique."
        ),
        "operate": (
            "Indication: functionally or psychosocially significant prominent ear, most commonly "
            "addressed in childhood but performed at any age. Setup: posterior approach with an "
            "elliptical skin excision, examine and mark the deformity components (antihelical fold, "
            "conchal bowl) preoperatively. Key steps: for antihelical underdevelopment, recreate the "
            "fold with cartilage-scoring (Stenström-type) techniques and/or permanent mattress "
            "sutures (Mustardé-type) placed from the scapha to the concha; for conchal excess, reduce "
            "or set back the conchal bowl (Furnas-type conchomastoid sutures, or conchal cartilage "
            "excision) to decrease the helix-to-mastoid distance. Danger structures: the external "
            "auditory canal (avoid narrowing it with overly aggressive conchal setback) and the "
            "cartilage's blood supply, since over-thinning or scoring too deeply risks cartilage "
            "necrosis or visible sharp edges. Failure mode: applying the same suture pattern to every "
            "ear rather than matching the technique to the specific deformity component present, and "
            "overcorrection, which produces an unnatural 'pinned-back' or telephone-ear appearance "
            "and is difficult to reverse. Postoperative plan: a protective headband/dressing to "
            "prevent traumatic disruption of the new fold while it sets, and monitoring for hematoma "
            "(a surgical emergency for cartilage viability) or infection (chondritis)."
        ),
    },
    "Le Fort / Panfacial Trauma": {
        "recognize": (
            "Panfacial trauma involves fractures across multiple facial thirds/buttresses "
            "simultaneously (upper, mid, and/or lower face), so restoring a single fracture in "
            "isolation without reference to the whole framework risks reconstructing the face onto a "
            "displaced, unstable foundation; recognition requires assessing occlusion, facial width/"
            "height/projection, and ocular/neurologic status together, not fracture by fracture."
        ),
        "localize": (
            "Le Fort patterns describe horizontal midface fracture planes (I: above the dental apices "
            "through the maxilla; II: pyramidal, through the nasal bones and infraorbital rims; III: "
            "craniofacial disjunction through the zygomaticofrontal and nasofrontal sutures), but "
            "panfacial injury often combines these with mandible, naso-orbito-ethmoid, and frontal "
            "sinus fractures, so localization means mapping every disrupted buttress (vertical: "
            "nasomaxillary, zygomaticomaxillary, pterygomaxillary; horizontal: frontal bar, "
            "infraorbital rim, maxillary alveolus) on CT before planning fixation order."
        ),
        "operate": (
            "Indication: displaced panfacial fractures causing malocclusion, facial "
            "widening/flattening/lengthening, or functional (ocular, airway, dental) compromise. "
            "Setup: fine-cut facial CT, ophthalmology and dental/occlusal assessment, and "
            "identification of stable reference points (an intact mandibular condyle-ramus unit or "
            "uninjured hemiface) to reconstruct width and projection against. Key steps: sequence "
            "fixation using an outside-in/bottom-up or top-down strategy depending on which stable "
            "reference points exist -- commonly restore mandibular occlusion first when the mandible "
            "is reducible, then work from a fixed point outward to reestablish the vertical buttresses "
            "and facial width, checking occlusion and symmetry at each stage rather than fixing every "
            "fracture independently. Danger structures: the globe/optic nerve (orbital fractures), "
            "infraorbital and mental nerves, the lacrimal system in naso-orbito-ethmoid injury, and "
            "the frontal sinus outflow tract, which if not addressed can cause a delayed mucocele. "
            "Failure mode: treating each fracture as an independent repair rather than a three-"
            "dimensional framework problem -- fixing one buttress without reference to the others "
            "can lock in facial widening, flattening, or malocclusion that is far harder to correct "
            "secondarily. Postoperative plan: confirm occlusion and symmetry intraoperatively before "
            "closing, then follow with serial exams for vision, occlusion, and hardware-related "
            "complications, plus later CT if malunion is suspected."
        ),
    },
}


def apply_depth_content_facial_plastics_v392(data_module):
    modules = {m.get("topic"): m for m in data_module.DEEP_MODULES_V6.get(DOMAIN, [])}
    missing = [t for t in DEPTH_V392 if t not in modules]
    if missing:
        raise RuntimeError(f"v39.2: expected {DOMAIN} topics not found: {missing}")
    for topic, fields in DEPTH_V392.items():
        modules[topic].update(fields)
    return {"enriched": list(DEPTH_V392.keys())}
