"""v38.9 — Thyroglossal duct cyst depth repair.

The shipped "Thyroglossal Duct Cyst" module (Pediatric Otolaryngology) had
two content-quality defects flagged directly on the Concept Hub card:
  1. recognize and localize were verbatim-duplicated text, so the six-stage
     card only actually taught four distinct stages.
  2. operate began with the unfilled generic authoring instruction ("For
     operative/procedural cases, explicitly state indication, setup,
     landmarks, danger structures, key steps, failure modes and
     postoperative plan.") rather than real advanced-decision content --
     a placeholder that was never replaced.

This enriches the existing canonical module in place (same pattern as
otitis_externa_depth_v157 / depth_enrichment_v158) rather than creating a
new topic, and fails loudly if the expected module is missing so drift is
caught rather than silently skipped.

Source basis: Bailey's Head and Neck Surgery-Otolaryngology (7e), ch. on
congenital neck masses; Cummings Otolaryngology-Head and Neck Surgery (7e),
pediatric neck masses chapter; Pasha & Golub, Otolaryngology-Head and Neck
Surgery: Clinical Reference Guide (6e), congenital neck mass section.
"""

TOPIC = "Thyroglossal Duct Cyst"
DOMAIN_CANDIDATES = ("Pediatric Otolaryngology",)

DEPTH_V389 = {
    "recognize": (
        "A thyroglossal duct cyst (TGDC) is a midline or near-midline anterior neck mass along "
        "the path of thyroid descent from the foramen cecum (tongue base) to the pretracheal "
        "position, most often at or just below the level of the hyoid bone. It classically "
        "elevates with swallowing and, distinctively, with tongue protrusion -- because the tract "
        "is tethered to the foramen cecum via the hyoid -- which separates it from other pediatric "
        "midline/off-midline neck masses (dermoid cyst moves with swallowing but not tongue "
        "protrusion; it does not track through the hyoid). Presentation is typically an "
        "asymptomatic, smooth, mobile cystic mass discovered in childhood, though it can present "
        "at any age and can enlarge or become tender/erythematous with an intercurrent upper "
        "respiratory infection due to secondary infection of retained epithelium."
    ),
    "localize": (
        "Localization follows the embryologic descent path of the thyroid: from the foramen cecum "
        "at the tongue base, through or just anterior to the body of the hyoid bone, down to the "
        "thyroid bed. About two-thirds of cysts are found at or below the hyoid; a minority are "
        "suprahyoid (near the tongue base/floor of mouth) or intralingual. Because the tract can "
        "pass anterior to, posterior to, or directly through the hyoid body, the hyoid -- not the "
        "cyst alone -- is the key anatomic landmark for both diagnosis and cure, not just a "
        "surrounding structure to avoid."
    ),
    "workup": (
        "Ultrasound is the first-line study: it confirms a cystic (vs. solid) midline mass and, "
        "critically, must confirm the presence of a normally located, normal-appearing thyroid "
        "gland before proceeding to excision, since 1-2% of patients have an ectopic thyroid with "
        "the TGDC representing their only functioning thyroid tissue. If ultrasound cannot "
        "definitively identify orthotopic thyroid tissue, obtain thyroid function tests and "
        "consider cross-sectional imaging (CT or MRI) or thyroid scintigraphy before surgery. "
        "Active infection should be treated with antibiotics (and aspiration if abscessed) before "
        "definitive excision, since operating through acutely infected tissue increases recurrence "
        "risk and surgical morbidity."
    ),
    "manage": (
        "Definitive management is the Sistrunk procedure: excision of the cyst en bloc with the "
        "central portion of the hyoid bone and a core of tissue along the tract up to the foramen "
        "cecum at the tongue base. Removing the central hyoid segment and tract -- not just the "
        "cyst -- is what distinguishes the Sistrunk procedure from simple cystectomy and is the "
        "reason it achieves markedly lower recurrence."
    ),
    "operate": (
        "Indication: confirmed TGDC with documented orthotopic thyroid tissue, quiescent (not "
        "acutely infected/abscessed) at the time of surgery. Setup: supine with neck extension, "
        "transverse incision centered over the mass/hyoid level. Key steps: dissect the cyst free "
        "circumferentially, identify and skeletonize the hyoid bone, resect the central (mid-body) "
        "segment of the hyoid along with the cyst, then core out the residual tract superiorly "
        "toward the foramen cecum -- classically to the base of tongue mucosa -- taking a generous "
        "cuff of surrounding strap/lingual musculature around the tract rather than trying to "
        "strip a thin cord. Danger structures: airway/foramen cecum region at the tongue base "
        "(avoid entering the oropharyngeal mucosa if possible; if entered, close it), and generally "
        "staying in the midline avoids the great vessels and hypoglossal/lingual nerves, which are "
        "only at risk if dissection strays laterally off the tract. Failure mode: incomplete "
        "removal of the central hyoid or an unrecognized branching/duplicated tract is the leading "
        "cause of recurrence -- simple cyst excision without the Sistrunk hyoid/tract component "
        "carries a recurrence rate as high as 40-50%, versus roughly 3-6% after a properly "
        "performed Sistrunk procedure. Postoperative plan: routine wound care, watch for hematoma "
        "or infection; recurrence, when it occurs, usually presents as a new mass along the same "
        "tract and warrants repeat imaging and revision Sistrunk."
    ),
    "teach": (
        "Teach the reasoning chain, not just the eponym: this is a remnant of the thyroid's "
        "embryologic migration route, so (1) confirm real thyroid tissue exists elsewhere before "
        "you remove the cyst, and (2) cure requires resecting the hyoid and tract the cyst is "
        "tethered to, not just the cyst itself -- that is precisely why simple excision fails at "
        "such a high rate while the Sistrunk procedure does not."
    ),
}


def apply_thyroglossal_duct_cyst_depth_v389(data_module):
    module = None
    for domain in DOMAIN_CANDIDATES:
        for candidate in data_module.DEEP_MODULES_V6.get(domain, []):
            if candidate.get("topic") == TOPIC:
                module = candidate
                break
        if module:
            break
    if module is None:
        raise RuntimeError(
            f"v38.9: expected canonical topic {TOPIC!r} not found under {DOMAIN_CANDIDATES!r}"
        )
    module.update(DEPTH_V389)
    return {"enriched": TOPIC}
