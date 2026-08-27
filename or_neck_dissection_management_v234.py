"""v23.4 neck-dissection OR Tomorrow planning and postoperative rescue.

Adds procedure-specific perioperative decisions and postoperative failure-mode teaching
without replacing the reviewed operative sequence or anatomy layers.
"""

TARGETS = [
    {
        "slug": "neck-dissection",
        "title_terms": ("neck", "dissection"),
        "setup": [
            "Before neck dissection, define the exact nodal levels and structures intended for preservation or sacrifice from the primary site, nodal burden and imaging rather than treating every lateral neck as the same operation. Document baseline shoulder function and lower cranial-nerve deficits when disease approaches CN XI, hypoglossal/vagus structures, carotid sheath or skull base, and anticipate reconstructive/vascular help when major-vessel involvement is suspected.",
            "Review prior neck surgery, radiation, central venous access and the side/extent of low-neck disease. A left level IV dissection, bulky disease near the venous angle or reoperative/radiated low neck should heighten the plan for thoracic-duct identification/control and postoperative chyle surveillance; bilateral IJV sacrifice or compromise requires deliberate cerebral-venous planning rather than routine bilateral completion.",
        ],
        "postop": [
            "After neck dissection, inspect drain character as well as volume. Milky output that increases with enteral fat intake, especially after left level IV work, should trigger evaluation for chyle leak: confirm the clinical pattern, quantify output, institute an appropriate low-fat/medium-chain-triglyceride or enteral-modification strategy with nutrition support, and escalate persistent high-output or clinically significant leaks for procedural or operative control rather than allowing prolonged nutritional and fluid losses.",
            "Document postoperative shoulder elevation/abduction and trapezius function even when CN XI was anatomically preserved, because traction and devascularization can produce meaningful shoulder dysfunction. Early recognition should prompt physical therapy and focused nerve examination; new tongue weakness, dysphonia, aspiration, diaphragmatic dysfunction or upper-extremity neurologic change should likewise be localized to hypoglossal, vagal, phrenic or brachial-plexus injury rather than attributed generically to postoperative pain.",
            "An expanding neck hematoma, airway compromise, brisk drain/wound hemorrhage or sentinel bleeding requires immediate assessment and operative hemorrhage control when indicated. In an infected or previously irradiated neck, wound breakdown with exposed carotid tissue or sentinel bleeding should be treated as impending carotid blowout until proven otherwise.",
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


def apply_or_neck_dissection_management_v234(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["neck_dissection_management_v234"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
