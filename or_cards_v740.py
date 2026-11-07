"""v74.0: OR Tomorrow card for tracheocutaneous fistula closure.

The site covered decannulation (Pediatric Tracheostomy / Decannulation) but had no operative
card for closing a persistent tracheocutaneous fistula. Linked to that topic so the card carries
its curriculum content. Installed before or_merge_v610.
"""

SLUG = "tracheocutaneous-fistula-closure"
TOPIC = "Pediatric Tracheostomy / Decannulation"

CARD_V740 = {
    "title": "Tracheocutaneous Fistula Closure",
    "domain": "Pediatric Airway",
    "linked_topic": TOPIC,
    "or_family_v190": "airway",
    "indications": (
        "A tracheocutaneous fistula that persists after successful decannulation, usually observed for a few "
        "months first because many stomas close on their own, and closed when it causes air leak with speech or "
        "cough, secretions, skin irritation, recurrent infection, aspiration risk, or interference with bathing, "
        "swimming or social life. Persistence is more likely after long-term tracheostomy (the tract becomes "
        "epithelialized), which is why it is common in children with tracheostomies of a year or more; a tracheostomy placed at a younger age also predicts persistence. Close only "
        "once the airway is clearly stable without the tube."
    ),
    "setup": [
        "Confirm durable decannulation: the child has been off the tube for months (many surgeons wait about 3 to 6 months or longer), with no stridor, increased work of breathing or sleep-disordered breathing, and no planned surgery or illness that might need the tracheostomy back.",
        "Review the airway history and the original indication. Consider airway endoscopy (direct laryngoscopy and bronchoscopy) before or at the time of closure to look for suprastomal collapse, granulation tissue, subglottic stenosis or tracheomalacia; a polysomnogram helps when sleep-disordered breathing is suspected.",
        "Decide on the technique: fistulectomy with layered primary closure, or fistulectomy with healing by secondary intention. Very small, short tracts are sometimes treated less invasively; large defects may need a local flap.",
        "Plan the airway with anesthesia: usually oral intubation with the cuff positioned below the fistula so the field is sealed, or mask or laryngeal mask airway for small tracts. Plan a smooth emergence: return to spontaneous ventilation and minimize positive pressure and coughing before extubation, since these drive air leak.",
        "Plan admission and monitoring. Children are commonly observed overnight (some centers use the ICU after primary closure) for airway compromise and air leak; secondary-intention closure usually shortens the stay.",
    ],
    "landmarks": [
        "the epithelialized fistula tract from skin to the anterior tracheal wall",
        "anterior tracheal wall and the tracheal opening at the fistula base",
        "strap muscles (sternohyoid, sternothyroid), which can be reapproximated over the closure",
        "thyroid isthmus and anterior jugular veins near a low or wide stoma",
        "cricoid cartilage above a high stoma",
    ],
    "steps": [
        "Infiltrate local anesthetic with epinephrine and make an elliptical incision around the fistula, oriented in a skin crease.",
        "Dissect the epithelialized tract circumferentially down to the trachea, keeping the dissection close to the tract.",
        "Excise the tract at the level of the tracheal wall, removing all epithelium so the opening can heal.",
        "Primary closure: close the tracheal opening (or its surrounding soft tissue) with absorbable sutures, reapproximate the strap muscles in the midline, then close subcutaneous tissue and skin. Some surgeons place a small drain.",
        "Secondary intention: after excising the tract, leave the tracheal opening and skin open or loosely approximated under a light dressing to granulate closed.",
        "Before finishing a primary closure, many surgeons ask anesthesia for positive-pressure ventilation (a leak test) under saline to check that the closure is airtight.",
    ],
    "danger": [
        "Air leak into the tissues after an airtight skin closure over a trachea that still leaks: subcutaneous emphysema, pneumomediastinum and pneumothorax.",
        "Airway compromise after closure from edema, hematoma, or a previously hidden suprastomal collapse or stenosis that the stoma had been bypassing.",
        "Closing before the child truly tolerates decannulation, so a new tracheostomy is needed.",
        "Injury to the anterior jugular veins or thyroid isthmus with a low or wide stoma.",
    ],
    "exit_check": [
        "Airtight closure on the positive-pressure leak test (for primary closure), hemostasis secured, and no tension on the skin.",
        "Plan monitoring for stridor, desaturation, neck swelling and crepitus; a chest x-ray if air leak is suspected.",
    ],
    "postop": [
        "Observe overnight in children (often with continuous pulse oximetry). Watch for stridor, work of breathing, neck swelling and crepitus.",
        "Subcutaneous emphysema: open the skin closure to release trapped air and get a chest x-ray to look for pneumothorax or pneumomediastinum; urgent airway assessment if breathing worsens.",
        "Limit coughing and straining where possible early on. After secondary-intention closure, expect small air bubbling and drainage through the wound for days to weeks while it granulates closed.",
        "Wound care and follow-up for infection, dehiscence, a recurrent fistula and a depressed scar, which can be revised later.",
    ],
    "complications": {
        "early": [
            "Subcutaneous emphysema, pneumomediastinum or pneumothorax from air leak.",
            "Airway obstruction from edema, hematoma or unmasked airway disease.",
            "Wound infection or dehiscence.",
        ],
        "late": [
            "Recurrent fistula.",
            "Depressed or tethered scar.",
            "Need for re-tracheostomy if the airway was not ready.",
        ],
    },
    "attending_followup": [
        ["How long do you wait after decannulation before closing a fistula, and why?",
         "Usually a few months (many wait about 3 to 6 months): it lets small stomas close on their own and proves the child tolerates decannulation, including through illness and sleep, before giving up the stoma as a backup airway."],
        ["Why does a tracheostomy stoma fail to close?",
         "The tract becomes lined with epithelium (skin grows down to the trachea), which happens with long-term tracheostomy. An epithelialized tract will not heal until the epithelium is excised."],
        ["Primary closure versus secondary intention: what is the trade-off?",
         "Both close more than 90% of fistulas, and pooled data show no significant difference in success, revision, infection or air leak (subcutaneous emphysema or pneumothorax). Secondary intention usually means a shorter operation and shorter ICU and hospital stay, but the wound heals over weeks and may leave a wider, depressed scar. Primary closure heals faster with a neater scar, but an airtight skin closure over a leaking trachea can trap air, so leak-test it and keep emergence smooth."],
        ["What do you do if the neck swells with crepitus a few hours after primary closure?",
         "Assess the airway first, open the skin closure to release the trapped air, and get a chest x-ray for pneumothorax or pneumomediastinum. Worsening breathing needs urgent airway management."],
        ["Why scope the airway before or at closure?",
         "Suprastomal collapse, granulation tissue, stenosis or tracheomalacia may have been bypassed by the stoma. Finding them first prevents an airway crisis after the stoma is closed."],
    ],
    "source_basis": [
        "Cummings Otolaryngology—Head and Neck Surgery, 7e — pediatric tracheotomy and decannulation; tracheocutaneous fistula.",
        "Bluestone and Stool's Pediatric Otolaryngology, 5e — tracheotomy, decannulation and tracheocutaneous fistula closure.",
        "Pasha & Golub, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — Pediatric Laryngoesophagology: tracheotomy.",
        "Mitchell RB et al. Clinical Consensus Statement: Tracheostomy Care. Otolaryngol Head Neck Surg. 2013;148(1):6-20.",
        "Lewis S, Arjomandi H, Rosenfeld R. Systematic review of surgery for persistent pediatric tracheocutaneous fistula. Laryngoscope. 2017;127(1):241-246.",
        "Cheng J, Setabutr D. Tracheocutaneous fistula closure in children: primary closure vs secondary intention, a meta-analysis. Int J Pediatr Otorhinolaryngol. 2016;89:107-111.",
        "Kennedy A, Hart CK, de Alarcon A, et al. International Pediatric Otolaryngology Group (IPOG) management recommendations: pediatric tracheostomy decannulation. Int J Pediatr Otorhinolaryngol. 2021;141:110565.",
    ],
}


def install_or_cards_v740(data, app_mod):
    import textbook_curriculum_v470
    registry = data.OR_PREP_REGISTRY
    if SLUG not in registry:
        c = {k: (list(v) if isinstance(v, list) else dict(v) if isinstance(v, dict) else v) for k, v in CARD_V740.items()}
        c["attending_followup"] = [list(p) for p in CARD_V740["attending_followup"]]
        c["complications"] = {k: list(v) for k, v in CARD_V740["complications"].items()}
        c.update({"slug": SLUG, "status": "authored-v74.0", "review_status_v190": "operative-depth reviewed",
                  "sequence_status_v200": "procedure-specific", "sources": list(CARD_V740["source_basis"])})
        registry[SLUG] = c
    m = textbook_curriculum_v470.TOPIC_OR_MAP_V470.setdefault(TOPIC, [])
    if SLUG not in m:
        m.insert(0, SLUG)
    if getattr(app_mod, "OR_PREP_REGISTRY", None) is not registry:
        app_mod.OR_PREP_REGISTRY = registry
    return {"added": [SLUG]}
