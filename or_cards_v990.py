"""v99.0: new OR Tomorrow cards and step refreshes from the textbook gap review.

New cards live in or_cards_v990_data/<slug>.json (17 high-priority missing surgeries plus the
laryngology and sinus operations the 2024 laryngology book and the sinus atlas cover that the site
had no card for). Steps for existing laryngology and sinus cards are refreshed from those two books
(or_steps_v990.json). No images and no antibiotic prophylaxis content, per the site's OR-card rules.
"""
import glob
import json
import os

_HERE = os.path.dirname(os.path.abspath(__file__))

# Common shorthand residents type into OR Tomorrow search (matched as whole phrases or extra tokens).
SEARCH_ALIASES = {
    "pectoralis-major-flap": ["pec flap", "pec major flap", "pec major", "pmmc flap", "pmmc"],
    "cricothyrotomy": ["cric", "crike", "surgical airway", "cricothyroidotomy"],
    "rhytidectomy": ["facelift", "face lift"],
    "blepharoplasty": ["bleph", "eyelid lift"],
    "panendoscopy": ["triple endoscopy", "dle", "direct laryngoscopy esophagoscopy bronchoscopy"],
    "comprehensive-neck-dissection": ["mrnd", "modified radical neck dissection", "radical neck dissection"],
    "sentinel-node-biopsy": ["slnb", "sentinel lymph node biopsy"],
    "lymph-node-excision-biopsy": ["excisional node biopsy", "lymph node biopsy", "node biopsy"],
    "epistaxis-packing-cautery": ["nosebleed", "posterior packing", "nasal packing"],
    "draf-iii-outside-in": ["modified lothrop", "emlp", "draf 3"],
    "t-tube-stent-placement": ["montgomery t tube", "t tube"],
}


def _cards():
    out = []
    for p in sorted(glob.glob(os.path.join(_HERE, "or_cards_v990_data", "*.json"))):
        with open(p, encoding="utf-8") as fh:
            out.append(json.load(fh))
    return out


def install_or_cards_v990(data, app_mod):
    import textbook_curriculum_v470
    registry = data.OR_PREP_REGISTRY
    added = []
    for card in _cards():
        slug = card["slug"]
        if slug in registry:
            continue
        steps = [[str(t), " ".join(str(d).split())] for t, d in card["steps"]]
        c = {k: v for k, v in card.items() if k not in ("steps", "source_label")}
        label = card.get("source_label", "")
        c.update({
            "steps_v840": steps,
            "steps": [f"{t}. {d}" for t, d in steps],
            "steps_source_v840": (label[:1].upper() + label[1:]) if label else "",
            "status": "authored-v99.0",
            "review_status_v190": "operative-depth reviewed",
            "sequence_status_v200": "procedure-specific",
            "sources": list(card.get("source_basis", [])),
        })
        registry[slug] = c
        added.append(slug)
        topic = card.get("linked_topic")
        if topic:
            m = textbook_curriculum_v470.TOPIC_OR_MAP_V470.setdefault(topic, [])
            if slug not in m:
                m.append(slug)
    for slug, al in SEARCH_ALIASES.items():
        if slug in registry:
            registry[slug]["search_aliases_v990"] = list(al)
    if getattr(app_mod, "OR_PREP_REGISTRY", None) is not registry:
        app_mod.OR_PREP_REGISTRY = registry
    return {"added": added}


def install_or_steps_v990(data):
    """Run last in the OR chain so the book-based sequence replaces older generic steps."""
    with open(os.path.join(_HERE, "or_steps_v990.json"), encoding="utf-8") as fh:
        refresh = json.load(fh)
    registry = data.OR_PREP_REGISTRY
    done, missing = [], []
    for slug, r in refresh.items():
        c = registry.get(slug)
        if not c:
            missing.append(slug)
            continue
        steps = [[str(t), " ".join(str(d).split())] for t, d in r["steps"]]
        c["steps_v840"] = steps
        c["steps"] = [f"{t}. {d}" for t, d in steps]
        lab = r["source_label"]
        c["steps_source_v840"] = lab[:1].upper() + lab[1:]
        if r.get("title"):
            c["title"] = r["title"]
        done.append(slug)
    return {"refreshed": len(done), "missing": missing}
