"""v20.4-v21.1 procedure-specific physiology and safety priorities for OR Tomorrow.

Adds high-yield patient-state checks that materially affect perioperative risk and
postoperative disposition, plus high-consequence postoperative failure-mode reminders.
These are deliberately targeted rather than blanket boilerplate.
"""

TARGETED_SETUP = {
    "parathyroidectomy": [
        "Review renal function and vitamin D status in context of the calcium/PTH disorder; identify severe bone disease or high bone-turnover features that increase postoperative hypocalcemia/hungry-bone risk.",
        "Interpret intraoperative PTH in light of renal clearance: if the expected >50% fall is not yet achieved at the standard early time point, advanced renal dysfunction can slow PTH clearance and delay the decline. Follow the institution's ioPTH protocol and consider a later sample (commonly around 20 minutes) before assuming failure, while still evaluating for missed or multigland hyperfunction rather than attributing an inadequate fall to renal disease alone."
    ],
    "four-gland": [
        "Review renal function and vitamin D status in context of the calcium/PTH disorder; identify severe bone disease or high bone-turnover features that increase postoperative hypocalcemia/hungry-bone risk.",
        "Interpret intraoperative PTH in light of renal clearance: if the expected >50% fall is not yet achieved at the standard early time point, advanced renal dysfunction can slow PTH clearance and delay the decline. Follow the institution's ioPTH protocol and consider a later sample (commonly around 20 minutes) before assuming failure, while still evaluating for residual hyperfunctioning tissue or the expected multigland disease pattern rather than attributing an inadequate fall to renal disease alone."
    ],
    "reop-parathyroid": [
        "Review renal function, vitamin D status, prior pathology/operative records and the biochemical pattern; define whether persistent/recurrent disease and high postoperative hypocalcemia risk are present before re-exploration.",
        "Interpret intraoperative PTH in light of renal clearance: an incomplete early >50% decline can reflect slower clearance in advanced renal dysfunction, so use protocol-consistent delayed sampling when appropriate before extending a scarred reoperative exploration. Renal dysfunction is not an automatic explanation for a failed criterion—persistent/missed or multigland hyperfunction still must be considered."
    ],
    "tonsillectomy": [
        "Define physiologic airway risk before surgery: review OSA severity and sleep-study data when available, age, obesity, craniofacial/neuromuscular disease, cardiopulmonary comorbidity and any prior postoperative respiratory events; use these factors to plan postoperative disposition."
    ],
    "tonsillectomy-adenoidectomy": [
        "Define physiologic airway risk before surgery: review OSA severity and sleep-study data when available, age, obesity, craniofacial/neuromuscular disease, cardiopulmonary comorbidity and any prior postoperative respiratory events; use these factors to plan postoperative disposition."
    ],
    "hypoglossal-stimulator": [
        "Confirm current OSA physiology and candidacy: review the diagnostic sleep study, central-versus-obstructive event burden, PAP intolerance, body habitus and DISE/anatomic findings rather than relying on anatomy alone."
    ],
    "free-flap-basics": [
        "Assess physiologic reserve before major reconstruction: screen for recent weight loss/malnutrition and anemia, review cardiopulmonary status and functional capacity, and identify tobacco/alcohol use or other modifiable factors that affect wound healing and flap recovery.",
        "For lower-extremity donor sites or patients with vascular disease, assess donor-site perfusion and relevant peripheral vascular history; also optimize diabetes, renal dysfunction, anemia and nutrition because these affect wound and flap recovery."
    ],
    "oral-composite": [
        "Before major ablative head-and-neck surgery, assess nutritional status/recent weight loss, anemia, cardiopulmonary reserve, aspiration risk and tobacco/alcohol use; coordinate airway and feeding access with the reconstructive plan."
    ],
    "total-laryngectomy": [
        "Assess preoperative nutritional status/recent weight loss, anemia and cardiopulmonary reserve; document baseline swallowing/pulmonary function and tobacco/alcohol use because these directly influence fistula, pulmonary and rehabilitation risk."
    ],
    "cochlear-implant": [
        "Confirm implant candidacy from current audiology and aided speech testing, review imaging for cochlear/nerve anatomy and prior ear disease, and verify age-appropriate pneumococcal vaccination status before implantation."
    ],
    "tracheal-resection": [
        "Quantify airway physiology as well as anatomy: review stenosis length/location and prior airway interventions, assess pulmonary reserve and active respiratory infection, and identify prior radiation, chronic steroid exposure or other factors that may impair anastomotic healing."
    ],
    "peds-ltr": [
        "Before reconstruction, review pulmonary status, aspiration/swallow history, reflux control, tracheostomy dependence/secretions and recent airway infection; these factors influence graft healing, postoperative intubation strategy and ICU planning."
    ],
}

