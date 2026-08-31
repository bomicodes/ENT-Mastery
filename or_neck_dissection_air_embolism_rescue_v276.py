"""v27.6 neck-dissection venous-air-embolism prevention and rescue layer.

Adds explicit prevention, recognition, and coordinated surgeon/anesthesia rescue choreography
for atmospheric air entrainment during open jugular/large cervical venous injury. The layer
keeps central-venous aspiration and advanced monitoring as selective adjuncts rather than
mandatory steps that delay definitive source control and hemodynamic support.
"""

AIR_EMBOLISM_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "Hybels RL. Venous air embolism in head and neck surgery. Laryngoscope. 1980;90(6 Pt 1):946-954.",
    "Rice JH et al. Large visible gas bubbles in the internal jugular vein: a common occurrence during supine radical neck surgery? J Clin Anesth. 1992;4(1):21-24.",
    "Altshuler JR, Abcejo AS. Venous Air Embolism. OpenAnesthesia. Updated March 11, 2026.",
]

TARGETS = [{
    "slug": "neck-dissection",
    "title_terms": ("neck", "dissection"),
    "setup": [
        "Treat an open internal jugular or other large noncollapsing cervical vein as an air-entry hazard as well as a bleeding problem, especially when the operative field is above the right atrium or venous pressure is low. Keep the field flooded/moist, obtain direct venous control promptly, and do not leave an open venous lumen exposed to atmosphere while attention shifts elsewhere.",
        "If venous air embolism is suspected during jugular/large-vein injury—classically a sudden unexplained fall in end-tidal CO2 with hypoxemia, hypotension, arrhythmia or cardiovascular collapse—announce it immediately and coordinate source control with anesthesia. Occlude the air-entry site and flood the field with saline while anesthesia gives 100% oxygen, stops nitrous oxide if being used, and supports preload/right-heart output and blood pressure. Do not let repeated blind venous clamping enlarge the injury while trying to stop air entry.",
        "After initial source control, use monitoring and rescue adjuncts according to severity and available access. Precordial Doppler or echocardiography can detect intravascular air in selected high-risk/unstable cases; aspiration through a suitably positioned central venous catheter may be attempted when immediately available but should not delay closure of the venous source, oxygenation, resuscitation, or CPR when required. Remember that paradoxical systemic embolization can occur through intracardiac or transpulmonary passage, so new focal neurologic or coronary findings after a significant event require urgent evaluation.",
    ],
    "postop": [
        "After a clinically significant venous air embolism, continue cardiopulmonary and neurologic surveillance after stabilization rather than assuming that repair of the neck vein ends the event. Escalate persistent hypoxemia, right-heart strain/hemodynamic instability, chest symptoms, altered mental status, or focal neurologic deficits for critical-care/anesthesia evaluation and appropriate echocardiographic or cross-sectional assessment for end-organ injury.",
    ],
    "sources": AIR_EMBOLISM_SOURCES,
    "marker": "neck_dissection_air_embolism_rescue_v276",
}]


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
    out = list(values or []); changed = False
    for text in reversed(additions or []):
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text); changed = True
    return out, changed


def _append_unique(values, additions):
    out = list(values or []); known = {str(x).strip().lower() for x in out}; changed = False
    for text in additions or []:
        key = str(text).strip().lower()
        if key and key not in known:
            out.append(text); known.add(key); changed = True
    return out, changed


def apply_or_neck_dissection_air_embolism_rescue_v276(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"]); continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        op["sources"], c3 = _append_unique(op.get("sources"), target["sources"])
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2 or c3: changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
