"""v35.1 — source-grounded nonallergic rhinitis and olfactory dysfunction depth.

Durable diagnostic, physiology, and treatment principles are grounded in Cummings 7e,
K.J. Lee 12e, and Pasha 6e. Management is cross-checked against the 2020 Rhinitis
Practice Parameter and ICAR:Olfaction so the final production curriculum protects
phenotype-specific decisions rather than generic labels.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


CORE_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7e — rhinitis differential, nasal autonomic physiology, olfactory physiology, evaluation and disease-specific treatment principles",
    "K.J. Lee's Essential Otolaryngology, 12e — nonallergic rhinitis phenotypes/differential and practical olfactory-loss evaluation",
    "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — resident-level rhinitis treatment, smell-loss workup and safety counseling",
]


def _sources(*extra):
    return list(CORE_SOURCES) + list(extra)


# Exact live canonical topic names only. Do not alias-normalize these targets: a
# canonical inventory rename must fail closed instead of silently patching the wrong row.
PATCHES = {
    "Nonallergic Rhinitis / Rhinitis Medicamentosa": {
        "recognize": "Recognize NONALLERGIC RHINITIS (NAR) as a phenotype-driven chronic rhinitis syndrome in which symptoms such as congestion and rhinorrhea are not explained by clinically relevant systemic IgE-mediated allergy. Do not use 'vasomotor rhinitis' as a wastebasket diagnosis. Identify reproducible triggers and subphenotypes: irritant/odor exposure, temperature or weather change, gustatory rhinorrhea, medication effects, hormonal states, rhinitis medicamentosa, and eosinophilic NARES. Local allergic rhinitis is a separate possibility when systemic testing is negative but the history remains strongly allergen-linked.",
        "localize": "Localize the dominant problem by symptom physiology rather than by label alone. Predominant watery rhinorrhea points toward excessive parasympathetic/glandular secretion; congestion may reflect neurovascular mucosal swelling or coexisting inflammatory/structural disease. NARES has eosinophilic inflammation without conventional systemic sensitization, while local allergic rhinitis requires evidence of local allergen-driven disease. Septal deviation, valve compromise, turbinate hypertrophy, CRS, medication overuse and CSF rhinorrhea are not interchangeable with NAR.",
        "workup": "Start with trigger chronology, medication review, laterality, prior surgery/trauma, allergy pattern and focused nasal examination/endoscopy. Use skin-prick or serum-specific IgE testing selectively when the history leaves allergic rhinitis plausible; a negative systemic test does not automatically prove NAR or exclude local allergic rhinitis. Look for dangerous alternatives: unilateral persistent clear watery drainage after trauma/skull-base surgery, salty/metallic postnasal taste, recurrent meningitis or positional leakage should trigger CSF-leak evaluation rather than empiric rhinitis treatment; unilateral bleeding, mass effect or progressive obstruction requires structural/neoplastic evaluation.",
        "manage": "Treat the dominant phenotype. The 2020 Rhinitis Practice Parameter supports either an INTRANASAL ANTIHISTAMINE or INTRANASAL CORTICOSTEROID as first-line monotherapy for NAR, with combination therapy when needed. For predominantly watery rhinorrhea—especially gustatory or trigger-driven disease—INTRANASAL IPRATROPIUM is a high-yield symptom-directed option. Add saline and trigger avoidance when useful. Stop chronic topical decongestant overuse in rhinitis medicamentosa and transition to safer therapy. Do not prescribe allergen immunotherapy for nonspecific NAR without evidence of clinically relevant allergen-driven disease.",
        "operate": "Surgery does not treat the abstract diagnosis of NAR. Operate only when a separate anatomic problem—such as meaningful septal deviation, turbinate hypertrophy or nasal-valve dysfunction—contributes to obstruction after appropriate medical assessment. In refractory chronic rhinorrhea, posterior nasal nerve–targeted procedures may be considered in appropriately selected patients after phenotype confirmation and counseling, but first exclude CSF leak and other dangerous unilateral causes. Preserve a bailout mindset: unexplained unilateral clear drainage is a diagnostic problem before it is an ablation target.",
        "teach": "Senior model: NAR is not 'allergy tests negative, therefore vasomotor.' Ask what triggers the symptoms, which symptom dominates, and what competing diagnosis would make treatment unsafe. Match therapy to phenotype—ipratropium for secretion-dominant rhinorrhea, intranasal antihistamine and/or steroid for broader NAR symptoms—and reserve procedures for a defined structural or refractory-rhinorrhea indication. The dangerous miss is ablating or repeatedly treating a unilateral CSF leak as rhinitis.",
        "tags": ["nonallergic rhinitis", "NAR", "NARES", "ipratropium", "intranasal antihistamine", "rhinitis medicamentosa", "CSF leak"],
        "source_basis": _sources("Rhinitis 2020: A Practice Parameter Update (AAAAI/ACAAI Joint Task Force) — NAR phenotypes, intranasal antihistamine/INCS monotherapy, combination treatment, ipratropium and diagnostic distinctions"),
    },
    "Olfactory Dysfunction": {
        "recognize": "Recognize OLFACTORY DYSFUNCTION as a symptom that requires characterization rather than a single diagnosis: anosmia/hyposmia are quantitative loss, while parosmia and phantosmia are qualitative distortions. Separate common inflammatory/conductive causes such as CRSwNP/CRS from postviral, post-traumatic, medication/toxin-related, congenital and central/neurodegenerative causes. Sudden smell loss, persistent unilateral symptoms, focal neurologic findings or an associated sinonasal mass change the urgency and differential.",
        "localize": "Localize smell loss along the pathway. Conductive/inflammatory disease prevents odorant access to the olfactory cleft or alters local mucosal function; sensorineural injury can involve olfactory neuroepithelium/nerve after viral or traumatic injury; central dysfunction involves bulb, tract or higher cortical processing. Endoscopy can identify olfactory-cleft edema, polyps, tumor or postoperative anatomy, but a normal-appearing nose does not exclude postviral or central olfactory loss.",
        "workup": "Take a cause-focused history including onset, URI/COVID-like illness, head trauma, CRS/polyps, medications/toxic exposure, smoking, neurologic symptoms and qualitative distortions. Perform nasal examination/endoscopy and use VALIDATED PSYCHOPHYSICAL OLFACTORY TESTING when objective baseline, severity classification or follow-up matters; self-rating alone is insufficient. Imaging is targeted rather than automatic: obtain CT for suspected sinonasal inflammatory/structural disease and MRI when unexplained loss, unilateral findings, mass concern, trauma-related central injury or focal neurologic features warrant evaluation.",
        "manage": "Treat the underlying cause when one is identified. Optimize topical anti-inflammatory therapy for inflammatory CRS/CRSwNP rather than treating every smell loss with empiric systemic steroids. OLFACTORY TRAINING is a low-risk evidence-supported rehabilitation strategy for persistent olfactory dysfunction, particularly postviral loss, and requires repeated structured odor exposure over time rather than a one-time smell test. Counsel that parosmia may emerge during recovery and that prognosis varies by etiology, duration and severity. Avoid unsupported supplements or repeated systemic-steroid courses without a disease-specific rationale.",
        "operate": "Surgery is appropriate only when a surgically correctable sinonasal process contributes to the smell deficit—for example obstructive polyposis or other objective disease where ESS is otherwise indicated. The goal is disease control and restoration of olfactory-cleft access/topical delivery, not a guarantee of normal smell. Do not operate for isolated unexplained sensorineural/postviral anosmia. If unilateral olfactory-cleft disease or a mass is present, shift from routine smell-loss management to oncologic/skull-base diagnosis and safe tissue/imaging planning.",
        "teach": "Senior model: first classify the deficit, then localize CONDUCTIVE/INFLAMMATORY versus SENSORINEURAL/CENTRAL, objectively measure when useful, and investigate according to red flags. ICAR:Olfaction emphasizes evidence-based diagnostic testing and treatment rather than symptom-only labeling. Every persistent smell-loss patient also needs SAFETY COUNSELING—working smoke/CO detectors, gas/fire precautions, and attention to spoiled food—because anosmia creates real-world hazard even when no curative treatment exists.",
        "tags": ["olfactory dysfunction", "anosmia", "hyposmia", "parosmia", "psychophysical testing", "olfactory training", "safety counseling"],
        "source_basis": _sources("International Consensus Statement on Allergy and Rhinology: Olfaction (ICAR:Olfaction), 2022 with 2023 correction — evidence-based diagnosis, psychophysical testing, imaging, etiologies, olfactory training, treatment and safety counseling"),
    },
}


def apply_rhinology_nonallergic_olfaction_depth_v351(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        topic = str(module.get("topic") or "")
        payload = PATCHES.get(topic)
        if payload is None:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v351"] = True
        module["deliberate_review_v351"] = {
            "foundation": "phenotype/pathway definition, physiology/localization and high-value differential",
            "application": "selective objective workup plus phenotype- or etiology-specific treatment",
            "senior_decision": "dangerous-alternative recognition, procedure/imaging restraint, rehabilitation and safety counseling",
        }
        patched.append(topic)
    expected = set(PATCHES)
    actual = set(patched)
    if actual != expected:
        missing = sorted(expected - actual)
        unexpected = sorted(actual - expected)
        raise RuntimeError(
            "v35.1 canonical patch-target mismatch: "
            f"missing={missing or 'none'} unexpected={unexpected or 'none'}"
        )
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
