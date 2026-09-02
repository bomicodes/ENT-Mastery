"""v28.8 shared-airway fire prevention and rescue for OR Tomorrow.

Extends existing shared-airway stop-point teaching into an executable airway-fire
response for microlaryngoscopy and RRP/laser laryngeal surgery. Foundational airway
and operative principles remain grounded in Cummings 7e, K.J. Lee 12e, and Pasha 6e;
current fire choreography follows ASA/APSF guidance and contemporary airway-fire
literature.
"""

AIRWAY_FIRE_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha: Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "American Society of Anesthesiologists. Practice Advisory for the Prevention and Management of Operating Room Fires.",
    "Anesthesia Patient Safety Foundation. Surgical Fire Prevention and Management guidance.",
    "Beaulieu F, Hobday S, Duffy CC. Fire Risks in Airway Procedures: A Clinical Review of Proactive Prevention and Emergency Response. Anesthesiol Clin. 2026;44(1):115-124.",
    "Pasick LJ, Tong JY, Benito DA, Sargi Z, Anis MM. Airway fires in otolaryngologic surgery: A database review. Am J Otolaryngol. 2023;44(6):104003.",
]

TARGETS = [
    {
        "slug": "microflap",
        "title_terms": ("microflap",),
    },
    {
        "slug": "rrp-debridement",
        "title_terms": ("rrp",),
    },
]

PREVENTION = (
    "For laser or other ignition-capable shared-airway work, explicitly brief the fire plan with anesthesia before energy is activated: identify the oxidizer, ignition source and fuel; use the lowest oxygen concentration compatible with safe oxygenation; avoid nitrous oxide; protect exposed combustible material and the cuff/field with the procedure-appropriate laser-resistant airway strategy and wet pledgets when used. A laser-resistant tube lowers risk but is not fire-proof. If physiology requires a higher oxidizer concentration, stop energy delivery and allow the airway/fire setup to become safe again before resuming rather than firing through an oxygen-enriched field."
)

RESCUE = (
    "If an airway fire or sustained flash occurs, announce the fire and immediately stop laser/energy delivery. In parallel, anesthesia stops/disconnects oxidizer flow and the breathing circuit as appropriate; promptly remove the burning endotracheal tube and other burning material from the airway when present, and extinguish residual flame in the airway with saline or water. Do not continue the procedure or pause for diagnostic imaging while combustion is ongoing. Once the fire is extinguished, re-establish ventilation, initially avoiding supplemental oxygen/nitrous oxide if the patient's physiology permits and then titrating oxygen to clinical need."
)

POST_FIRE = (
    "After extinguishment, inspect the removed tube for missing fragments and perform controlled airway reassessment—typically bronchoscopy when an airway fire occurred—to look for retained tube/foreign material, char, edema and distal thermal injury and to remove debris. Reoxygenation difficulty, progressive edema, major mucosal injury or an unsafe upper airway changes the case from elective lesion treatment to airway rescue: secure a controlled airway using the safest available endoscopic/intubation strategy or surgical airway when required, stop further elective energy treatment, and escalate postoperative monitoring/critical-care support according to the extent of inhalational or thermal injury."
)


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
        marker = text[:80].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def _append_unique(values, additions):
    out = list(values or [])
    known = {str(x).strip().lower() for x in out}
    changed = False
    for text in additions:
        key = str(text).strip().lower()
        if key and key not in known:
            out.append(text)
            known.add(key)
            changed = True
    return out, changed


def apply_or_airway_fire_rescue_v288(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), [PREVENTION])
        op["steps"], c2 = _prepend_unique(op.get("steps"), [RESCUE])
        op["postop"], c3 = _prepend_unique(op.get("postop"), [POST_FIRE])
        op["sources"], c4 = _append_unique(op.get("sources"), AIRWAY_FIRE_SOURCES)
        op["airway_fire_rescue_v288"] = True
        resolved.append(slug)
        if c1 or c2 or c3 or c4:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
