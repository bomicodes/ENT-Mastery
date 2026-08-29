"""v28.3 — source-grounded reoperative hyperparathyroidism Concept Hub rebuild.

Keeps reoperative hyperparathyroidism distinct from the primary and renal HPT cards by
centering confirmation of failure, review of the index operation, high-confidence
localization, risk-selected re-exploration, and scarred-neck operative strategy.

Production compatibility note: runtime_entry.py already imports and executes this module.
Until the generated production entrypoint is next consolidated, v28.4-v28.9 are
deliberately chained here so the later source-grounded rebuilds cannot remain orphan
source files on Render.
"""

import re
from deep_curriculum_otology_v284 import apply_otology_etd_rebuild_v284
from deep_curriculum_rhinology_v285 import apply_rhinology_rhinitis_rebuild_v285
from deep_curriculum_headneck_v286 import apply_headneck_neck_dissection_rebuild_v286
from deep_curriculum_headneck_v287 import apply_headneck_salvage_rebuild_v287
from deep_curriculum_headneck_v288 import apply_headneck_palliative_rebuild_v288
from deep_curriculum_headneck_v289 import apply_headneck_free_flap_rebuild_v289

DOMAIN = "Thyroid / Parathyroid / Salivary"
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


REOPERATIVE_PARATHYROID_V283 = {
    "reoperative hyperparathyroidism": {
        "recognize": (
            "Recognize reoperative primary hyperparathyroidism as a FAILURE/RECURRENCE problem, not simply another presentation of untreated PHPT. Persistent PHPT means failure to achieve normocalcemia within 6 months of parathyroidectomy; recurrent PHPT means hypercalcemia returning after a normocalcemic interval of more than 6 months. Before blaming a missed gland, reconfirm PTH-dependent hypercalcemia and revisit the original diagnosis—review calcium/PTH trends, renal function, vitamin-D status, medications, and whether familial hypocalciuric hypercalcemia or another mimic was ever adequately excluded."
        ),
        "localize": (
            "Localize WHY the first operation failed and WHERE hyperfunctioning tissue is likely to remain. Review the original operative note, gland-by-gland findings, pathology, intraoperative PTH curve, postoperative calcium trajectory, and any prior imaging before ordering new studies. Failure patterns include a missed normal-position or ectopic gland, unrecognized multigland disease, a supernumerary gland, incompletely resected tissue, or rarely parathyromatosis/carcinoma. Re-map embryologic hiding places—intrathymic/mediastinal inferior glands, retroesophageal or tracheoesophageal-groove tissue, carotid-sheath sites, and unusually descended superior glands—while also documenting the expected location of any known remaining glands."
        ),
        "workup": (
            "Do not re-enter a scarred neck until the biochemical diagnosis, indication, and target have been rebuilt from first principles. Repeat calcium (albumin-adjusted or ionized) and intact PTH and reassess renal/bone indications as in primary disease. Obtain preoperative laryngeal examination because a pre-existing vocal-fold paresis fundamentally changes risk counseling. Localization usually begins with expert cervical ultrasound plus sestamibi/SPECT-CT; 4D-CT is particularly useful when first-line studies are negative or discordant, and 18F-fluorocholine PET/CT can be valuable in difficult persistent/recurrent disease where available. Reserve invasive localization such as selective venous PTH sampling for carefully selected patients with confirmed disease and a surgical indication when noninvasive studies remain nonlocalizing or conflicting."
        ),
        "manage": (
            "Apply a HIGHER threshold for reoperation than for a straightforward index parathyroidectomy because scarred-neck exploration carries greater recurrent-laryngeal-nerve and permanent hypoparathyroidism risk. Reoperate for a meaningful guideline-based indication—symptomatic hypercalcemia, renal or skeletal end-organ disease, substantial biochemical disease, or another compelling indication—not merely because PTH is mildly elevated. If a patient does not have a clear indication or a credible target, optimize medical surveillance/therapy and continue localization rather than performing a blind exploration. When reoperation is appropriate, refer to a high-volume parathyroid surgeon and explicitly counsel that cure and complication profiles differ from first-time surgery."
        ),
        "operate": (
            "Re-exploration should be TARGET-DIRECTED whenever possible. Enter through the safest anticipated plane, use the prior operative map to predict scar and residual anatomy, and identify/protect the recurrent laryngeal nerve before aggressive dissection around a suspected gland. Intraoperative PTH is especially useful to test whether the localized target explains the biochemistry and whether additional hyperfunctioning tissue remains. Search ectopic or mediastinal sites according to embryology rather than escalating to indiscriminate bilateral scar dissection. If multigland disease is encountered, preserve a viable source of parathyroid function whenever oncologically appropriate; autotransplantation/cryopreservation considerations depend on the amount and quality of remaining tissue and institutional practice. The operative endpoint is durable biochemical cure with acceptable nerve/parathyroid function—not simply removal of something that looks enlarged."
        ),
        "teach": (
            "Chief/boards framework: CONFIRM → RECONSTRUCT THE FIRST OPERATION → LOCALIZE → SELECT → RE-EXPLORE. Persistent = never normocalcemic through 6 months; recurrent = hypercalcemia after more than 6 months of documented normocalcemia. Imaging is still not the diagnosis, but in a reoperative neck it becomes essential risk-mapping: do not perform a blind redo exploration for a weak biochemical indication. A 'missing gland' may be ectopic, supernumerary, or part of multigland disease, so review embryology and prior pathology before assuming technical failure. The two complications to fear more than at the index operation are recurrent-laryngeal-nerve injury and permanent hypoparathyroidism; preoperative vocal-fold status and a plan for the last functioning parathyroid tissue belong in the decision before incision."
        ),
        "tags": [
            "reoperative hyperparathyroidism", "persistent primary hyperparathyroidism",
            "recurrent primary hyperparathyroidism", "reoperative parathyroidectomy",
            "4D CT", "fluorocholine PET", "selective venous sampling",
            "intraoperative PTH", "ectopic parathyroid", "recurrent laryngeal nerve"
        ],
        "source_basis": [
            "Cummings Otolaryngology—Head and Neck Surgery, 7e — reoperative parathyroid surgery, ectopic anatomy, localization, and complication avoidance",
            "K.J. Lee's Essential Otolaryngology, 12e — persistent/recurrent hyperparathyroidism and re-exploration principles",
            "Pasha, Otolaryngology—Head & Neck Surgery: Clinical Reference Guide, 6e — parathyroid reoperation and operative pearls",
            "American Association of Endocrine Surgeons — Guidelines for Definitive Management of Primary Hyperparathyroidism (JAMA Surg 2016) — persistent/recurrent definitions, cure, and reoperative principles",
            "Persistent and Recurrent Primary Hyperparathyroidism: Etiological Factors and Pre-Operative Evaluation (Med Bull Sisli Etfal Hosp 2023) — structured review of prior surgery and staged reoperative localization",
        ],
    },
}


