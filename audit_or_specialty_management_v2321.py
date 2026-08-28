"""Hard gate for v23.21 specialty OR Tomorrow management review."""
import os, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_v2321_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

TARGETS = {
    "canalplasty": ("canalplasty_management_v2321", ("audiometry", "canal skin"), ("stenosis", "sensorineural")),
    "central-neck": ("central_neck_management_v2321", ("level vi", "recurrent laryngeal", "parathyroid"), ("hypocalcemia", "vocal-fold")),
    "ctr": ("ctr_management_v2321", ("cricotracheal", "posterior cricoid", "tension"), ("anastom", "restenosis")),
    "maxillary-antrostomy": ("maxillary_antrostomy_management_v2321", ("natural", "odontogenic", "recirculation"), ("unilateral", "patent")),
    "tegmen-repair": ("tegmen_repair_management_v2321", ("temporal-bone ct", "middle-fossa", "transmastoid"), ("mening", "pseudomeningocele")),
}

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures=[]
    for slug,(marker,setup_terms,postop_terms) in TARGETS.items():
        op=reg.get(slug)
        if not op:
            failures.append(f"{slug}: missing from live OR registry")
            continue
        if not op.get(marker): failures.append(f"{slug}: missing {marker}")
        setup=" ".join(str(x).lower() for x in (op.get("setup") or []))
        postop=" ".join(str(x).lower() for x in (op.get("postop") or []))
        for term in setup_terms:
            if term not in setup: failures.append(f"{slug}: setup missing {term!r}")
        for term in postop_terms:
            if term not in postop: failures.append(f"{slug}: postop missing {term!r}")
        r=client.get("/case-tomorrow",query_string={"q":op.get("title",slug)},follow_redirects=True)
        if r.status_code>=500: failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
    # Protect the central-vs-lateral neck separation explicitly.
    central=" ".join(str(x).lower() for x in (reg["central-neck"].get("setup") or []))
    if "spinal-accessory" not in central or "do not import lateral-neck" not in central:
        failures.append("central-neck: explicit lateral-neck contamination warning lost")
    if failures:
        print("OR v23.21 SPECIALTY FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"PASS: {len(TARGETS)} specialty OR modules carry v23.21 planning/rescue review and render successfully")
finally:
    try: os.remove(db)
    except OSError: pass
