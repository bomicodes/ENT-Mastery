"""Hard gate for v23.17 pediatric core OR Tomorrow management review."""
import os, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_v2317_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

TARGETS = {
    "DLB": ("pediatric_dlb_management_v2317", ("spontaneous ventilation", "airway measurement"), ("stridor", "disposition")),
    "direct-laryngoscopy-bronchoscopy": ("pediatric_dlb_management_v2317", ("spontaneous ventilation", "airway measurement"), ("stridor", "disposition")),
    "airway-fb": ("pediatric_airway_fb_management_v2317", ("aspiration", "blind grasping"), ("retained fragment", "pneumothorax")),
    "branchial": ("branchial_management_v2317", ("carotid", "infection"), ("cranial-nerve", "recurr")),
    "thyroglossal": ("sistrunk_management_v2317", ("thyroid", "hyoid"), ("hematoma", "recurr")),
    "palatoplasty": ("palatoplasty_management_v2317", ("airway", "levator"), ("obstruction", "velopharyngeal")),
    "tympanostomy-tubes": ("tympanostomy_tube_management_v2317", ("effusion", "hearing"), ("topical", "perforation")),
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
        if not op.get(marker):
            failures.append(f"{slug}: missing {marker}")
        setup = " ".join(str(x).lower() for x in (op.get("setup") or []))
        postop = " ".join(str(x).lower() for x in (op.get("postop") or []))
        for term in setup_terms:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in postop_terms:
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
    if failures:
        print("OR v23.17 PEDIATRIC CORE FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"PASS: {len(TARGETS)} pediatric OR modules carry v23.17 planning/rescue review and render successfully")
finally:
    try: os.remove(db)
    except OSError: pass
