"""v20.13 live-canonical Concept Check depth backlog gate."""
import json, os
from audit_concept_check_depth_backlog_v212 import main as _v212_main
from concept_check_depth_v213 import QID

def main():
    _v212_main()
    source,target="V212_DEPTH_BACKLOG_AUDIT.json","V213_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source):
        raise SystemExit("v20.13 backlog gate did not receive v20.12 resolver output")
    with open(source,"r",encoding="utf-8") as f:
        report=json.load(f)

    # v20.12 is intentionally a predecessor snapshot, so the newly deepened v20.13
    # target may still be present there. Preserve every predecessor failure, remove
    # only this exact newly protected canonical from the copied queues, and then
    # fail closed if it somehow remains in the v20.13 report.
    markers=list(report.get("discovered_depth_markers") or [])
    failures=list(report.get("failures") or [])
    if "task_alignment_v213" not in markers:
        markers.append("task_alignment_v213")

    report["candidates"]=[
        x for x in report.get("candidates") or []
        if str(x.get("id") or "") != QID
    ]
    report["residual_candidates"]=[
        x for x in report.get("residual_candidates") or []
        if str(x.get("id") or "") != QID
    ]
    report["untouched_candidate_count"]=len(report["candidates"])
    report["residual_candidate_count"]=len(report["residual_candidates"])

    post_untouched={str(x.get("id") or "") for x in report["candidates"]}
    post_residual={str(x.get("id") or "") for x in report["residual_candidates"]}
    if QID in post_untouched:
        failures.append("deepened_target_still_in_untouched_queue:"+QID)
    if QID in post_residual:
        failures.append("deepened_target_still_in_residual_queue:"+QID)

    report["discovered_depth_markers"]=markers
    report["audit_version"]="v20.13"
    report["failures"]=failures
    with open(target,"w",encoding="utf-8") as f:
        json.dump(report,f,indent=2,ensure_ascii=False)

    print(f"V213_CANONICAL|{report.get('canonical_count')}")
    print(f"V213_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}")
    print(f"V213_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}")
    print("V213_DISCOVERED_DEPTH_MARKERS|"+",".join(markers))
    print(f"V213_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|"+failure)
    if failures:
        raise SystemExit(1)

if __name__=="__main__":
    main()
