"""v16.1 — Concept Checks full-bank quality audit.

Audits the live CONCEPT_CHECKS_V112 bank after runtime patches. This is an
informational curation tool, not a release gate. It specifically targets the
failure mode surfaced by the Acute Otitis Externa screenshot: a topic-labelled
recall page asking the learner to identify the diagnosis that is already shown
in the header, plus other forms of answer leakage, tautology, duplicate content,
choice/schema problems and weak explanatory support.
"""

import difflib
import re
from collections import Counter, defaultdict

import runtime_entry  # noqa: F401 — boot/apply runtime patches first
import data


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()


def words(s):
    return {w for w in norm(s).split() if len(w) >= 3}


def question_text(q):
    return str(q.get("prompt") or q.get("question") or q.get("stem") or "")


def answer_index(q):
    try:
        return int(q.get("answer"))
    except (TypeError, ValueError):
        return -1


def correct_choice(q):
    ch = list(q.get("choices") or [])
    a = answer_index(q)
    return ch[a] if 0 <= a < len(ch) else ""


def looks_like_diagnosis_identification(prompt):
    p = norm(prompt)
    markers = (
        "which diagnosis", "most likely diagnosis", "what is the diagnosis",
        "which condition", "which disorder", "clinical framework best fits",
        "which disease", "what condition", "what diagnosis",
    )
    return any(m in p for m in markers)


def generic_pattern_prompt(prompt):
    p = norm(prompt)
    return (
        "a patient presents with the following pattern" in p
        or "which diagnosis or clinical framework best fits" in p
    )


def prompt_choice_leak_count(q):
    p = norm(question_text(q))
    leaked = []
    for i, c in enumerate(q.get("choices") or []):
        nc = norm(c)
        if len(nc) >= 5 and nc in p:
            leaked.append(i)
    return leaked


def title_leaks_answer(q):
    topic = norm(q.get("topic"))
    correct = norm(correct_choice(q))
    if not topic or not correct:
        return False
    # High-confidence only: page header substantially equals the keyed answer.
    return topic == correct or difflib.SequenceMatcher(None, topic, correct).ratio() >= 0.90


def weak_why_wrong(q):
    choices = list(q.get("choices") or [])
    why = list(q.get("why_wrong") or [])
    if not choices:
        return False
    if len(why) != len(choices):
        return True
    generic = (
        "incorrect", "not correct", "not the best answer", "wrong answer",
        "does not fit", "does not match", "correct.",
    )
    a = answer_index(q)
    for i, reason in enumerate(why):
        if i == a:
            continue
        nr = norm(reason)
        if len(nr.split()) < 5 or any(nr == g for g in generic):
            return True
    return False


