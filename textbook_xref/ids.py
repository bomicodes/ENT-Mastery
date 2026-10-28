"""Map review-bundle item IDs (T-<domain>-<n>, CC-<domain>-<n>.<k>) back to topics and source files.
Mirrors the numbering in build_review_bundle.py."""
import importlib, pkgutil
import pathophys_v470, cc_v471

ORDER = ["otology", "rhinology", "head_neck", "thyroid", "pediatric", "laryngology",
         "facial_plastics", "sleep", "general_ent"]

def _dom(name):
    return next(k for k in ORDER if name.startswith(k))

def topic_index():
    topics = {k: {} for k in ORDER}
    for info in pkgutil.iter_modules(pathophys_v470.__path__):
        mod = importlib.import_module("pathophys_v470." + info.name)
        for t in mod.CONTENT:
            topics[_dom(info.name)][t] = "pathophys_v470/%s.py" % info.name
    idx = {}
    for d in ORDER:
        for i, t in enumerate(sorted(topics[d]), 1):
            idx["T-%s-%d" % (d, i)] = (d, t, topics[d][t])
    checks = {}
    for info in sorted(pkgutil.iter_modules(cc_v471.__path__), key=lambda i: i.name):
        mod = importlib.import_module("cc_v471." + info.name)
        for row in mod.CHECKS:
            checks.setdefault((_dom(info.name), row[0]), []).append("cc_v471/%s.py" % info.name)
    known = set()
    for tid, (d, t, _) in list(idx.items()):
        known.add((d, t))
        for k, f in enumerate(checks.get((d, t), []), 1):
            idx["CC-%s.%d" % (tid[2:], k)] = (d, t, f)
    # Checks filed under legacy topic names are numbered globally in the bundle.
    k = 0
    for (d, t), files in checks.items():
        if (d, t) in known:
            continue
        for f in files:
            k += 1
            idx["CC-%s-legacy.%d" % (d, k)] = (d, t, f)
    return idx
