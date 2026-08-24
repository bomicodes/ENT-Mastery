"""ENT Mastery v13.5 canonical coverage audit.

Audits the live, runtime-patched curriculum rather than raw source fragments.
Default mode is informational and exits 0 so routine audits do not create
failure-alert noise. Use --strict when a CI gate should fail below 100%.

Coverage milestone 1: every canonical DEEP_MODULES_V6 concept has at least one
linked clinical vignette by concept_id. A separate depth report flags concepts
with only one vignette or missing teaching/curveball fields; those flags are not
silently treated as equivalent to complete resident-level depth.
"""

import argparse
import json
from collections import Counter, defaultdict

# Importing the runtime integration applies v13.x topic/vignette merges before
# we inspect the registries.
import recognize_stage_v127  # noqa: F401
import data


def build_report():
    cases = list(data.CLINICAL_CHALLENGES_V119)
    case_counts = Counter(q.get("concept_id") for q in cases if q.get("concept_id"))
    cases_by_concept = defaultdict(list)
    for q in cases:
        cid = q.get("concept_id")
        if cid:
            cases_by_concept[cid].append(q)

    domains = {}
    total_topics = total_covered = 0
    for domain, modules in data.DEEP_MODULES_V6.items():
        canonical = []
        for module in modules:
            topic = module.get("topic")
            if not topic:
                continue
            cid = data._v6_item_id(domain, topic)
            canonical.append((topic, cid))

        missing = [topic for topic, cid in canonical if case_counts[cid] == 0]
        shallow = []
        depth_gaps = []
        for topic, cid in canonical:
            linked = cases_by_concept.get(cid, [])
            if len(linked) == 1:
                shallow.append(topic)
            if linked:
                # At least one question should contain the teaching scaffolding
                # expected of a discriminating resident/chief-level case.
                has_explanation = any((q.get("explanation") or "").strip() for q in linked)
                has_curveball = any((q.get("curveball") or "").strip() for q in linked)
                has_pearl = any((q.get("board_pearl") or "").strip() for q in linked)
                if not (has_explanation and has_curveball and has_pearl):
                    depth_gaps.append(topic)

        n = len(canonical)
        covered = n - len(missing)
        pct = round(100.0 * covered / n, 1) if n else 100.0
        domains[domain] = {
            "topics": n,
            "covered": covered,
            "coverage_pct": pct,
            "missing": missing,
            "single_vignette": shallow,
            "teaching_scaffold_gaps": depth_gaps,
        }
        total_topics += n
        total_covered += covered

    return {
        "total_topics": total_topics,
        "total_covered": total_covered,
        "overall_coverage_pct": round(100.0 * total_covered / total_topics, 1) if total_topics else 100.0,
        "domains": domains,
    }


def print_text(report, show_depth=False):
    print(f"ENT Mastery canonical vignette coverage: {report['total_covered']}/{report['total_topics']} "
          f"({report['overall_coverage_pct']:.1f}%)")
    for domain, item in report["domains"].items():
        print(f"\n{domain}: {item['covered']}/{item['topics']} ({item['coverage_pct']:.1f}%)")
        if item["missing"]:
            print("  MISSING:")
            for topic in item["missing"]:
                print(f"    - {topic}")
        if show_depth:
            if item["single_vignette"]:
                print("  SINGLE-VIGNETTE (depth review):")
                for topic in item["single_vignette"]:
                    print(f"    - {topic}")
            if item["teaching_scaffold_gaps"]:
                print("  TEACHING-SCAFFOLD GAP:")
                for topic in item["teaching_scaffold_gaps"]:
                    print(f"    - {topic}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--depth", action="store_true")
    parser.add_argument("--strict", action="store_true",
                        help="Exit 1 unless every canonical topic has a vignette")
    args = parser.parse_args()

    report = build_report()
    if args.as_json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print_text(report, show_depth=args.depth)

    if args.strict and report["total_covered"] != report["total_topics"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
