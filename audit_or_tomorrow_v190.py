"""Hard gate for v19.0/v19.1 OR Tomorrow operative-depth and concept-link contract."""
import os, sys, tempfile

_fd, _db = tempfile.mkstemp(prefix="ent_or_v190_", suffix=".db")
os.close(_fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = _db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

try:
    import runtime_entry as rt
    reg=rt.data.OR_PREP_REGISTRY
    assert reg, "OR_PREP_REGISTRY is empty"
    failures=[]
    parathyroid_cases=[]
    for slug,op in reg.items():
        def need(cond,msg):
            if not cond: failures.append(f"{slug}: {msg}")
        need(op.get("review_status_v190")=="operative-depth reviewed","v19.0 review marker missing")
        need(len(op.get("setup") or [])>=2,"needs >=2 setup/planning items")
        need(len(op.get("steps") or [])>=6,"needs >=6 operative sequence steps")
        need(len(op.get("landmarks") or [])>=3,"needs >=3 positive landmarks")
        need(len(op.get("danger") or [])>=2,"needs >=2 danger items")
        need(len(op.get("exit_check") or [])>=2,"needs >=2 safe-exit checks")
        need(len(op.get("postop") or [])>=2,"needs >=2 immediate postoperative priorities")
        comp=op.get("complications") or {}
        need(len(comp.get("early") or [])>=1,"needs early complications")
        need(len(comp.get("late") or [])>=1,"needs late complications")
        need(len(op.get("source_basis") or [])>=2,"needs >=2 operative reference sources")
        if "parathyroidectomy" in str(op.get("title") or "").lower() or "parathyroid" in str(slug).lower():
            parathyroid_cases.append((slug, op))

    need_parathyroid = bool(parathyroid_cases)
    if not need_parathyroid:
        failures.append("registry: no parathyroid OR case found for link regression test")
    for slug, op in parathyroid_cases:
        if str(op.get("linked_topic") or "").strip().lower() != "parathyroid":
            failures.append(f"{slug}: parathyroid linked_topic must be canonical 'Parathyroid', got {op.get('linked_topic')!r}")

    if failures:
        print("OR v19.0/v19.1 CONTENT FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    client=rt.app.test_client()
    route_fail=[]
    for slug,op in reg.items():
        r=client.get("/case-tomorrow",query_string={"q":op.get("title",slug)},follow_redirects=True)
        text=r.get_data(as_text=True)
        if r.status_code>=500:
            route_fail.append(f"{slug}: HTTP {r.status_code}")
        for marker in ("OPERATIVE SEQUENCE","IMMEDIATE POST-OP PRIORITIES","POSTOPERATIVE COMPLICATIONS","SOURCE BASIS"):
            if marker not in text:
                route_fail.append(f"{slug}: rendered page missing {marker}")

    for slug,op in parathyroid_cases:
        r=client.get("/concept",query_string={"domain":op.get("domain",""),"topic":"Parathyroid"},follow_redirects=True)
        text=r.get_data(as_text=True).lower()
        if r.status_code>=500:
            route_fail.append(f"{slug}: canonical Parathyroid concept route HTTP {r.status_code}")
        if "parathyroid-disease" in text:
            route_fail.append(f"{slug}: legacy parathyroid-disease slug leaked into canonical concept route")

    if route_fail:
        print("OR v19.0/v19.1 ROUTE FAILURES")
        print("\n".join(route_fail[:100]))
        raise SystemExit(1)

    print(f"PASS: {len(reg)} OR modules meet v19.0 operative + postoperative contract")
    print("families:", rt.OR_TOMORROW_OVERHAUL_V190.get("profiles"))
    print("exact refinements:", rt.OR_TOMORROW_OVERHAUL_V190.get("exact"))
    print("concept-link fixes:", rt.OR_CONCEPT_LINK_FIX_V191)
finally:
    try: os.remove(_db)
    except OSError: pass
