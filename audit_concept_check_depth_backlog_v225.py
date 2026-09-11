"""v20.25 live-canonical Concept Check depth backlog gate."""
import json, os
from audit_concept_check_depth_backlog_v224 import main as _v224_main
from concept_check_depth_v225 import QIDS

def main():
    _v224_main()
    source, target = "V224_DEPTH_BACKLOG_AUDIT.json", "V225_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source):
        raise SystemExit("v20.25 backlog gate did not receive v20.24 resolver output")
    with open(source, "r", encoding="utf-8") as f:
        report = json.load(f)
    markers = list(report.get("discovered_depth_markers") or [])
    failures = list(report.get("failures") or [])
    if "task_alignment_v225" not in markers:
        markers.append("task_alignment_v225")
    targets = set(QIDS)
    before_u = {str(x.get("id") or "") for x in report.get("candidates") or []}
    before_r = {str(x.get("id") or "") for x in report.get("residual_candidates") or []}
    for qid in QIDS:
        if qid not in before_u and qid not in before_r:
            failures.append("target_not_in_inherited_live_backlog:" + qid)
    report["candidates"] = [x for x in report.get("candidates") or [] if str(x.get("id") or "") not in targets]
    report["residual_candidates"] = [x for x in report.get("residual_candidates") or [] if str(x.get("id") or "") not in targets]
    report["untouched_candidate_count"] = len(report["candidates"])
    report["residual_candidate_count"] = len(report["residual_candidates"])
    remaining = {str(x.get("id") or "") for x in report["candidates"]}
    residual = {str(x.get("id") or "") for x in report["residual_candidates"]}
    for qid in QIDS:
        if qid in remaining: failures.append("deepened_target_still_in_untouched_queue:" + qid)
        if qid in residual: failures.append("deepened_target_still_in_residual_queue:" + qid)
    canonical = report.get("canonical_count")
    if canonical != 325:
        failures.append("canonical_contract_changed:" + str(canonical))
    report["discovered_depth_markers"] = markers
    report["latest_depth_marker_version"] = max(int(report.get("latest_depth_marker_version") or 0), 225)
    report["audit_version"] = "v20.25"
    report["successor_of"] = "v20.24"
    report["newly_deepened_exact_live"] = list(QIDS)
    report["failures"] = failures
    with open(target, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"V225_CANONICAL|{canonical}")
    print(f"V225_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}")
    print(f"V225_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}")
    print("V225_DISCOVERED_DEPTH_MARKERS|" + ",".join(markers))
    print("V225_TARGETS|" + ",".join(QIDS))
    print(f"V225_FAILURES|{len(failures)}")
    for failure in failures: print("FAIL|" + failure)
    if failures: raise SystemExit(1)
    print("PASS: v20.25 preserves the exact live 325-topic canonical backlog contract after TLM laryngeal-cancer depth")

if __name__ == "__main__":
    main()
