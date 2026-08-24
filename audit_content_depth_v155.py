"""v15.5 — Content-depth audit: duplicates, distractor plausibility,
topic-weighted depth targets, and escalation-tag overuse.

This is deliberately a SEPARATE tool from preflight_boot_check_v155.py.
Boot health is a gate (fails the pipeline); everything in this file is
informational, the same posture as audit_learning_ladders_v154.py, because
these are content-quality judgment calls that deserve human review rather
than blocking a deploy automatically.

Covers the five tooling gaps identified after the v15.1-v15.4 audit cycle:

1. Near-duplicate detection within a topic — two "foundation" questions that
   are actually the same clinical scenario asked twice don't satisfy the
   foundation->application->senior_decision ladder; they just look like they
   do. (Confirmed real: v11_oto_02 and v135_oto_03 under Cholesteatoma.)

2. Distractor plausibility — flags choice sets where the wrong answers share
   almost no clinical vocabulary with the correct answer/stem, the "BPPV as a
   distractor for Gradenigo syndrome" failure mode. Heuristic, not definitive
   — flags candidates for human review, does not auto-fail anything.

3. Topic-weighted depth targets — replaces the flat ">=2 vignettes" bar with
   a rough high/medium/low board-and-call-yield weight per topic, so a narrow
   topic with 2 excellent questions isn't flagged the same way as a
   high-yield topic that also only has 2.

4. Escalation-tag overuse — flags topics where every existing vignette
   carries an emergency/OR/call focus tag with zero plain foundation-level
   content, the "everything is a chief-level dilemma" failure mode this
   whole framework exists to avoid. (Confirmed real: Carotid Blowout
   Syndrome, 5/5 vignettes are all sentinel-bleed/intraoperative scenarios.)

5. Legacy tag confidence — the learning_stage ladder audit's own docstring
   already says heuristic classification is "a prioritization aid, not a
   release gate." This tool surfaces exactly how much of the bank is still
   running on that guess (as opposed to explicit reviewed metadata) so the
   gap doesn't quietly stay invisible as the bank grows.

All checks are informational and exit 0 — this is a report to guide the next
pass, not a merge gate. Use --verbose for full detail on any section.
"""

import argparse
import difflib
import re
from collections import Counter, defaultdict

import recognize_stage_v127  # noqa: F401 - applies runtime merges
import data


# ---------------------------------------------------------------------------
# 1. Near-duplicate detection within a topic
# ---------------------------------------------------------------------------

_STEM_SIMILARITY_THRESHOLD = 0.72  # difflib ratio; tuned against the known
                                    # true positive (v11_oto_02 / v135_oto_03
                                    # score ~0.80) with margin below it.


