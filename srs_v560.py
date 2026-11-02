"""v56.0: spaced-repetition flashcards ("Cards").

Every board-style question, image question, tracing question and concept check is a card:
front = the stem (commit to an answer in your head), back = the correct answer, the board pearl and
the core of the explanation. Scheduling is per card and per user, with an Anki-style SM-2 variant:

  new / learning   Again -> 1 min, Hard -> 6 min, Good -> 1 day (graduate), Easy -> 4 days
  review           Again -> lapse: relearn in 10 min, ease -0.20, next interval about 25% of the old one
                   Hard  -> interval x 1.2, ease -0.15
                   Good  -> interval x ease
                   Easy  -> interval x ease x 1.3, ease +0.15
  ease starts at 2.5, floor 1.3; intervals are capped at 180 days and by the exam-date cap below.

Exam date: when set, no interval may push a card past the exam. The cap is about 45% of the days
left, so each card is seen at least once more before the exam, and reviews tighten as it nears.

Answers anywhere on the site feed the same schedule (quality_v540.record_review_answer is wrapped):
a miss is treated as Again, a correct answer as Good, so everything you have studied stays in rotation.

New cards per day are limited (default 20). They are drawn from your weakest domains first, then
interleaved across domains, with questions you have missed always enrolled immediately.
"""
import html
import json
import random
import re
import time
from datetime import datetime, timedelta, timezone

import db

DAY = 86400.0
MIN = 60.0
TZ_NAME = "America/Chicago"
DAY_CUTOFF_HOUR = 4
MAX_INTERVAL = 180.0
RATINGS = {1: "again", 2: "hard", 3: "good", 4: "easy"}


# ------------------------------------------------------------------------------------- storage
def ensure_schema():
    c = db.conn()
    pk = "BIGSERIAL PRIMARY KEY" if db.USE_POSTGRES else "INTEGER PRIMARY KEY AUTOINCREMENT"
    c.execute("""CREATE TABLE IF NOT EXISTS srs_cards (
        user_id INTEGER NOT NULL, card_id TEXT NOT NULL, state TEXT NOT NULL DEFAULT 'new',
        ease REAL DEFAULT 2.5, interval_days REAL DEFAULT 0, due_at REAL DEFAULT 0, reps INTEGER DEFAULT 0,
        lapses INTEGER DEFAULT 0, last_review REAL, relearn_interval REAL DEFAULT 0, introduced_at REAL,
        PRIMARY KEY (user_id, card_id))""")
    c.execute(f"""CREATE TABLE IF NOT EXISTS srs_log (
        id {pk}, user_id INTEGER NOT NULL, card_id TEXT NOT NULL, rating INTEGER, source TEXT,
        was_new INTEGER DEFAULT 0, interval_days REAL, ts REAL)""")
    c.execute("""CREATE TABLE IF NOT EXISTS srs_settings (
        user_id INTEGER PRIMARY KEY, exam_date TEXT, new_per_day INTEGER DEFAULT 20,
        sources TEXT DEFAULT 'board,image,check', domains TEXT DEFAULT '', updated_at TEXT)""")
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


def _tz():
    try:
        from zoneinfo import ZoneInfo
        return ZoneInfo(TZ_NAME)
    except Exception:
        return timezone(timedelta(hours=-6))


def day_start(now=None):
    """Start of the current study day (4 am local) as a unix timestamp."""
    now = now or time.time()
    local = datetime.fromtimestamp(now, _tz())
    start = local.replace(hour=DAY_CUTOFF_HOUR, minute=0, second=0, microsecond=0)
    if local < start:
        start -= timedelta(days=1)
    return start.timestamp()


# ------------------------------------------------------------------------------------- settings
DEFAULT_SETTINGS = {"exam_date": "", "new_per_day": 20, "sources": "board,image,check", "domains": ""}


def get_settings(uid):
    r = _rows("SELECT * FROM srs_settings WHERE user_id=?", (uid,))
    s = dict(DEFAULT_SETTINGS)
    if r:
        for k in s:
            if r[0].get(k) not in (None,):
                s[k] = r[0][k]
    s["new_per_day"] = max(0, min(200, int(s.get("new_per_day") or 0)))
    return s


