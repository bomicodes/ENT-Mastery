"""ENT Mastery v41.2 -- fix mismatched OR-prep complication entries."""
from copy import deepcopy


FIXES = {
    "tonsillectomy-adenoidectomy": {
        "early": [
            "Post-tonsillectomy/adenoid hemorrhage, airway obstruction or desaturation, dehydration/poor intake, or dental/lip/tongue injury from suspension.",
        ],
        "late": [
            "Recurrent tonsillitis or adenoid regrowth, persistent OSA from non-adenotonsillar collapse, velopharyngeal insufficiency (especially with unrecognized submucous cleft), or Eustachian-tube-related otologic sequelae.",
        ],
    },
    "microtia-reconstruction": {
        "early": [
            "Skin flap ischemia/necrosis or framework exposure, hematoma under the reconstructed framework, infection, or donor-site (costal cartilage/temporoparietal fascia) morbidity including pneumothorax risk with rib graft harvest.",
        ],
        "late": [
            "Framework malposition, resorption, or extrusion; contour asymmetry versus the contralateral ear; donor-site contour deformity; need for staged revision.",
        ],
    },
    "palatoplasty": {
        "early": [
            "Airway obstruction/desaturation (particularly with a large tongue-based flap or in a syndromic airway), bleeding from the greater palatine vessels, or aspiration.",
        ],
        "late": [
            "Oronasal fistula, velopharyngeal insufficiency with hypernasal speech/nasal regurgitation, growth restriction of the maxilla, or need for secondary speech surgery.",
        ],
    },
    "otoplasty": {
        "early": [
            "Hematoma (a firm indication for prompt evacuation to protect the cartilage), chondritis/infection, or suture extrusion.",
        ],
        "late": [
            "Recurrence of prominauris (\"telephone-ear\" deformity from suture pull-through or inadequate correction), asymmetry, keloid/hypertrophic scar, or a sharp/unnatural-appearing antihelical fold.",
        ],
    },
    "pharyngocutaneous-fistula": {
        "early": [
            "Persistent or worsening salivary drainage, wound breakdown, deep-neck infection, or aspiration of oral secretions through the fistula tract.",
        ],
        "late": [
            "Chronic non-healing fistula requiring flap closure, pharyngoesophageal stricture/stenosis at the closure site, and -- especially in an irradiated or previously dissected neck -- carotid blowout from chronic salivary contamination near the carotid sheath.",
        ],
    },
}


_MISMATCH_MARKERS = {
    "tonsillectomy-adenoidectomy": "framework surgery when applicable",
    "microtia-reconstruction": "framework surgery when applicable",
    "palatoplasty": "framework surgery when applicable",
    "otoplasty": "frontal sinus mucocele",
    "pharyngocutaneous-fistula": "Frey syndrome",
}


RIGID_TRACHEOBRONCHOSCOPY_ROLE_NOTE = (
    "ROLE: rigid-instrument-specific central-airway card (foreign-body "
    "extraction, dilation/debridement, large-channel suction). Use DLB for "
    "the concise pediatric diagnostic/stenosis-mapping card and "
    "direct-laryngoscopy-bronchoscopy for the comprehensive exact-sequence "
    "airway-evaluation card; retain this card for cases where rigid "
    "instrumentation itself is the operative reason, not general airway exam."
)


def apply_or_complications_fix_v412(data_module, app_module=None):
    ops_source = getattr(data_module, "OR_PREP_REGISTRY", None)
    if not isinstance(ops_source, dict):
        raise RuntimeError("v41.2: OR_PREP_REGISTRY unavailable")
    ops = deepcopy(ops_source)

    if "rigid-tracheobronchoscopy" not in ops:
        raise RuntimeError("v41.2: missing OR card: rigid-tracheobronchoscopy")
    rigid = ops["rigid-tracheobronchoscopy"]
    marker = "v41.2 role completion: " + RIGID_TRACHEOBRONCHOSCOPY_ROLE_NOTE
    prior = rigid.get("indications") or ""
    if marker not in prior:
        rigid["indications"] = prior.rstrip() + ("\n\n" if prior.strip() else "") + marker

    fixed, preserved = [], []
    for slug, replacement in FIXES.items():
        if slug not in ops:
            raise RuntimeError("v41.2: missing OR card: " + slug)
        current = ops[slug].get("complications")
        current_text = " ".join(
            " ".join(v) if isinstance(v, list) else str(v)
            for v in (current or {}).values()
        )
        if _MISMATCH_MARKERS[slug] in current_text:
            ops[slug]["complications"] = deepcopy(replacement)
            fixed.append(slug)
        else:
            preserved.append(slug + ":already-corrected-or-unrecognized")

    data_module.OR_PREP_REGISTRY.clear()
    data_module.OR_PREP_REGISTRY.update(ops)
    if app_module is not None:
        app_module.OR_PREP_REGISTRY = data_module.OR_PREP_REGISTRY
    return {"complications_fixed": fixed, "complications_preserved": preserved}
