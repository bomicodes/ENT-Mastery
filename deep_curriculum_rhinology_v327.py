"""v32.7 — source-grounded adult acute bacterial rhinosinusitis rebuild.

Replaces repetitive ABRS stage text with six different cognitive jobs: recognition,
mechanism/localization, diagnostic restraint, initial treatment, failure/complication
escalation, and a compact boards/chief mental model. Management is calibrated to the
2025 AAO-HNSF Adult Sinusitis update rather than older severity-based antibiotic dogma.
"""

import re

DOMAIN = "Rhinology / Allergy / Skull Base"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


ABRS_V327 = {
    "recognize": (
        "Recognize presumed ADULT ACUTE BACTERIAL RHINOSINUSITIS from the TIME COURSE, not from green mucus alone. The core AAO-HNSF patterns are acute-rhinosinusitis symptoms that persist WITHOUT improvement for at least 10 days, or symptoms that worsen again within 10 days after an initial improvement ('double worsening'). Purulent drainage should occur with nasal obstruction and/or facial pain-pressure-fullness. Most early viral URIs improve without antibiotics; isolated facial pain, headache, tooth pain, or discolored drainage without the appropriate syndrome and trajectory should make you reconsider the diagnosis."
    ),
    "localize": (
        "Localize ABRS as an acute inflammatory/infectious process arising after impaired sinus ventilation and mucociliary clearance, commonly following viral mucosal edema and ostial obstruction. The practical localization question is whether disease is still confined to the sinonasal compartment or has crossed a boundary: orbital symptoms suggest spread through the thin lamina papyracea/ethmoid region; frontal disease can threaten bone and intracranial spaces; severe unilateral maxillary disease should raise an odontogenic source or obstructing lesion rather than being treated as generic bilateral URI-associated ABRS."
    ),
    "workup": (
        "Diagnose uncomplicated ABRS CLINICALLY. Do not obtain routine plain films or CT simply to prove sinusitis when the history meets criteria. Image when a complication or alternative diagnosis is suspected, when disease is atypical/unilateral, or when the clinical course is not behaving like uncomplicated ABRS. Nasal endoscopy can identify middle-meatal purulence or another lesion but is not required for routine diagnosis. Culture is not a first-visit test; use an endoscopically directed middle-meatal culture or operative specimen when treatment fails, disease is complicated, the host is immunocompromised, or resistant/unusual microbiology is a meaningful concern. Reassess the diagnosis rather than ordering a scan reflexively for every nonresponder."
    ),
    "manage": (
        "For uncomplicated adult ABRS, use SHARED DECISION-MAKING: either watchful waiting or initial antibiotic therapy is appropriate when reliable follow-up exists. Watchful waiting is no longer restricted only to 'mild' disease in the 2025 AAO-HNSF update. Provide analgesia and consider saline irrigation and/or topical intranasal corticosteroid for symptom relief. If antibiotics are chosen, amoxicillin with or without clavulanate is first-line for most adults, generally for 5–7 days in the updated guideline. Select an alternative based on true beta-lactam allergy, local resistance, recent antibiotic exposure and patient-specific risk rather than automatically escalating everyone to a fluoroquinolone."
    ),
    "operate": (
        "ABRS itself is not an operative diagnosis. The advanced decision is FAILURE OR COMPLICATION. Reassess any patient who worsens at any time or fails to improve after the initial management interval: confirm that the syndrome is actually ABRS, look for dental disease, migraine/neuralgia, resistant organisms, an obstructing lesion, immunocompromise, or progression beyond the sinuses, and change therapy when appropriate. Orbital signs, vision change, ophthalmoplegia, proptosis, severe frontal swelling, meningismus, focal neurologic deficit, altered mental status, or toxic deterioration demand urgent cross-sectional imaging, IV therapy and ENT/ophthalmology/neurosurgical escalation as indicated. Drainage is directed at a defined abscess, threatened vision, intracranial complication, source-control problem, or other complication—not at routine uncomplicated ABRS."
    ),
    "teach": (
        "Chief/boards model: ABRS is a TRAJECTORY diagnosis. VIRAL = early and improving; ABRS = >=10 days without improvement or DOUBLE WORSENING. Uncomplicated adult disease does not require imaging, culture, or automatic antibiotics. The 2025 update deliberately expands watchful waiting to all uncomplicated ABRS when follow-up is assured and uses amoxicillin with or without clavulanate first-line when antibiotics are chosen. The dangerous pivot is not 'more sinus pressure'; it is loss of compartment containment—orbital, bony, intracranial, or systemic findings—which changes the problem from outpatient symptom management to urgent complication control."
    ),
    "tags": ["acute bacterial rhinosinusitis", "ABRS", "double worsening", "watchful waiting", "amoxicillin clavulanate", "sinusitis complications", "orbital complication"],
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — acute rhinosinusitis pathophysiology, differential diagnosis, complications, and surgical escalation framework",
        "K.J. Lee's Essential Otolaryngology, 12e — ARS/ABRS diagnostic patterns, uncomplicated evaluation, symptomatic treatment, and antimicrobial framework",
        "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — cardinal symptoms, imaging/culture indications, recurrent disease, and complicated-rhinosinusitis differential",
        "AAO-HNSF Clinical Practice Guideline: Adult Sinusitis Update, 2025 — ABRS diagnostic trajectory, no routine imaging, expanded watchful waiting, first-line amoxicillin with or without clavulanate, treatment duration, and reassessment",
    ],
}


def apply_rhinology_abrs_rebuild_v327(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        topic = _norm(module.get("topic"))
        if topic not in {"acute bacterial rhinosinusitis", "acute bacterial sinusitis"}:
            continue
        for field in FIELDS:
            module[field] = ABRS_V327[field]
        module["tags"] = list(ABRS_V327["tags"])
        module["source_basis"] = list(ABRS_V327["source_basis"])
        module["source_grounded_v327"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
