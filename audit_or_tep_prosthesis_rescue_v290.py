"""v29.0 adversarial gate for TEP voice-prosthesis dislodgement/aspiration rescue."""
import os, re, tempfile


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()


def has_groups(text, groups):
    t = norm(text)
    return all(any(norm(term) in t for term in group) for group in groups)


def resolve(reg):
    if "tep" in reg:
        return "tep", reg["tep"]
    for slug, op in reg.items():
        hay = norm(str(slug) + " " + str((op or {}).get("title", "")))
        if "tracheoesophageal" in hay and "puncture" in hay:
            return slug, op
    return None, None


AIRWAY_GROUPS = (
    ("neck only airway", "neck-only airway"),
    ("permanent stoma", "stoma"),
    ("not through the mouth", "not through the mouth or nose", "not through mouth"),
    ("oxygenation", "bag mask", "bag-mask"),
    ("senior ent", "anesthesia"),
)
MISSING_GROUPS = (
    ("cannot be physically accounted for", "unaccounted", "missing"),
    ("aspiration", "tracheobronchial foreign body"),
    ("chest radiograph", "radiograph"),
    ("radiographically occult", "normal or equivocal"),
    ("ct", "computed tomography"),
    ("bronchoscopy",),
    ("definitive airway assessment", "retrieval"),
)
RETRIEVAL_GROUPS = (
    ("direct bronchoscopic visualization", "bronchoscopic"),
    ("foreign body", "retrieval"),
    ("retained fragments", "fragments"),
    ("distal obstruction", "distal"),
    ("blind forceps", "blind"),
    ("controlled airway", "or rescue"),
)
TRACT_GROUPS = (
    ("tract",),
    ("narrow or close", "closure"),
    ("catheter", "stent"),
    ("trained clinician", "local laryngectomy", "slp protocol"),
    ("not blind", "blind instrumentation"),
    ("resistance",),
    ("false passage",),
    ("not a universal", "not universal", "not a universal first line"),
)
LEAK_GROUPS = (
    ("through",),
    ("around", "periprosthetic"),
    ("valve failure", "debris"),
    ("length", "fit"),
    ("tract enlargement", "granulation"),
    ("aspiration pneumonia", "pneumonia", "respiratory compromise"),
    ("ent slp", "ent", "slp"),
)
POSTOP_GROUPS = (
    ("patent stoma airway", "stoma airway"),
    ("safe prosthesis position", "prosthesis position"),
    ("swallowing leakage", "oral intake"),
    ("recurrent dislodgement", "recurrent missing"),
    ("unsupervised manipulation", "repeat airway"),
)
SOURCE_GROUPS = (
    ("cummings",),
    ("k j lee", "lee's essential"),
    ("pasha",),
    ("ottenstein", "tep in the er"),
    ("dewan", "aspirated tracheoesophageal"),
    ("brenner", "computed tomography and bronchoscopy"),
    ("national tracheostomy safety project",),
)


def main():
    fd, db = tempfile.mkstemp(prefix="ent_or_tep_", suffix=".db")
    os.close(fd)
    os.environ.pop("DATABASE_URL", None)
    os.environ["SQLITE_PATH"] = db
    os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)
    try:
        import runtime_entry_pasha as prod
        reg = prod.runtime_entry.data.OR_PREP_REGISTRY
        client = prod.app.test_client()
        failures = []
        slug, op = resolve(reg)
        if not op:
            failures.append("tep: no live tracheoesophageal puncture case resolved")
        else:
            if not op.get("tep_prosthesis_rescue_v290"):
                failures.append(f"{slug}: v29.0 production marker absent")
            setup = "\n".join(str(x) for x in (op.get("setup") or []))
            steps = "\n".join(str(x) for x in (op.get("steps") or []))
            postop = "\n".join(str(x) for x in (op.get("postop") or []))
            sources = "\n".join(str(x) for x in (op.get("sources") or []))
            if not has_groups(setup, AIRWAY_GROUPS):
                failures.append(f"{slug}: laryngectomy stoma-only airway rescue incomplete")
            if not has_groups(steps, MISSING_GROUPS):
                failures.append(f"{slug}: missing-prosthesis aspiration/localization pathway incomplete")
            if not has_groups(steps, RETRIEVAL_GROUPS):
                failures.append(f"{slug}: bronchoscopic retrieval/rescue choreography incomplete")
            if not has_groups(steps, TRACT_GROUPS):
                failures.append(f"{slug}: safe tract-preservation boundary incomplete")
            if not has_groups(steps, LEAK_GROUPS):
                failures.append(f"{slug}: through-versus-around leak triage incomplete")
            if not has_groups(postop, POSTOP_GROUPS):
                failures.append(f"{slug}: post-retrieval/replacement surveillance incomplete")
            if not has_groups(sources, SOURCE_GROUPS):
                failures.append(f"{slug}: TEP rescue source provenance incomplete")
            r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
            if r.status_code >= 500:
                failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
            body = norm(r.get_data(as_text=True))
            for concept in ("neck-only airway", "bronchoscopy", "false passage", "periprosthetic leakage"):
                if norm(concept) not in body:
                    failures.append(f"{slug}: {concept!r} not rendered on /case-tomorrow")
        if failures:
            print("OR v29.0 TEP PROSTHESIS RESCUE FAILURES")
            print("\n".join(failures))
            return 1
        print("PASS: TEP stoma-airway rescue, missing-device aspiration, bronchoscopic retrieval, safe tract preservation and leak triage render live")
        return 0
    finally:
        try: os.remove(db)
        except OSError: pass


if __name__ == "__main__":
    raise SystemExit(main())
