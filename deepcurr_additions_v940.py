"""v94.0: additions to Deep Curriculum topics (CI with middle-ear fluid, VS hearing prognosis,
oral hairy leukoplakia, Killian-Jamieson diverticulum). Data in deepcurr_additions_v940.json as
[{topic, field, text}]; each text is appended to that topic's section once."""
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_PATH = os.path.join(_HERE, "deepcurr_additions_v940.json")
# v99: textbook gap-review batches (Pasha 6e, Bluestone & Stool 5e, K.J. Lee 12e, Cummings 7e, ...)
_EXTRA = ["deepcurr_additions_v991.json", "deepcurr_additions_v992.json", "deepcurr_additions_v993.json"]


def install_deepcurr_additions_v940(data):
    with open(_PATH, encoding="utf-8") as fh:
        adds = json.load(fh)
    for name in _EXTRA:
        p = os.path.join(_HERE, name)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as fh:
                adds += json.load(fh)
    by_topic = {}
    for mods in data.DEEP_MODULES_V6.values():
        for m in mods:
            by_topic.setdefault(m.get("topic"), []).append(m)
    added, missing = 0, []
    for a in adds:
        mods = by_topic.get(a["topic"])
        if not mods:
            missing.append(a["topic"])
            continue
        for m in mods:
            v = m.get(a["field"]) or ""
            if a["text"] not in v:
                m[a["field"]] = (v.rstrip() + " " + a["text"]).strip()
                added += 1
    return {"added": added, "missing": missing}
