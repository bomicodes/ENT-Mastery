"""v37.6 — operationalize CRSsNP management decisions without false cutoffs.

Guidance: 2025 AAO-HNSF Adult Sinusitis Update, KAS 11, 13a and 14;
2025 AAO-HNSF Surgical Management of CRS, KAS 1A, 1B, 2 and 3.
https://aao-hnsfjournals.onlinelibrary.wiley.com/doi/10.1002/ohn.1344
https://aao-hnsfjournals.onlinelibrary.wiley.com/doi/10.1002/ohn.1287

The guidelines explicitly reject a universal antibiotic or medical-treatment duration
prerequisite, so this patch teaches actionable branches rather than fabricating a
fixed duration, biomarker threshold, or mandatory antibiotic course.
"""

TOPIC = "CRSsNP"
MARKER = "CRSSNP MANAGEMENT DECISION BRANCHES V376"
MANAGEMENT_ADDENDUM = (
    "\n\nCRSSNP MANAGEMENT DECISION BRANCHES V376 (2025 AAO-HNSF): FIRST confirm "
    "a chronic symptom syndrome plus objective inflammation on endoscopy or CT and "
    "document that there are no nasal polyps. For stable chronic inflammation without "
    "an acute bacterial exacerbation, use saline nasal irrigation, topical intranasal "
    "corticosteroid, or both; check technique, adherence, symptom burden and objective "
    "disease before changing treatment. Do NOT prescribe routine antibiotics merely "
    "for chronic symptoms or a CT abnormality, and do NOT require antibiotics as a "
    "prerequisite for CT or ESS. If there is a convincing acute bacterial exacerbation "
    "with significant/persistent purulent drainage, reassess clinically and consider "
    "appropriate acute infection treatment; culture is useful selectively in refractory "
    "purulence or unusual hosts, not automatically in every CRS patient. When persistent "
    "objective disease significantly affects quality of life despite appropriate "
    "patient-specific medical treatment, discuss ESS based on symptoms, disease "
    "characteristics, prior treatment and expected benefit; there is NO guideline-mandated "
    "number of weeks or antibiotic/steroid checklist before surgery. Do not routinely "
    "offer biologics for CRSsNP; if asthma or another condition independently warrants "
    "one, treat that condition rather than mislabeling it as a CRSsNP indication. "
    "Unilateral or maxillary-predominant disease requires attention to dental/focal causes; "
    "discordant symptoms with minimal objective inflammation warrant evaluation for "
    "migraine, neuralgia or other non-sinus drivers instead of escalating sinus therapy."
)


def apply_crssnp_management_v376(data_module, app_module=None):
    patched = []
    for modules in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).values():
        for module in modules or []:
            if module.get("topic") != TOPIC:
                continue
            current = str(module.get("manage") or "")
            if MARKER not in current:
                module["manage"] = current.rstrip() + MANAGEMENT_ADDENDUM
            tags = module.setdefault("tags", [])
            for tag in ("CRSsNP management decision", "2025 AAO-HNS CRS", "no routine antibiotics", "no routine biologics", "ESS candidacy"):
                if tag not in tags:
                    tags.append(tag)
            patched.append(TOPIC)
    if not patched:
        raise RuntimeError("v37.6: canonical CRSsNP topic not found")
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
