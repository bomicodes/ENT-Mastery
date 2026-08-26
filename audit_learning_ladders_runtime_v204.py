"""v20.5 runtime-aware learning-ladder hard gate.

Imports runtime_entry so all production ladder mutations are present before
evaluation. The completed Otology domain remains a full-domain hard gate, while
every concept deliberately reviewed in any domain must independently carry a
complete foundation -> application -> senior_decision ladder.

The gate is substantive rather than verbosity-driven: concise anatomy stems and
useful "Correct. ..." teaching rationales are valid. Generic, duplicated,
missing, malformed, orphaned, badly linked, or incomplete reviewed material is not.
"""

from collections import Counter, defaultdict
import re

import runtime_entry


data = runtime_entry.data
STAGES = ("foundation", "application", "senior_decision")
OTOLOGY = "Otology / Neurotology"

_GENERIC_MARKERS = (
    "use the mechanism, anatomy, and management priority in the explanation",
    "compare this option with the time-critical management principle in the explanation",
    "compare this option with the management principle and anatomy in the explanation",
    "review the explanation and compare the management principle with the clinical context",
    "this option misses the key clinical discriminator described in the explanation",
    "this option does not address the key discriminator in the scenario",
    "this option misses the key discriminator in the scenario",
    "this option misses the key clinical discriminator",
    "does not best address the management discriminator in this scenario",
    "pending distractor-specific review",
)

_REQUIRED = (
    "id", "domain", "topic", "concept_id", "learning_stage", "stem",
    "choices", "answer", "explanation", "why_wrong", "board_pearl", "curveball",
)


def _norm(value):
    return re.sub(r"\s+", " ", str(value or "").strip().lower())


def _words(value):
    return re.findall(r"[a-z0-9]+", _norm(value))


def _canonical_pairs():
    return {
        (domain, module.get("topic"))
        for domain, modules in data.DEEP_MODULES_V6.items()
        for module in modules
        if module.get("topic")
    }


def _quality_errors(q):
    errors = []
    for key in _REQUIRED:
        if q.get(key) in (None, ""):
            errors.append(f"missing {key}")

    choices = list(q.get("choices") or [])
    reasons = list(q.get("why_wrong") or [])
    if len(choices) < 4:
        errors.append("fewer than 4 choices")
    if len(set(_norm(choice) for choice in choices)) != len(choices):
        errors.append("duplicate choices")

    try:
        answer = int(q.get("answer"))
    except (TypeError, ValueError):
        answer = -1
    if not 0 <= answer < len(choices):
        errors.append("invalid answer index")

    if len(reasons) != len(choices):
        errors.append("why_wrong length mismatch")
    else:
        wrong = []
        for i, reason in enumerate(reasons):
            text = _norm(reason)
            if i == answer:
                if not text.startswith("correct."):
                    errors.append("correct option rationale does not start with 'Correct.'")
                continue
            wrong.append(text)
            if len(_words(reason)) < 4:
                errors.append(f"thin distractor rationale index {i}")
            if any(marker in text for marker in _GENERIC_MARKERS):
                errors.append(f"generic distractor rationale index {i}")
        if wrong and len(set(wrong)) != len(wrong):
            errors.append("duplicate distractor rationales")

    if len(_words(q.get("stem"))) < 8:
        errors.append("thin stem")
    if len(_words(q.get("explanation"))) < 10:
        errors.append("thin explanation")
    if len(_words(q.get("board_pearl"))) < 4:
        errors.append("thin board pearl")
    if len(_words(q.get("curveball"))) < 4:
        errors.append("thin curveball")
    return errors


def _stage_row(domain, topic, linked):
    counts = Counter(
        q.get("learning_stage")
        for q in linked
        if q.get("learning_stage") in STAGES
    )
    missing = [stage for stage in STAGES if counts[stage] == 0]
    return {
        "domain": domain,
        "topic": topic,
        "cases": len(linked),
        "stages": {stage: counts[stage] for stage in STAGES},
        "missing": missing,
    }


