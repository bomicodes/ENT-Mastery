"""v29.2 — airway-dilation laceration, rupture and air-leak rescue.

Deepens the existing endoscopic airway-dilation stop point into an executable
resident/chief response to suspected transmural laryngotracheal injury,
pneumomediastinum/pneumothorax, or acute loss of airway. Foundational ENT texts
anchor stenosis anatomy and dilation principles; contemporary tracheobronchial-injury
literature anchors bronchoscopy/CT assessment and selective conservative versus
endoscopic/open rescue.
"""

TRIGGERS = (
    "airway dilation",
    "balloon dilation",
    "subglottic dilation",
    "laryngotracheal dilation",
)

RESCUE = [
    "AIRWAY-DILATION COMMITMENT / STOP POINT: after balloon or rigid dilation, a deep tear with visible extraluminal tissue, rapidly increasing cervical/chest subcutaneous emphysema, unexpected major air leak, hypoxemia, respiratory distress, pneumothorax physiology, or inability to ventilate is not a cue for another larger dilation. Stop further dilation/instrumentation, announce the suspected airway injury, coordinate immediately with anesthesia, and prioritize oxygenation and a controlled rescue airway while preserving direct visualization of the injured segment.",
    "DEFINE THE INJURY UNDER CONTROL: bronchoscopy/direct endoscopic inspection is the key test for defining the level, depth and length of a suspected tracheal or laryngotracheal tear and for identifying distal blood/clot or obstruction. CT neck/chest is an important adjunct when the patient can be stabilized, defining pneumomediastinum, pneumothorax, subcutaneous air and associated mediastinal injury. A reassuring screening chest radiograph does not exclude a small pneumomediastinum or airway-wall injury when the clinical/endoscopic findings remain concerning.",
    "VENTILATION BAILOUT: avoid repeated blind traumatic instrumentation across a known tear. If positive-pressure ventilation is required, use bronchoscopic/direct guidance and, when anatomy allows, position an endotracheal-tube cuff distal to the injury in healthy airway rather than inflating a cuff directly across the defect. If the injury or stenosis prevents safe transoral ventilation, escalate early to the airway surgeon/anesthesia team for the most controlled alternative airway strategy rather than repeatedly forcing the same route.",
    "PLEURAL / MEDIASTINAL DANGER: new hypotension, severe hypoxemia, unilateral loss of breath sounds or other tension-pneumothorax physiology after dilation requires immediate pleural decompression followed by definitive drainage as appropriate; do not delay life-saving treatment for CT. Progressive pneumomediastinum, mediastinal fluid/infection, persistent large air leak, or concern for associated esophageal injury should trigger thoracic/airway surgical escalation and source-control planning rather than routine PACU observation.",
    "CONSERVATIVE VERSUS DEFINITIVE REPAIR: a superficial or small contained injury in a hemodynamically and respiratory-stable patient, without progressive air leak, esophageal injury or mediastinitis, can sometimes be managed nonoperatively with close monitored observation and serial clinical/endoscopic assessment. Full-thickness or enlarging disruption, inability to ventilate safely, persistent/progressive air leak, mediastinitis, associated esophageal injury, or clinical deterioration is a failure of conservative management and requires expert endoscopic stenting/closure or operative repair/reconstruction according to injury level, tissue quality and local expertise.",
    "POST-RESCUE SURVEILLANCE: after any clinically significant dilation injury, reassess work of breathing, oxygen requirement, neck/chest emphysema, hemoptysis and airway caliber before disposition. Worsening dyspnea, chest pain, fever, expanding crepitus, recurrent hypoxemia or new radiographic air should reopen the airway-injury pathway; later follow-up must also account for restenosis or granulation after healing.",
]

SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. — adult/pediatric laryngotracheal stenosis anatomy, endoscopic dilation and airway-complication principles",
    "K. J. Lee's Essential Otolaryngology, 12th ed. — laryngotracheal stenosis, endoscopic airway management and complication principles",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed. — subglottic/tracheal stenosis and airway rescue framework",
    "Bae JI, Kim YH, Lee KH, et al. Tracheobronchial laceration after balloon dilation for benign strictures: incidence and clinical significance. Chest. 2007;131(4):1114-1117. doi:10.1378/chest.06-2301",
    "Heyes R, Cervantes SS, Matthaeus J, Jaroszewski D, Lott DG. Balloon dilation causing tracheal rupture: endoscopic management and literature review. Laryngoscope. 2016;126(12):2774-2777. doi:10.1002/lary.25977",
    "Post-intubation iatrogenic tracheobronchial injuries: the state of art. Front Surg. 2023;10:1125997. doi:10.3389/fsurg.2023.1125997",
    "A Review of Indications and Technical Considerations of Endoscopic Balloon Dilation for Pediatric Subglottic Stenosis. J Clin Med. 2026;15(8):2940 — complication/risk-management synthesis",
]


def _matches(slug, op):
    hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
    if "sial" in hay:
        return False
    return any(term in hay for term in TRIGGERS)


def _append_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in additions:
        marker = text[:88].lower()
        if not any(marker in str(x).lower() for x in out):
            out.append(text)
            changed = True
    return out, changed


def apply_or_airway_dilation_injury_rescue_v292(registry):
    changed, resolved = [], []
    for slug, op in (registry or {}).items():
        if not _matches(slug, op):
            continue
        op["postop"], c1 = _append_unique(op.get("postop"), RESCUE)
        op["sources"], c2 = _append_unique(op.get("sources"), SOURCES)
        op["airway_dilation_injury_rescue_v292"] = True
        op["airway_dilation_injury_semantic_role_v292"] = (
            "stop dilation -> bronchoscopy/CT define injury -> controlled ventilation -> "
            "decompress pleural emergency -> observe contained injury or escalate repair"
        )
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "resolved": resolved}
