"""ENT Mastery v15.4 learning-ladder audit.

This audit asks a different question from coverage_v135 and quality_v149:
does the bank teach concepts in a progression rather than only at one level?

Explicit v15.4 metadata is authoritative. Legacy cases are classified
heuristically only for reporting; this audit is informational until enough
legacy questions have been deliberately reviewed/tagged.
"""

from collections import Counter, defaultdict
import re

import recognize_stage_v127  # noqa: F401 - applies runtime merges
import data

STAGES = ("foundation", "application", "senior_decision")

_FOUNDATION = {
    "define", "definition", "which structure", "which nerve", "which artery",
    "what type", "most typical", "classically", "mechanism", "anatomy",
    "audiogram", "staging", "criterion", "criteria",
}
_APPLICATION = {
    "best next", "next step", "management", "workup", "treat", "therapy",
    "interpret", "which test", "diagnostic", "indication", "observe",
    "surveillance", "biopsy", "imaging",
}
_SENIOR = {
    "during surgery", "during thyroidectomy", "during bronchoscopy", "during orif",
    "postoperative", "post-op", "overnight", "suddenly", "deteriorates",
    "worsening", "desatur", "stridor", "hematoma", "compromise", "salvage",
    "return to the or", "change the plan", "what should change", "before closure",
    "loss of signal", "vision", "hemorrhage", "airway",
}


def _norm(value):
    return re.sub(r"\s+", " ", str(value or "").strip().lower())


def _text(q):
    return " ".join(_norm(q.get(k)) for k in
                    ("topic", "stem", "explanation", "board_pearl", "curveball", "focus"))


def infer_stage(q):
    explicit = q.get("learning_stage")
    if explicit in STAGES:
        return explicit, "explicit"
    text = _text(q)
    senior_score = sum(term in text for term in _SENIOR)
    application_score = sum(term in text for term in _APPLICATION)
    foundation_score = sum(term in text for term in _FOUNDATION)
    if q.get("focus") in {"OR_prep", "overnight_call", "postoperative_call"}:
        senior_score += 2
    if senior_score >= 2:
        return "senior_decision", "heuristic"
    if application_score >= max(1, foundation_score):
        return "application", "heuristic"
    return "foundation", "heuristic"


def build_report():
    by_cid = defaultdict(list)
    for q in data.CLINICAL_CHALLENGES_V119:
        cid = q.get("concept_id")
        if cid:
            by_cid[cid].append(q)

    domains = {}
    complete_explicit = []
    missing = []
    for domain, modules in data.DEEP_MODULES_V6.items():
        rows = []
        for module in modules:
            topic = module.get("topic")
            if not topic:
                continue
            cid = data._v6_item_id(domain, topic)
            linked = by_cid.get(cid, [])
            explicit_counts = Counter()
            inferred_counts = Counter()
            for q in linked:
                stage, source = infer_stage(q)
                inferred_counts[stage] += 1
                if source == "explicit":
                    explicit_counts[stage] += 1
            explicit_complete = all(explicit_counts[s] > 0 for s in STAGES)
            inferred_complete = all(inferred_counts[s] > 0 for s in STAGES)
            row = {
                "topic": topic,
                "cases": len(linked),
                "explicit": dict(explicit_counts),
                "inferred": dict(inferred_counts),
                "explicit_complete": explicit_complete,
                "inferred_complete": inferred_complete,
            }
            rows.append(row)
            if explicit_complete:
                complete_explicit.append((domain, topic))
            elif not inferred_complete:
                missing.append((domain, topic, [s for s in STAGES if inferred_counts[s] == 0]))
        domains[domain] = rows
    return {
        "domains": domains,
        "explicit_complete": complete_explicit,
        "heuristic_missing": missing,
    }


def print_report(report):
    print("=== ENT MASTERY v15.4 LEARNING-LADDER AUDIT ===")
    print(f"EXPLICIT_COMPLETE_LADDERS|{len(report['explicit_complete'])}")
    for domain, topic in report["explicit_complete"]:
        print(f"EXPLICIT_LADDER|{domain}|{topic}|foundation+application+senior_decision")
    for domain, rows in report["domains"].items():
        total = len(rows)
        inferred_complete = sum(1 for r in rows if r["inferred_complete"])
        print(f"LADDER_DOMAIN|{domain}|{inferred_complete}|{total}")
    print(f"HEURISTIC_LADDER_GAPS|{len(report['heuristic_missing'])}")
    for domain, topic, stages in report["heuristic_missing"]:
        print(f"LADDER_GAP|{domain}|{topic}|missing={','.join(stages)}")
    print("LADDER_AUDIT_MODE|informational")
    print("NOTE|Heuristic legacy classification is a prioritization aid, not a release gate. Explicit reviewed metadata is the target state.")


if __name__ == "__main__":
    print_report(build_report())