def apply_reoperative_parathyroid_rebuild_v283(data_module, app_module=None):
    modules = (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).get(DOMAIN, [])
    patched = []
    for module in modules:
        key = _norm(module.get("topic"))
        payload = REOPERATIVE_PARATHYROID_V283.get(key)
        if not payload:
            continue
        for field in FIELDS:
            module[field] = payload[field]
        module["tags"] = list(payload["tags"])
        module["source_basis"] = list(payload["source_basis"])
        module["source_grounded_v283"] = True
        patched.append(module.get("topic"))
    if app_module is not None:
        app_module.DEEP_MODULES_V6 = data_module.DEEP_MODULES_V6

    # Production chain: runtime_entry.py already invokes this function. Apply each
    # subsequent source-grounded rebuild to the same live curriculum object before
    # Concept Checks are regenerated.
    etd_result = apply_otology_etd_rebuild_v284(data_module, app_module)
    rhinitis_result = apply_rhinology_rhinitis_rebuild_v285(data_module, app_module)
    neck_dissection_result = apply_headneck_neck_dissection_rebuild_v286(data_module, app_module)
    salvage_result = apply_headneck_salvage_rebuild_v287(data_module, app_module)
    palliative_result = apply_headneck_palliative_rebuild_v288(data_module, app_module)
    free_flap_result = apply_headneck_free_flap_rebuild_v289(data_module, app_module)
    return {
        "patched": patched,
        "count": len(patched),
        "v284_etd": etd_result,
        "v285_rhinitis": rhinitis_result,
        "v286_neck_dissection": neck_dissection_result,
        "v287_salvage": salvage_result,
        "v288_palliative": palliative_result,
        "v289_free_flap": free_flap_result,
    }
