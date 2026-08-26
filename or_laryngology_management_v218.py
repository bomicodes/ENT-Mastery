"""v21.8 laryngology/swallowing OR Tomorrow planning and postoperative priorities.

Adds high-confidence decision points for procedures whose technical choreography is
already specific but whose candidacy, approach, adjuncts, and postoperative risk
cannot be taught safely with a generic laryngology profile alone.
"""

TARGETS = [
    {
        "slug": "medialization-thyroplasty",
        "title_terms": ("medialization", "thyroplasty"),
        "setup": [
            "Before medialization thyroplasty, define the cause, duration and expected recovery of the vocal-fold immobility/paresis and document flexible laryngoscopy or stroboscopy, voice function, glottic-gap pattern and swallowing/aspiration symptoms. A large posterior gap or vertical height mismatch should prompt consideration of arytenoid adduction or another adjunct rather than assuming a type I implant alone will correct the entire insufficiency.",
            "Plan awake versus anesthetized framework surgery deliberately: when intraoperative phonation/endoscopic feedback is desired, ensure the patient can tolerate the awake technique; review anticoagulation/bleeding risk and airway reserve because postoperative edema or hematoma around a medialized larynx can become clinically important.",
        ],
        "postop": [
            "After framework surgery, new stridor, increasing work of breathing, rapidly expanding neck swelling or respiratory distress requires immediate airway and neck assessment for edema or hematoma rather than routine observation. New implant extrusion/migration, wound infection or marked deterioration in voice/swallow function also warrants prompt laryngologic evaluation.",
            "Reassess voice, vocal-fold position and swallowing after healing; persistent posterior insufficiency or height mismatch despite an appropriately positioned implant should trigger evaluation for arytenoid-position or other glottic-closure problems rather than reflexively increasing implant bulk.",
        ],
    },
    {
        "slug": "injection-laryngoplasty",
        "title_terms": ("injection", "laryngoplast"),
        "setup": [
            "Before injection laryngoplasty, define the cause and recovery potential of the glottic insufficiency, the size/location of the gap, voice demands and aspiration/cough impairment. When neural recovery remains possible, favor a temporary/shorter-duration augmentation strategy; when insufficiency is known to be permanent, material durability and whether framework surgery would better address a large/posterior gap should be considered explicitly.",
            "Choose office/awake versus operating-room injection based on patient tolerance, airway anatomy, visualization and need for concurrent endoscopy; early temporary augmentation is reasonable when aspiration risk, ineffective cough or major functional impairment makes prolonged observation undesirable.",
        ],
        "postop": [
            "After injection, dyspnea, stridor, progressive throat tightness, significant hematoma/bleeding or rapidly increasing edema is not expected overcorrection and requires urgent airway/laryngoscopic assessment. If injection was performed to improve aspiration, arrange earlier functional follow-up rather than relying only on subjective voice change.",
        ],
    },
    {
        "slug": "zenker-diverticulotomy",
        "title_terms": ("zenker",),
        "setup": [
            "Before treating a Zenker diverticulum, review the barium esophagram to confirm pouch size/configuration and the common wall/cricopharyngeal target, and assess dysphagia, regurgitation, aspiration/pneumonia, weight loss and nutritional risk. Select rigid endoscopic, flexible endoscopic/Z-POEM-type, or open treatment according to pouch anatomy, cervical/dental exposure, neck mobility, comorbidity and local expertise rather than assuming every pouch is suitable for one transoral platform.",
            "For rigid transoral treatment, anticipate exposure failure in patients with limited neck extension, unfavorable jaw/dentition or difficult hypopharyngeal exposure and have an alternate strategy before induction; the therapeutic endpoint is an adequate cricopharyngeal/septal myotomy, not simply shortening the visible pouch.",
        ],
        "postop": [
            "After Zenker treatment, fever, tachycardia, increasing neck/chest pain, cervical crepitus, dyspnea, sepsis or inability to handle secretions should trigger concern for pharyngoesophageal perforation or mediastinal infection rather than routine postoperative odynophagia. Diet advancement and need for contrast evaluation should follow the operative technique and intraoperative concern for leak.",
            "Recurrent dysphagia or regurgitation after initial improvement should prompt reassessment for residual/incomplete myotomy, recurrent pouch or another esophageal/swallowing disorder rather than assuming all recurrence requires the same repeat technique.",
        ],
    },
    {
        "slug": "cricopharyngeal-myotomy",
        "title_terms": ("cricopharyngeal", "myotomy"),
        "setup": [
            "Before cricopharyngeal myotomy, confirm that upper-esophageal-sphincter dysfunction is a meaningful driver of the dysphagia using the swallow history plus instrumental assessment such as modified barium swallow/FEES and esophagram, with manometry or additional esophageal testing when the physiology remains unclear. Generalized pharyngeal weakness, major neuromuscular disease or distal esophageal pathology may limit benefit and should not be mistaken for an isolated cricopharyngeal problem.",
            "Review for associated Zenker diverticulum, prior neck surgery/radiation, baseline vocal-fold function and aspiration burden because these findings change exposure, recurrent-laryngeal-nerve risk and the postoperative feeding/airway plan.",
        ],
        "postop": [
            "After open cricopharyngeal myotomy, new fever, tachycardia, neck/chest pain, crepitus, wound drainage or systemic toxicity raises concern for occult mucosal perforation/leak and requires urgent evaluation. New dysphonia should prompt vocal-fold examination for recurrent-laryngeal-nerve dysfunction, and diet advancement should follow the operative findings and local leak/swallow pathway.",
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


def apply_or_laryngology_management_v218(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        did_change = False
        op["setup"], c = _prepend_unique(op.get("setup"), target["setup"])
        did_change = did_change or c
        op["postop"], c = _prepend_unique(op.get("postop"), target["postop"])
        did_change = did_change or c
        op["laryngology_management_v218"] = True
        resolved.append(slug)
        if did_change:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
