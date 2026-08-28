"""v23.16 procedure-specific airway/laryngology OR Tomorrow management review.

Adds resident-level planning and postoperative rescue to seven high-yield procedures
that remained generic-only after the full live OR audit. Existing operative sequence,
anatomy and danger-structure content remains authoritative. The v23.17 pediatric core
review is chained through this tail to keep runtime mutation ordering atomic.
"""

from or_pediatric_core_management_v2317 import apply_or_pediatric_core_management_v2317

TARGETS = [
    {
        "slug": "tracheal-resection",
        "title_terms": ("tracheal", "resection"),
        "setup": [
            "Before tracheal resection, define the exact length and level of stenosis/tumor, distance from the cricoid and carina, vocal-fold mobility, pulmonary reserve and prior airway procedures using endoscopy plus cross-sectional imaging when appropriate. Decide whether a tension-free primary anastomosis is realistically achievable and what release maneuvers or alternate reconstruction would be required before committing to resection length.",
            "Coordinate ventilation and rescue-airway strategy with anesthesia before transection, including how cross-field ventilation will occur and how oxygenation will be maintained if the distal airway becomes difficult to control. Review steroid exposure, diabetes, malnutrition, smoking and prior radiation because impaired wound healing raises anastomotic risk.",
        ],
        "postop": [
            "After tracheal resection, new stridor, subcutaneous emphysema, hemoptysis, respiratory distress, neck swelling, air leak or sudden voice change should raise concern for anastomotic disruption, edema, hematoma or recurrent-laryngeal-nerve dysfunction. Protect the anastomosis from repeated traumatic instrumentation and escalate early to the operating surgeon/anesthesia team when airway deterioration is not clearly benign.",
            "Maintain the planned neck-position/tension-reduction strategy and monitor swallowing, secretion clearance and pulmonary status. Progressive fever, mediastinal/neck pain, wound air, increasing oxygen requirement or sepsis should prompt evaluation for leak or deep infection rather than routine postoperative atelectasis alone.",
        ],
        "marker": "tracheal_resection_management_v2316",
    },
    {
        "slug": "airway-dilation",
        "title_terms": ("airway", "dilation"),
        "setup": [
            "Before endoscopic airway dilation, characterize stenosis by level, length, diameter, maturity and circumferential extent and determine whether the problem is primarily scar, active inflammation, malacia or a fixed framework abnormality. Review prior dilations, intubation/tracheostomy history and reflux/inflammatory disease so the team knows whether dilation is temporizing, part of serial treatment, or unlikely to provide durable benefit.",
        ],
        "postop": [
            "After dilation, worsening stridor, chest/neck pain, subcutaneous emphysema, hemoptysis, respiratory distress or escalating oxygen need requires evaluation for edema, mucosal tear, pneumomediastinum/pneumothorax or airway perforation. Recurrent symptoms after an initially good response should trigger reassessment of restenosis or an incorrect underlying mechanism rather than reflexively repeating the same dilation indefinitely.",
        ],
        "marker": "airway_dilation_management_v2316",
    },
    {
        "slug": "cordotomy",
        "title_terms": ("cordotomy",),
        "setup": [
            "Before posterior cordotomy/arytenoidectomy, confirm bilateral vocal-fold immobility or another appropriate glottic-level indication and distinguish neurogenic fixation from cricoarytenoid joint fixation or posterior glottic stenosis. Define the acceptable tradeoff between airway enlargement and voice/swallow function, and review pulmonary reserve, aspiration history and whether tracheostomy remains a safer or reversible alternative.",
        ],
        "postop": [
            "After glottic-widening surgery, new or worsening aspiration, inability to clear secretions, pneumonia, severe dysphonia, stridor or persistent airway limitation should trigger functional reassessment. Recurrent dyspnea can reflect edema, granulation, scar restenosis or inadequate posterior opening; excessive breathiness or aspiration can reflect over-widening and should not be dismissed as an unavoidable endpoint without evaluation.",
        ],
        "marker": "cordotomy_management_v2316",
    },
    {
        "slug": "microflap",
        "title_terms": ("microflap",),
        "setup": [
            "Before microlaryngoscopy/microflap, correlate the lesion with stroboscopy and voice demands and make sure the suspected pathology is appropriate for epithelial preservation rather than simple stripping or empiric excision. Counsel on phonotrauma, smoking, reflux and professional voice requirements, and plan the smallest exposure/manipulation needed to preserve the superficial lamina propria.",
        ],
        "postop": [
            "After microflap surgery, progressive dyspnea, stridor or hemoptysis is not expected and requires airway evaluation. Persistent or worsened dysphonia should be reassessed with laryngoscopy/stroboscopy for edema, hematoma, stiffness/scar, residual lesion or an alternate diagnosis; voice rest and subsequent voice therapy should follow the actual lesion and surgeon protocol rather than a one-size-fits-all duration.",
        ],
        "marker": "microflap_management_v2316",
    },
    {
        "slug": "rrp-debridement",
        "title_terms": ("rrp",),
        "setup": [
            "Before recurrent-respiratory-papillomatosis debridement, document current airway burden, voice involvement, distal tracheobronchial disease when suspected and prior treatment frequency. The goal is disease control with preservation of normal epithelium and airway—not radical mucosal stripping; review laser/fire precautions when an energy device is used and consider adjuvant therapy when disease burden or recurrence pattern warrants it.",
        ],
        "postop": [
            "After RRP surgery, worsening stridor, dyspnea, hemoptysis or inability to handle secretions warrants urgent airway reassessment for edema, bleeding, retained debris or residual obstructive disease. Over time, new anterior/posterior glottic web, stenosis or progressive voice loss should raise concern for treatment-related scar in addition to recurrent papilloma.",
        ],
        "marker": "rrp_management_v2316",
    },
    {
        "slug": "laryngeal-fracture",
        "title_terms": ("laryngeal", "fracture"),
        "setup": [
            "Before operative laryngeal-fracture repair, secure or clearly plan the airway first, then define mucosal injury, cartilage displacement, exposed cartilage, vocal-fold mobility and cricoarytenoid-joint status with endoscopy and CT as the patient's stability allows. A seemingly minor external neck injury can conceal an unstable airway, so worsening voice, stridor, hemoptysis or subcutaneous emphysema changes urgency.",
        ],
        "postop": [
            "After repair, monitor for delayed edema, hematoma, airway compromise and infection of exposed cartilage. Persistent dysphonia, aspiration, vocal-fold immobility or airway narrowing should prompt endoscopic reassessment for malposition, joint fixation, granulation or evolving stenosis because functional deficits may declare themselves after the acute swelling resolves.",
        ],
        "marker": "laryngeal_fracture_management_v2316",
    },
    {
        "slug": "transoral-laser-laryngeal-cancer",
        "title_terms": ("transoral", "laser", "laryngeal"),
        "setup": [
            "Before transoral laser microsurgery for laryngeal cancer, confirm that endoscopic exposure and tumor extent permit an oncologically sound resection. Review anterior-commissure involvement, paraglottic/pre-epiglottic spread, cartilage invasion, subglottic extension and baseline vocal-fold mobility, and have a conversion/alternative-treatment plan if deep margins or exposure are inadequate.",
            "Coordinate laser-safe airway/fire precautions and orient the planned specimen/margins before cutting so margin interpretation remains meaningful. Baseline swallowing, pulmonary reserve and expected functional loss should influence whether the proposed resection is appropriate, especially for larger supraglottic or transglottic defects.",
        ],
        "postop": [
            "After transoral laser cancer resection, airway edema, bleeding, aspiration and inability to manage secretions should be actively assessed rather than treated as routine sore throat. Delayed hemorrhage or progressive respiratory distress warrants urgent airway/operative evaluation.",
            "Review final pathology for margin status, adverse features and pathologic extent and correlate this with the endoscopic resection map. Persistent dysphonia or dysphagia should be evaluated for expected tissue loss versus granulation, scar/stenosis, aspiration or residual/recurrent disease, with surveillance and adjuvant-treatment decisions based on oncologic findings rather than symptoms alone.",
        ],
        "marker": "tlm_laryngeal_cancer_management_v2316",
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


def apply_or_airway_laryngology_management_v2316(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    v2317 = apply_or_pediatric_core_management_v2317(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v2317": v2317}