def _norm_stem(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def find_near_duplicate_stems(challenges):
    """Returns [(topic, id_a, id_b, ratio), ...] for stem pairs sharing a
    topic that look like the same clinical scenario asked twice."""
    by_topic = defaultdict(list)
    for q in challenges:
        key = (q.get("domain"), q.get("canonical_topic") or q.get("topic"))
        by_topic[key].append(q)

    findings = []
    for key, qs in by_topic.items():
        if len(qs) < 2:
            continue
        for i in range(len(qs)):
            for j in range(i + 1, len(qs)):
                a, b = qs[i], qs[j]
                ratio = difflib.SequenceMatcher(
                    None, _norm_stem(a.get("stem")), _norm_stem(b.get("stem"))
                ).ratio()
                if ratio >= _STEM_SIMILARITY_THRESHOLD:
                    findings.append((key, a["id"], b["id"], round(ratio, 2)))
    return findings


# ---------------------------------------------------------------------------
# 2. Distractor plausibility (heuristic)
# ---------------------------------------------------------------------------

_STOPWORDS = {
    "the", "a", "an", "of", "to", "and", "or", "is", "in", "for", "with",
    "on", "at", "this", "that", "as", "by", "be", "not", "does", "do",
    "which", "what", "most", "best", "only", "no", "than", "correct",
    "option", "answer", "patient", "these", "would", "should", "can",
    "here", "given",
}


def _content_words(text):
    return {
        w for w in re.findall(r"[a-z][a-z\-]{2,}", (text or "").lower())
        if w not in _STOPWORDS
    }


def find_implausible_distractors(challenges, min_overlap_words=1):
    """Flags choices that share almost no clinical vocabulary with either the
    stem or the correct answer — candidates for the 'BPPV as a distractor for
    Gradenigo syndrome' failure mode. Heuristic: real synonyms/abbreviations
    can still trip this, so treat findings as a review list, not a verdict."""
    findings = []
    for q in challenges:
        choices = q.get("choices") or []
        try:
            answer_idx = int(q.get("answer"))
        except (TypeError, ValueError):
            continue
        if not (0 <= answer_idx < len(choices)):
            continue
        stem_words = _content_words(q.get("stem"))
        correct_words = _content_words(choices[answer_idx])
        reference = stem_words | correct_words
        if not reference:
            continue
        for idx, choice in enumerate(choices):
            if idx == answer_idx:
                continue
            choice_words = _content_words(choice)
            if not choice_words:
                continue
            overlap = choice_words & reference
            if len(overlap) < min_overlap_words:
                findings.append((q["id"], q.get("topic"), choice, idx))
    return findings


# ---------------------------------------------------------------------------
# 3. Topic-weighted depth targets
# ---------------------------------------------------------------------------

# Rough, deliberately coarse starting weights. This is a first pass meant to
# be refined by someone with board-pass-rate/service-call-volume data, not a
# final answer — the point is replacing a flat ">=2 for everyone" bar with
# *some* signal that high-yield topics deserve more than narrow ones.
_HIGH_YIELD_KEYWORDS = (
    "cholesteatoma", "sudden sensorineural", "epistaxis", "thyroidectomy",
    "carotid blowout", "airway foreign body", "epiglottitis", "peritonsillar",
    "deep neck", "obstructive sleep apnea", "osa", "laryngeal", "thyroid cancer",
    "parathyroid", "vestibular schwannoma", "tonsillectomy", "tracheostomy",
    "facial paralysis", "otitis media", "sinusitis", "vocal fold",
    "hearing loss", "rhinosinusitis", "neck mass", "squamous cell",
)
_NARROW_KEYWORDS = (
    "hair restoration", "aesthetic facial analysis", "aging face",
    "restless legs", "circadian rhythm", "narcolepsy",
)


def topic_depth_target(domain, topic):
    """Returns (target_min, weight_label) for a topic."""
    t = (topic or "").lower()
    if any(k in t for k in _NARROW_KEYWORDS):
        return 2, "narrow"
    if any(k in t for k in _HIGH_YIELD_KEYWORDS):
        return 4, "high_yield"
    return 2, "standard"


def find_underweighted_high_yield_topics(challenges):
    counts = Counter()
    for q in challenges:
        key = (q.get("domain"), q.get("canonical_topic") or q.get("topic"))
        counts[key] += 1
    findings = []
    for (domain, topic), n in counts.items():
        target, label = topic_depth_target(domain, topic)
        if label == "high_yield" and n < target:
            findings.append((domain, topic, n, target))
    return findings


# ---------------------------------------------------------------------------
# 4. Escalation-tag overuse ("everything is a chief-level dilemma")
# ---------------------------------------------------------------------------

_ESCALATION_FOCI = {"overnight_call", "OR_prep", "postoperative_call"}


def find_escalation_only_topics(challenges):
    """Flags topics where every vignette carries an escalation focus tag and
    none is plain foundational content — the inverse failure mode from
    'nothing but recall questions'."""
    by_topic = defaultdict(list)
    for q in challenges:
        key = (q.get("domain"), q.get("canonical_topic") or q.get("topic"))
        by_topic[key].append(q)
    findings = []
    for key, qs in by_topic.items():
        if len(qs) < 2:
            continue
        foci = [q.get("focus") for q in qs]
        escalation_count = sum(1 for f in foci if f in _ESCALATION_FOCI)
        if escalation_count == len(qs):
            findings.append((key[0], key[1], len(qs)))
    return findings


# ---------------------------------------------------------------------------
# 5. Legacy tag confidence
# ---------------------------------------------------------------------------

def learning_stage_confidence(challenges):
    total = len(challenges)
    explicit = sum(1 for q in challenges if q.get("learning_stage") is not None)
    return explicit, total


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args()

    challenges = data.CLINICAL_CHALLENGES_V119

    dupes = find_near_duplicate_stems(challenges)
    print(f"DUPLICATE_STEM_PAIRS|{len(dupes)}")
    for (domain, topic), a, b, ratio in dupes:
        print(f"DUPLICATE_STEM|{domain}|{topic}|{a}|{b}|ratio={ratio}")

    implausible = find_implausible_distractors(challenges)
    print(f"IMPLAUSIBLE_DISTRACTORS|{len(implausible)}")
    if args.verbose:
        for qid, topic, choice, idx in implausible:
            print(f"IMPLAUSIBLE_DISTRACTOR|{qid}|{topic}|choice[{idx}]={choice[:60]!r}")
    else:
        by_topic = Counter(topic for _, topic, _, _ in implausible)
        for topic, n in by_topic.most_common(15):
            print(f"IMPLAUSIBLE_DISTRACTOR_TOPIC|{topic}|{n}")

    underweighted = find_underweighted_high_yield_topics(challenges)
    print(f"UNDERWEIGHTED_HIGH_YIELD_TOPICS|{len(underweighted)}")
    for domain, topic, n, target in underweighted:
        print(f"UNDERWEIGHTED|{domain}|{topic}|has={n}|target={target}")

    escalation_only = find_escalation_only_topics(challenges)
    print(f"ESCALATION_ONLY_TOPICS|{len(escalation_only)}")
    for domain, topic, n in escalation_only:
        print(f"ESCALATION_ONLY|{domain}|{topic}|n={n}|no_foundation_content")

    explicit, total = learning_stage_confidence(challenges)
    pct = round(100 * explicit / total, 1) if total else 0.0
    print(f"LEARNING_STAGE_EXPLICIT_COVERAGE|{explicit}/{total}|{pct}%")

    print("CONTENT_DEPTH_AUDIT_MODE|informational")
    print(
        "NOTE|All findings here are review candidates, not a release gate. "
        "Distractor-plausibility and topic-weight checks are heuristic "
        "first passes and should be refined as real data becomes available."
    )


if __name__ == "__main__":
    main()
