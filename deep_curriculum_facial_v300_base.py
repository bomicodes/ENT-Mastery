"""v30.0 — source-grounded NOE fracture Concept Hub rebuild.

Separates the broad NOE fracture diagnostic/classification card from the operative
mechanics card. The parent card owns recognition, CT mapping, Markowitz-Manson type,
associated injuries, and indications; the mechanics card owns reduction sequence,
medial canthal tendon-bearing fragment control, buttress restoration, fixation, and
secondary deformity prevention.
"""

import re

DOMAIN = "Facial Plastics / Trauma"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


NOE_V300 = {
    "noe fracture": {
        "recognize": (
            "Recognize a naso-orbito-ethmoid (NOE) fracture as a CENTRAL MIDFACE injury involving the confluence of the nasal bones, frontal process of the maxilla, medial orbit/ethmoid region, and the bone supporting the medial canthal tendon (MCT). Do not label a displaced nasal fracture as NOE merely because the nasal bones are comminuted. Clinical clues include traumatic telecanthus, flattening/widening of the nasal bridge, medial orbital step-off, epiphora, nasal obstruction, CSF rhinorrhea, diplopia, and associated frontal sinus, orbital, Le Fort, or panfacial injury. The high-yield distinction is whether the MCT remains attached to a usable central bone fragment."
        ),
        "localize": (
            "Localize the injury on thin-cut maxillofacial CT before deciding treatment. Map unilateral versus bilateral injury; displacement/comminution of the central fragment; integrity of the nasofrontal and medial maxillary/nasomaxillary buttresses; medial orbital wall and floor; nasal dorsal support; frontal sinus/anterior skull-base involvement; lacrimal drainage pathway; and the relationship of the MCT to its bony insertion. Use the Markowitz-Manson framework: Type I = MCT attached to one substantial fragment; Type II = MCT attached to a comminuted but still identifiable bone fragment; Type III = MCT avulsed from its bony insertion. Classification describes the tendon-bearing segment—it does not replace a full CT map of the orbit, skull base, and nasal airway."
        ),
        "workup": (
            "Evaluate the patient as facial trauma first: stabilize life-threatening injury, document vision and globe status, extraocular movements/diplopia, pupils, facial sensation, occlusion, nasal airway, intercanthal distance, lacrimal symptoms, and CSF leak signs. Obtain thin-cut CT with multiplanar reconstructions; 3-D reconstructions can help understand complex displacement but do not substitute for axial/coronal review. Carefully assess the globes before manipulating the midface and identify associated frontal sinus/posterior table or skull-base injury because these can alter timing and exposure. Palpation or gentle traction of the medial canthal region may help assess tendon-bearing fragment mobility, but classification is ultimately a synthesis of examination and CT—not a bedside pull test alone."
        ),
        "manage": (
            "Manage according to displacement, functional deformity, and stability rather than fracture name alone. Truly nondisplaced injuries with preserved canthal position, stable nasal projection, no orbital/airway functional problem, and reliable follow-up may be observed. Displacement causing telecanthus, loss of nasal projection, unstable central fragments, orbital-volume disturbance, lacrimal or nasal-airway problems, or associated fractures requiring exposure generally favors operative repair once the patient and soft tissues permit. Coordinate ophthalmology, neurosurgery, or other facial-trauma teams when globe, skull-base/CSF, or complex panfacial injuries coexist. Delayed repair is harder because malpositioned canthal and central facial relationships scar in quickly."
        ),
        "operate": (
            "The broad operative objective is to restore CENTRAL FACIAL WIDTH, PROJECTION, and ORBITAL/CANTHAL SYMMETRY. Obtain enough exposure to see the stable peripheral skeleton and the MCT-bearing fragment; reconstruct the facial buttress framework before accepting the apparent position of small comminuted pieces. Preserve a viable tendon-bearing fragment whenever possible. Type I injuries often permit rigid fixation of that fragment; Types II and III more often require specialized control of comminution and, for Type III, canthopexy/re-creation of a secure MCT attachment. Restore nasal dorsal support when comminution has destroyed it and address associated orbital or frontal injuries in the same anatomic plan when indicated."
        ),
        "teach": (
            "Chief/boards framework: NOE = CENTRAL MIDFACE + MCT. Ask three questions: (1) Is this truly an NOE injury rather than an isolated nasal fracture? (2) What happened to the MCT-bearing segment—Type I, II, or III? (3) What associated orbital, lacrimal, frontal-sinus/skull-base, and buttress injuries must be repaired with it? Type I has a single substantial MCT-bearing fragment; Type II has comminution but the tendon remains attached to bone; Type III means tendon avulsion from bone. Telecanthus after repair usually reflects failure to restore the canthal-bearing framework, not simply inadequate nasal-bone reduction."
        ),
        "tags": [
            "NOE fracture", "naso-orbito-ethmoid fracture", "Markowitz-Manson",
            "medial canthal tendon", "telecanthus", "central midface trauma",
            "nasomaxillary buttress", "lacrimal injury", "frontal sinus fracture"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — facial trauma, naso-orbito-ethmoid injury, orbital and frontal-sinus relationships",
            "K.J. Lee's Essential Otolaryngology, 12e — facial fracture evaluation and NOE trauma principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — facial trauma classification, examination, and repair pearls",
            "AO CMF Surgery Reference — NOE Type I/II/III definitions and operative principles, including MCT-bearing fragment integrity, buttress restoration, CSF/globe assessment, and canthal reconstruction",
            "Leader et al., J Oral Maxillofac Surg 2024 — systematic review of NOE repair techniques after adoption of the Markowitz classification",
        ],
    },
    "noe fracture mechanics": {
        "recognize": (
            "Recognize the MECHANICS problem in NOE reconstruction: success depends less on collecting every comminuted fragment than on restoring the load-bearing central framework and recreating the correct medial canthal position. The key technical failures are persistent increased intercanthal distance, lateralized or asymmetric MCT position, loss of nasal dorsal projection, medial orbital malposition, and unstable comminution. This card therefore starts after the diagnosis/classification decision and focuses on how the reconstruction is built."
        ),
        "localize": (
            "Build an operative map from STABLE TO UNSTABLE structures. Identify stable frontal bone/nasofrontal junction, medial orbital rims, frontal process of maxilla/nasomaxillary buttresses, intact orbital rim segments, and the MCT-bearing bone. Determine whether the tendon is attached to a plateable fragment (Type I), attached to a small comminuted central fragment that must be captured and stabilized (Type II), or detached from bone and requiring formal reattachment/canthopexy (Type III). Also identify where nasal dorsal support has been lost and whether the medial orbital wall/floor requires reconstruction."
        ),
        "workup": (
            "Before fixation, translate the CT into a REDUCTION SEQUENCE rather than entering the operation with only a fracture list. Decide the exposure required to visualize stable reference points, measure/compare canthal position clinically, and plan whether rigid plates alone can control the MCT-bearing segment or whether transnasal/intercanthal fixation or canthopexy will be needed. Confirm that globe, lacrimal, frontal-sinus, and skull-base issues have been addressed in the operative plan. In severe comminution, plan graft material or structural support for the nasal dorsum rather than expecting tiny fragments to recreate projection by themselves."
        ),
        "manage": (
            "Use a FRAMEWORK-FIRST strategy: restore stable buttress relationships and central facial width/projection, then secure the canthal-bearing segment into that reconstructed framework. Do not accept a reduction merely because the nasal bones look straight from the front. Recheck intercanthal symmetry, medial orbital contour, nasal projection, and airway before final closure. Intercanthal wiring is a tool rather than an automatic requirement; contemporary series support selective use, particularly when comminution or instability prevents rigid fixation alone from reliably restoring the canthal relationship."
        ),
        "operate": (
            "Operative mechanics: expose enough stable skeleton for anatomic reference; reduce and rigidly fix the major central buttresses; anatomically position the MCT-bearing fragment; then secure it without lateralizing the tendon. In Type I, direct plate fixation of the large central fragment may restore canthal position. In Type II, capture the tendon-bearing comminuted segment and stabilize it to the reconstructed framework; transnasal/intercanthal wiring may be useful when plating alone cannot control the segment. In Type III, the tendon has lost bony attachment, so secure canthopexy to a stable position that recreates the posterior-medial canthal vector rather than simply pulling the canthus medially. Restore nasal dorsal/caudal support with structural grafting when comminution has eliminated a reliable bony scaffold. Before closure, compare both canthi and confirm that plates/wires do not create visible contour problems beneath thin medial-canthal skin."
        ),
        "teach": (
            "Chief/boards mechanics: REDUCE THE FRAME → RESTORE THE MCT → RESTORE THE NOSE. A Type III fracture is not solved by plating nasal fragments because the MCT is avulsed. Type II is not synonymous with mandatory transnasal wiring: the question is whether the MCT-bearing fragment can be stably and anatomically controlled. Persistent telecanthus means the canthal complex was left too lateral, unstable, or attached to the wrong vector. Severe NOE fractures also require deliberate nasal-support reconstruction; otherwise a technically united fracture can heal with a widened, flattened central face."
        ),
        "tags": [
            "NOE fracture mechanics", "medial canthal tendon fixation", "intercanthal wiring",
            "transnasal wiring", "canthopexy", "telecanthus", "NOE ORIF",
            "central facial buttress", "nasal dorsal graft"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — NOE exposure, fixation, medial canthal reconstruction, and secondary deformity prevention",
            "K.J. Lee's Essential Otolaryngology, 12e — facial fracture repair principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — NOE operative pearls and facial trauma reconstruction",
            "AO CMF Surgery Reference — NOE ORIF principles, Type III canthopexy, restoration of intercanthal distance, nasal support, and associated globe/CSF evaluation",
            "Leader et al., J Oral Maxillofac Surg 2024 — systematic review of NOE repair techniques",
            "Naso-Orbito-Ethmoid Fractures: Refining the Role of Wires and Plates (2025) — selective role of intercanthal wiring in restoring intercanthal distance",
        ],
    },
}


def apply_facial_noe_rebuild_v300(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = NOE_V300.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v300"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