def save_settings(uid, exam_date, new_per_day, sources, domains):
    stamp = datetime.now().isoformat(timespec="seconds")
    if _rows("SELECT user_id FROM srs_settings WHERE user_id=?", (uid,)):
        _run("UPDATE srs_settings SET exam_date=?, new_per_day=?, sources=?, domains=?, updated_at=? WHERE user_id=?",
             (exam_date, new_per_day, sources, domains, stamp, uid))
    else:
        _run("INSERT INTO srs_settings (user_id, exam_date, new_per_day, sources, domains, updated_at) VALUES (?,?,?,?,?,?)",
             (uid, exam_date, new_per_day, sources, domains, stamp))


def exam_ts(settings):
    d = (settings.get("exam_date") or "").strip()
    if not d:
        return None
    try:
        dt = datetime.strptime(d, "%Y-%m-%d").replace(hour=8, tzinfo=_tz())
        return dt.timestamp()
    except ValueError:
        return None


# ------------------------------------------------------------------------------------- scheduler
def _fuzz(days):
    if days < 2.5:
        return days
    return days * random.uniform(0.95, 1.05)


def _cap(days, now, exam):
    days = min(days, MAX_INTERVAL)
    if exam and exam > now:
        left = (exam - now) / DAY
        days = min(days, max(1.0, left * 0.45))
    return max(days, 0.0)


def schedule(card, rating, now=None, exam=None):
    """Return the updated card dict for a rating 1-4. Pure function (no I/O)."""
    now = now or time.time()
    c = dict(card)
    state = c.get("state") or "new"
    ease = float(c.get("ease") or 2.5)
    ivl = float(c.get("interval_days") or 0)
    c["reps"] = int(c.get("reps") or 0) + 1
    c["last_review"] = now
    if state in ("new", "learning"):
        if rating == 1:
            c.update(state="learning", due_at=now + 1 * MIN, interval_days=0)
        elif rating == 2:
            c.update(state="learning", due_at=now + 6 * MIN, interval_days=0)
        elif rating == 3:
            d = _cap(1.0, now, exam)
            c.update(state="review", interval_days=d, due_at=now + d * DAY)
        else:
            d = _cap(4.0, now, exam)
            c.update(state="review", interval_days=d, due_at=now + d * DAY, ease=min(3.5, ease + 0.15))
    elif state == "relearning":
        if rating in (1, 2):
            c.update(due_at=now + (1 if rating == 1 else 6) * MIN)
        else:
            d = _cap(max(1.0, float(c.get("relearn_interval") or 1.0)) * (1.3 if rating == 4 else 1.0), now, exam)
            c.update(state="review", interval_days=d, due_at=now + d * DAY)
    else:  # review
        # credit for reviewing late: use the actual elapsed time when it is longer than planned
        last = float(c.get("last_review_prev") or 0) or (now - ivl * DAY)
        elapsed = max(ivl, (now - last) / DAY) if last else ivl
        if rating == 1:
            ease = max(1.3, ease - 0.20)
            c.update(state="relearning", lapses=int(c.get("lapses") or 0) + 1, ease=ease,
                     relearn_interval=max(1.0, ivl * 0.25), due_at=now + 10 * MIN, interval_days=0)
        else:
            if rating == 2:
                ease = max(1.3, ease - 0.15)
                d = max(ivl + 1, ivl * 1.2)
            elif rating == 3:
                d = max(ivl + 1, (ivl + (elapsed - ivl) / 2) * ease)
            else:
                ease = min(3.5, ease + 0.15)
                d = max(ivl + 2, (ivl + (elapsed - ivl)) * ease * 1.3)
            d = _cap(_fuzz(d), now, exam)
            c.update(state="review", ease=ease, interval_days=d, due_at=now + d * DAY)
    return c


def preview_intervals(card, now=None, exam=None):
    """Human labels for what each button would do (shown under the buttons)."""
    out = {}
    random_state = random.getstate()
    for r in (1, 2, 3, 4):
        n = schedule(card, r, now, exam)
        secs = n["due_at"] - (now or time.time())
        out[r] = _fmt(secs)
    random.setstate(random_state)
    return out


