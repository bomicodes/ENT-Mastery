"""v54.0: question quality loop and missed-question review.

* Report a problem: any question page or exam review can send a report
  (/api/qreport). Chiefs and attendings (or everyone when accounts are off)
  work them at /review, can pull a question from exams, and see the hardest
  questions, likely duplicates and blueprint coverage.
* Difficulty: percent of residents whose latest answer to a question was
  correct (shown once at least 3 residents have answered).
* Missed-question review: a wrong answer schedules the question back
  (1 day, then 3 and 7 days after each correct answer); it leaves the queue
  after two correct reviews in a row.
"""
import json
import math
import re
import time
from collections import Counter, defaultdict
from datetime import datetime

import db

REASONS = [
    ("key", "Answer key looks wrong"),
    ("outdated", "Outdated / guideline changed"),
    ("ambiguous", "Ambiguous or two defensible answers"),
    ("image", "Image problem"),
    ("typo", "Typo or formatting"),
    ("other", "Other"),
]
REVIEW_STEPS_DAYS = [1, 3, 7]
DAY = 86400

# Published ABOto-derived content weights (ABMS-Singapore 2024 MCQ exam, which states it follows the ABOto
# blueprint), mapped onto ENT Mastery's domains. Head and Neck (19%) is split across oncology and
# thyroid/parathyroid/salivary; Rhinology (16%) + Allergy (6.5%) map to one domain.
BLUEPRINT_SOURCE = ("ABMS-Singapore Otorhinolaryngology MCQ Examination 2024 content outline, which states it is consistent "
                    "with the ABOto blueprint (Allergy 6.5, Head and Neck 19, Laryngology 8, Otology 19, Pediatrics 15, "
                    "Plastic and Reconstructive 9, Rhinology 16, Sleep 7.5).")
BLUEPRINT_URL = "https://healthprofessionals.gov.sg/sab/specialist-examination/otorhinolaryngology-examination-(2024)/examination-content"
BLUEPRINT = {
    "Otology / Neurotology": 19.0,
    "Rhinology / Allergy / Skull Base": 22.5,
    "Head & Neck Oncology": 12.0,
    "Thyroid / Parathyroid / Salivary": 7.0,
    "Pediatric Otolaryngology": 15.0,
    "Laryngology / Voice / Swallowing": 8.0,
    "Facial Plastics / Trauma": 9.0,
    "Sleep Surgery": 7.5,
    "General ENT / Emergencies": 0.0,
}


# --------------------------------------------------------------------------- storage
def ensure_schema():
    c = db.conn()
    pk = "BIGSERIAL PRIMARY KEY" if db.USE_POSTGRES else "INTEGER PRIMARY KEY AUTOINCREMENT"
    c.execute(f"""CREATE TABLE IF NOT EXISTS question_reports (
        id {pk}, user_id INTEGER, question_id TEXT NOT NULL, reason TEXT, note TEXT, created_at TEXT,
        status TEXT DEFAULT 'open', resolved_by INTEGER, resolution TEXT, resolved_at TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS question_admin (
        question_id TEXT PRIMARY KEY, paused INTEGER DEFAULT 0, note TEXT, updated_at TEXT)""")
    c.execute("""CREATE TABLE IF NOT EXISTS missed_review (
        user_id INTEGER NOT NULL, question_id TEXT NOT NULL, due_at REAL, streak INTEGER DEFAULT 0,
        misses INTEGER DEFAULT 1, updated_at TEXT, PRIMARY KEY (user_id, question_id))""")
    c.commit()
    c.close()


def _rows(sql, params=()):
    c = db.conn()
    try:
        return [dict(r) for r in db._execute(c, sql, params).fetchall()]
    finally:
        c.close()


def _run(sql, params=()):
    c = db.conn()
    try:
        db._execute(c, sql, params)
        c.commit()
    finally:
        c.close()


def paused_ids():
    try:
        return {r["question_id"] for r in _rows("SELECT question_id FROM question_admin WHERE paused=1")}
    except Exception:
        return set()


