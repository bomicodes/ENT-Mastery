"""Hard gate for v23.18 facial-trauma OR Tomorrow management review."""
import os, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_v2318_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

TARGETS = {
    "closed-nasal-reduction": ("closed_nasal_reduction_management_v2318", ("septal hematoma", "consolidation"), ("saddle", "valve")),
    "frontal-sinus-trauma": ("frontal_sinus_trauma_management_v2318", ("posterior-table", "outflow"), ("csf", "mucocele")),
    "mandible-orif": ("mandible_orif_management_v2318", ("occlusion", "inferior-alveolar"), ("malocclusion", "hardware")),
    "noe-orif": ("noe_orif_management_v2318", ("medial canthal", "lacrimal"), ("intercanthal", "epiphora")),
    "orbital-floor": ("orbital_floor_management_v2318", ("visual acuity", "entrapment"), ("rapd", "compartment")),
    "zmc-orif": ("zmc_orif_management_v2318", ("malar", "occlusion"), ("visual", "v2")),
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
    if failures:
        print("OR v23.18 FACIAL TRAUMA FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"PASS: {len(TARGETS)} facial-trauma OR modules carry v23.18 planning/rescue review and render successfully")
finally:
    try: os.remove(db)
    except OSError: pass
