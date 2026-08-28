"""v17.9 — final clinical-stem normalization after all-domain curation.

The v17.8 audit exposed one false-positive in the curation heuristic: the token
"ct " was found inside the word "tract", causing a didactic Aspiration-
Prevention Surgery prompt to be mistaken for a clinical CT-based vignette.

This pass uses word-boundary clinical markers identical in spirit to the hard
CI audit and converts any remaining nonclinical item to the domain-specific
oral-board format. It is deliberately small and idempotent.

Post-completion depth hardening also applies the focused v18.0 manual
answer/task-alignment repairs after generic normalization so they cannot be
silently overwritten by the fallback converter.
"""

import re

from concept_check_board_repair_v177 import _find_module
from concept_check_domain_curation_v178 import _convert_to_domain_oral_board
from concept_check_task_alignment_v180 import apply_concept_check_task_alignment_v180


CLINICAL_STEM_RE = re.compile(
    r"\b(patient|child|infant|adult|man|woman|boy|girl|presents|returns|develops|"
    r"postoperative|exam|otoscopy|endoscopy|ct|mri|ultrasound|audiogram|psg)\b",
    re.I,
)


def apply_final_clinical_gate_v179(checks, deep_modules, v6_item_id):
    converted = []
    unresolved = []
    for q in checks or []:
        prompt = str(q.get("prompt") or q.get("question") or q.get("stem") or "")
        if "?" in prompt and CLINICAL_STEM_RE.search(prompt):
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        if module and _convert_to_domain_oral_board(q, module):
            q["final_clinical_gate_v179"] = True
            converted.append(q.get("id"))
        else:
            unresolved.append(q.get("id"))

    alignment = apply_concept_check_task_alignment_v180(checks)
    return {
        "converted": converted,
        "unresolved": unresolved,
        "task_alignment_v180": alignment,
    }
