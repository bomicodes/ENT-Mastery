"""v49.0 board-style vignette expansion: brings every curriculum topic to 10 practice questions.

Authored items live in ``vignettes_v490/<group>.py`` as ``VIGNETTES`` lists. Each item is
validated, given a stable id (``v490-<group>-<n>``), and appended to the practice bank so it
appears on /clinical-challenges, in Concept Hub question lists, and in the Daily Path.
Must run before the Daily Path installer, which indexes questions at install time.
"""
import importlib
import pkgutil

REQUIRED = ("topic", "concept_id", "stem", "choices", "answer", "explanation", "why_wrong",
            "board_pearl", "curveball", "curveball_answer", "learning_stage", "focus")
MODE = {"diagnosis": "Recognize", "anatomy": "Recognize", "imaging": "Recognize", "mechanism": "Reasoning",
        "pharmacology": "Reasoning", "workup": "Workup", "management": "Manage", "counseling": "Manage",
        "surgery": "Operate", "complication": "Operate", "pediatrics": "Reasoning"}


def _load():
    import vignettes_v490
    out = []
    for info in sorted(pkgutil.iter_modules(vignettes_v490.__path__), key=lambda i: i.name):
        mod = importlib.import_module("vignettes_v490." + info.name)
        for n, q in enumerate(getattr(mod, "VIGNETTES", []), 1):
            out.append((info.name, n, q))
    return out


def install_clinical_challenge_vignettes_v490(data, app_mod=None):
    cid_domain = {}
    for domain, mods in data.DEEP_MODULES_V6.items():
        for m in mods:
            cid_domain[app_mod._v6_item_id(domain, m["topic"]) if app_mod else None] = (domain, m["topic"])
    bank = data.CLINICAL_CHALLENGES_V119
    existing = {q.get("id") for q in bank}
    added, rejected = [], []
    for group, n, q in _load():
        qid = "v490-%s-%d" % (group.replace("_", "-"), n)
        if qid in existing:
            continue
        ok = all(k in q for k in REQUIRED) and len(q["choices"]) == 4 and isinstance(q["answer"], int) \
            and 0 <= q["answer"] < 4 and len(q["why_wrong"]) == 4 and q["concept_id"] in cid_domain
        if not ok:
            rejected.append(qid)
            continue
        domain, topic = cid_domain[q["concept_id"]]
        row = {k: q[k] for k in REQUIRED}
        row.update({"id": qid, "domain": domain, "topic": topic, "tier": "Curated board-style",
                    "mode": MODE.get(q["focus"], "Reasoning"), "authored_v490": True})
        bank.append(row)
        existing.add(qid)
        added.append(qid)
    by_id = getattr(data, "CLINICAL_CHALLENGE_BY_ID_V119", None)
    if isinstance(by_id, dict):
        by_id.update({q["id"]: q for q in bank if q.get("id")})
    if app_mod is not None:
        for name in ("CLINICAL_CHALLENGE_BY_ID_V119",):
            target = getattr(app_mod, name, None)
            if isinstance(target, dict) and target is not by_id:
                target.update({q["id"]: q for q in bank if q.get("id")})
    result = {"added": len(added), "rejected": rejected, "bank_total": len(bank)}
    data.CLINICAL_CHALLENGE_VIGNETTES_V490 = result
    return result
