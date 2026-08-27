"""v23.3 total-laryngectomy OR Tomorrow planning and postoperative rescue.

Adds high-consequence perioperative decisions that are not adequately conveyed by a
generic head-and-neck profile. Operative choreography and procedure-specific anatomy
remain in the existing reviewed layers.
"""

TARGETS = [
    {
        "slug": "total-laryngectomy",
        "title_terms": ("total", "laryngectomy"),
        "setup": [
            "Before total laryngectomy, define tumor extent across the glottis, subglottis, pre-epiglottic/paraglottic spaces, hypopharynx, thyroid/cricoid framework and cervical esophagus, and review nodal disease so the planned pharyngeal resection, neck dissection, thyroid resection and reconstructive requirements are explicit before incision.",
            "Assess baseline nutrition, pulmonary reserve, swallowing/aspiration burden, prior radiation or chemoradiation and wound-healing risk; a previously irradiated or nutritionally depleted patient should prompt deliberate planning for vascularized tissue reinforcement or reconstruction rather than assuming primary pharyngeal closure will carry the same fistula risk as an untreated neck.",
            "Make the postoperative communication and airway plan explicit before surgery: counsel that the patient will be a permanent neck breather with complete separation of airway from mouth/nose, involve speech-language pathology, and decide whether primary tracheoesophageal puncture/voice prosthesis is appropriate versus delayed voice rehabilitation based on oncologic, reconstructive and healing factors.",
        ],
        "postop": [
            "After total laryngectomy, oxygenation and ventilation must occur through the neck stoma. In respiratory distress, do not rely on oral or nasal oxygenation or attempt oral endotracheal intubation; inspect/suction the stoma and ventilate or intubate the tracheal stoma directly while activating the airway team.",
            "Progressive neck erythema/swelling, salivary-appearing drain output, wound breakdown, fever, increasing pain or air/fluid around the pharyngeal closure should trigger concern for pharyngocutaneous fistula. Protect the great vessels, control contamination, maintain enteral nutrition and involve the reconstructive/oncologic team early rather than advancing oral intake through a suspected leak.",
            "Monitor the stoma for crusting, mucus plugging, stenosis and dehiscence and humidify the airway appropriately. Sentinel or major neck bleeding, especially in an irradiated/infected field or near a fistula, requires immediate hemorrhage escalation because carotid exposure or blowout can be catastrophic.",
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


def apply_or_laryngectomy_management_v233(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["laryngectomy_management_v233"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
