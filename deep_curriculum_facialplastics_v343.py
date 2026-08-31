"""v34.3 — tighten skin-graft vascularity semantics.

A skin graft is transferred without an intrinsic vascular pedicle, but successful take requires
a vascularized recipient bed. This bounded semantic patch removes wording that could be read
as endorsing an avascular wound bed and sharpens the graft-versus-flap distinction.
"""

import re

DOMAIN = "Facial Plastics / Trauma"


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def apply_facialplastics_graft_vascular_semantics_v343(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules or []:
        if _norm(module.get("topic")) != "skin graft selection":
            continue

        recognize = str(module.get("recognize") or "")
        recognize = recognize.replace(
            "This card owns AVASCULAR CUTANEOUS COVERAGE, not structural nasal support.",
            "This card owns NONVASCULARIZED CUTANEOUS GRAFT COVERAGE, not structural nasal support. "
            "The graft is transferred without its own vascular pedicle and therefore depends on a vascularized recipient bed for take."
        )
        module["recognize"] = recognize
        module["teach"] = str(module.get("teach") or "") + (
            " GRAFT-VERSUS-FLAP SEMANTIC RULE: a skin graft arrives without an intrinsic blood supply and must revascularize from the recipient bed; "
            "a flap transfers tissue with its own blood supply (or a vascular pedicle/microvascular inflow). Therefore an avascular recipient surface "
            "is a reason to change the bed or reconstructive method—not a defining feature of skin-graft coverage."
        )
        module["source_basis"] = list(dict.fromkeys(list(module.get("source_basis") or []) + [
            "Schwartzberg et al. Full-Thickness Skin Grafts for Nasal Defect Reconstruction. Cureus. 2025 — FTSGs depend on a well-vascularized wound bed; extensive bare cartilage is a poor recipient bed",
            "StatPearls Interpolated Flaps (updated 2024) — flaps retain/transfer an axial or random-pattern vascular supply, distinguishing flap perfusion from graft take"
        ]))
        module["facialplastics_graft_vascular_semantics_v343"] = True
        patched.append(module.get("topic"))

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
