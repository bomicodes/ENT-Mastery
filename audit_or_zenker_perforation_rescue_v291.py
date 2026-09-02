"""v29.1 adversarial gate for Zenker/cricopharyngeal postoperative perforation rescue."""
import os, re, tempfile


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()


def has_groups(text, groups):
    t = norm(text)
    return all(any(norm(term) in t for term in group) for group in groups)


def resolve_all(reg):
    found = []
    for slug, op in (reg or {}).items():
        hay = norm(str(slug) + " " + str((op or {}).get("title", "")))
        if "zenker" in hay or ("cricopharyngeal" in hay and "myotomy" in hay):
            found.append((slug, op))
    return found


RECOGNITION = (
    ("neck chest pain", "neck pain", "chest pain"),
    ("crepitus", "subcutaneous emphysema"),
    ("systemic toxicity", "sepsis"),
    ("stop oral intake", "npo"),
    ("airway",),
    ("hemodynamics", "resuscitation"),
)
DIAGNOSTIC = (
    ("ct", "computed tomography"),
    ("neck and chest", "neck chest"),
    ("extraluminal air", "extraluminal"),
    ("mediastinal", "pleural contamination"),
    ("contrast swallow", "water soluble"),
    ("avoid repeated blind instrumentation", "blind instrumentation"),
)
CONTAINMENT = (
    ("npo", "stop oral intake"),
    ("antimicrobial", "antibiotic"),
    ("nutritional", "diversion"),
    ("endoscopic closure",),
    ("secure mucosal closure", "controlled leak"),
    ("prophylactic antibiotics",),
)
ESCALATION = (
    ("contained cervical leak", "contained leak"),
    ("close inpatient observation", "observation"),
    ("free leak",),
    ("collection",),
    ("clinical deterioration", "deterioration"),
    ("source control failure", "source control"),
    ("drainage",),
    ("operative repair", "repair revision", "definitive strategy"),
)
POSTOP = (
    ("before resuming oral intake", "resuming oral intake"),
    ("recurrent fever",),
    ("neck pain swelling", "neck pain", "neck swelling"),
    ("aspiration",),
    ("deep infection", "perforation"),
)
SOURCE_GROUPS = (
    ("cummings",),
    ("k j lee", "lee's essential"),
    ("pasha",),
    ("paspatis", "esge position statement"),
    ("weusten", "esge guideline"),
    ("dhar", "zenker's per oral endoscopic myotomy"),
)


def main():
    fd, db = tempfile.mkstemp(prefix="ent_or_zenker_", suffix=".db")
    os.close(fd)
    os.environ.pop("DATABASE_URL", None)
    os.environ["SQLITE_PATH"] = db
    os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)
    try:
        import runtime_entry_pasha as prod
        reg = prod.runtime_entry.data.OR_PREP_REGISTRY
        client = prod.app.test_client()
        failures = []
        found = resolve_all(reg)
        if not found:
            failures.append("no live Zenker/cricopharyngeal-myotomy case resolved")
        for slug, op in found:
            if not op.get("zenker_perforation_rescue_v291"):
                failures.append(f"{slug}: v29.1 production marker absent")
                continue
            postop = "\n".join(str(x) for x in (op.get("postop") or []))
            sources = "\n".join(str(x) for x in (op.get("sources") or []))
            if not has_groups(postop, RECOGNITION):
                failures.append(f"{slug}: recognition/resuscitation pathway incomplete")
            if not has_groups(postop, DIAGNOSTIC):
                failures.append(f"{slug}: CT/leak-definition pathway incomplete")
            if not has_groups(postop, CONTAINMENT):
                failures.append(f"{slug}: containment/endoscopic-closure pathway incomplete")
            if not has_groups(postop, ESCALATION):
                failures.append(f"{slug}: source-control escalation incomplete")
            if not has_groups(postop, POSTOP):
                failures.append(f"{slug}: post-rescue reassessment incomplete")
            if not has_groups(sources, SOURCE_GROUPS):
                failures.append(f"{slug}: source provenance incomplete")
            r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
            if r.status_code >= 500:
                failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
            body = norm(r.get_data(as_text=True))
            for concept in ("stop oral intake", "endoscopic closure", "source-control", "mediastinal"):
                if norm(concept) not in body:
                    failures.append(f"{slug}: {concept!r} not rendered on /case-tomorrow")
        if failures:
            print("OR v29.1 ZENKER PERFORATION RESCUE FAILURES")
            print("\n".join(failures))
            return 1
        print("PASS: Zenker/cricopharyngeal leak recognition, CT localization, selective closure, containment and source-control escalation render live")
        return 0
    finally:
        try: os.remove(db)
        except OSError: pass


if __name__ == "__main__":
    raise SystemExit(main())
