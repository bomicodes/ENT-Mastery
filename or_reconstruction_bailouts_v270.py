"""v27.0 chief-level free-flap reconstruction commitment and bailout layer.

Adds intraoperative recipient-vessel and repeated-thrombosis decisions to the live
OR Tomorrow reconstruction cases without replacing the established planning or
postoperative flap-rescue content. The v27.1 airway bailout layer is chained through
this tail so both remain part of the production mutation path.
"""

from or_airway_bailouts_v271 import apply_or_airway_bailouts_v271

TARGETS = [
    {
        "slug": "free-flap-basics",
        "title_terms": ("free", "flap"),
        "setup": [
            "Make recipient-vessel quality and pedicle geometry a commitment point before anastomosis. If the planned artery or vein has poor flow, radiation/fibrotic injury, intimal damage, inadequate caliber, or would create tension, kinking, twist, or compression, do not accept a technically completed but physiologically unsound anastomosis simply to preserve the original plan. Trim back to healthy vessel when feasible and choose a better ipsilateral recipient, expose an alternate recipient system, or cross the neck when that provides more reliable inflow/outflow.",
            "Use interposition/vein grafting selectively when a dependable direct recipient-vessel anastomosis cannot be achieved because of reach or vessel depletion; it is a legitimate reconstructive tool, not a mandatory default. The added conduit and anastomoses create additional failure points, so first ask whether alternate recipient-vessel exposure, pedicle routing, or a different reconstructive plan can provide a shorter, healthier, tension-free circuit.",
        ],
        "postop": [],
    },
    {
        "slug": "free-flap-takeback",
        "title_terms": ("free", "flap", "takeback"),
        "setup": [
            "At takeback, recurrent thrombosis should trigger a cause-directed reconstruction rather than serially recreating the same anastomosis. Fully expose the pedicle and identify correctable mechanical causes such as hematoma/compression, kink, twist, tension, poor vessel geometry or a damaged recipient segment; revise back to healthy inflow/outflow and change recipient vessels when the original target remains hostile. Re-establishing flow without correcting the cause is not definitive salvage.",
            "If thrombosis recurs despite technically sound revision, reassess the entire system—recipient inflow and venous outflow, pedicle geometry, flap microcirculation and relevant systemic/coagulation factors—and decide whether further revision still offers a credible salvage path. Avoid an arbitrary fixed number of attempts, but do not allow repeated low-yield revisions to consume ischemia time when the flap is clearly unsalvageable; transition to a second free flap, regional/pedicled flap, or other defect-appropriate reconstruction when that is the safer durable endpoint.",
        ],
        "postop": [],
    },
]


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in target["title_terms"]):
            return slug, op
    return None, None


def _prepend_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_reconstruction_bailouts_v270(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["reconstruction_bailouts_v270"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    v271 = apply_or_airway_bailouts_v271(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v271": v271}
