"""v32.8 — source-grounded frontal-sinus-fracture vs decision-model rebuild.

Keeps the two frontal-sinus trauma cards clinically distinct:
1) Frontal Sinus Fracture = injury recognition, CT mapping, complication domains, and treatment principles.
2) Frontal Sinus Fracture Decision Model = an explicit anatomy-driven branching algorithm for sinus preservation, obliteration, or cranialization.
"""

import re

DOMAIN = "Facial Plastics / Trauma"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


FRONTAL_SINUS_REBUILD_V328 = {
    "frontal sinus fracture": {
        "recognize": (
            "This card owns the CLINICAL FRONTAL-SINUS TRAUMA PROBLEM, not the separate branching algorithm. After trauma stabilization, look for forehead/brow contour injury, laceration over the frontal sinus, supraorbital sensory change, orbital findings, rhinorrhea suspicious for CSF, pneumocephalus, and associated NOE/anterior-skull-base injury. A frontal-sinus fracture is not one binary injury: management depends on which of THREE DOMAINS are damaged — anterior table/contour, posterior table/dura, and the frontal sinus outflow pathway."
        ),
        "localize": (
            "Map thin-cut CT in all three domains. ANTERIOR TABLE: displacement, comminution and expected contour deformity. POSTERIOR TABLE: displacement/comminution, pneumocephalus, intracranial injury and clues to dural violation/CSF leak. OUTFLOW PATHWAY (FSOT/NFOT/frontal recess): inspect the sinus floor, medial frontal sinus/anterior table, frontal recess and adjacent ethmoid/NOE complex for obstruction or loss of a reconstructable drainage route. Also map orbit, cribriform/anterior skull base and any separate neurosurgical injury. Do not let a dramatic anterior-table defect distract from the posterior table or drainage pathway."
        ),
        "workup": (
            "Document ocular examination and neurologic status, examine wounds/forehead contour, and assess clear rhinorrhea when present; beta-2 transferrin can confirm suspected CSF when the diagnosis is uncertain. High-resolution CT is the key anatomic study. The goal is not merely to name a fracture but to decide whether the sinus can remain a SAFE, ventilated sinus with an intact intracranial barrier. Historical displacement thresholds can help describe severity, but they should not replace direct assessment of contour, posterior-table/dural injury, outflow patency, symptoms and the need for a concomitant craniotomy."
        ),
        "manage": (
            "Treat each injured domain on its own merits. Minimally displaced anterior-table injury without meaningful contour deformity or drainage injury can often be observed. Anterior-table deformity may require reduction/fixation or selected minimally invasive correction for contour. Posterior-table involvement ALONE is not an automatic cranialization indication: selected nondisplaced/minimally displaced injuries without persistent CSF leak or major dural/intracranial problems can be observed with surveillance. Outflow-pathway injury requires an explicit patency/reconstructability plan; contemporary management increasingly uses observation and endoscopic sinus-preserving strategies in selected patients rather than automatic obliteration."
        ),
        "operate": (
            "When surgery is required, solve the pathology rather than performing one operation for every frontal-sinus fracture. Restore forehead contour when the anterior table is the problem; repair dura/skull base and separate intracranial injury when present; restore or deliberately eliminate unsafe sinus drainage when the outflow pathway cannot remain functional. OBLITERATION removes sinus mucosa, closes the outflow tract and fills/excludes the sinus while retaining the posterior table. CRANIALIZATION removes the posterior table so the former sinus becomes part of the intracranial space after meticulous mucosal removal/outflow management and durable separation from the sinonasal tract."
        ),
        "teach": (
            "Chief/boards frame: FRONTAL SINUS FRACTURE asks, 'Which of the three domains is injured — contour, posterior table/dura, and outflow — and what complication does that create?' Do not memorize 'posterior table = cranialize' or 'outflow injury = obliterate.' Modern care is increasingly anatomy-driven and sinus-preserving when a safe ventilated sinus can be maintained. Long-term complications include chronic frontal sinusitis, mucocele/mucopyocele, osteomyelitis, meningitis/brain abscess, persistent CSF leak and contour deformity; mucoceles may present years after the trauma or repair, so delayed symptoms matter. The separate DECISION MODEL card owns the branch-by-branch operation choice."
        ),
        "tags": ["frontal sinus fracture", "anterior table", "posterior table", "frontal sinus outflow tract", "NFOT", "CSF leak", "mucocele", "cranialization", "obliteration", "frontal recess"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — frontal sinus and anterior skull-base trauma principles",
            "K.J. Lee's Essential Otolaryngology, 12e — frontal sinus fracture evaluation and facial-trauma management",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — frontal sinus anterior/posterior table, frontal recess/outflow, CSF and mucocele considerations",
            "Lever, Le & Chen. Frontal Sinus Fractures: A Changing Paradigm. Facial Plast Surg Clin North Am. 2025 — contemporary observation and sinus-preservation principles",
            "AO CMF Surgery Reference — frontal sinus posterior-table/cranialization technique and safe-sinus principles",
        ],
    },
    "frontal sinus fracture decision model": {
        "recognize": (
            "This is the ADVANCED BRANCHING-ALGORITHM card, not a second frontal-sinus-fracture overview. Start only after CT has mapped the anterior table, posterior table/dura and frontal sinus outflow pathway. The decision endpoint is a SAFE SINUS: either preserve a ventilated sinus with a durable intracranial barrier, or intentionally exclude/remove sinus function when that cannot be achieved safely. Every branch should answer which structure is driving intervention rather than using fracture displacement alone as a surrogate."
        ),
        "localize": (
            "BRANCH 1 — posterior table/dura/intracranial problem: persistent CSF leak, severe posterior comminution/displacement with nonviable barrier, significant dural injury, or a separate craniotomy indication moves the case toward combined skull-base repair and, when preservation is unsafe, cranialization. If those features are absent, posterior-table involvement can remain in a preservation pathway. BRANCH 2 — outflow: decide whether the frontal recess/FSOT is patent, likely to autoventilate, reconstructable/endoscopically maintainable, or truly unsalvageable. BRANCH 3 — anterior table: decide separately whether contour requires repair."
        ),
        "workup": (
            "Operational checklist before choosing the branch: 1) Is there an active/persistent CSF leak or dural defect? 2) Is a neurosurgical craniotomy needed anyway? 3) Can the posterior-table barrier remain safe? 4) Is frontal outflow patent or realistically restorable? 5) Is the anterior-table contour acceptable? 6) Can the patient complete endoscopic/radiographic follow-up? Serial imaging matters when observation is chosen because outflow obstruction and mucocele formation can declare themselves later. Avoid treating historical rules such as a fixed millimeter cutoff or 'one-table-width' displacement as absolute contemporary indications."
        ),
        "manage": (
            "Decision tree: STABLE posterior table/dura + patent or recoverable outflow -> preserve the sinus; observe or repair the anterior table only as contour dictates. NO major dural problem but outflow is injured/uncertain -> favor surveillance or drainage-restoring/endoscopic strategies when a durable patent pathway is achievable; intentionally eliminate sinus function only when safe drainage cannot be maintained. PERSISTENT CSF leak, destructive posterior-table injury, nonreconstructable intracranial barrier, or another required frontal craniotomy -> repair dura/skull base and consider cranialization when the sinus cannot safely remain. This replaces the obsolete reflex that every posterior-table fracture requires cranialization."
        ),
        "operate": (
            "Know the destructive options precisely. OBLITERATION: remove all reachable sinus mucosa, permanently close the frontal outflow pathway, and fill/exclude the sinus cavity while the posterior table remains. CRANIALIZATION: remove the posterior table, remove sinus mucosa, manage/close the outflow tract and reconstruct a durable barrier so the frontal lobes can occupy the former sinus space. Thus cranialization is primarily a posterior-table/dural-intracranial solution; obliteration is primarily an intentional sinus-exclusion solution. Anterior-table ORIF by itself does not treat an unsafe posterior table, CSF leak or obstructed outflow."
        ),
        "teach": (
            "Boards algorithm: 1) MAP three domains; 2) if severe posterior-table/dural disease or persistent CSF leak makes sinus preservation unsafe, repair the skull base and consider CRANIALIZATION; 3) otherwise interrogate OUTFLOW — preserve/restore it whenever safely feasible; 4) if a functional sinus truly cannot be maintained, select deliberate sinus exclusion/OBLITERATION as appropriate; 5) address ANTERIOR TABLE contour independently; 6) arrange long-term surveillance for delayed mucocele/sinusitis. The high-yield distinction is not 'how displaced is the fracture?' but 'can I leave a safe, ventilated sinus with a durable barrier from the intracranial space?'"
        ),
        "tags": ["frontal sinus decision model", "safe sinus", "sinus preservation", "FSOT", "frontal recess", "cranialization", "obliteration", "posterior table", "CSF leak", "mucocele surveillance"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — frontal sinus/skull-base trauma decision principles",
            "K.J. Lee's Essential Otolaryngology, 12e — facial-trauma and frontal-sinus management framework",
            "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6e — anterior/posterior table, nasofrontal outflow, CSF and delayed mucocele principles",
            "Lever, Le & Chen. Frontal Sinus Fractures: A Changing Paradigm. Facial Plast Surg Clin North Am. 2025 — contemporary conservative and sinus-preserving management",
            "Dedhia et al. Contemporary management of frontal sinus fractures. Curr Opin Otolaryngol Head Neck Surg. 2019 — anatomy-driven algorithm and expanding endoscopic preservation",
            "AO CMF Surgery Reference — frontal-sinus cranialization and posterior-table operative principles",
        ],
    },
}


def apply_frontal_sinus_decision_rebuild_v328(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = FRONTAL_SINUS_REBUILD_V328.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v328"] = True
        module["semantic_role_v328"] = (
            "frontal-sinus trauma recognition, three-domain injury mapping, and complication principles"
            if key == "frontal sinus fracture"
            else "anatomy-driven branch logic for sinus preservation, obliteration, or cranialization"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
