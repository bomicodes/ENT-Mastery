"""v27.1 chief-level airway exposure/ventilation bailout layer for OR Tomorrow.

Adds explicit stop/change-strategy decisions for shared-airway cases when repeated
instrumentation, worsening oxygenation, or inadequate exposure makes the original
endoscopic plan unsafe. Existing operative sequence and rescue content remains
authoritative and is only supplemented.
"""

TARGETS = [
    {
        "slug": "airway-dilation",
        "title_terms": ("airway", "dilation"),
        "setup": [
            "Make loss of ventilation or inability to maintain a controlled view a stop point during endoscopic airway dilation. If oxygenation/ventilation deteriorates, withdraw obstructing instruments as needed, re-establish oxygenation with the preplanned shared-airway strategy, and reassess exposure before further dilation. Repeated blind passes through a poorly visualized stenosis increase the risk of false passage, transmural tear, bleeding and loss of the airway; when safe endoscopic control cannot be restored, change the airway strategy rather than persisting with the planned dilation.",
            "If the stenosis will not accept the planned instrument or dilation despite adequate visualization, reassess the lesion mechanism and the distal airway before escalating force. Dense mature scar, framework collapse, unexpected complete/near-complete obstruction or anatomy that cannot be traversed safely may require a smaller controlled instrument, staged treatment, open reconstruction, or a surgical airway instead of increasingly aggressive endoscopic dilation.",
        ],
    },
    {
        "slug": "microflap",
        "title_terms": ("microflap",),
        "setup": [
            "Do not trade mucosal or airway injury for exposure during suspension microlaryngoscopy. If an adequate view cannot be obtained after deliberate repositioning, laryngoscope selection and external manipulation, stop repeated traumatic suspension attempts and change the plan; deferring or using an alternate approach is preferable to dental, tongue, pharyngeal or laryngeal injury simply to complete an elective microflap.",
            "In a shared-airway case, worsening oxygenation, ventilation difficulty, airway fire concern or loss of a stable endoscopic field takes priority over lesion removal. Stop energy delivery and instrumentation, re-establish a controlled airway/ventilation strategy with anesthesia, then decide whether it is safe to resume rather than continuing through physiologic instability.",
        ],
    },
    {
        "slug": "rrp-debridement",
        "title_terms": ("rrp",),
        "setup": [
            "For bulky obstructive papilloma, preserve a ventilation corridor while debulking rather than chasing complete disease clearance through a progressively unstable airway. If ventilation worsens or the endoscopic field becomes unsafe, stop treatment, re-establish oxygenation and airway control, and accept staged disease reduction when necessary; aggressive circumferential mucosal injury or blind distal instrumentation can turn a controllable papilloma burden into edema, stenosis or a lost airway.",
            "When laser or other ignition-capable energy is being used, any loss of fire-safety conditions is an immediate stop point. Cease energy delivery, restore the agreed airway/fire precautions and only resume when the shared-airway setup is controlled; completion of papilloma treatment is never more important than preventing an airway fire.",
        ],
    },
    {
        "slug": "tracheal-resection",
        "title_terms": ("tracheal", "resection"),
        "setup": [
            "At airway transection, failure of cross-field ventilation or inability to control the distal airway is a physiologic bailout, not a reason to keep dissecting through worsening gas exchange. Pause resection, re-establish oxygenation/ventilation using the preplanned rescue option, and only resume once the distal airway and tube position are controlled. Repeated uncontrolled tube manipulation across the operative field risks mucosal injury, fire/contamination problems and loss of a previously accessible distal airway.",
            "Before removing additional tracheal length, repeatedly reassess whether the remaining ends can meet with a well-perfused, tension-minimized anastomosis. If the planned resection would leave excessive tension or devascularized margins despite appropriate release maneuvers, change the reconstructive plan or limit resection rather than forcing a high-risk anastomosis merely to match the original resection target.",
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
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_airway_bailouts_v271(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], did_change = _prepend_unique(op.get("setup"), target["setup"])
        op["airway_bailouts_v271"] = True
        resolved.append(slug)
        if did_change:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
