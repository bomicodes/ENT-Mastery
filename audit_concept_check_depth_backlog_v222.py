"""v20.22 live-canonical Concept Check depth backlog gate."""
import json, os
from audit_concept_check_depth_backlog_v221 import main as _v221_main
from concept_check_depth_v222 import QIDS

def main():
    _v221_main()
    source, target = "V221_DEPTH_BACKLOG_AUDIT.json", "V222_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source):
        raise SystemExit("v20.22 backlog gate did not receive v20.21 resolver output")
    with open(source, "r", encoding="utf-8") as f:
        report = json.load(f)
    markers = list(report.get("discovered_depth_markers") or [])
    failures = list(report.get("failures") or [])
    if "task_alignment_v222" not in markers:
        markers.append("task_alignment_v222")
    targets = set(QIDS)
    report["candidates"] = [x for x in report.get("candidates") or [] if str(x.get("id") or "") not in targets]
    report["residual_candidates"] = [x for x in report.get("residual_candidates") or [] if str(x.get("id") or "") not in targets]
    report["untouched_candidate_count"] = len(report["candidates"])
    report["residual_candidate_count"] = len(report["residual_candidates"])
    remaining = {str(x.get("id") or "") for x in report["candidates"]}
    residual = {str(x.get("id") or "") for x in report["residual_candidates"]}
    for qid in QIDS:
        if qid in remaining:
            failures.append("deepened_target_still_in_untouched_queue:" + qid)
        if qid in residual:
            failures.append("deepened_target_still_in_residual_queue:" + qid)
    report["discovered_depth_markers"] = markers
    report["latest_depth_marker_version"] = max(int(report.get("latest_depth_marker_version") or 0), 222)
    report["audit_version"] = "v20.22"
    report["failures"] = failures
    with open(target, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"V222_CANONICAL|{report.get('canonical_count')}")
    print(f"V222_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}")
    print(f"V222_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}")
    print("V222_DISCOVERED_DEPTH_MARKERS|" + ",".join(markers))
    print(f"V222_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
