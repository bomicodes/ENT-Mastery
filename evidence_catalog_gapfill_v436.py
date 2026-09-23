"""v43.6: close the Allergy, Facial Plastics/Trauma, and Salivary gaps in the
Evidence & Sources catalog.

Requested 2026-09-22 (site audit): CURRENT_EVIDENCE_CATALOG_V98 had only 17
entries total and zero dedicated citations for allergy, facial trauma, or
salivary-gland disease despite deep curriculum content existing for all
three. Every citation below was verified against a live source (title,
publishing body, and year) before being added -- see verification notes.

Allergy (3 entries) -- the standing AAAAI/ACAAI/JCAAI Joint Task Force
practice-parameter series, which is what this curriculum's allergy content
(Allergic Rhinitis, Allergen Immunotherapy, Anaphylaxis) is actually built
against:
- "Rhinitis 2020: A Practice Parameter Update" (J Allergy Clin Immunol, 2020)
- "Anaphylaxis: A 2023 Practice Parameter Update" (Ann Allergy Asthma
  Immunol, 2023 -- supersedes the 2020 update)
- "Allergen Immunotherapy: A Practice Parameter Third Update" (J Allergy Clin
  Immunol, 2011 -- still the standing formal practice parameter for SCIT/SLIT)

Facial Plastics / Trauma (2 entries):
- "Acute Management of Nasal Bone Fractures: A Systematic Review and Practice
  Management Guideline" (The American Surgeon, 2026)
- "AAO-HNSF Clinical Practice Guideline: Bell's Palsy" (Otolaryngol Head Neck
  Surg, 2013) -- directly relevant to Facial Paralysis / Facial Nerve
  Reanimation content in this domain.

Salivary (2 entries):
- NCCN Clinical Practice Guidelines in Oncology: Head and Neck Cancers
  (covers salivary gland tumor workup/management; periodically updated,
  Version 2.2025 confirmed live at verification time)
- "2016 ACR/EULAR Classification Criteria for Primary Sjogren's Syndrome"
  (Arthritis Rheumatol / Ann Rheum Dis, 2016)
"""

NEW_EVIDENCE_ENTRIES = [
    {"area": "Allergy", "title": "Rhinitis 2020: A Practice Parameter Update", "year": "2020",
     "kind": "Practice Parameter", "status": "AAAAI/ACAAI/JCAAI Joint Task Force -- active management source"},
    {"area": "Allergy", "title": "Anaphylaxis: A 2023 Practice Parameter Update", "year": "2023",
     "kind": "Practice Parameter", "status": "AAAAI/ACAAI/JCAAI Joint Task Force -- supersedes the 2020 update"},
    {"area": "Allergy", "title": "Allergen Immunotherapy: A Practice Parameter Third Update", "year": "2011",
     "kind": "Practice Parameter", "status": "standing SCIT/SLIT practice parameter; newer literature builds on this"},
    {"area": "Facial Plastics / Trauma",
     "title": "Acute Management of Nasal Bone Fractures: A Systematic Review and Practice Management Guideline",
     "year": "2026", "kind": "Practice Management Guideline", "status": "active management source"},
    {"area": "Facial Plastics / Trauma", "title": "AAO-HNSF Clinical Practice Guideline: Bell's Palsy",
     "year": "2013", "kind": "CPG", "status": "active management source; facial paralysis / reanimation framework"},
    {"area": "Salivary", "title": "NCCN Clinical Practice Guidelines in Oncology: Head and Neck Cancers",
     "year": "living guideline (v2.2025 confirmed)", "kind": "Guideline",
     "status": "salivary gland tumor workup/management framework"},
    {"area": "Salivary", "title": "2016 ACR/EULAR Classification Criteria for Primary Sjogren's Syndrome",
     "year": "2016", "kind": "Classification Criteria", "status": "diagnostic framework"},
]


def apply_evidence_catalog_gapfill_v436(data_module, app_module=None):
    catalog = data_module.CURRENT_EVIDENCE_CATALOG_V98
    existing_titles = {row.get("title") for row in catalog}
    added = []
    for entry in NEW_EVIDENCE_ENTRIES:
        if entry["title"] not in existing_titles:
            catalog.append(dict(entry))
            existing_titles.add(entry["title"])
            added.append(entry["title"])
    if app_module is not None:
        app_module.CURRENT_EVIDENCE_CATALOG_V98 = catalog
    return {"added": added}
