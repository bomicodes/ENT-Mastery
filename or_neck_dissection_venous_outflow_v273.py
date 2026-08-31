"""v27.3 neck-dissection venous-outflow commitment and rescue layer.

Adds explicit last-patent-IJV planning, bilateral venous-outflow protection, and
postoperative escalation for acute head/neck venous hypertension. This is deliberately
conservative because contemporary literature supports the physiologic risk but does not
provide a single universal society algorithm.
"""

NECK_VENOUS_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "Quraishi HA et al. Internal jugular vein thrombosis after functional and selective neck dissection. Arch Otolaryngol Head Neck Surg. 1997;123:969-973.",
    "Prim MP et al. Patency and flow of the internal jugular vein after functional neck dissection. Laryngoscope. 2000;110:47-50.",
    "Patency and caliber of the internal jugular vein after neck dissection. 2003.",
]

TARGETS = [{
    "slug": "neck-dissection",
    "title_terms": ("neck", "dissection"),
    "setup": [
        "Before sacrificing or extensively skeletonizing an internal jugular vein, determine whether the contralateral jugular outflow is patent and whether this vein is effectively the last dependable major cervical venous pathway. Bilateral simultaneous IJV loss can produce severe head/neck venous hypertension and cerebral edema; when oncologically feasible, preserve at least one functional major jugular pathway, stage bilateral radical dissections, or plan venous reconstruction rather than treating the second IJV as expendable by default.",
        "During bilateral or vessel-depleted neck surgery, protect the preserved IJV from traction, thermal injury, desiccation, compression, pedicle kinking and closure-related narrowing. If the only reliable jugular pathway is injured or thromboses intraoperatively, restore dependable venous outflow when technically feasible rather than accepting bilateral obstruction without an explicit rescue plan.",
    ],
    "postop": [
        "After bilateral neck surgery or sacrifice of one IJV, rapidly progressive facial/neck edema, tense venous congestion, chemosis, severe headache, altered mental status, airway swelling or unexplained neurologic decline should trigger concern for critical remaining-jugular obstruction or thrombosis rather than being dismissed as routine postoperative edema. Reassess the airway immediately and obtain urgent vascular imaging/operative evaluation according to stability and local expertise.",
        "If the patient depends on a single preserved IJV, new thrombosis or compression is a time-sensitive outflow problem. Look for reversible causes such as hematoma, tight closure/dressing, pedicle compression or technical narrowing; escalate early to decompression, thrombectomy/revision, or venous reconstruction when indicated rather than waiting for progressive venous hypertension to declare itself fully.",
    ],
    "sources": NECK_VENOUS_SOURCES,
    "marker": "neck_dissection_venous_outflow_v273",
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


def apply_or_neck_dissection_venous_outflow_v273(registry):
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
