"""v34.2 — add bounded rescue choreography to facial-plastics graft selection.

This module preserves the v34.1 semantic split between structural nasal grafting and
cutaneous skin-graft selection while adding chief-resident bailout actions for two
predictable failure modes: pleural injury during autologous costal-cartilage harvest and
early skin-graft separation from hematoma/seroma or shear.
"""

import re

DOMAIN = "Facial Plastics / Trauma"


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _append_text(existing, addition):
    base = str(existing or "").strip()
    return f"{base} {addition}".strip() if base else addition


def apply_facialplastics_graft_rescue_v342(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []

    for module in modules or []:
        topic = _norm(module.get("topic"))

        if topic == "rhinoplasty graft selection":
            module["operate"] = _append_text(
                module.get("operate"),
                "COSTAL-CARTILAGE HARVEST BAILOUT: stay directly on rib/perichondrial planes and treat an unexpected pleural violation as a separate physiologic problem, not as permission to continue harvesting blindly. Stop deeper dissection, obtain direct control/visualization of the defect, alert anesthesia, and assess ventilation/oxygenation and hemodynamics. If pleural injury or pneumothorax is suspected, use an appropriate leak/pneumothorax assessment and obtain chest imaging when the diagnosis is not already established clinically; significant or symptomatic pneumothorax requires prompt pleural decompression/drainage rather than merely closing the donor incision. Re-establish a safe harvest plane—or abandon further rib harvest if that plane cannot be trusted—before proceeding with nasal reconstruction."
            )
            module["teach"] = _append_text(
                module.get("teach"),
                "CHIEF COMMITMENT POINT: the need for more cartilage never outranks donor-site safety. A suspected pleural entry converts the case from routine harvest to stop-assess-control-rescue; do not keep dissecting for graft volume while the chest complication is unresolved."
            )
            module["source_basis"] = list(dict.fromkeys(list(module.get("source_basis") or []) + [
                "Varadharajan et al. Complications Associated With the Use of Autologous Costal Cartilage in Rhinoplasty: A Systematic Review. Aesthet Surg J. 2015 — donor-site pleural tear/pneumothorax risk",
                "Chen et al. Complications Associated with Autologous Costal Cartilage Used in Rhinoplasty: An Updated Meta-Analysis. Plast Reconstr Surg. 2022 — contemporary donor- and recipient-site complication estimates",
            ]))
            module["facialplastics_graft_rescue_v342"] = True
            patched.append(module.get("topic"))

        elif topic == "skin graft selection":
            module["manage"] = _append_text(
                module.get("manage"),
                "EARLY TAKE-FAILURE RESCUE: a tense hematoma/seroma, focal graft lift, or loss of graft-bed contact is a correctable mechanical emergency during the take window. Release the collection when clinically indicated, achieve hemostasis, restore intimate graft-to-bed contact, and re-secure/immobilize the graft rather than simply observing progressive separation. If the graft is clearly nonviable, debride nonviable tissue and reassess the recipient bed, infection/contamination, perfusion, dead space, and reconstructive requirement before repeating the same graft. Do not solve a persistently avascular bed by repeatedly changing graft thickness."
            )
            module["teach"] = _append_text(
                module.get("teach"),
                "CHIEF RESCUE FRAME: early graft failure should trigger a cause-based diagnosis—fluid under the graft, shear/motion, infection, inadequate hemostasis, or an avascular bed—followed by correction of that mechanism before regrafting."
            )
            module["source_basis"] = list(dict.fromkeys(list(module.get("source_basis") or []) + [
                "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e, Ch 8 — graft take depends on vascular bed, immobilization, and prevention of hematoma/seroma",
            ]))
            module["facialplastics_graft_rescue_v342"] = True
            patched.append(module.get("topic"))

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