def _fmt(secs):
    if secs < 3600:
        return f"{max(1, round(secs / 60))} min"
    if secs < 0.9 * DAY:
        return f"{round(secs / 3600)} h"
    d = secs / DAY
    if d < 30:
        return f"{round(d)} d"
    if d < 365:
        return f"{d / 30:.1f} mo"
    return f"{d / 365:.1f} y"


# ------------------------------------------------------------------------------------- card content
_TAG = re.compile(r"<[^>]+>")


def _clean(t):
    return html.unescape(_TAG.sub("", str(t or ""))).strip()


def _first_sentences(t, n=3, limit=520):
    t = _clean(t)
    parts = re.split(r"(?<=[.!?])\s+", t)
    out = " ".join(parts[:n])
    return out if len(out) <= limit else out[:limit].rsplit(" ", 1)[0] + "…"


class Catalog:
    """All cards available on the site, built once from the in-memory banks."""

    def __init__(self, data, paused=lambda: set()):
        self.data = data
        self.paused = paused
        self.cards = {}
        self.order = []
        bank = getattr(data, "CLINICAL_CHALLENGES_V119", []) or []
        for q in bank:
            qid = q.get("id")
            if not qid or not q.get("choices") or q.get("answer") is None:
                continue
            board = q.get("tier") == "Curated board-style"
            if qid.startswith("img_") or q.get("image_url") or q.get("figure_html") or q.get("figure_static"):
                kind = "image"
            elif board:
                kind = "board"
            else:
                continue  # templated coverage items are not carded
            self._add("q:" + qid, kind, q)
        for q in getattr(data, "CONCEPT_CHECKS_V112", []) or []:
            if not q.get("id"):
                continue
            mcq = bool(q.get("choices")) and q.get("answer") is not None
            recall = bool(q.get("prompt") and q.get("answer_text"))
            if mcq or recall:
                self._add("cc:" + q["id"], "check", q)

    def _add(self, cid, kind, q):
        self.cards[cid] = {"id": cid, "kind": kind, "domain": q.get("domain") or "", "topic": q.get("topic") or "",
                           "concept_id": q.get("concept_id") or ""}
        self.order.append(cid)

    def source(self, cid):
        if cid.startswith("q:"):
            return (getattr(self.data, "CLINICAL_CHALLENGE_BY_ID_V119", {}) or {}).get(cid[2:])
        if cid.startswith("cc:"):
            idx = getattr(self.data, "CONCEPT_CHECK_BY_ID_V112", None)
            if idx is None:
                idx = {q.get("id"): q for q in getattr(self.data, "CONCEPT_CHECKS_V112", [])}
                self.data.CONCEPT_CHECK_BY_ID_V112 = idx
            return idx.get(cid[3:])
        return None

    def render(self, cid):
        meta = self.cards.get(cid)
        q = self.source(cid)
        if not meta or not q:
            return None
        choices = list(q.get("choices") or [])
        try:
            ans_i = int(q.get("answer"))
        except (TypeError, ValueError):
            ans_i = -1
        answer = _clean(choices[ans_i]) if 0 <= ans_i < len(choices) else _clean(q.get("answer_text"))
        link = ("/clinical-challenge/" + cid[2:]) if cid.startswith("q:") else ("/concept-check/" + cid[3:])
        return {
            "id": cid, "kind": meta["kind"], "domain": meta["domain"], "topic": _clean(q.get("answer_topic") or meta["topic"]),
            "stem": _clean(q.get("stem") or q.get("question") or q.get("prompt")),
            "image_url": q.get("image_url"), "image_credit": _clean(q.get("image_credit")),
            "figure_html": q.get("figure_html") or "",
            "figure_static": q.get("figure_static") or "",
            "answer": answer,
            "pearl": _clean(q.get("board_pearl")),
            "why": "" if (q.get("answer_text") and not choices) else _first_sentences(q.get("explanation"), 3),
            "link": link,
        }


# ------------------------------------------------------------------------------------- per-user ops
def _card_row(uid, cid):
    r = _rows("SELECT * FROM srs_cards WHERE user_id=? AND card_id=?", (uid, cid))
    return r[0] if r else None


