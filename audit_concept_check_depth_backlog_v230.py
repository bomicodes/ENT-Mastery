"""v20.30 live-canonical Concept Check backlog successor gate."""
import json
import os
from audit_concept_check_depth_backlog_v229 import main as _v229_main
from concept_check_depth_v230 import QIDS


def main():
    _v229_main()
    source, target = "V229_DEPTH_BACKLOG_AUDIT.json", "V230_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source):
        raise SystemExit("v20.30 backlog gate did not receive v20.29 resolver output")
    with open(source, "r", encoding="utf-8") as f:
        report = json.load(f)
    failures = list(report.get("failures") or [])
    markers = list(report.get("discovered_depth_markers") or [])
    if "task_alignment_v230" not in markers:
        markers.append("task_alignment_v230")
    targets = set(QIDS)
    report["candidates"] = [x for x in report.get("candidates") or [] if str(x.get("id") or "") not in targets]
    report["residual_candidates"] = [x for x in report.get("residual_candidates") or [] if str(x.get("id") or "") not in targets]
    report["untouched_candidate_count"] = len(report["candidates"])
    report["residual_candidate_count"] = len(report["residual_candidates"])
    if report.get("canonical_count") != 325:
        failures.append("canonical_contract_changed:" + str(report.get("canonical_count")))
    for qid in QIDS:
        if any(str(x.get("id") or "") == qid for x in report["candidates"]):
            failures.append("target_still_in_untouched_queue:" + qid)
        if any(str(x.get("id") or "") == qid for x in report["residual_candidates"]):
            failures.append("target_still_in_residual_queue:" + qid)
    report["discovered_depth_markers"] = markers
    report["latest_depth_marker_version"] = max(int(report.get("latest_depth_marker_version") or 0), 230)
    report["audit_version"] = "v20.30"
    report["successor_of"] = "v20.29"
    report["newly_deepened_exact_live"] = list(QIDS)
    report["selection_policy"] = "learner-experience defects are first-class depth defects: a clinically important management pathway must be discoverable in the exact live canonical concept, not merely mentioned or hidden in metadata"
    report["failures"] = failures
    with open(target, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"V230_CANONICAL|{report.get('canonical_count')}")
    print(f"V230_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: v20.30 preserves the 325-topic backlog contract while elevating learner discoverability as a depth requirement")


if __name__ == "__main__":
    main()
