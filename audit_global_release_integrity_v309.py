"""Fail-closed global release integrity bridge through the v34.8 oncology source gate.

Historical filename remains v30.9 for workflow compatibility. In addition to the
existing chained release-manifest checks, the global release now executes the current
phenotype-specific Head & Neck Oncology source-trail gate so disease-specific source
routing cannot regress while the overall release still appears green.
"""
from pathlib import Path
from audit_global_release_integrity_v308 import main as _v308_main
from audit_hn_source_saturation_v348 import main as _v348_source_main

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / ".github" / "workflows" / "release-integrity.yml"
GATE = "audit_hn_cutaneous_site_semantic_v309.py"
SOURCE_GATE = "audit_hn_source_saturation_v348.py"


def main():
    _v308_main()
    text = WORKFLOW.read_text(encoding="utf-8")
    failures = []
    if GATE not in text:
        failures.append("global workflow missing H&N cutaneous-site semantic gate:" + GATE)
    if "audit_*semantic*.py" not in text:
        failures.append("global workflow missing semantic-audit path trigger")

    print("GLOBAL_RELEASE_HN_CUTANEOUS_SITE_GATE|" + GATE)
    print(f"GLOBAL_RELEASE_V309_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: global release protects the current H&N cSCC-versus-BCC adaptive semantic gate")

    print("GLOBAL_RELEASE_HN_PHENOTYPE_SOURCE_GATE|" + SOURCE_GATE)
    source_rc = _v348_source_main()
    if source_rc:
        raise SystemExit(source_rc)
    print("PASS: global release protects phenotype-specific Head & Neck Oncology source routing")


if __name__ == "__main__":
    main()