def _save(uid, c, is_new_row):
    vals = (c.get("state"), float(c.get("ease") or 2.5), float(c.get("interval_days") or 0), float(c.get("due_at") or 0),
            int(c.get("reps") or 0), int(c.get("lapses") or 0), c.get("last_review"), float(c.get("relearn_interval") or 0))
    if is_new_row:
        _run("INSERT INTO srs_cards (state, ease, interval_days, due_at, reps, lapses, last_review, relearn_interval, "
             "introduced_at, user_id, card_id) VALUES (?,?,?,?,?,?,?,?,?,?,?)", vals + (time.time(), uid, c["card_id"]))
    else:
        _run("UPDATE srs_cards SET state=?, ease=?, interval_days=?, due_at=?, reps=?, lapses=?, last_review=?, "
             "relearn_interval=? WHERE user_id=? AND card_id=?", vals + (uid, c["card_id"]))


def rate(uid, cid, rating, source="cards", now=None):
    now = now or time.time()
    settings = get_settings(uid)
    row = _card_row(uid, cid)
    was_new = row is None or (row.get("state") == "new")
    base = row or {"card_id": cid, "state": "new", "ease": 2.5, "interval_days": 0}
    if row:
        base["last_review_prev"] = row.get("last_review")
    nxt = schedule(base, int(rating), now, exam_ts(settings))
    nxt["card_id"] = cid
    _save(uid, nxt, row is None)
    _run("INSERT INTO srs_log (user_id, card_id, rating, source, was_new, interval_days, ts) VALUES (?,?,?,?,?,?,?)",
         (uid, cid, int(rating), source, 1 if was_new else 0, float(nxt.get("interval_days") or 0), now))
    return nxt


def record_answer(uid, qid, correct):
    """Hook for answers given anywhere on the site (bank, exams, tutor blocks)."""
    if not uid or not qid:
        return
    cid = "q:" + qid
    row = _card_row(uid, cid)
    if correct and row and row.get("state") in ("review",) and float(row.get("due_at") or 0) > time.time():
        return  # answered early and correctly: do not inflate the interval
    rate(uid, cid, 3 if correct else 1, source="answer")


def _filters(settings):
    srcs = {s for s in (settings.get("sources") or "").split(",") if s}
    doms = {d for d in (settings.get("domains") or "").split("|") if d}
    return srcs, doms


def eligible_new(uid, catalog, settings, domain_weakness=None):
    srcs, doms = _filters(settings)
    seen = {r["card_id"] for r in _rows("SELECT card_id FROM srs_cards WHERE user_id=?", (uid,))}
    paused = catalog.paused() or set()
    pool = [c for c in catalog.order if c not in seen and catalog.cards[c]["kind"] in srcs
            and (not doms or catalog.cards[c]["domain"] in doms) and c[2:] not in paused]
    # weakest domains first, then interleave across domains so one sitting is mixed
    weak = domain_weakness or {}
    by_dom = {}
    for c in pool:
        by_dom.setdefault(catalog.cards[c]["domain"], []).append(c)
    rnd = random.Random(f"{uid}-new")
    for v in by_dom.values():
        rnd.shuffle(v)
    doms_sorted = sorted(by_dom, key=lambda d: (weak.get(d, 50), d))
    out = []
    while any(by_dom.values()):
        for d in doms_sorted:
            if by_dom[d]:
                out.append(by_dom[d].pop())
    return out


def new_today(uid, now=None):
    r = _rows("SELECT COUNT(*) AS n FROM srs_log WHERE user_id=? AND was_new=1 AND source='cards' AND ts>=?",
              (uid, day_start(now)))
    return int(r[0]["n"]) if r else 0


def due_cards(uid, now=None, learn_ahead=20 * MIN):
    now = now or time.time()
    rows = _rows("SELECT card_id, state, due_at FROM srs_cards WHERE user_id=? AND state<>'new' AND due_at<=? ORDER BY due_at",
                 (uid, now + learn_ahead))
    return rows


