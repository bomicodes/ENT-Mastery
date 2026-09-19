"""
audit_question_quality.py

Standalone audit for ENT Mastery. Run this from the repo root (same directory
as runtime_entry_pasha.py) with your normal virtualenv active:

    python audit_question_quality.py

It imports the ACTUAL production entrypoint (runtime_entry_pasha), so every
check runs against the fully-assembled, fully-patched data your live site
serves -- not a guess from outside.

What it checks
---------------
1. GENERIC_WHY_WRONG
   Clinical Challenge items whose "why_wrong" explanations are placeholder
   or duplicate text instead of real per-choice reasoning. Catches both the
   raw Q()-factory default string and the quality_repair_v151.py fallback
   pattern ("... is not the best answer here. The case-specific discriminator
   is: ...") when it is reused identically across 2+ choices.

2. KITCHEN_SINK_ANSWER
   Items where the correct choice is a padded catch-all (contains hedge
   phrases like "or other X features" / "and other X features") and is
   noticeably longer than the distractors -- guessable from shape alone,
   regardless of content knowledge.

3. ALIAS_REVEALING_BLIND_CARD
   Daily Path "recognize" items where blind_reveal=True (i.e. the UI shows
   "Unidentified case") but the topic name (or a very close variant) still
   appears verbatim in the prompt or answer text, defeating the blind format.
   This is the same class of bug daily_curriculum_quality_v370.py already
   fixes for a hand-curated topic list -- this check finds topics NOT yet on
   that list.

4. EMPTY_OR_SHORT_WHY_WRONG
   why_wrong entries that are blank or trivially short (<15 chars), which
   almost never carry real discriminating reasoning.

Output
------
Prints a human-readable report to stdout and writes a machine-readable
`question_quality_report.json` you can hand back to Claude (or anyone) for
targeted rewrites -- only the flagged items, not the whole bank.
"""

import json
import re
import sys


def _norm(s):
    return " ".join(str(s or "").strip().lower().split())


GENERIC_WHY_WRONG_MARKERS = (
    "compare this option with the time-critical management principle in the explanation",
    "compare this option with the management principle and anatomy in the explanation",
    "review the explanation and compare the management principle with the clinical context",
    "this option misses the key clinical discriminator described in the explanation",
    "this option does not address the key discriminator in the scenario",
    "this option misses the key discriminator in the scenario",
    "this option misses the key clinical discriminator",
    "does not best address the management discriminator in this scenario",
    "pending distractor-specific review",
    "does not match the keyed clinical decision in this vignette",
    "compare the option with the management principle in the explanation and the specific clinical context",
    "compare this option with the decision rule and anatomy described in the explanation",
    "compare this option with the triage, anatomy, or management principle in the explanation",
)

FALLBACK_PATTERN = re.compile(
    r"is not the best answer here\.\s*the case-specific discriminator is:", re.IGNORECASE
)

KITCHEN_SINK_HEDGES = (
    "or other major",
    "or other high-risk",
    "and other high-risk",
    "or other adverse",
    "and other adverse",
    "or other aggressive",
    "or other concerning",
    "or other red flag",
)


def audit_clinical_challenges(challenges):
    flagged = []
    for q in challenges:
        qid = q.get("id", "?")
        topic = q.get("topic", "?")
        why_wrong = q.get("why_wrong") or []
        choices = q.get("choices") or []
        answer_idx = q.get("answer")

        # --- Check 1: generic / duplicate why_wrong text ---
        normed = [_norm(w) for w in why_wrong]
        issues = []

        # exact-marker hits
        marker_hits = [i for i, w in enumerate(normed) if any(m in w for m in GENERIC_WHY_WRONG_MARKERS)]
        if marker_hits:
            issues.append(("GENERIC_WHY_WRONG", f"choice(s) {marker_hits} use a known placeholder phrase"))

        # duplicate-across-choices hits (catches the fallback pattern reused verbatim)
        non_empty = [w for w in normed if w]
        if len(non_empty) >= 2 and len(set(non_empty)) == 1:
            issues.append(("GENERIC_WHY_WRONG", "all why_wrong entries are byte-identical"))
        elif any(FALLBACK_PATTERN.search(w) for w in normed):
            # fallback pattern present at all -> worth a human look even if not fully duplicated
            dup_check = {}
            for i, w in enumerate(normed):
                if FALLBACK_PATTERN.search(w):
                    dup_check.setdefault(w, []).append(i)
            for text, idxs in dup_check.items():
                if len(idxs) >= 2:
                    issues.append(("GENERIC_WHY_WRONG", f"choices {idxs} share identical fallback reasoning"))

        # --- Check 4: empty / too-short why_wrong ---
        short_hits = [i for i, w in enumerate(normed) if w and len(w) < 15 and i != answer_idx]
        empty_hits = [i for i, w in enumerate(why_wrong) if choices and i != answer_idx and not _norm(w)]
        if short_hits:
            issues.append(("EMPTY_OR_SHORT_WHY_WRONG", f"choice(s) {short_hits} have <15 char reasoning"))
        if empty_hits:
            issues.append(("EMPTY_OR_SHORT_WHY_WRONG", f"choice(s) {empty_hits} have no reasoning at all"))

        # --- Check 2: kitchen-sink correct answer ---
        if choices and answer_idx is not None and 0 <= answer_idx < len(choices):
            correct = choices[answer_idx]
            correct_norm = _norm(correct)
            others = [c for i, c in enumerate(choices) if i != answer_idx]
            avg_other_len = sum(len(c) for c in others) / max(len(others), 1)
            has_hedge = any(h in correct_norm for h in KITCHEN_SINK_HEDGES)
            is_much_longer = len(correct) > 1.6 * avg_other_len if avg_other_len else False
            if has_hedge and is_much_longer:
                issues.append((
                    "KITCHEN_SINK_ANSWER",
                    f"correct choice is {len(correct)} chars vs avg distractor {avg_other_len:.0f} "
                    f"chars and contains a catch-all hedge phrase",
                ))

        if issues:
            flagged.append({
                "id": qid,
                "topic": topic,
                "domain": q.get("domain"),
                "tier": q.get("tier"),
                "issues": issues,
            })
    return flagged


