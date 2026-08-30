"""v27.1 chief-level airway exposure/ventilation bailout layer for OR Tomorrow.

Adds explicit stop/change-strategy decisions for shared-airway cases when repeated
instrumentation, worsening oxygenation, or inadequate exposure makes the original
endoscopic plan unsafe. Existing operative sequence and rescue content remains
authoritative and is only supplemented.

The pediatric bronchoscopy additions were cross-checked against the connected
Cummings 7th ed., K.J. Lee 12th ed., and Pasha 6th ed. references, then reconciled
with current pediatric bronchoscopy/foreign-body consensus and review literature.
"""

PEDIATRIC_AIRWAY_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha: Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "Society for Pediatric Pneumology: Pediatric Airway Endoscopy recommendations (2021)",
    "ERS statement: Interventional Bronchoscopy in Children (2017)",
    "Brown MC, Powers A, Trope M, Jacobs I. Airway Foreign Bodies. Otolaryngol Clin North Am. 2026.",
]

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
    {
        "slug": "airway-fb",
        "title_terms": ("airway", "foreign", "body"),
        "setup": [
            "During pediatric airway foreign-body extraction, oxygenation outranks completing the retrieval attempt. If saturation falls, ventilation becomes ineffective, or a previously bronchial object migrates into the trachea/carina and creates critical obstruction, stop traction and keep the object under direct endoscopic control. Withdraw the forceps or bronchoscope enough to restore a ventilating lumen as appropriate, suction obstructing secretions/blood, and re-establish ventilation with anesthesia before another extraction attempt. In a true central asphyxiating obstruction, deliberate movement of the object into one mainstem bronchus can be a rescue maneuver to permit ventilation of the opposite lung, but it should be performed under direct visualization as a temporizing airway maneuver—not as blind distal displacement.",
            "If a foreign body has been mobilized but cannot pass safely through the glottis/subglottis because of its size, shape, sharp edge, orientation, or surrounding edema, do not repeatedly drag it against the pediatric larynx. Reassess the grasp and orientation, change the retrieval instrument when useful, and use a controlled bronchoscope-object withdrawal strategy when feasible. A large or sharp object that still cannot traverse the upper airway may require a planned tracheotomy/open extraction under endoscopic control; rare conversion is safer than repeated traumatic attempts that convert partial obstruction into a lost airway.",
            "Treat fragmentation of friable organic material as a new search problem, not proof of completion. Remove visible fragments under direct vision, clear secretions, and reinspect the trachea, both main bronchi and accessible distal branches after extraction when physiology permits. Persistent focal obstruction, an unexplained ventilation problem, or an incomplete second-look should lower the threshold to continue controlled endoscopic assessment for retained fragments rather than ending the case because the first visible piece was removed.",
        ],
        "sources": PEDIATRIC_AIRWAY_SOURCES,
    },
    {
        "slug": "direct-laryngoscopy-bronchoscopy",
        "title_terms": ("direct", "laryngoscopy", "bronchoscopy"),
        "setup": [
            "During pediatric diagnostic direct laryngoscopy/bronchoscopy, worsening oxygenation or loss of effective ventilation is a stop point for measurement and inspection. Withdraw obstructing instrumentation as needed, re-establish oxygenation with anesthesia, and only resume after deciding whether spontaneous ventilation, controlled ventilation, a smaller instrument, or a secured airway better fits the physiology. Repeated instrumentation through an increasingly edematous airway can turn a diagnostic examination into an airway emergency.",
            "Do not obtain a stenosis size or distal-airway view by forcing an endotracheal tube, bronchoscope, or dilator through resistance. Document the best atraumatic measurement that can be obtained; if the lesion cannot be crossed safely, the inability to traverse it is itself an operative finding and should trigger a controlled airway/reconstructive plan rather than escalating force merely to complete the examination.",
        ],
        "sources": PEDIATRIC_AIRWAY_SOURCES,
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


def _append_unique(values, additions):
    out = list(values or [])
    changed = False
    known = {str(x).strip().lower() for x in out}
    for text in additions:
        key = str(text).strip().lower()
        if key and key not in known:
            out.append(text)
            known.add(key)
            changed = True
    return out, changed


def apply_or_airway_bailouts_v271(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["sources"], c2 = _append_unique(op.get("sources"), target.get("sources", []))
        op["airway_bailouts_v271"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
