"""v37.9: Add operational BWH staging, prophylactic central neck dissection criteria,
and postoperative thyroid calcium/PTH thresholds to the canonical deep curriculum.
Idempotent per field; unrelated scanner false positives are unchanged.
"""

CSCC_TOPIC = "Cutaneous Squamous Cell Carcinoma of the Head & Neck"
CND_TOPIC = "Central Neck Dissection"
HUNGRY_BONE_TOPIC = "Hungry Bone / Post-Thyroid Calcium Management"

CSCC_WORKUP_ADDENDUM = (
    " THE FOUR BWH RISK FACTORS THAT ACTUALLY SET THE STAGE: tumor diameter >=2 cm, poor "
    "differentiation, perineural invasion of a nerve >=0.1 mm, and tumor invasion beyond "
    "subcutaneous fat (excluding bone invasion, which is scored separately). Stage by how "
    "many of these are present: T1 = zero factors, T2a = one factor, T2b = two or three "
    "factors, T3 = four factors or bone invasion. T2b and T3 carry substantially higher "
    "nodal-metastasis and disease-specific-death risk than T1/T2a, which is why they "
    "generally justify the imaging and multidisciplinary-discussion threshold described "
    "above rather than routine excision alone."
)

CND_MANAGE_ADDENDUM = (
    " WHAT ACTUALLY PUSHES TOWARD PROPHYLACTIC (cN0) CENTRAL NECK DISSECTION: a primary tumor "
    ">4 cm, gross extrathyroidal extension, clinically apparent lateral neck disease (cN1b) "
    "even when the central compartment looks clinically negative, or a situation where nodal "
    "status will materially change the RAI/follow-up plan. Low-risk small intrathyroidal "
    "papillary carcinoma without these features generally does NOT warrant prophylactic CND "
    "given the added hypoparathyroidism/RLN-injury risk for an uncertain oncologic benefit."
)

HUNGRY_BONE_WORKUP_ADDENDUM = (
    " NUMBERS USED AT THE BEDSIDE: an intact PTH drawn roughly 1 hour after thyroidectomy "
    "below approximately 10-15 pg/mL predicts a high risk of symptomatic hypocalcemia and "
    "supports starting empiric calcium/calcitriol before the patient becomes symptomatic, "
    "rather than waiting for a low calcium level to appear."
)

HUNGRY_BONE_MANAGE_ADDENDUM = (
    " TYPICAL DOSING AND TRIGGERS: start oral calcium carbonate or citrate roughly 1-2 g "
    "elemental calcium divided through the day for mild/asymptomatic postoperative "
    "hypocalcemia, adding calcitriol (commonly 0.25-0.5 mcg twice daily) when PTH is low or "
    "risk is high. Reserve monitored IV calcium gluconate for symptomatic hypocalcemia or a "
    "corrected serum calcium roughly below 7.0-7.5 mg/dL, with magnesium repletion first when "
    "magnesium is low, since hypocalcemia will not correct until magnesium is restored."
)


def _apply_cscc(deep_modules):
    patched = []
    for modules in deep_modules.values():
        for module in modules or []:
            if module.get("topic") != CSCC_TOPIC:
                continue
            workup = module.get("workup", "") or ""
            if "FOUR BWH RISK FACTORS" not in workup:
                module["workup"] = workup.rstrip() + CSCC_WORKUP_ADDENDUM
            tags = module.setdefault("tags", [])
            for tag in ("BWH staging criteria", "T2b", "T3 cutaneous SCC"):
                if tag not in tags:
                    tags.append(tag)
            patched.append(module.get("topic"))
    return patched


def _apply_cnd(deep_modules):
    patched = []
    for modules in deep_modules.values():
        for module in modules or []:
            if module.get("topic") != CND_TOPIC:
                continue
            manage = module.get("manage", "") or ""
            if "WHAT ACTUALLY PUSHES TOWARD PROPHYLACTIC" not in manage:
                module["manage"] = manage.rstrip() + CND_MANAGE_ADDENDUM
            tags = module.setdefault("tags", [])
            for tag in ("prophylactic CND criteria", "cN1b", "extrathyroidal extension"):
                if tag not in tags:
                    tags.append(tag)
            patched.append(module.get("topic"))
    return patched


def _apply_hungry_bone(deep_modules):
    patched = []
    for modules in deep_modules.values():
        for module in modules or []:
            if module.get("topic") != HUNGRY_BONE_TOPIC:
                continue
            workup = module.get("workup", "") or ""
            if "NUMBERS USED AT THE BEDSIDE" not in workup:
                module["workup"] = workup.rstrip() + HUNGRY_BONE_WORKUP_ADDENDUM
            manage = module.get("manage", "") or ""
            if "TYPICAL DOSING AND TRIGGERS" not in manage:
                module["manage"] = manage.rstrip() + HUNGRY_BONE_MANAGE_ADDENDUM
            tags = module.setdefault("tags", [])
            for tag in ("postop PTH cutoff", "calcium/calcitriol dosing", "IV calcium threshold"):
                if tag not in tags:
                    tags.append(tag)
            patched.append(module.get("topic"))
    return patched


def apply_named_grading_criteria_v379(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    results = {
        "cutaneous_scc_head_neck": _apply_cscc(deep_modules),
        "central_neck_dissection": _apply_cnd(deep_modules),
        "hungry_bone_post_thyroid_calcium": _apply_hungry_bone(deep_modules),
    }
    missing = [name for name, patched in results.items() if not patched]
    if missing:
        raise RuntimeError(f"v37.9: could not find canonical topic(s) for: {missing}")
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"results": results, "count": sum(len(v) for v in results.values())}
