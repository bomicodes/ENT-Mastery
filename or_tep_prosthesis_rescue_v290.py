"""v29.0 tracheoesophageal voice-prosthesis rescue for OR Tomorrow.

Deepens the existing TEP card from recognition of leakage/dislodgement into an
executable resident/chief pathway for the laryngectomy airway, missing-prosthesis
aspiration, bronchoscopic retrieval, tract preservation, and leak triage. Foundational
laryngectomy/TEP principles remain grounded in Cummings 7e, K.J. Lee 12e, and Pasha
6e; emergency management is aligned with contemporary TEP literature and laryngectomy
airway guidance.
"""

TEP_RESCUE_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology: Head and Neck Surgery, 12th ed.",
    "Pasha: Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "Ottenstein LR, Shipp C, Patel M, El-Deiry M, Sebelik M. TEP in the ER: After Hours Tracheoesophageal Prosthesis Management for the Otolaryngologist. Ann Otol Rhinol Laryngol. 2025;134(3). doi:10.1177/00034894241295467.",
    "Goldstein DP, Ralph G, de Almeida JR, et al. Tracheoesophageal voice prosthesis management in laryngectomy patients during the COVID-19 pandemic. J Otolaryngol Head Neck Surg. 2020;49:59. doi:10.1186/s40463-020-00456-z.",
    "Dewan K, Erman A, Long JL, Chhetri DK. Assessment and Retrieval of Aspirated Tracheoesophageal Prosthesis in the Ambulatory Setting. Case Rep Otolaryngol. 2018;2018:9369602. doi:10.1155/2018/9369602.",
    "Brenner MJ, Floyd L, Collins SL. Role of computed tomography and bronchoscopy in speech prosthesis aspiration. Ann Otol Rhinol Laryngol. 2007;116(12):882-886. doi:10.1177/000348940711601202.",
    "National Tracheostomy Safety Project. Emergency laryngectomy management algorithm/guidance.",
]

TARGET = {"slug": "tep", "title_terms": ("tracheoesophageal", "puncture")}

AIRWAY = (
    "A total-laryngectomy patient is a neck-only airway: oxygenation, suction, bag-mask ventilation and emergency airway access are performed through the permanent stoma, not through the mouth or nose. If a voice prosthesis is missing and the patient has dyspnea, hypoxemia, stridor/noisy stomal breathing or inability to clear secretions, stabilize the stoma airway first, call senior ENT/anesthesia support and treat the missing device as a possible tracheobronchial foreign body rather than focusing first on voice restoration."
)

MISSING = (
    "If a dislodged prosthesis cannot be physically accounted for, assume aspiration remains possible even when symptoms are mild. Inspect the stoma/TEP and airway, but do not let a normal or equivocal chest radiograph close the evaluation because aspirated prostheses may be radiographically occult. CT can help localize an unaccounted-for device in a stable patient, while flexible or rigid bronchoscopy—selected for airway stability, object position and available expertise—provides definitive airway assessment and retrieval when aspiration is suspected or confirmed."
)

RETRIEVAL = (
    "Retrieve an aspirated prosthesis under direct bronchoscopic visualization with appropriate foreign-body instruments, then inspect for retained fragments, mucosal injury and distal obstruction before declaring the airway clear. Respiratory distress, near-obstruction, difficult extraction or an unstable stoma airway moves the case to controlled airway/OR rescue rather than repeated blind forceps attempts through the stoma."
)

TRACT = (
    "After prosthesis extrusion, preserve the mature TEP tract when feasible because it can narrow or close, but tract preservation must not become blind instrumentation. If the tract is clearly identified and the local laryngectomy/SLP protocol supports it, an appropriately sized catheter or stent may be placed by a trained clinician as a temporary bridge until definitive prosthesis replacement; stop if there is resistance, uncertain tract anatomy, bleeding, pain, suspected false passage or tissue breakdown. A catheter is not a universal first-line treatment for every leaking prosthesis, and an unaccounted-for prosthesis must still be evaluated for airway aspiration."
)

LEAK = (
    "For leakage, first determine whether liquid passes through the valve or around the prosthesis. Through-device leakage suggests valve failure/debris and usually requires cleaning or prosthesis replacement; periprosthetic leakage should trigger assessment of prosthesis length/fit, tract enlargement, granulation/infection, swallowing pressure or stenosis rather than serial empiric upsizing. Significant aspiration, pneumonia/respiratory compromise, inability to maintain oral hydration safely, embedded prosthesis or recurrent tract breakdown warrants prompt ENT/SLP reassessment and definitive refitting or another tract-management strategy rather than accepting chronic aspiration for speech."
)

POSTOP = (
    "After retrieval/replacement, confirm a patent stoma airway and safe prosthesis position/function, reassess swallowing leakage before routine oral intake when clinically indicated, and give the patient/caregiver an explicit plan for recurrent dislodgement or leakage. New dyspnea, increased secretions, fever, coughing with liquids, recurrent missing-device events, bleeding or inability to pass/seat the prosthesis is a reason for repeat airway/TEP evaluation rather than repeated unsupervised manipulation."
)


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
        marker = text[:80].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def _append_unique(values, additions):
    out = list(values or [])
    known = {str(x).strip().lower() for x in out}
    changed = False
    for text in additions:
        key = str(text).strip().lower()
        if key and key not in known:
            out.append(text)
            known.add(key)
            changed = True
    return out, changed


def apply_or_tep_prosthesis_rescue_v290(registry):
    slug, op = _resolve(registry, TARGET)
    if not op:
        return {"changed": [], "count": 0, "resolved": [], "missing": [TARGET["slug"]]}
    op["setup"], c1 = _prepend_unique(op.get("setup"), [AIRWAY])
    op["steps"], c2 = _prepend_unique(op.get("steps"), [MISSING, RETRIEVAL, TRACT, LEAK])
    op["postop"], c3 = _prepend_unique(op.get("postop"), [POSTOP])
    op["sources"], c4 = _append_unique(op.get("sources"), TEP_RESCUE_SOURCES)
    op["tep_prosthesis_rescue_v290"] = True
    changed = [slug] if any((c1, c2, c3, c4)) else []
    return {"changed": changed, "count": len(changed), "resolved": [slug], "missing": []}
