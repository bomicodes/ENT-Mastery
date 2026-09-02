"""Fail-closed global release integrity bridge through current source/rescue gates.

Historical filename remains v30.9 for workflow compatibility. In addition to the
existing chained release-manifest checks, the global release executes the current
phenotype-specific Head & Neck Oncology source-trail gate and the high-consequence
post-tonsillectomy hemorrhage, post-thyroidectomy hematoma, tracheostomy
hemorrhage/TIF, post-septoplasty septal hematoma/abscess, post-esophagoscopy
esophageal-perforation, post-laryngectomy pharyngocutaneous-fistula, shared-airway
fire, posterior-epistaxis/SPA, and TEP prosthesis-displacement/aspiration rescue gates.
The manifest also verifies that edits to source-saturation and OR rescue audit families
themselves trigger this global release workflow and that the newest validated Concept
Check alignment/backlog cohort cannot be silently omitted from release validation.
"""
from pathlib import Path
from audit_global_release_integrity_v308 import main as _v308_main
from audit_hn_source_saturation_v348 import main as _v348_source_main
from audit_or_tonsil_hemorrhage_rescue_v281 import main as _v281_tonsil_main
from audit_or_thyroid_hematoma_rescue_v282 import main as _v282_thyroid_main
from audit_or_tracheostomy_hemorrhage_rescue_v283 import main as _v283_trach_main
from audit_or_septal_hematoma_rescue_v284 import main as _v284_septal_main
from audit_or_esophageal_perforation_rescue_v285 import main as _v285_esophageal_main
from audit_or_laryngectomy_fistula_rescue_v287 import main as _v287_laryngectomy_main
from audit_or_airway_fire_rescue_v288 import main as _v288_airway_fire_main
from audit_or_posterior_epistaxis_rescue_v289 import main as _v289_epistaxis_main
from audit_or_tep_prosthesis_rescue_v290 import main as _v290_tep_main

ROOT = Path(__file__).resolve().parent
WORKFLOW = ROOT / ".github" / "workflows" / "release-integrity.yml"
GATE = "audit_hn_cutaneous_site_semantic_v309.py"
SOURCE_GATE = "audit_hn_source_saturation_v348.py"
SOURCE_TRIGGER = "audit_*source_saturation_v*.py"
OR_RESCUE_TRIGGER = "audit_or_*rescue_v*.py"
TONSIL_GATE = "audit_or_tonsil_hemorrhage_rescue_v281.py"
THYROID_GATE = "audit_or_thyroid_hematoma_rescue_v282.py"
TRACHEOSTOMY_GATE = "audit_or_tracheostomy_hemorrhage_rescue_v283.py"
SEPTAL_GATE = "audit_or_septal_hematoma_rescue_v284.py"
ESOPHAGEAL_GATE = "audit_or_esophageal_perforation_rescue_v285.py"
LARYNGECTOMY_GATE = "audit_or_laryngectomy_fistula_rescue_v287.py"
AIRWAY_FIRE_GATE = "audit_or_airway_fire_rescue_v288.py"
EPISTAXIS_GATE = "audit_or_posterior_epistaxis_rescue_v289.py"
TEP_GATE = "audit_or_tep_prosthesis_rescue_v290.py"
CONCEPT_ALIGNMENT_GATE = "audit_concept_check_task_alignment_v204.py"
CONCEPT_BACKLOG_GATE = "audit_concept_check_depth_backlog_v204.py"


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
    if OR_RESCUE_TRIGGER not in text:
        failures.append("global workflow missing generic OR rescue audit path trigger:" + OR_RESCUE_TRIGGER)
    if CONCEPT_ALIGNMENT_GATE not in text:
        failures.append("global workflow missing newest Concept Check alignment gate:" + CONCEPT_ALIGNMENT_GATE)
    if CONCEPT_BACKLOG_GATE not in text:
        failures.append("global workflow missing newest Concept Check backlog gate:" + CONCEPT_BACKLOG_GATE)

    print("GLOBAL_RELEASE_HN_CUTANEOUS_SITE_GATE|" + GATE)
    print("GLOBAL_RELEASE_SOURCE_SATURATION_TRIGGER|" + SOURCE_TRIGGER)
    print("GLOBAL_RELEASE_OR_RESCUE_TRIGGER|" + OR_RESCUE_TRIGGER)
    print("GLOBAL_RELEASE_CONCEPT_ALIGNMENT_GATE|" + CONCEPT_ALIGNMENT_GATE)
    print("GLOBAL_RELEASE_CONCEPT_BACKLOG_GATE|" + CONCEPT_BACKLOG_GATE)
    print(f"GLOBAL_RELEASE_V309_FAILURES|{len(failures)}")
    for failure in failures:
        print("FAIL|" + failure)
    if failures:
        raise SystemExit(1)
    print("PASS: global release protects the current H&N cSCC-versus-BCC adaptive semantic gate")
    print("PASS: source-saturation audit edits trigger the global fail-closed release workflow")
    print("PASS: OR rescue audit edits trigger the global fail-closed release workflow")
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

    print("GLOBAL_RELEASE_SEPTAL_HEMATOMA_RESCUE_GATE|" + SEPTAL_GATE)
    septal_rc = _v284_septal_main()
    if septal_rc:
        raise SystemExit(septal_rc)
    print("PASS: global release protects post-septoplasty septal hematoma/abscess rescue choreography")

    print("GLOBAL_RELEASE_ESOPHAGEAL_PERFORATION_RESCUE_GATE|" + ESOPHAGEAL_GATE)
    esophageal_rc = _v285_esophageal_main()
    if esophageal_rc:
        raise SystemExit(esophageal_rc)
    print("PASS: global release protects post-esophagoscopy cervical esophageal perforation rescue choreography")

    print("GLOBAL_RELEASE_LARYNGECTOMY_FISTULA_RESCUE_GATE|" + LARYNGECTOMY_GATE)
    laryngectomy_rc = _v287_laryngectomy_main()
    if laryngectomy_rc:
        raise SystemExit(laryngectomy_rc)
    print("PASS: global release protects post-laryngectomy PCF/salivary-leak rescue, vessel safety, and revision decisions")

    print("GLOBAL_RELEASE_AIRWAY_FIRE_RESCUE_GATE|" + AIRWAY_FIRE_GATE)
    airway_fire_rc = _v288_airway_fire_main()
    if airway_fire_rc:
        raise SystemExit(airway_fire_rc)
    print("PASS: global release protects shared-airway fire prevention, extinguishment, bronchoscopy, and airway-rescue decisions")

    print("GLOBAL_RELEASE_POSTERIOR_EPISTAXIS_RESCUE_GATE|" + EPISTAXIS_GATE)
    epistaxis_rc = _v289_epistaxis_main()
    if epistaxis_rc:
        raise SystemExit(epistaxis_rc)
    print("PASS: global release protects posterior-epistaxis stabilization, SPA branch control, failure re-localization, embolization tradeoffs, and ICA danger")

    print("GLOBAL_RELEASE_TEP_PROSTHESIS_RESCUE_GATE|" + TEP_GATE)
    tep_rc = _v290_tep_main()
    if tep_rc:
        raise SystemExit(tep_rc)
    print("PASS: global release protects laryngectomy stoma-airway, missing-prosthesis aspiration, bronchoscopic retrieval, tract preservation and leak-triage decisions")


if __name__ == "__main__":
    main()
