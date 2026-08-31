"""v27.8 adversarial production gate for neck-dissection critical non-XI nerve rescue."""
import os, re, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_neck_critical_nerve_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)


def norm(value):
    return re.sub(r"[^a-z0-9]+", " ", str(value or "").lower()).strip()


def has_groups(text, groups):
    t = norm(text)
    return all(any(norm(term) in t for term in group) for group in groups)


def resolve(reg):
    if "neck-dissection" in reg:
        return "neck-dissection", reg["neck-dissection"]
    for slug, op in reg.items():
        hay = norm(str(slug) + " " + str((op or {}).get("title", "")))
        if "neck dissection" in hay and "complication" not in hay:
            return slug, op
    return None, None


try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    slug, op = resolve(reg)
    failures = []
    if not op:
        failures.append("neck-dissection: no live OR Tomorrow case resolved")
    else:
        combined = "\n".join(str(x) for key in ("setup", "steps", "postop") for x in (op.get(key) or []))
        sources = "\n".join(str(x) for x in (op.get("sources") or []))
        if not op.get("neck_dissection_critical_nerve_rescue_v278"):
            failures.append(f"{slug}: v27.8 production marker absent")
        checks = [
            ("three-nerve commitment", (("vagus", "cn x"), ("hypoglossal", "cn xii"), ("phrenic",), ("directly invaded", "oncologic commitment"))),
            ("anatomic protection", (("carotid sheath",), ("anterior scalene",), ("thermal",), ("traction",))),
            ("monitoring nuance", (("monitor", "stimulation"), ("may be considered", "considered"), ("does not replace",), ("not a universal", "universal requirement"))),
            ("transection rescue", (("transect",), ("proximal",), ("distal",), ("tension free", "tension-free"), ("graft",))),
            ("hypoglossal deficit rescue", (("tongue",), ("dysarthria",), ("dysphagia",), ("speech", "swallow"))),
            ("vagal deficit rescue", (("vagal", "vagus"), ("flexible laryngeal",), ("aspiration",), ("bilateral vocal fold",), ("airway emergency",))),
            ("phrenic deficit rescue", (("phrenic",), ("dyspnea",), ("pneumothorax",), ("diaphragm ultrasound", "sniff"), ("respiratory support",))),
        ]
        for label, groups in checks:
            if not has_groups(combined, groups):
                failures.append(f"{slug}: missing critical-nerve concept {label!r}")
        source_groups = (("cummings",), ("k j lee", "lee's essential"), ("pasha",), ("american head neck society",), ("scharpf",), ("phrenic nerve",), ("nerve tension",))
        if not has_groups(sources, source_groups):
            failures.append(f"{slug}: textbook/critical-nerve source trail incomplete")
        client = rt.app.test_client()
        response = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if response.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {response.status_code}")
        body = norm(response.get_data(as_text=True))
        route_groups = (("vagus",), ("hypoglossal",), ("phrenic",), ("tension free",), ("flexible laryngeal",), ("diaphragm",))
        if not has_groups(body, route_groups):
            failures.append(f"{slug}: rendered OR Tomorrow route does not expose v27.8 critical-nerve rescue")
    if failures:
        print("OR v27.8 NECK-DISSECTION CRITICAL-NERVE FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: live neck-dissection OR Tomorrow protects vagus/hypoglossal/phrenic commitment, transection bailout, deficit-specific rescue, provenance, and route coverage")
finally:
    try: os.remove(db)
    except OSError: pass
