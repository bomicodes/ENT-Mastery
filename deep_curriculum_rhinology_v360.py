"""v36.0 — isolated sphenoid/posterior sinus clinical depth on the exact Sphenoidotomy card.

The existing three-stage ladder is intentionally preserved: it already teaches sphenoidotomy
anatomy and carotid/optic operative safety well. This bounded successor adds the missing
clinical-disease layer: presentation, differential, imaging escalation, urgency and pathology-
specific management. It adds, removes, or renames no canonical topic.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "Sphenoidotomy"

SOURCE_BASIS_V360 = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e (2021) — sphenoid sinus anatomy, isolated sphenoid inflammatory/fungal/mucocele/neoplastic disease, imaging, complications and endoscopic surgical principles. Connected Google Drive source: CUMMINGS OTOLARYNGOLOGY–HEAD AND NECK 7th Ed 2021_compressed.pdf, file id 18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t.",
    "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e (2022) — paranasal sinus differential, sphenoid/skull-base danger anatomy and endoscopic management framework. Connected Google Drive file id 14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52.",
    "K.J. Lee's Essential Otolaryngology, 12e — sphenoid sinus disease, fungal disease, mucoceles, neoplasia and endoscopic sinus surgery principles. Connected Google Drive file id 112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR.",
    "Moss WJ et al. Isolated sphenoid sinus opacifications: a systematic review and meta-analysis. Int Forum Allergy Rhinol. 2017;7(12):1201-1206. PMID 29024448. doi:10.1002/alr.22023 — isolated sphenoid opacification has a broad differential including inflammatory disease, mucocele, fungal disease and neoplasia; cranial neuropathy is a meaningful presentation.",
    "Clinical Findings in Symptomatic Patients With Radiologically Isolated Sphenoid Sinus Disease: A Systematic Review and Meta-Analysis. Clin Otolaryngol. 2025. PMID 40040258 — headache is the dominant presentation; visual symptoms are clinically important and nasal endoscopy is frequently negative, so a normal endoscopic examination does not exclude clinically significant isolated sphenoid disease.",
    "Current evidence distinction (rechecked 2026-09-11): isolated sphenoid opacification is an anatomic finding, not a single diagnosis; urgent visual/cranial-neuropathy presentations and suspected invasive/vascular/neoplastic disease require escalation beyond routine inflammatory-sinus pathways."
]

DEPTH_APPEND_V360 = {
    "recognize": " FOUNDATION REFINEMENT — ISOLATED SPHENOID DISEASE is a differential, not a synonym for sinusitis. Headache may be the only complaint and nasal endoscopy can be normal. Think inflammatory sphenoiditis, noninvasive fungal ball, mucocele/mucopyocele, benign or malignant tumor, skull-base/intracranial lesion and less common vascular pathology. Visual loss, diplopia, ophthalmoplegia or another cranial neuropathy is a danger presentation because the optic nerve, cavernous sinus and internal carotid artery border the sinus.",
    "localize": " APPLICATION REFINEMENT — use CT to define isolated opacification, bony sclerosis/erosion, ostial obstruction, pneumatization, optic/carotid relationships, Onodi cells and septal insertions; add contrast MRI when a mass, skull-base/cavernous-sinus process, cranial neuropathy, invasive fungal disease or intracranial/orbital extension is possible. A negative office endoscopy does not clear the sphenoid when the symptom pattern or imaging remains concerning.",
    "workup": " SENIOR DIAGNOSTIC REFINEMENT — do not let months of nonspecific headache or a normal nasal examination delay evaluation of a persistent isolated sphenoid abnormality. New visual decline, afferent pupillary defect, diplopia/ophthalmoplegia, severe progressive headache, multiple cranial neuropathies, neurologic findings or systemic toxicity requires urgent imaging and multidisciplinary escalation. If imaging suggests a vascular lesion or carotid abnormality, obtain vascular-safe evaluation before biopsy or routine instrumentation; if neoplasia is plausible, plan tissue diagnosis and staging rather than treating radiographic opacity as chronic sinusitis.",
    "manage": " SENIOR MANAGEMENT REFINEMENT — match treatment to pathology. Uncomplicated acute inflammatory disease can begin with appropriate medical therapy, but persistent/refractory isolated disease or an uncertain unilateral sphenoid opacity often needs endoscopic drainage and tissue diagnosis. Noninvasive fungal ball is treated by surgical clearance/ventilation rather than routine systemic antifungal therapy; a mucocele requires durable marsupialization when symptomatic, expanding or threatening adjacent structures; tumor management follows histology/staging; suspected invasive fungal disease follows the separate emergency debridement/systemic-antifungal pathway. Visual or cranial-nerve compromise lowers the threshold for urgent decompression/source control when a sphenoid process is causal.",
    "operate": " OR DECISION REFINEMENT — the operation should create safe durable access to the actual disease, not maximal lateral/superior enlargement. Identify the natural ostium and preoperative optic/carotid/skull-base map, enlarge under direct control, clear obstructing inflammatory/fungal material or marsupialize the lesion, and send pathology/microbiology when the diagnosis is not already secure. Preserve or deliberately drill around carotid-attached septa rather than torquing them. If orientation is uncertain, disease extends beyond a safe endonasal corridor, or unexpected brisk bleeding/CSF/visual-risk anatomy appears, STOP, re-localize with imaging/navigation and escalate the approach/team rather than forcing exposure. Plan endoscopic follow-up for restenosis or recurrent disease.",
    "teach": " CHIEF FRAMEWORK — SPHENOID = CLINICAL DISEASE + DANGER ANATOMY. 1) headache with a normal nose can still be sphenoid disease; 2) distinguish inflammation, fungal ball, mucocele and tumor instead of treating every opacity as CRS; 3) visual/CN findings are urgent; 4) CT maps bone and danger anatomy, MRI maps soft tissue/skull base/cavernous sinus; 5) operate for a defined diagnostic/therapeutic goal; 6) never trade carotid/optic safety for a larger cavity. The older ladder remains the operative-anatomy foundation; v36.0 adds the disease reasoning it lacked."
}


def apply_rhinology_sphenoid_v360(data_module, app_module=None):
    deep = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    rows = deep.get(DOMAIN, []) or []
    by_topic = {str(row.get("topic") or ""): row for row in rows}
    if len(rows) != 42 or len(by_topic) != 42:
        raise RuntimeError(f"v36.0 requires exact 42-topic Rhinology inventory; got rows={len(rows)} unique={len(by_topic)}")
    matches = [row for row in rows if row.get("topic") == TOPIC]
    if len(matches) != 1:
        raise RuntimeError(f"v36.0 requires exactly one exact live {DOMAIN} / {TOPIC!r}; found {len(matches)}")
    row = matches[0]
    for field, addition in DEPTH_APPEND_V360.items():
        current = str(row.get(field) or "").strip()
        if addition not in current:
            row[field] = (current + " " + addition).strip()
    source_basis = list(row.get("source_basis") or [])
    for source in SOURCE_BASIS_V360:
        if source not in source_basis:
            source_basis.append(source)
    row["source_basis"] = source_basis
    row["source_grounded_v360"] = True
    row["source_metadata_v360"] = {
        "canonical_link": {"domain": DOMAIN, "topic": TOPIC},
        "identity_rule": "exact live canonical domain/topic equality; canonical count must remain 42",
        "textbook_drive_ids": {
            "cummings_7e": "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t",
            "pasha_6e": "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52",
            "kj_lee_12e": "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR",
        },
        "management_currency": "Core-text anatomy/pathology cross-referenced with systematic-review evidence through 2025 and rechecked 2026-09-11.",
        "preserved_ladder_ids": ["v136_rhi_26", "v144_rh_21", "v209_rhi_sphenoid_snr"],
    }
    row["deliberate_review_v360"] = {
        "foundation": "recognize isolated sphenoid opacity as a broad clinical differential whose headache-predominant presentation may have a normal nasal endoscopy",
        "application": "use CT/MRI and red-flag cranial-neuropathy findings to distinguish inflammatory, fungal, mucocele, neoplastic, skull-base and vascular processes",
        "senior_decision": "match medical therapy, endoscopic drainage/tissue diagnosis, urgent decompression or multidisciplinary oncologic/invasive-fungal/vascular escalation to the actual pathology while preserving optic/carotid safety",
        "traps": [
            "equating isolated sphenoid opacification with routine CRS",
            "using a normal nasal endoscopy to exclude sphenoid disease",
            "ignoring visual loss or ophthalmoplegia as a time-sensitive sphenoid complication",
            "assuming headache location alone proves sphenoid causality",
            "treating a noninvasive fungal ball with systemic antifungal therapy instead of clearance/ventilation",
            "biopsying or instrumenting a possible vascular lesion without vascular-safe planning",
            "torquing an intersinus septum attached to the carotid canal",
            "maximally widening superior/lateral sphenoid walls when the disease goal is already met",
        ],
    }
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [TOPIC], "count": 1, "canonical_topic": TOPIC}
