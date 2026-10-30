"""v49.2: real attending curveballs for Concept Checks.

Most concept-check curveballs were statements copied from teaching text (not questions), and many
answers were identical to the curveball or templated. ``cc_curveballs_v492/<batch>.py`` defines
``CURVEBALLS = {check_id: {"curveball", "curveball_answer"}}``; this replaces those two fields in place.
Checks whose wording a release audit pins are not included in the batches.
"""
import importlib
import pkgutil


def _load():
    import cc_curveballs_v492
    out = {}
    for info in sorted(pkgutil.iter_modules(cc_curveballs_v492.__path__), key=lambda i: i.name):
        out.update(getattr(importlib.import_module("cc_curveballs_v492." + info.name), "CURVEBALLS", {}))
    return out


def install_concept_check_curveballs_v492(data):
    new = _load()
    applied = 0
    for q in getattr(data, "CONCEPT_CHECKS_V112", None) or []:
        r = new.get(q.get("id"))
        if r and str(r.get("curveball", "")).strip().endswith("?") and str(r.get("curveball_answer", "")).strip():
            q["curveball"] = r["curveball"]
            q["curveball_answer"] = r["curveball_answer"]
            q["curveball_v492"] = True
            applied += 1
    result = {"applied": applied, "available": len(new)}
    data.CONCEPT_CHECK_CURVEBALLS_V492 = result
    return result
