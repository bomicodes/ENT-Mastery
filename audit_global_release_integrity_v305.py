"""v30.5 fail-closed extension: protect the newest shared-airway bailout gate globally."""
from pathlib import Path
import re
from audit_global_release_integrity_v304 import main as _v304_main

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / ".github" / "workflows" / "release-integrity.yml"


def latest_airway_gate():
    rx = re.compile(r"audit_or_airway_bailouts_v(\d+)\.py")
    rows = []
    for path in ROOT.glob("audit_or_airway_bailouts_v*.py"):
        m = rx.fullmatch(path.name)
        if m:
            rows.append((int(m.group(1)), path.name))
    if not rows:
        raise SystemExit("GLOBAL_RELEASE_V305_FAIL|no airway-bailout audit found")
    return max(rows)


def main():
    _v304_main()
    version, gate = latest_airway_gate()
    text = WORKFLOW.read_text(encoding="utf-8")
    failures = []
    if gate not in text:
        failures.append("global workflow missing current airway bailout gate:" + gate)
    if "audit_or_airway_bailouts_v*.py" not in text:
        failures.append("global workflow missing airway-bailout path trigger")
    if "or_airway_bailouts_v*.py" not in text and "or_*.py" not in text:
        failures.append("global workflow missing airway bailout implementation trigger")
    print(f"GLOBAL_RELEASE_LATEST_AIRWAY_BAILOUT|{gate}")
    print(f"GLOBAL_RELEASE_AIRWAY_BAILOUT_VERSION|v{version}")
    print(f"GLOBAL_RELEASE_V305_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: global release additionally protects the current shared-airway exposure and ventilation bailout gate")


if __name__ == "__main__":
    main()
