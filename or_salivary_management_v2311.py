"""v23.11 salivary OR Tomorrow planning and postoperative rescue.

Adds procedure-specific perioperative decisions and postoperative failure recognition
for parotid, submandibular-gland, and sialendoscopic surgery. Operative choreography
and anatomy remain in the existing reviewed layers.
"""

TARGETS = [
    {
        "slug": "parotidectomy",
        "title_terms": ("parotidectomy",),
        "exclude_terms": ("total",),
        "setup": [
            "Before parotidectomy, document facial-nerve function by major branch territory rather than simply recording 'intact,' and correlate the lesion with superficial/deep-lobe extent, stylomastoid-foramen/skull-base proximity, skin fixation and nodal disease. If malignancy or nerve involvement is plausible, define whether nerve sacrifice, immediate reconstruction, neck dissection or soft-tissue reconstruction may be required before incision.",
        ],
        "postop": [
            "Immediately after parotid surgery, document forehead elevation, eye closure, midface excursion and lower-lip movement. New complete or progressive facial weakness, inability to protect the cornea, an expanding preauricular/neck hematoma or rapidly increasing pain/swelling requires prompt focused assessment rather than routine observation; institute eye protection when closure is impaired while the cause is evaluated.",
            "A soft or fluctuant postoperative collection that enlarges with meals suggests sialocele or salivary fistula rather than simple seroma. Confirm the clinical diagnosis, protect the wound/skin and use stepwise salivary-leak management according to persistence and severity; later gustatory sweating/flushing is consistent with Frey syndrome and should be treated as a distinct delayed complication rather than recurrent infection.",
        ],
    },
    {
        "slug": "parotid-total",
        "title_terms": ("total", "parotid"),
        "exclude_terms": (),
        "setup": [
            "For total parotidectomy, review whether deep-lobe/parapharyngeal extension, skull-base proximity or known facial-nerve invasion changes exposure and reconstruction. If a branch or trunk may require sacrifice, identify the intended proximal/distal nerve strategy and available graft or nerve-transfer options before resection rather than deciding only after the nerve has been divided.",
        ],
        "postop": [
            "After total parotidectomy, perform and record a branch-level facial examination and distinguish expected weakness after planned nerve sacrifice from an unexpected new deficit in a preserved nerve. Inability to close the eye requires immediate corneal-protection measures; progressive swelling, hematoma, wound compromise or salivary leakage warrants early reassessment of the operative bed and reconstruction.",
        ],
    },
    {
        "slug": "submandibular-gland",
        "title_terms": ("submandibular", "gland"),
        "exclude_terms": (),
        "setup": [
            "Before submandibular-gland excision, document lower-lip symmetry, tongue protrusion and tongue sensation when disease is extensive or posterior, and review whether the indication is chronic obstruction/inflammation versus neoplasm. A suspected malignancy should trigger oncologic margin and neck-management planning rather than being approached as routine inflammatory gland excision.",
        ],
        "postop": [
            "After submandibular-gland surgery, examine marginal-mandibular function, tongue protrusion and ipsilateral tongue sensation. New tongue deviation suggests hypoglossal dysfunction, numbness/taste change suggests lingual-nerve injury, and lower-lip asymmetry localizes to the marginal-mandibular branch; documenting the pattern is more useful than labeling all deficits 'facial weakness.'",
            "Progressive upper-neck/floor-of-mouth swelling, dysphagia, respiratory symptoms or an expanding hematoma requires urgent airway and wound assessment. Persistent salivary drainage or meal-related swelling should prompt evaluation for ductal/oral communication or residual obstructive disease rather than repeated empiric antibiotics alone.",
        ],
    },
    {
        "slug": "sialendoscopy",
        "title_terms": ("sialendosc",),
        "exclude_terms": (),
        "setup": [
            "Before sialendoscopy, map stone number, size and position, ductal stenosis and whether disease is intraductal, hilar or intraparenchymal. Define an endoscopic-only versus combined transoral/open strategy in advance for large impacted or posterior submandibular stones so repeated traumatic instrumentation is not used as a substitute for an appropriate combined approach.",
        ],
        "postop": [
            "After sialendoscopy, rapidly increasing floor-of-mouth or gland swelling, fever, severe pain, dysphagia, respiratory symptoms or new tongue numbness requires assessment for duct perforation, extravasation, infection, hematoma or lingual-nerve injury rather than being dismissed as expected irrigation edema.",
            "For a ductotomy, stent or treated stenosis, document the planned stent/oral-care pathway and reassess recurrent meal-related swelling for restenosis, residual stone or recurrent obstructive disease. Persistent symptoms should trigger anatomic re-evaluation rather than indefinite repeat dilation without identifying the recurrent obstruction.",
        ],
    },
]


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if not all(term in hay for term in target["title_terms"]):
            continue
        if any(term in hay for term in target.get("exclude_terms", ())):
            continue
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


def apply_or_salivary_management_v2311(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["salivary_management_v2311"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
