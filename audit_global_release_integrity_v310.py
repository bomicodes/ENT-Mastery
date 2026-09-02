"""Fail-closed global release bridge through airway-dilation injury rescue v29.2.

Keeps the historical v30.9 manifest intact, then requires the newest procedure-specific
airway-dilation laceration/rupture rescue gate so production cannot silently lose its
stop, controlled-airway, pleural-emergency, and definitive-repair decisions.
"""
from audit_global_release_integrity_v309 import main as _v309_main
from audit_or_airway_dilation_injury_rescue_v292 import main as _v292_airway_dilation_main

AIRWAY_DILATION_GATE = "audit_or_airway_dilation_injury_rescue_v292.py"


def main():
    _v309_main()
    print("GLOBAL_RELEASE_AIRWAY_DILATION_INJURY_RESCUE_GATE|" + AIRWAY_DILATION_GATE)
    rc = _v292_airway_dilation_main()
    if rc:
        raise SystemExit(rc)
    print("PASS: global release protects airway-dilation stop point, controlled ventilation, pleural emergency rescue and definitive repair escalation")


if __name__ == "__main__":
    main()
