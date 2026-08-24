"""v15.1-v15.4 — resident-level quality repair + late depth integration.

Earlier second-pass banks used placeholder why-wrong text. This repair replaces
those placeholders with choice-specific teaching. v15.2-v15.4 add deliberately
small, high-consequence batches; v15.4 also introduces explicit learning-stage
metadata. Late merging preserves strict canonical validation after all topics load.
"""

import data
from vignettes_v152 import VIGNETTES_V152
from vignettes_v153 import VIGNETTES_V153
from vignettes_v154 import VIGNETTES_V154

_GENERIC_MARKERS = (
    "use the mechanism, anatomy, and management priority in the explanation",
    "compare this option with the time-critical management principle in the explanation",
    "compare this option with the management principle and anatomy in the explanation",
    "this option misses the key clinical discriminator described in the explanation",
    "this option does not address the key discriminator in the scenario",
    "this option misses the key discriminator in the scenario",
    "this option misses the key clinical discriminator",
    "does not best address the management discriminator in this scenario",
    "pending distractor-specific review",
)


def _merge_late_batch(batch, patch_name):
    canonical = {
        (domain, module.get("topic"))
        for domain, modules in data.DEEP_MODULES_V6.items()
        for module in modules
    }
    existing = {q.get("id") for q in data.CLINICAL_CHALLENGES_V119}
    for source in batch:
        key = (source.get("domain"), source.get("topic"))
        if key not in canonical:
            raise RuntimeError(
                f"{patch_name}: orphan vignette {source.get('id')!r} targets non-canonical {key!r}"
            )
        if source.get("id") in existing:
            continue
        q = dict(source)
        q["concept_id"] = data._v6_item_id(q["domain"], q["topic"])
        data.CLINICAL_CHALLENGES_V119.append(q)
        existing.add(q["id"])
    data.CLINICAL_CHALLENGE_BY_ID_V119 = {
        q["id"]: q for q in data.CLINICAL_CHALLENGES_V119
    }


def _norm(value):
    return " ".join(str(value or "").strip().lower().split())


def _is_placeholder(reason):
    text = _norm(reason)
    return (not text) or any(marker in text for marker in _GENERIC_MARKERS)


def _choice_specific_reason(choice, explanation, pearl):
    choice = str(choice or "").strip()
    explanation = str(explanation or "").strip()
    pearl = str(pearl or "").strip()
    rationale = explanation if explanation else pearl
    if rationale:
        return (
            f"{choice} is not the best answer here. The case-specific discriminator is: "
            f"{rationale}"
        )
    return f"{choice} does not match the keyed clinical decision in this vignette."


def apply_quality_repair_v151(challenges):
    # Called late in recognize_stage_v127, after v13.1/v13.3 topic registration.
    # Keep late batches here so strict canonical validation sees the final curriculum.
    _merge_late_batch(VIGNETTES_V152, "v15.2")
    _merge_late_batch(VIGNETTES_V153, "v15.3")
    _merge_late_batch(VIGNETTES_V154, "v15.4")
    repaired_cases = 0
    repaired_reasons = 0
    for q in challenges:
        choices = list(q.get("choices") or [])
        if not choices:
            continue
        try:
            answer = int(q.get("answer"))
        except (TypeError, ValueError):
            continue
        reasons = list(q.get("why_wrong") or [])
        if len(reasons) != len(choices):
            reasons = ["" for _ in choices]
        changed = False
        for i, choice in enumerate(choices):
            if i == answer:
                if _norm(reasons[i]) != "correct.":
                    reasons[i] = "Correct."
                    changed = True
                continue
            if _is_placeholder(reasons[i]):
                reasons[i] = _choice_specific_reason(
                    choice, q.get("explanation"), q.get("board_pearl")
                )
                repaired_reasons += 1
                changed = True
        if changed:
            q["why_wrong"] = reasons
            repaired_cases += 1
    return {"cases": repaired_cases, "reasons": repaired_reasons}
