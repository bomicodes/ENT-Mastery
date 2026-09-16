#!/usr/bin/env python3
"""Fail-closed all-topic Deep Curriculum mastery-depth audit (v369).

This is deliberately structural rather than lexical: every exact live canonical
concept is inventoried for foundation, application, traps, senior-decision
teaching, and total teaching surface. It complements source saturation.

The first rollout is a ratcheting non-regression gate: it fails on canonical
contract drift and on any increase above the measured depth backlog ceiling.
Reviewed clinical cohorts lower MAX_DEPTH_BACKLOG until it reaches zero.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import runtime_entry_pasha

EXPECTED_TOPICS = 325
# Initial ceiling is intentionally permissive until the first real inventory run
# establishes the exact backlog. Never raise this after ratcheting begins.
MAX_DEPTH_BACKLOG = 325
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
    data = runtime_entry_pasha.runtime_entry.data
    modules = getattr(data, "DEEP_MODULES_V6", {}) or {}
    canonical = []
    for domain, rows in modules.items():
        if not isinstance(rows, list):
            continue
        for row in rows:
            if isinstance(row, dict) and (row.get("topic") or row.get("id")):
                canonical.append((domain, row))

    failures = []
    backlog = []
    if len(canonical) != EXPECTED_TOPICS:
        failures.append(f"canonical contract drift: expected {EXPECTED_TOPICS}, found {len(canonical)}")

    keys = [(domain, str(row.get("topic") or row.get("id") or "").strip()) for domain, row in canonical]
    if len(set(keys)) != len(keys):
        failures.append("duplicate exact domain/topic canonical rows detected")

    for domain, row in canonical:
        cid = row.get("id") or f"{domain}:{row.get('topic')}"
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

    if len(backlog) > MAX_DEPTH_BACKLOG:
        failures.append(f"depth backlog regressed: expected <= {MAX_DEPTH_BACKLOG}, found {len(backlog)}")

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
            "max_depth_backlog": MAX_DEPTH_BACKLOG,
            "note": "Structural floor only; clinical correctness and source quality remain separately gated."
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("canonical_topics", "mastery_ready", "depth_backlog", "failures")}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
