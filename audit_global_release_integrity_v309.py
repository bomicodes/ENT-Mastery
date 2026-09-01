"""Fail-closed global release integrity bridge through current source/rescue gates.

Historical filename remains v30.9 for workflow compatibility. In addition to the
existing chained release-manifest checks, the global release executes the current
phenotype-specific Head & Neck Oncology source-trail gate and the high-consequence
post-tonsillectomy hemorrhage rescue gate. The manifest also verifies that edits to
source-saturation audit families themselves trigger this global release workflow.
"""
from pathlib import Path
from audit_global_release_integrity_v308 import main as _v308_main
from audit_hn_source_saturation_v348 import main as _v348_source_main
from audit_or_tonsil_hemorrhage_rescue_v281 import main as _v281_tonsil_main

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / ".github" / "workflows" / "release-integrity.yml"
GATE = "audit_hn_cutaneous_site_semantic_v309.py"
SOURCE_GATE = "audit_hn_source_saturation_v348.py"
SOURCE_TRIGGER = "audit_*source_saturation_v*.py"
TONSIL_GATE = "audit_or_tonsil_hemorrhage_rescue_v281.py"


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

    print("GLOBAL_RELEASE_HN_CUTANEOUS_SITE_GATE|" + GATE)
    print("GLOBAL_RELEASE_SOURCE_SATURATION_TRIGGER|" + SOURCE_TRIGGER)
    print(f"GLOBAL_RELEASE_V309_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: global release protects the current H&N cSCC-versus-BCC adaptive semantic gate")
    print("PASS: source-saturation audit edits trigger the global fail-closed release workflow")

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


if __name__ == "__main__":
    main()