def record_review_answer(uid, qid, correct):
    """Update the missed-question queue after any bank or exam answer."""
    now = time.time()
    cur = _rows("SELECT * FROM missed_review WHERE user_id=? AND question_id=?", (uid, qid))
    stamp = datetime.now().isoformat(timespec="seconds")
    if not correct:
        if cur:
            _run("UPDATE missed_review SET due_at=?, streak=0, misses=misses+1, updated_at=? WHERE user_id=? AND question_id=?",
                 (now + REVIEW_STEPS_DAYS[0] * DAY, stamp, uid, qid))
        else:
            _run("INSERT INTO missed_review (user_id,question_id,due_at,streak,misses,updated_at) VALUES (?,?,?,?,?,?)",
                 (uid, qid, now + REVIEW_STEPS_DAYS[0] * DAY, 0, 1, stamp))
        return
    if not cur:
        return
    streak = (cur[0]["streak"] or 0) + 1
    if streak >= 2:
        _run("DELETE FROM missed_review WHERE user_id=? AND question_id=?", (uid, qid))
    else:
        _run("UPDATE missed_review SET due_at=?, streak=?, updated_at=? WHERE user_id=? AND question_id=?",
             (now + REVIEW_STEPS_DAYS[min(streak, len(REVIEW_STEPS_DAYS) - 1)] * DAY, streak, stamp, uid, qid))


def due_reviews(uid, now=None):
    now = now or time.time()
    rows = _rows("SELECT question_id, due_at, misses FROM missed_review WHERE user_id=? ORDER BY due_at", (uid,))
    due = [r["question_id"] for r in rows if (r["due_at"] or 0) <= now]
    return {"due": due, "queued": len(rows), "next_at": min((r["due_at"] for r in rows if (r["due_at"] or 0) > now), default=None)}


def difficulty_map():
    """{qid: (pct_correct, n_users)} from each user's latest answer."""
    latest = {}
    for r in _rows("SELECT user_id, source_id, score FROM mastery_events WHERE source_type='clinical_challenge' ORDER BY id"):
        latest[(r["user_id"], r["source_id"])] = (r["score"] or 0) >= 2
    agg = defaultdict(lambda: [0, 0])
    for (u, q), ok in latest.items():
        agg[q][0] += ok
        agg[q][1] += 1
    return {q: (round(100 * ok / n), n) for q, (ok, n) in agg.items()}


# --------------------------------------------------------------------------- duplicates
_WORD = re.compile(r"[a-z][a-z0-9\-]{2,}")
_STOP = set("the and with for that this what which most best next from into have has are was were his her their than then a an of to in on is be by or as at it its after before patient year old man woman child shows show who whom".split())


def _tokens(text):
    return [w for w in _WORD.findall((text or "").lower()) if w not in _STOP]


def near_duplicates(bank, threshold=0.62, limit=80):
    """Cosine similarity on stem TF-IDF within each domain; returns the closest pairs."""
    docs = {q["id"]: Counter(_tokens(q.get("stem", ""))) for q in bank}
    df = Counter(w for c in docs.values() for w in c)
    n = len(docs)
    vec = {}
    for qid, c in docs.items():
        v = {w: (1 + math.log(f)) * math.log(n / df[w]) for w, f in c.items()}
        norm = math.sqrt(sum(x * x for x in v.values())) or 1
        vec[qid] = {w: x / norm for w, x in v.items()}
    by_topic = defaultdict(list)
    for q in bank:
        by_topic[q.get("domain")].append(q["id"])
    pairs = []
    for ids in by_topic.values():
        for i in range(len(ids)):
            a = vec[ids[i]]
            for j in range(i + 1, len(ids)):
                b = vec[ids[j]]
                if len(a) > len(b):
                    s = sum(x * a.get(w, 0) for w, x in b.items())
                else:
                    s = sum(x * b.get(w, 0) for w, x in a.items())
                if s >= threshold:
                    pairs.append((round(s, 2), ids[i], ids[j]))
    pairs.sort(reverse=True)
    return pairs[:limit], len(pairs)


