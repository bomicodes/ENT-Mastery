"""v20.8 procedure-specific safety priorities for OR Tomorrow.

Adds only high-consequence perioperative details that are not well served by the
family-level setup/postoperative framework.
"""

UPDATES = {
    "tracheal-resection": {
        "setup": [
            "Quantify airway physiology as well as anatomy: review stenosis length/location and prior airway interventions, assess pulmonary reserve and active respiratory infection, and identify prior radiation, chronic steroid exposure or other factors that may impair anastomotic healing."
        ],
        "postop": [
            "Protect the fresh tracheal anastomosis: maintain the planned neck-flexion strategy, avoid unnecessary positive-pressure ventilation/coughing strain, and treat new subcutaneous emphysema, air leak, respiratory distress or wound crepitus as possible anastomotic failure requiring urgent surgical review."
        ],
    },
    "peds-ltr": {
        "setup": [
            "Before reconstruction, review pulmonary status, aspiration/swallow history, reflux control, tracheostomy dependence/secretions and recent airway infection; these factors influence graft healing, postoperative intubation strategy and ICU planning."
        ],
        "postop": [
            "Make the postoperative airway plan explicit: tube/stent size and position, sedation/extubation timing, secretion clearance and criteria for urgent endoscopy if ventilation worsens or the reconstructed airway is threatened."
        ],
    },
    "total-laryngectomy": {
        "postop": [
            "A total-laryngectomy patient is a permanent neck breather: all oxygenation, bag-mask ventilation and emergency intubation must occur through the tracheal stoma; oral or nasal intubation cannot ventilate the lungs."
        ],
    },
    "neck-dissection": {
        "postop": [
            "After low-neck dissection, inspect drain character and output for chyle leak—especially on the left and after enteral feeding—and document shoulder function/CN XI status early so new deficits are recognized rather than attributed to routine postoperative pain."
        ],
    },
    "free-flap-basics": {
        "setup": [
            "For lower-extremity donor sites or patients with vascular disease, assess donor-site perfusion and relevant peripheral vascular history; also optimize diabetes, renal dysfunction, anemia and nutrition because these affect wound and flap recovery."
        ],
        "postop": [
            "Treat a new change in flap color, turgor, temperature, capillary refill or Doppler signal as time-critical vascular compromise; venous congestion or arterial insufficiency requires immediate flap-team assessment and a low threshold for operative exploration."
        ],
    },
    "cochlear-implant": {
        "postop": [
            "Document immediate facial-nerve function and vestibular symptoms; new facial weakness, severe/progressive vertigo, CSF-like drainage, meningitic symptoms or wound/device infection warrants urgent otologic evaluation."
        ],
    },
}


def _prepend_unique(values, additions):
    out = list(values or [])
    for text in reversed(additions):
        marker = text[:56].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
    return out


def apply_or_safety_priorities_v208(registry):
    changed = []
    for slug, sections in UPDATES.items():
        op = registry.get(slug)
        if not op:
            continue
        before = repr((op.get("setup"), op.get("postop")))
        for key, additions in sections.items():
            op[key] = _prepend_unique(op.get(key), additions)
        op["safety_priorities_v208"] = True
        if before != repr((op.get("setup"), op.get("postop"))):
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(UPDATES)}
