"""v23.20 general/emergency ENT OR Tomorrow management review.

Adds procedure-specific preoperative decision-making and postoperative rescue to six
remaining general/emergency endoscopic and neck-infection modules. Existing v20.x
button-battery, esophageal-perforation and airway safety warnings are intentionally
preserved and complemented rather than duplicated. The v23.21 specialty review is
chained through this tail to preserve one ordered runtime mutation path.
"""

from or_specialty_management_v2321 import apply_or_specialty_management_v2321

TARGETS = [
    {
        "slug": "button-battery",
        "title_terms": ("button", "battery"),
        "setup": [
            "An esophageal button battery is an emergency: confirm location and orientation on appropriate radiographs, estimate ingestion time and move to removal without avoidable delay rather than observing for spontaneous passage. Review age/weight, symptoms, airway/secretions, co-ingestants and whether the battery lies near the aortic arch because duration, impaction level and adjacent vascular anatomy influence the post-removal injury plan.",
            "Before extraction, coordinate airway control and retrieval equipment with anesthesia and anticipate caustic adherence or deep mucosal injury. Plan to inspect the esophageal injury after removal and define in advance which findings would trigger admission, multidisciplinary consultation or cross-sectional vascular/mediastinal evaluation rather than treating successful extraction as the endpoint.",
        ],
        "postop": [
            "Grade and document the mucosal injury after battery removal and base feeding, observation and additional imaging/endoscopy on the depth/location of injury and clinical course. Significant circumferential necrosis, injury adjacent to major vessels, fever, chest pain, dysphagia, respiratory symptoms or bleeding warrants monitored multidisciplinary management because tissue injury can evolve after the battery is gone.",
        ],
        "marker": "button_battery_management_v2320",
    },
    {
        "slug": "esophageal-fb",
        "title_terms": ("esophageal", "foreign"),
        "setup": [
            "Before esophageal foreign-body endoscopy, define object type, sharpness/size, level, duration and whether the patient has complete obstruction or cannot handle secretions. Batteries, sharp objects, complete obstruction and suspected perforation change urgency and technique; review imaging and underlying stricture/eosinophilic or other esophageal disease when the presentation suggests a food impaction rather than an isolated accidental ingestion.",
            "Choose flexible versus rigid endoscopic strategy according to location, object characteristics, airway risk and local expertise, with protective retrieval tools available for sharp material. Avoid repeated blind pushing or grasping when the object cannot be safely visualized and controlled.",
        ],
        "postop": [
            "After extraction, document mucosal injury and reassess swallowing/secretions. Diet advancement, observation, contrast imaging or surgical consultation should reflect the degree of trauma and perforation concern; persistent focal dysphagia after food impaction also warrants evaluation for an underlying esophageal disorder rather than assuming the foreign body was the entire diagnosis.",
        ],
        "marker": "esophageal_fb_management_v2320",
    },
    {
        "slug": "deep-neck-drain",
        "title_terms": ("deep", "neck", "abscess"),
        "setup": [
            "Before deep-neck abscess drainage, assess the airway before focusing on the collection: voice change, drooling, trismus, floor-of-mouth elevation, stridor, respiratory distress or rapidly progressive swelling can make airway control the first procedure. Review contrast CT for involved spaces, source, carotid/jugular relationships, gas, mediastinal extension and drainable versus phlegmonous disease, and start appropriate IV antibiotics while coordinating dental, thoracic or other source-control teams when needed.",
            "Plan the drainage route around the involved fascial space and major vessels and obtain cultures from purulent material when possible. A small radiographic collection in a stable patient can be different from a toxic patient with multiloculated disease, septic thrombophlebitis or descending infection; the operative decision should follow physiology and source-control need, not size alone.",
        ],
        "postop": [
            "After drainage, worsening swelling, respiratory effort, sepsis, chest pain, crepitus or persistent fever should trigger reassessment for residual/loculated infection, inadequate source control, mediastinal spread or vascular complication rather than simply extending antibiotics. Maintain airway surveillance until edema and secretion burden are clearly improving.",
            "Trend the clinical response and narrow antimicrobial therapy when culture data permit. Failure to improve should prompt review of the original source—especially odontogenic disease, infected hardware, necrotic tissue or an undrained space—rather than repeated superficial wound manipulation alone.",
        ],
        "marker": "deep_neck_abscess_management_v2320",
    },
    {
        "slug": "pta-drainage",
        "title_terms": ("peritonsillar", "abscess"),
        "setup": [
            "Before peritonsillar abscess drainage, confirm the diagnosis clinically and assess airway, hydration and ability to tolerate a bedside procedure. Marked trismus, toxic appearance, atypical neck findings, immunocompromise or concern for deeper-space infection should lower the threshold for imaging, operative drainage or higher-acuity care rather than routine office aspiration alone.",
            "Choose needle aspiration, incision/drainage or tonsillectomy in selected patients based on age/cooperation, recurrence history, airway status and response to prior drainage. Keep the needle/incision controlled and medial because the carotid lies posterolateral to the tonsillar fossa; adequate analgesia and suction are part of safe drainage, not optional comfort measures.",
        ],
        "postop": [
            "After drainage, confirm the patient can manage secretions and oral hydration and give antimicrobial/analgesic therapy appropriate to the clinical setting. Persistent fever, worsening neck swelling, respiratory symptoms, recurrent trismus or failure to improve should prompt reassessment for inadequate drainage, parapharyngeal/deep-neck spread or an alternative diagnosis.",
        ],
        "marker": "pta_management_v2320",
    },
    {
        "slug": "rigid-tracheobronchoscopy",
        "title_terms": ("rigid", "tracheobronchoscopy"),
        "setup": [
            "Before rigid tracheobronchoscopy, define whether the goal is diagnosis, dilation/debridement, foreign-body removal, biopsy or control of a central-airway lesion and review imaging/endoscopy for the narrowest segment, distal airway access and bleeding risk. Coordinate the shared-airway ventilation strategy and rescue plan with anesthesia before instrumentation; when laser or other ignition-capable energy is used, explicitly implement airway-fire precautions and minimize oxidizer concentration as clinically feasible.",
        ],
        "postop": [
            "After rigid bronchoscopy, new stridor, respiratory distress, hemoptysis, chest pain, subcutaneous emphysema or increased oxygen requirement warrants evaluation for edema, bleeding, pneumothorax/pneumomediastinum or airway perforation. After biopsy/debulking of a vascular lesion, delayed bleeding or clot obstruction can be as dangerous as immediate hemorrhage and should be included in disposition planning.",
        ],
        "marker": "rigid_tracheobronchoscopy_management_v2320",
    },
    {
        "slug": "transnasal-esophagoscopy",
        "title_terms": ("transnasal", "esophagoscopy"),
        "setup": [
            "Before transnasal esophagoscopy, define the diagnostic target—dysphagia, reflux-related symptoms, surveillance, biopsy or evaluation of a suspected upper-esophageal lesion—and review anticoagulation/bleeding risk, nasal patency, aspiration risk and prior esophageal surgery/stricture. A patient with complete obstruction, unstable airway, suspected perforation or a lesion requiring major therapeutic intervention is not automatically an office-TNE candidate simply because the scope can be passed transnasally.",
        ],
        "postop": [
            "After transnasal esophagoscopy, mild nasal/throat discomfort can be expected, but escalating neck/chest pain, fever, crepitus, dyspnea, hematemesis or inability to swallow secretions should prompt evaluation for perforation or significant bleeding. Pathology and structural findings should drive the next diagnostic/therapeutic step rather than treating a technically completed examination as definitive when symptoms remain unexplained.",
        ],
        "marker": "transnasal_esophagoscopy_management_v2320",
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


def apply_or_general_emergency_management_v2320(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target["setup"])
        op["postop"], c2 = _prepend_unique(op.get("postop"), target["postop"])
        op[target["marker"]] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    v2321 = apply_or_specialty_management_v2321(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v2321": v2321}
