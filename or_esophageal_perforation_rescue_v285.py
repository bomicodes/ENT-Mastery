"""v28.5 — iatrogenic cervical esophageal perforation rescue after endoscopy/foreign-body work.

Extends recognition-only postoperative warnings into an executable resident/chief
response. Foundational ENT texts anchor cervical esophageal anatomy and operative
principles; contemporary ESGE perforation guidance anchors CT-first evaluation,
endoscopic closure selection, diversion, and escalation after failed closure or clinical
deterioration.
"""

TARGETS = (
    ("esophageal-fb", ("esophageal", "foreign")),
    ("transnasal-esophagoscopy", ("transnasal", "esophagoscopy")),
)

RESCUE = [
    "ESOPHAGEAL PERFORATION COMMITMENT POINT: after esophagoscopy or foreign-body extraction, escalating neck/chest pain, fever, tachycardia, crepitus/subcutaneous emphysema, dyspnea, hematemesis, inability to swallow secretions, or systemic toxicity is not routine post-instrumentation discomfort. Stop oral intake, reassess airway/hemodynamics, obtain IV access, begin resuscitation as needed, and involve the responsible ENT/esophageal surgical team early. A normal early examination does not reliably exclude a small cervical perforation when symptoms are evolving.",
    "DIAGNOSTIC BAILOUT: suspected iatrogenic perforation should be evaluated promptly with CT of the neck/chest using an appropriate esophageal leak protocol when clinically feasible; CT also defines extraluminal air/fluid and mediastinal or pleural contamination that changes management. A contrast swallow can be complementary in a stable patient, but do not let a negative or equivocal study override worsening physiology or CT evidence of contamination. Avoid repeated blind instrumentation through a suspected defect.",
    "CONTAINMENT / SOURCE-CONTROL FRAME: keep the patient NPO and provide IV broad-spectrum antimicrobial therapy covering oral/upper-GI flora, with drainage and nutritional planning according to the leak and clinical course. A small, early, contained cervical perforation in a stable patient with minimal contamination may be managed nonoperatively only with close inpatient observation, antimicrobial therapy, nutritional diversion/support, and a clear plan for repeat clinical/imaging assessment; deterioration, free leak, enlarging collection, mediastinal/pleural contamination, necrotic tissue, or uncontrolled sepsis is a source-control failure, not a reason to simply extend antibiotics.",
    "CLOSURE / OPERATIVE ESCALATION: when an iatrogenic esophageal defect is recognized early and is technically suitable, endoscopic closure can be considered based on defect size/location and local expertise, with diversion of luminal contents and ongoing monitoring after closure. Failed or infeasible endoscopic closure, clinical deterioration, uncontrolled contamination, or a noncontained leak requires urgent surgical consultation for drainage and repair or other definitive source-control strategy appropriate to the cervical versus thoracic location. The endpoint is durable leak control plus sepsis control—not merely successful scope withdrawal or temporary symptom improvement.",
]

SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. — hypopharyngeal/cervical esophageal anatomy, endoscopy complications, and perforation principles",
    "K. J. Lee's Essential Otolaryngology, 12th ed. — esophagoscopy, foreign-body, and cervical esophageal perforation principles",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed. — esophageal foreign body/endoscopy complication framework",
    "Paspatis GA, Arvanitakis M, Dumonceau JM, et al. Diagnosis and management of iatrogenic endoscopic perforations: ESGE Position Statement—Update 2020. Endoscopy. 2020;52(9):792-810. doi:10.1055/a-1222-3191",
]


def _resolve(registry, slug, terms):
    reg = registry or {}
    if slug in reg:
        return slug, reg[slug]
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


def apply_or_esophageal_perforation_rescue_v285(registry):
    changed, resolved, missing = [], [], []
    for slug, terms in TARGETS:
        key, op = _resolve(registry, slug, terms)
        if not op:
            missing.append(slug)
            continue
        op["postop"], c1 = _append_unique(op.get("postop"), RESCUE)
        op["sources"], c2 = _append_unique(op.get("sources"), SOURCES)
        op["esophageal_perforation_rescue_v285"] = True
        op["esophageal_perforation_semantic_role_v285"] = (
            "recognize perforation -> NPO/resuscitate/antibiotics -> CT define contamination -> "
            "contained-stable selective nonoperative pathway versus early closure -> source-control escalation"
        )
        resolved.append(key)
        if c1 or c2:
            changed.append(key)
    return {"changed": changed, "count": len(changed), "resolved": resolved, "missing": missing}
