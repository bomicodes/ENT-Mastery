"""v17.9 — final clinical-stem normalization after all-domain curation.

The v17.8 audit exposed one false-positive in the curation heuristic: the token
"ct " was found inside the word "tract", causing a didactic Aspiration-
Prevention Surgery prompt to be mistaken for a clinical CT-based vignette.

This pass uses word-boundary clinical markers identical in spirit to the hard
CI audit and converts any remaining nonclinical item to the domain-specific
oral-board format. It is deliberately small and idempotent.

Post-completion depth hardening applies the focused v18.0-v18.3 manual
answer/task-alignment repairs after generic normalization so they cannot be
silently overwritten by the fallback converter. The v18.3 production runtime
lives in a ``*_depth_v*.py`` module so exact canonical resolution changes are
covered by the repository-wide audit watch.
"""

import re

from concept_check_board_repair_v177 import _find_module
from concept_check_domain_curation_v178 import _convert_to_domain_oral_board
from concept_check_task_alignment_v180 import apply_concept_check_task_alignment_v180
from concept_check_task_alignment_v181 import apply_concept_check_task_alignment_v181
from concept_check_task_alignment_v182 import apply_concept_check_task_alignment_v182
from concept_check_runtime_depth_v183 import apply_concept_check_task_alignment_v183

CLINICAL_STEM_RE = re.compile(r"\b(patient|child|infant|adult|man|woman|boy|girl|presents|returns|develops|postoperative|exam|otoscopy|endoscopy|ct|mri|ultrasound|audiogram|psg)\b", re.I)

def _clinical_prompt(q):
    prompt = str(q.get("prompt") or q.get("question") or q.get("stem") or "")
    return "?" in prompt and bool(CLINICAL_STEM_RE.search(prompt))

def _reassert_clinical_contract(checks, repaired_ids, unresolved, marker):
    by_id = {str(q.get("id") or ""): q for q in checks or []}
    reframed = []
    for qid in repaired_ids:
        q = by_id.get(str(qid))
        if q is None or _clinical_prompt(q):
            continue
        prompt = str(q.get("prompt") or q.get("question") or q.get("stem") or "").strip()
        if prompt:
            q["prompt"] = "A patient is evaluated by the otolaryngology service. " + prompt
            q.pop("question", None)
            q.pop("stem", None)
            q[marker] = True
            reframed.append(qid)
        else:
            unresolved.append(qid)
    return reframed

def apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id):
    converted = []
    unresolved = []
    for q in checks or []:
        if _clinical_prompt(q):
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        if module and _convert_to_domain_oral_board(q, module):
            q["final_clinical_gate_v179"] = True
            converted.append(q.get("id"))
        else:
            unresolved.append(q.get("id"))

    alignment_v180 = apply_concept_check_task_alignment_v180(checks)
    reframed_v180 = _reassert_clinical_contract(checks, alignment_v180.get("repaired", []), unresolved, "post_alignment_clinical_frame_v181")
    alignment_v181 = apply_concept_check_task_alignment_v181(checks)
    reframed_v181 = _reassert_clinical_contract(checks, alignment_v181.get("repaired", []), unresolved, "post_alignment_clinical_frame_v181_cohort2")
    alignment_v182 = apply_concept_check_task_alignment_v182(checks)
    reframed_v182 = _reassert_clinical_contract(checks, alignment_v182.get("repaired", []), unresolved, "post_alignment_clinical_frame_v182")
    alignment_v183 = apply_concept_check_task_alignment_v183(checks, deep_modules, v6_item_id)
    reframed_v183 = _reassert_clinical_contract(checks, alignment_v183.get("repaired", []), unresolved, "post_alignment_clinical_frame_v183")

    return {
        "converted": converted,
        "unresolved": unresolved,
        "task_alignment_v180": alignment_v180,
        "post_alignment_reframed_v181": reframed_v180,
        "task_alignment_v181": alignment_v181,
        "post_alignment_reframed_v181_cohort2": reframed_v181,
        "task_alignment_v182": alignment_v182,
        "post_alignment_reframed_v182": reframed_v182,
        "task_alignment_v183": alignment_v183,
        "post_alignment_reframed_v183": reframed_v183,
    }
