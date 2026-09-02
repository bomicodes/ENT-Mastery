"""v28.9 adversarial gate for posterior epistaxis / SPA rescue."""
import os, re, tempfile


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()


def has_groups(text, groups):
    t = norm(text)
    return all(any(norm(term) in t for term in group) for group in groups)


def resolve(reg):
    if "spa-ligation" in reg:
        return "spa-ligation", reg["spa-ligation"]
    for slug, op in reg.items():
        hay = norm(str(slug) + " " + str((op or {}).get("title", "")))
        if "sphenopalatine" in hay and "artery" in hay:
            return slug, op
    return None, None


STABILIZE_GROUPS = (
    ("airway",),
    ("suction",),
    ("iv access", "large bore"),
    ("packing", "balloon"),
    ("temporizing", "bridge"),
    ("definitive control", "operative control"),
    ("anesthesia",),
)
EXPOSURE_GROUPS = (
    ("crista ethmoidalis", "ethmoid crest"),
    ("sphenopalatine foramen",),
    ("mucoperiosteal", "mucoperiosteal flap"),
    ("multiple branches", "additional posterior nasal", "accessory foramina"),
)
FAILURE_GROUPS = (
    ("missed spa", "posterior nasal branch", "missed"),
    ("contralateral",),
    ("ethmoidal", "ethmoid"),
    ("pseudoaneurysm", "vascular lesion"),
    ("blind cautery", "deeper blind cautery"),
)
ESCALATION_GROUPS = (
    ("surgical arterial control", "surgical"),
    ("endovascular embolization", "embolization"),
    ("not universally", "neither modality", "universally mandatory"),
    ("external to internal carotid", "external-to-internal carotid", "ophthalmic anastomoses"),
    ("stroke",),
    ("blindness", "visual"),
    ("internal carotid",),
    ("neurointerventional",),
)
POSTOP_GROUPS = (
    ("recurrent", "rebleed"),
    ("aspiration", "airway compromise"),
    ("neurologic",),
    ("visual",),
    ("ischemia", "non target", "non-target"),
)
SOURCE_GROUPS = (
    ("cummings",),
    ("k j lee", "lee's essential"),
    ("pasha",),
    ("tunkel", "clinical practice guideline nosebleed"),
    ("bonnici", "endovascular embolization"),
    ("simmen", "sphenopalatine artery"),
)


def main():
    fd, db = tempfile.mkstemp(prefix="ent_or_epistaxis_", suffix=".db")
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
            failures.append("spa-ligation: no live SPA control case resolved")
        else:
            if not op.get("posterior_epistaxis_rescue_v289"):
                failures.append(f"{slug}: v28.9 production marker absent")
            setup = "\n".join(str(x) for x in (op.get("setup") or []))
            steps = "\n".join(str(x) for x in (op.get("steps") or []))
            postop = "\n".join(str(x) for x in (op.get("postop") or []))
            sources = "\n".join(str(x) for x in (op.get("sources") or []))
            if not has_groups(setup, STABILIZE_GROUPS):
                failures.append(f"{slug}: hemorrhage stabilization/airway commitment incomplete")
            if not has_groups(steps, EXPOSURE_GROUPS):
                failures.append(f"{slug}: SPA exposure/complete-branch choreography incomplete")
            if not has_groups(steps, FAILURE_GROUPS):
                failures.append(f"{slug}: recurrent-bleed source re-localization incomplete")
            if not has_groups(steps, ESCALATION_GROUPS):
                failures.append(f"{slug}: surgery/embolization and major-vessel danger decisions incomplete")
            if not has_groups(postop, POSTOP_GROUPS):
                failures.append(f"{slug}: post-control recurrence/ischemia surveillance incomplete")
            if not has_groups(sources, SOURCE_GROUPS):
                failures.append(f"{slug}: posterior-epistaxis source provenance incomplete")
            r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
            if r.status_code >= 500:
                failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
            body = norm(r.get_data(as_text=True))
            for concept in ("crista ethmoidalis", "embolization", "pseudoaneurysm", "neurointerventional"):
                if norm(concept) not in body:
                    failures.append(f"{slug}: {concept!r} not rendered on /case-tomorrow")
        if failures:
            print("OR v28.9 POSTERIOR EPISTAXIS RESCUE FAILURES")
            print("\n".join(failures))
            return 1
        print("PASS: posterior epistaxis stabilization, SPA exposure/branch control, failure re-localization, embolization tradeoffs and ICA danger render live")
        return 0
    finally:
        try: os.remove(db)
        except OSError: pass


if __name__ == "__main__":
    raise SystemExit(main())
