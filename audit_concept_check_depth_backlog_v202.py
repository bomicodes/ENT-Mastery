"""v20.2 live-canonical Concept Check depth backlog gate."""
import json
import os
from audit_concept_check_depth_backlog_v201 import main as _v201_main


def main():
    _v201_main()
    source, target = "V201_DEPTH_BACKLOG_AUDIT.json", "V202_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source):
        raise SystemExit("v20.2 backlog gate did not receive v20.1 resolver output")
    with open(source, "r", encoding="utf-8") as f:
        report = json.load(f)
    markers = report.get("discovered_depth_markers") or []
    failures = list(report.get("failures") or [])
    if "task_alignment_v202" not in markers:
        failures.append("missing_dynamic_depth_marker:task_alignment_v202")

    target_id = "cc-v112-rec-general-ent-emergencies-ludwig-angina"
    untouched_ids = {str(x.get("id") or "") for x in report.get("candidates") or []}
    residual_ids = {str(x.get("id") or "") for x in report.get("residual_candidates") or []}
    if target_id in untouched_ids:
        failures.append("deepened_target_still_in_untouched_queue:" + target_id)
    if target_id in residual_ids:
        failures.append("deepened_target_still_in_residual_queue:" + target_id)

    report["audit_version"] = "v20.2"
    report["failures"] = failures
    with open(target, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"V202_CANONICAL|{report.get('canonical_count')}")
    print(f"V202_DEEPENED_CONCEPTS|{report.get('deepened_concept_count')}")
    print(f"V202_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}")
    print(f"V202_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}")
    print("V202_DISCOVERED_DEPTH_MARKERS|" + ",".join(markers))
    print(f"V202_FAILURES|{len(failures)}")
    for x in failures:
        print("FAIL|" + x)
    if failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
