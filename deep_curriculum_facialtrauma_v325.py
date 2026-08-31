"""v32.5 — source-grounded mandible-fracture vs biomechanics/occlusion rebuild.

Keeps the parent trauma card and the advanced mechanics card clinically distinct:
1) Mandible Fracture = recognition, fracture mapping, treatment branch, and complications.
2) Mandibular Biomechanics and Occlusion = force vectors, occlusal reduction, load sharing/
   load bearing, fixation geometry, and failure analysis.
"""

import re

DOMAIN = "Facial Plastics / Trauma"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


MANDIBLE_REBUILD_V325 = {
    "mandible fracture": {
        "recognize": (
            "This card owns the CLINICAL MANDIBLE-TRAUMA PATHWAY, not plate biomechanics. After trauma stabilization, suspect fracture with malocclusion, trismus, pain with jaw movement, segment mobility/step-off, gingival laceration, sublingual ecchymosis, missing or fractured teeth, lower-lip/chin sensory change, or deviation on opening. Bilateral anterior body/parasymphyseal injury can allow posterior displacement of the tongue-bearing segment and create an airway problem. Document the patient's PREINJURY occlusion whenever possible; the postoperative target is the patient's baseline bite, not an abstract Angle Class I bite that the patient may never have had."
        ),
        "localize": (
            "Map every fracture by region and by what it changes: symphysis/parasymphysis, body, angle, ramus, coronoid, subcondylar/condylar neck, and condylar head. Then describe displacement, comminution, dentition, open communication through tooth-bearing mucosa/skin, inferior-alveolar-nerve findings, and associated midface injury. A chin impact should trigger a deliberate search for bilateral condylar injury; an apparent single fracture should trigger review of the entire mandibular ring for a second injury. Favorable/unfavorable orientation predicts muscle-driven displacement, but it does not by itself dictate the definitive operation."
        ),
        "workup": (
            "Examine occlusion before repeated manipulation: prematurity, open bite, crossbite, dental midlines, missing/loose teeth, wear facets, and any known pre-existing asymmetry. Assess maximal opening, deviation, floor-of-mouth swelling, mucosal wounds, tooth viability, V3 sensation, and TMJ/condylar tenderness. Thin-cut maxillofacial CT is the usual trauma study when clinically significant mandibular injury is suspected or facial injuries are complex; panoramic imaging can add useful dental/fracture information in selected stable patients. Identify teeth/root apices and the inferior alveolar canal because they constrain screw position. The BIOMECHANICS card owns how those findings become a fixation construct."
        ),
        "manage": (
            "Choose observation/soft diet, closed treatment with guiding elastics/MMF, or ORIF according to displacement, occlusal stability, fracture pattern, dentition, associated injuries, ability to rehabilitate, and patient factors. Nondisplaced stable fractures with preserved occlusion may be managed nonoperatively in reliable patients. ORIF is favored when stable anatomic/functional reduction cannot be maintained closed, including many displaced tooth-bearing fractures and selected significantly displaced extracapsular condylar injuries. Condylar management remains individualized: preserve or restore ramus height and function while avoiding prolonged immobilization that promotes stiffness/ankylosis. Do not turn historical lists of condylar 'absolute indications' into a substitute for current anatomy and function."
        ),
        "operate": (
            "The parent-card operative sequence is: establish the intended occlusion -> expose with protection of tooth roots, mental/inferior-alveolar nerve and facial nerve as relevant -> anatomically reduce the fracture -> apply a fixation construct appropriate to the pattern -> RELEASE MMF/temporary occlusal fixation and verify the bite and mandibular motion before closure. A visually aligned inferior border with a wrong bite is a failed reduction. In multiple fractures, rebuild a stable mandibular framework and repeatedly recheck width/ramus height/occlusion so fixation of one segment does not lock in lingual splay or gonial flaring. The detailed force-vector and plate-selection logic lives in the separate BIOMECHANICS card."
        ),
        "teach": (
            "Chief/boards frame: MANDIBLE FRACTURE asks, 'Where are all the fractures, what happened to the patient's occlusion/ramus height/airway, and does this pattern need observation, closed treatment, or ORIF?' Always document preinjury bite, inspect the whole mandibular ring, and reassess occlusion after fixation. Complications to recognize include malocclusion/malunion, nonunion, infection/osteomyelitis, hardware exposure/failure, dental injury, inferior-alveolar/mental neuropathy, facial-nerve injury from external approaches, and TMJ stiffness. Do not duplicate Champy/load-bearing details here; that is the job of the mechanics card."
        ),
        "tags": ["mandible fracture", "malocclusion", "condylar fracture", "MMF", "ORIF", "inferior alveolar nerve", "mandibular trauma", "ramus height"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — mandibular trauma evaluation, occlusion, fracture patterns, and treatment principles",
            "K.J. Lee's Essential Otolaryngology, 12e — craniomaxillofacial trauma and mandibular fracture management",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — facial trauma examination, mandibular fracture classification and management",
            "AO CMF Surgery Reference — mandibular fracture reduction/fixation principles and postoperative occlusion verification",
        ],
    },
    "mandibular biomechanics and occlusion": {
        "recognize": (
            "This is an ADVANCED FIXATION-REASONING card, not a second mandible-fracture workup. Treat the mandible as a curved load-bearing beam exposed to bending, torsion and muscle-driven distraction. During common functional loading, the tooth-bearing/alveolar border often experiences distracting (tension) forces while the inferior border is relatively compressed; the exact force pattern changes with fracture site and loading. The fixation question is therefore not 'which plate do I always use?' but 'what forces remain after reduction, how much bone can share them, and where can fixation safely neutralize them?'"
        ),
        "localize": (
            "Localize the MECHANICAL FAILURE MODE. Simple well-reduced fractures with broad bony contact can share functional load with smaller fixation. Comminution, segmental defects, severe atrophy, infected bone after debridement, or inadequate buttressing behave as load-bearing problems because the plate must bridge forces the bone cannot transmit. In the anterior mandible, curvature and muscular loading add torsion, so a single weak point of fixation can permit lingual splay/rotation. At the angle, elevator/depressor forces create combined tension, compression and torsion. Translate CT geometry into the force vector before selecting hardware."
        ),
        "workup": (
            "Build the fixation plan from four inputs: BASELINE OCCLUSION, bone contact/quality, fracture geometry, and safe screw corridors. Use wear facets, dental midlines, preinjury photographs/dental records when available, and the maxillary dentition as a template; Angle class is descriptive, not a command to 'normalize' a patient's longstanding bite. Decide whether an arch bar/MMF will function only as temporary reduction assistance or also as a tension band. Map tooth roots, mental foramina and the inferior alveolar canal before choosing monocortical versus bicortical screw corridors. For multiple fractures, decide which large stable segments will restore mandibular width and continuity first."
        ),
        "manage": (
            "LOAD SHARING means the reduced bone buttresses across the fracture and transmits part of functional force, allowing appropriately placed miniplates/lag screws in suitable simple patterns. Champy's ideal osteosynthesis lines are a load-sharing concept, not permission to use one miniplate for every fracture. LOAD BEARING means the reconstruction construct must carry essentially all functional load across an unstable/comminuted/defect/markedly atrophic segment; use a sufficiently rigid bridging construct fixed into healthy bone. If reduction leaves a gap or the inferior border is not buttressed, ask whether the case has silently converted from load sharing to load bearing."
        ),
        "operate": (
            "Mechanical sequence: reproduce occlusion with temporary MMF/elastics -> reduce bone without letting the fixation device create distraction -> control rotation/width -> apply fixation along safe force-neutralizing corridors -> release MMF and stress-test the result by checking bilateral posterior contacts, midlines, mandibular excursion and fracture stability. In body/angle simple patterns, an appropriately placed superior monocortical miniplate can neutralize the tension zone when the basal cortex is well reduced; in symphyseal/parasymphyseal fractures, torsion usually requires TWO POINTS of stabilization unless a sufficiently rigid load-bearing construct is used. Lag screws compress only when their geometry truly creates gliding and purchase across appropriate fragments; otherwise tightening can displace the reduction."
        ),
        "teach": (
            "Boards/mechanics algorithm: 1) establish the patient's bite; 2) reduce the fracture so bone can share load when possible; 3) identify tension/compression/torsion; 4) ask whether bone stock/buttressing permits LOAD SHARING; 5) if not, bridge with LOAD-BEARING fixation; 6) protect roots and the inferior alveolar nerve; 7) release MMF and verify occlusion before closure. AO CMF specifically treats severely atrophic, comminuted and defect patterns as load-bearing problems, while simple buttressed fractures can use load-sharing constructs. An occlusal error after rigid fixation is not something elastics should be expected to rescue if the skeleton was fixed in the wrong position."
        ),
        "tags": ["mandibular biomechanics", "occlusion", "load sharing", "load bearing", "Champy", "tension band", "torsion", "lag screw", "reconstruction plate", "MMF"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — mandibular biomechanics, occlusal restoration and fixation principles",
            "K.J. Lee's Essential Otolaryngology, 12e — tension/compression behavior, ideal osteosynthesis lines, miniplate/reconstruction-plate and lag-screw principles",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — favorable/unfavorable mandibular fractures, occlusion and fixation concepts",
            "AO CMF Surgery Reference: Load bearing vs load sharing; mandibular symphysis/body/angle ORIF principles — contemporary fixation geometry and indications for load-bearing constructs",
        ],
    },
}


def apply_mandible_biomechanics_rebuild_v325(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = MANDIBLE_REBUILD_V325.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v325"] = True
        module["semantic_role_v325"] = (
            "clinical fracture mapping, treatment branching, and complication recognition"
            if key == "mandible fracture"
            else "occlusal reduction, force-vector analysis, and load-sharing/load-bearing fixation reasoning"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
