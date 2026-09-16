#!/usr/bin/env python3
"""All-topic learner-facing Deep Curriculum depth inventory (v37.1).

Scores the fully assembled production canonical rows rather than assuming mastery
content lives in overview/keyPoints/pitfalls/pearls. This first pass is an inventory
and fail-closed canonical-integrity gate; clinical cohorts can ratchet the measured
backlog after the baseline artifact is reviewed.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import runtime_entry_pasha

EXPECTED_TOPICS = 325
OUT = Path("ALL_TOPIC_LEARNER_DEPTH_V371.json")
WORD_RE = re.compile(r"\b[\w’'-]+\b")
# Fields actually rendered/assembled by the live curriculum patches. Metadata and
# source_basis are intentionally excluded from teaching-depth credit.
TEACHING_FIELDS = (
    "recognize", "localize", "workup", "manage", "operate", "teach",
    "overview", "keyPoints", "pitfalls", "pearls", "clinicalPearls",
    "decisionPoints", "differential", "diagnosis", "treatment", "complications",
)
APPLICATION_FIELDS = ("workup", "manage", "operate", "decisionPoints", "treatment")
FOUNDATION_FIELDS = ("recognize", "localize", "overview", "diagnosis", "differential")
SENIOR_FIELDS = ("operate", "teach", "pearls", "clinicalPearls", "decisionPoints", "complications")


def words(value):
    if isinstance(value, str):
        return len(WORD_RE.findall(value))
    if isinstance(value, list):
        return sum(words(x) for x in value)
    if isinstance(value, dict):
        return sum(words(v) for v in value.values())
    return 0


def field_words(row, names):
    return sum(words(row.get(name)) for name in names)


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
    if len(canonical) != EXPECTED_TOPICS:
        failures.append(f"canonical contract drift: expected {EXPECTED_TOPICS}, found {len(canonical)}")
    keys = [(d, str(r.get("topic") or r.get("id") or "").strip()) for d, r in canonical]
    if len(set(keys)) != len(keys):
        failures.append("duplicate exact domain/topic canonical rows detected")

    backlog = []
    domain_summary = {}
    for domain, row in canonical:
        cid = row.get("id") or f"{domain}:{row.get('topic')}"
        title = row.get("title") or row.get("topic") or cid
        foundation = field_words(row, FOUNDATION_FIELDS)
        application = field_words(row, APPLICATION_FIELDS)
        senior = field_words(row, SENIOR_FIELDS)
        total = field_words(row, TEACHING_FIELDS)
        active = [f for f in TEACHING_FIELDS if words(row.get(f)) > 0]
        reasons = []
        # Conservative structural floor: enough learner-facing material to support
        # foundation -> application -> senior reasoning without prescribing prose schema.
        if foundation < 35:
            reasons.append(f"foundation surface thin ({foundation} words)")
        if application < 70:
            reasons.append(f"application surface thin ({application} words)")
        if senior < 45:
            reasons.append(f"senior-decision surface thin ({senior} words)")
        if total < 180:
            reasons.append(f"total learner-facing teaching thin ({total} words)")
        if len(active) < 3:
            reasons.append(f"teaching dimensions thin ({len(active)} active fields)")
        ready = not reasons
        ds = domain_summary.setdefault(domain, {"topics": 0, "ready": 0, "backlog": 0})
        ds["topics"] += 1
        ds["ready" if ready else "backlog"] += 1
        if reasons:
            backlog.append({
                "id": cid, "title": title, "domain": domain, "reasons": reasons,
                "foundation_words": foundation, "application_words": application,
                "senior_words": senior, "teaching_words": total, "active_fields": active,
                "has_source_basis": bool(row.get("source_basis")),
            })

    report = {
        "audit": "all-topic-learner-depth-v371",
        "canonical_topics": len(canonical),
        "mastery_ready_structural": len(canonical) - len(backlog),
        "depth_backlog": len(backlog),
        "domain_summary": domain_summary,
        "backlog": backlog,
        "failures": failures,
        "policy": {
            "foundation_words_min": 35, "application_words_min": 70,
            "senior_words_min": 45, "teaching_words_min": 180,
            "active_teaching_fields_min": 3,
            "note": "Inventory floor on final assembled learner-facing fields; source quality and clinical correctness remain separately gated."
        },
    }
    OUT.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("canonical_topics", "mastery_ready_structural", "depth_backlog", "domain_summary", "failures")}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
