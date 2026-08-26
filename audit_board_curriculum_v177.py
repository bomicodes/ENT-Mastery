"""v17.7 — Full Concept Check + Deep Curriculum board-style audit.

Audits every live Concept Check, every six-layer Deep Curriculum module, and
all attending curveballs after runtime mutations. Informational by default so a
single content edge case cannot take production down, but prints a concrete
repair queue for continued human/clinical curation.
"""

import re
from collections import Counter, defaultdict

import runtime_entry


data = runtime_entry.data
FIELDS = ("recognize", "localize", "workup", "manage", "operate", "teach")


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s or "").lower()).strip()


def qtext(q):
    return str(q.get("prompt") or q.get("question") or q.get("stem") or "")


def clinical(q):
    p = norm(qtext(q))
    markers = (
        "patient", "child", "infant", "adult", "man ", "woman ", "boy ", "girl ",
        "presents", "develops", "returns", "history", "exam", "otoscopy", "imaging",
        "postoperative", "after ", "with ",
    )
    return "?" in qtext(q) and any(m in p for m in markers)


def answer_index(q):
    try:
        return int(q.get("answer"))
    except (TypeError, ValueError):
        return -1


def correct_text(q):
    choices = list(q.get("choices") or [])
    i = answer_index(q)
    if 0 <= i < len(choices):
        return str(choices[i])
    return str(q.get("answer_text") or q.get("model_answer") or q.get("correct_answer") or "")


def main():
    checks = list(data.CONCEPT_CHECKS_V112)
    print(f"CONCEPT_CHECK_TOTAL|{len(checks)}")
    flags = defaultdict(list)
    ids = [q.get("id") for q in checks]
    dup = [x for x, n in Counter(ids).items() if x and n > 1]
    print(f"CONCEPT_DUPLICATE_IDS|{len(dup)}")

    answer_positions = Counter()
    for q in checks:
        qid = q.get("id") or "<missing-id>"
        prompt = qtext(q)
        choices = list(q.get("choices") or [])
        if not clinical(q):
            flags[qid].append("not_clinical_board_vignette")
        if not str(q.get("explanation") or "").strip():
            flags[qid].append("missing_explanation")
        if not str(correct_text(q)).strip():
            flags[qid].append("missing_reveal_answer")
        if choices:
            a = answer_index(q)
            if not (0 <= a < len(choices)):
                flags[qid].append("invalid_answer_index")
            else:
                answer_positions[a] += 1
            if len(choices) < 3:
                flags[qid].append("too_few_choices")
            why = list(q.get("why_wrong") or [])
            if len(why) != len(choices):
                flags[qid].append("why_wrong_misaligned")
            # If the keyed answer is essentially the page title and the prompt asks
            # for a diagnosis, the title itself can reveal the answer.
            p = norm(prompt)
            diagnosis_prompt = any(x in p for x in (
                "most likely diagnosis", "which diagnosis", "what is the diagnosis",
                "which condition", "which disease",
            ))
            if diagnosis_prompt and norm(q.get("topic")) == norm(correct_text(q)):
                flags[qid].append("header_reveals_answer")
        if q.get("curveball") and not str(q.get("curveball_answer") or "").strip():
            flags[qid].append("curveball_without_reveal_answer")

    print("CONCEPT_ANSWER_POSITION_COUNTS|" + "|".join(f"{k}:{v}" for k, v in sorted(answer_positions.items())))
    print(f"CONCEPT_FLAGGED|{len(flags)}")
    for q in checks:
        qid = q.get("id") or "<missing-id>"
        if qid in flags:
            print("CONCEPT_REPAIR|%s|%s|%s|%s" % (
                qid, q.get("domain"), q.get("topic"), ",".join(flags[qid])
            ))

    # Deep Curriculum: every module must contain the six canonical teaching
    # layers; each layer should teach rather than merely ask the learner to do so.
    deep_flags = []
    teach_prompt_re = re.compile(r"(?:^|[.;]\s+)(?:explain|discuss|describe|compare|contrast|what|how|why)\b|\?", re.I)
    total_modules = 0
    for domain, modules in (data.DEEP_MODULES_V6 or {}).items():
        for m in modules or []:
            total_modules += 1
            issues = []
            for field in FIELDS:
                txt = str(m.get(field) or "").strip()
                if not txt:
                    issues.append("missing_" + field)
                elif len(txt) < 70:
                    issues.append("thin_" + field)
            teach = str(m.get("teach") or "").strip()
            if teach and teach_prompt_re.search(teach):
                issues.append("teach_reads_like_prompt")
            if issues:
                deep_flags.append((domain, m.get("topic"), issues))
    print(f"DEEP_MODULE_TOTAL|{total_modules}")
    print(f"DEEP_MODULE_FLAGGED|{len(deep_flags)}")
    for domain, topic, issues in deep_flags:
        print("DEEP_REPAIR|%s|%s|%s" % (domain, topic, ",".join(issues)))

    # Attending curveballs anywhere in the Clinical Challenge bank require a
    # visible reveal answer. This catches legacy curveballs added before the UI
    # supported explicit reasoning reveals.
    challenges = list(data.CLINICAL_CHALLENGES_V119)
    missing_curveball_answers = [
        q for q in challenges
        if str(q.get("curveball") or "").strip() and not str(q.get("curveball_answer") or "").strip()
    ]
    print(f"CLINICAL_CHALLENGE_TOTAL|{len(challenges)}")
    print(f"CURVEBALLS_WITHOUT_REVEAL|{len(missing_curveball_answers)}")
    for q in missing_curveball_answers:
        print("CURVEBALL_REPAIR|%s|%s|%s" % (q.get("id"), q.get("domain"), q.get("topic")))

    print("BOARD_CURRICULUM_AUDIT_MODE|informational")


if __name__ == "__main__":
    main()