TARGETED_POSTOP = {
    "tracheal-resection": [
        "Protect the fresh tracheal anastomosis: maintain the planned neck-flexion strategy, avoid unnecessary positive-pressure ventilation/coughing strain, and treat new subcutaneous emphysema, air leak, respiratory distress or wound crepitus as possible anastomotic failure requiring urgent surgical review."
    ],
    "peds-ltr": [
        "Make the postoperative airway plan explicit: tube/stent size and position, sedation/extubation timing, secretion clearance and criteria for urgent endoscopy if ventilation worsens or the reconstructed airway is threatened."
    ],
    "total-laryngectomy": [
        "A total-laryngectomy patient is a permanent neck breather: all oxygenation, bag-mask ventilation and emergency intubation must occur through the tracheal stoma; oral or nasal intubation cannot ventilate the lungs."
    ],
    "neck-dissection": [
        "After low-neck dissection, inspect drain character and output for chyle leak—especially on the left and after enteral feeding—and document shoulder function/CN XI status early so new deficits are recognized rather than attributed to routine postoperative pain."
    ],
    "free-flap-basics": [
        "Treat a new change in flap color, turgor, temperature, capillary refill or Doppler signal as time-critical vascular compromise; venous congestion or arterial insufficiency requires immediate flap-team assessment and a low threshold for operative exploration."
    ],
    "cochlear-implant": [
        "Document immediate facial-nerve function and vestibular symptoms; new facial weakness, severe/progressive vertigo, CSF-like drainage, meningitic symptoms or wound/device infection warrants urgent otologic evaluation."
    ],
    "tonsillectomy": [
        "Treat fresh or recurrent oral bleeding, repeated swallowing/hematemesis, tachycardia, pallor or hemodynamic change as possible post-tonsillectomy hemorrhage; secure airway/resuscitation resources and obtain urgent ENT assessment rather than relying on a normal-appearing momentary oropharyngeal exam."
    ],
    "tonsillectomy-adenoidectomy": [
        "Treat fresh or recurrent oral/nasal bleeding, repeated swallowing/hematemesis, tachycardia, pallor or hemodynamic change as possible post-tonsillectomy/adenoid hemorrhage; secure airway/resuscitation resources and obtain urgent ENT assessment."
    ],
    "button-battery": [
        "After esophageal button-battery removal, ongoing injury can progress despite extraction: new hematemesis, sentinel bleeding, chest pain, fever, respiratory symptoms or neurologic change raises concern for delayed perforation, tracheoesophageal fistula or aorto-esophageal fistula and requires emergency multidisciplinary evaluation."
    ],
    "esophageal-fb": [
        "After esophageal foreign-body extraction, escalating neck/chest pain, fever, crepitus, tachycardia, dyspnea or inability to handle secretions should trigger concern for occult esophageal perforation rather than routine post-instrumentation discomfort."
    ],
    "pharyngocutaneous-fistula": [
        "In a pharyngocutaneous fistula or irradiated open neck, sentinel hemorrhage or new bleeding near an exposed carotid is a carotid-blowout warning; activate emergency airway/hemorrhage control and vascular/interventional support rather than performing blind bedside probing or packing against the vessel."
    ],
    "translabyrinthine-skull-base": [
        "After translabyrinthine skull-base surgery, clear wound/nasal drainage, enlarging pseudomeningocele, meningitic symptoms, worsening facial weakness or new lower-cranial-nerve dysfunction requires prompt skull-base evaluation for CSF leak or neurologic complication."
    ],
    "retrosigmoid-skull-base": [
        "After retrosigmoid skull-base surgery, new severe headache, declining mental status, focal neurologic deficit, lower-cranial-nerve dysfunction/aspiration, wound CSF leak or pseudomeningocele warrants urgent neurologic and skull-base reassessment."
    ],
    "middle-fossa-skull-base": [
        "After middle-fossa skull-base surgery, new aphasia/confusion, focal neurologic deficit, seizure, worsening facial function or CSF-like otorrhea/rhinorrhea should prompt urgent evaluation for temporal-lobe, hematoma or CSF-leak complication."
    ],
}


def _prepend_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:48].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_preop_physiology_v204(registry):
    changed = []
    slugs = set(TARGETED_SETUP) | set(TARGETED_POSTOP)
    for slug in sorted(slugs):
        op = registry.get(slug)
        if not op:
            continue
        did_change = False
        if slug in TARGETED_SETUP:
            op["setup"], section_changed = _prepend_unique(op.get("setup"), TARGETED_SETUP[slug])
            did_change = did_change or section_changed
        if slug in TARGETED_POSTOP:
            op["postop"], section_changed = _prepend_unique(op.get("postop"), TARGETED_POSTOP[slug])
            did_change = did_change or section_changed
        if did_change:
            changed.append(slug)
        op["preop_physiology_v204"] = True
        if slug in TARGETED_POSTOP:
            op["safety_priorities_v208"] = True
    return {"changed": changed, "count": len(changed), "targets": len(slugs)}
