"""v30.9 fail-closed extension: protect the H&N cSCC-vs-BCC adaptive semantic gate globally."""
from pathlib import Path
from audit_global_release_integrity_v308 import main as _v308_main

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / ".github" / "workflows" / "release-integrity.yml"
GATE = "audit_hn_cutaneous_site_semantic_v309.py"


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


if __name__ == "__main__":
    main()
