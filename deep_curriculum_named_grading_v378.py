"""v37.8: Named diagnostic and treatment criteria for three canonical deep modules.

Adult thyroid malignancy risks use the 2023 Bethesda third edition, not the
superseded 2017 ranges. Idempotent field additions and tag updates.
References: ACR TI-RADS atlas; 2023 Bethesda System (PMID 37438235);
RTOG 91-11 long-term results (PMID 23182993); UVFP guidelines
(PMC7669319). Clinical guidance is patient-specific.
"""

NODULE_TOPIC = "Thyroid Nodule"
LARYNX_TOPIC = "Laryngeal Preservation Decision"
UVFP_TOPIC = "Unilateral Vocal Fold Paralysis"

NODULE_WORKUP_ADDENDUM = (
    " USE THE NAMED RISK SYSTEMS, NOT JUST 'ULTRASOUND RISK': in adults, ACR TI-RADS "
    "scores composition, echogenicity, shape, margin, and echogenic foci. TR1 (0 points) "
    "and TR2 (2 points) do not routinely require FNA; TR3 (3 points): follow if >=1.5 cm, "
    "FNA if >=2.5 cm; TR4 (4-6 points): follow if >=1 cm, FNA if >=1.5 cm; "
    "TR5 (>=7 points): follow if >=0.5 cm, FNA if >=1 cm. Suspicious lymph nodes, "
    "radiation/familial risk, or other clinical concerns may alter this nodule-based pathway. "
    "REPORT FNA WITH THE 2023 BETHESDA SYSTEM (adult mean malignancy risk and range; "
    "risks depend on case mix and NIFTP classification): I nondiagnostic 13% (5-20%), "
    "repeat ultrasound-guided FNA; II benign 4% (2-7%), clinical/ultrasound follow-up; "
    "III atypia of undetermined significance (AUS) 22% (13-30%), repeat FNA, "
    "molecular testing, lobectomy or surveillance as indicated; IV follicular neoplasm "
    "30% (23-34%), molecular testing or diagnostic lobectomy; V suspicious for malignancy "
    "74% (67-83%), usually surgical evaluation with extent individualized; VI malignant "
    "97% (97-100%), cancer-specific surgical evaluation. The old terms AUS/FLUS and "
    "follicular/oncocytic neoplasm are often encountered in older resources, but the 2023 "
    "Bethesda category names are AUS and follicular neoplasm. Afirma/ThyroSeq primarily "
    "inform indeterminate Bethesda III/IV management; they do not replace cytology. "
    "Pediatric risk estimates and management differ."
)

NODULE_MANAGE_ADDENDUM = (
    " Let sonographic findings, cytology, clinical factors and patient preference determine "
    "the pathway: Bethesda II generally receives risk-adapted clinical/ultrasound follow-up; "
    "Bethesda III allows repeat FNA, molecular testing, surveillance or diagnostic lobectomy; "
    "Bethesda IV commonly prompts molecular testing or diagnostic lobectomy rather than "
    "mandatory repeat FNA; Bethesda V/VI generally prompt surgery or appropriate "
    "cancer-specific management, with extent decided by tumor size, pathology, nodes and "
    "risk factors rather than Bethesda category alone. Thermal ablation may be considered "
    "for appropriately verified benign symptomatic/cosmetic nodules in experienced hands; "
    "ethanol ablation is particularly used for recurrent symptomatic cystic nodules. "
    "These options do not replace indicated biopsy or malignancy evaluation."
)

