"""v28.6 — cervical chyle leak rescue after neck dissection.

Adds an executable resident/chief pathway after the existing low-neck thoracic-duct
avoidance choreography. Foundational ENT texts anchor anatomy and operative principles;
current head-and-neck literature anchors nutritional support and earlier escalation to
thoracic duct ligation/embolization for persistent higher-volume leaks.
"""

TARGET_TERMS = ("neck dissection",)

RESCUE = [
    "CHYLE-LEAK RECOGNITION / COMMITMENT POINT: after a low-neck dissection, especially left level IV, new high drain output or fluid that becomes milky after enteral fat exposure should trigger evaluation for lymphatic leak. Chyle can initially look clear when the patient is fasting, so appearance alone is not exclusionary. Inspect the neck and drain, quantify output/trend, and if the diagnosis is uncertain send drain triglycerides and/or chylomicrons rather than simply removing the drain.",
    "PHYSIOLOGIC RESCUE: maintain controlled drainage and follow fluid balance, electrolytes, protein/nutritional status and clinical volume status because sustained chyle loss can cause dehydration, electrolyte disturbance, protein-calorie depletion, immune compromise and impaired wound/flap healing. Begin nutrition-directed flow reduction with a low-fat or medium-chain-triglyceride strategy when enteral feeding is appropriate; involve nutrition early. Parenteral nutrition is a selected escalation for leaks that cannot be controlled enterally, not an automatic first step for every low-output leak.",
    "ADJUNCTS WITHOUT FALSE REASSURANCE: octreotide/somatostatin analog therapy can be considered as an adjunct, but evidence and protocols are heterogeneous and it does not replace drainage, nutritional support or timely source control. Compression dressings are not mandatory and should be individualized because excessive external pressure can threaten skin, a free flap, venous outflow or the airway.",
    "BAILOUT / SOURCE-CONTROL DECISION: do not wait for a single universal milliliter cutoff. Escalate early when output remains substantial or is rising despite appropriate conservative therapy, when the leak persists without a convincing downward trajectory, or when metabolic/nutritional deterioration, wound/flap compromise, cervical collection or airway/chest complications develop. Re-exploration can identify and ligate the leaking lymphatic with clips/suture and vascularized muscle coverage when appropriate; refractory or higher-volume leaks should also prompt early multidisciplinary consideration of lymphangiography with thoracic-duct/tributary embolization or thoracoscopic thoracic-duct ligation according to local expertise. The endpoint is durable leak control with physiologic recovery, not prolonged drain output tolerated until a fixed day or number is reached.",
]

SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. — neck-dissection anatomy, level-IV thoracic-duct risk, and chyle-fistula principles",
    "K. J. Lee's Essential Otolaryngology, 12th ed. — neck-dissection complications and cervical chyle-leak principles",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed. — neck-dissection complication framework",
    "Smith R, Higginson J, Breik O, Praveen P, Parmar S. Nutritional management of chyle leak after head and neck surgery: a systematic review and proposed protocol for management. Oral Maxillofac Surg. 2024;28(1):51-62. doi:10.1007/s10006-023-01152-8",
    "Picton C, Mouratidou S, Al-Lami A, et al. Improving the management of cervical chyle leak following neck dissection. J Laryngol Otol. 2026;140(1):25-30. doi:10.1017/S0022215125103526",
]


def _append_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in additions:
        marker = text[:88].lower()
        if not any(marker in str(x).lower() for x in out):
            out.append(text)
            changed = True
    return out, changed


def apply_or_neck_chyle_leak_rescue_v286(registry):
    changed, resolved = [], []
    for slug, op in (registry or {}).items():
        label = f"{slug} {(op or {}).get('title', '')}".lower()
        if not all(term in label for term in TARGET_TERMS):
            continue
        op["postop"], c1 = _append_unique(op.get("postop"), RESCUE)
        op["sources"], c2 = _append_unique(op.get("sources"), SOURCES)
        op["neck_chyle_leak_rescue_v286"] = True
        op["neck_chyle_leak_semantic_role_v286"] = (
            "recognize/confirm -> quantify and replace losses -> reduce lymphatic flow -> "
            "trend response -> escalate to cervical, interventional-radiology, or thoracic source control"
        )
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "resolved": resolved}
