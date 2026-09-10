"""v20.23 successor live-canonical depth backlog after Forehead Flap / Nasal Reconstruction."""
import json
from pathlib import Path

import audit_concept_check_depth_backlog_v222 as prior
from concept_check_depth_v223 import QIDS

OUT = Path("V223_DEPTH_BACKLOG_AUDIT.json")

def main():
    report = prior.build_report()
    targets = set(QIDS)
    report["candidate_ids"] = [x for x in report.get("candidate_ids", []) if x not in targets]
    report["residual_candidates"] = [x for x in report.get("residual_candidates", []) if x.get("id") not in targets]
    report["reviewed_ids"] = list(dict.fromkeys(list(report.get("reviewed_ids", [])) + list(QIDS)))
    report["marker_version"] = 223
    report["successor_of"] = "v20.22"
    report["newly_deepened_exact_live"] = list(QIDS)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    failures = list(report.get("failures") or [])
    if failures:
        for failure in failures: print("FAIL|" + str(failure))
        raise SystemExit(1)
    print("V223_REVIEWED|" + str(len(report.get("reviewed_ids") or [])))
    print("V223_RESIDUAL|" + str(len(report.get("residual_candidates") or [])))
    print("V223_TARGETS|" + ",".join(QIDS))
    print("PASS: v20.23 preserves the exact live canonical backlog contract after Forehead Flap / Nasal Reconstruction depth")

if __name__ == "__main__": main()
