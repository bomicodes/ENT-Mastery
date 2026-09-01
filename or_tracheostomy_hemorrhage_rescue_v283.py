"""v28.3 — tracheostomy hemorrhage / tracheo-innominate fistula rescue.

Adds an executable resident/chief response to delayed or major tracheostomy bleeding
without replacing the established v22.7 surgical landmarks or v26.8 false-passage and
laryngectomy-distinction rescue. The specific emergency choreography is anchored to
NTSP emergency guidance and contemporary TIF reviews; textbooks remain foundational
for tracheostomy anatomy and complication principles.
"""

TARGET = "tracheostomy"

RESCUE = [
    "TRACHEOSTOMY BLEED COMMITMENT POINT: blood-stained secretions that persist, recurrent fresh bleeding, pulsatile bleeding, or any moderate/large-volume hemorrhage from a tracheostomy must be treated as potentially vascular until proven otherwise. A small self-limited early stomal ooze is not the same problem as delayed or recurrent bleeding. A seemingly minor sentinel bleed can precede catastrophic tracheo-innominate fistula hemorrhage; do not dismiss delayed fresh blood as granulation tissue without careful assessment. Activate senior ENT/airway help, anesthesia, hemorrhage resuscitation/blood access, and the appropriate vascular/cardiothoracic or endovascular team early while suction and oxygenation are maintained.",
    "TIF TEMPORARY-CONTROL BAILOUT: if significant tracheostomy hemorrhage is occurring and the tube is cuffed/patent, hyperinflate the cuff as a temporizing tamponade maneuver while resuscitation and definitive control are mobilized. If this controls bleeding and the tube is ventilating, avoid casually removing or repeatedly manipulating it because the tube/cuff may be providing the only tamponade. If hemorrhage continues despite cuff tamponade, apply firm digital compression through the stoma into the pretracheal space to compress the innominate artery against the posterior manubrium/sternum (often termed the Utley maneuver) while maintaining airway/oxygenation and proceeding immediately toward definitive hemorrhage control. These maneuvers are bridges, not endpoints.",
    "AIRWAY + DEFINITIVE CONTROL: simultaneously manage exsanguination and airway contamination by blood. Suction aggressively, obtain large-bore access and transfuse/resuscitate as clinically required. If ventilation fails or the existing tracheostomy cannot be safely used, secure a cuffed airway with senior airway expertise using the route dictated by the patient's anatomy and stoma maturity; avoid blind repeated tube exchanges through a fresh tract. Do not delay life-saving intervention for CT/bronchoscopy in an unstable actively bleeding patient. Once temporized, proceed urgently to definitive open vascular control/ligation-repair with tracheal management and/or an endovascular strategy according to anatomy, stability, and local expertise. Persistent digital/cuff tamponade may need to be maintained during transfer to definitive control.",
    "PREVENTION / POST-RESCUE FRAME: review tracheostomy level and tube position, cuff pressure, local infection/pressure injury, radiation or other tissue-risk factors, and preoperative imaging when abnormal innominate anatomy is suspected. After any credible sentinel bleed, continued high-acuity observation and definitive evaluation are required even if bleeding stops; spontaneous cessation does not make a vascular fistula safe.",
]

SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed. — tracheostomy anatomy and complication principles",
    "K. J. Lee's Essential Otolaryngology, 12th ed. — tracheostomy and airway-complication principles",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed. — tracheostomy complications and emergency framework",
    "National Tracheostomy Safety Project (NTSP) Adult Emergency Guidelines / Tracheostomy Red Flags — delayed bleeding may indicate vascular erosion; cuff hyperinflation can provide temporary control and a tamponading tube should not be removed casually",
    "Joshi KD et al. Tracheo-Innominate Artery Fistula: A Systematic Review of Diagnostic and Management Strategies. Otolaryngol Head Neck Surg. 2025;173(4):824-839. doi:10.1002/ohn.1333",
    "Heller MA et al. Bleeding Tracheostomies—Management and Challenges. Anesthesiol Clin. 2026;44(1):101-114. doi:10.1016/j.anclin.2025.10.003",
]


def _resolve(registry):
    reg = registry or {}
    if TARGET in reg:
        return TARGET, reg[TARGET]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if "tracheostomy" in hay and not any(x in hay for x in ("laryngectomy", "tracheoesophageal puncture", "tep")):
            return slug, op
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


def apply_or_tracheostomy_hemorrhage_rescue_v283(registry):
    slug, op = _resolve(registry)
    if not op:
        return {"changed": [], "count": 0, "resolved": [], "missing": [TARGET]}
    op["postop"], c1 = _append_unique(op.get("postop"), RESCUE)
    op["sources"], c2 = _append_unique(op.get("sources"), SOURCES)
    op["tracheostomy_hemorrhage_rescue_v283"] = True
    op["tracheostomy_hemorrhage_semantic_role_v283"] = (
        "sentinel bleed recognition -> senior/hemorrhage activation -> cuff tamponade -> "
        "digital innominate compression if persistent -> simultaneous airway/resuscitation -> definitive vascular control"
    )
    return {"changed": [slug] if (c1 or c2) else [], "count": int(bool(c1 or c2)), "resolved": [slug], "missing": []}
