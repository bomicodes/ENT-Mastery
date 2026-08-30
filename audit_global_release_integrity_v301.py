"""v30.1 fail-closed manifest audit for ENT Mastery's global release gates.

Extends the v29.7 manifest contract so the global release workflow must execute
both the newest adversarial OR rescue gate and the newest OR commitment/bailout
gate. This prevents a release from retaining complication recognition while
silently losing the explicit stop/reassess/convert/sacrifice decisions required
in high-risk operations.
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

    failures = []
    required = list(DOMAIN_GATES) + list(CORE_GATES) + [
        latest_alignment,
        latest_backlog,
        latest_rescue,
        latest_commitment,
    ]
    failures.extend(item for item in required if item not in workflow_text)

    # The depth cohort and its hard gate advance as a matched release unit.
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
    print(f"GLOBAL_RELEASE_FAILURES|{len(failures)}")
    for failure in failures:
        print(f"FAIL|{failure}")
    if failures:
        raise SystemExit(1)
    print(
        "PASS: global release workflow is fail-closed for the newest applied-and-audited "
        "Concept Check depth cohort, current backlog, OR rescue, OR commitment/bailout, "
        "all nine domain gates, strict canonical coverage, and answer balance"
    )


if __name__ == "__main__":
    main()