def summary(uid, catalog, now=None):
    now = now or time.time()
    s = get_settings(uid)
    rows = _rows("SELECT state, due_at, interval_days FROM srs_cards WHERE user_id=?", (uid,))
    due_now = sum(1 for r in rows if r["state"] != "new" and (r["due_at"] or 0) <= now)
    learning = sum(1 for r in rows if r["state"] in ("learning", "relearning"))
    mature = sum(1 for r in rows if r["state"] == "review" and (r["interval_days"] or 0) >= 21)
    young = sum(1 for r in rows if r["state"] == "review" and (r["interval_days"] or 0) < 21)
    srcs, doms = _filters(s)
    total = sum(1 for c in catalog.order if catalog.cards[c]["kind"] in srcs and (not doms or catalog.cards[c]["domain"] in doms))
    seen = len(rows)
    new_left_today = max(0, s["new_per_day"] - new_today(uid, now))
    # 14-day forecast of reviews by local day
    ds = day_start(now)
    fc = [0] * 14
    for r in rows:
        if r["state"] == "new":
            continue
        d = int(max(0, (float(r["due_at"] or 0) - ds) // DAY))
        if d < 14:
            fc[d] += 1
    ex = exam_ts(s)
    days_left = max(0, int((ex - now) // DAY)) if ex else None
    unseen = max(0, total - seen)
    needed = (unseen + days_left - 1) // days_left if days_left else None
    streak = study_streak(uid, now)
    retention = recent_retention(uid, now)
    return {"due_now": due_now, "learning": learning, "young": young, "mature": mature, "seen": seen, "total": total,
            "unseen": unseen, "new_left_today": new_left_today, "forecast": fc, "days_left": days_left,
            "new_needed_per_day": needed, "settings": s, "streak": streak, "retention": retention}


def study_streak(uid, now=None):
    now = now or time.time()
    rows = _rows("SELECT ts FROM srs_log WHERE user_id=? AND ts>=? ", (uid, now - 400 * DAY))
    days = {day_start(r["ts"]) for r in rows}
    streak, d = 0, day_start(now)
    if d not in days:
        d -= DAY  # today not done yet: count from yesterday
    while d in days:
        streak += 1
        d -= DAY
    return streak


def recent_retention(uid, now=None):
    now = now or time.time()
    r = _rows("SELECT rating FROM srs_log WHERE user_id=? AND was_new=0 AND ts>=?", (uid, now - 30 * DAY))
    if len(r) < 10:
        return None
    return round(100 * sum(1 for x in r if int(x["rating"]) > 1) / len(r))


def _today_new_by_domain(uid, catalog, now=None):
    rows = _rows("SELECT card_id FROM srs_log WHERE user_id=? AND was_new=1 AND source='cards' AND ts>=?", (uid, day_start(now)))
    out = {}
    for r in rows:
        d = (catalog.cards.get(r["card_id"]) or {}).get("domain", "")
        out[d] = out.get(d, 0) + 1
    return out


def next_card(uid, catalog, domain_weakness=None, now=None):
    """Order: cards actually due, then today's new cards (rotating across domains, weakest first),
    then learning cards a few minutes early so a session can finish."""
    now = now or time.time()
    due = due_cards(uid, now)
    real = [r for r in due if (r["due_at"] or 0) <= now]
    if real:
        return real[0]["card_id"], "review"
    s = get_settings(uid)
    if new_today(uid, now) < s["new_per_day"]:
        pool = eligible_new(uid, catalog, s, domain_weakness)
        if pool:
            weak = domain_weakness or {}
            done = _today_new_by_domain(uid, catalog, now)
            first = {}
            for c in pool:
                first.setdefault(catalog.cards[c]["domain"], c)
            d = min(first, key=lambda k: (done.get(k, 0), weak.get(k, 50), k))
            return first[d], "new"
    if due:
        return due[0]["card_id"], "review"
    return None, None


# ------------------------------------------------------------------------------------- web
def install_srs_v560(app, data, app_mod=None):
    from flask import jsonify, redirect, render_template, request, url_for

    ensure_schema()
    q540 = getattr(data, "QUALITY_V540", {}) or {}
    catalog = Catalog(data, paused=q540.get("paused_ids", lambda: set()))
    data.SRS_V560 = {"catalog": catalog}

    def uid():
        return db._current_user_id()

    def weakness(u):
        try:
            return db.unified_domain_mastery(user_id=u)
        except Exception:
            return {}

    # --- every answer on the site feeds the card schedule
    import quality_v540 as qv
    orig = qv.record_review_answer

    def record_review_answer_v560(u, qid, correct):
        orig(u, qid, correct)
        try:
            if ("q:" + str(qid)) in catalog.cards:
                record_answer(u, str(qid), bool(correct))
        except Exception:
            pass

    qv.record_review_answer = record_review_answer_v560
    if isinstance(q540, dict):
        q540["record_review_answer"] = record_review_answer_v560

    def cards_home():
        u = uid()
        sm = summary(u, catalog)
        doms = sorted({c["domain"] for c in catalog.cards.values() if c["domain"]})
        return render_template("cards_v560.html", sm=sm, domains=doms,
                               kinds={k: sum(1 for c in catalog.cards.values() if c["kind"] == k) for k in ("board", "image", "check")})

    def cards_settings():
        u = uid()
        f = request.form
        exam = (f.get("exam_date") or "").strip()
        try:
            if exam:
                datetime.strptime(exam, "%Y-%m-%d")
        except ValueError:
            exam = ""
        try:
            npd = max(0, min(200, int(f.get("new_per_day") or 20)))
        except ValueError:
            npd = 20
        srcs = ",".join(k for k in ("board", "image", "check") if f.get("src_" + k)) or "board"
        doms = "|".join(f.getlist("domains"))
        save_settings(u, exam, npd, srcs, doms)
        return redirect(url_for("cards_home_v560"))

    def cards_study():
        return render_template("cards_study_v560.html")

    def _payload(u, now=None):
        cid, kind = next_card(u, catalog, weakness(u), now)
        sm = summary(u, catalog, now)
        counts = {"due": sm["due_now"], "learning": sm["learning"], "new_left": sm["new_left_today"]}
        if not cid:
            return {"done": True, "counts": counts}
        card = catalog.render(cid)
        if not card:
            # source vanished: drop the card from the schedule and move on
            _run("DELETE FROM srs_cards WHERE user_id=? AND card_id=?", (u, cid))
            return _payload(u, now)
        row = _card_row(u, cid) or {"state": "new", "ease": 2.5, "interval_days": 0}
        card["queue"] = kind
        card["state"] = row.get("state")
        card["intervals"] = preview_intervals(row, exam=exam_ts(get_settings(u)))
        return {"done": False, "card": card, "counts": counts}

    def api_next():
        return jsonify(_payload(uid()))

    def api_rate():
        body = request.get_json(force=True) or {}
        cid = str(body.get("card_id") or "")
        try:
            r = int(body.get("rating"))
        except (TypeError, ValueError):
            r = 0
        if cid not in catalog.cards or r not in RATINGS:
            return jsonify({"error": "bad card or rating"}), 400
        u = uid()
        rate(u, cid, r)
        return jsonify(_payload(u))

    app.jinja_env.globals["cards_due_v560"] = lambda: (lambda sm: {"due": sm["due_now"], "new": sm["new_left_today"],
                                                                     "days_left": sm["days_left"]})(summary(uid(), catalog))
    routes = [
        ("/cards", "cards_home_v560", cards_home, ["GET"]),
        ("/cards/settings", "cards_settings_v560", cards_settings, ["POST"]),
        ("/cards/study", "cards_study_v560", cards_study, ["GET"]),
        ("/api/cards/next", "api_cards_next_v560", api_next, ["GET"]),
        ("/api/cards/rate", "api_cards_rate_v560", api_rate, ["POST"]),
    ]
    served = getattr(app, "_got_first_request", False)
    if served:
        app._got_first_request = False
    try:
        for rule, name, fn, methods in routes:
            if name not in app.view_functions:
                app.add_url_rule(rule, name, fn, methods=methods)
    finally:
        if served:
            app._got_first_request = True
    counts = {k: sum(1 for c in catalog.cards.values() if c["kind"] == k) for k in ("board", "image", "check")}
    data.SRS_V560["counts"] = counts
    return {"cards": len(catalog.cards), **counts}
