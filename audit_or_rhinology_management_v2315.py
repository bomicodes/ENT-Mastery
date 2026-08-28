"""Hard gate for v23.15 procedure-specific rhinology OR Tomorrow management."""
import os, tempfile

_fd, _db = tempfile.mkstemp(prefix="ent_or_v2315_", suffix=".db")
os.close(_fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = _db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

EXPECT = {
    "endoscopic-sinus-surgery": ("fess_management_v2315", ("three planes", "image guidance"), ("visual", "clear unilateral rhinorrhea")),
    "draf": ("draf_management_v2315", ("frontal drainage", "neo-ostium"), ("restenosis", "clear rhinorrhea")),
    "sphenoidotomy": ("sphenoidotomy_management_v2315", ("carotid", "optic"), ("visual", "arterial bleeding")),
    "spa-ligation": ("spa_management_v2315", ("multiple spa branches", "coagulopathy"), ("recurrent brisk bleeding", "anterior ethmoid")),
    "orbital-abscess": ("orbital_abscess_management_v2315", ("vision", "contrast imaging"), ("rapd", "residual")),
}

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    client = rt.app.test_client()
    failures = []
    for slug, (marker, setup_terms, postop_terms) in EXPECT.items():
        op = reg.get(slug)
        if not op:
            failures.append(f"{slug}: missing live module")
            continue
        if not op.get(marker):
            failures.append(f"{slug}: missing {marker}")
        setup = " ".join(map(str, op.get("setup") or [])).lower()
        postop = " ".join(map(str, op.get("postop") or [])).lower()
        for term in setup_terms:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in postop_terms:
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: route HTTP {r.status_code}")
        rendered = r.get_data(as_text=True).lower()
        if setup_terms[0] not in rendered or postop_terms[0] not in rendered:
            failures.append(f"{slug}: reviewed content not rendered")
    if failures:
        print("OR v23.15 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: v23.15 reviewed rhinology management is live for", ", ".join(EXPECT))
finally:
    try: os.remove(_db)
    except OSError: pass
