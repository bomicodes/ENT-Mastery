"""v27.4 neck-dissection carotid danger-zone commitment and rescue layer.

Adds explicit loss-of-safe-plane stop rules for carotid involvement/injury and
postoperative sentinel-bleed/carotid-blowout rescue. The layer deliberately avoids a
single mandatory ligation/reconstruction algorithm because vessel sacrifice tolerance,
oncologic benefit, endovascular options, and reconstructive resources are patient- and
center-dependent.
"""

CAROTID_DANGER_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "Sun K et al. Surgical Management Strategies for Carotid Artery Invasion by Head and Neck Cancer: Ligation Versus Reconstruction. Otolaryngol Head Neck Surg. 2024.",
    "Pace GM et al. Survival and complications after carotid resection for head and neck squamous cell carcinoma: a systematic review and pooled analysis. Head Neck. 2024.",
    "Zhu WY et al. Management of post-radiation carotid blowout syndrome in patients with head and neck cancer: A systematic review. Radiother Oncol. 2024;200:110502.",
    "Slijepcevic AA et al. Carotid Blowout Syndrome in Head and Neck Cancer Patients: Management of Patients At Risk for CBS. Laryngoscope. 2023;133:576-587.",
]

TARGETS = [{
    "slug": "neck-dissection",
    "title_terms": ("neck", "dissection"),
    "setup": [
        "Make carotid involvement a pre-incision commitment point when imaging, prior radiation/surgery, recurrent disease, or examination suggests fixation to the common or internal carotid. Define whether the operative goal is separation with preservation versus planned en-bloc arterial resection, and involve vascular/endovascular/reconstructive expertise before committing to a maneuver that may require carotid sacrifice or reconstruction. Do not discover an unplanned carotid-resection strategy only after the vessel has been entered.",
        "During dissection, distinguish a difficult but recoverable plane from loss of a safe arterial plane. If tumor or dense irradiated scar is inseparable from the carotid and continued sharp/blind dissection is progressively thinning or injuring the arterial wall, stop circumferential stripping and re-establish proximal/distal control and the oncologic/vascular plan. Planned carotid resection with reconstruction can be appropriate in highly selected patients, but simple ligation/sacrifice is not an automatic default; cerebral ischemic risk, resectability/expected oncologic benefit, collateral tolerance, available reconstruction/endovascular options, and patient goals must be integrated before irreversible division.",
        "If the carotid is injured intraoperatively, prioritize immediate controlled hemorrhage management: call for help, obtain proximal and distal vascular control when feasible, resuscitate in parallel, and convert to a deliberate repair/reconstruction/sacrifice decision with vascular/endovascular support rather than blind deep clamping or repeated instrument passes in an obscured field. Temporary pressure or packing is a bridge to control, not the definitive plan when a major carotid injury is suspected.",
    ],
    "postop": [
        "In a previously operated or irradiated neck, especially with wound breakdown, fistula, infection, recurrent tumor, or an exposed carotid, a small self-limited or recurrent 'sentinel' bleed is a carotid-blowout warning until proved otherwise. Do not dismiss it because the hemorrhage stopped. Protect the airway, obtain large-bore access/blood-product readiness, escalate urgently to head-and-neck plus neurointerventional/vascular expertise, and pursue definitive vascular evaluation/treatment according to hemodynamic stability and local capability.",
        "For active major cervical hemorrhage, activate massive-hemorrhage resuscitation, secure an airway strategy that anticipates blood/aspiration and distorted anatomy, and use focused direct pressure/packing only as temporizing control while mobilizing definitive endovascular or operative management. Avoid blind clamping/probing of an irradiated or fistulized wound. Endovascular vessel sacrifice/embolization or covered-stent reconstruction are common modern strategies; open ligation, bypass, or repair remain selected options rather than interchangeable defaults, and each carries rebleeding, infection and neurologic/stroke tradeoffs.",
    ],
    "sources": CAROTID_DANGER_SOURCES,
    "marker": "neck_dissection_carotid_danger_v274",
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


def apply_or_neck_dissection_carotid_danger_v274(registry):
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
