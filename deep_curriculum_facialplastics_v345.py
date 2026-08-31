"""v34.5 — paramedian forehead-flap vascular compromise recognition and rescue.

Bounded follow-on to v34.4. Adds chief-level stop points for threatened axial flap
perfusion without changing the general local-flap/forehead-flap semantic split.
"""

import re

DOMAIN = "Facial Plastics / Trauma"
TOPIC = "forehead flap nasal reconstruction"


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _extend_sources(module, sources):
    module["source_basis"] = list(dict.fromkeys(list(module.get("source_basis") or []) + list(sources)))


def apply_facialplastics_forehead_rescue_v345(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []

    for module in modules or []:
        if _norm(module.get("topic")) != TOPIC:
            continue

        module["manage"] = (
            str(module.get("manage") or "")
            + " COMMITMENT/RESCUE POINT: before leaving stage 1, the pedicle must lie without kink, torsion, compression, or an over-tight inset/dressing. "
              "A threatened flap is a diagnosis-and-correction problem, not a watch-and-wait color change. Dusky, swollen/turgid tissue with rapid dark bleeding favors venous congestion; "
              "a pale, cool flap with poor capillary refill/bleeding suggests inadequate arterial inflow. First remove reversible mechanical causes: release constricting sutures or dressings, "
              "correct pedicle twist/kink or excessive tension, and evacuate a compressive hematoma while preserving the vascular pedicle. Reassess immediately after each correction."
        )
        module["operate"] = (
            str(module.get("operate") or "")
            + " BAILOUT CHOREOGRAPHY: if perfusion remains abnormal after bedside/mechanical correction, escalate early to operative reassessment when a surgically correctable cause is plausible; "
              "do not repeatedly needle, aggressively thin, or otherwise traumatize a threatened pedicle. For persistent venous congestion with adequate inflow and no correctable obstruction, "
              "medicinal leech therapy is a selective salvage adjunct—not a substitute for correcting torsion, compression, hematoma, or tension—and requires an Aeromonas-active antimicrobial protocol "
              "plus close monitoring for blood loss/anemia. If distal necrosis declares itself, preserve viable tissue and pedicle options, allow the reconstructive plan to declare the true defect when appropriate, "
              "and revise deliberately rather than debriding viable flap reflexively. Do not divide a forehead-flap pedicle simply because the calendar says it is time when distal perfusion or healing is questionable."
        )
        module["teach"] = (
            str(module.get("teach") or "")
            + " CHIEF RESCUE FRAME: threatened forehead flap = RECOGNIZE arterial vs venous pattern -> REMOVE mechanical obstruction/tension/hematoma -> REASSESS -> RETURN TO OR early if a correctable cause remains -> "
              "use venous-decongestion adjuncts selectively when inflow is intact. Pedicle division is a perfusion/healing decision, not merely a scheduled date."
        )
        module["tags"] = list(dict.fromkeys(list(module.get("tags") or []) + [
            "forehead flap venous congestion", "forehead flap arterial insufficiency", "pedicle kink", "flap salvage", "medicinal leech", "Aeromonas"
        ]))
        _extend_sources(module, [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — nasal reconstruction and forehead-flap vascular principles",
            "K.J. Lee's Essential Otolaryngology, 12e — facial plastic reconstruction and flap vascularity",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e, Ch 8 — Facial Reconstruction Techniques",
            "Boissiere F et al. Flap Venous Congestion and Salvage Techniques: A Systematic Literature Review. Plast Reconstr Surg Glob Open. 2021 — early recognition, correction of mechanical causes, and evidence for leech salvage",
            "Herlin C et al. Leech therapy in flap salvage: systematic review and practical recommendations. Ann Chir Plast Esthet. 2017 — venous-congestion salvage and monitoring considerations",
            "Wiener M et al. A New Approach to an Old Flap: A Technique to Augment Venous Drainage from the Paramedian Forehead Flap. Plast Reconstr Surg. 2019 — superficial venous drainage and congestion mechanism",
            "Gates CK et al. Repurposing the PMFF Pedicle Before Final Division: Distal Necrosis Salvage With Long-Term Success. Laryngoscope. 2026 — contemporary salvage example emphasizing preservation of reconstructive options"
        ])
        module["facialplastics_forehead_rescue_v345"] = True
        module["semantic_role_v345"] = "forehead-flap arterial/venous compromise recognition, mechanical rescue, escalation, and pedicle-preserving salvage"
        patched.append(module.get("topic"))

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
