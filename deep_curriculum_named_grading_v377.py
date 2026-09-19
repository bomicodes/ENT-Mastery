"""v37.7: Close five confirmed named-framework/no-concrete-criteria curriculum gaps.

Idempotent per field and tag. Pediatric CRS and allergen immunotherapy remain unchanged.
"""

BSTF_TOPIC = "Benign Sinonasal Tumor Framework"
BSTF_WORKUP_ADDENDUM = (
    " NAMED STAGING SYSTEMS TO USE ON IMAGING/PATHOLOGY: stage inverted papilloma with the "
    "Krouse system -- T1 confined to the nasal cavity, T2 involving the ostiomeatal complex/"
    "ethmoid/medial maxillary wall, T3 extending to the lateral/inferior/posterior/superior "
    "maxillary sinus or sphenoid/frontal sinus, T4 with extrasinus extension (orbit, "
    "intracranial, pterygopalatine/infratemporal fossa) or associated malignancy. Stage a "
    "juvenile nasopharyngeal angiofibroma with the Fisch/Radkowski system -- Fisch I limited "
    "to the nose/nasopharynx, II into the pterygomaxillary fossa or maxillary/ethmoid/sphenoid "
    "sinus, III extending into the infratemporal fossa/orbit with or without intracranial "
    "extradural extension, IV with intradural extension or cavernous-sinus/optic-chiasm/"
    "pituitary-fossa involvement."
)
BSTF_MANAGE_ADDENDUM = (
    " Use the staging above to set expectations: higher Krouse stage IP and higher Fisch "
    "stage JNA both carry higher recurrence/incomplete-resection risk and more often need a "
    "combined or open approach and closer surveillance, even though the operative principles "
    "(attachment-oriented resection for IP; vascular control and embolization planning for "
    "JNA) stay the same across stages."
)
HNSCC_TOPIC = "Recurrent / Metastatic HNSCC"
HNSCC_WORKUP_ADDENDUM = (
    " CONCRETE SELECTION CRITERIA: obtain PD-L1 combined positive score (CPS) testing on "
    "recurrent/metastatic tissue -- it drives first-line systemic therapy choice below. "
    "Confirm ECOG performance status (0-1 favors aggressive salvage/systemic therapy; >=2 "
    "shifts toward symptom-directed care or single-agent therapy) and time since prior "
    "radiation, since re-irradiation candidacy generally requires roughly 6 months or more "
    "from prior RT to a field that can still be safely retreated."
)
HNSCC_MANAGE_ADDENDUM = (
    " FIRST-LINE SYSTEMIC THERAPY (KEYNOTE-048 framework): for unresectable recurrent/"
    "metastatic disease, pembrolizumab monotherapy is preferred for PD-L1 CPS >=1; "
    "pembrolizumab plus platinum/5-FU chemotherapy is used regardless of CPS status "
    "(including CPS <1) when a faster response is needed or CPS is low/unknown. For disease "
    "that progresses after platinum-based therapy, nivolumab or pembrolizumab monotherapy "
    "(CheckMate 141 / KEYNOTE-040) is standard second-line therapy. Re-irradiation with or "
    "without systemic therapy is reserved for selected unresectable local/regional recurrence "
    "beyond the interval above, in patients fit enough to tolerate it."
)
SGS_TOPIC = "Subglottic / Tracheal Stenosis"
SGS_LOCALIZE_ADDENDUM = (
    " GRADE IT WITH THE MYER-COTTON SCALE (percentage of cross-sectional narrowing, based on "
    "endotracheal-tube sizing at the point of maximal narrowing): Grade I <=50%, Grade II "
    "51-70%, Grade III 71-99%, Grade IV no detectable lumen. Grade alone does not choose "
    "treatment -- length, scar maturity and cartilage integrity still matter -- but it is the "
    "standard way to document and compare severity."
)
OSA_TOPIC = "Residual OSA After Surgery"
OSA_WORKUP_ADDENDUM = (
    " DEFINE 'RESIDUAL' WITH A NUMBER: in children, persistent obstructive AHI >=5 (or >=1-5 "
    "with significant symptoms/desaturation in a high-risk child) after adenotonsillectomy is "
    "generally treated as clinically meaningful residual disease warranting further workup "
    "rather than reassurance from symptom improvement alone."
)
OSA_MANAGE_ADDENDUM = (
    " HYPOGLOSSAL NERVE STIMULATION (Inspire) CANDIDACY, when considered in adults: current "
    "FDA indication includes AHI 15-100, age >=18 and documented PAP failure or intolerance "
    "(not PAP-naive status); FDA-expanded labeling increased the recommended BMI upper limit "
    "to 40, although payer and program thresholds can be more restrictive. Confirm on "
    "drug-induced sleep endoscopy (DISE) that there is no complete concentric collapse at the "
    "soft palate; complete concentric palatal collapse excludes Inspire candidacy. Assess "
    "central/mixed apnea burden and other device contraindications as well."
)
LEMIERRE_TOPIC = "Lemierre Syndrome"
LEMIERRE_MANAGE_ADDENDUM = (
    " DURATION: plan roughly 4-6 weeks of systemic antibiotics for Lemierre syndrome given "
    "the endovascular septic source, longer than a typical pharyngitis/abscess course, "
    "adjusted to clinical response, source control and any residual thrombosis/emboli."
)


