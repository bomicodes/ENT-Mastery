"""v23.9 septoplasty OR Tomorrow planning and postoperative rescue.

Adds procedure-specific decision-making and high-consequence postoperative recognition
for septoplasty. Operative choreography and anatomy remain in existing reviewed layers.
"""

TARGETS = [
    {
        "slug": "septoplasty",
        "title_terms": ("septoplasty",),
        "setup": [
            "Before septoplasty, define the functional deformity rather than treating a deviated septum on imaging alone: document the side and level of obstruction, caudal versus dorsal versus bony deviation, internal/external nasal-valve contribution, turbinate hypertrophy, prior trauma or surgery, and whether structural support or concurrent functional rhinoplasty may be required. A septoplasty that corrects the septal component but ignores major valve collapse may not address the patient's obstruction.",
            "Review bleeding risk, intranasal drug exposure, mucosal health and prior septal surgery, then plan cartilage preservation deliberately. Maintain an adequate dorsal and caudal L-strut and recognize that aggressive resection near the keystone region or caudal septal attachment can trade obstruction for postoperative instability, saddle deformity or tip-support problems.",
        ],
        "postop": [
            "After septoplasty, disproportionate pain/pressure, progressive bilateral obstruction, fever or a boggy fluctuant septal swelling should trigger urgent intranasal examination for septal hematoma or abscess; prompt drainage and treatment are important because prolonged cartilage separation from its mucoperichondrium risks necrosis, perforation and saddle-nose deformity.",
            "New persistent clear unilateral rhinorrhea, severe headache, visual symptoms, brisk uncontrolled epistaxis or rapidly progressive facial/orbital swelling is not routine postoperative congestion. Escalate according to the finding rather than repeatedly repacking or observing; later persistent obstruction should be reassessed for residual caudal/dorsal deviation, valve collapse, synechiae, perforation or turbinate disease rather than assuming all failure is recurrent septal deviation.",
        ],
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
        marker = text[:64].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_septoplasty_management_v239(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["septoplasty_management_v239"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
