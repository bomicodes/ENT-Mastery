"""v47.1 Concept Check rewrite.

309 multiple-choice Concept Checks were auto-generated from one template:
  "A patient has been diagnosed with <Topic>. Based on the current curriculum
   framework, which management principle is most appropriate?"
with distractors copied (often truncated) from *other* topics' management text, so
the question tested "which sentence belongs to this topic" rather than medicine.

This module replaces each templated item in place with an authored, board-style
vignette that tests the topic's mechanism or key decision.  Authored items live in
``cc_v471/<domain>.py`` as::

    CHECKS = [
        (topic, stem, correct_choice,
         [(distractor, why_it_is_wrong), x3],
         explanation, board_pearl),
        ...
    ]

IDs, concept_id, domain, topic and all review metadata are preserved so learner
history and audits keep working.  The correct answer position rotates A-D across
the bank so position carries no signal.  Free-text Concept Checks are untouched.
"""
from __future__ import annotations

import importlib
import pkgutil
import re

TEMPLATE_RE = re.compile(r"curriculum framework", re.I)


def _load():
    import cc_v471
    by_topic = {}
    for info in sorted(pkgutil.iter_modules(cc_v471.__path__), key=lambda i: i.name):
        mod = importlib.import_module("cc_v471." + info.name)
        for row in getattr(mod, "CHECKS", []):
            topic, stem, correct, distractors, explanation, pearl = row
            if len(distractors) != 3:
                raise RuntimeError("v47.1 check for %s needs exactly 3 distractors" % topic)
            by_topic.setdefault(topic, []).append(row)
    return by_topic


def install_concept_checks_v471(data):
    authored = _load()
    used = {t: 0 for t in authored}
    replaced, missing, slot = 0, [], 0
    for q in data.CONCEPT_CHECKS_V112:
        stem = q.get("stem") or q.get("prompt") or ""
        # Only live multiple-choice templates. Items an earlier patch already
        # converted to deep free-response (empty choices + answer_text) stay as-is.
        if not (isinstance(q.get("choices"), list) and q["choices"] and TEMPLATE_RE.search(stem)):
            continue
        rows = authored.get(q.get("topic"))
        if not rows or used[q["topic"]] >= len(rows):
            missing.append(q.get("id"))
            continue
        topic, stem, correct, distractors, explanation, pearl = rows[used[q["topic"]]]
        used[q["topic"]] += 1
        pos = slot % 4
        slot += 1
        choices = [d for d, _ in distractors]
        why = [w for _, w in distractors]
        choices.insert(pos, correct)
        why.insert(pos, "Correct.")
        q.update({
            "stem": stem,
            "choices": choices,
            "answer": pos,
            "explanation": explanation,
            "why_wrong": why,
            "board_pearl": pearl,
            "authored_v471": True,
        })
        q.pop("prompt", None)
        replaced += 1
    leftover = sorted(t for t, n in used.items() if n < len(authored[t]))
    result = {"replaced": replaced, "missing": missing, "unused_topics": leftover}
    data.CONCEPT_CHECKS_V471 = result
    if missing:
        raise RuntimeError("v47.1 Concept Checks still templated: %s" % missing[:10])
    return result
