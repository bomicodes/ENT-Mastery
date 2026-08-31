"""v23.14 OR Tomorrow high-risk end-to-end management review.

Closes high-yield perioperative gaps identified by the full live OR registry audit.
Existing procedure-specific operative sequences, anatomy, and danger structures remain
authoritative and are not replaced. Later reviewed rhinology management is chained here
to keep the runtime mutation path atomic.
"""

from or_rhinology_management_v2315 import apply_or_rhinology_management_v2315

LARYNGECTOMY_SOURCES = [
    "Cummings Otolaryngology—Head and Neck Surgery, 7th ed.",
    "K. J. Lee's Essential Otolaryngology—Head and Neck Surgery, 12th ed.",
    "Pasha & Golub, Otolaryngology—Head and Neck Surgery Clinical Reference Guide, 6th ed.",
    "National Tracheostomy Safety Project adult laryngectomy emergency algorithm (current algorithm reviewed fit for purpose through 2026)",
    "IFOS Consensus on Prevention, Diagnosis, and Management of Pharyngocutaneous Fistula After Total Laryngectomy (2026)",
]

TARGETS = [
    {
        "slug": "tors",
        "title_terms": ("tors",),
        "setup": [
            "Before TORS, define the primary site, laterality, depth and relationship to the glossotonsillar sulcus, tongue base, vallecula, parapharyngeal space and major vessels on examination and imaging; confirm whether the intent is diagnostic, primary oncologic resection, or salvage. Review mouth opening, dentition, cervical mobility and anticipated line-of-sight because inadequate exposure can change the operation before docking, and coordinate the neck plan when nodal surgery or prophylactic control of external-carotid branches is being considered.",
            "Plan the postoperative airway and hemorrhage strategy before resection. Large tongue-base resections, significant edema risk, difficult exposure, anticoagulation/coagulopathy, prior radiation and limited pulmonary reserve can change extubation, observation and feeding decisions; counsel that delayed oropharyngeal hemorrhage can be abrupt and life-threatening even after an initially uncomplicated recovery.",
        ],
        "postop": [
            "After TORS, airway and bleeding surveillance outrank routine pain control. New brisk oral bleeding, repeated swallowing of blood, hematemesis, tachycardia, hypotension, hemoptysis or an enlarging neck/oropharyngeal collection should be treated as a hemorrhage emergency with immediate airway/anesthesia and operative-control planning rather than bedside observation alone.",
            "Assess swallowing and aspiration risk according to resection extent before advancing intake. Progressive tongue-base edema, stridor, increasing work of breathing, inability to manage secretions, aspiration, dehydration or pneumonia should trigger reassessment of airway protection and feeding rather than assuming these are expected postoperative symptoms.",
        ],
        "marker": "tors_management_v2314",
    },
    {
        "slug": "tracheostomy",
        "title_terms": ("tracheostomy",),
        "setup": [
            "Before surgical tracheostomy, define why the airway is needed, whether the upper airway remains usable for rescue, and whether anatomy makes a standard cervical tracheostomy hazardous: prior neck surgery/radiation, obesity or short neck, thyroid enlargement, distorted trachea, high-riding innominate artery, cervical spine restrictions, or need for unusually low placement. Confirm the intended tube type/size, cuff requirement, stay-suture or maturation strategy if used, and the immediate rescue plan for accidental decannulation.",
            "Coordinate ventilation with anesthesia before entering the trachea and make the first postoperative tube-change plan explicit. A fresh tract is not a mature airway: the team caring for the patient must know the date, tracheal level, tube size, whether the upper airway is intubatable, and whom to call if the tube dislodges.",
        ],
        "postop": [
            "A fresh-tracheostomy patient with accidental decannulation, inability to pass suction, rapidly rising airway pressures, loss of end-tidal CO2 or respiratory distress requires immediate airway assessment. Do not repeatedly force a tube through an immature tract or persist with blind reinsertion that can create a false passage; oxygenate/ventilate by the safest available route and obtain experienced airway help urgently.",
            "Sentinel bleeding from a tracheostomy—especially new pulsatile or recurrent bleeding days to weeks after placement—must raise concern for tracheo-innominate fistula until proven otherwise. Escalate emergently for airway and hemorrhage control; do not dismiss a small warning bleed as routine stomal irritation. Also assess early subcutaneous emphysema, pneumothorax, posterior-wall injury, tube obstruction and cuff-related ventilation problems when the clinical course is not routine.",
        ],
        "marker": "tracheostomy_management_v2314",
    },
    {
        "slug": "csf-nasoseptal",
        "title_terms": ("csf", "nasoseptal"),
        "setup": [
            "Before endoscopic CSF-leak repair, localize the suspected defect and determine whether this is spontaneous, traumatic, iatrogenic or tumor-related; review thin-cut CT and, when indicated, MRI for encephalocele, multifocal disease, prior repair and anatomy that changes the endonasal corridor. In spontaneous leaks, consider the broader intracranial-pressure context because successful closure without addressing clinically relevant elevated-pressure physiology can increase recurrence risk.",
            "Plan reconstruction before harvesting the nasoseptal flap: defect size/location, expected flow, prior septal surgery or posterior septal artery injury, availability of vascularized tissue, multilayer graft strategy and backup options should be known before the skull-base defect is enlarged. Coordinate perioperative antibiotics, lumbar-drain use and postoperative pressure precautions according to the actual defect and institutional protocol rather than applying them automatically to every leak.",
        ],
        "postop": [
            "After skull-base repair, persistent or recurrent unilateral clear rhinorrhea, salty drainage, severe positional headache, meningismus, fever, photophobia, altered mental status or neurologic change should prompt urgent evaluation for recurrent CSF leak or intracranial infection. A normal-appearing nasal cavity or absence of a continuous drip does not by itself exclude an intermittent postoperative leak.",
            "New orbital pain/swelling, visual change, significant epistaxis, progressive pneumocephalus symptoms or declining mental status is not routine postoperative congestion. Reassess the reconstruction, sinonasal/skull-base complications and need for imaging or operative exploration based on the presentation; protect the flap from unnecessary instrumentation during early healing.",
        ],
        "marker": "csf_nasoseptal_management_v2314",
    },
    {
        "slug": "total-laryngectomy",
        "title_terms": ("total", "laryngectomy"),
        "setup": [
            "Treat total laryngectomy as creation of a permanently separated airway, not as a tracheostomy. Once the trachea is divided, ventilation is through the distal trachea/stoma, and after reconstruction the mouth and nose no longer communicate with the lungs. Make that neck-breather anatomy explicit in the operative handoff, bedside signage, oxygen plan and emergency-airway plan so a future responder does not waste critical time attempting oral or nasal intubation.",
            "Before closure, identify fistula risk and plan the pharyngeal reconstruction accordingly. Prior radiation/chemoradiation, salvage surgery, poor nutrition, hypothyroidism, diabetes, extensive pharyngeal resection and tenuous tissue should lower the threshold for deliberate vascularized-tissue reinforcement when appropriate. Optimize nutrition and define postoperative enteral-feeding and fistula-surveillance plans rather than relying on a fixed oral-feeding date for every patient.",
        ],
        "postop": [
            "In a total-laryngectomy patient with respiratory distress, direct oxygen to the stoma immediately and assess the stoma/airway for removable obstruction, crust, mucus plug, displaced appliance or tube, and inability to pass suction. If ventilation is required, ventilate through the stoma and place a cuffed tracheal tube through the stoma when necessary and feasible. Oral or nasal mask ventilation/intubation cannot ventilate the lungs after a completed total laryngectomy because the upper airway is anatomically disconnected from the trachea.",
            "Suspect pharyngocutaneous fistula when salivary drainage appears in the neck or drain, the wound becomes erythematous/swollen or breaks down, fever/infection develops, or swallowing/feeding is followed by concerning cervical leakage. Stop oral intake when a leak is suspected, maintain enteral nutritional support by the planned route, obtain drainage/source control and assess the extent of tissue breakdown. Persistent or complex fistula, especially in irradiated tissue, may require operative revision with vascularized tissue rather than indefinite local care.",
            "Treat exposed great vessels, sentinel bleeding or brisk hemorrhage in a fistula-infected laryngectomy wound as a carotid-blowout danger state. Escalate immediately for hemorrhage control and airway/stoma management; do not probe, debride or pack a friable wound casually when the carotid may be exposed.",
        ],
        "marker": "total_laryngectomy_rescue_v2314",
        "sources": LARYNGECTOMY_SOURCES,
    },
    {
        "slug": "vestibular-schwannoma",
        "title_terms": ("vestibular", "schwannoma"),
        "setup": [
            "Before vestibular-schwannoma surgery, choose the corridor from the patient's actual hearing, tumor size/location, internal-auditory-canal anatomy, brainstem/CPA relationships and goals—not from tumor diagnosis alone. Serviceable-hearing preservation may favor a middle-fossa or retrosigmoid strategy in selected tumors, whereas a translabyrinthine approach intentionally sacrifices residual hearing; document baseline audiometry, facial function and vestibular symptoms so expected tradeoffs are explicit.",
            "Review imaging for fundal extension, cochlear/vestibular anatomy, facial-nerve displacement clues, vascular relationships and hydrocephalus, and coordinate neuromonitoring and CSF-closure strategy before incision. Large tumors, poor baseline balance, contralateral hearing impairment, lower-cranial-nerve symptoms or major medical frailty should influence counseling, extent-of-resection goals and postoperative level of care.",
        ],
        "postop": [
            "After vestibular-schwannoma resection, document facial function, hearing status when preservation was intended, vestibular findings and lower-cranial-nerve/swallow function when relevant. New facial weakness, dysphagia/aspiration, worsening headache, somnolence, focal neurologic deficit or disproportionate nausea/vomiting should trigger evaluation for cranial-nerve injury, posterior-fossa complication, hemorrhage or hydrocephalus rather than being attributed automatically to routine postoperative vertigo.",
            "Clear wound or nasal/ear drainage, enlarging pseudomeningocele, fever/meningismus, persistent CSF leak or wound breakdown requires prompt skull-base evaluation. Long-term follow-up should address residual/recurrent tumor, facial rehabilitation, hearing rehabilitation, chronic imbalance and headache according to the approach and extent of resection.",
        ],
        "marker": "vestibular_schwannoma_management_v2314",
    },
]


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
        marker = text[:72].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def _merge_sources(values, additions):
    out = list(values or [])
    seen = {str(x).strip().lower() for x in out}
    changed = False
    for source in additions or []:
        key = str(source).strip().lower()
        if key and key not in seen:
            out.append(source)
            seen.add(key)
            changed = True
    return out, changed


def apply_or_high_risk_management_v2314(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        op["sources"], c3 = _merge_sources(op.get("sources"), target.get("sources", []))
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2 or c3:
            changed.append(slug)
    v2315 = apply_or_rhinology_management_v2315(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v2315": v2315}
