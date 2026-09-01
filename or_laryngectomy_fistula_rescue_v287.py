"""v28.7 — pharyngocutaneous fistula/salivary-leak rescue after total laryngectomy.

Adds an executable resident/chief postoperative pathway to the existing laryngectomy
margin/closure commitments. Foundational ENT texts anchor pharyngeal closure and neck
anatomy; the 2026 IFOS consensus and contemporary systematic reviews anchor current
surveillance, nutritional support, selective conservative care and revision decisions.
Where current consensus is absent (for example routine salivary-bypass tubes, negative
pressure therapy, or one universal oral-feeding timetable), this module deliberately
avoids presenting a local preference as a mandatory standard.
"""

TARGETS = (
    ("total-laryngectomy", ("total", "laryngectomy")),
)

RESCUE = [
    "PHARYNGOCUTANEOUS FISTULA RECOGNITION: after total laryngectomy, new salivary or turbid neck/drain output, wound erythema or separation, increasing neck tenderness/swelling, fever/tachycardia, foul drainage, or unexplained inflammatory deterioration should trigger focused evaluation for pharyngocutaneous fistula and associated collection. Remember that this patient is a neck-only airway: protect and suction the laryngectomy stoma as needed while evaluating the pharyngeal wound; oral/nasal oxygen or intubation will not ventilate the lungs after total laryngectomy.",
    "EARLY CONTAINMENT / PHYSIOLOGY: stop oral intake when an active pharyngeal leak is suspected until the responsible head-and-neck team defines the feeding plan, maintain or establish enteral nutritional support away from the leaking pharyngeal closure when feasible, correct dehydration/electrolyte and protein-calorie deficits, and optimize wound-healing factors such as infection, anemia, glycemic control and hypothyroidism when present. Culture frankly infected drainage and use systemic antibiotics for cellulitis, abscess, sepsis or other clinical infection rather than treating an uncomplicated controlled salivary leak with an indefinite antibiotic course by default.",
    "DEFINE THE WOUND, NOT JUST THE SKIN OPENING: examine for cavity size, dependent drainage, exposed reconstruction and proximity to the carotid/great vessels; obtain cross-sectional imaging when deep infection/collection, uncertain extent, flap compromise or great-vessel risk is suspected. Drain an undrained infected collection and provide meticulous local wound/saliva control. A small, well-drained fistula in a clinically stable patient can often begin with structured conservative management plus enteral nutrition and close surveillance, but the plan must demonstrate improving wound condition and leak trajectory rather than passive waiting.",
    "DANGER-ZONE / CAROTID BAILOUT: salivary contamination, infection and tissue breakdown in an irradiated or previously operated neck can expose a carotid or flap pedicle. Visible/palpable vessel exposure, tissue necrosis over a great vessel, or any sentinel or brisk hemorrhage is a change-of-plan emergency: activate senior head-and-neck, anesthesia/resuscitation and vascular/interventional expertise, protect the neck-only airway, and pursue urgent definitive vascular and wound control rather than routine bedside fistula care or blind deep packing/clamping around the vessel.",
    "REVISION COMMITMENT: failure of a fistula to close or clearly improve, recurrent/deep infection, major wound breakdown, exposed vessel/hardware, necrotic pharyngeal closure or flap, or inability to maintain safe nutrition/vascular coverage should trigger reconstructive reassessment and operative source control. Debride nonviable tissue, close the pharyngeal defect when feasible and bring well-vascularized tissue into a hostile irradiated/infected field when needed. Persistent fistula is not an indication to continue the same conservative plan indefinitely simply because the patient remains temporarily stable.",
    "EQUIPOISE / LOCAL-PROTOCOL POINT: do not teach prophylactic salivary-bypass tubes, negative-pressure wound therapy, or a single postoperative day for oral feeding as universal requirements. Contemporary IFOS consensus found important areas of ongoing practice variation; use these adjuncts selectively according to defect geometry, tissue quality, reconstruction, aspiration/saliva-control needs and local expertise while keeping the non-negotiable endpoints—adequate nutrition, drainage/infection control, vessel protection and durable fistula closure—explicit.",
]

SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. — total-laryngectomy/pharyngeal closure anatomy, fistula risk and reconstructive principles",
    "K. J. Lee's Essential Otolaryngology, 12th ed. — laryngectomy complications and pharyngocutaneous fistula principles",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed. — total-laryngectomy postoperative complication framework",
    "Maniaci A, et al. Pharyngocutaneous Fistula After Total Laryngectomy: IFOS Consensus on Prevention, Diagnosis, and Management. Head Neck. 2026. doi:10.1002/hed.70436",
    "Gomis-Lleal E, Sampieri C, Costa-Gonzalez JM, et al. Pharyngocutaneous fistula following total laryngectomy: a systematic review of risk factors and management strategies (2010-2024). Eur Arch Otorhinolaryngol. 2026;283:4609-4618. doi:10.1007/s00405-026-10157-4",
    "Williamson A, et al. Vascularized Tissue to Reduce Fistula After Salvage Total Laryngectomy: A Network Meta-analysis. Laryngoscope. 2024;134:2991-3002. doi:10.1002/lary.31287",
]


def _resolve(registry, slug, terms):
    reg = registry or {}
    if slug in reg:
        return slug, reg[slug]
    for key, op in reg.items():
        hay = (str(key) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in terms):
            return key, op
    return None, None


def _append_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in additions:
        marker = text[:88].lower()
        if not any(marker in str(x).lower() for x in out):
            out.append(text)
            changed = True
    return out, changed


def apply_or_laryngectomy_fistula_rescue_v287(registry):
    changed, resolved, missing = [], [], []
    for slug, terms in TARGETS:
        key, op = _resolve(registry, slug, terms)
        if not op:
            missing.append(slug)
            continue
        op["postop"], c1 = _append_unique(op.get("postop"), RESCUE)
        op["sources"], c2 = _append_unique(op.get("sources"), SOURCES)
        op["laryngectomy_fistula_rescue_v287"] = True
        op["laryngectomy_fistula_semantic_role_v287"] = (
            "recognize leak -> protect neck-only airway -> divert saliva/support nutrition -> "
            "define/drain wound -> protect great vessels -> revise persistent/unsafe fistula"
        )
        resolved.append(key)
        if c1 or c2:
            changed.append(key)
    return {"changed": changed, "count": len(changed), "resolved": resolved, "missing": missing}
