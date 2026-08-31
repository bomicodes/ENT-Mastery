"""v34.7 — facelift/rhytidectomy expanding-hematoma recognition and rescue.

Bounded follow-on to v34.6. Adds a high-consequence postoperative hematoma layer to the
canonical Aging Face / Injectables / Resurfacing card without creating a duplicate
rhytidectomy topic or changing facial-plastics taxonomy.
"""

import re

DOMAIN = "Facial Plastics / Trauma"
TOPIC = "aging face injectables resurfacing"


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _extend_sources(module, sources):
    module["source_basis"] = list(dict.fromkeys(list(module.get("source_basis") or []) + list(sources)))


def apply_facialplastics_facelift_hematoma_rescue_v347(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []

    for module in modules or []:
        if _norm(module.get("topic")) != TOPIC:
            continue

        module["manage"] = (
            str(module.get("manage") or "")
            + " FACELIFT HEMATOMA COMMITMENT POINT: after rhytidectomy/facelift, new asymmetric or rapidly progressive facial/neck swelling, "
              "increasing pain or pressure, tense ecchymosis, brisk drain output, skin-flap duskiness, or progressive dysphagia/airway symptoms should trigger immediate assessment for an expanding hematoma. "
              "A small, stable, nonexpanding collection is not the same problem as a tense or enlarging hematoma. The latter can compromise skin-flap perfusion and, when the cervical component is substantial, can threaten the airway; do not passively observe a progressive tension hematoma while waiting for routine imaging. "
              "Reassess blood pressure and contributing anticoagulant/coagulopathy issues in parallel, because perioperative hypertension is a reproducible hematoma risk factor, but medical correction does not replace source control once a major hematoma is present."
        )
        module["operate"] = (
            str(module.get("operate") or "")
            + " EXPANDING-HEMATOMA BAILOUT: a rapidly expanding or tense post-facelift hematoma with threatened flap viability, active bleeding, severe pain/pressure, or airway progression requires prompt decompression and definitive hemostasis rather than repeated needle aspiration alone. "
              "Coordinate airway support when cervical swelling is compromising ventilation or access. Release constricting dressings/closure as needed for urgent decompression, return to the operative field for evacuation when indicated, remove clot enough to expose the bleeding bed, identify and control the source, irrigate and perform a deliberate hemostasis check, then reassess flap color, capillary refill/tension and the need for drainage before reclosure. "
              "Treat severe hypertension, nausea/retching and correctable coagulopathy concurrently; none should delay evacuation of a clearly expanding tension hematoma. After evacuation, continue close surveillance for reaccumulation and skin-flap ischemia/necrosis."
        )
        module["teach"] = (
            str(module.get("teach") or "")
            + " CHIEF RESCUE FRAME: SMALL/STABLE COLLECTION may be managed selectively; EXPANDING/TENSE HEMATOMA is a different entity. "
              "Recognize progressive swelling/pressure and flap compromise -> assess airway and hemodynamics -> DECOMPRESS/EVACUATE when major -> FIND AND CONTROL THE BLEEDING SOURCE -> correct BP/coagulopathy/nausea in parallel -> reassess flap perfusion and recurrence. "
              "The resident should know why this is time-sensitive: sustained subflap pressure can impair perfusion and convert a reversible bleeding complication into skin-flap necrosis."
        )
        module["tags"] = list(dict.fromkeys(list(module.get("tags") or []) + [
            "rhytidectomy", "facelift", "expanding hematoma", "postoperative hemorrhage", "skin flap ischemia", "blood pressure", "hematoma evacuation"
        ]))
        _extend_sources(module, [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — facial rejuvenation/rhytidectomy and postoperative complication principles",
            "K.J. Lee's Essential Otolaryngology, 12e — facial plastic surgery and postoperative bleeding framework",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e, Ch 8 — Rhytidoplasty (Rhytidectomy, Facelift) and Complications of Rhytidectomy/Brow Lift/Liposurgery",
            "Azzi JL et al. Prevention of Hematoma in Patients Undergoing Facelift (Rhytidectomy): A Systematic Review and Meta-Analysis. Facial Plast Surg Aesthet Med. 2026;28(3):260-266 — contemporary hematoma incidence and prevention evidence",
            "Stewart CM et al. Evidence of Hematoma Prevention After Facelift. Aesthet Surg J. 2024;44(2):134-143 — perioperative hematoma risk factors and prevention framework",
            "Baker DC. Expanding hematoma in face-lift surgery: literature review, case presentations, and caveats. Dermatol Surg. 2005;31(9 Pt 2):1139-1144 — prompt recognition/treatment of expanding hematoma and flap-ischemia risk",
            "Ramanadham SR et al. Evolution of hypertension management in face lifting in 1089 patients: optimizing safety and outcomes. Plast Reconstr Surg. 2015;135(6):1037e-1043e — perioperative hypertension as a modifiable hematoma risk factor"
        ])
        module["facialplastics_facelift_hematoma_rescue_v347"] = True
        module["semantic_role_v347"] = "post-rhytidectomy expanding-hematoma recognition, decompression, definitive hemostasis, and flap rescue"
        patched.append(module.get("topic"))

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
