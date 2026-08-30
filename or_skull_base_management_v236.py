"""v23.6+ skull-base OR Tomorrow planning and postoperative rescue.

Adds high-confidence perioperative decision points for lateral skull-base operations
whose approach selection and operative choreography are already procedure-specific.
Later arytenoid-adduction management is chained here so the existing decision hook
remains atomic.
"""

from or_arytenoid_adduction_management_v237 import apply_or_arytenoid_adduction_management_v237

TARGETS = [
    {
        "slug": "jugular-foramen-tumor",
        "title_terms": ("jugular", "foramen"),
        "setup": [
            "Before jugular-foramen tumor surgery, document baseline CN IX-XII function, voice, swallowing/aspiration, shoulder strength, tongue mobility, hearing and facial function because postoperative deficits must be interpreted against the preoperative examination. Review tumor relationship to the jugular bulb/sigmoid sinus, carotid artery, dura/brainstem and lower cranial nerves and make the airway, feeding and vascular-control plan explicit before incision.",
            "For hypervascular lesions, review vascular imaging and the multidisciplinary embolization or proximal-control strategy when appropriate. The operative goal should balance tumor control against avoidable lower-cranial-nerve or carotid injury rather than treating gross-total removal as mandatory when a critical structure is inseparable from tumor.",
            "Make loss of a safe plane around the internal carotid artery, brainstem, or functioning lower cranial nerves an explicit extent-of-resection commitment point. If tumor cannot be separated without disproportionate neurovascular morbidity, stop escalating traction or blind peeling and reassess the goal of surgery; intentional residual disease with surveillance and, when appropriate, staged radiation is preferable to unplanned carotid sacrifice, brainstem injury, or avoidable loss of functioning CN IX-XII simply to achieve gross-total removal.",
            "Unexpected jugular-bulb or sigmoid-sinus hemorrhage is a vascular bailout, not a cue for blind deep clamping. Obtain controlled exposure, use direct compression or carefully placed packing for immediate control, identify the injured venous segment and reassess the planned extent of resection. Preserve dominant venous outflow when it has not been deliberately assessed and planned for sacrifice; a preplanned sinus/jugular sacrifice after review of collateral drainage is fundamentally different from uncontrolled intraoperative loss of venous outflow.",
        ],
        "postop": [
            "After jugular-foramen surgery, new dysphonia, weak cough, secretion intolerance, aspiration, tongue weakness or shoulder weakness should trigger focused CN IX-XII examination and early swallowing/airway assessment rather than routine diet advancement. Significant lower-cranial-nerve dysfunction may require protected enteral nutrition and a deliberate airway strategy while function is characterized.",
            "Clear wound/ear/nasal drainage, meningitic symptoms, severe headache or unexplained fever should raise concern for CSF leak or intracranial infection. New focal neurologic change, expanding neck/skull-base hematoma, brisk bleeding or hemodynamic instability requires urgent evaluation for intracranial or major-vessel complication rather than routine postoperative observation.",
        ],
    },
    {
        "slug": "translabyrinthine-skull-base",
        "title_terms": ("translabyrinthine",),
        "setup": [
            "Before a translabyrinthine approach, reconfirm that the hearing-sacrificing corridor matches the patient's current audiogram and treatment goal, document facial and lower-cranial-nerve function, and review tumor size, brainstem relationship and facial-nerve course. Plan the fat/fascial or other CSF-leak closure strategy before opening air cells and dura rather than treating closure as an afterthought.",
        ],
        "postop": [
            "After translabyrinthine surgery, document facial-nerve function immediately and serially; new or progressive weakness, severe headache, altered mental status, lower-cranial-nerve dysfunction or unexpected neurologic decline requires prompt skull-base evaluation rather than attribution to routine postoperative disequilibrium.",
            "Persistent clear rhinorrhea/otorrhea or wound drainage, a ballotable postauricular collection, meningitic symptoms or fever should trigger evaluation for CSF leak/pseudomeningocele and infection. Expected vestibular imbalance should progressively compensate; severe or worsening symptoms with neurologic findings warrant reassessment for central or surgical complication.",
        ],
    },
    {
        "slug": "retrosigmoid-skull-base",
        "title_terms": ("retrosigmoid",),
        "setup": [
            "Before a retrosigmoid skull-base operation, define whether hearing preservation is an operative goal from current audiometry and tumor anatomy, and document baseline facial, vestibular and lower-cranial-nerve function. Review CPA/brainstem displacement, internal-auditory-canal extension, venous-sinus anatomy and the monitoring/drilling strategy so the hearing, facial-nerve and brainstem tradeoffs are explicit.",
        ],
        "postop": [
            "After retrosigmoid surgery, serially assess mental status, focal neurologic function, facial movement, hearing symptoms, swallowing/voice and vestibular status. Progressive headache with vomiting, declining mental status, new long-tract/cerebellar findings or cranial-nerve deterioration requires urgent evaluation for hemorrhage, edema, hydrocephalus or brainstem/cerebellar complication rather than routine postoperative analgesia alone.",
            "Clear wound or nasal/ear drainage, enlarging pseudomeningocele, fever or meningitic symptoms should trigger CSF-leak/infection evaluation. New aspiration or ineffective cough warrants early swallowing assessment because lower-cranial-nerve dysfunction can be clinically subtle but pulmonary consequences can be significant.",
        ],
    },
    {
        "slug": "middle-fossa-skull-base",
        "title_terms": ("middle", "fossa"),
        "setup": [
            "Before a middle-fossa approach, confirm the hearing-preservation indication from current audiometry and lesion/IAC anatomy, document facial and vestibular function, and review temporal-lobe, labyrinth/cochlea, geniculate/facial-nerve and petrous-carotid relationships. Define facial/cochlear monitoring and CSF-leak closure strategy before temporal-lobe elevation and petrous drilling.",
        ],
        "postop": [
            "After middle-fossa surgery, document facial function and hearing symptoms and monitor mental status for consequences of temporal-lobe retraction or intracranial bleeding. New seizure, aphasia/confusion, focal deficit, severe progressive headache or declining consciousness is not routine postoperative discomfort and requires urgent neurologic/skull-base evaluation.",
            "Clear rhinorrhea/otorrhea, wound drainage or pseudomeningocele, fever or meningitic symptoms should prompt evaluation for CSF leak and intracranial infection. Persistent or worsening vestibular symptoms with new hearing/facial change should trigger targeted reassessment rather than reassurance alone.",
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


def apply_or_skull_base_management_v236(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["skull_base_management_v236"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    v237 = apply_or_arytenoid_adduction_management_v237(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v237": v237}
