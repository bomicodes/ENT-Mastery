"""v20.4 procedure-specific preoperative physiology/optimization for OR Tomorrow.

Adds high-yield patient-state checks that materially affect perioperative risk and
postoperative disposition. These are deliberately targeted rather than a blanket
'order labs' layer.
"""

TARGETED_SETUP = {
    "parathyroidectomy": [
        "Review renal function and vitamin D status in context of the calcium/PTH disorder; identify severe bone disease or high bone-turnover features that increase postoperative hypocalcemia/hungry-bone risk."
    ],
    "four-gland": [
        "Review renal function and vitamin D status in context of the calcium/PTH disorder; identify severe bone disease or high bone-turnover features that increase postoperative hypocalcemia/hungry-bone risk."
    ],
    "reop-parathyroid": [
        "Review renal function, vitamin D status, prior pathology/operative records and the biochemical pattern; define whether persistent/recurrent disease and high postoperative hypocalcemia risk are present before re-exploration."
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
        "Assess physiologic reserve before major reconstruction: screen for recent weight loss/malnutrition and anemia, review cardiopulmonary status and functional capacity, and identify tobacco/alcohol use or other modifiable factors that affect wound healing and flap recovery."
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
}


def apply_or_preop_physiology_v204(registry):
    changed = []
    for slug, additions in TARGETED_SETUP.items():
        op = registry.get(slug)
        if not op:
            continue
        setup = list(op.get("setup") or [])
        did_change = False
        for text in reversed(additions):
            marker = text[:48].lower()
            if not any(marker in str(x).lower() for x in setup):
                setup.insert(0, text)
                did_change = True
        if did_change:
            op["setup"] = setup
            changed.append(slug)
        op["preop_physiology_v204"] = True
    return {"changed": changed, "count": len(changed), "targets": len(TARGETED_SETUP)}
