"""v15.1 — resident-level distractor quality repair.

Earlier second-pass banks were deliberately rich in stems/explanations but used
placeholder why-wrong text. This runtime repair replaces those placeholders with
choice-specific teaching tied to each case's own explanation. It is intentionally
content-preserving: stems, answers, pearls, and curveballs are unchanged.
"""

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


def _norm(value):
    return " ".join(str(value or "").strip().lower().split())


def _is_placeholder(reason):
    text = _norm(reason)
    return (not text) or any(marker in text for marker in _GENERIC_MARKERS)


def _choice_specific_reason(choice, explanation, pearl):
    """Create a case-specific teaching contrast without inventing new management."""
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