def build_report():
    cases = list(data.CLINICAL_CHALLENGES_V119)
    canonical = _canonical_pairs()
    ids = [q.get("id") for q in cases if q.get("id")]
    duplicate_ids = sorted(qid for qid, n in Counter(ids).items() if n > 1)

    reviewed = [q for q in cases if q.get("ladder_reviewed")]
    reviewed_errors = {}
    orphan_reviewed = []
    bad_links = []
    reviewed_pairs = set()
    for q in reviewed:
        key = (q.get("domain"), q.get("topic"))
        reviewed_pairs.add(key)
        if key not in canonical:
            orphan_reviewed.append(q.get("id"))
        expected = data._v6_item_id(q.get("domain"), q.get("topic"))
        if q.get("concept_id") != expected:
            bad_links.append((q.get("id"), q.get("concept_id"), expected))
        errors = _quality_errors(q)
        if errors:
            reviewed_errors[q.get("id")] = sorted(set(errors))

    by_cid = defaultdict(list)
    for q in cases:
        cid = q.get("concept_id")
        if cid:
            by_cid[cid].append(q)

    reviewed_rows = []
    reviewed_ladder_gaps = []
    for domain, topic in sorted(reviewed_pairs):
        if (domain, topic) not in canonical:
            continue
        cid = data._v6_item_id(domain, topic)
        row = _stage_row(domain, topic, by_cid.get(cid, []))
        reviewed_rows.append(row)
        if row["missing"]:
            reviewed_ladder_gaps.append(row)

    domain_progress = []
    for domain, modules in data.DEEP_MODULES_V6.items():
        topics = [m.get("topic") for m in modules if m.get("topic")]
        reviewed_topics = {
            topic for d, topic in reviewed_pairs if d == domain and (d, topic) in canonical
        }
        complete = 0
        for topic in reviewed_topics:
            cid = data._v6_item_id(domain, topic)
            if not _stage_row(domain, topic, by_cid.get(cid, []))["missing"]:
                complete += 1
        domain_progress.append({
            "domain": domain,
            "canonical": len(topics),
            "reviewed": len(reviewed_topics),
            "complete": complete,
        })

    otology_rows = []
    otology_gaps = []
    modules = data.DEEP_MODULES_V6.get(OTOLOGY, [])
    for module in modules:
        topic = module.get("topic")
        if not topic:
            continue
        cid = data._v6_item_id(OTOLOGY, topic)
        row = _stage_row(OTOLOGY, topic, by_cid.get(cid, []))
        otology_rows.append(row)
        if row["missing"]:
            otology_gaps.append(row)

    reviewed_answer_counts = Counter()
    for q in reviewed:
        try:
            reviewed_answer_counts[int(q.get("answer"))] += 1
        except (TypeError, ValueError):
            pass
    reviewed_n = sum(reviewed_answer_counts.values())
    max_answer_share = (
        max(reviewed_answer_counts.values()) / reviewed_n
        if reviewed_n and reviewed_answer_counts else 0.0
    )
    answer_bias = max_answer_share > 0.40

    return {
        "total_cases": len(cases),
        "reviewed_cases": len(reviewed),
        "duplicate_ids": duplicate_ids,
        "orphan_reviewed": orphan_reviewed,
        "bad_links": bad_links,
        "reviewed_errors": reviewed_errors,
        "reviewed_rows": reviewed_rows,
        "reviewed_ladder_gaps": reviewed_ladder_gaps,
        "domain_progress": domain_progress,
        "otology_topic_count": len(otology_rows),
        "otology_rows": otology_rows,
        "otology_gaps": otology_gaps,
        "answer_counts": dict(sorted(reviewed_answer_counts.items())),
        "max_answer_share": round(max_answer_share, 3),
        "answer_bias": answer_bias,
    }


def print_report(report):
    print("=== ENT MASTERY v20.5 RUNTIME LEARNING-LADDER GATE ===")
    print(f"TOTAL_CASES|{report['total_cases']}")
    print(f"REVIEWED_CASES|{report['reviewed_cases']}")
    print(f"DUPLICATE_IDS|{len(report['duplicate_ids'])}")
    for qid in report["duplicate_ids"]:
        print(f"DUPLICATE_ID|{qid}")
    print(f"REVIEWED_ORPHANS|{len(report['orphan_reviewed'])}")
    for qid in report["orphan_reviewed"]:
        print(f"REVIEWED_ORPHAN|{qid}")
    print(f"BAD_CONCEPT_LINKS|{len(report['bad_links'])}")
    for qid, actual, expected in report["bad_links"]:
        print(f"BAD_CONCEPT_LINK|{qid}|actual={actual}|expected={expected}")
    print(f"REVIEWED_QUALITY_ERRORS|{len(report['reviewed_errors'])}")
    for qid, errors in sorted(report["reviewed_errors"].items()):
        print(f"REVIEWED_QUALITY_ERROR|{qid}|{' ; '.join(errors)}")

    print(f"REVIEWED_LADDER_GAPS|{len(report['reviewed_ladder_gaps'])}")
    for row in report["reviewed_ladder_gaps"]:
        print(
            f"REVIEWED_LADDER_GAP|{row['domain']}|{row['topic']}|"
            f"missing={','.join(row['missing'])}"
        )

    for row in report["domain_progress"]:
        print(
            f"DOMAIN_REVIEW_PROGRESS|{row['domain']}|"
            f"canonical={row['canonical']}|reviewed={row['reviewed']}|complete={row['complete']}"
        )

    print(f"OTOLOGY_CANONICAL_TOPICS|{report['otology_topic_count']}")
    for row in report["otology_rows"]:
        stage_text = ",".join(f"{s}={row['stages'][s]}" for s in STAGES)
        print(f"OTOLOGY_LADDER|{row['topic']}|cases={row['cases']}|{stage_text}")
    print(f"OTOLOGY_LADDER_GAPS|{len(report['otology_gaps'])}")

    counts = ",".join(f"{k}={v}" for k, v in report["answer_counts"].items())
    print(f"REVIEWED_ANSWER_POSITIONS|{counts}|max_share={report['max_answer_share']}")
    print("RUNTIME_LADDER_EXIT_STATUS|" + ("1" if has_failures(report) else "0"))


def has_failures(report):
    return bool(
        report["duplicate_ids"]
        or report["orphan_reviewed"]
        or report["bad_links"]
        or report["reviewed_errors"]
        or report["reviewed_ladder_gaps"]
        or report["otology_topic_count"] != 45
        or report["otology_gaps"]
        or report["answer_bias"]
    )


if __name__ == "__main__":
    report = build_report()
    print_report(report)
    if has_failures(report):
        raise SystemExit(1)