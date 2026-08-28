"""Hard gate for v23.20 general/emergency ENT OR Tomorrow management review."""
import os, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_v2320_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

TARGETS = {
    "button-battery": ("button_battery_management_v2320", ("emergency", "orientation", "aortic"), ("mucosal", "tissue injury")),
    "esophageal-fb": ("esophageal_fb_management_v2320", ("sharp", "complete obstruction"), ("mucosal", "underlying")),
    "deep-neck-drain": ("deep_neck_abscess_management_v2320", ("airway", "contrast ct", "mediastinal"), ("source control", "airway")),
    "pta-drainage": ("pta_management_v2320", ("airway", "carotid"), ("hydration", "deep-neck")),
    "rigid-tracheobronchoscopy": ("rigid_tracheobronchoscopy_management_v2320", ("shared-airway", "fire"), ("pneumothorax", "perforation")),
    "transnasal-esophagoscopy": ("transnasal_esophagoscopy_management_v2320", ("diagnostic target", "office-tne"), ("perforation", "pathology")),
}

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []
    for slug, (marker, setup_terms, postop_terms) in TARGETS.items():
        op = reg.get(slug)
        if not op:
            failures.append(f"{slug}: missing from live OR registry")
            continue
        if not op.get(marker): failures.append(f"{slug}: missing {marker}")
        setup = " ".join(str(x).lower() for x in (op.get("setup") or []))
        postop = " ".join(str(x).lower() for x in (op.get("postop") or []))
        for term in setup_terms:
            if term not in setup: failures.append(f"{slug}: setup missing {term!r}")
        for term in postop_terms:
            if term not in postop: failures.append(f"{slug}: postop missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500: failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
    # Protect the older high-consequence safety language while adding the new decision layer.
    battery = " ".join(str(x).lower() for x in (reg["button-battery"].get("postop") or []))
    if "aorto-esophageal" not in battery or "tracheoesophageal" not in battery:
        failures.append("button-battery: prior delayed fistula/aorto-esophageal safety warning lost")
    esoph = " ".join(str(x).lower() for x in (reg["esophageal-fb"].get("postop") or []))
    if "perforation" not in esoph:
        failures.append("esophageal-fb: prior perforation safety warning lost")
    if failures:
        print("OR v23.20 GENERAL/EMERGENCY FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"PASS: {len(TARGETS)} general/emergency OR modules carry v23.20 planning/rescue review and preserve prior safety content")
finally:
    try: os.remove(db)
    except OSError: pass
