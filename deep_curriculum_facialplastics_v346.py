"""v34.6 — eyelid/periocular reconstruction orbital-compartment rescue.

Bounded follow-on to v34.5. Adds a sight-threatening postoperative commitment/rescue layer
to the canonical Eyelid Reconstruction card without changing facial-plastics taxonomy.
"""

import re

DOMAIN = "Facial Plastics / Trauma"
TOPIC = "eyelid reconstruction"


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _extend_sources(module, sources):
    module["source_basis"] = list(dict.fromkeys(list(module.get("source_basis") or []) + list(sources)))


def apply_facialplastics_eyelid_ocs_rescue_v346(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []

    for module in modules or []:
        if _norm(module.get("topic")) != TOPIC:
            continue

        module["manage"] = (
            str(module.get("manage") or "")
            + " SIGHT-THREAT COMMITMENT POINT: after eyelid/periocular reconstruction, rapidly increasing orbital pain/pressure, proptosis or a tense orbit, "
              "new reduction in visual acuity or color vision, a relative afferent pupillary defect, ophthalmoplegia, or a marked intraocular-pressure rise should trigger concern for "
              "retrobulbar/orbital hemorrhage with ORBITAL COMPARTMENT SYNDROME (OCS). Do not require every finding to be present before acting when the clinical picture is compelling. "
              "Build postoperative checks around vision, pupils, globe position/motility, pain and orbital tension rather than documenting the incision alone."
        )
        module["operate"] = (
            str(module.get("operate") or "")
            + " OCS BAILOUT CHOREOGRAPHY: clinically convincing, sight-threatening OCS is a decompression emergency; obtain urgent ophthalmic help, but do not delay pressure release solely to obtain CT. "
              "Immediately remove a constricting dressing or periocular closure if it is contributing, open/evacuate an accessible compressive hematoma when appropriate, and perform lateral canthotomy with "
              "inferior cantholysis to decompress the orbit. Reassess visual function, pupil, globe tension/position and pressure after decompression. If the orbit remains tight or visual compromise persists, "
              "escalate promptly for further orbital exploration/decompression rather than assuming the initial canthotomy was sufficient. Anticoagulation/coagulopathy and the bleeding source should be addressed in parallel, "
              "but reversal/hemostatic work must not become the reason a threatened optic nerve waits for decompression."
        )
        module["teach"] = (
            str(module.get("teach") or "")
            + " CHIEF RESCUE FRAME: after periocular surgery, PAIN/PROPTOSIS/TENSE ORBIT + NEW VISUAL OR PUPILLARY DEFICIT = presume OCS until rapidly disproved. "
              "The rescue sequence is RECOGNIZE -> RELEASE external/closure compression -> LATERAL CANTHOTOMY + INFERIOR CANTHOLYSIS -> REASSESS -> ESCALATE if still tight/visually compromised. "
              "Imaging can define cause after immediate stabilization; it must not postpone decompression in an obvious sight-threatening compartment syndrome."
        )
        module["tags"] = list(dict.fromkeys(list(module.get("tags") or []) + [
            "orbital compartment syndrome", "retrobulbar hemorrhage", "lateral canthotomy", "inferior cantholysis", "vision rescue", "RAPD"
        ]))
        _extend_sources(module, [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — eyelid/periocular reconstruction and orbital emergency principles",
            "K.J. Lee's Essential Otolaryngology, 12e — orbital/facial trauma anatomy and vision-threatening complication framework",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — facial reconstruction and orbital trauma principles",
            "Papadiochos I et al. Acute orbital compartment syndrome due to traumatic hemorrhage: 4-year case series and relevant literature review with emphasis on its management. Oral Maxillofac Surg. 2023;27(1):101-116 (online 2022) — prompt clinical recognition, emergency decompression, and imaging without delaying indicated treatment",
            "Mei F et al. Orbital Compartment Syndrome After Primary Scleral Buckle Surgery. Retin Cases Brief Rep. 2025;19(2):240-243 — postoperative OCS successfully treated with canthotomy/cantholysis",
            "Dryden S et al. Marginal Full Thickness Blepharotomy for Management of Orbital Compartment Syndrome. Ophthalmic Plast Reconstr Surg. 2024;40(4):408-410 — OCS as a time-sensitive vision-threatening emergency and an escalation option when standard canthotomy/cantholysis is inadequate or cannot be performed"
        ])
        module["facialplastics_eyelid_ocs_rescue_v346"] = True
        module["semantic_role_v346"] = "postoperative orbital-compartment recognition, immediate decompression, reassessment, and escalation"
        patched.append(module.get("topic"))

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
