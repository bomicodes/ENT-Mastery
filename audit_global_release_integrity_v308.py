"""v30.8 fail-closed extension: protect the cross-domain late-radiation aspiration gate globally."""
from pathlib import Path
from audit_global_release_integrity_v307 import main as _v307_main

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / ".github" / "workflows" / "release-integrity.yml"
GATE = "audit_cross_domain_aspiration_semantic_v308.py"


def main():
    _v307_main()
    text = WORKFLOW.read_text(encoding="utf-8")
    failures = []
    if GATE not in text:
        failures.append("global workflow missing cross-domain aspiration semantic gate:" + GATE)
    if "audit_*semantic*.py" not in text:
        failures.append("global workflow missing semantic-audit path trigger")

    print("GLOBAL_RELEASE_CROSS_DOMAIN_ASPIRATION_GATE|" + GATE)
    print(f"GLOBAL_RELEASE_V308_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: global release protects the current cross-domain late-radiation aspiration semantic gate")


if __name__ == "__main__":
    main()
