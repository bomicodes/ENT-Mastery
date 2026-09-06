"""Fail-closed global release bridge through the newest Concept Check depth cohort.

Chains the current rescue/source manifest, requires all live Rhinology source-semantic
gates, then discovers the highest Concept Check depth, alignment, and backlog versions
present in the repository and requires the final clinical gate, dedicated workflow, and
global release workflow to point at that exact same cohort.
"""
import re
from pathlib import Path
from audit_global_release_integrity_v310 import main as _v310_main
from audit_rhinology_allergy_source_semantic_v349 import main as _rhinology_allergy_source_main
from audit_rhinology_crs_inflammatory_source_semantic_v350 import main as _rhinology_crs_source_main
from audit_rhinology_nonallergic_olfaction_source_semantic_v351 import main as _rhinology_nonallergic_olfaction_source_main

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
    print("GLOBAL_RELEASE_RHINOLOGY_ALLERGY_SOURCE_GATE|audit_rhinology_allergy_source_semantic_v349.py")
    rc = _rhinology_allergy_source_main()
    if rc: raise SystemExit(rc)
    print("GLOBAL_RELEASE_RHINOLOGY_CRS_SOURCE_GATE|audit_rhinology_crs_inflammatory_source_semantic_v350.py")
    rc = _rhinology_crs_source_main()
    if rc: raise SystemExit(rc)
    print("GLOBAL_RELEASE_RHINOLOGY_NONALLERGIC_OLFACTION_SOURCE_GATE|audit_rhinology_nonallergic_olfaction_source_semantic_v351.py")
    rc = _rhinology_nonallergic_olfaction_source_main()
    if rc: raise SystemExit(rc)
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
        required_final=[f"from concept_check_depth_v{latest} import apply_concept_check_task_alignment_v{latest}",f'task_alignment_v{latest}']
        for token in required_final:
            if token not in final_text: failures.append("final_gate_missing:"+token)
        required_release=[f"audit_concept_check_task_alignment_v{latest}.py",f"audit_concept_check_depth_backlog_v{latest}.py",f"V{latest}_DEPTH_BACKLOG_AUDIT.json",f"concept-check-depth-backlog-v{latest}"]
        for token in required_release:
            if token not in release_text: failures.append("release_workflow_missing:"+token)
        dedicated=ROOT / ".github" / "workflows" / f"concept-check-depth-v{latest}.yml"
        if not dedicated.exists(): failures.append("missing_dedicated_workflow:"+dedicated.name)
    print("GLOBAL_RELEASE_LATEST_CONCEPT_DEPTH|"+(f"v{latest}" if latest is not None else "none"))
    print("GLOBAL_RELEASE_DYNAMIC_CONCEPT_FAILURES|"+str(len(failures)))
    for failure in failures: print("FAIL|"+failure)
    if failures: raise SystemExit(1)
    print("PASS: global release protects Rhinology Allergy + CRS inflammatory + Nonallergic/Olfaction source contracts and dynamically protects the newest Concept Check depth/alignment/backlog cohort")

if __name__ == "__main__": main()
