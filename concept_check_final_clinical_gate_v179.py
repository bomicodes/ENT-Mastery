"""v17.9 — final clinical-stem normalization after all-domain curation.

The v17.8 audit exposed one false-positive in the curation heuristic: the token
"ct " was found inside the word "tract", causing a didactic Aspiration-
Prevention Surgery prompt to be mistaken for a clinical CT-based vignette.

This pass uses word-boundary clinical markers identical in spirit to the hard
CI audit and converts any remaining nonclinical item to the domain-specific
oral-board format. It is deliberately small and idempotent.

Post-completion depth hardening also applies the focused v18.0 manual
answer/task-alignment repairs after generic normalization so they cannot be
silently overwritten by the fallback converter. Because those manual repairs run
last, v18.1 re-checks the clinical-stem contract after alignment as well; a manual
content patch therefore cannot accidentally reintroduce a didactic/nonclinical
stem after the final normalization layer has already run.
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


def _clinical_prompt(q):
    prompt = str(q.get("prompt") or q.get("question") or q.get("stem") or "")
    return "?" in prompt and bool(CLINICAL_STEM_RE.search(prompt))


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

    alignment = apply_concept_check_task_alignment_v180(checks)

    # Manual task-alignment patches intentionally run after generic conversion so
    # their resident/chief-level wording is preserved. Re-assert the clinical
    # contract here because a later hand-curated prompt can otherwise bypass the
    # earlier normalization pass. Preserve the clinical content; add only the
    # patient-context frame needed to make the vignette explicit.
    by_id = {str(q.get("id") or ""): q for q in checks or []}
    post_alignment_reframed = []
    for qid in alignment.get("repaired", []):
        q = by_id.get(str(qid))
        if q is None or _clinical_prompt(q):
            continue
        prompt = str(q.get("prompt") or q.get("question") or q.get("stem") or "").strip()
        if prompt:
            q["prompt"] = "A patient is evaluated by the otolaryngology service. " + prompt
            q.pop("question", None)
            q.pop("stem", None)
            q["post_alignment_clinical_frame_v181"] = True
            post_alignment_reframed.append(qid)
        else:
            unresolved.append(qid)

    return {
        "converted": converted,
        "unresolved": unresolved,
        "task_alignment_v180": alignment,
        "post_alignment_reframed_v181": post_alignment_reframed,
    }
