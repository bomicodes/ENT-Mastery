"""v34.4 — separate general local-flap reconstruction from paramedian forehead-flap nasal reconstruction.

Bounded Concept Hub rebuild. The parent local-flap card should teach movement geometry,
vascularity, tension-vector planning, and facial-subunit selection. The forehead-flap card
should own staged axial nasal reconstruction, three-layer defect analysis, supratrochlear
vascular anatomy, lining/support/cover sequencing, and pedicle division/refinement.
"""

import re

DOMAIN = "Facial Plastics / Trauma"


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _extend_sources(module, sources):
    module["source_basis"] = list(dict.fromkeys(list(module.get("source_basis") or []) + list(sources)))


def apply_facialplastics_local_forehead_v344(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []

    for module in modules or []:
        topic = _norm(module.get("topic"))

        if topic == "local flap reconstruction":
            module["recognize"] = (
                "This card owns GENERAL FACIAL LOCAL-FLAP DECISION-MAKING, not the staged paramedian forehead flap. "
                "Start with the defect: size, depth, vascular bed, exposed cartilage/bone/nerve, aesthetic subunit, free-margin involvement, "
                "skin laxity, scar orientation, and whether adjacent tissue can be recruited without distorting the eyelid, lip, nasal ala, "
                "brow, or hairline. Choose a local flap only when vascularized neighboring tissue can restore coverage with an acceptable donor deformity."
            )
            module["localize"] = (
                "Name the MOVEMENT before naming the flap. Advancement moves tissue primarily along one vector; rotation pivots an arc of tissue into a defect; "
                "transposition moves tissue over intervening intact skin; interpolation crosses intact skin on a pedicle and therefore requires later pedicle division. "
                "Bilobed flaps are double-transposition flaps that redistribute closure tension and are commonly used for selected small distal-nasal defects. "
                "Rhombic and nasolabial/melolabial designs solve different geometry and tissue-match problems. The best flap recruits laxity from where the face can spare it."
            )
            module["workup"] = (
                "Reconstruct from the inside out: confirm oncologic clearance when applicable, assess depth and missing support, then mark relaxed skin-tension lines, "
                "aesthetic-unit boundaries, natural creases and the intended tension vector before infiltration distorts landmarks. Ask whether primary closure, secondary "
                "intention, a skin graft, or a regional/interpolated flap would produce a better functional result. A local flap is not automatically superior merely because "
                "it provides color-matched skin."
            )
            module["manage"] = (
                "Design around BLOOD SUPPLY + TENSION. Preserve a broad viable base for random-pattern flaps, avoid unnecessary narrowing or torsion, undermine in the correct "
                "anatomic plane to gain mobility, and distribute tension away from free margins. Dog-ears, standing cones and Burrow triangles are geometry problems; pincushioning "
                "is favored by concentric scar contraction, thick subcutaneous tissue and poor lymphatic drainage. On the nose, use bilobed or other local flaps selectively rather "
                "than allowing a convenient design to distort multiple subunits or retract the alar rim."
            )
            module["operate"] = (
                "Operate by VECTOR, not by memorized drawing. Size the flap after the true defect is known, incise cleanly, elevate without injuring the vascular base, mobilize enough "
                "that the flap reaches without excessive tension, obtain meticulous hemostasis, and inset the key functional edge first. Check eyelid closure/ectropion risk, oral competence, "
                "alar position and nasal-valve shape before final sutures. If the defect needs independent lining, cartilage/bone support, or substantially more surface area than adjacent tissue "
                "can safely provide, escalate reconstruction instead of stretching a local flap beyond its job."
            )
            module["teach"] = (
                "BOARDS/CHIEF FRAME: LOCAL FLAP = 'Where is the expendable adjacent laxity, what movement recruits it, what is the vascular basis, and where will the closure tension go?' "
                "Know advancement versus rotation versus transposition versus interpolation, and protect facial free margins from the secondary vector. This card is the geometric toolkit; it does "
                "not substitute for the dedicated staged nasal-reconstruction algorithm of a paramedian forehead flap."
            )
            module["tags"] = list(dict.fromkeys(list(module.get("tags") or []) + [
                "local flap", "advancement flap", "rotation flap", "transposition flap", "interpolation flap", "bilobed flap",
                "tension vector", "random pattern flap", "pincushioning", "aesthetic subunit"
            ]))
            _extend_sources(module, [
                "Cummings Otolaryngology—Head and Neck Surgery, 7e — facial cutaneous reconstruction, local-flap design, and aesthetic-unit principles",
                "K.J. Lee's Essential Otolaryngology, 12e — facial plastic/reconstructive flap principles",
                "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e, Ch 8 — Facial Reconstruction Techniques",
                "Steiger JD. Bilobed flaps in nasal reconstruction. Facial Plast Surg Clin North Am. 2011 — double-transposition geometry and distal-nasal indications",
                "StatPearls: Bilobed Flaps — local transposition mechanics, tension redistribution, design, and complications"
            ])
            module["facialplastics_local_forehead_v344"] = True
            module["semantic_role_v344"] = "general local-flap geometry, vascularity, tissue recruitment, and tension-vector control"
            patched.append(module.get("topic"))

        elif topic == "forehead flap nasal reconstruction":
            module["recognize"] = (
                "This card owns STAGED PARAMEDIAN FOREHEAD-FLAP NASAL RECONSTRUCTION. It is an interpolated AXIAL flap based on the supratrochlear vascular system and is most useful "
                "when a sizable or deep nasal defect cannot be restored reliably with primary closure, a skin graft, or a smaller local flap—particularly distal nasal defects involving multiple "
                "subunits or defects requiring robust vascularized cover over reconstructed support/lining."
            )
            module["localize"] = (
                "Analyze the nose as THREE LAYERS: LINING, STRUCTURAL SUPPORT, and EXTERNAL COVER. A forehead flap replaces external cover; it does not by itself recreate missing vestibular lining "
                "or alar/tip framework. Map the defect by nasal subunit (tip, ala, dorsum, sidewall, soft triangle, columella), consider complete subunit replacement when loss is extensive, and identify "
                "whether cartilage grafting or vascularized lining must be rebuilt before/with cover. The pedicle is centered on the supratrochlear artery near the medial brow/orbital rim."
            )
            module["workup"] = (
                "Confirm final defect dimensions and oncologic clearance, assess forehead height/hairline/scars/prior radiation, smoking and vascular risk, contralateral nasal anatomy for templates, and "
                "whether the patient can tolerate MULTISTAGE reconstruction. Large distal defects, defects roughly >1.5–2 cm, or loss of >50% of an aesthetic subunit commonly push reconstruction toward a "
                "forehead flap, but size alone is not the indication: depth, subunits, lining/support loss and available adjacent tissue matter."
            )
            module["manage"] = (
                "Choose TWO versus THREE stages based on defect complexity, need for intermediate thinning/framework refinement, vascular risk and surgeon plan. In a classic first stage, create lining/support as "
                "needed, template the defect, design a vertically oriented paramedian flap with reliable supratrochlear inflow, elevate in progressively deeper planes toward the brow to protect the pedicle, rotate "
                "without kinking, and inset without excessive distal thinning. Subsequent stages permit contour refinement and finally pedicle division/inset once neovascularization is established."
            )
            module["operate"] = (
                "The operation succeeds by SEQUENCE. Do not cover a poorly designed foundation. Restore internal lining when absent; reconstruct alar/tip/dorsal support with cartilage when required; then provide vascularized "
                "forehead skin as cover. Preserve pedicle width and avoid compression/torsion, thin conservatively at the first transfer when perfusion is most vulnerable, and plan brow/forehead donor closure deliberately. At division, "
                "trim and inset both nasal and brow ends rather than simply cutting the bridge. Watch for venous congestion, distal necrosis, trapdoor/bulk, brow distortion, hair-bearing transfer and nasal-valve compromise."
            )
            module["teach"] = (
                "BOARDS/CHIEF FRAME: PARAMEDIAN FOREHEAD FLAP = 'Does this nose need a staged axial cover solution, and have I separately rebuilt lining + support + cover?' It is based on the SUPRATROCHLEAR system, is usually "
                "at least two stages, and is a workhorse for large/complex distal nasal defects. A forehead flap is not merely a bigger local flap: it is an interpolated staged reconstruction with its own vascular anatomy and sequencing."
            )
            module["tags"] = list(dict.fromkeys(list(module.get("tags") or []) + [
                "paramedian forehead flap", "supratrochlear artery", "nasal reconstruction", "nasal lining", "cartilage support",
                "external cover", "interpolation flap", "two stage forehead flap", "three stage forehead flap", "nasal subunit"
            ]))
            _extend_sources(module, [
                "Cummings Otolaryngology—Head and Neck Surgery, 7e — nasal reconstruction, subunit analysis, lining/support/cover reconstruction",
                "K.J. Lee's Essential Otolaryngology, 12e — facial plastic and nasal reconstructive anatomy",
                "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e, Ch 8 — Facial Reconstruction Techniques",
                "StatPearls: Paramedian Forehead Flaps — supratrochlear axial anatomy, large nasal-defect indications, staged reconstruction, and complications",
                "Correa BJ et al. Nasal Reconstruction: An Overview and Nuances. Semin Plast Surg. 2010 — subunit and three-layer nasal reconstruction principles",
                "Two or Three? Approaches to Staging of the Paramedian Forehead Flap for Nasal Reconstruction. Plast Reconstr Surg Glob Open. 2021 — two- versus three-stage framework"
            ])
            module["facialplastics_local_forehead_v344"] = True
            module["semantic_role_v344"] = "staged supratrochlear axial nasal reconstruction with lining-support-cover sequencing"
            patched.append(module.get("topic"))

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
