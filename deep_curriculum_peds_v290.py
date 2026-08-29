"""v29.0 — source-grounded pediatric upper-airway Concept Hub rebuild.

Separates the broad bedside differential card Croup vs Epiglottitis from the dedicated
Epiglottitis card. The differential card teaches pattern recognition and first-response
triage; the epiglottitis card teaches airway-risk assessment, controlled evaluation,
antibiotics, and operative airway planning.
"""

import re

DOMAIN = "Pediatric Otolaryngology"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


PEDS_AIRWAY_REBUILD_V290 = {
    "croup vs epiglottitis": {
        "recognize": (
            "Recognize the CHILD WITH ACUTE UPPER-AIRWAY OBSTRUCTION before naming the diagnosis. Croup classically produces a barking cough, hoarseness, and inspiratory stridor after a viral prodrome, often with a child who can still handle secretions. Epiglottitis more often presents with toxic appearance, high fever, severe odynophagia/dysphagia, muffled voice, drooling, preference for sitting upright or leaning forward, and relatively little cough. The immediate question is not which eponym fits best; it is whether the child is maintaining oxygenation, ventilation, secretion control, and a stable work of breathing."
        ),
        "localize": (
            "Localize the obstruction from the SOUND + VOICE + SECRETIONS. Croup is predominantly subglottic inflammation, so the signature is barking cough plus hoarseness and inspiratory or biphasic stridor. Epiglottitis/supraglottitis is supraglottic inflammation, so painful swallowing, drooling, muffled voice, and reluctance to lie flat are more discriminating than stridor alone. Also keep bacterial tracheitis, retropharyngeal abscess, peritonsillar infection, foreign body, anaphylaxis, and deep-neck infection in the differential when the pattern is atypical. Stridor is a localization clue, not a diagnosis."
        ),
        "workup": (
            "Evaluate severity clinically before ordering tests. In typical croup, laboratory testing and neck radiographs are usually unnecessary; the Westley-style features that matter are stridor at rest, retractions, air entry, cyanosis, and mental status. In suspected epiglottitis, do NOT force an agitated child supine, repeatedly examine the oropharynx, or send an unstable patient away for radiography. Stable patients with uncertain diagnoses may undergo controlled flexible laryngoscopy or imaging only when the airway team judges it safe. A classic AP 'steeple sign' can occur in croup and a lateral 'thumb sign' can occur in epiglottitis, but neither image should delay treatment or controlled airway management."
        ),
        "manage": (
            "Treat croup by severity: give corticosteroid to essentially all clinically significant cases; add nebulized epinephrine for moderate/severe disease or stridor at rest, then observe for recurrent symptoms after the medication's transient effect. Keep the child calm and avoid unnecessary procedures. Suspected epiglottitis requires a different pathway: minimize agitation, provide oxygen as tolerated, summon anesthesia/ENT/critical-care support early, and begin IV antibiotics active against Haemophilus influenzae and other likely bacterial pathogens once doing so will not destabilize the airway. Do not treat a toxic drooling child as 'severe croup' simply because stridor is present."
        ),
        "operate": (
            "Escalate based on AIRWAY TRAJECTORY. Most croup does not require intubation; impending failure is suggested by worsening fatigue, decreased air movement, hypoxemia, altered mental status, or severe obstruction despite medical therapy. Suspected epiglottitis with significant distress, hypoxemia, rapidly progressive symptoms, inability to handle secretions, or concerning endoscopic findings should be secured in a CONTROLLED environment by the most experienced airway team available, ideally with ENT prepared for surgical airway rescue. Avoid provocative bedside instrumentation in a tenuous child."
        ),
        "teach": (
            "Boards framework: CROUP = BARKING COUGH + HOARSENESS + SUBGLOTTIC STRIDOR; EPIGLOTTITIS = TOXIC/DROOLING/ODYNOPHAGIA + SUPRAGLOTTIC AIRWAY RISK. Steroid is foundational for croup; nebulized epinephrine is added when symptoms are more than mild. Epiglottitis is an airway-management problem first and a diagnostic-test problem second. Never let a radiograph, throat culture, or forced oral examination destabilize a child whose airway could close."
        ),
        "tags": ["croup", "epiglottitis", "pediatric stridor", "upper airway obstruction", "barking cough", "drooling", "nebulized epinephrine", "dexamethasone"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — pediatric stridor, croup, supraglottitis/epiglottitis, and acute airway management",
            "K.J. Lee's Essential Otolaryngology, 12e — pediatric airway infection differential and emergency management",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — croup, epiglottitis, stridor, and pediatric airway pearls",
            "Canadian Paediatric Society practice point: Acute management of croup in the emergency department — corticosteroid for croup and nebulized epinephrine for moderate/severe disease",
        ],
    },
    "epiglottitis": {
        "recognize": (
            "Recognize EPIGLOTTITIS/SUPRAGLOTTITIS as potentially rapidly progressive supraglottic infection with risk of abrupt airway obstruction. The classic pediatric picture is fever, severe sore throat/odynophagia, dysphagia, drooling, muffled voice, anxiety, upright or tripod positioning, and respiratory distress out of proportion to visible oropharyngeal findings. Hib vaccination has made classic Hib pediatric epiglottitis far less common, but the diagnosis still occurs from Hib breakthrough, other streptococcal/staphylococcal organisms, and in incompletely immunized children. Absence of the old textbook presentation does not make the airway safe."
        ),
        "localize": (
            "Localize disease to the SUPRAGLOTTIS and estimate how much reserve remains. Inflammation can involve the epiglottis, aryepiglottic folds, arytenoids, and adjacent supraglottic tissues. Clinical danger rises with stridor, retractions, hypoxemia, inability to swallow secretions, rapidly progressive symptoms, altered mental status, or inability to tolerate supine positioning. Distinguish supraglottitis from croup, bacterial tracheitis, deep-neck infection, peritonsillar/retropharyngeal abscess, angioedema, and foreign body because those entities differ in where obstruction occurs and how the airway should be approached."
        ),
        "workup": (
            "Work up suspected epiglottitis only in a manner that preserves airway control. Keep the child with the caregiver in a position of comfort, minimize agitation, and obtain continuous cardiorespiratory/oxygen monitoring while mobilizing the airway team. Flexible nasolaryngoscopy can confirm supraglottic edema in a sufficiently stable patient when performed by an experienced clinician in an appropriately monitored setting. Lateral neck radiography is not required and should never delay airway management. Blood cultures and, after the airway is secured, supraglottic cultures may identify the pathogen; do not provoke gagging or obtain a throat culture from a tenuous child simply to secure microbiology."
        ),
        "manage": (
            "Management is AIRWAY + ANTIBIOTICS + ICU-LEVEL OBSERVATION. Maintain calm, avoid unnecessary venipuncture or procedures until the airway plan is established, and involve ENT/anesthesia/critical care early. After airway safety is addressed, start parenteral broad bacterial coverage such as a third-generation cephalosporin, with additional anti-staphylococcal/MRSA coverage when local epidemiology or clinical features warrant. If Hib is confirmed, manage close-contact prophylaxis according to public-health recommendations and vaccination status. Corticosteroids are sometimes used, but they are not a substitute for airway planning or antibiotics."
        ),
        "operate": (
            "Secure a threatened epiglottitis airway under CONTROLLED CONDITIONS rather than waiting for a crash airway. The most experienced laryngoscopist/anesthesiologist should lead, with ENT immediately available for rigid bronchoscopy/intubation assistance and surgical airway rescue. Preserve spontaneous ventilation until the airway strategy is secure when feasible; have smaller endotracheal tubes available because supraglottic edema narrows the passage. Once intubated, manage in the ICU and extubate only after clinical improvement and evidence that edema has sufficiently resolved. Emergency tracheotomy/cricothyrotomy is a rescue option, not the planned default in a child."
        ),
        "teach": (
            "Chief/boards framework: EPIGLOTTITIS = DON'T AGITATE, DON'T FORCE THE EXAM, CONTROL THE ENVIRONMENT. A drooling toxic child who prefers upright positioning has a potentially unstable supraglottic airway until proven otherwise. Diagnosis can be clinical or endoscopic in a stable setting, but airway security takes precedence over imaging. Antibiotics treat the infection; they do not immediately reverse obstruction. Hib vaccination changed epidemiology, not the fundamental airway principles."
        ),
        "tags": ["epiglottitis", "supraglottitis", "pediatric airway", "drooling", "tripod position", "Hib", "controlled intubation", "third generation cephalosporin"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — epiglottitis/supraglottitis, pediatric airway assessment, and controlled airway management",
            "K.J. Lee's Essential Otolaryngology, 12e — acute supraglottic infection and pediatric airway emergencies",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — epiglottitis diagnosis, antimicrobial therapy, and airway pearls",
            "CDC guidance for Haemophilus influenzae disease — vaccination, invasive Hib disease, and rifampin chemoprophylaxis for indicated close contacts",
        ],
    },
}


def apply_peds_airway_rebuild_v290(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = PEDS_AIRWAY_REBUILD_V290.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v290"] = True
        module["semantic_role_v290"] = (
            "acute pediatric upper-airway differential and initial triage"
            if key == "croup vs epiglottitis"
            else "epiglottitis-specific airway risk, treatment, and controlled airway strategy"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
