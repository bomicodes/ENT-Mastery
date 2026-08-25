"""v16.2 — Full Concept Check bank repair.

The v16.1 audit found a systematic cohort of 104 generated recall checks that
asked the learner to identify a diagnosis while the Concept Check page itself
already displayed that diagnosis as the title. Those same items frequently
copied answer/choice language into the prompt and had no explanation.

This patch repairs that cohort in place without changing IDs/concept links:
- converts tautological diagnosis-ID items into genuine known-topic active recall;
- uses the live Deep Curriculum as the answer source so the recall target stays
  aligned with the canonical curriculum rather than inventing parallel content;
- removes meaningless MC distractors for those items (the page already has a
  free-response commit box, which is the better format for this kind of recall);
- supplies an explanation and board pearl from the curriculum;
- repairs missing/very weak why-wrong arrays in the remaining MC bank;
- deterministically rebalances answer positions in the remaining MC checks.

This intentionally treats Concept Checks as the basic/foundation retrieval tier.
Application and senior-decision discrimination remain the job of Clinical
Challenges and Chief/Attending modes.
"""

import difflib
import hashlib
import re


def _norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def _prompt(q):
    return str(q.get("prompt") or q.get("question") or q.get("stem") or "")


def _answer_index(q):
    try:
        return int(q.get("answer"))
    except (TypeError, ValueError):
        return -1


def _correct_choice(q):
    choices = list(q.get("choices") or [])
    idx = _answer_index(q)
    return choices[idx] if 0 <= idx < len(choices) else ""


def _is_bad_generated_diagnosis_check(q):
    """High-confidence match for the 104-item tautological generated cohort."""
    p = _norm(_prompt(q))
    diagnosis_markers = (
        "which diagnosis or clinical framework best fits",
        "which diagnosis", "most likely diagnosis", "what is the diagnosis",
        "which condition", "which disorder", "which disease", "what condition",
    )
    if not any(m in p for m in diagnosis_markers):
        return False
    if "a patient presents with the following pattern" not in p:
        return False
    topic = _norm(q.get("topic"))
    correct = _norm(_correct_choice(q))
    if not topic or not correct:
        return False
    return topic == correct or difflib.SequenceMatcher(None, topic, correct).ratio() >= 0.90


def _deep_lookup(deep_modules):
    exact = {}
    by_concept = {}
    for domain, modules in (deep_modules or {}).items():
        for module in modules or []:
            topic = module.get("topic")
            if not topic:
                continue
            exact[(domain, topic)] = module
            cid = module.get("concept_id")
            if cid:
                by_concept[cid] = module
    return exact, by_concept


def _find_module(q, deep_modules, v6_item_id):
    exact, _ = _deep_lookup(deep_modules)
    domain = q.get("domain")
    topic = q.get("canonical_topic") or q.get("topic")
    if (domain, topic) in exact:
        return exact[(domain, topic)]

    # Concept-ID match is safer than fuzzy text when an alias exists.
    qcid = q.get("concept_id")
    if qcid:
        for d, modules in (deep_modules or {}).items():
            for m in modules or []:
                if v6_item_id(d, m.get("topic", "")) == qcid:
                    return m

    # Conservative same-domain fuzzy fallback for legacy label drift.
    target = _norm(topic)
    best = None
    for d, modules in (deep_modules or {}).items():
        if d != domain:
            continue
        for m in modules or []:
            ratio = difflib.SequenceMatcher(None, target, _norm(m.get("topic"))).ratio()
            if best is None or ratio > best[0]:
                best = (ratio, m)
    return best[1] if best and best[0] >= 0.72 else None


def _recall_prompt(topic, module):
    """Use a known-topic recall question; never ask the diagnosis shown in title."""
    recognize = str(module.get("recognize") or "").strip()
    localize = str(module.get("localize") or "").strip()
    workup = str(module.get("workup") or "").strip()
    manage = str(module.get("manage") or "").strip()

    if recognize:
        return (
            f"For {topic}, retrieve the core recognition framework without looking: "
            "what presentation or defining features should you recognize, what close "
            "mimic/subtype must you distinguish when relevant, and what red flag would "
            "make you escalate beyond the routine pathway?"
        ), recognize, "recognition"
    if localize:
        return (
            f"For {topic}, what anatomy, localization, or mechanism is essential to "
            "understanding the condition, and why does that localization matter clinically?"
        ), localize, "localization"
    if workup:
        return (
            f"For {topic}, what is the foundational evaluation and which finding most "
            "meaningfully changes the next step?"
        ), workup, "evaluation"
    if manage:
        return (
            f"For {topic}, state the basic management framework: what is first-line, and "
            "what finding or failure should trigger escalation?"
        ), manage, "management"
    return (
        f"Without looking, state the core framework you should know for {topic}.",
        str(module.get("teach") or module.get("operate") or "").strip(),
        "core framework",
    )


