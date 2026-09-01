"""Fail-closed global release integrity bridge through current source/rescue gates.

Historical filename remains v30.9 for workflow compatibility. In addition to the
existing chained release-manifest checks, the global release executes the current
phenotype-specific Head & Neck Oncology source-trail gate and the high-consequence
post-tonsillectomy hemorrhage, post-thyroidectomy hematoma, and tracheostomy
hemorrhage/TIF rescue gates. The manifest also verifies that edits to source-saturation
audit families themselves trigger this global release workflow and that the newest
validated Concept Check alignment/backlog cohort cannot be silently omitted from
release validation.
"""
from pathlib import Path
from audit_global_release_integrity_v308 import main as _v308_main
from audit_hn_source_saturation_v348 import main as _v348_source_main
from audit_or_tonsil_hemorrhage_rescue_v281 import main as _v281_tonsil_main
from audit_or_thyroid_hematoma_rescue_v282 import main as _v282_thyroid_main
from audit_or_tracheostomy_hemorrhage_rescue_v283 import main as _v283_trach_main

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / ".github" / "workflows" / "release-integrity.yml"
GATE = "audit_hn_cutaneous_site_semantic_v309.py"
SOURCE_GATE = "audit_hn_source_saturation_v348.py"
SOURCE_TRIGGER = "audit_*source_saturation_v*.py"
TONSIL_GATE = "audit_or_tonsil_hemorrhage_rescue_v281.py"
THYROID_GATE = "audit_or_thyroid_hematoma_rescue_v282.py"
TRACHEOSTOMY_GATE = "audit_or_tracheostomy_hemorrhage_rescue_v283.py"
CONCEPT_ALIGNMENT_GATE = "audit_concept_check_task_alignment_v203.py"
CONCEPT_BACKLOG_GATE = "audit_concept_check_depth_backlog_v203.py"


def main():
    _v308_main()
    text = WORKFLOW.read_text(encoding="utf-8")
    failures = []
    if GATE not in text:
        failures.append("global workflow missing H&N cutaneous-site semantic gate:" + GATE)
    if "audit_*semantic*.py" not in text:
        failures.append("global workflow missing semantic-audit path trigger")
    if SOURCE_TRIGGER not in text:
        failures.append("global workflow missing source-saturation audit path trigger:" + SOURCE_TRIGGER)
    if "audit_or_rescue_v*.py" not in text and "or_*.py" not in text:
        failures.append("global workflow missing OR rescue path trigger")
    if CONCEPT_ALIGNMENT_GATE not in text:
        failures.append("global workflow missing newest Concept Check alignment gate:" + CONCEPT_ALIGNMENT_GATE)
    if CONCEPT_BACKLOG_GATE not in text:
        failures.append("global workflow missing newest Concept Check backlog gate:" + CONCEPT_BACKLOG_GATE)

    print("GLOBAL_RELEASE_HN_CUTANEOUS_SITE_GATE|" + GATE)
    print("GLOBAL_RELEASE_SOURCE_SATURATION_TRIGGER|" + SOURCE_TRIGGER)
    print("GLOBAL_RELEASE_CONCEPT_ALIGNMENT_GATE|" + CONCEPT_ALIGNMENT_GATE)
    print("GLOBAL_RELEASE_CONCEPT_BACKLOG_GATE|" + CONCEPT_BACKLOG_GATE)
    print(f"GLOBAL_RELEASE_V309_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: global release protects the current H&N cSCC-versus-BCC adaptive semantic gate")
    print("PASS: source-saturation audit edits trigger the global fail-closed release workflow")
    print("PASS: global release cannot silently omit the newest Concept Check depth cohort")

    print("GLOBAL_RELEASE_HN_PHENOTYPE_SOURCE_GATE|" + SOURCE_GATE)
    source_rc = _v348_source_main()
    if source_rc:
        raise SystemExit(source_rc)
    print("PASS: global release protects phenotype-specific Head & Neck Oncology source routing")

    print("GLOBAL_RELEASE_TONSIL_HEMORRHAGE_RESCUE_GATE|" + TONSIL_GATE)
    tonsil_rc = _v281_tonsil_main()
    if tonsil_rc:
        raise SystemExit(tonsil_rc)
    print("PASS: global release protects post-tonsillectomy hemorrhage rescue choreography")

    print("GLOBAL_RELEASE_THYROID_HEMATOMA_RESCUE_GATE|" + THYROID_GATE)
    thyroid_rc = _v282_thyroid_main()
    if thyroid_rc:
        raise SystemExit(thyroid_rc)
    print("PASS: global release protects post-thyroidectomy hematoma airway rescue choreography")

    print("GLOBAL_RELEASE_TRACHEOSTOMY_HEMORRHAGE_RESCUE_GATE|" + TRACHEOSTOMY_GATE)
    trach_rc = _v283_trach_main()
    if trach_rc:
        raise SystemExit(trach_rc)
    print("PASS: global release protects tracheostomy hemorrhage/TIF rescue choreography")


if __name__ == "__main__":
    main()
