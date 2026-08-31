"""v27.3 adversarial production gate for neck-dissection venous-outflow protection."""
import os, re, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_neck_venous_", suffix=".db")
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
        if not op.get("neck_dissection_venous_outflow_v273"):
            failures.append(f"{slug}: v27.3 production marker absent")
        checks = [
            ("last-patent-IJV commitment", (("contralateral", "last dependable", "last patent"), ("bilateral",), ("preserve", "stage", "reconstruction"), ("venous hypertension", "cerebral edema"))),
            ("protect remaining outflow", (("traction", "thermal injury", "compression"), ("only reliable", "last dependable"), ("restore", "reconstruction", "venous outflow"))),
            ("postoperative danger recognition", (("facial", "head", "neck edema"), ("chemosis", "headache", "mental status", "neurologic"), ("airway",), ("thrombosis", "obstruction"))),
            ("time-sensitive rescue", (("hematoma", "tight closure", "compression", "technical narrowing"), ("decompression", "thrombectomy", "revision", "reconstruction"), ("early", "time sensitive"))),
        ]
        for label, groups in checks:
            if not has_groups(combined, groups):
                failures.append(f"{slug}: missing venous-outflow concept {label!r}")
        source_groups = (("cummings",), ("k j lee", "lee's essential"), ("pasha",), ("quraishi",), ("prim",))
        if not has_groups(sources, source_groups):
            failures.append(f"{slug}: textbook/venous-outflow source trail incomplete")
        client = rt.app.test_client()
        response = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if response.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {response.status_code}")
        body = norm(response.get_data(as_text=True))
        if "internal jugular" not in body or "venous" not in body or "cerebral edema" not in body:
            failures.append(f"{slug}: rendered OR Tomorrow route does not expose v27.3 venous-outflow rescue")
    if failures:
        print("OR v27.3 NECK-DISSECTION VENOUS-OUTFLOW FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: live neck-dissection OR Tomorrow preserves last-patent-IJV planning, venous-outflow rescue, source provenance, and route coverage")
finally:
    try: os.remove(db)
    except OSError: pass
