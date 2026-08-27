"""v23.8+ pediatric adenotonsillar OR Tomorrow planning and postoperative rescue.

Adds procedure-specific perioperative decisions and high-consequence postoperative
failure modes for tonsillectomy, adenoidectomy, and combined adenotonsillectomy.
Later reviewed septoplasty management is chained here so the decision hook remains
atomic. Operative choreography and anatomy remain in their existing reviewed layers.
"""

from or_septoplasty_management_v239 import apply_or_septoplasty_management_v239

TARGETS = [
    {
        "slug": "tonsillectomy",
        "title_terms": ("tonsillectomy",),
        "exclude_terms": ("adenoid", "lingual"),
        "setup": [
            "Before tonsillectomy, define the indication and postoperative risk rather than treating all cases identically: review sleep-study severity when available, age, obesity, craniofacial/neuromuscular or cardiopulmonary disease, baseline oxygenation, bleeding history, anticoagulant/platelet-affecting medication exposure, hydration/nutrition, and prior peritonsillar surgery or unusual anatomy. Severe OSA or significant medical comorbidity should lower the threshold for monitored postoperative observation rather than routine outpatient disposition.",
            "Clarify whether the planned technique is extracapsular versus intracapsular and align counseling with that choice. The tradeoff is not simply pain versus speed: intracapsular surgery generally leaves a rim of tonsillar tissue and can reduce postoperative morbidity in selected patients but carries a small risk of regrowth/revision, whereas extracapsular removal exposes the constrictor-plane fossae and carries the classic secondary-hemorrhage risk.",
        ],
        "postop": [
            "Any post-tonsillectomy oral bleeding, hematemesis, repeated swallowing, tachycardia, pallor or unexplained hypotension should be treated as possible tonsillar hemorrhage until proven otherwise. Stabilize airway and circulation, obtain IV access/laboratory support as appropriate, involve ENT/anesthesia early, keep the patient NPO, and recognize that brisk or recurrent bleeding often requires operative control; a temporarily dry oropharynx does not exclude a recent significant bleed.",
            "After tonsillectomy, respiratory obstruction or repeated desaturation requires reassessment for residual OSA, anesthetic/opioid effect, edema or bleeding rather than reflexive escalation of opioids. Poor oral intake, reduced urine output, uncontrolled pain or persistent emesis should prompt active dehydration/analgesia management because inadequate hydration can drive unplanned return care even without hemorrhage.",
        ],
    },
    {
        "slug": "adenoidectomy",
        "title_terms": ("adenoidectomy",),
        "exclude_terms": ("tonsil",),
        "setup": [
            "Before adenoidectomy, examine or review the palate for overt or submucous cleft and assess baseline speech/velopharyngeal function when history raises concern. In a child at risk for velopharyngeal insufficiency, the extent of adenoid removal should be individualized rather than assuming complete posterior-wall clearance is always desirable.",
            "Clarify the indication—nasal obstruction/OSA, chronic adenoiditis, or otologic disease—and review prior cleft surgery, syndromic craniofacial diagnosis, nasal regurgitation or hypernasality because these findings materially change counseling and the operative endpoint.",
        ],
        "postop": [
            "After adenoidectomy, new persistent hypernasality, nasal air escape or nasal regurgitation should prompt assessment for velopharyngeal insufficiency rather than being dismissed as routine congestion; transient resonance change can occur, but persistent or functionally important symptoms need speech/velopharyngeal evaluation.",
            "Significant postoperative epistaxis/oropharyngeal bleeding, hematemesis, respiratory distress, severe neck pain/stiffness, fever with toxicity or neurologic symptoms is not routine recovery. Examine for surgical bleeding or infection and escalate severe cervical symptoms because rare deep-space/inflammatory complications require prompt recognition.",
        ],
    },
    {
        "slug": "adenotonsillectomy",
        "title_terms": ("tonsillectomy", "adenoid"),
        "exclude_terms": (),
        "setup": [
            "Before adenotonsillectomy for sleep-disordered breathing, use age, polysomnographic severity when available, obesity, craniofacial/neuromuscular or cardiopulmonary disease, baseline hypoxemia and prior airway history to determine postoperative disposition. The operation does not guarantee normalization of OSA in high-risk children, so families and the care team should have an explicit plan for monitored recovery and later reassessment when residual disease risk is substantial.",
            "Review bleeding risk and palate/velopharyngeal function before combining the procedures. If submucous cleft or velopharyngeal vulnerability is suspected, modify the adenoid component rather than allowing a routine complete adenoidectomy to create avoidable postoperative VPI.",
        ],
        "postop": [
            "After adenotonsillectomy, manage any oral bleeding, hematemesis or repeated swallowing as possible post-tonsillectomy hemorrhage and any progressive obstruction/desaturation as an airway problem requiring immediate reassessment. Hemorrhage and respiratory compromise can coexist, so a bleeding child should not be evaluated only from a hemodynamic perspective.",
            "Monitor hydration, analgesia and oral intake while avoiding respiratory-depressant medication escalation in an obstructive-sleep-apnea patient without reassessing ventilation. Persistent hypernasality or nasal regurgitation after the adenoid component should trigger velopharyngeal assessment, and persistent snoring/obstructive symptoms in a high-risk child should prompt objective OSA follow-up rather than assuming surgical cure.",
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


def apply_or_adenotonsillar_management_v238(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["adenotonsillar_management_v238"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    v239 = apply_or_septoplasty_management_v239(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v239": v239}
