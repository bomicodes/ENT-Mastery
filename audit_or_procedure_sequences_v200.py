"""Hard gate for v20.x procedure-specific OR Tomorrow choreography.

Fails if any live OR module still depends on v19 generic filler or lacks a deliberate
procedure-level sequence after both the broad v20.0 and exact v20.1 layers run.
"""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_v200_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

BANNED = (
    "perform the planned exposure",
    "procedure-appropriate approach",
    "same principles",
    "same nerve and parathyroid principles",
    "reinspect the operative field for hemostasis, anatomic integrity",
)

SENTINELS = [
    (("total thyroidectomy",), (("superior pole", "superior thyroid"), ("recurrent laryngeal", "rln"), ("parathyroid",), ("berry",), ("contralateral", "opposite side"))),
    (("maxillary antrostomy",), (("uncinate",), ("natural maxillary ostium", "natural ostium"), ("nasolacrimal",), ("orbit", "orbital"))),
    (("stapedotomy", "stapedectomy"), (("incus",), ("footplate",), ("fenestra",), ("prosthesis",))),
    (("cochlear implant",), (("facial recess",), ("round-window", "round window"), ("electrode",), ("receiver",))),
    (("neck dissection",), (("cn xi", "accessory nerve"), ("ijv", "jugular"), ("carotid",), ("thoracic duct", "lymphatic"))),
    (("total laryngectomy",), (("trachea",), ("phary",), ("specimen",), ("stoma",))),
    (("microflap",), (("superficial lamina propria",), ("microflap",), ("vocal ligament",), ("redrape",))),
    (("medialization", "thyroplasty"), (("thyroid cartilage",), ("window",), ("implant",), ("airway", "laryngoscopy", "phonat"))),
    (("laryngotracheal reconstruction",), (("cricoid",), ("cartilage graft", "rib cartilage"), ("stent", "ett"), ("airway",))),
    (("orbital floor",), (("forced duction",), ("implant",), ("infraorbital",), ("vision", "visual"))),
    (("hypoglossal",), (("hypoglossal",), ("cuff",), ("sensing",), ("tongue protrusion", "protrus"))),
    (("free-flap-basics", "head & neck free-flap reconstruction"), (("pedicle",), ("anastom",), ("recipient",), ("perfusion", "doppler"))),
]

try:
    import runtime_entry as rt

    reg = rt.data.OR_PREP_REGISTRY
    assert reg, "OR_PREP_REGISTRY is empty"
    failures = []
    broad = getattr(rt, "OR_PROCEDURE_SEQUENCES_V200", {}) or {}
    exact = getattr(rt, "OR_PROCEDURE_SEQUENCES_V201", {}) or {}

    if exact.get("missing_registry_slugs"):
        failures.append(f"v20.1 exact table references missing registry slugs: {exact['missing_registry_slugs']}")

    for slug, op in reg.items():
        title = str(op.get("title") or slug)
        steps = [str(x).strip() for x in (op.get("steps") or []) if str(x).strip()]
        joined = " ".join(steps).lower()

        if op.get("sequence_status_v200") != "procedure-specific":
            failures.append(f"{slug}: no final procedure-specific sequence")
        if len(steps) < 7:
            failures.append(f"{slug}: only {len(steps)} operative steps; need >=7")
        if len(set(s.lower() for s in steps)) != len(steps):
            failures.append(f"{slug}: duplicate operative steps")
        for phrase in BANNED:
            if phrase in joined:
                failures.append(f"{slug}: banned generic filler remains: {phrase!r}")

        too_short = [s for s in steps if len(s.split()) < 8]
        if too_short:
            failures.append(f"{slug}: underspecified steps: {too_short[:3]}")

        label = (slug + " " + title).lower()
        for triggers, groups in SENTINELS:
            if any(trig in label for trig in triggers):
                for group in groups:
                    if not any(term in joined for term in group):
                        failures.append(f"{slug}: sentinel {triggers[0]!r} missing one of {group!r}")

    client = rt.app.test_client()
    for slug, op in reg.items():
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
            continue
        text = r.get_data(as_text=True).lower()
        for phrase in BANNED:
            if phrase in text:
                failures.append(f"{slug}: rendered page leaked generic filler {phrase!r}")

    if failures:
        print("OR v20.x PROCEDURE-SEQUENCE FAILURES")
        print("\n".join(failures[:300]))
        raise SystemExit(1)

    print(
        f"PASS: {len(reg)} OR modules have procedure-specific v20.x sequences; "
        f"broad_replaced={broad.get('replaced')} exact_overrides={exact.get('count')} "
        f"generic_removed={broad.get('generic_removed')}"
    )
finally:
    try:
        os.remove(db)
    except OSError:
        pass
