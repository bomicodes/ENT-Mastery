"""v15.8 — Etiology/risk-factor depth enrichment.

Found by sampling the deep curriculum broadly and reading full recognize/
localize text for diagnosis-type topics (not procedural/technique topics,
which legitimately don't need this). Four topics were genuinely thin on why
the condition happens and who is at risk, as opposed to simply how it
presents:

- BPPV: no mention of the actual otolith mechanism or known associations
  (trauma, prior vestibular neuritis, aging, migraine).
- Recurrent Acute Rhinosinusitis: no diagnostic threshold, no mention that
  recurrence itself should prompt workup for an underlying cause (allergy,
  immunodeficiency, anatomic variant, undiagnosed CRS).
- Thyroid Nodule: covered management urgency triggers but never named the
  classic malignancy risk factors (radiation exposure, family history/MEN),
  which is one of the more commonly tested facts about this topic.
- Choanal Atresia: no mention of the CHARGE association, a high-yield fact
  since bilateral atresia should specifically prompt CHARGE workup.

In-place enrichment of existing canonical topics, same pattern as
otitis_externa_depth_v157.py — no new topics created, fails loudly if the
target module cannot be found rather than silently no-op'ing.
"""

DEPTH_ENRICHMENT_V158 = {
    ("Otology / Neurotology", "BPPV"): {
        "recognize": (
            "Brief vertigo triggered by position change with reproducible canal-specific "
            "positional nystagmus is a mechanical otolith disorder. Persistent spontaneous "
            "vertigo or atypical neurologic nystagmus should trigger a different differential. "
            "Mechanistically, BPPV results from otoconia (calcium carbonate crystals) that have "
            "become dislodged from the utricular macula and migrated into a semicircular canal "
            "(most often posterior, given its dependent position), where their movement with "
            "head position abnormally stimulates the canal's cupula. Most cases are idiopathic, "
            "but recognized associations include head trauma, prior vestibular neuritis or "
            "labyrinthitis, prolonged bed rest or immobility, migraine, and age-related "
            "degeneration of the otolithic membrane — inquire about these when a cause isn't "
            "obvious, since recurrent or atypical BPPV in a younger patient without an "
            "identifiable trigger warrants a closer look."
        ),
        "localize": (
            "The posterior semicircular canal is affected in the large majority of cases given "
            "its dependent anatomic position relative to the utricle; horizontal and, rarely, "
            "anterior canal involvement produce distinct nystagmus patterns and require different "
            "repositioning maneuvers. Distinguish canalithiasis (free-floating debris, the more "
            "common pattern, with nystagmus that is transient and fatigable) from cupulolithiasis "
            "(debris adherent to the cupula, producing more persistent, non-fatiguing nystagmus)."
        ),
    },
    ("Rhinology / Allergy / Skull Base", "Recurrent Acute Rhinosinusitis"): {
        "recognize": (
            "Discrete bacterial-pattern episodes with symptom-free intervals are different from "
            "chronic daily symptoms. Recurrent acute rhinosinusitis is generally defined as four "
            "or more distinct episodes of acute bacterial rhinosinusitis in a year, each meeting "
            "criteria for acute disease with resolution of symptoms between episodes — the "
            "symptom-free interval is what separates this from chronic rhinosinusitis with "
            "exacerbations. The recurrence pattern itself is a clinical signal, not just a "
            "frequency count: it should prompt a search for an underlying driver rather than "
            "repeated courses of antibiotics alone."
        ),
        "localize": (
            "Consider and evaluate for predisposing factors specifically because they are "
            "identifiable and often modifiable: allergic rhinitis and other atopic disease, "
            "anatomic variants that impair sinus drainage (significant septal deviation, "
            "concha bullosa, Onodi cell obstructing natural ostia), immunodeficiency (screen "
            "when episodes are unusually frequent or severe), and, in children, cystic fibrosis "
            "or primary ciliary dyskinesia when accompanied by other suggestive features. "
            "Biofilm-associated bacterial persistence is also increasingly recognized as a "
            "contributor to a recurrent pattern rather than true reinfection each time."
        ),
    },
    ("Thyroid / Parathyroid / Salivary", "Thyroid Nodule"): {
        "recognize": (
            "A thyroid nodule is a malignancy-risk and symptom problem, not an automatic "
            "surgical diagnosis. Suspicious nodes, hoarseness, rapid growth or fixation change "
            "urgency. Specific history should be taken for known malignancy risk factors: prior "
            "head/neck external-beam radiation exposure (including childhood radiation "
            "therapy), a family history of thyroid cancer or a hereditary syndrome such as MEN2 "
            "(RET-associated) or PTEN hamartoma syndrome, and — while most nodules occur in "
            "women — nodules in male patients and in patients at the extremes of age carry a "
            "higher relative likelihood of malignancy and should lower the threshold for "
            "biopsy even when ultrasound features look otherwise reassuring."
        ),
    },
    ("Pediatric Otolaryngology", "Choanal Atresia"): {
        "recognize": (
            "Neonatal bilateral obstruction causes cyclical cyanosis/respiratory distress "
            "(worse with feeding, relieved by crying); unilateral disease presents later with "
            "chronic unilateral symptoms such as persistent unilateral rhinorrhea or congestion, "
            "sometimes not recognized until childhood. Choanal atresia is associated with CHARGE "
            "syndrome (Coloboma, Heart defects, Atresia choanae, Retarded growth/development, "
            "Genital abnormalities, Ear abnormalities) often enough that any infant with "
            "confirmed choanal atresia — particularly bilateral — should be evaluated for other "
            "CHARGE features and undergo appropriate genetic/syndromic workup rather than being "
            "treated as an isolated anatomic finding."
        ),
    },
}


def apply_depth_enrichment_v158(deep_modules):
    """Enrich existing modules in place by exact (domain, topic) match.
    Fails loudly if any target module cannot be found, matching the
    established defensive pattern from otitis_externa_depth_v157."""
    applied = []
    missing = []
    for (domain, topic), fields in DEPTH_ENRICHMENT_V158.items():
        modules = deep_modules.get(domain, [])
        found = False
        for module in modules:
            if module.get("topic") == topic:
                module.update(fields)
                applied.append((domain, topic))
                found = True
                break
        if not found:
            missing.append((domain, topic))
    if missing:
        raise RuntimeError(
            f"v15.8: could not find {len(missing)} target module(s) for depth "
            f"enrichment, refusing to silently skip: {missing}"
        )
    return applied
