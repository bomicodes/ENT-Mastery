"""v90.0: fill operative-step gaps from the Iowa Head and Neck Protocols.

Cards whose steps were never built from a surgical atlas (facial plastics, trauma, laryngology,
rhinology, pediatrics, sleep), and atlas cards with known gaps (reoperative thyroid/parathyroid,
flap salvage, fistula repair, intact-canal-wall mastoidectomy, prosthesis placement, transmastoid
tegmen repair), were filled in our own words from the University of Iowa protocols
(iowaprotocols.medicine.uiowa.edu). Data: or_steps_iowa_v900.json, as
{slug: {mode: replace|edit, steps | edits, protocol_urls, notes}}. Installed after the v86 card
fixes so it builds on the reviewed text.
"""
import json
import os

_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "or_steps_iowa_v900.json")
LABEL = "the Iowa Head and Neck Protocols (University of Iowa)"
_REVIEW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "or_steps_iowa_v900_review.json")


def _apply_review(steps, fixes):
    """Independent clinical review edits, indexed against the post-Iowa step list."""
    steps = [list(s) for s in steps]
    edits = [f for f in fixes if isinstance(f.get("index"), int)]
    inserts = [f for f in fixes if isinstance(f.get("index"), str) and f["index"].startswith("insert:")]
    appends = [f for f in fixes if f.get("index") == "append"]
    for f in sorted(edits, key=lambda f: -f["index"]):
        i = f["index"]
        if 0 <= i < len(steps):
            if f.get("new") == "DELETE":
                steps[i] = None
            else:
                steps[i] = list(f["new"])
    for f in sorted(inserts, key=lambda f: -int(f["index"].split(":")[1])):
        i = int(f["index"].split(":")[1])
        steps.insert(max(0, min(len(steps), i)), list(f["new"]))
    for f in appends:
        steps.append(list(f["new"]))
    return [s for s in steps if s is not None]


def install_or_steps_iowa_v900(data):
    registry = data.OR_PREP_REGISTRY
    try:
        with open(_PATH, encoding="utf-8") as fh:
            table = json.load(fh)
    except FileNotFoundError:
        table = {}
    review = {}
    try:
        with open(_REVIEW, encoding="utf-8") as fh:
            for f in json.load(fh):
                review.setdefault(f["slug"], []).append(f)
    except FileNotFoundError:
        pass
    replaced, edited, skipped = [], [], []
    for slug, entry in table.items():
        card = registry.get(slug)
        if not card:
            skipped.append(slug)
            continue
        current = card.get("steps_v840") or [[s, ""] for s in card.get("steps", [])]
        if entry.get("mode") == "replace" and entry.get("steps"):
            new = [list(s) for s in entry["steps"]]
            card["steps_source_v840"] = LABEL[0].upper() + LABEL[1:]
            replaced.append(slug)
        else:
            new = [list(s) for s in current]
            reps = [e for e in entry.get("edits", []) if e.get("op") == "replace"]
            ins = [e for e in entry.get("edits", []) if e.get("op") == "insert_after"]
            for e in reps:
                i = int(e["index"])
                if 0 <= i < len(new):
                    new[i] = list(e["step"])
            for e in sorted(ins, key=lambda e: -int(e["index"])):
                i = int(e["index"])
                new.insert(max(0, min(len(new), i + 1)), list(e["step"]))
            base = card.get("steps_source_v840")
            card["steps_source_v840"] = f"{base}, with gaps filled from {LABEL}" if base else LABEL[0].upper() + LABEL[1:]
            edited.append(slug)
        new = _apply_review(new, review.get(slug, []))
        card["steps_v840"] = new
        card["steps"] = [f"{t}. {d}" if d else t for t, d in new]
        urls = entry.get("protocol_urls") or []
        if urls:
            card["iowa_links_v900"] = urls[:4]
        src = card.get("source_basis")
        if isinstance(src, list) and "Iowa Head and Neck Protocols" not in src:
            src.append("Iowa Head and Neck Protocols")
    return {"replaced": replaced, "edited": edited, "skipped": skipped}
