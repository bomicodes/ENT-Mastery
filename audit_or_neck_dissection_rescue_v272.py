"""v27.2 adversarial production gate for neck-dissection chyle prevention/rescue."""
import os, re, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_neck_chyle_", suffix=".db")
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
        if not op.get("neck_dissection_chyle_rescue_v272"):
            failures.append(f"{slug}: v27.2 production marker absent")
        checks = [
            ("intraoperative lymphatic control", (("left level iv", "venous angle"), ("clip", "ligation", "secure repair"), ("valsalva", "intrathoracic pressure"), ("re inspect", "reinspect"))),
            ("postoperative recognition and consequences", (("milky", "enteral fat"), ("trend output", "quantify"), ("triglyceride", "chylomicron"), ("electrolyte",), ("protein", "malnutrition"), ("wound", "free flap", "great vessel"))),
            ("trajectory rather than magic cutoff", (("trajectory", "clinical consequence"), ("single memorized", "arbitrary output threshold"), ("low fat", "mct"), ("fluid", "electrolyte", "protein"), ("failure to improve", "persistently large"))),
            ("definitive escalation options", (("re exploration", "re-exploration", "ligation"), ("lymphangiography",), ("embolization",), ("transthoracic", "thoracic duct ligation"))),
        ]
        for label, groups in checks:
            if not has_groups(combined, groups):
                failures.append(f"{slug}: missing chyle-rescue concept {label!r}")
        source_groups = (("cummings",), ("k j lee", "lee's essential"), ("pasha",), ("smith", "systematic review"), ("ganesan", "comprehensive review"), ("picton", "improving the management"))
        if not has_groups(sources, source_groups):
            failures.append(f"{slug}: textbook/recent-literature source trail incomplete")
        client = rt.app.test_client()
        response = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if response.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {response.status_code}")
        body = norm(response.get_data(as_text=True))
        if "chyle" not in body or "embolization" not in body:
            failures.append(f"{slug}: rendered OR Tomorrow route does not expose v27.2 chyle rescue")
    if failures:
        print("OR v27.2 NECK-DISSECTION CHYLE RESCUE FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: live neck-dissection OR Tomorrow preserves source-grounded chyle prevention, trend-based rescue, escalation, and rendered-route coverage")
finally:
    try: os.remove(db)
    except OSError: pass
