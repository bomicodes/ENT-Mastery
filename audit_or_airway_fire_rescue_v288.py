"""v28.8 adversarial gate for shared-airway fire prevention and rescue."""
import os, re, tempfile


def norm(s):
    return re.sub(r"[^a-z0-9]+", " ", str(s).lower()).strip()


def has_groups(text, groups):
    t = norm(text)
    return all(any(norm(term) in t for term in group) for group in groups)


def resolve(reg, preferred, aliases):
    if preferred in reg:
        return preferred, reg[preferred]
    for slug, op in reg.items():
        hay = norm(str(slug) + " " + str((op or {}).get("title", "")))
        if any(norm(alias) in hay for alias in aliases):
            return slug, op
    return None, None


TARGETS = [
    ("microflap", ("microflap",)),
    ("rrp-debridement", ("rrp", "papilloma")),
]

PREVENTION_GROUPS = (
    ("lowest oxygen", "minimum oxygen", "lowest oxygen concentration"),
    ("nitrous oxide", "n2o"),
    ("laser resistant", "laser-resistant"),
    ("wet pledget", "wet pledgets"),
    ("not fire proof", "not fire-proof"),
)
FIRE_RESPONSE_GROUPS = (
    ("announce the fire", "airway fire"),
    ("stop laser", "stop energy", "cease energy"),
    ("stop oxidizer", "stops oxidizer", "disconnects oxidizer", "stop oxygen"),
    ("remove the burning endotracheal tube", "remove burning tube", "burning endotracheal tube"),
    ("saline", "water"),
)
POST_FIRE_GROUPS = (
    ("bronchoscopy",),
    ("fragment", "debris"),
    ("thermal injury", "mucosal injury"),
    ("surgical airway", "controlled airway"),
    ("critical care", "postoperative monitoring"),
)
SOURCE_GROUPS = (
    ("cummings",),
    ("k j lee", "lee's essential"),
    ("pasha",),
    ("american society of anesthesiologists", "asa"),
    ("anesthesia patient safety foundation", "apsf"),
    ("beaulieu", "fire risks in airway procedures"),
)


def main():
    fd, db = tempfile.mkstemp(prefix="ent_or_airway_fire_", suffix=".db")
    os.close(fd)
    os.environ.pop("DATABASE_URL", None)
    os.environ["SQLITE_PATH"] = db
    os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)
    try:
        import runtime_entry_pasha as prod
        reg = prod.runtime_entry.data.OR_PREP_REGISTRY
        client = prod.app.test_client()
        failures = []
        resolved = 0
        for preferred, aliases in TARGETS:
            slug, op = resolve(reg, preferred, aliases)
            if not op:
                failures.append(f"{preferred}: no live case resolved")
                continue
            resolved += 1
            if not op.get("airway_fire_rescue_v288"):
                failures.append(f"{slug}: v28.8 production marker absent")
            setup = "\n".join(str(x) for x in (op.get("setup") or []))
            steps = "\n".join(str(x) for x in (op.get("steps") or []))
            postop = "\n".join(str(x) for x in (op.get("postop") or []))
            sources = "\n".join(str(x) for x in (op.get("sources") or []))
            if not has_groups(setup, PREVENTION_GROUPS):
                failures.append(f"{slug}: prevention/fire-triangle choreography incomplete")
            if not has_groups(steps, FIRE_RESPONSE_GROUPS):
                failures.append(f"{slug}: immediate airway-fire rescue choreography incomplete")
            if not has_groups(postop, POST_FIRE_GROUPS):
                failures.append(f"{slug}: post-fire airway assessment/bailout incomplete")
            if not has_groups(sources, SOURCE_GROUPS):
                failures.append(f"{slug}: airway-fire source provenance incomplete")
            r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
            if r.status_code >= 500:
                failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")
            body = norm(r.get_data(as_text=True))
            if "airway fire" not in body or "bronchoscopy" not in body:
                failures.append(f"{slug}: v28.8 rescue not rendered on /case-tomorrow")
        if resolved != len(TARGETS):
            failures.append(f"resolved {resolved}/{len(TARGETS)} live airway-fire targets")
        if failures:
            print("OR v28.8 AIRWAY FIRE RESCUE FAILURES")
            print("\n".join(failures))
            return 1
        print("PASS: shared-airway fire prevention, immediate extinguishment, tube/oxidizer control, bronchoscopy and airway-rescue decisions render live")
        return 0
    finally:
        try: os.remove(db)
        except OSError: pass


if __name__ == "__main__":
    raise SystemExit(main())
