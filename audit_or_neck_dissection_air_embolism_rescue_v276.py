"""v27.6 adversarial production gate for neck-dissection venous-air-embolism rescue."""
import os, re, tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_neck_air_embolism_", suffix=".db")
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
        if not op.get("neck_dissection_air_embolism_rescue_v276"):
            failures.append(f"{slug}: v27.6 production marker absent")
        checks = [
            ("air-entry prevention", (("air entry", "air-entry"), ("internal jugular", "large"), ("flooded", "saline", "moist"), ("control",))),
            ("clinical recognition", (("end tidal co2", "etco2"), ("hypoxemia",), ("hypotension", "collapse"), ("arrhythmia",))),
            ("coordinated immediate rescue", (("occlude", "control"), ("100 oxygen", "100% oxygen"), ("nitrous oxide",), ("preload", "right heart", "blood pressure"))),
            ("adjuncts do not delay", (("central venous catheter",), ("aspirat",), ("should not delay", "do not delay"), ("resuscitation", "cpr"))),
            ("paradoxical/end-organ rescue", (("paradoxical",), ("neurologic",), ("coronary", "cardiac"), ("surveillance", "evaluation"))),
        ]
        for label, groups in checks:
            if not has_groups(combined, groups):
                failures.append(f"{slug}: missing venous-air-embolism concept {label!r}")
        source_groups = (("cummings",), ("k j lee", "lee's essential"), ("pasha",), ("hybels",), ("rice jh",), ("openanesthesia", "altshuler"))
        if not has_groups(sources, source_groups):
            failures.append(f"{slug}: textbook/air-embolism source trail incomplete")
        client = rt.app.test_client()
        response = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if response.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {response.status_code}")
        body = norm(response.get_data(as_text=True))
        route_groups = (("air embol",), ("end tidal co2",), ("100 oxygen",), ("nitrous oxide",), ("paradoxical",))
        if not has_groups(body, route_groups):
            failures.append(f"{slug}: rendered OR Tomorrow route does not expose v27.6 venous-air-embolism rescue")
    if failures:
        print("OR v27.6 NECK-DISSECTION VENOUS-AIR-EMBOLISM FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)
    print("PASS: live neck-dissection OR Tomorrow preserves venous-air-embolism prevention, recognition, coordinated rescue, non-delaying adjuncts, end-organ surveillance, provenance, and route coverage")
finally:
    try: os.remove(db)
    except OSError: pass
