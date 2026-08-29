"""v17.8 — preserve clinically distinct disease entities after canonicalization.

Comparison/parent nodes may coexist with disease-specific nodes. This runtime
safeguard restores a standalone pediatric Epiglottitis module if a historical
canonicalization pass collapsed it into "Croup vs Epiglottitis", and verifies
that necrotizing otitis externa remains distinct from uncomplicated AOE.

v27.5 also invokes the source-grounded salivary Concept Hub repair after the
historical deep-curriculum loaders have finished.
"""


def _find(modules, topic):
    return next((m for m in modules or [] if m.get("topic") == topic), None)


EPIGLOTTITIS_MODULE_V178 = {
    "topic": "Epiglottitis",
    "recognize": (
        "Suspect epiglottitis in a toxic-appearing child with abrupt fever, severe odynophagia or dysphagia, "
        "drooling, muffled voice, tripod positioning, and respiratory distress; classic barking cough is absent. "
        "Vaccination has reduced Hib disease, but epiglottitis remains an airway emergency and can be caused by "
        "other bacterial pathogens."
    ),
    "localize": (
        "The dangerous process is supraglottic inflammation involving the epiglottis and adjacent supraglottic "
        "structures. Progressive edema can rapidly narrow the pediatric airway; agitation or traumatic pharyngeal "
        "examination can worsen obstruction."
    ),
    "workup": (
        "Airway stability determines the workup. Do not delay airway control for radiography or routine throat "
        "examination in an unstable child. If the child is stable and the diagnosis is uncertain, imaging may support "
        "the diagnosis, but definitive evaluation is controlled visualization of the supraglottis in an environment "
        "where the airway can be secured. Obtain cultures after the airway is controlled when feasible."
    ),
    "manage": (
        "Keep the child calm, provide oxygen as tolerated, mobilize ENT/anesthesia/pediatric critical care, and secure "
        "the airway in a controlled setting when respiratory compromise or significant obstruction is present. Treat "
        "with appropriate intravenous antibiotics covering likely bacterial pathogens and manage in a monitored setting."
    ),
    "operate": (
        "Airway intervention is the operative priority, not diagnostic laryngoscopy for its own sake. Controlled "
        "intubation in the operating room is preferred when feasible, with surgical-airway capability immediately "
        "available. Avoid repeated traumatic attempts; the threshold for securing the airway is driven by clinical "
        "trajectory, work of breathing, oxygenation, and endoscopic severity."
    ),
    "teach": (
        "Board distinction: croup is usually viral with barking cough and subglottic disease; epiglottitis is a "
        "supraglottic bacterial airway emergency characterized by toxicity, drooling, dysphagia, muffled voice, and "
        "tripod positioning. In suspected epiglottitis, airway planning comes before a complete office examination."
    ),
    "source_basis": [
        "Pasha 6e",
        "K.J. Lee 12e",
        "Cummings 7e reconciliation",
        "current pediatric airway/infectious disease evidence",
    ],
    "restored_distinct_entity_v178": True,
}


def apply_distinct_entities_v178(data):
    restored = []
    verified = []

    ped = data.DEEP_MODULES_V6.setdefault("Pediatric Otolaryngology", [])
    if _find(ped, "Epiglottitis") is None:
        m = dict(EPIGLOTTITIS_MODULE_V178)
        m["concept_id"] = data._v6_item_id("Pediatric Otolaryngology", "Epiglottitis")
        ped.append(m)
        restored.append(("Pediatric Otolaryngology", "Epiglottitis"))

    oto = data.DEEP_MODULES_V6.get("Otology / Neurotology", [])
    aoe = _find(oto, "Acute Otitis Externa")
    noe = _find(oto, "Necrotizing Otitis Externa")
    if aoe is not None and noe is not None and aoe is not noe:
        verified.append(("Otology / Neurotology", "AOE_and_NOE_distinct"))

    # Source-ground the legacy salivary card at the same post-canonicalization
    # point.  Keeping this call here avoids another production-entrypoint shim.
    from deep_curriculum_salivary_v275 import apply_salivary_concept_rebuild_v275
    salivary = apply_salivary_concept_rebuild_v275(data)

    return {"restored": restored, "verified": verified, "salivary_v275": salivary}
