"""v43.9: fix stale topic-name keys/values in the Prerequisite and Clinical
Relationship cross-link data (2026-09-23 audit finding #3).

data.PREREQUISITES_SUGGESTED_V114 is looked up in app.py's concept() route via
PREREQUISITES_SUGGESTED_V114.get(mod["topic"], []), and data.CURRICULUM_RELATIONSHIPS_V167
is looked up the same way in reliability_v168.py's concept_context_v168 (both by KEY,
and the relationship dict's "parents" values are matched again to find "clinical_children"
for the PARENT topic's own page). Both dicts were authored against old
OR-procedure-style names or mismatched casing that no longer exists in
DEEP_MODULES_V6, so roughly half of their entries never render on any Concept Hub page:

- 16 of 32 PREREQUISITES_SUGGESTED_V114 keys, plus most of their prerequisite values,
  don't exactly match a live topic title (e.g. 'Mastoidectomy', 'Stapes surgery',
  'Thyroid lobectomy', 'Cochlear implantation', 'HNS candidacy', 'Functional rhinoplasty'
  are OR-procedure names, not curriculum topics; 'Audiogram interpretation' is just
  miscased).
- 3 of 16 CURRICULUM_RELATIONSHIPS_V167 keys ('Type I Thyroplasty', 'Laryngeal
  Reinnervation', 'Endoscopic CSF Leak Repair') and 2 parent values don't match either.

This module rewrites both dicts in place: exact-cased/renamed keys where a clear
1:1 real-topic target exists, values remapped to the closest matching real topic,
and any value with no honest match (e.g. a self-referential duplicate, or a
fragment like 'FNA'/'SGS' with no dedicated topic) dropped rather than forced into
a misleading link. No entry that was already correct is touched.
"""

# key -> (new_key_or_None_if_unchanged, [new prerequisite values])
PREREQUISITE_FIXES_V439 = {
    "Audiogram interpretation": ("Audiogram Interpretation", ["Auditory Neuroanatomy / Cochlear Physiology"]),
    "Tympanoplasty": ("Tympanic Membrane Perforation", ["Audiogram Interpretation"]),
    "Mastoidectomy": ("Chronic Otitis Media / Cholesteatoma", ["Temporal Bone Anatomy"]),
    "Stapes surgery": ("Otosclerosis / Stapes Fixation", ["Audiogram Interpretation"]),
    "Cochlear implantation": ("Cochlear Implant Surgery", ["Cochlear Implant Candidacy", "Pediatric Hearing Loss Workup", "Audiogram Interpretation"]),
    "Ethmoidectomy": (None, ["Nasal Anatomy for Endoscopy", "CRSsNP", "CRSwNP"]),
    "Frontal sinus surgery": ("Frontal Sinusotomy / Draf Procedures", ["Ethmoidectomy", "Frontal Recess / Frontal Sinus"]),
    "Revision FESS": (None, ["Ethmoidectomy", "Nasal Anatomy for Endoscopy"]),
    "Neck dissection": ("Neck Dissection", ["Neck Management by Primary Site", "Unknown Primary with Cervical Metastasis"]),
    "Thyroid lobectomy": ("Differentiated Thyroid Cancer", ["Thyroid Nodule"]),
    "Total thyroidectomy": ("Completion Thyroidectomy", ["Thyroid Nodule", "Differentiated Thyroid Cancer"]),
    "Airway reconstruction": ("Subglottic / Tracheal Stenosis", ["Tracheostomy Emergency", "Laryngeal Anatomy"]),
    "Supraglottoplasty": (None, ["Laryngomalacia"]),
    "Medialization": ("Medialization Thyroplasty", ["Unilateral Vocal Fold Paralysis", "Laryngeal Anatomy"]),
    "HNS candidacy": ("Hypoglossal Nerve Stimulation", ["Adult PSG Interpretation", "DISE"]),
    "Functional rhinoplasty": ("Functional Septorhinoplasty", ["Septal Deviation", "Alar Retraction / Nasal Vestibular Stenosis"]),
}

# old_key -> new_key (relationship content itself is unchanged unless noted)
RELATIONSHIP_KEY_RENAMES_V439 = {
    "Type I Thyroplasty": "Medialization Thyroplasty",
    "Laryngeal Reinnervation": "Arytenoid Adduction / Reinnervation",
    "Endoscopic CSF Leak Repair": "Endoscopic CSF Leak Repair / Nasoseptal Flap",
}

# key (post-rename) -> corrected parents list
RELATIONSHIP_PARENT_FIXES_V439 = {
    "Endoscopic CSF Leak Repair / Nasoseptal Flap": ["CSF Rhinorrhea"],
    "Arytenoid Adduction / Reinnervation": ["Unilateral Vocal Fold Paralysis", "Bilateral Vocal Fold Immobility"],
    "Free-Flap Monitoring / Compromise / Salvage": ["Reconstruction Selection After Head & Neck Ablation"],
}


def apply_prerequisite_relationship_repair_v439(data_module, app_module=None):
    result = {"prereq_keys_fixed": 0, "relationship_keys_renamed": 0, "relationship_parents_fixed": 0}

    preq = getattr(data_module, "PREREQUISITES_SUGGESTED_V114", None)
    if isinstance(preq, dict):
        for old_key, (new_key, new_values) in PREREQUISITE_FIXES_V439.items():
            if old_key not in preq:
                continue
            preq.pop(old_key)
            final_key = new_key if new_key else old_key
            if preq.get(final_key) != new_values:
                preq[final_key] = new_values
                result["prereq_keys_fixed"] += 1
        # clinical_hierarchy_v167.apply_clinical_hierarchy_v167() runs earlier in the
        # boot chain and merges CURRICULUM_RELATIONSHIPS_V167's (pre-fix) keys/parents
        # into PREREQUISITES_SUGGESTED_V114 too, so the same 3 stale relationship
        # names and 1 stale parent value leak into this dict as well -- clean those
        # up here using the same rename map.
        for old_key, new_key in RELATIONSHIP_KEY_RENAMES_V439.items():
            if old_key in preq:
                values = preq.pop(old_key)
                if new_key in preq:
                    merged = list(preq[new_key])
                    for v in values:
                        if v not in merged:
                            merged.append(v)
                    preq[new_key] = merged
                else:
                    preq[new_key] = values
                result["prereq_keys_fixed"] += 1
        stale_value_renames = {
            "Reconstruction Selection After H&N Ablation": "Reconstruction Selection After Head & Neck Ablation",
            "CSF Rhinorrhea / Skull-Base Defects": "CSF Rhinorrhea",
        }
        for key, values in preq.items():
            preq[key] = [stale_value_renames.get(v, v) for v in values]

        data_module.PREREQUISITES_SUGGESTED_V114 = preq
        if app_module is not None:
            app_module.PREREQUISITES_SUGGESTED_V114 = preq

    rel = getattr(data_module, "CURRICULUM_RELATIONSHIPS_V167", None)
    if isinstance(rel, dict):
        for old_key, new_key in RELATIONSHIP_KEY_RENAMES_V439.items():
            if old_key in rel and new_key not in rel:
                rel[new_key] = rel.pop(old_key)
                result["relationship_keys_renamed"] += 1
        for key, parents in RELATIONSHIP_PARENT_FIXES_V439.items():
            if key in rel and rel[key].get("parents") != parents:
                rel[key]["parents"] = parents
                result["relationship_parents_fixed"] += 1
        data_module.CURRICULUM_RELATIONSHIPS_V167 = rel
        if app_module is not None:
            app_module.CURRICULUM_RELATIONSHIPS_V167 = rel

    return result
