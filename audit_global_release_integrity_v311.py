"""Fail-closed global release bridge through the newest Concept Check depth cohort.

Chains the current rescue/source manifest, discovers the highest Concept Check depth,
alignment, and backlog versions present in the repository, requires the final clinical gate
and dedicated workflow to point at that exact cohort, and then executes that cohort's exact
alignment and backlog gates. This keeps release validation fail-closed without requiring a
manual release-workflow stanza for every new depth increment.
"""
import importlib
import re
from pathlib import Path
from audit_global_release_integrity_v310 import main as _v310_main

ROOT = Path(__file__).resolve().parent
RELEASE_WORKFLOW = ROOT / ".github" / "workflows" / "release-integrity.yml"
FINAL_GATE = ROOT / "concept_check_final_clinical_gate_v179.py"

def _versions(pattern):
    out=[]
    for path in ROOT.glob(pattern):
        m=re.search(r"_v(\d+)\.py$",path.name)
        if m: out.append(int(m.group(1)))
    return sorted(out)

def main():
    _v310_main()
    depth=_versions("concept_check_depth_v*.py")
    align=_versions("audit_concept_check_task_alignment_v*.py")
    backlog=_versions("audit_concept_check_depth_backlog_v*.py")
    failures=[]
    if not depth or not align or not backlog:
        failures.append("missing_concept_check_version_family"); latest=None
    else:
        latest=max(depth)
        if max(align)!=latest: failures.append(f"latest_alignment_v{max(align)}_does_not_match_depth_v{latest}")
        if max(backlog)!=latest: failures.append(f"latest_backlog_v{max(backlog)}_does_not_match_depth_v{latest}")
    if latest is not None:
        final_text=FINAL_GATE.read_text(encoding="utf-8")
        release_text=RELEASE_WORKFLOW.read_text(encoding="utf-8")
        for token in (f"from concept_check_depth_v{latest} import apply_concept_check_task_alignment_v{latest}",f'task_alignment_v{latest}'):
            if token not in final_text: failures.append("final_gate_missing:"+token)
        if "python audit_global_release_integrity_v311.py" not in release_text:
            failures.append("release_workflow_missing_dynamic_manifest_call")
        dedicated=ROOT / ".github" / "workflows" / f"concept-check-depth-v{latest}.yml"
        if not dedicated.exists(): failures.append("missing_dedicated_workflow:"+dedicated.name)
    print("GLOBAL_RELEASE_LATEST_CONCEPT_DEPTH|"+(f"v{latest}" if latest is not None else "none"))
    print("GLOBAL_RELEASE_DYNAMIC_CONCEPT_FAILURES|"+str(len(failures)))
    for failure in failures: print("FAIL|"+failure)
    if failures: raise SystemExit(1)
    # Execute, rather than merely name-check, the newest exact-canonical/source and backlog gates.
    alignment_mod=importlib.import_module(f"audit_concept_check_task_alignment_v{latest}")
    backlog_mod=importlib.import_module(f"audit_concept_check_depth_backlog_v{latest}")
    alignment_mod.main(); backlog_mod.main()
    print("PASS: global release dynamically executes and protects the newest Concept Check depth/alignment/backlog cohort")

if __name__ == "__main__": main()
