"""v36.1 — pediatric CRS age-specific diagnostic and treatment depth.

The existing Pediatric Chronic Rhinosinusitis ladder is preserved, including its strong
host-disorder/PCD escalation. This bounded successor adds the missing child-specific
sequence: distinguish persistent CRS from recurrent viral/adenoid disease, use objective
confirmation thoughtfully, treat host disease, use adenoidectomy as the usual first
surgical step in otherwise uncomplicated younger children, and reserve ESS for a defined
refractory/complicated target. It adds, removes, or renames no canonical topic.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Pediatric Chronic Rhinosinusitis"

SOURCE_BASIS_V361 = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — pediatric rhinosinusitis definition/differential, adenoid contribution, host disorders and medical/surgical management. Connected Google Drive source: CUMMINGS OTOLARYNGOLOGY–HEAD AND NECK 7th Ed 2021_compressed.pdf, file id 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022) — pediatric CRS differential, adenoid disease, medical therapy and ESS principles. Connected Google Drive file id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "K.J. Lee's Essential Otolaryngology, 12e — pediatric sinus development, chronic rhinosinusitis, adenoids, CF/PCD/immune disease and surgery principles. Connected Google Drive file id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "Brietzke SE et al. Clinical Consensus Statement: Pediatric Chronic Rhinosinusitis. Otolaryngol Head Neck Surg. 2014;151(4):542-553. PMID 25274375 — child-specific diagnostic and treatment framework, including adenoidectomy and selective ESS escalation.",
    "Orlandi RR et al. International consensus statement on allergy and rhinology: rhinosinusitis 2021. Int Forum Allergy Rhinol. 2021;11(3):213-739. PMID 33236525 — contemporary evidence framework for rhinosinusitis phenotyping, objective disease and treatment.",
    "Kais A et al. Predictors of Success of Adenoidectomy in the Treatment of Pediatric Chronic Rhinosinusitis. Ear Nose Throat J. 2024. PMID 38400707 — contemporary outcome data supporting adenoidectomy as an important first surgical intervention across children through age 12 after medical-therapy failure.",
    "Evaluation of balloon sinuplasty for the treatment of pediatric chronic rhinosinusitis. Curr Opin Otolaryngol Head Neck Surg. 2024. PMID 39392410 — evidence remains insufficient for routine balloon-first substitution; adenoidectomy remains first-line surgery and ESS is selected by imaging/clinical disease burden.",
    "Current evidence rechecked 2026-09-11: pediatric CRS should not be managed as miniature adult CRS; age, adenoid disease, sinus development and CF/PCD/immune phenotypes change diagnosis, sequencing and operative goals."
]

DEPTH_APPEND_V361 = {
    "recognize": " PEDIATRIC REFINEMENT — do not equate weeks of nasal symptoms in a child with CRS. Separate persistent inflammatory disease from serial viral URIs, chronic adenoiditis/adenoid hypertrophy, allergic/nonallergic rhinitis, reflux/irritant symptoms and foreign body. Pediatric CRS requires a compatible chronic symptom pattern plus objective evidence of sinonasal inflammation; symptom-free intervals instead suggest recurrent acute episodes rather than CRS.",
    "localize": " AGE-SPECIFIC REFINEMENT — localize both the sinonasal disease and the driver. Adenoids can function as an inflammatory/bacterial reservoir even when they are not massively obstructive. Map which sinuses are actually developed and diseased rather than importing an adult 'full-house' template. Look deliberately for nasal polyps, severe/refractory diffuse disease, bronchiectasis/chronic wet cough, neonatal respiratory distress, recurrent otitis, poor growth, unusual infections or family history that should reopen CF, PCD or immune evaluation.",
    "workup": " APPLICATION REFINEMENT — confirm that symptoms are chronic and concordant with endoscopy and/or appropriate imaging before escalating treatment. Nasal endoscopy can document purulence, edema, polyps and adenoid disease; CT is most useful when symptoms persist despite appropriate treatment, complications/atypical disease are suspected, or surgery is being planned rather than as a reflex test for every child with congestion. Culture selectively when refractory, unusual or host-factor disease makes microbiology actionable. Nasal polyposis or a strong lower-airway/systemic phenotype should trigger targeted host-disease evaluation instead of repeated empiric antibiotics.",
    "manage": " CHILD-SPECIFIC SEQUENCING — begin with appropriate medical management and treatment of contributing rhinitis/host disease; avoid simply repeating broad antibiotic courses without verifying the phenotype. When an otherwise uncomplicated child remains symptomatic after adequate medical therapy, ADENOIDECTOMY is generally the first surgical step because it addresses an important pediatric reservoir and may improve CRS even without dramatic obstructive hypertrophy. If symptoms persist after adenoidectomy, reassess the diagnosis, adherence, allergy, dental/focal disease and CF/PCD/immune context before escalating. Balloon dilation is not a default substitute for this sequence: evidence remains less robust and cost-effectiveness is unfavorable compared with established adenoidectomy/ESS pathways.",
    "operate": " SENIOR OPERATIVE REFINEMENT — perform ESS for a defined refractory target: persistent objectively confirmed disease after appropriate medical therapy and usually adenoid-directed treatment, significant anatomic/focal disease, complications, or selected CF/PCD/other high-burden phenotypes. Tailor the extent to the child's diseased, developed sinuses and the goal of drainage/topical access rather than automatically performing adult-style complete ESS. In very young children or systemic mucociliary disease, counsel that surgery improves ventilation/access but does not cure the underlying host defect. Orbital/intracranial complications follow the separate urgent source-control pathway and should not be delayed by the elective CRS sequence.",
    "teach": " CHIEF FRAMEWORK — PEDIATRIC CRS = PROVE THE PHENOTYPE, FIND THE DRIVER, ESCALATE IN CHILD-SPECIFIC ORDER. 1) distinguish persistent CRS from serial URI/adenoiditis/rhinitis; 2) use objective disease, not symptoms alone; 3) screen selectively for CF/PCD/immune disease when the phenotype demands it; 4) after medical therapy, adenoidectomy is commonly the first operation; 5) persistent disease earns diagnostic reassessment before ESS; 6) when ESS is needed, operate on the child's actual developed/diseased sinuses and a defined goal; 7) do not turn balloon dilation or adult-style full-house ESS into automatic shortcuts. Preserve the older PCD/CF senior case as the host-disease branch of this framework."
}


def apply_rhinology_peds_crs_v361(data_module, app_module=None):
    deep = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    rows = deep.get(DOMAIN, []) or []
    topics = [str(row.get("topic") or "") for row in rows]
    if len(rows) != 42 or len(set(topics)) != 42:
        raise RuntimeError(f"v36.1 requires exact 42-topic Rhinology inventory; got rows={len(rows)} unique={len(set(topics))}")
    matches = [row for row in rows if row.get("topic") == TOPIC]
    if len(matches) != 1:
        raise RuntimeError(f"v36.1 requires exactly one exact live {DOMAIN}/{TOPIC}; found {len(matches)}")
    row = matches[0]
    for field, extra in DEPTH_APPEND_V361.items():
        current = str(row.get(field) or "").strip()
        if extra not in current:
            row[field] = (current + extra).strip()
    sources = list(row.get("source_basis") or [])
    for source in SOURCE_BASIS_V361:
        if source not in sources:
            sources.append(source)
    row["source_basis"] = sources
    row["source_grounded_v361"] = True
    row["source_metadata_v361"] = {
        "canonical_link": {"domain": DOMAIN, "topic": TOPIC},
        "textbook_drive_ids": {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        },
        "preserved_ladder_ids": ["v136_rhi_21", "v144_rh_17", "v208_rhi_pedscrs_snr"],
        "evidence_checked": "2026-09-11",
    }
    row["deliberate_review_v361"] = {
        "foundation": "Defines pediatric CRS as persistent symptom phenotype plus objective inflammation and separates serial URI/adenoid/rhinitis mimics.",
        "application": "Uses endoscopy/imaging selectively, identifies adenoid contribution and triggers targeted CF/PCD/immune workup when phenotype demands it.",
        "senior_decision": "Sequences medical therapy to adenoidectomy, reassessment, then tailored ESS for a defined target; avoids adult-style or balloon-first shortcuts.",
        "traps": [
            "calling serial viral URIs chronic sinusitis",
            "treating adenoid size as the only reason adenoidectomy can help CRS",
            "ordering CT reflexively before an appropriate treatment trial",
            "repeating antibiotics without objective/phenotypic reassessment",
            "missing CF/PCD/immune disease in a multisystem phenotype",
            "skipping directly to adult-style complete ESS",
            "assuming adenoidectomy failure automatically proves the need for ESS",
            "using balloon dilation as a routine first surgical substitute",
            "forgetting sinus development and age when planning surgical extent",
            "delaying urgent complication source control to complete an elective CRS sequence",
        ],
    }
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [TOPIC], "count": 1}
