"""v29.8 — source-grounded adult vs pediatric PSG Concept Hub rebuild.

Separates ADULT PSG INTERPRETATION (adult respiratory-event burden, phenotype, and
management implications) from PEDIATRIC PSG INTERPRETATION (age-specific obstructive
indices, gas-exchange burden, and perioperative pediatric ENT decision-making).
"""

import re

DOMAIN = "Sleep Surgery"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


SLEEP_PSG_REBUILD_V298 = {
    "adult psg interpretation": {
        "recognize": (
            "Read an ADULT polysomnogram as an integrated physiology study, not as a single AHI. First confirm total sleep time, sleep efficiency and stage distribution; then identify obstructive apneas/hypopneas, central and mixed events, respiratory-effort related arousals when reported, oxygen desaturation, snoring/flow limitation, arousal burden, body position, and REM dependence. An obstructive event has persistent respiratory effort despite reduced/absent airflow; a central event lacks respiratory effort; mixed events change physiology within the same event. The ENT resident should be able to distinguish obstructive disease that may benefit from airway-directed therapy from central-predominant or hypoventilation physiology that requires a different pathway."
        ),
        "localize": (
            "Phenotype WHERE and WHEN the adult disease expresses itself physiologically, while remembering that PSG does not anatomically localize the collapse site. Compare supine versus nonsupine AHI, REM versus non-REM AHI, obstructive versus central event burden, oxygen nadir and time below clinically relevant saturation, and whether events cluster around stage or position. A markedly positional study may support positional strategies; REM-predominant disease may be underestimated if REM time is sparse; central-predominant events, periodic breathing, or sustained hypoxemia out of proportion to discrete obstruction should redirect the differential toward cardiopulmonary, medication, neurologic, altitude-related, or hypoventilation causes rather than palate/tongue-base surgery."
        ),
        "workup": (
            "Use a disciplined read sequence: recording quality and total sleep time -> sleep architecture -> respiratory event table -> AHI/RDI and event type -> oxygenation -> position/REM effects -> arousals/limb movements/cardiac observations -> impression. Common adult OSA severity conventions use an AHI/RDI of about 5 to <15 events/hour as mild, 15 to 30 as moderate, and >30 as severe, but the number must be interpreted with symptoms, comorbidity, oxygen burden, and study quality. Check whether little supine or REM sleep could falsely reassure, whether short total sleep time makes indices unstable, and whether a high central apnea burden means the label 'OSA' is incomplete."
        ),
        "manage": (
            "Translate the adult PSG into a treatment problem rather than treating the AHI in isolation. Obstructive-predominant disease may lead to PAP, oral-appliance, weight-directed, positional, nasal, or site-directed surgical discussions according to severity, anatomy, preferences, and prior therapy. Central-predominant disease or suspected hypoventilation should prompt etiologic sleep/medical evaluation rather than reflexive upper-airway surgery. When PAP appears ineffective, distinguish persistent obstruction, leak/poor adherence, treatment-emergent central events, and inadequate titration. Repeat objective testing is appropriate when treatment response, recurrent symptoms, major weight change, or a high-stakes surgical decision cannot be judged clinically."
        ),
        "operate": (
            "For the sleep surgeon, the PSG defines DISEASE PHYSIOLOGY and risk but not the operative target. Do not infer 'palatal collapse' from a high AHI. Combine PSG with awake anatomy and, when useful, DISE to decide whether obstruction is retropalatal, lateral-wall, tongue-base, epiglottic, skeletal, or multilevel. Severe oxygen desaturation, substantial cardiopulmonary disease, opioid sensitivity, or very severe OSA should influence postoperative monitoring and analgesic strategy. A central or sustained hypoventilation phenotype should make you stop before proposing a purely anatomic operation unless a separate obstructive component has been demonstrated."
        ),
        "teach": (
            "Chief/boards distinction: ADULT PSG INTERPRETATION = quantify adult respiratory-event burden, classify obstructive versus central physiology, and decide what the study can and cannot tell you. Adult severity commonly starts at approximately 5 events/hour, unlike pediatric practice. AHI is a rate, not an anatomic map and not the whole disease: always inspect event type, oxygenation, REM/position sampling, and total sleep time. An adult AHI of 3 and a pediatric obstructive AHI of 3 do NOT carry the same interpretation."
        ),
        "tags": [
            "adult PSG", "polysomnography", "AHI", "RDI", "obstructive apnea", "central apnea",
            "mixed apnea", "REM-predominant OSA", "positional OSA", "oxygen nadir", "sleep architecture"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — adult sleep-disordered breathing evaluation, PSG interpretation, OSA phenotyping, and surgical decision-making",
            "K.J. Lee's Essential Otolaryngology, 12e — adult OSA diagnosis, polysomnography, and treatment selection",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — sleep-study interpretation and OSA management pearls",
            "American Academy of Sleep Medicine Manual for the Scoring of Sleep and Associated Events, Version 3 — standard respiratory-event, arousal, sleep-stage, and PSG scoring framework",
            "American Academy of Sleep Medicine adult OSA evaluation/management guidance — adult severity conventions and integration of objective testing with clinical assessment",
        ],
    },
    "pediatric psg interpretation": {
        "recognize": (
            "Read a PEDIATRIC polysomnogram with pediatric thresholds and pediatric physiology. Children can have clinically meaningful obstructive sleep apnea at event rates that would look trivial by adult criteria. Identify obstructive apnea/hypopnea, paradoxical thoracoabdominal effort, snoring/flow limitation, arousals, oxygen desaturation, REM clustering, and sustained carbon-dioxide elevation/obstructive hypoventilation. Separate obstructive from central events, but remember that central event interpretation is age- and context-dependent. The ENT question is often not simply 'is the AHI high?' but whether adenotonsillar or multilevel obstruction is causing clinically important sleep, gas-exchange, behavioral, growth, cardiovascular, or perioperative risk."
        ),
        "localize": (
            "Phenotype the child's study as obstructive-event dominant, obstructive-hypoventilation/gas-exchange dominant, central-predominant, REM-predominant, or mixed. Review the obstructive AHI/OAHI when supplied, oxygen nadir and desaturation pattern, carbon-dioxide burden, arousal pattern, and whether REM sleep was adequately sampled. PSG still does NOT identify the exact anatomic collapse site: adenotonsillar hypertrophy is common, but obesity, craniofacial restriction, Down syndrome, neuromuscular weakness, lingual tonsil/tongue-base obstruction, laryngomalacia/epiglottic collapse, and nasal obstruction can create persistent or multilevel pediatric disease."
        ),
        "workup": (
            "Use the same disciplined PSG sequence as in adults but apply pediatric interpretation: recording quality/sleep time -> sleep architecture -> obstructive and central respiratory events -> OAHI/AHI -> oxygenation -> CO2/hypoventilation -> REM/position effects -> arousals and other observations. Common clinical conventions often describe pediatric OSA around OAHI 1 to <5 as mild, 5 to <10 as moderate, and >=10 as severe, but cut points vary across literature and should not replace symptoms, comorbidity, gas-exchange abnormalities, or local sleep-lab definitions. Before tonsillectomy for obstructive sleep-disordered breathing, AAO-HNS recommends PSG particularly for children under 2 years or with obesity, Down syndrome, craniofacial abnormality, neuromuscular disorder, sickle cell disease, or mucopolysaccharidosis, and when the need for surgery or exam/history concordance is uncertain."
        ),
        "manage": (
            "Translate pediatric PSG findings into the child's actual treatment pathway. Adenotonsillar hypertrophy with PSG-confirmed OSA commonly supports adenotonsillectomy, while obesity, syndromic/craniofacial disease, neuromuscular weakness, small tonsils, or persistent OSA after surgery should trigger a broader multilevel plan and may require PAP, weight-directed therapy, anti-inflammatory nasal therapy in selected cases, DISE-directed surgery, or other site-specific treatment. Counsel that OSA may persist after adenotonsillectomy, especially in higher-risk phenotypes. Do not dismiss a symptomatic child because the numeric AHI is below adult diagnostic thresholds, and do not attribute sustained CO2 abnormalities to simple adenotonsillar OSA without considering hypoventilation physiology and comorbidity."
        ),
        "operate": (
            "Use the pediatric PSG to plan perioperative risk as well as indication. AAO-HNS recommends overnight inpatient monitoring after tonsillectomy for children younger than 3 years or with severe OSA, defined in that guideline as AHI >=10 obstructive events/hour, oxygen saturation nadir <80%, or both. Severe desaturation, major comorbidity, craniofacial/syndromic disease, neuromuscular weakness, and very young age should increase caution with airway observation and opioid-sparing analgesia. Persistent OSA after adenotonsillectomy is a new localization problem: reassess anatomy and physiology rather than repeating generic treatment, and use DISE or targeted imaging selectively when it will change the next intervention."
        ),
        "teach": (
            "Chief/boards distinction: PEDIATRIC PSG INTERPRETATION = low-threshold obstructive disease + gas-exchange physiology + pediatric perioperative implications. Never paste adult AHI cutoffs onto a child. An OAHI around 3 events/hour can represent meaningful pediatric OSA, and CO2 burden or major desaturation can matter even when event counts are not dramatic. For tonsillectomy planning, know the AAO-HNS high-risk PSG referral groups and the overnight-monitoring trigger of age <3 years or severe OSA (AHI >=10, nadir <80%, or both). Pediatric PSG informs risk and disease severity; it still does not tell you the exact level of airway collapse."
        ),
        "tags": [
            "pediatric PSG", "pediatric OSA", "OAHI", "adenotonsillectomy", "obstructive hypoventilation",
            "carbon dioxide", "oxygen nadir", "Down syndrome", "persistent pediatric OSA", "post-tonsillectomy monitoring"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — pediatric OSA, polysomnography, adenotonsillectomy, and persistent disease",
            "K.J. Lee's Essential Otolaryngology, 12e — pediatric sleep-disordered breathing and PSG interpretation",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — pediatric OSA workup, operative indications, and perioperative pearls",
            "American Academy of Sleep Medicine Manual for the Scoring of Sleep and Associated Events, Version 3 — pediatric respiratory-event and hypoventilation scoring framework",
            "AAO-HNSF Clinical Practice Guideline: Tonsillectomy in Children (Update), 2019 — indications for preoperative PSG and overnight monitoring after tonsillectomy",
            "American Thoracic Society clinical practice guideline on management of persistent post-adenotonsillectomy OSA in children — persistent pediatric OSA evaluation and treatment framework",
        ],
    },
}


def apply_sleep_psg_rebuild_v298(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = SLEEP_PSG_REBUILD_V298.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v298"] = True
        module["semantic_role_v298"] = (
            "adult PSG respiratory physiology, severity, and treatment implications"
            if key == "adult psg interpretation"
            else "pediatric PSG thresholds, gas exchange, and perioperative ENT decision-making"
        )
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"patched": patched, "count": len(patched)}