def _repair_tautological_checks(checks, deep_modules, v6_item_id):
    repaired = []
    unresolved = []
    for q in checks:
        if not _is_bad_generated_diagnosis_check(q):
            continue
        module = _find_module(q, deep_modules, v6_item_id)
        if not module:
            unresolved.append(q.get("id"))
            continue
        topic = q.get("topic") or module.get("topic") or "this topic"
        prompt, answer_text, dimension = _recall_prompt(topic, module)
        q["prompt"] = prompt
        q.pop("question", None)
        q.pop("stem", None)
        q["choices"] = []
        q["answer"] = None
        q["answer_text"] = answer_text
        q["explanation"] = (
            f"This check is testing the foundational {dimension} framework for {topic}. "
            "Compare your retrieval with the canonical Deep Curriculum answer above; the "
            "goal is to recall the discriminating facts, not recognize the topic name."
        )
        if module.get("teach"):
            q["board_pearl"] = module.get("teach")
        q["recall_source"] = "Deep Curriculum"
        q["concept_check_repaired_v162"] = True
        q.pop("why_wrong", None)
        repaired.append(q.get("id"))
    return repaired, unresolved


def _reason_is_weak(reason):
    nr = _norm(reason)
    if not nr:
        return True
    if len(nr.split()) < 5:
        return nr not in {"correct"}
    generic = {
        "incorrect", "not correct", "not the best answer", "wrong answer",
        "does not fit", "does not match",
    }
    return nr in generic


def _repair_why_wrong(checks):
    repaired = []
    for q in checks:
        choices = list(q.get("choices") or [])
        if len(choices) < 2:
            continue
        a = _answer_index(q)
        if not (0 <= a < len(choices)):
            continue
        old = list(q.get("why_wrong") or [])
        reasons = old if len(old) == len(choices) else [""] * len(choices)
        explanation = str(q.get("explanation") or q.get("answer_text") or "").strip()
        changed = len(old) != len(choices)
        for i, choice in enumerate(choices):
            if i == a:
                if _norm(reasons[i]) != "correct":
                    reasons[i] = "Correct."
                    changed = True
                continue
            if _reason_is_weak(reasons[i]):
                key = explanation or f"The keyed answer is {choices[a]}."
                reasons[i] = (
                    f"{choice} is not the best answer for the distinction being tested. "
                    f"The key reasoning is: {key}"
                )
                changed = True
        if changed:
            q["why_wrong"] = reasons
            repaired.append(q.get("id"))
    return repaired


def _rebalance_mc_answers(checks):
    """Deterministic shuffle, preserving choice/why-wrong alignment."""
    changed = []
    for q in checks:
        choices = list(q.get("choices") or [])
        if len(choices) < 2:
            continue
        answer = _answer_index(q)
        if not (0 <= answer < len(choices)):
            continue
        digest = hashlib.sha256(("concept-check-v162:" + str(q.get("id", ""))).encode("utf-8")).digest()
        target = int.from_bytes(digest[:4], "big") % len(choices)
        if target == answer:
            continue
        why = list(q.get("why_wrong") or [])
        correct_choice = choices.pop(answer)
        choices.insert(target, correct_choice)
        if len(why) == len(choices):
            correct_reason = why.pop(answer)
            why.insert(target, correct_reason)
            q["why_wrong"] = why
        q["choices"] = choices
        q["answer"] = target
        changed.append(q.get("id"))
    return changed


def apply_concept_check_repair_v162(checks, deep_modules, v6_item_id):
    repaired_tautological, unresolved = _repair_tautological_checks(
        checks, deep_modules, v6_item_id
    )
    repaired_why_wrong = _repair_why_wrong(checks)
    rebalanced = _rebalance_mc_answers(checks)
    return {
        "tautological_repaired": repaired_tautological,
        "unresolved": unresolved,
        "why_wrong_repaired": repaired_why_wrong,
        "rebalanced": rebalanced,
    }