def main():
    qs = list(data.CONCEPT_CHECKS_V112)
    print(f"CONCEPT_CHECK_TOTAL|{len(qs)}")

    ids = [q.get("id") for q in qs]
    dup_ids = [k for k, n in Counter(ids).items() if k and n > 1]
    print(f"DUPLICATE_IDS|{len(dup_ids)}")

    schema = []
    for q in qs:
        ch = list(q.get("choices") or [])
        a = answer_index(q)
        if not q.get("id") or not q.get("topic") or not question_text(q):
            schema.append((q.get("id"), "missing_core_field"))
        elif ch and not (0 <= a < len(ch)):
            schema.append((q.get("id"), "invalid_answer_index"))
    print(f"SCHEMA_ERRORS|{len(schema)}")
    for x in schema[:25]:
        print("SCHEMA|%s|%s" % x)

    pos = Counter(answer_index(q) for q in qs if q.get("choices"))
    print("ANSWER_POSITION_COUNTS|" + "|".join(f"{k}:{v}" for k, v in sorted(pos.items())))

    generic = [q for q in qs if generic_pattern_prompt(question_text(q))]
    print(f"GENERIC_PATTERN_PROMPTS|{len(generic)}")

    diagnosis = [q for q in qs if looks_like_diagnosis_identification(question_text(q))]
    print(f"DIAGNOSIS_IDENTIFICATION_PROMPTS|{len(diagnosis)}")

    header_giveaway = [q for q in diagnosis if title_leaks_answer(q)]
    print(f"HEADER_REVEALS_DIAGNOSIS_ANSWER|{len(header_giveaway)}")

    prompt_leaks = []
    for q in qs:
        leaked = prompt_choice_leak_count(q)
        if leaked:
            prompt_leaks.append((q, leaked))
    print(f"PROMPT_CONTAINS_CHOICE_TEXT|{len(prompt_leaks)}")

    multi_choice_leaks = [(q, li) for q, li in prompt_leaks if len(li) >= 2]
    print(f"PROMPT_CONTAINS_MULTIPLE_CHOICES|{len(multi_choice_leaks)}")

    tautological = []
    for q in qs:
        p = norm(question_text(q))
        topic = norm(q.get("topic"))
        cc = norm(correct_choice(q))
        if looks_like_diagnosis_identification(p) and topic and cc:
            if (topic in p and title_leaks_answer(q)) or generic_pattern_prompt(p):
                tautological.append(q)
    print(f"TAUTOLOGICAL_RECALL_CANDIDATES|{len(tautological)}")

    weak_why = [q for q in qs if weak_why_wrong(q)]
    print(f"WEAK_OR_MISSING_WHY_WRONG|{len(weak_why)}")

    missing_expl = [q for q in qs if not str(q.get("explanation") or "").strip()]
    print(f"MISSING_EXPLANATION|{len(missing_expl)}")

    # Exact duplicate prompts and near-duplicates within the same topic.
    by_prompt = defaultdict(list)
    for q in qs:
        by_prompt[norm(question_text(q))].append(q)
    exact_dupes = [v for k, v in by_prompt.items() if k and len(v) > 1]
    print(f"EXACT_DUPLICATE_PROMPT_GROUPS|{len(exact_dupes)}")

    by_topic = defaultdict(list)
    for q in qs:
        by_topic[(q.get("domain"), q.get("topic"))].append(q)
    near = []
    for key, rows in by_topic.items():
        for i in range(len(rows)):
            for j in range(i + 1, len(rows)):
                a, b = norm(question_text(rows[i])), norm(question_text(rows[j]))
                if not a or not b:
                    continue
                r = difflib.SequenceMatcher(None, a, b).ratio()
                if r >= 0.82:
                    near.append((key, rows[i].get("id"), rows[j].get("id"), r))
    print(f"NEAR_DUPLICATE_PROMPT_PAIRS|{len(near)}")

    # Per-domain burden so curation can proceed systematically.
    flags = defaultdict(set)
    for q in generic: flags[q.get("id")].add("generic")
    for q in header_giveaway: flags[q.get("id")].add("header_giveaway")
    for q, _ in multi_choice_leaks: flags[q.get("id")].add("choice_leak")
    for q in weak_why: flags[q.get("id")].add("why_wrong")
    for q in missing_expl: flags[q.get("id")].add("missing_explanation")

    domain_counts = Counter()
    q_by_id = {q.get("id"): q for q in qs}
    for qid in flags:
        domain_counts[q_by_id.get(qid, {}).get("domain", "UNKNOWN")] += 1
    for d, n in sorted(domain_counts.items()):
        print(f"FLAGGED_BY_DOMAIN|{d}|{n}")

    # Print the concrete repair queue; cap only display, not counting.
    ordered = sorted(
        flags.items(),
        key=lambda kv: (
            q_by_id.get(kv[0], {}).get("domain", ""),
            q_by_id.get(kv[0], {}).get("topic", ""),
            str(kv[0]),
        ),
    )
    print(f"REPAIR_QUEUE|{len(ordered)}")
    for qid, reasons in ordered[:250]:
        q = q_by_id[qid]
        print(
            "REPAIR|%s|%s|%s|%s|%s" % (
                qid, q.get("domain"), q.get("topic"), ",".join(sorted(reasons)),
                question_text(q).replace("|", "/")[:180],
            )
        )

    print("CONCEPT_CHECK_AUDIT_MODE|informational")


if __name__ == "__main__":
    main()
