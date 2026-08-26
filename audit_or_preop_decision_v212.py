"""Hard gate for v21.2-v21.6 OR Tomorrow decisions and procedure-specific anatomy."""
import os
import tempfile

fd, db = tempfile.mkstemp(prefix="ent_or_preop_decision_v216_", suffix=".db")
os.close(fd)
os.environ.pop("DATABASE_URL", None)
os.environ["SQLITE_PATH"] = db
os.environ.pop("ENT_MASTERY_ACCESS_PASSWORD", None)

CHECKS = [
    (("superficial parotid",), ("baseline facial", "deep-lobe/parapharyngeal", "nodal disease"), "preop_decision_v212"),
    (("total parotid",), ("baseline facial-nerve", "nerve sacrifice/reconstruction", "deep lobe/parapharyngeal"), "preop_decision_v212"),
    (("submandibular gland",), ("inflammatory/stone disease versus neoplasm", "tongue mobility/sensation", "oncologic neck"), "preop_decision_v212"),
    (("sialendosc",), ("stone size", "combined approach", "lingual-nerve risk"), "preop_decision_v212"),
    (("jugular foramen",), ("cn ix-xii", "aspiration status", "vascular imaging"), "preop_decision_v212"),
    (("translabyrinthine",), ("hearing-sacrificing", "preoperative hearing status", "csf-leak closure"), "preop_decision_v212"),
    (("retrosigmoid",), ("serviceable hearing", "lower-cranial-nerve status", "hearing-preservation intent"), "preop_decision_v212"),
    (("middle fossa",), ("hearing-preservation", "geniculate/facial-nerve", "petrous-carotid"), "preop_decision_v212"),
    (("conservation", "laryng"), ("cricoarytenoid unit", "pulmonary reserve", "swallowing/aspiration", "appropriate margins"), "preop_decision_v213"),
    (("transoral", "laser", "laryngeal"), ("completely exposed transorally", "anterior-commissure", "unsafe deep/cartilage margins"), "preop_decision_v213"),
    (("supraglottoplasty",), ("feeding/aspiration history", "synchronous lesions", "postoperative level of care"), "preop_decision_v213"),
    (("laryngotracheal", "cleft"), ("cleft type/length", "aspiration physiology", "open-versus-endoscopic"), "preop_decision_v213"),
    (("direct laryngoscopy", "bronch"), ("spontaneous versus controlled ventilation", "rescue strategy", "critical stenosis"), "preop_decision_v213"),
    (("tracheal", "resection"), ("tension-free resection", "innominate", "release maneuvers", "backup airway"), "preop_decision_v213"),
]

LANDMARK_CHECKS = [
    (("superficial parotid",), "landmarks_v214", ("facial nerve trunk", "tragal pointer", "tympanomastoid", "posterior belly of digastric", "retromandibular vein"), ("lingual nerve", "hypoglossal nerve", "wharton")),
    (("total parotid",), "landmarks_v214", ("facial nerve trunk", "pes anserinus", "retromandibular vein", "deep lobe/parapharyngeal"), ("lingual nerve", "hypoglossal nerve", "wharton")),
    (("submandibular gland",), "landmarks_v214", ("marginal mandibular", "facial artery", "lingual nerve", "wharton duct", "hypoglossal nerve"), ("retromandibular vein", "stensen duct")),
    (("sialendosc",), "landmarks_v214", ("duct papilla", "branch-point", "wharton duct", "stensen duct"), ()),
    (("total", "laryngectomy"), "landmarks_v215", ("hyoid", "pyriform", "permanent tracheal stoma", "carotid sheath"), ("thoracic duct", "marginal mandibular")),
    (("neck", "dissection"), "landmarks_v215", ("spinal accessory", "internal jugular", "hypoglossal", "phrenic", "thoracic duct"), ("pre-epiglottic", "wharton")),
    (("oral", "composite"), "landmarks_v215", ("lingual nerve", "hypoglossal", "lingual artery", "wharton", "mylohyoid"), ("thoracic duct", "tragal pointer")),
    (("conservation", "laryng"), "landmarks_v215", ("anterior commissure", "pre-epiglottic", "paraglottic", "cricoarytenoid", "pyriform"), ("thoracic duct", "marginal mandibular")),
    (("staped",), "landmarks_v216", ("lenticular", "footplate", "pyramidal eminence", "tympanic segment of the facial nerve", "chorda tympani"), ("sigmoid sinus", "tegmen")),
    (("cochlear", "implant"), "landmarks_v216", ("sigmoid sinus", "lateral semicircular canal", "incus", "mastoid segment of the facial nerve", "chorda tympani", "round-window"), ("stapes head", "pyramidal eminence")),
    (("cholesteat",), "landmarks_v216", ("tegmen", "sigmoid sinus", "lateral semicircular canal", "facial nerve", "antrum", "sinus tympani"), ("wharton", "tragal pointer")),
]


def _find(reg, terms):
    for slug, op in reg.items():
        hay = (str(slug) + " " + str((op or {}).get("title", ""))).lower()
        if all(term in hay for term in terms):
            return slug, op
    return None, None

try:
    import runtime_entry as rt
    reg = rt.data.OR_PREP_REGISTRY
    failures = []
    client = rt.app.test_client()

    for title_terms, required, marker in CHECKS:
        slug, op = _find(reg, title_terms)
        label = "/".join(title_terms)
        if not op:
            failures.append(f"{label}: live OR module not found")
            continue
        if not op.get(marker):
            failures.append(f"{slug}: {marker} missing")
        setup = " ".join(str(x) for x in (op.get("setup") or [])).lower()
        for term in required:
            if term not in setup:
                failures.append(f"{slug}: setup missing {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: /case-tomorrow HTTP {r.status_code}")

    for title_terms, marker, required, forbidden in LANDMARK_CHECKS:
        slug, op = _find(reg, title_terms)
        label = "/".join(title_terms)
        if not op:
            failures.append(f"{label}: landmark module not found")
            continue
        if op.get(marker) != "procedure-specific":
            failures.append(f"{slug}: {marker} procedure-specific landmark marker missing")
        landmarks = " ".join(str(x) for x in (op.get("landmarks") or [])).lower()
        for term in required:
            if term not in landmarks:
                failures.append(f"{slug}: landmarks missing {term!r}")
        for term in forbidden:
            if term in landmarks:
                failures.append(f"{slug}: landmarks retain irrelevant family anatomy {term!r}")
        r = client.get("/case-tomorrow", query_string={"q": op.get("title", slug)}, follow_redirects=True)
        if r.status_code >= 500:
            failures.append(f"{slug}: landmark page /case-tomorrow HTTP {r.status_code}")

    if failures:
        print("OR DECISION/ANATOMY v21.2-v21.6 FAILURES")
        print("\n".join(failures))
        raise SystemExit(1)

    print(f"PASS: {len(CHECKS)} decision modules and {len(LANDMARK_CHECKS)} procedure-specific anatomy modules are live")
finally:
    try:
        os.remove(db)
    except OSError:
        pass
