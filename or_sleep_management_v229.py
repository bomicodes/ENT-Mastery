"""v22.9 sleep-surgery OR Tomorrow planning and postoperative management.

Adds procedure-specific candidacy/optimization and postoperative rescue priorities
for hypoglossal-nerve stimulation and hyoid/genioglossus airway surgery without
hard-coding payer- or device-specific numeric eligibility thresholds that can change.
"""

TARGETS = [
    {
        "slug": "hypoglossal-nerve-stimulation",
        "title_terms": ("hypoglossal",),
        "exclude_terms": ("reanimation",),
        "setup": [
            "Before hypoglossal-nerve stimulation, confirm that obstructive sleep apnea has been objectively characterized and that the patient has an appropriate non-PAP treatment indication; review current device/payer criteria, PAP intolerance or failure, BMI, central-versus-obstructive event burden, prior upper-airway surgery and the drug-induced sleep endoscopy pattern rather than relying on one historical eligibility cutoff.",
            "Use DISE to confirm that the collapse pattern is compatible with the selected stimulation system and to identify substantial multilevel obstruction that could limit response. Document baseline tongue mobility and review prior neck/chest surgery or implanted hardware because scar, altered hypoglossal branching, or generator/sensing-lead conflicts can change the operative plan.",
        ],
        "postop": [
            "After implantation, new tongue deviation/weakness, dysarthria, dysphagia, expanding neck swelling, respiratory symptoms, severe pleuritic chest pain or hypoxemia requires focused evaluation for hypoglossal-nerve dysfunction, hematoma, airway compromise, or pleural injury rather than being attributed to routine postoperative discomfort.",
            "Separate surgical healing from device programming: confirm incision and lead/generator integrity first, then proceed with activation, titration and sleep-outcome reassessment according to the device pathway. Persistent poor response should prompt evaluation of stimulation pattern, cuff/lead function, residual collapse phenotype, weight change and adherence before assuming technical failure alone.",
        ],
    },
    {
        "slug": "hyoid-genioglossus",
        "title_terms": ("hyoid", "genioglossus"),
        "exclude_terms": (),
        "setup": [
            "Before genioglossus advancement or hyoid suspension, define the level and pattern of obstruction from the sleep study plus awake examination and DISE/imaging when used; these operations should target a demonstrated tongue-base or hypopharyngeal component rather than being added automatically to every multilevel OSA operation.",
            "For genioglossus advancement, review mandibular dentition/root position and genial-tubercle anatomy so the osteotomy can capture the genioglossus attachment without injuring tooth roots or compromising mandibular continuity. For hyoid suspension, define the intended fixation vector and counsel for postoperative swallowing discomfort/dysphagia and rare neurovascular injury.",
        ],
        "postop": [
            "After tongue-base/hyoid surgery, progressive floor-of-mouth or neck swelling, worsening dysphagia, tongue weakness, airway obstruction, bleeding, malocclusion, dental symptoms or unexpected mandibular pain should trigger examination for hematoma, hypoglossal injury, osteotomy/fixation complication or airway edema rather than routine observation alone.",
            "Long-term success should be judged by symptom and objective sleep-study response, not by anatomic advancement alone; persistent OSA warrants reassessment for residual multilevel collapse and adjunctive therapy rather than repeating the same vector without re-localizing obstruction.",
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


def apply_or_sleep_management_v229(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["sleep_management_v229"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