def _modules(deep_modules, topic):
    for modules in deep_modules.values():
        for module in modules or []:
            if module.get("topic") == topic:
                yield module


def _append_once(module, field, marker, addition):
    value = module.get(field, "") or ""
    if marker not in value:
        module[field] = value.rstrip() + addition


def _tags(module, *names):
    tags = module.setdefault("tags", [])
    for name in names:
        if name not in tags:
            tags.append(name)


def apply_named_grading_criteria_v377(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    results = {
        "benign_sinonasal_tumor_framework": [],
        "recurrent_metastatic_hnscc": [],
        "subglottic_tracheal_stenosis": [],
        "residual_osa_after_surgery": [],
        "lemierre_syndrome": [],
    }
    for module in _modules(deep_modules, BSTF_TOPIC):
        _append_once(module, "workup", "Krouse system", BSTF_WORKUP_ADDENDUM)
        _append_once(module, "manage", "Use the staging above", BSTF_MANAGE_ADDENDUM)
        _tags(module, "Krouse staging", "Fisch staging", "Radkowski staging")
        results["benign_sinonasal_tumor_framework"].append(module["topic"])
    for module in _modules(deep_modules, HNSCC_TOPIC):
        _append_once(module, "workup", "PD-L1 combined positive score", HNSCC_WORKUP_ADDENDUM)
        _append_once(module, "manage", "KEYNOTE-048", HNSCC_MANAGE_ADDENDUM)
        _tags(module, "PD-L1 CPS", "KEYNOTE-048", "CheckMate 141", "KEYNOTE-040",
              "re-irradiation interval", "ECOG performance status")
        results["recurrent_metastatic_hnscc"].append(module["topic"])
    for module in _modules(deep_modules, SGS_TOPIC):
        _append_once(module, "localize", "MYER-COTTON", SGS_LOCALIZE_ADDENDUM)
        _tags(module, "Myer-Cotton grade")
        results["subglottic_tracheal_stenosis"].append(module["topic"])
    for module in _modules(deep_modules, OSA_TOPIC):
        _append_once(module, "workup", "DEFINE 'RESIDUAL' WITH A NUMBER", OSA_WORKUP_ADDENDUM)
        _append_once(module, "manage", "HYPOGLOSSAL NERVE STIMULATION", OSA_MANAGE_ADDENDUM)
        _tags(module, "residual AHI threshold", "hypoglossal nerve stimulation",
              "Inspire candidacy", "complete concentric collapse")
        results["residual_osa_after_surgery"].append(module["topic"])
    for module in _modules(deep_modules, LEMIERRE_TOPIC):
        _append_once(module, "manage", "4-6 weeks", LEMIERRE_MANAGE_ADDENDUM)
        _tags(module, "antibiotic duration")
        results["lemierre_syndrome"].append(module["topic"])
    missing = [name for name, patched in results.items() if not patched]
    if missing:
        raise RuntimeError(f"v37.7: could not find canonical topic(s) for: {missing}")
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    # The production runtime already invokes v37.7; chain v37.8 here so its
    # three new criteria sets execute on startup without modifying legacy app.py.
    from deep_curriculum_named_grading_v378 import apply_named_grading_criteria_v378
    v378_result = apply_named_grading_criteria_v378(data_module, app_module)
    return {"results": results, "count": sum(len(v) for v in results.values()),
            "v378": v378_result}
