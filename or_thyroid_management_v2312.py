"""v23.12 thyroid OR Tomorrow planning and postoperative rescue.

Adds procedure-specific perioperative decisions and postoperative failure recognition
for lobectomy, total thyroidectomy, and reoperative thyroid surgery. Existing exact
operative choreography, endocrine physiology, and reviewed anatomy remain unchanged.
"""

TARGETS = [
    {
        "slug": "thyroid-lobectomy",
        "title_terms": ("thyroid", "lobectomy"),
        "exclude_terms": ("total", "reop", "reoperative"),
        "setup": [
            "Before thyroid lobectomy, confirm the indication and intended unilateral extent from cytology/pathology, imaging and contralateral-lobe findings, and document baseline voice with vocal-fold examination when there is dysphonia, prior neck surgery, invasive disease or another reason to suspect pre-existing laryngeal nerve dysfunction. Review whether the operation could reasonably require conversion or future completion surgery so that consent and oncologic planning match the actual disease rather than the word 'lobectomy' alone.",
        ],
        "postop": [
            "After thyroid lobectomy, an expanding central-neck swelling, stridor, respiratory distress, dysphagia with neck pressure or rapidly increasing wound tension is a postoperative hematoma/airway emergency and requires immediate bedside assessment with a low threshold for urgent decompression and operative control. New persistent dysphonia should prompt vocal-fold assessment rather than being attributed indefinitely to intubation alone.",
        ],
    },
    {
        "slug": "total-thyroidectomy",
        "title_terms": ("total", "thyroidectomy"),
        "exclude_terms": (),
        "setup": [
            "Before total thyroidectomy, review disease-specific factors that change technical or postoperative risk: Graves/hypervascular disease, large or substernal goiter, invasive malignancy, prior neck treatment, baseline voice/vocal-fold function when indicated, and the anticipated need for central/lateral nodal surgery. Define the intraoperative nerve-monitoring/staging strategy if used and the postoperative calcium/PTH pathway before surgery rather than reacting only after symptoms develop.",
        ],
        "postop": [
            "After total thyroidectomy, assess the airway and neck first, then evaluate voice and calcium physiology. Perioral/acral paresthesias, cramps, carpopedal spasm or other neuromuscular irritability should trigger prompt calcium assessment/treatment according to the local pathway; a low early PTH identifies patients who may need closer calcium/vitamin-D supplementation and follow-up rather than waiting for severe symptoms.",
            "New stridor or respiratory distress after bilateral thyroid dissection requires urgent evaluation for neck hematoma, edema and bilateral vocal-fold dysfunction. When unexplained intraoperative loss of nerve signal occurred, the postoperative airway plan should explicitly reflect that risk rather than relying on routine recovery-room observation.",
        ],
    },
    {
        "slug": "reop-thyroid",
        "title_terms": ("reop", "thyroid"),
        "exclude_terms": (),
        "setup": [
            "Before reoperative/completion thyroid surgery, obtain and review prior operative and pathology reports, map the remaining target and prior nodal fields on current imaging, and document preoperative vocal-fold mobility because an unrecognized pre-existing unilateral paralysis materially changes the risk of contralateral dissection. Anticipate scar-displaced RLN/parathyroid anatomy and define whether the least-scarred nerve-identification route, nerve monitoring, or staged extent should change the plan.",
        ],
        "postop": [
            "After reoperative thyroid surgery, have a lower threshold to investigate new dysphonia, dysphagia, stridor, hypocalcemic symptoms or expanding neck swelling because scarred anatomy increases the consequences of recurrent-nerve, parathyroid and bleeding complications. If the remaining functional side of the larynx was at risk, postoperative vocal-fold assessment and airway planning should be driven by the actual nerve history and intraoperative findings rather than routine thyroidectomy assumptions.",
        ],
    },
]


def _resolve(registry, target):
    reg = registry or {}
    if target["slug"] in reg:
        return target["slug"], reg[target["slug"]]
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if not all(term in hay for term in target["title_terms"]):
            continue
        if any(term in hay for term in target.get("exclude_terms", ())):
            continue
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


def apply_or_thyroid_management_v2312(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["thyroid_management_v2312"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing}
