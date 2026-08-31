"""v27.2 source-grounded neck-dissection chyle prevention and rescue for OR Tomorrow.

Adds an executable postoperative escalation strategy without imposing a brittle single
volume cutoff. The connected Cummings/K.J. Lee/Pasha references were reconciled with
recent systematic/review literature showing heterogeneous definitions and limited
high-level evidence for one universal chyle-leak algorithm.
"""

NECK_CHYLE_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "Smith R et al. Nutritional management of chyle leak after head and neck surgery: systematic review and proposed protocol. Oral Maxillofac Surg. 2024;28:51-62.",
    "Ganesan A et al. Chyle leak after head and neck surgeries: comprehensive review of diagnosis and management strategies. J Korean Assoc Oral Maxillofac Surg. 2024;50:3-12.",
    "Picton C et al. Improving the management of cervical chyle leak following neck dissection. J Laryngol Otol. 2025.",
    "Minimally invasive lymphatic embolization series after thyroidectomy/cervical lymph-node dissection. 2024.",
]

TARGETS = [
    {
        "slug": "neck-dissection",
        "title_terms": ("neck", "dissection"),
        "setup": [
            "At completion of low-neck dissection, deliberately inspect the lymphatic danger zone before closure—especially the left level IV/venous-angle region, while remembering that right-sided cervical lymphatic leaks also occur. If clear or milky lymphatic flow is seen, obtain direct control with clipping, ligation or another secure repair rather than assuming a drain will make the problem harmless; increase intrathoracic pressure/Valsalva when appropriate and re-inspect the repair before closing. Persistent uncontrolled flow should trigger better exposure and definitive control rather than repeated blind cautery or closure over an active leak.",
        ],
        "postop": [
            "After neck dissection, a drain that becomes milky or increases substantially after enteral fat exposure should raise concern for chyle leak, but appearance alone is not mandatory—trend output and correlate it with feeding, wound findings and patient physiology. When the diagnosis is uncertain, drain triglyceride/chylomicron testing can support it. Quantify ongoing losses because sustained chyle loss can produce volume depletion, electrolyte abnormalities, protein/calorie malnutrition, lymphocyte/immunologic depletion, delayed wound healing and free-flap or great-vessel exposure risk.",
            "Treat a cervical chyle leak by trajectory and clinical consequence rather than a single memorized milliliter cutoff. Protect the wound and drain appropriately, reduce long-chain-fat delivery with a low-fat/MCT or other enteral strategy when suitable, replace fluid/electrolyte/protein losses, and involve nutrition early. Failure to improve, persistently large losses, nutritional/metabolic deterioration, wound or flap compromise, or a leak unlikely to close conservatively should prompt earlier definitive escalation rather than prolonged observation.",
            "Definitive escalation is anatomy- and expertise-dependent: options include directed cervical re-exploration/ligation or muscle coverage and image-guided lymphangiography with selective lymphatic/thoracic-duct embolization; some centers use transthoracic thoracic-duct ligation for selected refractory leaks. Choose the least morbid strategy likely to stop the leak promptly, and do not delay escalation while the patient becomes progressively depleted merely because an arbitrary output threshold has not been crossed.",
        ],
        "marker": "neck_dissection_chyle_rescue_v272",
        "sources": NECK_CHYLE_SOURCES,
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
    known = {str(x).strip().lower() for x in out}
    changed = False
    for text in additions or []:
        key = str(text).strip().lower()
        if key and key not in known:
            out.append(text)
            known.add(key)
            changed = True
    return out, changed


def apply_or_neck_dissection_rescue_v272(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["sources"], c3 = _append_unique(op.get("sources"), target.get("sources", []))
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2 or c3:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
