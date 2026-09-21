"""ENT Mastery v41.3 -- fix mismatched OR-prep landmarks, exit checks,
and complications missed by v41.2's complications-only pass.
"""
from copy import deepcopy


LANDMARKS = {
    "otoplasty": [
        "auricular cartilage framework: conchal bowl, antihelical fold and scapha",
        "postauricular sulcus and mastoid periosteum (conchomastoid suture anchor site)",
        "greater auricular nerve coursing across the sternocleidomastoid toward the lobule",
        "helical rim contour used to judge symmetry against the contralateral ear",
    ],
    "septorhino": [
        "bony-cartilaginous vault junction (keystone area) where septum meets nasal bones and upper laterals",
        "quadrangular cartilage and dorsal/caudal L-strut required for structural support",
        "upper lateral cartilages and internal nasal valve angle",
        "lower lateral (alar) cartilages and external nasal valve",
        "columella and membranous septum",
        "mucoperichondrial/mucoperiosteal flaps on each side of the septum",
    ],
}

EXIT_CHECK = {
    "otoplasty": [
        "Confirm symmetric antihelical fold/setback and adequate hemostasis before dressing; rule out an early hematoma.",
        "Secure a non-compressive mastoid (Fluffs/head) dressing and confirm mattress-suture security without excess skin tension.",
    ],
    "septorhino": [
        "Confirm septal L-strut stability and mucosal flap integrity; check for unrecognized perforation or hematoma.",
        "Assess internal/external nasal-valve patency and dorsal-line symmetry; secure splint/packing per plan and document airway patency.",
    ],
    "septoplasty": [
        "Confirm septal L-strut stability and mucosal flap integrity; check for unrecognized perforation or hematoma.",
        "Confirm nasal airway patency bilaterally; secure splint/packing per plan and document hemostasis.",
    ],
}

COMPLICATIONS = {
    "septorhino": {
        "early": [
            "Septal hematoma (a firm indication for prompt drainage to prevent abscess or cartilage necrosis), epistaxis, or acute nasal-valve collapse/obstruction from swelling.",
        ],
        "late": [
            "Septal perforation, saddle-nose or other dorsal/caudal contour deformity from unrecognized L-strut destabilization, residual or recurrent valve dysfunction, or asymmetry requiring revision.",
        ],
    },
    "septoplasty": {
        "early": [
            "Septal hematoma (requires prompt drainage to prevent abscess and cartilage necrosis), epistaxis, or infection.",
        ],
        "late": [
            "Septal perforation, persistent or recurrent obstruction, dorsal/caudal destabilization (saddle deformity) if the L-strut is compromised, or synechiae.",
        ],
    },
}


_LANDMARKS_MARKER = "frontal outflow tract/skull base"
_EXIT_CHECK_TRAUMA_MARKER = "repeat forced ductions when indicated"
_EXIT_CHECK_SKULLBASE_MARKER = "intended sinus/skull-base exposure"
_SEPTORHINO_COMPLICATIONS_MARKER = "frontal sinus mucocele"
_SEPTOPLASTY_COMPLICATIONS_MARKER = "intracranial complication"


def _text(value):
    if isinstance(value, dict):
        return " ".join(_text(v) for v in value.values())
    if isinstance(value, list):
        return " ".join(str(v) for v in value)
    return str(value)


def apply_or_landmarks_exitcheck_fix_v413(data_module, app_module=None):
    ops_source = getattr(data_module, "OR_PREP_REGISTRY", None)
    if not isinstance(ops_source, dict):
        raise RuntimeError("v41.3: OR_PREP_REGISTRY unavailable")
    ops = deepcopy(ops_source)

    landmarks_fixed, exit_check_fixed, complications_fixed = [], [], []
    preserved = []

    for slug in ("otoplasty", "septorhino"):
        if slug not in ops:
            raise RuntimeError("v41.3: missing OR card: " + slug)
        card = ops[slug]
        if _LANDMARKS_MARKER in _text(card.get("landmarks")):
            card["landmarks"] = deepcopy(LANDMARKS[slug])
            landmarks_fixed.append(slug)
        else:
            preserved.append(slug + ":landmarks-already-corrected-or-unrecognized")
        if _EXIT_CHECK_TRAUMA_MARKER in _text(card.get("exit_check")):
            card["exit_check"] = deepcopy(EXIT_CHECK[slug])
            exit_check_fixed.append(slug)
        else:
            preserved.append(slug + ":exit_check-already-corrected-or-unrecognized")

    if _SEPTORHINO_COMPLICATIONS_MARKER in _text(ops["septorhino"].get("complications")):
        ops["septorhino"]["complications"] = deepcopy(COMPLICATIONS["septorhino"])
        complications_fixed.append("septorhino")
    else:
        preserved.append("septorhino:complications-already-corrected-or-unrecognized")

    if "septoplasty" not in ops:
        raise RuntimeError("v41.3: missing OR card: septoplasty")
    septoplasty = ops["septoplasty"]
    if _EXIT_CHECK_SKULLBASE_MARKER in _text(septoplasty.get("exit_check")):
        septoplasty["exit_check"] = deepcopy(EXIT_CHECK["septoplasty"])
        exit_check_fixed.append("septoplasty")
    else:
        preserved.append("septoplasty:exit_check-already-corrected-or-unrecognized")
    if _SEPTOPLASTY_COMPLICATIONS_MARKER in _text(septoplasty.get("complications")):
        septoplasty["complications"] = deepcopy(COMPLICATIONS["septoplasty"])
        complications_fixed.append("septoplasty")
    else:
        preserved.append("septoplasty:complications-already-corrected-or-unrecognized")

    data_module.OR_PREP_REGISTRY.clear()
    data_module.OR_PREP_REGISTRY.update(ops)
    if app_module is not None:
        app_module.OR_PREP_REGISTRY = data_module.OR_PREP_REGISTRY

    return {
        "landmarks_fixed": landmarks_fixed,
        "exit_check_fixed": exit_check_fixed,
        "complications_fixed": complications_fixed,
        "preserved": preserved,
    }
