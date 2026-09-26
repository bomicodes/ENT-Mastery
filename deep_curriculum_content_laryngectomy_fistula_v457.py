"""ENT Mastery v45.7 -- Content addition (not a readability rewrite): laryngectomy
fistula/reconstruction and partial-laryngectomy candidacy teaching points requested
directly by the user, with claim-level sourcing for every new numeric statement.

Adds, to two existing Head & Neck Oncology topics:
  - Total Laryngectomy: preoperative thyroid-function checking, and the specific
    fistula-rate data behind why vascularized-tissue (pedicled/free flap)
    reconstruction is favored in salvage laryngectomy and extensive-resection
    primary cases rather than after an uncomplicated primary closure.
  - Open Partial / Conservation Laryngectomy: why significant COPD/limited
    pulmonary reserve is a contraindication to hemilaryngectomy and other
    conservation procedures (expected postoperative aspiration during swallow
    relearning), and why true-vocal-fold/glottic involvement is a contraindication
    to supraglottic laryngectomy specifically (it is a horizontal resection that
    depends on an intact glottis for postoperative airway protection).

All four additions were explicitly checked against the existing content before
writing this module (2026-09-25 conversation) and were absent -- this is new
material, not a rephrasing. Every added sentence carrying a number (fistula-rate
percentages, odds ratios, confidence intervals) is backed by a specific study
in that topic's source_basis, appended below the existing list rather than
replacing it. The COPD/hemilaryngectomy and glottic-involvement/supraglottic
points are standard operative-candidacy teaching already covered by each
topic's existing domain-foundational textbook citations (Cummings 7e Ch.
Conservation Laryngeal Surgery, Pasha & Golub 6e Ch 6, K.J. Lee 12e) and did
not need a new source added.

Follows the established deepcopy -> mutate copy -> dict.clear()/update()
pattern so DEEP_MODULES_V6 object identity is preserved for the cache-
fingerprint system in concept_check_board_repair_v177.py.
"""

from copy import deepcopy

DOMAIN = "Head & Neck Oncology"

FIELD_UPDATES = {
    "Total Laryngectomy": {
        "workup": (
            "Pre-op staging, pulmonary/nutritional assessment, speech "
            "rehabilitation planning and counseling about permanent stoma. "
            "**Check thyroid function preoperatively**, especially after prior "
            "neck irradiation or thyroidectomy: postoperative hypothyroidism is "
            "associated with pharyngocutaneous fistula (see "
            "Manage), not just a metabolic afterthought."
        ),
        "manage": (
            "Resection + pharyngeal closure ± neck treatment/reconstruction; "
            "postoperative fistula and swallow management are major issues. "
            "**Fistula risk drives reconstructive choice**. In salvage "
            "laryngectomy after failed chemoradiation, primary closure alone "
            "carries a high fistula rate -- one comparative series found 78.6% "
            "versus 30.8% with a prophylactic pectoralis major flap (p=0.047), "
            "and a 2022 network meta-analysis of 1,694 patients found pedicled "
            "flap onlay reduced the odds of fistula versus primary closure alone "
            "(OR 0.35, 95% CI 0.20-0.61). **Why vascularized tissue helps**: "
            "previously irradiated, poorly vascularized pharyngeal mucosa heals "
            "poorly on its own, and a flap brings in a new, non-irradiated blood "
            "supply to reinforce the closure rather than relying on the "
            "compromised native tissue. This is why free or pedicled flap "
            "reinforcement is favored in salvage cases and in primary cases with "
            "an extensive resection (large mucosal deficit, prior radiation, or "
            "a closure under tension), rather than after an uncomplicated "
            "primary resection with adequate remaining mucosa, where primary "
            "closure alone is often sufficient. **Thyroid function**: "
            "postoperative hypothyroidism is an independent, modifiable fistula "
            "risk marker -- one series found a 47% fistula rate in patients who "
            "became hypothyroid after laryngectomy versus 23% in those who "
            "stayed euthyroid (OR 3.6, 95% CI 1.8-7.1), with reoperation in "
            "24.4% versus 5.4% (OR 11.4, 95% CI 2.6-49.9) and roughly a 12.5% "
            "incremental rise in absolute fistula risk with each doubling of "
            "TSH. Check thyroid function early postoperatively and replace "
            "promptly when hypothyroidism is present, particularly after prior "
            "neck irradiation or thyroidectomy. These observational data "
            "establish an association; they do not prove that replacement "
            "prevents fistula."
        ),
    },
    "Open Partial / Conservation Laryngectomy": {
        "workup": (
            "Endoscopy plus imaging define extent and mobility. Patient "
            "pulmonary/swallowing reserve and ability to rehabilitate are part "
            "of candidacy. **Pulmonary reserve is a hard gate, not a soft "
            "preference**: partial laryngectomy (hemilaryngectomy, "
            "supracricoid, supraglottic) sacrifices part of the glottic or "
            "supraglottic sphincter, producing an expected period of "
            "postoperative aspiration during swallow relearning. A patient with "
            "significant COPD or otherwise limited pulmonary reserve and cough "
            "clearance cannot protect the airway or clear aspirated secretions "
            "through that window, so significant COPD is a relative-to-absolute "
            "contraindication to hemilaryngectomy and other conservation "
            "procedures -- it converts an intended voice- and swallow-"
            "preserving operation into chronic aspiration, recurrent "
            "pneumonia, or an unplanned total laryngectomy. Total laryngectomy "
            "avoids this problem entirely by separating the airway from the "
            "alimentary tract, which is part of why it can be the better "
            "choice in a marginal-pulmonary-reserve patient even when the "
            "tumor itself is technically resectable by conservation surgery."
        ),
        "operate": (
            "Know supraglottic and supracricoid principles, arytenoid "
            "preservation, pexy/reconstruction and the major complications of "
            "aspiration, edema/stenosis and delayed decannulation. "
            "**Supraglottic laryngectomy is a horizontal resection that "
            "depends on an intact glottis**: it removes the epiglottis, false "
            "cords, and pre-epiglottic space above the ventricle while "
            "deliberately preserving the true vocal folds and their closure "
            "mechanism, which is what is left to protect the airway "
            "afterward. **Key trap**: true-vocal-fold (glottic) involvement, "
            "impaired cord mobility, anterior commissure or subglottic "
            "extension, and cricoarytenoid joint fixation are all "
            "reasons to reconsider a standard supraglottic resection: true "
            "glottic extension cannot be removed with this operation, and "
            "impaired glottic closure may compromise airway protection. "
            "Proximity to the anterior commissure alone is not an absolute "
            "contraindication if an adequate margin and functional glottis "
            "can be preserved. Glottic involvement should redirect planning "
            "toward supracricoid partial laryngectomy, if disease extent and "
            "pulmonary reserve still allow conservation, or toward total "
            "laryngectomy -- not toward extending a supraglottic resection down "
            "onto the cords."
        ),
    },
}

