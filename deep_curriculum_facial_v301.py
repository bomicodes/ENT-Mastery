"""v30.1 — source-grounded frontal sinus fracture Concept Hub rebuild.

Separates the parent injury-recognition/anatomic-mapping card from the decision-model
card. The parent owns diagnosis, CT mapping, complications, and longitudinal risks;
the decision model owns observation vs contour repair vs sinus-preserving treatment
vs obliteration vs cranialization.
"""

import re

DOMAIN = "Facial Plastics / Trauma"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


FRONTAL_SINUS_V301 = {
    "frontal sinus fracture": {
        "recognize": (
            "Recognize frontal sinus fracture as a HIGH-ENERGY craniofacial injury whose importance is not the forehead laceration alone but the combination of anterior-table contour, posterior-table/anterior-skull-base integrity, frontal sinus outflow tract (FSOT) function, and intracranial injury. Presentations include forehead depression or step-off, laceration, epistaxis, orbital injury, pneumocephalus, or CSF rhinorrhea; some fractures are found only on trauma CT. Late morbidity includes chronic frontal sinusitis, mucocele/mucopyocele, osteomyelitis, contour deformity, and intracranial infection."
        ),
        "localize": (
            "Localize the fracture on thin-cut CT by explicitly mapping THREE compartments: ANTERIOR TABLE, POSTERIOR TABLE, and FRONTAL RECESS/FSOT. For the anterior table, record displacement/comminution and cosmetic contour. For the posterior table, record displacement/comminution, intracranial air, dural injury/CSF leak, and associated skull-base injury. For the FSOT, look for fractures through the inferomedial sinus/frontal recess, displaced fragments or obstruction that threaten drainage. Also map orbit, NOE complex, ethmoid roof, and other panfacial fractures because these can change exposure and reconstruction."
        ),
        "workup": (
            "Treat the patient as major trauma first, then document neurologic status, globe/vision, facial nerve and sensation, forehead contour, nasal findings, and evidence of CSF leak. Thin-cut maxillofacial/head CT with multiplanar review is the key study; 3-D reconstructions can clarify contour but do not substitute for frontal-recess and posterior-table assessment. Suspected persistent CSF leak or significant posterior-table injury should trigger coordinated skull-base/neurosurgical planning. Do not assume FSOT obstruction from fracture proximity alone; the management question is whether drainage is actually disrupted or predictably unsalvageable."
        ),
        "manage": (
            "Manage the INJURY rather than reflexively operating on every radiographic fracture. Nondisplaced or minimally displaced injuries with intact drainage and no concerning intracranial complication are commonly observed. A displaced anterior-table injury may need repair primarily for contour even when the sinus can be preserved. Posterior-table and FSOT injuries require a separate risk assessment because the therapeutic goal is a durable 'safe sinus' while avoiding unnecessary morbidity. Long-term follow-up matters even after successful nonoperative management because mucoceles and chronic sinus complications can present years later."
        ),
        "operate": (
            "When surgery is required, match exposure and reconstruction to the injured compartment. Anterior-table repair restores forehead contour with reduction/fixation or reconstruction. Sinus-preserving strategies may be appropriate when the posterior table and drainage pathway can be made safe. Obliteration requires meticulous mucosal removal and dependable closure of the frontal recess; cranialization removes the posterior table, eliminates sinus function, separates the intracranial space from the sinonasal tract, and reconstructs the anterior contour. Preserve a vascularized pericranial flap when open skull-base reconstruction may be needed."
        ),
        "teach": (
            "Chief/boards framework: FRONT TABLE = CONTOUR; BACK TABLE = BRAIN/DURA; OUTFLOW TRACT = FUTURE SINUS FUNCTION. Never let the amount of anterior-table displacement answer the posterior-table question, and never let a posterior-table fracture automatically force cranialization without considering displacement, CSF leak, comminution, FSOT status, and contemporary sinus-preserving options. The delayed board complication is a mucocele from retained mucosa or obstructed drainage, which is why safe sinus physiology and long-term surveillance matter."
        ),
        "tags": ["frontal sinus fracture", "anterior table", "posterior table", "frontal sinus outflow tract", "frontal recess", "CSF leak", "mucocele", "cranialization", "sinus obliteration"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — frontal sinus trauma, anterior/posterior table injury, outflow tract assessment, and delayed complications",
            "K.J. Lee's Essential Otolaryngology, 12e — frontal sinus fracture evaluation and operative principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — facial trauma and frontal sinus management pearls",
            "AO CMF Surgery Reference — frontal sinus posterior-table, obliteration, cranialization, mucosal removal, recess closure, and safe-sinus principles",
            "Current Concepts in Frontal Sinus Fracture Management (2026) — anatomy-driven assessment, sinus preservation when feasible, and long-term surveillance",
        ],
    },
    "frontal sinus fracture decision model": {
        "recognize": (
            "Recognize the DECISION-MODEL problem: frontal sinus treatment is not a single displacement cutoff. The operation is chosen by the interaction of anterior-table contour, posterior-table severity/dural violation, FSOT patency, CSF leak, associated injuries, and the feasibility of creating a durable safe sinus. Modern practice increasingly favors observation or sinus-preserving/endoscopic strategies when those goals can be met rather than routine open obliteration or cranialization."
        ),
        "localize": (
            "Sort the CT into a decision grid. ANTERIOR TABLE: nondisplaced versus contour-deforming displacement/comminution. POSTERIOR TABLE: minimal versus substantial displacement/comminution, pneumocephalus, dural injury, persistent CSF leak, or tissue loss. FSOT: likely patent, threatened, or clearly obstructed/disrupted. Then add modifiers: open contamination, need for craniotomy for another indication, severe NOE/orbital injury, endoscopic access, and reliability for surveillance. This grid is more useful than memorizing one historical millimeter threshold."
        ),
        "workup": (
            "Before choosing a procedure, answer five questions: (1) Does the anterior table need contour repair? (2) Is the posterior table/dura safe enough to preserve? (3) Is the FSOT patent or reconstructible? (4) Is there a persistent CSF leak or intracranial indication for open access? (5) Can the patient undergo reliable radiographic/endoscopic follow-up? Short-interval reassessment can be appropriate when drainage is uncertain but not clearly destroyed; evolving endoscopic frontal-sinus techniques allow selected delayed rescue of outflow obstruction without prophylactically sacrificing the sinus."
        ),
        "manage": (
            "Use a hierarchy. OBSERVE when injury is minimal, drainage is intact, and there is no unresolved CSF/intracranial problem. REPAIR THE ANTERIOR TABLE when contour is the principal issue but sinus physiology is salvageable. PRESERVE/RESTORE DRAINAGE when FSOT injury can be treated safely with observation, endoscopic management, or selected reconstruction. OBLITERATE when the sinus is nonfunctional but the posterior table/intracranial interface does not require cranialization: remove all mucosa and permanently close the recess. CRANIALIZE for severe posterior-table/dural injury when the posterior sinus wall cannot safely remain or a craniotomy is otherwise required."
        ),
        "operate": (
            "Technical endpoint follows the chosen branch. For contour repair, restore the anterior table without unnecessarily sacrificing sinus function. For obliteration, remove mucosa meticulously—including recesses and fracture lines—and securely occlude the FSOT before filling/allowing obliteration according to the chosen technique. For cranialization, remove the posterior table, strip all sinus mucosa, close the outflow tract, repair dura/skull base as needed, use vascularized tissue such as pericranium when appropriate, and reconstruct the anterior table. Inadequate mucosal removal or recess closure creates the setup for delayed mucocele/infection."
        ),
        "teach": (
            "Boards algorithm: CONTOUR? → DURA/BACK TABLE? → DRAINAGE? → SAFE SINUS? An isolated contour problem is not an indication for cranialization. FSOT involvement is not synonymous with automatic obliteration if drainage can remain or be restored and surveillance is reliable. Conversely, severe posterior-table disruption with significant dural/skull-base injury may require cranialization even if the anterior table looks modest. Historical algorithms were more aggressive; contemporary evidence supports selective observation/endoscopic preservation, so reason from anatomy and physiology rather than one obsolete threshold."
        ),
        "tags": ["frontal sinus fracture algorithm", "safe sinus", "observation", "anterior table ORIF", "frontal sinus preservation", "frontal sinus obliteration", "cranialization", "FSOT obstruction", "posterior table fracture"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — frontal sinus fracture treatment algorithms and skull-base reconstruction",
            "K.J. Lee's Essential Otolaryngology, 12e — facial trauma decision-making and frontal sinus surgery",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — concise frontal sinus trauma algorithm and operative pearls",
            "AO CMF Surgery Reference — obliteration and cranialization techniques and posterior-table severity principles",
            "Current Concepts in Frontal Sinus Fracture Management (2026) — conservative anatomy-driven treatment and expanding sinus-preservation/endoscopic options",
            "Wolbert et al., J Craniofac Surg 2026 — systematic review/meta-analysis of cranialization versus noncranialization strategies for displaced posterior-table fractures",
        ],
    },
}


def apply_facial_frontal_sinus_rebuild_v301(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = FRONTAL_SINUS_V301.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v301"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
