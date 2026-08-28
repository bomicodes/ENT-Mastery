"""v23.17 pediatric core OR Tomorrow management review.

Adds resident-level selection, perioperative planning and postoperative rescue to seven
pediatric procedures that remained generic-only after the live OR coverage audit.
The two DLB registry entries are reviewed deliberately because they serve different
linked curricular contexts but share the same airway-endoscopy safety principles.
The v23.18 facial-trauma review is chained through this tail.
"""

from or_facial_trauma_management_v2318 import apply_or_facial_trauma_management_v2318

DLB_SETUP = [
    "Before pediatric direct laryngoscopy/bronchoscopy, define the question the endoscopy must answer—dynamic obstruction, stenosis sizing, recurrent croup/stridor, aspiration/foreign body, tracheostomy planning, or surveillance after reconstruction—because this determines whether spontaneous ventilation, controlled ventilation or a secured airway best preserves the physiology being examined. Review prior airway grade, difficult-intubation history, current respiratory infection, oxygen requirement and cardiopulmonary comorbidity with anesthesia before induction.",
    "Plan the endoscopy as an airway measurement, not only a visual inspection: document vocal-fold mobility, subglottic/tracheal caliber and length of any lesion, dynamic collapse when relevant, distal airway findings, and the largest atraumatically tolerated airway size when sizing is clinically needed. Have rescue equipment and a clear stop/escalation plan immediately available because repeated traumatic instrumentation can convert a stable diagnostic airway into an edematous difficult airway.",
]

DLB_POSTOP = [
    "After pediatric airway endoscopy, new or worsening stridor, increased work of breathing, persistent hypoxemia, hemoptysis, subcutaneous emphysema or inability to manage secretions is not simply expected emergence and should prompt airway reassessment for edema, laryngospasm/bronchospasm, mucosal injury, pneumothorax or an inadequately characterized obstruction.",
    "Disposition should reflect what was found and what was done, not the label DLB alone. Significant stenosis, difficult instrumentation, airway intervention, baseline oxygen dependence or concerning postoperative respiratory findings may require prolonged monitored observation rather than routine discharge.",
]

