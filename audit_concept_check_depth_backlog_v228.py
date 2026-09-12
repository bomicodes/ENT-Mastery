"""v20.28 live-canonical Concept Check depth backlog gate."""
import json
import os
from audit_concept_check_depth_backlog_v227 import main as _v227_main
from concept_check_depth_v228 import QIDS


def main():
    _v227_main()
    source, target = "V227_DEPTH_BACKLOG_AUDIT.json", "V228_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source):
        raise SystemExit("v20.28 backlog gate did not receive v20.27 resolver output")
    with open(source, "r", encoding="utf-8") as f:
        report = json.load(f)

    markers = list(report.get("discovered_depth_markers") or [])
    failures = list(report.get("failures") or [])
    if "task_alignment_v228" not in markers:
        markers.append("task_alignment_v228")

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

    canonical = report.get("canonical_count")
    if canonical != 325:
        failures.append("canonical_contract_changed:" + str(canonical))

    report["discovered_depth_markers"] = markers
    report["latest_depth_marker_version"] = max(int(report.get("latest_depth_marker_version") or 0), 228)
    report["audit_version"] = "v20.28"
    report["successor_of"] = "v20.27"
    report["selection_policy"] = "clinically high-yield exact-live resident/board/OR gaps take precedence over noisy lexical rank; exact canonical identity remains fail-closed"
    report["newly_deepened_exact_live"] = list(QIDS)
    report["failures"] = failures

    with open(target, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"V228_CANONICAL|{canonical}")
    print(f"V228_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}")
    print(f"V228_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}")
    print("V228_DISCOVERED_DEPTH_MARKERS|" + ",".join(markers))
    print("V228_TARGETS|" + ",".join(QIDS))
    print("V228_SELECTION_POLICY|" + report["selection_policy"])
    print(f"V228_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: v20.28 preserves the exact live 325-topic canonical backlog contract after Hemostasis / Coagulopathy / Antithrombotic Management in ENT depth")


if __name__ == "__main__":
    main()
