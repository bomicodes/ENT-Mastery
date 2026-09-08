"""v35.5 — deepen the exact-live CRSsNP card for odontogenic and unilateral disease.

This is intentionally a bounded extension of the existing CRSsNP topic, not a new topic.
Durable CRS anatomy/differential/ESS principles are inherited from v35.0/v35.4 and grounded
in Cummings 7e, K.J. Lee 12e, and Pasha 6e. This pass adds a focused odontogenic/unilateral
senior-decision boundary from multidisciplinary consensus literature while preserving the
strict 325-topic / 42-topic Rhinology inventories.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "CRSsNP"

EXTRA_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — unilateral maxillary sinus disease differential, dental-source considerations, endoscopic/CT evaluation and ESS principles",
    "K.J. Lee's Essential Otolaryngology, 12e — unilateral sinonasal disease differential and odontogenic maxillary sinusitis framework",
    "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — odontogenic/focal sinus disease evaluation and surgical principles",
    "Craig JR et al. Diagnosing odontogenic sinusitis: an international multidisciplinary consensus statement. Int Forum Allergy Rhinol. 2021 — ENT confirmation of sinusitis plus dental confirmation of odontogenic pathology; multidisciplinary diagnosis",
    "Craig JR et al. Management of odontogenic sinusitis: multidisciplinary consensus statement. Int Forum Allergy Rhinol. 2020 — shared ENT/dental/patient decision-making; no universal dental-first versus ESS-first sequence",
    "Lin J et al. Expert consensus on odontogenic maxillary sinusitis multi-disciplinary treatment. Int J Oral Sci. 2024 — multidisciplinary diagnosis, dental source control and individualized combined treatment pathways",
]

WORKUP_ADD = (
    " ODONTOGENIC/UNILATERAL ESCALATION: unilateral maxillary-predominant opacification or unilateral middle-meatal purulence should trigger a focal-source workup rather than automatic labeling as routine inflammatory CRS. "
    "Ask specifically about recent or remote dental infection, endodontic treatment, extraction, implant or sinus-lift procedures, oroantral communication/fistula, dental pain and foul smell/taste, recognizing that dental pain may be absent. "
    "On CT, inspect the maxillary dentition and sinus floor for periapical disease, periodontal bone loss, foreign material, oroantral communication and a pattern centered on the ipsilateral maxillary sinus; do not assume that an incidental dental abnormality proves causality. "
    "Confirm the SINUS component with ENT assessment/endoscopy and obtain DENTAL evaluation with appropriate dental examination/imaging to confirm the odontogenic pathology when suspected. "
    "If the unilateral pattern is atypical, destructive, mass-like, bloody, necrotic or associated with cranial neuropathy/orbital findings, reopen neoplasm, invasive fungal disease and complicated sinusitis rather than forcing an odontogenic diagnosis."
)

MANAGE_ADD = (
    " For confirmed odontogenic sinusitis, treat the dental source and the sinonasal disease as linked problems. Repeated antibiotics alone are not definitive when infected dental pathology, a foreign body or an oroantral fistula persists. "
    "Coordinate ENT and dental/oral-surgery management and use shared decision-making about sequencing. Some patients improve after dental source control alone; others with substantial sinus burden, obstructed drainage, persistent disease, complications, implant/foreign-body issues or a need for rapid symptom control benefit from ESS plus dental treatment. "
    "Do not teach a rigid dental-first or ESS-first rule: sequence and extent should reflect dental pathology, sinus burden, symptoms, anatomy, complications and patient preference."
)

OPERATE_ADD = (
    " In odontogenic disease requiring ESS, open the involved sinus sufficiently for drainage, source clearance when appropriate, postoperative surveillance and topical access while preserving orbital/skull-base safety. "
    "Coordinate removal or management of displaced dental material and closure of a persistent oroantral communication/fistula with the dental/oral-surgery team when indicated. The operation treats the sinonasal consequence; unresolved dental pathology can drive persistence or recurrence."
)

TEACH_ADD = (
    " Senior unilateral rule: one-sided maxillary disease is a diagnostic prompt, not a phenotype shortcut. ENT confirms sinusitis; dental evaluation confirms a causal odontogenic lesion. "
    "Antibiotics without source control often fail, but there is no universal dental-first versus ESS-first sequence. The bailout is to stop and reconsider tumor, invasive fungal disease or orbital/intracranial complication when the unilateral process is destructive, necrotic, bloody, neurologically progressive or otherwise atypical."
)


def apply_rhinology_odontogenic_unilateral_depth_v355(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    matches = [r for r in rows if str(r.get("topic") or "") == TOPIC]
    if len(matches) != 1:
        raise RuntimeError(f"v35.5 expected exactly one exact-live {TOPIC!r} row; found {len(matches)}")
    row = matches[0]
    if row.get("source_grounded_v355"):
        return {"patched": [], "already_applied": [TOPIC]}
    if not row.get("source_grounded_v354"):
        raise RuntimeError("v35.5 requires v35.4 predecessor on exact-live CRSsNP")
    row["workup"] = str(row.get("workup") or "") + WORKUP_ADD
    row["manage"] = str(row.get("manage") or "") + MANAGE_ADD
    row["operate"] = str(row.get("operate") or "") + OPERATE_ADD
    row["teach"] = str(row.get("teach") or "") + TEACH_ADD
    existing_sources = list(row.get("source_basis") or [])
    for source in EXTRA_SOURCES:
        if source not in existing_sources:
            existing_sources.append(source)
    row["source_basis"] = existing_sources
    row["source_grounded_v355"] = True
    row["deliberate_review_v355"] = {
        "foundation": "unilateral maxillary disease should trigger odontogenic/focal-source and atypical-disease differential",
        "application": "ENT confirmation of sinusitis plus dental confirmation of causal pathology; antibiotics are not definitive source control",
        "senior_decision": "multidisciplinary individualized sequencing of dental treatment and ESS with explicit neoplasm/fungal/complication bailout",
    }
    return {"patched": [TOPIC], "canonical_id": data_module._v6_item_id(DOMAIN, TOPIC)}
