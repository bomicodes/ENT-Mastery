"""v28.4 — Source-grounded Olfactory Dysfunction Concept Hub rebuild.

Repairs the legacy card that duplicated Recognize/Localize, mixed mechanisms with
etiologies, and inherited generic procedural boilerplate.  The six stages now teach
clinically distinct tasks: define the phenotype -> reason about mechanism/anatomic
level -> evaluate the cause -> manage by cause -> make selective imaging/referral/
procedural decisions -> synthesize board-level discriminators.

Source basis: Cummings 7e olfaction chapter, K.J. Lee 12e nasal function/taste-smell
chapter, and Pasha 6e olfactory dysfunction section.  Management language is kept
conservative where older textbook therapies have limited/uncertain evidence.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _is_target(topic):
    n = _norm(topic)
    return "olfactory" in n and ("dysfunction" in n or "loss" in n)


OLFACTORY_REBUILD_V284 = {
    "recognize": (
        "First define what the patient actually means by 'I can't smell' or 'I can't taste.' Quantitative olfactory dysfunction includes hyposmia and anosmia; qualitative dysfunction includes parosmia (a real odor is perceived in a distorted way) and phantosmia (an odor is perceived without an external odorant). Many patients who report loss of taste actually have impaired retronasal olfaction and therefore loss of flavor rather than primary gustatory failure. Establish onset, severity, laterality, fluctuation and whether quantitative and qualitative symptoms coexist."
    ),
    "localize": (
        "Use anatomy as a reasoning framework without confusing mechanism with etiology. Conductive dysfunction means odorants cannot adequately reach the olfactory neuroepithelium/olfactory cleft, as with marked mucosal edema, polyps or other obstruction. Sensorineural/peripheral dysfunction reflects injury to the olfactory receptor neuroepithelium or its axons, while central dysfunction involves the olfactory bulb, tract or higher processing pathways. A single disease can involve more than one level: chronic rhinosinusitis may have conductive plus inflammatory neuroepithelial effects, and head trauma may cause nasal obstruction, shearing of olfactory fila and/or central injury. Therefore also classify by likely cause rather than labeling postviral, traumatic or neurodegenerative disease as if each were an anatomic compartment."
    ),
    "workup": (
        "Let the history drive the differential. Ask about preceding upper-respiratory infection, chronic rhinosinusitis/polyps or allergy, head trauma, sinonasal or neurosurgery, medications, smoking/toxin or occupational exposure, congenital lifelong loss, aging and associated neurologic symptoms or family history. Ask specifically about unilateral symptoms, epistaxis, obstruction, headache and other cranial-nerve findings because these may change the workup. Perform a complete head-and-neck examination with nasal endoscopy to inspect the olfactory cleft and exclude inflammatory, obstructive or mass lesions. Confirm and quantify dysfunction with validated psychophysical smell testing when it will establish baseline severity, document recovery or clarify unreliable subjective reporting; commonly used paradigms assess odor identification and/or threshold/discrimination. Idiopathic olfactory dysfunction is a diagnosis of exclusion, not a shortcut after a normal anterior rhinoscopy."
    ),
    "manage": (
        "Treat the identified cause rather than treating all smell loss as one disease. Manage chronic rhinosinusitis, polyposis or other reversible sinonasal inflammation/obstruction with appropriate disease-directed medical therapy and selected surgery when independently indicated; improvement in olfaction after sinus treatment is possible but not guaranteed. Olfactory training is the principal rehabilitative strategy for persistent postinfectious and other appropriate nonconductive losses. Review potentially contributory drugs/exposures and address them when feasible. Counsel every patient with substantial loss about practical safety: functioning smoke/fire and natural-gas/CO detection as applicable, food-expiration/spoilage precautions, and added caution with cooking. Discuss prognosis by etiology and duration rather than promising recovery."
    ),
    "operate": (
        "Olfactory dysfunction itself is usually not an operative diagnosis. Imaging and procedures should answer a specific clinical question. Use CT when the history/endoscopy suggests sinonasal inflammatory, obstructive, traumatic or structural disease for which bony/sinus anatomy matters. Use MRI when a neural/central process, olfactory-bulb/tract abnormality, intracranial tumor or other concerning neurologic/atypical presentation is suspected; routine imaging of every otherwise typical bilateral postinfectious loss is not the goal. Persistent unilateral dysfunction, unilateral obstruction/bleeding, a focal endoscopic finding or associated neurologic/cranial-nerve deficits deserve directed evaluation rather than empiric reassurance. Operate only when there is a separate treatable structural/inflammatory indication; destructive olfactory-mucosa procedures described for refractory phantosmia are exceptional, high-risk interventions and are not routine management."
    ),
    "teach": (
        "Boards/rounds framework: first separate QUANTITATIVE loss (hyposmia/anosmia) from QUALITATIVE distortion (parosmia/phantosmia), then decide whether the history favors postinfectious disease, sinonasal inflammation/obstruction, trauma, congenital loss, medication/toxin exposure, aging/neurodegeneration or another central cause. Remember that 'taste loss' commonly reflects impaired retronasal smell. Endoscopy evaluates access to the olfactory cleft and occult sinonasal disease; validated smell testing makes subjective loss measurable. Do not force etiologies into a false conductive-versus-sensorineural binary, because CRS and trauma can produce mixed mechanisms. The high-value red flags are unilateral or progressive symptoms, epistaxis/mass/obstruction and focal neurologic or additional cranial-nerve findings."
    ),
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — Olfaction and olfactory dysfunction",
        "K.J. Lee's Essential Otolaryngology, 12e — Nasal function and evaluation of taste/smell",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Olfactory Dysfunction",
    ],
    "source_grounded_v284": True,
}


def apply_olfactory_rebuild_v284(data_module, app_module=None):
    patched = []
    for domain_name, modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).items():
        for module in modules or []:
            if not _is_target(module.get("topic")):
                continue
            for field in FIELDS:
                module[field] = OLFACTORY_REBUILD_V284[field]
            module["source_basis"] = list(OLFACTORY_REBUILD_V284["source_basis"])
            module["source_grounded_v284"] = True
            patched.append({"domain": domain_name, "topic": module.get("topic")})

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6

    return {"patched": patched, "count": len(patched)}
