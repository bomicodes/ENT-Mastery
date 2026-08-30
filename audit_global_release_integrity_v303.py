"""v30.3 fail-closed manifest audit for ENT Mastery's global release gates.

Extends the v30.1 release contract so clinically focused semantic/depth gates are
part of the global release path, not only their domain-specific workflows. This
prevents a broad domain ladder gate from staying green while a deliberately
reviewed distinction (for example NOE mechanics, frontal-sinus outflow,
AR-vs-LAR, pediatric ear decisions, neck-dissection complications, salvage, or
pediatric PSG management) silently regresses.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / ".github" / "workflows" / "release-integrity.yml"
FINAL_GATE = ROOT / "concept_check_final_clinical_gate_v179.py"

DOMAIN_GATES = (
    "audit_rhinology_ladder_complete_v218.py",
    "audit_otology_ladder_complete_v232.py",
    "audit_hn_ladder_complete_v231.py",
    "audit_tps_ladder_complete_v240.py",
    "audit_pediatric_ladder_complete_v248.py",
    "audit_laryngology_ladder_complete_v256.py",
    "audit_facial_plastics_full_domain_v262.py",
    "audit_sleep_surgery_progress_v266.py",
    "audit_general_ent_complete_v274.py",
)
CORE_GATES = (
    "audit_coverage_v135.py --depth --strict",
    "audit_ladder_answer_balance_v211.py",
)
SEMANTIC_FAMILIES = (
    ("audit_pediatric_ear_semantic_v*.py", r"audit_pediatric_ear_semantic_v(\d+)\.py"),
    ("audit_hn_salvage_ladder_distinction_v*.py", r"audit_hn_salvage_ladder_distinction_v(\d+)\.py"),
    ("audit_hn_neck_semantic_v*.py", r"audit_hn_neck_semantic_v(\d+)\.py"),
    ("audit_facial_frontal_sinus_management_v*.py", r"audit_facial_frontal_sinus_management_v(\d+)\.py"),
    ("audit_facial_noe_management_v*.py", r"audit_facial_noe_management_v(\d+)\.py"),
    ("audit_rhinology_rhinitis_semantic_v*.py", r"audit_rhinology_rhinitis_semantic_v(\d+)\.py"),
    ("audit_sleep_peds_psg_management_v*.py", r"audit_sleep_peds_psg_management_v(\d+)\.py"),
    ("audit_facial_deep_semantic_boundaries_v*.py", r"audit_facial_deep_semantic_boundaries_v(\d+)\.py"),
)


def latest(pattern: str, rx: str):
    rows = []
    compiled = re.compile(rx)
    for path in ROOT.glob(pattern):
        match = compiled.fullmatch(path.name)
        if match:
            rows.append((int(match.group(1)), path.name))
    if not rows:
        raise SystemExit(f"GLOBAL_RELEASE_MANIFEST_FAIL|no files matched {pattern}")
    return max(rows)


def main() -> None:
    if not WORKFLOW.exists():
        raise SystemExit(f"GLOBAL_RELEASE_MANIFEST_FAIL|missing workflow:{WORKFLOW.relative_to(ROOT)}")
    if not FINAL_GATE.exists():
        raise SystemExit(f"GLOBAL_RELEASE_MANIFEST_FAIL|missing final gate:{FINAL_GATE.relative_to(ROOT)}")

    workflow_text = WORKFLOW.read_text(encoding="utf-8")
    final_gate_text = FINAL_GATE.read_text(encoding="utf-8")

    alignment_version, latest_alignment = latest(
        "audit_concept_check_task_alignment_v*.py",
        r"audit_concept_check_task_alignment_v(\d+)\.py",
    )
    backlog_version, latest_backlog = latest(
        "audit_concept_check_depth_backlog_v*.py",
        r"audit_concept_check_depth_backlog_v(\d+)\.py",
    )
    depth_version, latest_depth = latest(
        "concept_check_depth_v*.py",
        r"concept_check_depth_v(\d+)\.py",
    )
    rescue_version, latest_rescue = latest(
        "audit_or_rescue_v*.py",
        r"audit_or_rescue_v(\d+)\.py",
    )
    commitment_version, latest_commitment = latest(
        "audit_or_commitment_v*.py",
        r"audit_or_commitment_v(\d+)\.py",
    )
    semantic_gates = [latest(pattern, rx)[1] for pattern, rx in SEMANTIC_FAMILIES]

    failures = []
    required = list(DOMAIN_GATES) + list(CORE_GATES) + semantic_gates + [
        latest_alignment,
        latest_backlog,
        latest_rescue,
        latest_commitment,
    ]
    failures.extend(item for item in required if item not in workflow_text)

    if depth_version != alignment_version:
        failures.append(
            f"depth_alignment_version_mismatch:depth=v{depth_version}:alignment=v{alignment_version}"
        )
    if backlog_version < depth_version:
        failures.append(
            f"stale_backlog_version:backlog=v{backlog_version}:depth=v{depth_version}"
        )

    alignment_text = (ROOT / latest_alignment).read_text(encoding="utf-8")
    depth_module = Path(latest_depth).stem
    expected_alignment_import = f"from {depth_module} import COHORT"
    if expected_alignment_import not in alignment_text:
        failures.append(
            f"latest_alignment_does_not_import_latest_depth:{latest_alignment}:{latest_depth}"
        )

    apply_name = f"apply_concept_check_task_alignment_v{depth_version}"
    expected_final_import = f"from {depth_module} import {apply_name}"
    if expected_final_import not in final_gate_text:
        failures.append(f"final_gate_missing_latest_depth_import:{expected_final_import}")
    if f"{apply_name}(checks, deep_modules, v6_item_id)" not in final_gate_text:
        failures.append(f"final_gate_missing_latest_depth_apply:{apply_name}")
    if f'"task_alignment_v{depth_version}"' not in final_gate_text:
        failures.append(f"final_gate_missing_latest_depth_result:task_alignment_v{depth_version}")

    trigger_tokens = (
        "audit_concept_check_task_alignment_v*.py",
        "audit_concept_check_depth_backlog_v*.py",
        "concept_check_depth_v*.py",
        "concept_check_final_clinical_gate_v179.py",
        "audit_or_rescue_v*.py",
        "audit_or_commitment_v*.py",
        "audit_global_release_integrity_v*.py",
        "audit_*semantic*.py",
        "audit_*management_v*.py",
        "audit_*ladder_distinction_v*.py",
    )
    failures.extend(
        f"missing trigger:{token}" for token in trigger_tokens if token not in workflow_text
    )

    print(f"GLOBAL_RELEASE_LATEST_DEPTH|{latest_depth}")
    print(f"GLOBAL_RELEASE_LATEST_ALIGNMENT|{latest_alignment}")
    print(f"GLOBAL_RELEASE_LATEST_BACKLOG|{latest_backlog}")
    print(f"GLOBAL_RELEASE_LATEST_OR_RESCUE|{latest_rescue}")
    print(f"GLOBAL_RELEASE_LATEST_OR_COMMITMENT|{latest_commitment}")
    print(f"GLOBAL_RELEASE_OR_COMMITMENT_VERSION|v{commitment_version}")
    print(f"GLOBAL_RELEASE_DOMAIN_GATES|{len(DOMAIN_GATES)}")
    print(f"GLOBAL_RELEASE_SEMANTIC_GATES|{len(semantic_gates)}")
    for gate in semantic_gates:
        print(f"GLOBAL_RELEASE_SEMANTIC_GATE|{gate}")
    print(f"GLOBAL_RELEASE_FAILURES|{len(failures)}")
    for failure in failures:
        print(f"FAIL|{failure}")
    if failures:
        raise SystemExit(1)
    print(
        "PASS: global release workflow is fail-closed for the newest applied-and-audited "
        "Concept Check cohort, current backlog, OR rescue/commitment, all nine domain gates, "
        "focused semantic gates, strict canonical coverage, and answer balance"
    )


if __name__ == "__main__":
    main()
