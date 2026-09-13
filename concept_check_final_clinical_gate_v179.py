"""Final clinical-stem normalization plus exact-live v20.32 successor alignment.

The validated v20.30 implementation remains the complete predecessor. v20.32 adds an exact-canonical
Unilateral Sinonasal Disease Concept Check after inherited normalization so the learner pathway is
not fragmented between Deep Curriculum and Daily Curriculum.
"""
import concept_check_final_clinical_gate_v179_source_v228 as _base
from concept_check_final_clinical_gate_v179_source_v228 import *
from concept_check_board_repair_v177 import _find_module
from concept_check_depth_v229 import apply_concept_check_task_alignment_v229
from concept_check_depth_v230 import apply_concept_check_task_alignment_v230
from concept_check_rhinology_unilateral_v232 import (
    SOURCE_REFS as UNILATERAL_SOURCE_REFS_V232,
    apply_rhinology_unilateral_concept_check_v232,
)


def _reassert_onb_search_aliases_v230(checks, deep_modules, v6_item_id):
    """Keep all learner synonyms in the live canonical Deep Curriculum search text.

    The search index intentionally indexes learner-facing Deep Curriculum prose rather than hidden
    metadata. Therefore the historical alias ``esthesioblastoma`` is repeated in the recognize layer
    instead of being stored only in ``search_aliases``.
    """
    qid = "cc-v112-rec-rhinology-allergy-skull-base-sinonasal-malignancy"
    q = next((x for x in checks if str(x.get("id") or "") == qid), None)
    module = _find_module(q, deep_modules, v6_item_id) if q else None
    if not module:
        return False
    addition = (
        "ONB terminology: esthesioneuroblastoma and olfactory neuroblastoma are synonyms for the "
        "same olfactory-neuroepithelial malignancy; the historical alias esthesioblastoma may also "
        "appear in older literature and should resolve to this same canonical topic."
    )
    current = str(module.get("recognize") or "")
    if "esthesioblastoma" not in current.lower():
        module["recognize"] = (current.rstrip() + ("\n\n" if current.strip() else "") + addition).strip()
    return True


def _reassert_unilateral_visible_sources_v232(checks, deep_modules, v6_item_id):
    """Make core textbook provenance visible on every exact unilateral learner check.

    Older v112 recognize/manage checks remain useful and are intentionally retained.  The v31.3
    learner audit showed that those inherited checks rendered only partial source trails even after
    the new integrated v20.32 check was added.  Enrich the existing exact-canonical checks in place
    instead of deleting them, weakening the gate, or hiding the provenance in Deep-only metadata.
    """
    repaired = []
    for q in checks or []:
        if str(q.get("domain") or "") != "Rhinology / Allergy / Skull Base":
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        if not module or str(module.get("topic") or "") != "Unilateral Sinonasal Disease":
            continue
        refs = list(q.get("source_refs_v230") or [])
        existing = {
            str(ref.get("citation") or "").strip().lower()
            for ref in refs
            if isinstance(ref, dict)
        }
        changed = False
        for ref in UNILATERAL_SOURCE_REFS_V232:
            citation = str(ref.get("citation") or "").strip().lower()
            if citation and citation not in existing:
                refs.append(dict(ref))
                existing.add(citation)
                changed = True
        if changed:
            q["source_refs_v230"] = refs
            repaired.append(str(q.get("id") or ""))
    return repaired


def apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id):
    results = _base.apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id)
    alignment_v229 = apply_concept_check_task_alignment_v229(checks, deep_modules, v6_item_id)
    results["task_alignment_v229"] = alignment_v229
    results["post_alignment_reframed_v229"] = _base._reassert_clinical_contract(
        checks,
        alignment_v229.get("repaired", []),
        results.get("unresolved", []),
        "post_alignment_clinical_frame_v229",
    )
    alignment_v230 = apply_concept_check_task_alignment_v230(checks, deep_modules, v6_item_id)
    results["task_alignment_v230"] = alignment_v230
    results["post_alignment_reframed_v230"] = _base._reassert_clinical_contract(
        checks,
        alignment_v230.get("repaired", []),
        results.get("unresolved", []),
        "post_alignment_clinical_frame_v230",
    )
    results["onb_search_aliases_v230"] = _reassert_onb_search_aliases_v230(checks, deep_modules, v6_item_id)
    results["rhinology_unilateral_concept_check_v232"] = apply_rhinology_unilateral_concept_check_v232(
        checks, deep_modules, v6_item_id
    )
    results["rhinology_unilateral_visible_sources_v232"] = _reassert_unilateral_visible_sources_v232(
        checks, deep_modules, v6_item_id
    )
    return results
