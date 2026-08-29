"""v20.10 focused postoperative safety layer for OR Tomorrow.

Adds a small number of procedure-specific, high-consequence postoperative failure
modes that are not adequately conveyed by family-level complication boilerplate.
The matcher is title/slug based so the layer remains robust to canonical slug naming.
"""

from or_csf_rescue_v269 import apply_or_csf_rescue_v269

TARGETS = [
    {
        "name": "tracheostomy",
        "triggers": ("tracheostomy",),
        "exclude": ("laryngectomy", "tracheoesophageal puncture", "tep"),
        "postop": [
            "In a fresh surgical tracheostomy, accidental decannulation or difficult reinsertion can create a false passage because the tract is not mature. Call experienced airway/ENT help, remove a clearly displaced tube that is not ventilating, and prioritize oxygenation through the upper airway when it remains anatomically usable; bag-mask ventilation and oral endotracheal intubation are generally safer than repeatedly forcing a tube through an immature tract. If the stoma must be used, re-establish the lumen under direct/endoscopic guidance with an appropriate same-size or smaller tube rather than blind probing.",
            "A tracheostomy patient is not automatically a neck-only airway: explicitly distinguish a standard tracheostomy from a total laryngectomy before choosing the rescue route. A laryngectomy patient must be oxygenated/ventilated through the stoma because the mouth and nose no longer communicate with the lungs.",
            "New brisk or sentinel bleeding from a tracheostomy, particularly days to weeks after placement, is a tracheo-innominate fistula warning until excluded and requires immediate airway/hemorrhage escalation and definitive operative or endovascular control planning.",
        ],
    },
    {
        "name": "endoscopic-sinus-surgery",
        "triggers": ("endoscopic sinus surgery", "fess"),
        "exclude": (),
        "postop": [
            "After endoscopic sinus surgery, sudden visual decline, RAPD, proptosis, ophthalmoplegia, severe orbital pain or a tense orbit should be treated as possible orbital compartment syndrome. Stop nonessential delays, obtain an immediate focused visual/pupillary/orbital examination, summon ophthalmology/ENT support, and if vision is threatened with convincing compartment syndrome proceed to urgent orbital decompression (classically lateral canthotomy with cantholysis, with further surgical decompression/source control as required) rather than waiting for routine imaging. Pressure-lowering medication is adjunctive and must not substitute for timely decompression.",
        ],
    },
    {
        "name": "tors",
        "triggers": ("tors", "transoral robotic"),
        "exclude": (),
        "postop": [
            "Brisk or recurrent bleeding after TORS is an airway-and-hemorrhage emergency. Activate anesthesia/OR and transfusion support as needed, keep aggressive suction available, position and temporize with direct pressure/packing only when safely accessible, and secure the airway early when ongoing bleeding, edema or aspiration threatens ventilation. Definitive control generally requires urgent transoral re-exploration and/or neck vascular control; angiographic embolization is a selected option when physiology and bleeding pattern permit, not a reason to delay control in an unstable patient. Avoid blind deep clamping in the oropharynx.",
            "A smaller sentinel bleed after TORS still warrants urgent assessment because it can precede major hemorrhage; do not discharge or simply observe a recurrent warning bleed without a defined airway and definitive-hemostasis plan.",
        ],
    },
    {
        "name": "tracheal-resection",
        "triggers": ("tracheal resection", "cricotracheal resection"),
        "exclude": (),
        "postop": [
            "After tracheal or cricotracheal resection, new subcutaneous emphysema, air leak, stridor, respiratory distress, wound separation, hemoptysis or rapidly progressive neck/mediastinal symptoms should raise concern for anastomotic dehiscence. Call the airway surgeon and anesthesia immediately, preserve the planned neck-flexion/tension-reduction strategy, and avoid repeated blind or traumatic instrumentation across the anastomosis. If airway control is required, obtain bronchoscopic/direct visualization and place the cuff distal to the anastomosis when feasible, followed by urgent operative evaluation for drainage, repair/reconstruction and vascularized buttress as dictated by the defect and tissue quality.",
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
    v269 = apply_or_csf_rescue_v269(registry)
    return {"targets": len(TARGETS), "applied": applied, "v269": v269}
