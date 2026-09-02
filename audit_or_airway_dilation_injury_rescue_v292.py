"""v29.2 adversarial gate for airway-dilation laceration/rupture rescue."""
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
        if any(term in hay for term in ("airway dilation", "balloon dilation", "subglottic dilation", "laryngotracheal dilation")) and "sial" not in hay:
            found.append((slug, op))
    return found


STOP_RESCUE = (
    ("stop further dilation", "stop dilation"),
    ("controlled rescue airway", "controlled alternative airway"),
    ("direct visualization", "bronchoscopic"),
)
DEFINE_INJURY = (
    ("bronchoscopy", "endoscopic inspection"),
    ("ct neck chest", "ct neck and chest"),
    ("pneumomediastinum",),
    ("pneumothorax",),
)
VENTILATION = (
    ("avoid repeated blind", "blind traumatic instrumentation"),
    ("cuff distal", "distal to the injury"),
    ("bronchoscopic", "direct guidance"),
)
ESCALATION = (
    ("tension pneumothorax",),
    ("immediate pleural decompression", "pleural decompression"),
    ("conservative", "nonoperatively"),
    ("full thickness", "enlarging disruption"),
    ("mediastinitis",),
    ("endoscopic stenting", "endoscopic closure", "operative repair", "reconstruction"),
)
POSTOP = (
    ("work of breathing",),
    ("oxygen requirement", "hypoxemia"),
    ("crepitus", "emphysema"),
    ("restenosis", "granulation"),
)
SOURCE_GROUPS = (
    ("cummings",),
    ("k j lee", "lee's essential"),
    ("pasha",),
    ("bae", "tracheobronchial laceration"),
    ("heyes", "tracheal rupture"),
    ("front surg", "state of art"),
)


def main():
    fd, db = tempfile.mkstemp(prefix="ent_or_airway_dilation_", suffix=".db")
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
            failures.append("no live airway-dilation case resolved")
        for slug, op in found:
            if not op.get("airway_dilation_injury_rescue_v292"):
                failures.append(f"{slug}: v29.2 production marker absent")
                continue
            postop = "\n".join(str(x) for x in (op.get("postop") or []))
            sources = "\n".join(str(x) for x in (op.get("sources") or []))
            if not has_groups(postop, STOP_RESCUE):
                failures.append(f"{slug}: stop/rescue-airway choreography incomplete")
            if not has_groups(postop, DEFINE_INJURY):
                failures.append(f"{slug}: bronchoscopy/CT injury-definition pathway incomplete")
            if not has_groups(postop, VENTILATION):
                failures.append(f"{slug}: controlled ventilation bailout incomplete")
            if not has_groups(postop, ESCALATION):
                failures.append(f"{slug}: pleural emergency/repair escalation incomplete")
            if not has_groups(postop, POSTOP):
                failures.append(f"{slug}: post-rescue surveillance incomplete")
            if not has_groups(sources, SOURCE_GROUPS):
                failures.append(f"{slug}: source provenance incomplete")
            r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
            if r.status_code >= 500:
                failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
            body = norm(r.get_data(as_text=True))
            for concept in ("stop further dilation", "bronchoscopy", "tension pneumothorax", "pleural decompression", "mediastinitis"):
                if norm(concept) not in body:
                    failures.append(f"{slug}: {concept!r} not rendered on /case-tomorrow")
        if failures:
            print("OR v29.2 AIRWAY DILATION INJURY RESCUE FAILURES")
            print("\n".join(failures))
            return 1
        print("PASS: airway-dilation stop point, bronchoscopy/CT definition, controlled ventilation, pleural rescue and repair escalation render live")
        return 0
    finally:
        try: os.remove(db)
        except OSError: pass


if __name__ == "__main__":
    raise SystemExit(main())