TARGETS = [
    {
        "slug": "DLB",
        "title_terms": ("direct", "laryngoscopy", "bronchoscopy"),
        "setup": DLB_SETUP,
        "postop": DLB_POSTOP,
        "marker": "pediatric_dlb_management_v2317",
    },
    {
        "slug": "direct-laryngoscopy-bronchoscopy",
        "title_terms": ("direct", "laryngoscopy", "bronchoscopy"),
        "setup": DLB_SETUP,
        "postop": DLB_POSTOP,
        "marker": "pediatric_dlb_management_v2317",
    },
    {
        "slug": "airway-fb",
        "title_terms": ("airway", "foreign", "body"),
        "setup": [
            "Before rigid bronchoscopy for suspected airway foreign body, treat a convincing aspiration event with persistent focal respiratory findings as potentially significant even when plain radiographs are normal. Review timing, object type, choking/cyanosis history, unilateral wheeze or diminished breath sounds, fever and imaging, and coordinate induction/ventilation with anesthesia so positive-pressure ventilation does not inadvertently worsen distal obstruction when a mobile object is suspected.",
            "Have appropriately sized rigid bronchoscopes, optical forceps and backup retrieval instruments available before induction. The operative goal is controlled visualization and extraction—not repeated blind grasping; anticipate friable organic material, distal migration and the possibility of more than one fragment, and plan a complete airway reinspection after removal.",
        ],
        "postop": [
            "After foreign-body removal, persistent unilateral findings, hypoxemia, fever, wheeze or respiratory distress should trigger consideration of retained fragment, mucosal edema/injury, atelectasis, pneumonia or pneumothorax rather than assuming all symptoms will resolve immediately. Sudden deterioration after difficult extraction warrants prompt chest/airway assessment.",
            "Document complete reinspection of the tracheobronchial tree when feasible and base observation/discharge on respiratory recovery, extraction trauma and infection burden. A child with ongoing focal symptoms after an apparently successful procedure needs reassessment rather than repeated empiric treatment without reconsidering retained foreign body.",
        ],
        "marker": "pediatric_airway_fb_management_v2317",
    },
    {
        "slug": "branchial",
        "title_terms": ("branchial",),
        "setup": [
            "Before branchial cleft anomaly excision, establish whether the lesion is a cyst, sinus or fistula and review imaging for its relationship to the carotid space, pharynx, parotid/facial nerve and other cranial nerves according to the suspected anomaly. Whenever feasible, treat acute infection first so definitive surgery is performed after inflammation has settled; prior incision/drainage should be anticipated to distort planes and increase recurrence risk.",
        ],
        "postop": [
            "After branchial anomaly surgery, expanding neck swelling, respiratory symptoms or rapidly increasing pain should prompt evaluation for hematoma or deep-space complication. New facial, vagal, hypoglossal or other focal cranial-nerve deficit should be localized to the operative corridor rather than labeled nonspecific postoperative weakness.",
            "Recurrent drainage, infection or mass suggests residual epithelial tract or incomplete excision and deserves an anatomic reassessment before repeat surgery, particularly after prior infected or scarred dissections.",
        ],
        "marker": "branchial_management_v2317",
    },
    {
        "slug": "thyroglossal",
        "title_terms": ("sistrunk",),
        "setup": [
            "Before a Sistrunk procedure, confirm the clinical/imaging diagnosis and verify a normally located functioning thyroid when there is uncertainty that the midline mass could represent the patient's only thyroid tissue. Resolve acute infection before elective excision when possible and plan removal of the cyst/tract with the central hyoid segment and suprahyoid core toward the tongue base rather than simple cyst excision, which carries a substantially higher recurrence risk.",
        ],
        "postop": [
            "After Sistrunk surgery, rapidly expanding midline neck swelling, dysphagia, stridor or respiratory distress is a hematoma/airway concern and requires urgent assessment. Later recurrent midline swelling or drainage should raise concern for residual tract or recurrent disease rather than routine scar maturation.",
        ],
        "marker": "sistrunk_management_v2317",
    },
    {
        "slug": "palatoplasty",
        "title_terms": ("palatoplasty",),
        "setup": [
            "Before cleft-palate repair, integrate airway risk, feeding/growth, hearing/ear disease, speech goals and syndromic anatomy into the plan. Children with Pierre Robin sequence, significant OSA, micrognathia, cardiopulmonary disease or prior difficult airway need an explicit postoperative airway/disposition strategy; the operation should restore palatal separation and levator function while minimizing tension rather than simply close the visible cleft.",
            "Review cleft width, prior repairs/scar, fistula history and planned myoplasty with the family and multidisciplinary cleft team. Coordinate postoperative feeding and analgesia instructions in advance because dehydration, oral trauma and uncontrolled pain can jeopardize both recovery and repair protection.",
        ],
        "postop": [
            "After palatoplasty, progressive obstruction, desaturation, stridor, retractions, inability to handle secretions or excessive somnolence requires airway assessment; children with baseline OSA or micrognathia may decompensate after edema and analgesia even when the intraoperative airway was uncomplicated.",
            "Monitor hydration and repair integrity. Significant oral bleeding, wound dehiscence or a new symptomatic palatal fistula requires surgical reassessment; longer-term follow-up should evaluate speech/velopharyngeal function, fistula, maxillary growth and middle-ear/hearing issues through the cleft team rather than considering an intact early incision the final endpoint.",
        ],
        "marker": "palatoplasty_management_v2317",
    },
    {
        "slug": "tympanostomy-tubes",
        "title_terms": ("tympanostomy", "tube"),
        "setup": [
            "Before tympanostomy tubes, verify that the child meets an appropriate indication—such as chronic otitis media with effusion affecting hearing/quality of life or recurrent acute otitis media with middle-ear effusion at assessment—and account for speech/language, developmental, craniofacial or other factors that increase the consequence of persistent effusion. Document the tympanic membrane and middle-ear status rather than treating infection count alone as the operative indication.",
        ],
        "postop": [
            "After tube placement, uncomplicated acute tube otorrhea is generally managed with topical otic therapy rather than routine systemic antibiotics when there is no competing indication. Persistent drainage should prompt assessment for obstructed tube, resistant infection, granulation, foreign material or another diagnosis rather than indefinite empiric drops.",
            "Long-term follow-up should recognize premature extrusion with recurrent effusion, retained tube, granulation and persistent tympanic-membrane perforation as distinct problems. Hearing or developmental concerns that persist despite a patent, aerated middle ear need reassessment beyond the tube itself.",
        ],
        "marker": "tympanostomy_tube_management_v2317",
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


def apply_or_pediatric_core_management_v2317(registry):
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
    v2318 = apply_or_facial_trauma_management_v2318(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v2318": v2318}
