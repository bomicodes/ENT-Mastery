"""v23.5 major oncologic-resection OR Tomorrow planning and postoperative rescue.

Adds high-confidence perioperative decision points for oral composite resection and
conservation laryngectomy. Their operative choreography and procedure-specific anatomy
remain in the existing reviewed layers.
"""

TARGETS = [
    {
        "slug": "oral-composite",
        "title_terms": ("oral", "composite"),
        "setup": [
            "Before oral composite resection, map the primary in three dimensions across tongue/floor of mouth, mandible, adjacent oropharynx, skin and neurovascular structures and decide whether mandibular management is marginal, segmental or unnecessary based on true bone involvement rather than proximity alone. Review dental status and occlusion when mandibular resection or fixation is possible, and define the neck-dissection extent from nodal risk and imaging.",
            "Plan reconstruction from the anticipated functional defect before incision: determine the need for thin pliable lining versus bulk, mandibular continuity/support, oral competence and separation of the oral cavity from neck; coordinate recipient vessels, donor site, tracheostomy strategy and enteral access with the ablative plan rather than making these decisions after the specimen is removed.",
            "Document baseline speech, tongue mobility, swallowing/aspiration, nutrition and pulmonary reserve. Large tongue-base/floor-of-mouth resections, prior radiation, poor nutrition or major composite defects should lower the threshold for deliberate postoperative airway protection and early speech/swallow/nutrition planning.",
        ],
        "postop": [
            "After oral composite resection, airway obstruction from tongue/floor-of-mouth edema, hematoma, bulky reconstruction or secretion burden is time-critical. Progressive swelling, stridor, inability to handle secretions or respiratory distress requires immediate airway assessment and activation of the established tracheostomy/intubation rescue plan rather than routine observation.",
            "Monitor the oral-neck closure and drains for salivary leak or fistula. Increasing neck erythema/swelling, salivary-appearing drainage, wound breakdown, fever or exposed hardware/vessels should prompt cessation of unsafe oral intake, wound-source evaluation, nutritional support and early reconstructive/oncologic involvement because persistent contamination can threaten fixation, flap tissue and major vessels.",
            "Reassess tongue mobility, lower-cranial-nerve function, oral competence, occlusion when the mandible was manipulated, and objective swallowing safety before advancing diet. Persistent aspiration, severe dysphagia or speech dysfunction should trigger targeted rehabilitation and structural/neurologic reassessment rather than assuming recovery will follow wound healing alone.",
        ],
    },
    {
        "slug": "conservation-laryngectomy",
        "title_terms": ("conservation", "laryngectomy"),
        "setup": [
            "Before conservation laryngectomy, confirm that the tumor can be removed while preserving the functional laryngeal unit required by the selected operation. Review arytenoid/cricoarytenoid-unit mobility, paraglottic and pre-epiglottic extension, cartilage involvement, subglottic/hypopharyngeal extent and margins; oncologic or functional findings that violate the operation's prerequisites should prompt a different resection rather than stretching a conservation indication.",
            "Assess whether the patient can tolerate the expected postoperative swallowing burden: document baseline pulmonary reserve, cough, aspiration history, nutrition and neurologic function. Significant pulmonary compromise or inability to protect the airway can make an anatomically feasible conservation operation functionally unsafe.",
            "Make the temporary airway, feeding and rehabilitation pathway explicit before surgery, including tracheostomy and enteral access when required, expected aspiration during retraining, speech/swallow therapy milestones and the criteria for eventual decannulation rather than treating decannulation as automatic after wound healing.",
        ],
        "postop": [
            "After conservation laryngectomy, airway edema, secretion retention, aspiration and pneumonia are central early risks. Worsening work of breathing, repeated desaturation, inability to clear secretions or new pulmonary decline requires airway and swallowing reassessment rather than simply prolonging routine tracheostomy care.",
            "Advance swallowing rehabilitation according to demonstrated airway protection and reconstruction healing, not time alone. Persistent severe aspiration, recurrent pneumonia or inability to progress despite therapy should trigger endoscopic/functional evaluation for structural obstruction, poor neoglottic closure, impaired cricoarytenoid-unit function or a reconstruction problem.",
            "Neck swelling, fever, wound drainage, cervical crepitus or salivary contamination raises concern for pharyngeal leak or reconstruction dehiscence and requires prompt evaluation. Decannulation should occur only after the airway is stable, secretions are manageable and pulmonary protection is adequate.",
        ],
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
        marker = text[:64].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_major_oncologic_resection_management_v235(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["major_oncologic_resection_management_v235"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
