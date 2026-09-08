"""v35.4 — deepen the existing exact-live CRSsNP card for secondary host-factor disease.

This is intentionally a one-card extension, not a new topic. Durable ENT framing is inherited
from v35.0 (Cummings 7e, K.J. Lee 12e, Pasha 6e). This pass adds the resident-to-senior
immune/CF/PCD workup boundary using current authoritative guidance while preserving the
strict 325-topic / 42-topic Rhinology inventories.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "CRSsNP"

EXTRA_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — secondary CRS/host-factor differential and sinonasal inflammatory disease framework",
    "K.J. Lee's Essential Otolaryngology, 12e — refractory CRS differential including systemic and mucociliary disorders",
    "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — CRS workup and modifying host factors",
    "AAO-HNSF Clinical Practice Guideline: Adult Sinusitis Update, 2025 — assess CRS/recurrent ARS for cystic fibrosis, immunocompromised state and ciliary dyskinesia; allergy/immune-function testing may be obtained when clinically indicated",
    "AAAAI/ACAAI Practice Parameter for Primary Immunodeficiency, 2015 — quantitative immunoglobulins plus antigen-specific antibody responses/vaccine-response assessment for suspected humoral immune deficiency",
    "Cystic Fibrosis Foundation ENT Clinical Care Guideline — multidisciplinary CF sinonasal care, topical therapy and selected ESS; surgery does not correct CFTR dysfunction",
    "Cystic Fibrosis Foundation CF Diagnosis Clinical Care Guidelines — sweat chloride/CFTR-centered diagnostic evaluation when CF or CFTR-related disease is suspected",
    "ERS/ATS Guideline for Diagnosis of Primary Ciliary Dyskinesia, 2025 — phenotype-driven referral-center testing using nasal nitric oxide and complementary genetics/TEM/high-speed video microscopy/immunofluorescence rather than a single rule-out test",
]

WORKUP_ADD = (
    " SECONDARY/HOST-FACTOR ESCALATION: recurrent, unusually severe, culture-unusual, childhood-onset, "
    "bronchiectatic or medically refractory disease should trigger a cause-directed history before another empiric antibiotic cycle. "
    "For a humoral immune-deficiency phenotype, start with CBC/differential and quantitative IgG, IgA and IgM, then assess "
    "antigen-specific antibody function (including appropriately interpreted vaccine responses, commonly pneumococcal serotypes) when suspicion persists; "
    "do not diagnose or exclude clinically important antibody deficiency from an isolated IgG-subclass value. Escalate to Allergy/Immunology for abnormal results, "
    "recurrent severe/unusual infections, or suspected combined immune disease. A lifelong oto-sino-pulmonary phenotype, bronchiectasis, neonatal respiratory disease, "
    "laterality defect or infertility should reopen PRIMARY CILIARY DYSKINESIA: refer to an experienced center because nasal nitric oxide, genetics, TEM, high-speed video microscopy "
    "and immunofluorescence are complementary and no single negative adjunct test rules out PCD. Chronic sinopulmonary disease, bronchiectasis, pancreatic disease, male infertility, "
    "suggestive family history or an otherwise unexplained CFTR phenotype should prompt CF-center evaluation with sweat chloride and CFTR-directed testing rather than labeling the sinus disease idiopathic."
)

MANAGE_ADD = (
    " When a secondary driver is identified, treat the host disorder and the sinonasal inflammatory burden in parallel. Coordinate immune deficiency with Allergy/Immunology and recurrent-infection specialists; "
    "coordinate CF with the CF/pulmonary team because airway microbiology, infection-control practices and systemic CFTR-directed care matter. In CF or PCD, saline/topical anti-inflammatory therapy and selected ESS can improve clearance, "
    "symptom burden, surveillance and topical access, but surgery is not a cure for CFTR dysfunction or defective mucociliary clearance. Avoid repeating surgery or antibiotics without reassessing the underlying host disorder."
)

TEACH_ADD = (
    " Secondary-CRS senior rule: refractory CRSsNP is a prompt to ask WHY. Immune phenotype -> quantitative immunoglobulins plus functional antibody/vaccine-response assessment; "
    "CF phenotype -> sweat chloride/CFTR pathway with CF expertise; PCD phenotype -> referral-center multimodal testing, not TEM or nasal nitric oxide alone. "
    "The bailout is diagnostic: when treatment repeatedly fails, stop escalating routine CRS therapy until an occult host factor, odontogenic/focal source, fungal process or neoplasm has been reconsidered."
)


def apply_rhinology_secondary_crs_host_factor_depth_v354(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    matches = [r for r in rows if str(r.get("topic") or "") == TOPIC]
    if len(matches) != 1:
        raise RuntimeError(f"v35.4 expected exactly one exact-live {TOPIC!r} row; found {len(matches)}")
    row = matches[0]
    if row.get("source_grounded_v354"):
        return {"patched": [], "already_applied": [TOPIC]}
    row["workup"] = str(row.get("workup") or "") + WORKUP_ADD
    row["manage"] = str(row.get("manage") or "") + MANAGE_ADD
    row["teach"] = str(row.get("teach") or "") + TEACH_ADD
    existing_sources = list(row.get("source_basis") or [])
    for source in EXTRA_SOURCES:
        if source not in existing_sources:
            existing_sources.append(source)
    row["source_basis"] = existing_sources
    row["source_grounded_v354"] = True
    row["deliberate_review_v354"] = {
        "foundation": "secondary CRS host-factor phenotypes: humoral immune deficiency, CF/CFTR disease and PCD",
        "application": "cause-directed immune, CF and PCD diagnostic pathways rather than repeated empiric CRS treatment",
        "senior_decision": "multidisciplinary escalation and recognition that ESS improves access/burden but does not cure the systemic host defect",
    }
    return {"patched": [TOPIC], "canonical_id": data_module._v6_item_id(DOMAIN, TOPIC)}
