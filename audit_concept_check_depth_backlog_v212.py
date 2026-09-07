"""v20.12 live-canonical Concept Check depth backlog gate."""
import json
import os
from audit_concept_check_depth_backlog_v211 import main as _v211_main
from concept_check_depth_v212 import QID


def main():
    _v211_main()
    source, target = "V211_DEPTH_BACKLOG_AUDIT.json", "V212_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source):
        raise SystemExit("v20.12 backlog gate did not receive v20.11 resolver output")
    with open(source, "r", encoding="utf-8") as f:
        report = json.load(f)
    markers = report.get("discovered_depth_markers") or []
    failures = list(report.get("failures") or [])
    if "task_alignment_v212" not in markers:
        failures.append("missing_dynamic_depth_marker:task_alignment_v212")
    untouched = {str(x.get("id") or "") for x in report.get("candidates") or []}
    residual = {str(x.get("id") or "") for x in report.get("residual_candidates") or []}
    if QID in untouched:
        failures.append("deepened_target_still_in_untouched_queue:" + QID)
    if QID in residual:
        failures.append("deepened_target_still_in_residual_queue:" + QID)
    report["audit_version"] = "v20.12"
    report["failures"] = failures
    with open(target, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"V212_CANONICAL|{report.get('canonical_count')}")
    print(f"V212_DEEPENED_CONCEPTS|{report.get('deepened_concept_count')}")
    print(f"V212_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}")
    print(f"V212_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}")
    print("V212_DISCOVERED_DEPTH_MARKERS|" + ",".join(markers))
    print(f"V212_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
