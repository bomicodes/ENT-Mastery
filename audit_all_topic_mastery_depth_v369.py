#!/usr/bin/env python3
"""Fail-closed all-topic Deep Curriculum mastery-depth audit (v369).

This is deliberately structural rather than lexical: every exact live canonical
concept must expose enough teaching surface for foundation, application, and
senior-decision review. It complements (does not replace) source saturation.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import runtime_entry

EXPECTED_TOPICS = 325
OUT = Path("ALL_TOPIC_MASTERY_DEPTH_V369.json")
WORD_RE = re.compile(r"\b[\w’'-]+\b")


def words(value):
    if isinstance(value, str):
        return len(WORD_RE.findall(value))
    if isinstance(value, list):
        return sum(words(x) for x in value)
    if isinstance(value, dict):
        return sum(words(v) for v in value.values())
    return 0


def items(value):
    return len(value) if isinstance(value, list) else 0


def main():
    data = runtime_entry.data
    modules = getattr(data, "DEEP_MODULES_V6", {})
    canonical = []
    for domain, rows in modules.items():
        if not isinstance(rows, list):
            continue
        for row in rows:
            if isinstance(row, dict) and row.get("id"):
                canonical.append((domain, row))

    failures = []
    backlog = []
    if len(canonical) != EXPECTED_TOPICS:
        failures.append(f"canonical contract drift: expected {EXPECTED_TOPICS}, found {len(canonical)}")

    for domain, row in canonical:
        cid = row.get("id")
        title = row.get("title") or row.get("topic") or cid
        overview_words = words(row.get("overview"))
        kp = items(row.get("keyPoints"))
        pitfalls = items(row.get("pitfalls"))
        pearls = items(row.get("pearls"))
        total_words = words({
            "overview": row.get("overview"),
            "keyPoints": row.get("keyPoints"),
            "pitfalls": row.get("pitfalls"),
            "pearls": row.get("pearls"),
        })
        reasons = []
        if overview_words < 45:
            reasons.append(f"foundation overview thin ({overview_words} words)")
        if kp < 4:
            reasons.append(f"application keyPoints thin ({kp})")
        if pitfalls < 2:
            reasons.append(f"individualized traps thin ({pitfalls})")
        if pearls < 1:
            reasons.append("senior-decision pearl missing")
        if total_words < 180:
            reasons.append(f"teaching surface thin ({total_words} words)")
        if reasons:
            backlog.append({"id": cid, "title": title, "domain": domain, "reasons": reasons,
                            "overview_words": overview_words, "keyPoints": kp,
                            "pitfalls": pitfalls, "pearls": pearls, "teaching_words": total_words})

    report = {
        "audit": "all-topic-mastery-depth-v369",
        "canonical_topics": len(canonical),
        "mastery_ready": len(canonical) - len(backlog),
        "depth_backlog": len(backlog),
        "backlog": backlog,
        "failures": failures,
        "policy": {
            "overview_words_min": 45,
            "keyPoints_min": 4,
            "pitfalls_min": 2,
            "pearls_min": 1,
            "teaching_words_min": 180,
            "note": "Structural floor only; clinical correctness and source quality remain separately gated."
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("canonical_topics", "mastery_ready", "depth_backlog", "failures")}, indent=2))
    if failures or backlog:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
