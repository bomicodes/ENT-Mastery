"""v22.6+ procedure-specific anatomy for pediatric adenotonsillar OR Tomorrow cases.

Replaces the broad pediatric-family landmark list for tonsillectomy, adenoidectomy,
and combined adenotonsillectomy with the structures that actually govern exposure,
bleeding risk, velopharyngeal safety, and Eustachian-tube preservation. Later reviewed
tracheostomy anatomy is chained here so the runtime anatomy hook remains atomic.
"""

from or_landmarks_v227 import apply_or_landmarks_v227

TARGETS = [
    {
        "slug": "tonsillectomy",
        "title_terms": ("tonsillectomy",),
        "exclude_terms": ("adenoid", "lingual"),
        "landmarks": [
            "palatine tonsil capsule and peritonsillar plane",
            "superior pharyngeal constrictor forming the muscular tonsillar bed",
            "palatoglossus and palatopharyngeus pillars defining the anterior and posterior fossal boundaries",
            "superior pole and lower-pole vascular pedicles requiring targeted hemostasis",
            "glossopharyngeal nerve deep to the inferior tonsillar fossa as a functional danger structure",
            "parapharyngeal carotid system lateral to the pharyngeal musculature, protected by staying on the tonsillar capsule rather than dissecting deeply lateral",
        ],
    },
    {
        "slug": "adenotonsillectomy",
        "title_terms": ("tonsillectomy", "adenoid"),
        "exclude_terms": (),
        "landmarks": [
            "palatine tonsil capsule and superior-constrictor plane",
            "palatoglossus and palatopharyngeus pillars with superior- and lower-pole tonsillar vascular regions",
            "posterior choanae and vomer defining the superior nasopharyngeal airway",
            "torus tubarius and Eustachian-tube orifices laterally",
            "soft palate/velopharyngeal musculature and Passavant region, particularly when submucous cleft or velopharyngeal insufficiency risk is present",
            "posterior nasopharyngeal wall and prevertebral plane, which should not be violated during adenoid removal",
        ],
    },
    {
        "slug": "adenoidectomy",
        "title_terms": ("adenoidectomy",),
        "exclude_terms": ("tonsil",),
        "landmarks": [
            "adenoid pad on the posterior nasopharyngeal wall",
            "posterior choanae and vomer superior/anterior to the operative field",
            "torus tubarius and Eustachian-tube orifices laterally",
            "soft palate and velopharyngeal musculature inferiorly",
            "Passavant ridge/velopharyngeal contact region, with conservative tissue preservation when VPI risk is present",
            "prevertebral fascia deep to the posterior pharyngeal wall as a boundary that should not be violated",
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


def apply_or_landmarks_v226(registry):
    changed, resolved, missing = [], [], []
    for target in TARGETS:
        slug, op = _resolve(registry, target)
        if not op:
            missing.append(target["slug"])
            continue
        desired = list(target["landmarks"])
        if list(op.get("landmarks") or []) != desired:
            op["landmarks"] = desired
            changed.append(slug)
        op["landmarks_v226"] = "procedure-specific"
        resolved.append(slug)
    v227 = apply_or_landmarks_v227(registry)
    return {"changed": changed, "count": len(changed), "targets": len(TARGETS), "resolved": resolved, "missing": missing, "v227": v227}
