"""v31.5 — source-grounded pediatric croup/epiglottitis Concept Hub rebuild.

Separates the comparison/triage card from the disease-specific epiglottitis card.
The comparison card owns bedside discrimination and immediate branching; the
standalone epiglottitis card owns airway-control choreography, infectious workup,
antimicrobial treatment, extubation, and prevention context.
"""

import re

FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


PEDIATRIC_UPPER_AIRWAY_REBUILD_V315 = {
    "croup vs epiglottitis": {
        "recognize": (
            "Use this card as an AIRWAY-TRIAGE comparison, not as a second epiglottitis chapter. Croup is usually a viral subglottic illness in a young child with barking cough, hoarseness, inspiratory stridor, and symptoms that often evolve over hours after an upper-respiratory prodrome. Epiglottitis/supraglottitis is an invasive inflammatory process above the glottis: the dangerous phenotype is abrupt toxic appearance, high fever, severe odynophagia/dysphagia, drooling, muffled voice, tripod/sniffing posture, and reluctance to lie flat; cough is usually absent or not the dominant feature. Stridor in either disease signals narrowing, but quietness, fatigue, cyanosis, altered mental status, poor air movement, or decreasing stridor despite worsening effort are pre-arrest findings rather than improvement."
        ),
        "localize": (
            "Localize by CLINICAL COMPARTMENT. Croup primarily narrows the subglottis; the classic radiographic steeple sign is neither required nor sufficiently sensitive/specific to make the diagnosis. Epiglottitis primarily involves the epiglottis and adjacent supraglottic tissues, so swallowing pain, drooling, muffled voice, and positional distress carry more weight than a barking cough. Other must-not-miss causes of pediatric stridor include bacterial tracheitis, retropharyngeal abscess, peritonsillar infection, foreign body, anaphylaxis/angioedema, and deep-neck infection. The bedside goal is not to obtain a perfect label before acting; it is to recognize which child can tolerate routine examination and which child may lose the airway if agitated or placed supine."
        ),
        "workup": (
            "For typical croup, diagnosis is clinical and routine neck radiographs, viral testing, and laboratory studies are unnecessary. Grade severity from stridor at rest, retractions, air entry, agitation/lethargy, and oxygenation rather than from the bark alone. In suspected epiglottitis with respiratory distress, DO NOT force an oral/pharyngeal examination, tongue-depressor exam, IV placement, CT scan, or supine radiograph before an airway plan is ready; keep the child calm in the position of comfort and mobilize pediatric anesthesia/ENT/critical care. Imaging or flexible visualization is appropriate only in a stable patient when it will change the differential and can be performed without destabilizing the airway. After the airway is secured, obtain blood culture and, when safely obtainable, epiglottic/supraglottic culture to refine therapy."
        ),
        "manage": (
            "Branch early. CROUP: give dexamethasone to essentially all clinically diagnosed cases; add nebulized epinephrine for moderate/severe disease or significant stridor at rest, then observe long enough to ensure recurrent obstruction does not emerge as epinephrine effect wanes. Humidified mist, antibiotics, and sedatives do not treat routine viral croup. EPIGLOTTITIS: minimize agitation, provide oxygen only if tolerated without provoking distress, keep the child with a caregiver when possible, and move toward controlled airway management with ENT/anesthesia rather than repeated bedside procedures. After airway control, start IV therapy active against invasive H. influenzae and other likely bacterial pathogens, then narrow to cultures/local susceptibility and infectious-disease guidance."
        ),
        "operate": (
            "The operative decision in this comparison card is WHEN TO ESCALATE, not the full technique of epiglottitis intubation. Croup rarely requires intubation; escalating epinephrine requirement, exhaustion, hypercarbia, altered mental status, cyanosis, or poor air entry should trigger ICU/anesthesia involvement and controlled airway planning. Suspected epiglottitis with progressive obstruction is different: do not wait for complete obstruction or attempt a casual bedside intubation. Transfer with personnel/equipment capable of controlled airway rescue, while maintaining spontaneous ventilation and a backup surgical airway plan. The disease-specific epiglottitis card owns the detailed intubation/extubation choreography."
        ),
        "teach": (
            "Chief/boards discriminator: BARKING COUGH + HOARSENESS + SUBGLOTTIC STRIDOR = think croup; DROOLING + DYSPHAGIA/ODYNOPHAGIA + MUFFLED VOICE + TOXIC/TRIPOD CHILD = think epiglottitis until proven otherwise. Croup management is steroid-based, with nebulized epinephrine when more severe. Epiglottitis management is airway-first and agitation-averse. Do not use a normal-looking throat, absence of a thumbprint sign, or current Hib vaccination as permission to dismiss a dangerous supraglottic phenotype. Hib vaccination has made classic pediatric Hib epiglottitis uncommon, not impossible, and non-Hib organisms also cause epiglottitis."
        ),
        "tags": ["croup", "epiglottitis", "stridor", "barking cough", "drooling", "dexamethasone", "nebulized epinephrine", "pediatric airway", "airway triage"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — pediatric inflammatory upper-airway obstruction, croup, epiglottitis/supraglottitis, and airway management",
            "K.J. Lee's Essential Otolaryngology, 12e — pediatric upper-airway obstruction and infectious airway emergencies",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — pediatric airway, croup, epiglottitis, and stridor differential",
            "Canadian Paediatric Society, Acute management of croup in the emergency department — dexamethasone; nebulized epinephrine for moderate/severe croup; post-epinephrine observation",
            "CDC Haemophilus influenzae type b clinical/vaccine resources — epiglottitis as a potentially life-threatening invasive Hib manifestation and prevention through Hib vaccination",
        ],
    },
    "epiglottitis": {
        "recognize": (
            "Recognize epiglottitis/supraglottitis as an AIRWAY EMERGENCY caused by rapidly progressive inflammation of the epiglottis and surrounding supraglottic tissues. In children, high-risk findings are fever, severe throat pain/odynophagia, dysphagia, drooling, muffled or 'hot-potato' voice, tripod/sniffing posture, anxiety, stridor, and refusal to lie flat. The post-Hib-vaccine era changes epidemiology but not the emergency: H. influenzae type b is far less common in immunized populations, while non-type-b H. influenzae, streptococci, S. aureus and other pathogens can cause disease. Vaccination status modifies probability; it does not rule out epiglottitis."
        ),
        "localize": (
            "Localize obstruction to the SUPRAGLOTTIS and distinguish airway severity from diagnostic certainty. The epiglottis, aryepiglottic folds, arytenoids, and adjacent tissues may become markedly edematous, creating a small dynamic airway that can deteriorate with crying, instrumentation, sedation, or supine positioning. Flexible nasolaryngoscopy can confirm supraglottic edema in an appropriately monitored, stable patient with immediate rescue capability; it is not a mandatory bedside test in a distressed child. Distinguish bacterial tracheitis (toxic child with thick tracheal secretions/crusting), deep-neck infection, croup, foreign body, and anaphylaxis because their airway and source-control strategies differ."
        ),
        "workup": (
            "AIRWAY STABILITY DETERMINES THE WORKUP. In a distressed child, diagnosis is clinical enough to mobilize the airway team; do not delay for lateral neck film, CT, labs, or throat examination. If the patient is stable, lateral neck imaging may show an enlarged epiglottis ('thumbprint') but a negative film cannot safely exclude disease when the phenotype is concerning. After controlled airway establishment, obtain blood cultures and culture of supraglottic material if safely available. Check CBC/chemistry as clinically useful, but no laboratory value replaces repeated airway assessment. Review Hib immunization and immune risk, and consider public-health/infectious-disease implications when invasive H. influenzae is confirmed."
        ),
        "manage": (
            "Management has three priorities: CONTROL THE AIRWAY, TREAT INVASIVE INFECTION, THEN DE-ESCALATE SAFELY. Keep the child calm, upright, and with minimal unnecessary manipulation; summon pediatric anesthesia, ENT, PICU, respiratory therapy, and operating-room support early. Once the airway is secured, give IV third-generation cephalosporin therapy such as ceftriaxone/cefotaxime for invasive H. influenzae coverage, with additional anti-staphylococcal/MRSA coverage when severity, local epidemiology, culture data, or clinical context warrants it; tailor to cultures and susceptibilities. Provide ICU care, hydration/analgesia, and monitor for bacteremia or other invasive infection. Steroids are not the defining treatment and should never delay airway/antibiotic management."
        ),
        "operate": (
            "If airway intervention is needed, plan a CONTROLLED intubation in the operating room or similarly resourced environment with the most experienced pediatric airway operator, ENT present for rescue, difficult-airway equipment ready, and tracheotomy/cricothyrotomy capability appropriate to the child's age. Preserve spontaneous ventilation until the airway is secured when feasible; profound paralysis/sedation before the team can ventilate the patient can convert partial obstruction to complete obstruction. Expect edema to require a smaller-than-age-predicted endotracheal tube and secure it carefully. Reassess supraglottic edema after treatment and extubate only when the airway is clearly improved and the team is prepared for reintubation; an audible cuff leak can support but does not independently determine readiness."
        ),
        "teach": (
            "Chief/boards framework: EPIGLOTTITIS = DON'T AGITATE, DON'T FORCE THE THROAT EXAM, DON'T SEND AN UNSTABLE CHILD TO RADIOLOGY. Bring the airway team to the patient, maintain position of comfort/spontaneous ventilation, and secure the airway under controlled conditions before completing diagnostic workup. Then culture and treat as invasive bacterial disease. Know why the classic epidemiology changed—Hib conjugate vaccination—but also why the diagnosis still matters: other organisms remain, under-immunized patients remain at risk, and the consequence of missing progressive supraglottic obstruction is catastrophic. Keep this card distinct from 'Croup vs Epiglottitis': the comparison card asks WHICH BRANCH; this card teaches HOW TO MANAGE THE EPIGLOTTITIS BRANCH."
        ),
        "tags": ["epiglottitis", "supraglottitis", "Hib", "drooling", "tripod", "pediatric airway", "controlled intubation", "ceftriaxone", "airway emergency"],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — pediatric infectious upper-airway obstruction and operative airway management",
            "K.J. Lee's Essential Otolaryngology, 12e — epiglottitis/supraglottitis, pediatric stridor, and airway emergencies",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — pediatric airway emergencies and infectious management",
            "CDC Haemophilus influenzae type b resources — invasive Hib can present as epiglottitis and produce life-threatening airway obstruction; vaccination markedly reduces Hib disease",
            "Contemporary pediatric airway practice — controlled multidisciplinary airway management with minimal agitation and post-airway culture-directed antimicrobial therapy",
        ],
    },
}


def apply_pediatric_upper_airway_rebuild_v315(data_module, app_module=None):
    deep_modules = getattr(data_module, "DEEP_MODULES_V6", {}) or {}
    patched = []
    for _domain, modules in deep_modules.items():
        for module in modules or []:
            key = _norm(module.get("topic"))
            payload = PEDIATRIC_UPPER_AIRWAY_REBUILD_V315.get(key)
            if not payload:
                continue
            for field in FIELDS:
                module[field] = payload[field]
            module["tags"] = list(payload["tags"])
            module["source_basis"] = list(payload["source_basis"])
            module["source_grounded_v315"] = True
            module["semantic_role_v315"] = (
                "bedside croup-versus-epiglottitis discrimination and immediate treatment branch"
                if key == "croup vs epiglottitis"
                else "epiglottitis airway-control choreography, infectious treatment, and de-escalation"
            )
            patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
