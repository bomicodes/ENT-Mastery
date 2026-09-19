"""v38.3 — Name FDA-approved CRSwNP biologics in the management field.

Adds drug names, targets and approval years while retaining existing individualized
management language. Idempotent and fails clearly if the canonical topic is absent.
"""

DOMAIN = "Rhinology / Allergy / Skull Base"
TOPIC = "CRSwNP"

ADDENDUM = (
    " As of 2025-26, four biologics carry an FDA-approved add-on CRSwNP "
    "indication, each targeting a different point in the type-2 cascade: "
    "dupilumab (anti-IL-4Ralpha, approved 2019), omalizumab (anti-IgE, "
    "approved 2020), mepolizumab (anti-IL-5, approved 2021), and tezepelumab "
    "(anti-TSLP, approved October 2025, ages 12+) -- the first CRSwNP "
    "biologic to target an upstream epithelial alarmin rather than a single "
    "downstream effector. Choice among them still follows the same "
    "individualized framework (asthma/AERD phenotype, steroid burden, prior "
    "surgery, access) rather than a fixed drug-per-phenotype rule, and this "
    "list should be re-verified against current FDA labeling before relying "
    "on it, since approvals in this class continue to change."
)

MARKER = "tezepelumab"


def apply_crswnp_biologics_named_v383(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    missing = True
    for module in modules:
        if module.get("topic") != TOPIC:
            continue
        missing = False
        manage = module.get("manage") or ""
        if MARKER.lower() not in manage.lower():
            module["manage"] = manage + ADDENDUM
            patched.append(TOPIC)
    if missing:
        raise RuntimeError(f"v38.3: topic '{TOPIC}' not found in domain '{DOMAIN}'")
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
