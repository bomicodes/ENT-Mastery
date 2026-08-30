"""v30.7 fail-closed extension: protect current H&N subsite semantic gates globally."""
from pathlib import Path
from audit_global_release_integrity_v305 import main as _v305_main

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / ".github" / "workflows" / "release-integrity.yml"

REQUIRED_HN_SEMANTIC_GATES = (
    "audit_hn_larynx_site_semantic_v306.py",
    "audit_hn_tongue_site_semantic_v307.py",
)


def main():
    _v305_main()
    text = WORKFLOW.read_text(encoding="utf-8")
    failures = []
    for gate in REQUIRED_HN_SEMANTIC_GATES:
        if gate not in text:
            failures.append("global workflow missing current H&N site semantic gate:" + gate)
    if "audit_*semantic*.py" not in text:
        failures.append("global workflow missing semantic-audit path trigger")

    print("GLOBAL_RELEASE_HN_SITE_SEMANTIC_GATES|" + ",".join(REQUIRED_HN_SEMANTIC_GATES))
    print(f"GLOBAL_RELEASE_V307_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: global release protects current laryngeal-site and tongue-site semantic ladder gates")


if __name__ == "__main__":
    main()
