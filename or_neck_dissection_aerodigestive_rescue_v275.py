"""v27.5 neck-dissection aerodigestive injury/contamination rescue layer.

Adds explicit recognition, source-control, repair, nutrition and stop-rule choreography for
pharyngeal/cervical-esophageal injury during neck dissection or composite resection. The
layer deliberately avoids a universal flap or diversion mandate because defect size,
tissue quality, contamination, distal obstruction, prior treatment and patient physiology
change the durable endpoint.
"""

AERODIGESTIVE_RESCUE_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "Chen S et al. Management of Iatrogenic Cervical Esophageal Perforations: A Narrative Review. JAMA Otolaryngol Head Neck Surg. 2020;146(5):488-494.",
    "Chirica M et al. Esophageal emergencies: WSES guidelines. World J Emerg Surg. 2019;14:26.",
    "American Association for Thoracic Surgery. TSRA Primer: Esophageal Perforation. Accessed 2026.",
    "Journal of Trauma and Acute Care Surgery Emergency General Surgery Algorithms Work Group. Evidence-based, cost-effective management of nontraumatic esophageal perforations. 2026.",
]

TARGETS = [{
    "slug": "neck-dissection",
    "title_terms": ("neck", "dissection"),
    "setup": [
        "Treat an unintended pharyngeal or cervical-esophageal entry as an immediate contamination/source-control problem, not a minor mucosal defect to hide at closure. Define the full extent of injury under exposure, suction saliva/enteric contamination, irrigate and debride clearly nonviable tissue, and identify whether there is distal obstruction or associated tracheal/vascular injury before choosing the durable repair strategy.",
        "If a cervical aerodigestive defect is clearly visualized and the edges are viable, favor a tension-free primary repair when technically sound, with layered closure when anatomy permits. Reinforce with well-vascularized tissue selectively when tissue is irradiated, devascularized, contaminated, under tension, or the repair is otherwise tenuous; do not encode a muscle/free flap as mandatory for every small healthy-tissue injury. Drain the contaminated cervical space rather than relying on closure alone.",
        "Make loss of a safe aerodigestive plane a stop rule. If tumor, scar, or instrumentation has created an injury whose true limits cannot be seen, repeated blind probing or continued stripping can enlarge the perforation and injure the RLN, trachea or great vessels. Stop, improve exposure and define the defect; if a safe primary repair is not achievable, transition deliberately to drainage plus defect-appropriate diversion/reconstruction or obtain additional reconstructive/thoracic expertise rather than forcing an unreliable closure.",
    ],
    "postop": [
        "After known or suspected pharyngeal/cervical-esophageal injury, protect the repair and control contamination with appropriate cervical drainage, broad-spectrum antimicrobial therapy tailored to contamination/infection, temporary avoidance of oral intake, and an early enteral or other nutrition plan. Fever, tachycardia, neck pain/swelling, erythema, crepitus, salivary or enteric drain output, wound breakdown, systemic toxicity, chest symptoms, or unexpected inflammatory deterioration should trigger urgent reassessment for persistent leak, deep-neck infection or descending mediastinal contamination rather than routine observation.",
        "For a postoperative salivary/esophageal leak, prioritize source control and anatomy: drain collections, assess the defect and distal patency, support nutrition, and escalate persistent/uncontained leaks, sepsis, necrotic tissue, threatened reconstruction, or great-vessel exposure to operative/endoscopic/reconstructive management according to location and physiology. In an infected or fistulized neck, protect an exposed carotid or other major vessel with viable tissue when feasible and treat sentinel bleeding as a separate vascular emergency; do not repeatedly probe or pack a leaking wound at bedside when a major vessel may be exposed.",
    ],
    "sources": AERODIGESTIVE_RESCUE_SOURCES,
    "marker": "neck_dissection_aerodigestive_rescue_v275",
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


def apply_or_neck_dissection_aerodigestive_rescue_v275(registry):
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