def coverage(bank, canon):
    board = [q for q in bank if q.get("tier") == "Curated board-style"]
    per_dom = Counter(canon(q.get("domain")) for q in board)
    total = sum(per_dom.values()) or 1
    rows = []
    for d, w in BLUEPRINT.items():
        have = per_dom.get(d, 0)
        share = round(100 * have / total, 1)
        rows.append({"domain": d, "blueprint": w, "have": have, "share": share, "gap": round(share - w, 1)})
    topics = Counter((canon(q.get("domain")), q.get("topic")) for q in board)
    all_topics = Counter((canon(q.get("domain")), q.get("topic")) for q in bank)
    thin = sorted(((d, t, topics.get((d, t), 0), n) for (d, t), n in all_topics.items() if topics.get((d, t), 0) < 3),
                  key=lambda r: (r[2], r[0], str(r[1])))
    return rows, thin


# --------------------------------------------------------------------------- install
def install_quality_v540(app, data, app_mod=None):
    from flask import render_template, request, redirect, url_for, jsonify, session, abort
    import os

    ensure_schema()
    bank = data.CLINICAL_CHALLENGES_V119
    by_id = data.CLINICAL_CHALLENGE_BY_ID_V119
    src = app_mod if app_mod is not None else data
    canon = getattr(src, "canonical_domain_v94", None) or getattr(data, "canonical_domain_v94", lambda d: d)

    def uid():
        return db._current_user_id()

    def privileged():
        if os.environ.get("ENT_MASTERY_AUDIT_MODE") == "1":
            return True
        try:
            from accounts_v444 import PRIVILEGED_ROLES, _gate_enabled
            if not _gate_enabled():
                return True
            return (session.get("user_role") or "") in PRIVILEGED_ROLES
        except Exception:
            return True

    def api_qreport():
        p = request.get_json(force=True) or {}
        qid = str(p.get("qid", ""))
        if qid not in by_id:
            return jsonify({"ok": False, "error": "unknown question"}), 404
        reason = p.get("reason") if p.get("reason") in dict(REASONS) else "other"
        _run("INSERT INTO question_reports (user_id,question_id,reason,note,created_at,status) VALUES (?,?,?,?,?,?)",
             (uid(), qid, reason, (p.get("note") or "")[:2000], datetime.now().isoformat(timespec="minutes"), "open"))
        return jsonify({"ok": True})

    def api_qstats(qid):
        d = difficulty_map().get(qid)
        return jsonify({"ok": True, "pct": d[0] if d and d[1] >= 3 else None, "n": d[1] if d else 0})

    def review_home():
        if not privileged():
            abort(403)
        reports = _rows("SELECT * FROM question_reports WHERE status='open' ORDER BY id DESC")
        grouped = defaultdict(list)
        for r in reports:
            grouped[r["question_id"]].append(r)
        names = {}
        try:
            for u in _rows("SELECT id, name FROM users"):
                names[u["id"]] = u.get("name")
        except Exception:
            pass
        paused = paused_ids()
        diff = difficulty_map()
        open_items = []
        for qid, rs in sorted(grouped.items(), key=lambda kv: -len(kv[1])):
            q = by_id.get(qid, {})
            open_items.append({"qid": qid, "q": q, "reports": rs, "paused": qid in paused, "diff": diff.get(qid),
                               "names": names})
        hardest = sorted(((v[0], v[1], k) for k, v in diff.items() if v[1] >= 3), key=lambda t: (t[0], -t[1]))[:25]
        hardest = [{"pct": p, "n": n, "q": by_id.get(k, {"id": k})} for p, n, k in hardest]
        resolved = _rows("SELECT * FROM question_reports WHERE status!='open' ORDER BY id DESC LIMIT 20")
        return render_template("review_v540.html", open_items=open_items, hardest=hardest, resolved=resolved,
                               reasons=dict(REASONS), paused=[by_id.get(p, {"id": p}) for p in sorted(paused)],
                               tab="queue")

    def review_action(rid):
        if not privileged():
            abort(403)
        action = request.form.get("action")
        qid = request.form.get("qid", "")
        note = (request.form.get("resolution") or "")[:2000]
        stamp = datetime.now().isoformat(timespec="minutes")
        if action in ("resolved", "dismissed"):
            _run("UPDATE question_reports SET status=?, resolved_by=?, resolution=?, resolved_at=? WHERE question_id=? AND status='open'",
                 (action, uid(), note, stamp, qid))
        if action in ("pause", "unpause"):
            cur = _rows("SELECT * FROM question_admin WHERE question_id=?", (qid,))
            val = 1 if action == "pause" else 0
            if cur:
                _run("UPDATE question_admin SET paused=?, note=?, updated_at=? WHERE question_id=?", (val, note, stamp, qid))
            else:
                _run("INSERT INTO question_admin (question_id,paused,note,updated_at) VALUES (?,?,?,?)", (qid, val, note, stamp))
        return redirect(url_for("review_home_v540") + "#" + qid)

    def review_coverage():
        if not privileged():
            abort(403)
        rows, thin = coverage(bank, canon)
        pairs, total_pairs = near_duplicates(bank)
        pairs = [{"s": s, "a": by_id.get(a, {"id": a}), "b": by_id.get(b, {"id": b})} for s, a, b in pairs]
        return render_template("review_coverage_v540.html", rows=rows, thin=thin[:150], thin_total=len(thin),
                               pairs=pairs, total_pairs=total_pairs, source=BLUEPRINT_SOURCE, source_url=BLUEPRINT_URL,
                               tab="coverage")

    def review_start():
        """Start a tutor-mode block of the user's due missed questions."""
        d = due_reviews(uid())
        ids = [q for q in d["due"] if q in by_id]
        if not ids:
            return redirect(url_for("progress"))
        return render_template("review_start_v540.html", ids=",".join(ids[:60]), n=min(len(ids), 60))

    # Wrap the single-question answer API so misses enter the review queue.
    orig_api = app.view_functions.get("api_clinical_challenge")

    def api_clinical_challenge_v540():
        resp = orig_api()
        try:
            payload = request.get_json(silent=True) or {}
            body = resp.get_json() if hasattr(resp, "get_json") else None
            if body and body.get("ok"):
                record_review_answer(uid(), str(payload.get("qid", "")), bool(body.get("correct")))
        except Exception:
            pass
        return resp

    app.jinja_env.globals["due_reviews_v540"] = lambda: due_reviews(uid())
    app.jinja_env.globals["qreport_reasons_v540"] = REASONS
    app.jinja_env.globals["is_reviewer_v540"] = privileged
    data.QUALITY_V540 = {"blueprint": BLUEPRINT, "paused_ids": paused_ids, "record_review_answer": record_review_answer,
                         "due_reviews": due_reviews, "difficulty_map": difficulty_map}

    routes = [
        ("/api/qreport", "qreport_v540", api_qreport, ["POST"]),
        ("/api/qstats/<qid>", "qstats_v540", api_qstats, ["GET"]),
        ("/review", "review_home_v540", review_home, ["GET"]),
        ("/review/coverage", "review_coverage_v540", review_coverage, ["GET"]),
        ("/review/<int:rid>/action", "review_action_v540", review_action, ["POST"]),
        ("/review/missed", "review_start_v540", review_start, ["GET"]),
    ]
    served = getattr(app, "_got_first_request", False)
    if served:
        app._got_first_request = False
    try:
        for rule, name, fn, methods in routes:
            if name not in app.view_functions:
                app.add_url_rule(rule, name, fn, methods=methods)
        if orig_api is not None:
            app.view_functions["api_clinical_challenge"] = api_clinical_challenge_v540
    finally:
        if served:
            app._got_first_request = True
    return {"routes": [r[0] for r in routes]}
