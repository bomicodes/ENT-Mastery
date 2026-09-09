"""v20.20 live-canonical Concept Check depth backlog gate."""
import json, os
from audit_concept_check_depth_backlog_v219 import main as _v219_main
from concept_check_depth_v220 import QIDS

def main():
    _v219_main()
    source,target="V219_DEPTH_BACKLOG_AUDIT.json","V220_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source): raise SystemExit("v20.20 backlog gate did not receive v20.19 resolver output")
    with open(source,"r",encoding="utf-8") as f: report=json.load(f)
    markers=list(report.get("discovered_depth_markers") or []); failures=list(report.get("failures") or [])
    if "task_alignment_v220" not in markers: markers.append("task_alignment_v220")
    targets=set(QIDS)
    report["candidates"]=[x for x in report.get("candidates") or [] if str(x.get("id") or "") not in targets]
    report["residual_candidates"]=[x for x in report.get("residual_candidates") or [] if str(x.get("id") or "") not in targets]
    report["untouched_candidate_count"]=len(report["candidates"]); report["residual_candidate_count"]=len(report["residual_candidates"])
    remaining={str(x.get("id") or "") for x in report["candidates"]}; residual={str(x.get("id") or "") for x in report["residual_candidates"]}
    for qid in QIDS:
        if qid in remaining: failures.append("deepened_target_still_in_untouched_queue:"+qid)
        if qid in residual: failures.append("deepened_target_still_in_residual_queue:"+qid)
    report["discovered_depth_markers"]=markers; report["audit_version"]="v20.20"; report["failures"]=failures
    with open(target,"w",encoding="utf-8") as f: json.dump(report,f,indent=2,ensure_ascii=False)
    print(f"V220_CANONICAL|{report.get('canonical_count')}"); print(f"V220_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}"); print(f"V220_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}"); print("V220_DISCOVERED_DEPTH_MARKERS|"+",".join(markers)); print(f"V220_FAILURES|{len(failures)}")
    for failure in failures: print("FAIL|"+failure)
    if failures: raise SystemExit(1)

if __name__=="__main__": main()
