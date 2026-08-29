"""v29.6 fail-closed manifest audit for ENT Mastery's global release gates.

This audit is intentionally architecture-focused. It discovers the newest
Concept Check alignment/backlog audits and newest adversarial OR rescue audit
from the repository, then requires the global release-integrity workflow to
execute those exact files. A future cohort therefore cannot be added under the
existing wildcard trigger and silently escape the release gate.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / ".github" / "workflows" / "release-integrity.yml"

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


def latest(pattern: str, rx: str) -> str:
    rows = []
    compiled = re.compile(rx)
    for path in ROOT.glob(pattern):
        match = compiled.fullmatch(path.name)
        if match:
            rows.append((int(match.group(1)), path.name))
    if not rows:
        raise SystemExit(f"GLOBAL_RELEASE_MANIFEST_FAIL|no files matched {pattern}")
    return max(rows)[1]


def main() -> None:
    if not WORKFLOW.exists():
        raise SystemExit(f"GLOBAL_RELEASE_MANIFEST_FAIL|missing workflow:{WORKFLOW.relative_to(ROOT)}")
    text = WORKFLOW.read_text(encoding="utf-8")

    latest_alignment = latest(
        "audit_concept_check_task_alignment_v*.py",
        r"audit_concept_check_task_alignment_v(\d+)\.py",
    )
    latest_backlog = latest(
        "audit_concept_check_depth_backlog_v*.py",
        r"audit_concept_check_depth_backlog_v(\d+)\.py",
    )
    latest_rescue = latest(
        "audit_or_rescue_v*.py",
        r"audit_or_rescue_v(\d+)\.py",
    )

    required = list(DOMAIN_GATES) + list(CORE_GATES) + [
        latest_alignment,
        latest_backlog,
        latest_rescue,
    ]
    failures = [item for item in required if item not in text]

    # The workflow must remain wired to wildcard triggers so adding a new
    # versioned cohort/rescue file automatically causes this manifest to run.
    trigger_tokens = (
        "audit_concept_check_task_alignment_v*.py",
        "audit_concept_check_depth_backlog_v*.py",
        "audit_or_rescue_v*.py",
        "audit_global_release_integrity_v*.py",
    )
    failures.extend(f"missing trigger:{token}" for token in trigger_tokens if token not in text)

    print(f"GLOBAL_RELEASE_LATEST_ALIGNMENT|{latest_alignment}")
    print(f"GLOBAL_RELEASE_LATEST_BACKLOG|{latest_backlog}")
    print(f"GLOBAL_RELEASE_LATEST_OR_RESCUE|{latest_rescue}")
    print(f"GLOBAL_RELEASE_DOMAIN_GATES|{len(DOMAIN_GATES)}")
    print(f"GLOBAL_RELEASE_FAILURES|{len(failures)}")
    for failure in failures:
        print(f"FAIL|{failure}")
    if failures:
        raise SystemExit(1)
    print("PASS: global release workflow is fail-closed for newest Concept Check cohorts, OR rescue, all nine domain gates, strict canonical coverage, and answer balance")


if __name__ == "__main__":
    main()
