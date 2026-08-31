"""Hard gate for v23.14 high-risk OR Tomorrow management review."""
import os, tempfile

_fd, _db = tempfile.mkstemp(prefix="ent_or_v2314_", suffix=".db")
os.close(_fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = _db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

EXPECT = {
    "tors": {
        "marker": "tors_management_v2314",
        "setup": ("exposure", "hemorrhage"),
        "postop": ("bleeding", "aspiration"),
    },
    "tracheostomy": {
        "marker": "tracheostomy_management_v2314",
        "setup": ("fresh tract", "rescue"),
        "postop": ("false passage", "tracheo-innominate"),
    },
    "csf-nasoseptal": {
        "marker": "csf_nasoseptal_management_v2314",
        "setup": ("intracranial-pressure", "reconstruction"),
        "postop": ("mening", "clear rhinorrhea"),
    },
    "total-laryngectomy": {
        "marker": "total_laryngectomy_rescue_v2314",
        "title_terms": ("total", "laryngectomy"),
        "setup": ("permanently separated airway", "neck-breather", "vascularized-tissue reinforcement"),
        "postop": ("direct oxygen to the stoma", "oral or nasal", "pharyngocutaneous fistula", "carotid-blowout"),
        "sources": ("cummings", "k. j. lee", "pasha", "national tracheostomy safety project", "ifos"),
    },
    "vestibular-schwannoma": {
        "marker": "vestibular_schwannoma_management_v2314",
        "setup": ("hearing", "corridor"),
        "postop": ("facial", "hydrocephalus"),
    },
}


def _resolve(reg, preferred, spec):
    if preferred in reg:
        return preferred, reg[preferred]
    terms = spec.get("title_terms") or ()
    if terms:
        for slug, op in reg.items():
            hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
            if all(term in hay for term in terms):
                return slug, op
    return None, None


try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    failures = []
    client = rt.app.test_client()

    for preferred, spec in EXPECT.items():
        slug, op = _resolve(reg, preferred, spec)
        if not op:
            failures.append(f"{preferred}: missing from live registry")
            continue
        if not op.get(spec["marker"]):
            failures.append(f"{slug}: missing {spec['marker']}")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        postop = " ".join(str(x) for x in (op.get("postop") or [])).lower()
        sources = " ".join(str(x) for x in (op.get("sources") or [])).lower()
        for term in spec["setup"]:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        for term in spec["postop"]:
            if term not in postop:
                failures.append(f"{slug}: postop missing {term!r}")
        for term in spec.get("sources", ()):
            if term not in sources:
                failures.append(f"{slug}: source trail missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: route HTTP {r.status_code}")
        text = r.get_data(as_text=True).lower()
        for term in (spec["setup"][0], spec["postop"][0]):
            if term not in text:
                failures.append(f"{slug}: rendered route missing {term!r}")

    if failures:
        print("OR v23.14 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print("PASS: v23.14 high-risk management review is live for", ", ".join(EXPECT))
finally:
    try:
        os.remove(_db)
    except OSError:
        pass