def _topic_variants(topic):
    """Rough variant set for alias detection: full topic, and its significant words."""
    variants = {topic.strip()}
    variants.add(topic.replace("&", "and").strip())
    for part in re.split(r"\s*(?:/|—|\(|\)|\bof the\b|\bof\b)\s*", topic, flags=re.IGNORECASE):
        part = part.strip(" -")
        if len(part) >= 6:
            variants.add(part)
    return {v for v in variants if v}


def audit_daily_path(items):
    flagged = []
    for item in items:
        if item.get("stage") != "recognize" or not item.get("blind_reveal"):
            continue
        topic = item.get("topic") or ""
        if not topic:
            continue
        haystacks = [
            item.get("prompt") or "",
            item.get("answer") or "",
        ]
        combined = " ".join(haystacks).lower()
        for variant in _topic_variants(topic):
            pattern = r"(?<!\w)" + re.escape(variant.lower()) + r"(?!\w)"
            if re.search(pattern, combined):
                flagged.append({
                    "topic": topic,
                    "domain": item.get("domain"),
                    "concept_id": item.get("concept_id"),
                    "issue": (
                        f"blind_reveal=True but topic variant {variant!r} appears verbatim "
                        f"in prompt/answer text -- card is not actually blind"
                    ),
                })
                break
    return flagged


def main():
    sys.path.insert(0, ".")
    try:
        import runtime_entry_pasha as prod
    except ImportError as e:
        print(f"Could not import runtime_entry_pasha: {e}")
        print("Run this script from the repo root, with your venv active.")
        sys.exit(1)

    data_mod = prod.runtime_entry.data
    challenges = data_mod.CLINICAL_CHALLENGES_V119
    daily_items = data_mod.get_adaptive_items_v120()

    challenge_flags = audit_clinical_challenges(challenges)
    daily_flags = audit_daily_path(daily_items)

    print("=" * 70)
    print("QUESTION QUALITY AUDIT")
    print("=" * 70)
    print(f"Clinical Challenges scanned: {len(challenges)}")
    print(f"  Flagged: {len(challenge_flags)} "
          f"({100 * len(challenge_flags) / max(len(challenges), 1):.1f}%)")
    print(f"Daily Path 'recognize' items scanned (blind_reveal=True subset checked)")
    print(f"  Alias-revealing blind cards flagged: {len(daily_flags)}")
    print()

    if challenge_flags:
        print("-" * 70)
        print("CLINICAL CHALLENGE ISSUES")
        print("-" * 70)
        for f in challenge_flags:
            print(f"[{f['id']}] {f['domain']} / {f['topic']} (tier: {f['tier']})")
            for kind, detail in f["issues"]:
                print(f"    - {kind}: {detail}")
        print()

    if daily_flags:
        print("-" * 70)
        print("DAILY PATH ALIAS-REVEALING BLIND CARDS")
        print("-" * 70)
        seen_topics = set()
        for f in daily_flags:
            if f["topic"] in seen_topics:
                continue
            seen_topics.add(f["topic"])
            print(f"{f['domain']} / {f['topic']}")
            print(f"    - {f['issue']}")
        print()
        print(f"({len(seen_topics)} distinct topics affected)")

    report = {
        "clinical_challenge_flags": challenge_flags,
        "daily_path_flags": daily_flags,
        "totals": {
            "challenges_scanned": len(challenges),
            "challenges_flagged": len(challenge_flags),
            "daily_alias_flags": len(daily_flags),
        },
    }
    with open("question_quality_report.json", "w") as f:
        json.dump(report, f, indent=2)
    print()
    print("Full machine-readable report written to question_quality_report.json")


if __name__ == "__main__":
    main()
