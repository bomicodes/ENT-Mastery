"""v19.7 live-canonical Concept Check depth backlog gate.

Reuse the mature v19.6 resolver/priority contract while requiring the exact HNSCC
immunotherapy repair to leave both short-answer queues. Dynamic marker discovery
continues to prevent later depth cohorts from being invisible to backlog accounting.
"""
import json, os
from audit_concept_check_depth_backlog_v196 import main as _v196_main

def main():
    _v196_main()
    source = "V196_DEPTH_BACKLOG_AUDIT.json"
    target = "V197_DEPTH_BACKLOG_AUDIT.json"
    if not os.path.exists(source):
        raise SystemExit("v19.7 backlog gate did not receive v19.6 resolver output")
    with open(source, "r", encoding="utf-8") as f:
        report = json.load(f)
    markers = report.get("discovered_depth_markers") or []
    failures = list(report.get("failures") or [])
    if "task_alignment_v197" not in markers:
        failures.append("missing_dynamic_depth_marker:task_alignment_v197")
    target_id = "cc-v112-rec-head-neck-oncology-tumor-immunology-immunotherapy-in-hnscc"
    untouched_ids = {str(x.get("id") or "") for x in report.get("candidates") or []}
    residual_ids = {str(x.get("id") or "") for x in report.get("residual_candidates") or []}
    if target_id in untouched_ids:
        failures.append("deepened_target_still_in_untouched_queue:" + target_id)
    if target_id in residual_ids:
        failures.append("deepened_target_still_in_residual_queue:" + target_id)
    report["audit_version"] = "v19.7"
    report["failures"] = failures
    with open(target, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"V197_CANONICAL|{report.get('canonical_count')}")
    print(f"V197_DEEPENED_CONCEPTS|{report.get('deepened_concept_count')}")
    print(f"V197_UNTOUCHED_UNDER_75_WORDS|{report.get('untouched_candidate_count')}")
    print(f"V197_RESIDUAL_UNDER_75_WORDS|{report.get('residual_candidate_count')}")
    print("V197_DISCOVERED_DEPTH_MARKERS|" + ",".join(markers))
    print(f"V197_FAILURES|{len(failures)}")
    for x in failures: print("FAIL|" + x)
    if failures: raise SystemExit(1)

if __name__ == "__main__": main()
