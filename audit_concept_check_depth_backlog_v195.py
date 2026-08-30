"""v19.5 live-canonical Concept Check depth backlog gate.

Reuse the mature v19.4 resolver/priority contract. The inherited resolver discovers
truthy task_alignment_vN markers dynamically, so the newly deepened exact canonical
head-and-neck concept must leave the untouched queue without weakening canonical
resolution or the clinical-priority override contract.
"""
import json, os
from audit_concept_check_depth_backlog_v194 import main as _v194_main

def main():
    _v194_main()
    source="V194_DEPTH_BACKLOG_AUDIT.json"
    target="V195_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source):
        raise SystemExit("v19.5 backlog gate did not receive v19.4 resolver output")
    with open(source,"r",encoding="utf-8") as f:
        report=json.load(f)
    markers=report.get("discovered_depth_markers") or []
    failures=list(report.get("failures") or [])
    if "task_alignment_v195" not in markers:
        failures.append("missing_dynamic_depth_marker:task_alignment_v195")
    target_id="cc-v112-rec-head-neck-oncology-adverse-pathology-and-adjuvant-therapy"
    untouched_ids={str(x.get("id") or "") for x in report.get("candidates") or []}
    residual_ids={str(x.get("id") or "") for x in report.get("residual_candidates") or []}
    if target_id in untouched_ids:
        failures.append("deepened_target_still_in_untouched_queue:"+target_id)
    if target_id in residual_ids:
        failures.append("deepened_target_still_in_residual_queue:"+target_id)
    report["audit_version"]="v19.5"
    report["failures"]=failures
    with open(target,"w",encoding="utf-8") as f:
        json.dump(report,f,indent=2,ensure_ascii=False)
    print(f"V195_CANONICAL|{report.get('canonical_count')}")
    print(f"V195_DEEPENED_CONCEPTS|{report.get('deepened_concept_count')}")
    print(f"V195_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}")
    print(f"V195_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}")
    print("V195_DISCOVERED_DEPTH_MARKERS|"+",".join(markers))
    print(f"V195_FAILURES|{len(failures)}")
    for x in failures: print("FAIL|"+x)
    if failures: raise SystemExit(1)

if __name__=="__main__": main()
