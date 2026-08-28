"""v23.13 parathyroid OR Tomorrow planning and postoperative rescue.

Adds procedure-specific decision points and postoperative calcium/airway rescue for
focused parathyroidectomy, bilateral four-gland exploration, and reoperative
parathyroid surgery. Existing ioPTH renal-clearance nuance, operative choreography,
and reviewed endocrine anatomy remain unchanged. Later high-risk generic-only OR
management review is chained here so the existing decision hook remains atomic.
"""

from or_high_risk_management_v2314 import apply_or_high_risk_management_v2314

TARGETS = [
    {
        "slug": "parathyroidectomy",
        "title_terms": ("parathyroidectomy",),
        "exclude_terms": ("reop", "reoperative", "four", "4-gland", "bilateral"),
        "setup": [
            "Before focused parathyroidectomy, confirm the biochemical diagnosis and review whether localization studies are concordant with the planned side; localization guides the operation but does not establish the diagnosis. Define in advance what will trigger conversion from a focused exploration to a broader search—failed target identification, discordant intraoperative findings, or an inadequate protocol-consistent ioPTH response—rather than extending the incision without a decision framework.",
        ],
        "postop": [
            "After parathyroidectomy, distinguish routine transient calcium change from clinically important hypocalcemia. Perioral or acral paresthesias, cramps, carpopedal spasm, worsening neuromuscular irritability, or QT-related symptoms should prompt calcium assessment and treatment according to the local pathway; patients with severe preoperative bone disease, vitamin-D deficiency, or renal hyperparathyroidism need particular vigilance for hungry-bone physiology rather than assuming a short-lived postoperative dip.",
            "An expanding central-neck swelling, stridor, dyspnea, rapidly increasing pressure, or dysphagia after parathyroid surgery is a neck-hematoma/airway emergency. New persistent dysphonia should trigger vocal-fold assessment, especially when the exploration approached the recurrent-laryngeal-nerve plane.",
        ],
    },
    {
        "slug": "four-gland",
        "title_terms": ("four", "gland"),
        "exclude_terms": (),
        "setup": [
            "Before bilateral four-gland exploration, define why multigland disease is expected—such as familial/MEN-pattern disease, lithium-associated disease, or renal hyperparathyroidism—and clarify the planned extent of resection and strategy for preserving viable functioning parathyroid tissue. Because bilateral exploration is an anatomic operation, intraoperative PTH should complement rather than replace systematic identification of the expected glands and ectopic pathways.",
        ],
        "postop": [
            "After bilateral parathyroid exploration, use a planned calcium/PTH surveillance and replacement strategy that reflects the larger reduction in functioning parathyroid mass. Symptomatic or progressive hypocalcemia, particularly with high preoperative bone turnover or renal hyperparathyroidism, should raise concern for hungry-bone syndrome and may require sustained calcium plus active-vitamin-D replacement rather than repeated isolated rescue doses.",
            "Document postoperative voice and inspect the neck for hematoma after bilateral exploration; bilateral dissection increases the importance of recognizing recurrent-laryngeal-nerve dysfunction or airway compromise early rather than waiting for routine follow-up.",
        ],
    },
    {
        "slug": "reop-parathyroid",
        "title_terms": ("reop", "parathyroid"),
        "exclude_terms": (),
        "setup": [
            "Before reoperative parathyroid surgery, verify persistent versus recurrent biochemical disease, review every prior operative/pathology report and current localization study, and require a convincing target before entering a scarred neck whenever possible. Document preoperative vocal-fold mobility because an unrecognized pre-existing unilateral recurrent-laryngeal-nerve deficit materially changes the risk of re-exploration, and define the least-scarred route to the suspected gland rather than planning a routine bilateral redissection.",
        ],
        "postop": [
            "After reoperative parathyroid surgery, have a lower threshold to evaluate new dysphonia, dysphagia, stridor, expanding neck swelling, or hypocalcemic symptoms because scarred anatomy increases the consequences of recurrent-nerve injury, bleeding, and devascularization of remaining parathyroid tissue. Calcium surveillance should reflect both the preoperative skeletal/renal risk and how much viable parathyroid tissue remains after re-exploration.",
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


def apply_or_parathyroid_management_v2313(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        op["setup"], c1 = _prepend_unique(op.get("setup"), target.get("setup", []))
        op["postop"], c2 = _prepend_unique(op.get("postop"), target.get("postop", []))
        op["parathyroid_management_v2313"] = True
        resolved.append(slug)
        if c1 or c2:
            changed.append(slug)
    v2314 = apply_or_high_risk_management_v2314(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v2314": v2314}