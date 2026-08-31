"""Cumulative Concept Hub production bridge through v34.3.

The final Render entrypoint imports runtime_entry_pasha, so source-grounded Concept Hub
rebuilds added after v28.4 must be applied there. This bridge intentionally applies the
bounded deep-curriculum modules in version order; each patch is idempotent and later
rebuilds win when a concept is intentionally revisited.

The historical filename/function remain v314 for compatibility with the production
entrypoint, but the module registry below is authoritative and now runs through v34.3.
"""

import importlib
import inspect
import re

MODULES_V314 = [
    "deep_curriculum_rhinology_v285",
    "deep_curriculum_headneck_v286",
    "deep_curriculum_headneck_v287",
    "deep_curriculum_headneck_v288",
    "deep_curriculum_headneck_v289",
    "deep_curriculum_peds_v290",
    "deep_curriculum_sleep_v296",
    "deep_curriculum_sleep_v298",
    "deep_curriculum_rhinology_v299",
    "deep_curriculum_rhinology_v304",
    "deep_curriculum_larynx_v305",
    "deep_curriculum_headneck_v306",
    "deep_curriculum_thyroid_v307",
    "deep_curriculum_headneck_v308",
    "deep_curriculum_headneck_v309",
    "deep_curriculum_peds_v310",
    "deep_curriculum_otology_v311",
    "deep_curriculum_parathyroid_v312",
    "deep_curriculum_otology_v313",
    "deep_curriculum_headneck_v314",
    "deep_curriculum_peds_v315",
    "deep_curriculum_headneck_v316",
    "deep_curriculum_headneck_v317",
    "deep_curriculum_thyroid_v318",
    "deep_curriculum_otology_v319",
    "deep_curriculum_thyroid_v320",
    "deep_curriculum_rhinology_v321",
    "deep_curriculum_otology_v322",
    "deep_curriculum_headneck_v323",
    "deep_curriculum_facialtrauma_v324",
    "deep_curriculum_facialtrauma_v325",
    "deep_curriculum_headneck_v326",
    "deep_curriculum_rhinology_v327",
    "deep_curriculum_facialtrauma_v328",
    "deep_curriculum_otology_v329",
    "deep_curriculum_headneck_v330",
    "deep_curriculum_peds_v331",
    "deep_curriculum_rhinology_v332",
    "deep_curriculum_peds_v333",
    "deep_curriculum_thyroid_v334",
    "deep_curriculum_headneck_v335",
    "deep_curriculum_reconstruction_v335",
    "deep_curriculum_parathyroid_v336",
    "deep_curriculum_headneck_v337",
    "deep_curriculum_otology_v338",
    "deep_curriculum_otology_v339",
    "deep_curriculum_salivary_v340",
    "deep_curriculum_facialplastics_v341",
    "deep_curriculum_facialplastics_v342",
    "deep_curriculum_facialplastics_v343",
]


def _version(module_name):
    match = re.search(r"_v(\d+)$", module_name)
    return match.group(1) if match else ""


def _apply_function(module, version):
    candidates = []
    for name in dir(module):
        obj = getattr(module, name)
        if callable(obj) and name.startswith("apply_") and name.endswith("_v" + version):
            candidates.append((name, obj))
    if len(candidates) != 1:
        raise RuntimeError(
            f"Expected exactly one apply_*_v{version} function in {module.__name__}; "
            f"found {[name for name, _ in candidates]}"
        )
    return candidates[0]


def apply_deep_curriculum_production_chain_v314(data_module, app_module=None):
    applied = []
    for module_name in MODULES_V314:
        module = importlib.import_module(module_name)
        version = _version(module_name)
        fn_name, fn = _apply_function(module, version)
        params = list(inspect.signature(fn).parameters.values())
        if len(params) >= 2:
            result = fn(data_module, app_module)
        else:
            result = fn(data_module)
        applied.append({"module": module_name, "function": fn_name, "result": result})
    return {"applied": applied, "count": len(applied)}
