"""v36.5 — deepen the exact Facial Pain / Headache vs Rhinogenic Disease card.

This is a bounded learner-facing extension of one existing canonical Rhinology topic. It
adds no topic and deliberately separates objective sinonasal inflammatory disease from the
common but nonspecific label "sinus headache." Durable ENT anatomy/differential principles
are anchored to connected Cummings 7e, Pasha 6e, and K.J. Lee 12e; causation is updated to
ICHD-3 and contemporary CRS guidance.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TARGET = "Facial Pain / Headache vs Rhinogenic Disease"

CUMMINGS_ID = "18QGOAaZhvH-kEUJxtwDWXn1ho86PRY-t"
PASHA_ID = "14E4Iy4XCjGPSyMT5n7uyURGtIDnhi-52"
KJLEE_ID = "112c9y0fb1z_7OLP4aLlAG2z-r8weuXvR"

SOURCES = [
    f"Cummings Otolaryngology—Head and Neck Surgery, 7e [connected Drive {CUMMINGS_ID}] — rhinologic facial pain, CRS diagnostic confirmation, neurologic/dental mimics, and surgical-candidacy principles",
    f"Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e [connected Drive {PASHA_ID}] — sinus/facial pain differential, objective rhinologic evaluation, and resident management pearls",
    f"K.J. Lee's Essential Otolaryngology, 12e [connected Drive {KJLEE_ID}] — headache/facial pain differential and sinonasal disease evaluation",
    "International Headache Society. International Classification of Headache Disorders, 3rd edition (ICHD-3), section 11.5 — headache attributed to acute or chronic/recurring rhinosinusitis requires objective sinonasal disease plus evidence of causation; endoscopy/imaging abnormalities alone do not establish pain causation",
    "AAO-HNSF Clinical Practice Guideline: Adult Sinusitis Update, 2025 — CRS diagnosis requires objective confirmation of sinonasal inflammation and assessment of modifying factors rather than symptom labels alone",
    "AAO-HNSF Clinical Practice Guideline: Surgical Management of Chronic Rhinosinusitis, 2025 — surgery should be offered when objective disease, symptom burden, prior therapy, expected benefit, and patient goals support candidacy rather than for nonspecific facial pressure alone",
]

RECOGNIZE = (
    " FOUNDATION — 'SINUS HEADACHE' IS A SYMPTOM LABEL, NOT A DIAGNOSIS. The related phrase 'rhinogenic headache' should likewise trigger a causation question rather than be accepted as a diagnosis by itself. Facial pressure, frontal pain, nasal congestion, tearing, or weather sensitivity can occur with migraine and other primary headache disorders as well as sinonasal disease. A rhinogenic attribution requires a compatible sinonasal disorder plus objective evidence and a credible causal relationship. Reopen migraine, tension-type headache, trigeminal autonomic cephalalgia, trigeminal neuralgia/other neuropathic pain, dental disease, and temporomandibular disorder when the pain phenotype or objective nasal evaluation does not fit inflammatory sinus disease."
)

LOCALIZE = (
    " APPLICATION — localize from the pain phenotype instead of the word 'sinus.' Rhinosinusitis-associated pain should track a real inflammatory process; unilateral inflammatory disease can produce ipsilateral pain, but laterality alone is not proof. Brief electric-shock attacks with triggers suggest trigeminal neuralgia; strictly unilateral severe orbital/temporal attacks with prominent autonomic features demand a trigeminal-autonomic differential; jaw/dental provocation redirects toward odontogenic/TMJ disease. Severe focal pain with cranial neuropathy, orbital deficit, epistaxis, necrosis, or destructive imaging reopens neoplasm, invasive fungal disease, skull-base disease, and other dangerous secondary causes."
)

WORKUP = (
    " SENIOR WORKUP — first ask whether there is OBJECTIVE SINONASAL DISEASE on nasal endoscopy and/or appropriate imaging, then ask whether the pain behaves causally with that disease. ICHD-3 requires more than coincidental mucosal thickening: timing, worsening/improvement in parallel with rhinosinusitis, localization concordance, and exclusion of a better headache diagnosis matter. Incidental CT opacification or a septal spur/contact point that merely occupies the same side as pain is not sufficient by itself. When endoscopy and CT are normal or discordant with disabling pain, stop escalating antibiotics or sinus procedures and pursue the neurologic, dental, TMJ, ophthalmic, or other pathway suggested by the phenotype."
)

MANAGE = (
    " MANAGEMENT — treat proven acute or chronic rhinosinusitis according to its actual phenotype, but do not use treatment response as a license to keep relabeling recurrent migraine as infection. If objective CRS is present yet facial pain is disproportionate or persists despite successful inflammatory control, manage the CRS for its own indications and separately evaluate the residual headache disorder. Counsel patients explicitly that nasal/autonomic symptoms can accompany migraine. For proposed 'contact-point headache,' acknowledge that selected patients may improve after carefully chosen nasal surgery, but contact on CT/endoscopy is common and causation is uncertain; do not promise pain cure from anatomy alone."
)

OPERATE = (
    " OPERATIVE DECISION / BAILOUT — FESS is not a diagnostic trial for unexplained facial pain. Operate when objective sinonasal disease and the total clinical picture support a reasonable expectation that surgery will improve the rhinologic disease; do not perform or revise technically patent sinus surgery simply because facial pressure persists. Likewise, septoplasty/turbinate surgery for a presumed contact-point mechanism requires a coherent, carefully selected case rather than imaging contact alone. STOP the routine-rhinology pathway and escalate urgently for new neurologic deficit, vision change/ophthalmoplegia, thunderclap or rapidly progressive headache, meningismus, cranial neuropathy, necrotic tissue, or destructive/skull-base findings."
)

TEACH = (
    " CHIEF RULE — prove DISEASE, then prove CONCORDANCE. Objective endoscopy/CT can support rhinosinusitis, but it does not by itself prove the sinus abnormality caused the headache. 'Sinus headache' with a migraine phenotype and no objective inflammatory disease is migraine until another diagnosis is established. The senior move is often knowing when NOT to prescribe another antibiotic, obtain another low-value sinus scan, or offer FESS."
)


def _append(row, field, text):
    current = str(row.get(field) or "")
    if text not in current:
        row[field] = current + text


def apply_rhinology_facial_pain_v365(data_module, app_module=None):
    rows = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, []) or []
    by_topic = {str(r.get("topic") or ""): r for r in rows}
    if len(rows) != 42 or len(by_topic) != 42:
        raise RuntimeError(f"v36.5 requires exact 42-topic Rhinology inventory; got rows={len(rows)} unique={len(by_topic)}")
    if TARGET not in by_topic:
        raise RuntimeError(f"v36.5 missing exact canonical target: {TARGET!r}")

    row = by_topic[TARGET]
    if not row.get("source_grounded_v365"):
        for field, text in (
            ("recognize", RECOGNIZE), ("localize", LOCALIZE), ("workup", WORKUP),
            ("manage", MANAGE), ("operate", OPERATE), ("teach", TEACH),
        ):
            _append(row, field, text)
        source_basis = list(row.get("source_basis") or [])
        for source in SOURCES:
            if source not in source_basis:
                source_basis.append(source)
        row["source_basis"] = source_basis
        row["source_metadata_v365"] = {
            "connected_textbooks": {
                "Cummings 7e": CUMMINGS_ID,
                "Pasha 6e": PASHA_ID,
                "K.J. Lee 12e": KJLEE_ID,
            },
            "current_guidance": ["ICHD-3 section 11.5", "AAO-HNSF Adult Sinusitis CPG 2025", "AAO-HNSF Surgical Management of CRS CPG 2025"],
            "learner_boundary": "Objective sinonasal inflammation is necessary but not sufficient to attribute headache; concordance and exclusion of a better headache diagnosis are required.",
        }
        aliases = list(row.get("tags") or [])
        for alias in ("sinus headache", "rhinogenic headache", "facial pressure", "migraine", "contact point headache", "trigeminal neuralgia", "TAC"):
            if alias not in aliases:
                aliases.append(alias)
        row["tags"] = aliases
        row["source_grounded_v365"] = True
        row["deliberate_review_v365"] = {
            "foundation": "Separate nonspecific sinus-headache language from evidence-supported headache attributed to rhinosinusitis.",
            "application": "Require objective disease plus temporal/anatomic concordance and actively differentiate migraine, neuralgia, TAC, dental and TMJ pain.",
            "senior_decision": "Do not use FESS as a diagnostic trial for discordant pain; escalate secondary-headache danger signs and be explicit about contact-point uncertainty.",
        }

    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": [TARGET], "count": 1, "canonical_id": data_module._v6_item_id(DOMAIN, TARGET)}