NEW_SOURCES = {
    "Total Laryngectomy": [
        "Fistula rate 78.6% (primary closure) vs 30.8% (pectoralis major flap), p=0.047, PMID 30683565, Braz J Otorhinolaryngol -- 'Salvage total laryngectomy: is a flap necessary?'",
        "Pedicled flap onlay OR 0.35 (95% CI 0.20-0.61) vs primary closure for fistula, n=1,694, PMID 35731297, Eur Arch Otorhinolaryngol 2022 -- 'Surgical prevention of pharyngocutaneous fistula in salvage total laryngectomy: a systematic review and network meta-analysis'",
        "Hypothyroidism vs euthyroid fistula rate 47% vs 23% (OR 3.6, 95% CI 1.8-7.1), reoperation 24.4% vs 5.4% (OR 11.4, 95% CI 2.6-49.9), ~12.5% incremental absolute fistula-risk rise per TSH doubling, PMID 29264671, Ann Surg Oncol 2017 -- 'Hypothyroidism and Wound Healing After Salvage Laryngectomy' (Rosko et al.)",
        "Kennedy et al., 'Association of Hypothyroidism With Wound Complications Post-Laryngectomy: A Systematic Review and Meta-Analysis', Laryngoscope 2025, PMID 40673661 -- corroborating systematic review.",
    ],
}


def apply_deep_curriculum_content_laryngectomy_fistula_v457(data_module, app_module=None):
    deep_source = getattr(data_module, "DEEP_MODULES_V6", None)
    if not isinstance(deep_source, dict):
        raise RuntimeError("v45.7: DEEP_MODULES_V6 unavailable")
    original_mods = deep_source.get(DOMAIN)
    mods = deepcopy(original_mods) if original_mods else None
    if not mods:
        raise RuntimeError(f"v45.7: domain not found: {DOMAIN!r}")
    by_topic = {m.get("topic"): m for m in mods}
    missing_topics = [t for t in FIELD_UPDATES if t not in by_topic]
    if missing_topics:
        raise RuntimeError(f"v45.7: missing topics: {missing_topics}")

    fields_updated = 0
    topics_updated = 0
    for topic, fields in FIELD_UPDATES.items():
        row = by_topic[topic]
        touched = False
        for field, text in fields.items():
            if row.get(field) != text:
                row[field] = text
                fields_updated += 1
                touched = True
        extra_sources = NEW_SOURCES.get(topic)
        if extra_sources:
            existing = row.get("source_basis")
            if isinstance(existing, list):
                for src in extra_sources:
                    if src not in existing:
                        existing.append(src)
                        touched = True
        if touched:
            topics_updated += 1

    deep_source[DOMAIN] = mods
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6
    return {"topics_updated": topics_updated, "fields_updated": fields_updated}
