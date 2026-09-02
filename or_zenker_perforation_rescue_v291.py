"""v29.1 — post-Zenker/cricopharyngeal myotomy perforation and leak rescue.

Extends the older recognition-only Zenker/cricopharyngeal postoperative warning into an
executable resident/chief response. Foundational ENT texts anchor pharyngoesophageal
anatomy and operative principles; contemporary ESGE perforation guidance anchors rapid
CT evaluation, selective endoscopic closure, diversion and escalation after failed
closure or clinical deterioration.
"""

TARGETS = (
    ("zenker", ("zenker",)),
    ("cricopharyngeal-myotomy", ("cricopharyngeal", "myotomy")),
)

RESCUE = [
    "ZENKER / CRICOPHARYNGEAL LEAK COMMITMENT POINT: after endoscopic septotomy, Z-POEM, rigid diverticulotomy, or open cricopharyngeal myotomy, escalating neck/chest pain, fever, tachycardia, crepitus/subcutaneous emphysema, dyspnea, inability to handle secretions, rapidly progressive swelling, or systemic toxicity is not routine postoperative discomfort. Stop oral intake, reassess airway and hemodynamics, obtain IV access, begin resuscitation as needed, and involve the responsible laryngology/head-and-neck or esophageal surgical team early.",
    "DEFINE THE LEAK BEFORE ROUTINE DIET ADVANCEMENT: when perforation or pharyngoesophageal leak is suspected, obtain prompt CT of the neck and chest with an appropriate leak protocol when clinically feasible to define extraluminal air/fluid, cervical collection, mediastinal or pleural contamination, and the likely level of the defect. A water-soluble contrast swallow may be complementary in a stable patient, but an equivocal study should not override worsening physiology or convincing CT findings. Avoid repeated blind instrumentation through a suspected defect.",
    "CONTAINMENT / EARLY ENDOSCOPIC BAILOUT: keep the patient NPO and provide IV antimicrobial therapy covering upper aerodigestive flora while planning nutritional diversion/support. If an endoscopic mucosal defect or perforation is recognized early and is technically suitable, endoscopic closure can be considered according to defect size/location and available expertise; after Z-POEM or flexible endoscopic treatment, the endpoint is a secure mucosal closure and controlled leak, not merely completion of the myotomy. Prophylactic antibiotics for an uncomplicated Zenker septotomy are not the same as therapeutic antibiotics for a suspected perforation or infected leak.",
    "SOURCE-CONTROL DECISION: a small, early, contained cervical leak in a clinically stable patient with minimal contamination may be managed nonoperatively only with close inpatient observation, NPO/diversion, antimicrobial therapy, nutritional support, and a defined reassessment plan. Free leak, enlarging cervical collection, mediastinal or pleural contamination, necrotic tissue, sepsis, airway compromise, failed/infeasible endoscopic closure, or clinical deterioration is source-control failure and should trigger drainage and operative repair/revision or another definitive strategy appropriate to the defect and prior approach. Do not simply extend antibiotics while contamination progresses.",
    "POST-RESCUE ENDPOINTS: before resuming oral intake, confirm that the leak trajectory is clinically controlled and use targeted imaging/endoscopic reassessment when indicated by the repair strategy and symptoms. Recurrent fever, neck pain/swelling, aspiration, chest symptoms, leukocytosis, or worsening oxygen requirement after initial improvement should reopen the perforation/deep-infection pathway rather than being attributed to routine postoperative inflammation.",
]

SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. — Zenker diverticulum, pharyngoesophageal anatomy, cricopharyngeal myotomy and complication principles",
    "K. J. Lee's Essential Otolaryngology, 12th ed. — Zenker diverticulum/cricopharyngeal dysfunction and cervical esophageal complication principles",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed. — Zenker/cricopharyngeal management framework",
    "Paspatis GA, Arvanitakis M, Dumonceau JM, et al. Diagnosis and management of iatrogenic endoscopic perforations: ESGE Position Statement—Update 2020. Endoscopy. 2020;52(9):792-810. doi:10.1055/a-1222-3191",
    "Weusten BLAM, Barret M, Bredenoord AJ, et al. Endoscopic management of gastrointestinal motility disorders—part 2: ESGE Guideline. Endoscopy. 2020;52:600-614. Zenker diverticulum recommendations.",
    "Dhar SI. How I do It: Zenker's Per Oral Endoscopic Myotomy with Partial Mucosal Septum Division Modification. Laryngoscope. 2025;135:1029-1033. doi:10.1002/lary.31840",
]


def _resolve(registry, preferred, terms):
    reg = registry or {}
    if preferred in reg:
        return preferred, reg[preferred]
    for key, op in reg.items():
        hay = (str(key) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in terms):
            return key, op
    return None, None


def _append_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in additions:
        marker = text[:88].lower()
        if not any(marker in str(x).lower() for x in out):
            out.append(text)
            changed = True
    return out, changed


def apply_or_zenker_perforation_rescue_v291(registry):
    changed, resolved, missing = [], [], []
    seen = set()
    for preferred, terms in TARGETS:
        key, op = _resolve(registry, preferred, terms)
        if not op:
            missing.append(preferred)
            continue
        if key in seen:
            continue
        seen.add(key)
        op["postop"], c1 = _append_unique(op.get("postop"), RESCUE)
        op["sources"], c2 = _append_unique(op.get("sources"), SOURCES)
        op["zenker_perforation_rescue_v291"] = True
        op["zenker_perforation_semantic_role_v291"] = (
            "recognize leak -> NPO/resuscitate/antibiotics -> CT define contamination -> "
            "selective early closure/contained observation -> drainage or operative source control"
        )
        resolved.append(key)
        if c1 or c2:
            changed.append(key)
    return {"changed": changed, "count": len(changed), "resolved": resolved, "missing": missing}