LARYNX_MANAGE_ADDENDUM = (
    " EVIDENCE AND THRESHOLD BEHIND THE DEFAULT: RTOG 91-11 compared induction "
    "cisplatin/5-FU followed by radiation, concurrent cisplatin-radiation and radiation "
    "alone in selected stage III-IV glottic/supraglottic SCC. Concurrent treatment improved "
    "larynx preservation and locoregional control versus the other arms, but did NOT show "
    "a statistically significant overall-survival or laryngectomy-free-survival advantage "
    "over induction chemotherapy at long-term follow-up; late toxicity and functional "
    "larynx outcomes matter. High-volume T4 tumors penetrating through thyroid cartilage "
    "or extending >1 cm into the base of tongue were excluded. For resectable T4a disease "
    "with gross through-cartilage invasion or substantial extralaryngeal extension, primary "
    "total laryngectomy is generally considered; do not extrapolate RTOG 91-11 organ "
    "preservation results to this excluded group. Evaluate baseline swallowing, aspiration, "
    "airway, tumor extent and patient goals in multidisciplinary discussion."
)

UVFP_MANAGE_ADDENDUM = (
    " TIMING AND NAMED CLASSIFICATION: if neural recovery remains plausible and there is "
    "no known transection, spontaneous vocal fold motion recovery can occur within 6-12 "
    "months, though most recover earlier. Voice therapy and early temporary injection "
    "augmentation can address dysphonia, aspiration or high vocal demands during this "
    "period; significant aspiration warrants earlier intervention rather than waiting. "
    "Consider laryngeal EMG and etiology/prognosis when choosing earlier permanent "
    "medialization; a mandatory 6-12 month delay is not appropriate for every patient, "
    "especially with known irreversible nerve injury. ISSHIKI FRAMEWORK SURGERY: Type I "
    "medialization thyroplasty, Type II lateralization, Type III shortening/relaxation "
    "(pitch lowering), Type IV lengthening/tensioning (pitch raising). Type II is not a "
    "medialization operation for unilateral paralysis."
)


def _apply_field(module, field, marker, addendum):
    text = module.get(field, "") or ""
    if marker.casefold() not in text.casefold():
        module[field] = text.rstrip() + addendum


def _add_tags(module, tags):
    existing = module.setdefault("tags", [])
    for tag in tags:
        if tag not in existing:
            existing.append(tag)


def _apply_thyroid_nodule(deep_modules):
    patched = []
    for modules in deep_modules.values():
        for module in modules or []:
            if module.get("topic") != NODULE_TOPIC:
                continue
            _apply_field(module, "workup", "USE THE NAMED RISK SYSTEMS", NODULE_WORKUP_ADDENDUM)
            _apply_field(module, "manage", "Let sonographic findings, cytology", NODULE_MANAGE_ADDENDUM)
            _add_tags(module, ("Bethesda system", "TI-RADS", "molecular testing", "FNA size thresholds"))
            patched.append(module["topic"])
    return patched


def _apply_larynx(deep_modules):
    patched = []
    for modules in deep_modules.values():
        for module in modules or []:
            if module.get("topic") != LARYNX_TOPIC:
                continue
            _apply_field(module, "manage", "RTOG 91-11", LARYNX_MANAGE_ADDENDUM)
            _add_tags(module, ("RTOG 91-11", "T4a cartilage invasion"))
            patched.append(module["topic"])
    return patched


def _apply_uvfp(deep_modules):
    patched = []
    for modules in deep_modules.values():
        for module in modules or []:
            if module.get("topic") != UVFP_TOPIC:
                continue
            _apply_field(module, "manage", "ISSHIKI FRAMEWORK SURGERY", UVFP_MANAGE_ADDENDUM)
            _add_tags(module, ("Isshiki classification", "6-12 month observation window"))
            patched.append(module["topic"])
    return patched


def apply_named_grading_criteria_v378(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    results = {
        "thyroid_nodule": _apply_thyroid_nodule(deep_modules),
        "laryngeal_preservation_decision": _apply_larynx(deep_modules),
        "unilateral_vocal_fold_paralysis": _apply_uvfp(deep_modules),
    }
    missing = [name for name, patched in results.items() if not patched]
    if missing:
        raise RuntimeError(f"v37.8: could not find canonical topic(s) for: {missing}")
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"results": results, "count": sum(len(v) for v in results.values())}
