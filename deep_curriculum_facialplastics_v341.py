"""v34.1 — separate structural rhinoplasty grafting from cutaneous skin-graft selection.

Bounded Concept Hub rebuild. The title similarity is misleading: rhinoplasty graft selection
is a nasal-framework biomechanics problem, whereas skin-graft selection is a wound-bed,
coverage, contraction, and donor-match problem. Keep the cards clinically distinct.
"""

import re

DOMAIN = "Facial Plastics / Trauma"


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def apply_facialplastics_graft_selection_v341(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []

    for module in modules or []:
        topic = _norm(module.get("topic"))

        if topic == "rhinoplasty graft selection":
            module["recognize"] = (
                "This card owns STRUCTURAL NASAL GRAFT SELECTION, not skin coverage. Start by naming the mechanical problem: "
                "midvault collapse/internal nasal valve narrowing, weak lateral wall or alar rim, inadequate caudal septal support, "
                "tip projection/rotation instability, dorsal deficiency, or major framework loss. Then choose graft geometry and donor "
                "material that can supply the required stiffness, shape, volume, and long-term stability. Do not choose a donor first and "
                "then invent a use for the harvested cartilage."
            )
            module["localize"] = (
                "Match graft to subunit and force. SPREADER grafts reconstruct/support the middle vault and can widen the internal nasal "
                "valve while restoring dorsal aesthetic lines. ALAR BATTEN or LATERAL CRURAL STRUT grafts reinforce a weak/collapsing lateral "
                "wall or malpositioned lateral crus; an alar-rim graft addresses rim support/contour rather than caudal septal strength. A "
                "SEPTAL EXTENSION graft fixes tip support, projection and rotation to the caudal septal complex more powerfully than a simple "
                "columellar strut. DORSAL ONLAY/augmentation grafting restores height and contour but must be stable, smooth and appropriately camouflaged."
            )
            module["workup"] = (
                "Analyze the nose before selecting material: external shape, tip support, middle-vault width, dynamic lateral-wall collapse, "
                "septal support/available cartilage, airway goals, skin-soft-tissue-envelope thickness, prior operations, scars and prior grafts. "
                "In revision or post-traumatic cases, determine whether the native septum is depleted or structurally unsafe to harvest. Preserve "
                "an adequate dorsal/caudal L-strut and do not create iatrogenic septal instability merely to obtain graft material."
            )
            module["manage"] = (
                "AUTOGRAFT hierarchy is job-dependent. Septal cartilage is commonly preferred when available because it is straight, relatively "
                "stiff and harvested in the same field. Auricular/conchal cartilage is curved and pliable, useful when contour or alar/lateral-wall "
                "shape is advantageous, but it supplies less straight load-bearing stock. Costal cartilage provides abundant strong material for major "
                "dorsal/caudal/septal reconstruction and revision noses when septum is inadequate, at the cost of a separate donor site and risks such "
                "as warping/calcification. Cadaveric costal cartilage or selected alloplastic material can be alternatives in appropriately selected "
                "patients, but material choice must account for structural demand, infection/extrusion/resorption/warping tradeoffs and surgeon experience."
            )
            module["operate"] = (
                "At operation, re-diagnose the deforming force after exposure; do not solve every irregularity by stacking grafts. Harvest only what "
                "is needed while protecting donor-site function. Carve structural grafts with sufficient dimensions and stable fixation so the graft "
                "resists the force it is meant to correct; bevel/camouflage edges where visibility is a risk. In rib grafting, anticipate warping and "
                "shape balanced segments deliberately. Confirm both airway and aesthetic consequences before closure because a technically straight graft "
                "can still narrow another airway segment or create a visible contour."
            )
            module["teach"] = (
                "BOARDS/CHIEF FRAME: rhinoplasty graft selection asks, 'WHAT FORCE OR FRAMEWORK DEFICIT am I correcting, what graft geometry solves it, "
                "and which donor material has the right mechanical properties?' Septum is often first-line straight structural stock; concha is useful "
                "for curved/contour work; rib is the high-volume/high-strength option when major reconstruction is required. This is not a wound-coverage "
                "decision and should never be conflated with FTSG-versus-STSG selection."
            )
            module["tags"] = list(dict.fromkeys(list(module.get("tags") or []) + [
                "rhinoplasty graft", "septal cartilage", "auricular cartilage", "costal cartilage", "spreader graft",
                "alar batten", "lateral crural strut", "septal extension graft", "dorsal augmentation"
            ]))
            module["source_basis"] = list(dict.fromkeys(list(module.get("source_basis") or []) + [
                "Cummings Otolaryngology—Head and Neck Surgery, 7e — rhinoplasty framework reconstruction and grafting principles",
                "K.J. Lee's Essential Otolaryngology, 12e — facial plastic/rhinoplasty anatomy and structural-grafting framework",
                "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e, Ch 8 — Grafts, Implants, and Expanders; Rhinoplasty",
                "AAO-HNSF Clinical Practice Guideline: Improving Nasal Form and Function after Rhinoplasty (2017) — functional/aesthetic preoperative assessment and outcome framework",
                "Grafting in Rhinoplasty: A Survey of Surgeon Preferences When Donor Material Is Limited (Plast Reconstr Surg, 2025) — septal preference and job-specific donor-material patterns",
                "Fedok. Costal Cartilage Grafts in Rhinoplasty. Clin Plast Surg. 2016 — rib indications in major/revision reconstruction"
            ]))
            module["facialplastics_graft_selection_v341"] = True
            module["semantic_role_v341"] = "nasal structural biomechanics, graft geometry, and donor-material selection"
            patched.append(module.get("topic"))

        elif topic == "skin graft selection":
            module["recognize"] = (
                "This card owns AVASCULAR CUTANEOUS COVERAGE, not structural nasal support. Before choosing full- versus split-thickness skin, ask whether "
                "a skin graft is appropriate at all: the defect needs a vascularized recipient bed, oncologic clearance when relevant, hemostasis, and a "
                "surface on which the graft can remain immobile while neovascularization occurs. If missing framework, exposed critical structures, dead "
                "space, or contour requirements demand vascularized tissue, a local/regional/free flap may be the better reconstruction."
            )
            module["localize"] = (
                "Recipient-bed biology drives take. Muscle, fascia, granulation tissue, intact perichondrium and intact periosteum can support grafting; "
                "bare avascular cartilage or cortical bone stripped of perichondrium/periosteum is a poor bed and should trigger a plan to create vascularized "
                "coverage rather than simply choosing a thinner graft. On the face, also analyze aesthetic subunit, contour depth, eyelid/lip free-margin "
                "distortion risk, and donor color/texture/thickness/hair match."
            )
            module["workup"] = (
                "Choose thickness by defect and reconstructive goal. FULL-THICKNESS SKIN GRAFT (FTSG) contains epidermis plus the full dermis: it generally "
                "gives superior facial color/texture match and less secondary contraction, making it useful for smaller cosmetically sensitive defects, but "
                "it requires a robust vascular bed and the donor site usually must close primarily. SPLIT-THICKNESS SKIN GRAFT (STSG) contains epidermis plus "
                "part of dermis: it can cover much larger areas, its donor site re-epithelializes, and it generally takes more readily, but secondary contraction, "
                "pigment/texture mismatch and contour depression are greater concerns."
            )
            module["manage"] = (
                "Optimize TAKE, not just graft choice. Debride nonviable tissue, control infection and meticulous bleeding, contour the graft to full contact, "
                "eliminate hematoma/seroma and shear, and secure it with an appropriate bolster or other immobilizing dressing. Smoking, irradiation, poor "
                "perfusion and contaminated beds increase failure risk. Meshing STSG expands coverage and permits fluid egress but sacrifices surface texture; "
                "sheet grafts are preferred when appearance is important and drainage can be managed."
            )
            module["operate"] = (
                "Know the physiology: early graft survival begins with PLASMATIC IMBIBITION, followed by INOSCULATION between graft and recipient vessels and "
                "then NEOVASCULARIZATION/revascularization. Every technical step should protect that sequence. Defat FTSGs enough for intimate bed contact "
                "without injuring the dermis, orient the best-matched donor skin, avoid tenting across concavities, fenestrate/pie-crust when needed for drainage, "
                "and prevent motion. A successful skin graft resurfaces a defect; it does not replace absent cartilage/bone support or obliterate meaningful dead space."
            )
            module["teach"] = (
                "BOARDS/CHIEF FRAME: skin-graft selection asks, 'IS THE BED VASCULAR ENOUGH, how much surface must I cover, how much contraction can the site tolerate, "
                "and what donor gives the best match?' FTSG = better facial match/less secondary contraction but greater metabolic demand and limited harvest; "
                "STSG = larger/easier-take coverage but more secondary contraction and poorer texture/pigment match. Bare cartilage/bone without vascularized covering "
                "is a BED problem, not an indication to keep switching graft thickness."
            )
            module["tags"] = list(dict.fromkeys(list(module.get("tags") or []) + [
                "full thickness skin graft", "split thickness skin graft", "recipient bed", "perichondrium", "periosteum",
                "plasmatic imbibition", "inosculation", "neovascularization", "graft contraction", "bolster"
            ]))
            module["source_basis"] = list(dict.fromkeys(list(module.get("source_basis") or []) + [
                "Cummings Otolaryngology—Head and Neck Surgery, 7e — facial reconstruction and graft/wound-healing principles",
                "K.J. Lee's Essential Otolaryngology, 12e — reconstructive wound-coverage framework",
                "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e, Ch 8 — Fundamentals of Wound Healing; Grafts, Implants, and Expanders; Facial Reconstruction Techniques",
                "NCBI/StatPearls Full-Thickness Skin Grafts (updated 2026) — facial indications, vascular-bed requirements and phases of graft take",
                "NCBI/StatPearls Split-Thickness Skin Grafts (updated 2025/2026) — STSG biology, donor healing, contraction and recipient-bed requirements"
            ]))
            module["facialplastics_graft_selection_v341"] = True
            module["semantic_role_v341"] = "cutaneous wound-bed assessment, graft thickness selection, take physiology, and surface coverage"
            patched.append(module.get("topic"))

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
