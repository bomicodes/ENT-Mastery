"""v19.4 live-canonical Concept Check depth backlog gate.

Reuse the mature v19.3 resolver/priority contract. That contract discovers every
truthy task_alignment_vN marker with N>=180 dynamically, so after the v19.4
runtime cohort is applied the two newly deepened canonical concepts leave the
untouched queue without weakening canonical resolution or clinical-priority
override behavior.
"""
import json, os
from audit_concept_check_depth_backlog_v193 import main as _v193_main


def main():
    _v193_main()
    source="V193_DEPTH_BACKLOG_AUDIT.json"
    target="V194_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source):
        raise SystemExit("v19.4 backlog gate did not receive v19.3 resolver output")
    with open(source,"r",encoding="utf-8") as f:
        report=json.load(f)
    markers=report.get("discovered_depth_markers") or []
    failures=list(report.get("failures") or [])
    if "task_alignment_v194" not in markers:
        failures.append("missing_dynamic_depth_marker:task_alignment_v194")
    report["audit_version"]="v19.4"
    report["failures"]=failures
    with open(target,"w",encoding="utf-8") as f:
        json.dump(report,f,indent=2,ensure_ascii=False)
    print(f"V194_CANONICAL|{report.get('canonical_count')}")
    print(f"V194_DEEPENED_CONCEPTS|{report.get('deepened_concept_count')}")
    print(f"V194_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}")
    print(f"V194_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}")
    print("V194_DISCOVERED_DEPTH_MARKERS|"+",".join(markers))
    print(f"V194_FAILURES|{len(failures)}")
    for x in failures: print("FAIL|"+x)
    if failures: raise SystemExit(1)


if __name__=="__main__": main()
