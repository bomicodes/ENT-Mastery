"""v32.4 — NOE fracture clinical framework versus fixation-mechanics separation.

The duplicate audit identifies full title containment between NOE Fracture and NOE Fracture
Mechanics. Preserve both, but make the first the ACUTE DIAGNOSIS/INJURY-MAPPING card and
the second the OPERATIVE BIOMECHANICS/FIXATION card. The mechanics card must assume that
the learner already knows the Markowitz pattern and should not re-teach generic trauma workup.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


NOE_REBUILD_V324 = {
    "noe fracture": {
        "recognize": (
            "Use this card for ACUTE NOE INJURY RECOGNITION AND MAPPING. Suspect a naso-orbito-ethmoid injury after high-energy central midface trauma with flattening/loss of nasal projection, widened or rounded medial canthi, epiphora, severe periorbital edema, nasal obstruction/epistaxis, or associated CSF rhinorrhea. Telecanthus can be subtle early; do not exclude NOE injury because swelling obscures the deformity. Document vision, pupils, extraocular movements, globe position, medial canthal stability/bowstring behavior, nasal/septal injury, lacrimal symptoms, and neurologic/skull-base findings before edema and operative manipulation change the exam."
        ),
        "localize": (
            "Localize the injury around the CENTRAL FRAGMENT that carries the medial canthal tendon (MCT), not simply the nasal bones. Markowitz-Manson: Type I = MCT attached to a sufficiently large, relatively intact central fragment; Type II = MCT remains attached to a comminuted/small central fragment; Type III = MCT avulsed from its bony attachment. Then map associated medial orbital wall/floor, frontal process of maxilla, nasal root/septum, nasolacrimal apparatus, frontal sinus/anterior skull base, and panfacial fractures. The classification predicts what structure must ultimately be stabilized; it is not itself an operative recipe."
        ),
        "workup": (
            "After trauma stabilization, obtain thin-cut maxillofacial/orbital CT with multiplanar reconstructions for fracture displacement, comminution, central-fragment geometry, orbital volume, frontal sinus/skull-base extension and associated injuries. Ophthalmic emergency findings take precedence over reconstructive planning. Evaluate suspected CSF leak and lacrimal/canalicular injury selectively with the appropriate teams; epiphora immediately after trauma can reflect edema and does not by itself mandate primary DCR. Preinjury photographs can help establish native intercanthal distance, nasal width and dorsal projection when available."
        ),
        "manage": (
            "Management is driven by displacement, instability and functional/aesthetic derangement rather than by a memorized label alone. Protect the globe, address septal hematoma and urgent orbital/skull-base problems, and plan timely anatomic reconstruction for displaced/unstable NOE injuries because secondary correction of telecanthus and loss of nasal projection is substantially harder. The clinical goals are restoration of medial canthal position, nasal root/dorsal projection, orbital volume/medial wall support and a functional lacrimal pathway while coordinating associated frontal sinus, skull-base and panfacial injuries."
        ),
        "operate": (
            "This parent card stops at OPERATIVE PLAN FORMULATION: obtain sufficient exposure to identify stable reference bone, the central fragment/MCT relationship, medial orbital boundaries and nasal support; decide whether the MCT-bearing fragment is rigidly fixable or requires canthal fixation; and coordinate orbital/nasal/skull-base reconstruction. Detailed plate/wire vectors, stable-to-unstable sequencing and transnasal fixation belong to the companion 'NOE Fracture Mechanics' card. Avoid the common conceptual error of treating NOE repair as a nasal-bone reduction with canthal wiring added at the end."
        ),
        "teach": (
            "Boards/chief discriminator: NOE FRACTURE = FIND THE CENTRAL FRAGMENT AND ASK WHETHER THE MCT IS ATTACHED TO A FIXABLE PIECE OF BONE. Type I: large fixable MCT-bearing fragment. Type II: tendon attached, fragment comminuted/small. Type III: tendon avulsed. Also look deliberately for ocular injury, lacrimal injury, CSF/skull-base extension and loss of nasal projection. This card answers WHAT IS INJURED and WHAT MUST BE RESTORED—not the fixation mechanics."
        ),
        "tags": ["NOE fracture", "naso-orbito-ethmoid", "Markowitz", "medial canthal tendon", "central fragment", "telecanthus", "nasal projection", "lacrimal injury", "skull base trauma"],
        "source_basis": [
            "K.J. Lee's Essential Otolaryngology, 12e — craniomaxillofacial trauma: NOE recognition, central-fragment/MCT classification, and need for early anatomic repair",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — NOE anatomy, bowstring/telecanthus findings, lacrimal and skull-base associations, and MCT-centered management",
            "Leader & Gal, J Oral Maxillofac Surg 2024 — systematic review of NOE repair techniques after adoption of the Markowitz classification",
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — facial trauma and NOE reconstruction framework (textbook backbone; current technique details cross-checked against contemporary review)",
        ],
    },
    "noe fracture mechanics": {
        "recognize": (
            "Use this card only AFTER the NOE injury has been classified and the reconstruction is indicated. The operative problem is not 'telecanthus' in the abstract; it is loss of a stable three-dimensional medial orbital/nasal framework that can hold the MCT at its native posterior-superior-medial vector. Determine whether the MCT-bearing central fragment can accept reliable rigid fixation, whether the medial orbital wall must first be rebuilt to provide a stable anchor, and whether nasal dorsal support/projection has been lost."
        ),
        "localize": (
            "Think in FIXATION VECTORS and REFERENCE POINTS. Rebuild from stable craniofacial bone toward the comminuted NOE segment; restore medial orbital buttress/volume and nasal root width/projection before accepting canthal position. A Type I central fragment is useful because rigidly fixing that fragment can restore the tendon indirectly. In Type II, the tendon-bearing fragment may be too small/comminuted for dependable plating, so transnasal canthal fixation may be needed. In Type III, the avulsed tendon itself requires secure reattachment. The reconstructed MCT vector must resist its tendency to drift anteriorly, laterally and inferiorly."
        ),
        "workup": (
            "The 'workup' here is PREOPERATIVE GEOMETRY, not repeat trauma screening. Review thin-cut CT specifically for stable superior/lateral fixation points, central-fragment size, medial orbital wall loss, bilateral symmetry, nasal bone/root telescoping, nasofrontal/frontal sinus extension and the route of any planned transnasal wire or permanent fixation. Use the opposite side and preinjury appearance as references when reliable. Anticipate whether bone grafting is required to recreate the medial orbit or nasal dorsal support before attempting final canthal tension."
        ),
        "manage": (
            "MECHANICS ALGORITHM: (1) expose enough stable anatomy; (2) reduce and rigidly fix reconstructable bony buttresses/central fragments from stable to unstable; (3) restore the medial orbital wall when deficient so the canthal anchor has a skeletal foundation; (4) restore nasal root width and dorsal projection; (5) secure the MCT-bearing fragment or tendon with plate/screw fixation when truly stable, or transnasal wire/permanent fixation when comminution/avulsion prevents reliable fragment fixation; (6) set symmetric intercanthal position with the vector posterior, superior and medial; (7) verify globe/orbital relationships, nasal projection and canthal symmetry before closure."
        ),
        "operate": (
            "A plate is only useful if it controls a fragment large enough to transmit MCT force without secondary displacement. Transnasal fixation is therefore a biomechanical solution for Type II/III patterns, not a ritual for every NOE fracture. When used, place fixation so the canthus is drawn toward a stable contralateral or reconstructed medial-orbital anchor rather than merely narrowing the skin-level intercanthal distance. Avoid low/anterior fixation, which can leave canthal rounding, scleral show or recurrent telecanthus. Do not sacrifice restoration of nasal projection: a perfectly narrowed intercanthal distance on a flattened, widened nasal root is still a poor NOE reconstruction."
        ),
        "teach": (
            "Boards/chief discriminator: NOE MECHANICS = WHAT STRUCTURE WILL ACTUALLY HOLD THE MCT IN THE CORRECT 3-D VECTOR? Large stable central fragment -> rigidly fix the fragment. Comminuted fragment or avulsed tendon -> build a stable medial orbital/nasal framework, then use transnasal/permanent fixation as needed. Reconstruct bone before asking soft tissue to hold the face together. The 2024 systematic review found plates/screws and transnasal wiring remain the dominant techniques but the evidence base is mostly low level, so teach principles and geometry rather than one universal exposure or wiring recipe."
        ),
        "tags": ["NOE mechanics", "central fragment fixation", "transnasal wiring", "medial orbital buttress", "medial canthal tendon vector", "stable-to-unstable fixation", "nasal projection", "telecanthus repair"],
        "source_basis": [
            "K.J. Lee's Essential Otolaryngology, 12e — Type I fragment fixation versus Type II/III transnasal fixation; posterior-superior-medial MCT vector; stable-to-unstable craniofacial repair",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — rebuild medial orbital wall before MCT repair and recreate posterior/superior canthal pull",
            "Leader & Gal, J Oral Maxillofac Surg 2024 — systematic review: open exposure with miniplates/screws and transnasal wiring remain common; evidence is predominantly level IV",
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — operative facial-trauma anatomy and reconstruction principles",
        ],
    },
}


def apply_noe_rebuild_v324(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = NOE_REBUILD_V324.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v324"] = True
            module["semantic_role_v324"] = (
                "acute NOE recognition, injury mapping, Markowitz classification, and reconstructive goals"
                if key == "noe fracture"
                else "three-dimensional central-fragment, medial-orbital, nasal-support, and canthal fixation mechanics"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
