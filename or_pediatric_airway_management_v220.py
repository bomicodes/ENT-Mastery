"""v22.0 focused pediatric-airway perioperative management for OR Tomorrow.

Adds high-confidence postoperative and planning details that materially affect airway
safety after supraglottoplasty, laryngotracheal reconstruction, and laryngeal cleft
repair. Operative choreography remains in the existing sequence layers.
"""

TARGETS = [
    {
        "slug": "supraglottoplasty",
        "title_terms": ("supraglottoplasty",),
        "setup": "Match postoperative disposition to physiologic risk rather than the procedure name alone: severe OSA/hypoxemia, neurologic or cardiopulmonary disease, significant aspiration/feeding dysfunction, very young age, difficult airway, or extensive supraglottic work should lower the threshold for monitored or ICU-level observation.",
        "postop": "After supraglottoplasty, reassess work of breathing, stridor, oxygen requirement and secretion handling as anesthesia resolves; progressive obstruction, repeated desaturation, inability to clear secretions or concern for supraglottic edema requires immediate airway reassessment rather than routine observation alone. Reassess feeding safety when preoperative aspiration/dysphagia was present or symptoms worsen after surgery.",
    },
    {
        "slug": "peds-ltr",
        "title_terms": ("laryngotracheal reconstruction",),
        "setup": "Define whether the reconstruction is single-stage versus double-stage and document the intended postoperative airway before incision: graft configuration, ETT or stent type/size and fixation, tracheostomy plan when present, sedation strategy, extubation/stent-removal timing, and the rescue plan if the reconstructed airway cannot be ventilated safely.",
        "postop": "Protect the fresh laryngotracheal reconstruction as a critical airway: unexpected tube/stent displacement, rising peak pressures, new air leak, worsening stridor/retractions, difficult suction passage, bleeding or unexplained desaturation should prompt urgent ENT/anesthesia assessment with a low threshold for controlled endoscopy. Avoid repeated blind tube manipulation across fresh grafts; re-establish the airway under direct visualization whenever feasible.",
    },
    {
        "slug": "laryngotracheal-cleft-repair",
        "title_terms": ("laryngotracheal", "cleft"),
        "setup": "Before repair, make the postoperative airway and feeding plan explicit: intended extubation versus protected intubation, enteral access, timing of oral intake, and the planned swallow/endoscopic reassessment should reflect cleft depth, pulmonary disease, aspiration burden and whether the repair is endoscopic or open.",
        "postop": "After laryngeal cleft repair, new respiratory distress, aspiration symptoms, fever, neck/chest crepitus, feeding intolerance or unexplained pulmonary decline should trigger concern for repair failure, edema or aerodigestive leak rather than being attributed automatically to baseline aspiration. Advance oral feeding according to the operative plan and postoperative swallow assessment rather than by time alone.",
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


def _prepend_unique(values, text):
    out = list(values or [])
    marker = text[:64].lower()
    if any(marker in str(x).lower() for x in out):
        return out, False
    out.insert(0, text)
    return out, True


def apply_or_pediatric_airway_management_v220(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        did_change = False
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        did_change = c1 or c2
        op["pediatric_airway_management_v220"] = True
        resolved.append(slug)
        if did_change:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
