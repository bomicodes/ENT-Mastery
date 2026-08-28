"""Hard gate for v23.22 final OR Tomorrow procedure-specific management reviews."""
import os, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_v2322_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

TARGETS = {
    "laryngeal-botox": ("laryngeal_botox_management_v2322", ("adductor", "abductor", "emg"), ("aspiration", "dyspnea")),
    "lingual-tonsillectomy": ("lingual_tonsillectomy_management_v2322", ("dise", "multilevel", "osa"), ("airway", "hemorrhage")),
    "pharyngocutaneous-fistula": ("pharyngocutaneous_fistula_management_v2322", ("radiation", "carotid", "nutrition"), ("carotid blowout", "sentinel")),
    "reconstructive-palate": ("reconstructive_palate_management_v2322", ("pap", "retropalatal", "multilevel"), ("velopharyngeal", "objective")),
    "tep": ("tep_management_v2322", ("primary", "secondary", "speech-language"), ("leakage through", "dislodged", "aspiration")),
}

try:
    import runtime_entry as rt
    reg=rt.data.OR_PREP_REGISTRY
    client=rt.app.test_client()
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
    # Preserve the pre-existing high-consequence fistula warning while deepening management.
    fist=" ".join(str(x).lower() for x in (reg["pharyngocutaneous-fistula"].get("postop") or []))
    if "carotid blowout" not in fist:
        failures.append("pharyngocutaneous-fistula: carotid-blowout rescue language missing")
    if failures:
        print("OR v23.22 FINAL MANAGEMENT FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print(f"PASS: final {len(TARGETS)} OR modules carry v23.22 procedure-specific planning/rescue review and render successfully")
finally:
    try: os.remove(db)
    except OSError: pass
