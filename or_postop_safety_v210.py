"""v20.10 focused postoperative safety layer for OR Tomorrow.

Adds a small number of procedure-specific, high-consequence postoperative failure
modes that are not adequately conveyed by family-level complication boilerplate.
The matcher is title/slug based so the layer remains robust to canonical slug naming.
"""

TARGETS = [
    {
        "name": "tracheostomy",
        "triggers": ("tracheostomy",),
        "exclude": ("laryngectomy", "tracheoesophageal puncture", "tep"),
        "postop": [
            "In a fresh surgical tracheostomy, accidental decannulation or difficult reinsertion can create a false passage because the tract is not mature; do not repeatedly force a tube blindly—activate the airway/ENT team and manage oxygenation according to the known upper-airway anatomy while the tract is safely re-established.",
            "New brisk or sentinel bleeding from a tracheostomy, particularly days to weeks after placement, is a tracheo-innominate fistula warning until excluded and requires immediate airway/hemorrhage escalation and definitive operative or endovascular control planning.",
        ],
    },
    {
        "name": "septoplasty",
        "triggers": ("septoplasty",),
        "exclude": (),
        "postop": [
            "After septoplasty, disproportionate nasal pain/pressure, progressive bilateral obstruction, fever or a boggy septal swelling should prompt urgent examination for septal hematoma or abscess; delay risks cartilage necrosis, perforation and saddle-nose deformity.",
        ],
    },
    {
        "name": "pharyngoesophageal-myotomy",
        "triggers": ("zenker", "cricopharyngeal myotomy", "cricopharyngeal-myotomy"),
        "exclude": (),
        "postop": [
            "After Zenker septotomy or cricopharyngeal myotomy, escalating neck/chest pain, fever, tachycardia, crepitus, dyspnea or systemic toxicity should trigger urgent evaluation for pharyngoesophageal perforation and cervical/mediastinal infection rather than routine diet advancement.",
        ],
    },
]


def _label(slug, op):
    return f"{slug} {op.get('title', '')}".lower()


def _prepend_unique(values, additions):
    out = list(values or [])
    changed = False
    for text in reversed(additions):
        marker = text[:56].lower()
        if not any(marker in str(x).lower() for x in out):
            out.insert(0, text)
            changed = True
    return out, changed


def apply_or_postop_safety_v210(registry):
    applied = {}
    for target in TARGETS:
        matches = []
        for slug, op in (registry or {}).items():
            label = _label(slug, op)
            if not any(term in label for term in target["triggers"]):
                continue
            if any(term in label for term in target["exclude"]):
                continue
            op["postop"], changed = _prepend_unique(op.get("postop"), target["postop"])
            op["postop_safety_v210"] = True
            matches.append({"slug": slug, "changed": changed})
        applied[target["name"]] = matches
    return {"targets": len(TARGETS), "applied": applied}
