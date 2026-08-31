"""v33.9 — cochlear implant intraoperative commitment/bailout rescue.

Bounded additive layer after v33.8. It keeps candidacy vs surgery separation intact while
making high-risk malformed-cochlea complications executable at resident/chief level.
"""

import re


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def apply_cochlear_implant_rescue_v339(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            if _norm(module.get("topic")) != "cochlear implant surgery":
                continue

            operate = str(module.get("operate") or "")
            manage = str(module.get("manage") or "")
            teach = str(module.get("teach") or "")

            operate += (
                " MALFORMED-COCHLEA COMMITMENT/RESCUE: before opening the cochlea in IP-III, common-cavity, "
                "or other anatomy with a broad cochlea-IAC/CSF communication, explicitly anticipate a gusher and "
                "electrode misdirection pathway: have sealing material ready, expose the round-window/cochlear entry "
                "well enough to control it, and choose an array/insertion strategy that can be verified rather than "
                "forcing a routine technique onto abnormal anatomy. If brisk clear fluid occurs after opening the "
                "cochlea, do not enlarge the opening reflexively and do not chase the flow with suction inside the "
                "cochlea. Maintain visualization, proceed only with a controlled insertion when the intended cochlear "
                "path is defined, then create a snug soft-tissue/fascial seal around the electrode at the cochlear entry. "
                "Persistent high-flow leakage despite a secure local seal is a bailout point: stop, reassess the anatomy "
                "and closure, and escalate CSF-pressure management/reconstructive strategy rather than simply adding "
                "blind packing."
                " ELECTRODE-POSITION STOP RULE: unexpected insertion resistance, an implausibly easy/deep trajectory, "
                "abnormal intraoperative responses, or malformed anatomy should trigger a pause before further advancement. "
                "Reconfirm the round window/basal turn and obtain position verification according to available local practice; "
                "do not repeatedly advance a questionable array toward the IAC or another extracochlear space. If IAC or "
                "other extracochlear misplacement is identified, stop further insertion and convert to a deliberate "
                "reposition/revision decision with attention to facial/cochlear nerve injury risk rather than treating the "
                "telemetry result alone as proof of correct placement."
            )

            manage += (
                " After a significant intraoperative gusher, document that the cochlear entry is sealed and follow for "
                "persistent clear otorrhea/rhinorrhea, wound fluid, meningitic symptoms, or other evidence of ongoing CSF leak. "
                "After difficult or anatomically uncertain insertion, poor early performance or unexpected facial stimulation "
                "must reopen the electrode-position differential; device integrity testing alone does not exclude scalar or "
                "extracochlear malposition."
            )

            teach += (
                " Chief-level rescue: IP-III is not merely a label for 'higher gusher risk.' It should change the room plan. "
                "Anticipate CSF flow, control the cochlear entry, avoid uncontrolled intracochlear suction or blind enlargement, "
                "seal around the electrode, and use a stop-and-verify rule when trajectory or resistance is wrong. A technically "
                "functioning implant can still be anatomically misplaced."
            )

            module["operate"] = operate
            module["manage"] = manage
            module["teach"] = teach
            module["tags"] = list(module.get("tags") or []) + [
                "IP-III bailout", "CSF gusher rescue", "electrode misplacement stop rule", "IAC misplacement"
            ]
            module["source_basis"] = list(module.get("source_basis") or []) + [
                "K.J. Lee's Essential Otolaryngology, 12e, Ch 20 Cochlear Implants — malformed cochlea, IP-III/wide-IAC CSF-gusher risk and operative complication principles",
                "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — cochlear-implant CSF leak/gusher and malformed-ear complication framework",
                "Johnson et al., Otology & Neurotology 2024 — systematic review of cochlear-implant arrays misplaced in the internal auditory canal; IP-III/common-cavity overrepresented",
                "Outcomes and Considerations of Cochlear Implantation in Patients With Incomplete Partition Type-III Malformation, scoping review, 2026 — CSF gusher is expected/common in reported IP-III CI series",
            ]
            module["cochlear_implant_rescue_v339"] = True
            patched.append(module.get("topic"))

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
