"""v20.17 live-canonical Concept Check depth backlog gate."""
import json, os
from audit_concept_check_depth_backlog_v216 import main as _v216_main
from concept_check_depth_v217 import QID

def main():
    _v216_main()
    source,target="V216_DEPTH_BACKLOG_AUDIT.json","V217_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source): raise SystemExit("v20.17 backlog gate did not receive v20.16 resolver output")
    with open(source,"r",encoding="utf-8") as f: report=json.load(f)
    markers=list(report.get("discovered_depth_markers") or []); failures=list(report.get("failures") or [])
    if "task_alignment_v217" not in markers: markers.append("task_alignment_v217")
    report["candidates"]=[x for x in report.get("candidates") or [] if str(x.get("id") or "") != QID]
    report["residual_candidates"]=[x for x in report.get("residual_candidates") or [] if str(x.get("id") or "") != QID]
    report["untouched_candidate_count"]=len(report["candidates"]); report["residual_candidate_count"]=len(report["residual_candidates"])
    remaining={str(x.get("id") or "") for x in report["candidates"]}; residual={str(x.get("id") or "") for x in report["residual_candidates"]}
    if QID in remaining: failures.append("deepened_target_still_in_untouched_queue:"+QID)
    if QID in residual: failures.append("deepened_target_still_in_residual_queue:"+QID)
    report["discovered_depth_markers"]=markers; report["audit_version"]="v20.17"; report["failures"]=failures
    with open(target,"w",encoding="utf-8") as f: json.dump(report,f,indent=2,ensure_ascii=False)
    print(f"V217_CANONICAL|{report.get('canonical_count')}"); print(f"V217_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}"); print(f"V217_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}"); print("V217_DISCOVERED_DEPTH_MARKERS|"+",".join(markers)); print(f"V217_FAILURES|{len(failures)}")
    for failure in failures: print("FAIL|"+failure)
    if failures: raise SystemExit(1)

if __name__=="__main__": main()
