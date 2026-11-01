"""v53.1: timed exam mode, question flags/notes, and bank status filters.

/exam                 build a block (size, domains, pool, timed/untimed, exam/tutor)
/exam/<id>            take it: one question at a time, timer, flag, navigator
/exam/<id>/report     score, time, by-domain breakdown, full review, retry missed
/api/qmeta/<qid>      GET/POST a question's flag and note (any page)

Answers submitted in an exam are recorded like Clinical Challenge answers, so
the bank's Unused / Incorrect / Flagged filters and mastery see them too.
"""
import json
import random
import time
from datetime import datetime

import db

SECONDS_PER_QUESTION = 60
TIER_GROUPS = {
    "board": ("Board-style", lambda t: t == "Curated board-style"),
    "ladder": ("Learning ladder", lambda t: t == "Curated learning ladder"),
    "chief": ("Chief / call / OR depth", lambda t: t not in ("Curated board-style", "Curated learning ladder")),
}


# ----------------------------------------------------------------------------- storage
def ensure_schema():
    c = db.conn()
    pk = "BIGSERIAL PRIMARY KEY" if db.USE_POSTGRES else "INTEGER PRIMARY KEY AUTOINCREMENT"
    c.execute(f"""CREATE TABLE IF NOT EXISTS exam_sessions (
        id {pk}, user_id INTEGER NOT NULL, created_at TEXT, config TEXT, question_ids TEXT,
        answers TEXT, flags TEXT, time_limit INTEGER, started_at REAL, finished_at REAL,
        correct INTEGER, total INTEGER)""")
    c.execute("""CREATE TABLE IF NOT EXISTS question_meta (
        user_id INTEGER NOT NULL, question_id TEXT NOT NULL, flagged INTEGER DEFAULT 0,
        note TEXT DEFAULT '', updated_at TEXT, PRIMARY KEY (user_id, question_id))""")
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
        cur = db._execute(c, sql, params)
        c.commit()
        return cur
    finally:
        c.close()


def question_meta(uid):
    return {r["question_id"]: r for r in _rows("SELECT * FROM question_meta WHERE user_id=?", (uid,))}


def set_meta(uid, qid, flagged=None, note=None):
    cur = _rows("SELECT * FROM question_meta WHERE user_id=? AND question_id=?", (uid, qid))
    f = int(bool(flagged)) if flagged is not None else (cur[0]["flagged"] if cur else 0)
    n = (note if note is not None else (cur[0]["note"] if cur else "")) or ""
    now = datetime.now().isoformat()
    if cur:
        _run("UPDATE question_meta SET flagged=?, note=?, updated_at=? WHERE user_id=? AND question_id=?", (f, n[:4000], now, uid, qid))
    else:
        _run("INSERT INTO question_meta (user_id,question_id,flagged,note,updated_at) VALUES (?,?,?,?,?)", (uid, qid, f, n[:4000], now))
    return {"flagged": bool(f), "note": n}


def question_status(uid):
    """{qid: 'correct'|'incorrect'} from the latest Clinical Challenge answer."""
    out = {}
    for r in _rows("SELECT source_id, score FROM mastery_events WHERE user_id=? AND source_type='clinical_challenge' ORDER BY id", (uid,)):
        out[r["source_id"]] = "correct" if (r["score"] or 0) >= 2 else "incorrect"
    return out


def _load(eid, uid):
    rows = _rows("SELECT * FROM exam_sessions WHERE id=? AND user_id=?", (eid, uid))
    if not rows:
        return None
    s = rows[0]
    s["config"] = json.loads(s["config"] or "{}")
    s["question_ids"] = json.loads(s["question_ids"] or "[]")
    s["answers"] = {int(k): v for k, v in json.loads(s["answers"] or "{}").items()}
    s["flags"] = set(json.loads(s["flags"] or "[]"))
    return s


def _save(s):
    _run("UPDATE exam_sessions SET answers=?, flags=? WHERE id=?",
         (json.dumps({str(k): v for k, v in s["answers"].items()}), json.dumps(sorted(s["flags"])), s["id"]))


def remaining_seconds(s):
    if not s["time_limit"]:
        return None
    return max(0, int(s["time_limit"] - (time.time() - (s["started_at"] or time.time()))))


# ----------------------------------------------------------------------------- install
def install_exam_mode_v531(app, data, app_mod=None):
    from flask import render_template, request, redirect, url_for, jsonify, abort

    ensure_schema()
    bank = data.CLINICAL_CHALLENGES_V119
    by_id = data.CLINICAL_CHALLENGE_BY_ID_V119
    src = app_mod if app_mod is not None else data
    canon = getattr(src, "canonical_domain_v94", None) or getattr(data, "canonical_domain_v94", lambda d: d)
    domains = list(getattr(src, "CANONICAL_DOMAINS_V94", None) or getattr(data, "CANONICAL_DOMAINS_V94", None) or sorted({q.get("domain") for q in bank}))

    def uid():
        return db._current_user_id()

    def _quality():
        return getattr(data, "QUALITY_V540", None) or {}

    def pool_for(cfg, u):
        paused = _quality().get("paused_ids", lambda: set())()
        rows = [q for q in bank if q["id"] not in paused]
        tg = TIER_GROUPS.get(cfg.get("tier", "board"))
        if tg:
            rows = [q for q in rows if tg[1](q.get("tier"))]
        doms = cfg.get("domains") or []
        if doms:
            want = {canon(d) for d in doms}
            rows = [q for q in rows if canon(q.get("domain")) in want]
        pool = cfg.get("pool", "all")
        if pool in ("unused", "incorrect"):
            st = question_status(u)
            rows = [q for q in rows if (st.get(q["id"]) is None) == (pool == "unused") and (pool == "unused" or st.get(q["id"]) == "incorrect")]
        elif pool == "image":
            rows = [q for q in rows if q.get("image_url")]
        elif pool == "due":
            due = set(_quality().get("due_reviews", lambda u: {"due": []})(u)["due"])
            rows = [q for q in rows if q["id"] in due]
        elif pool == "flagged":
            meta = question_meta(u)
            rows = [q for q in rows if meta.get(q["id"], {}).get("flagged")]
        elif pool == "ids":
            ids = [i for i in cfg.get("ids", []) if i in by_id]
            rows = [by_id[i] for i in ids]
        return rows

    def exam_home():
        u = uid()
        st = question_status(u)
        meta = question_meta(u)
        past = _rows("SELECT id, created_at, config, correct, total, finished_at, started_at, time_limit FROM exam_sessions WHERE user_id=? ORDER BY id DESC LIMIT 15", (u,))
        for p in past:
            p["config"] = json.loads(p["config"] or "{}")
            p["pct"] = round(100 * p["correct"] / p["total"]) if p["finished_at"] and p["total"] else None
        board = [q for q in bank if q.get("tier") == "Curated board-style"]
        counts = {
            "board": len(board), "all": len(bank),
            "answered": len(st), "incorrect": sum(1 for v in st.values() if v == "incorrect"),
            "flagged": sum(1 for v in meta.values() if v.get("flagged")),
            "images": sum(1 for q in bank if q.get("image_url")),
            "due": len(_quality().get("due_reviews", lambda u: {"due": []})(u)["due"]),
        }
        return render_template("exam_home.html", domains=domains, counts=counts, past=past,
                               tier_groups=TIER_GROUPS, error=request.args.get("error"))

    def exam_start():
        u = uid()
        f = request.form
        cfg = {
            "count": max(5, min(200, int(f.get("count") or 40))),
            "domains": f.getlist("domains"),
            "pool": f.get("pool", "all"),
            "tier": f.get("tier", "board"),
            "mode": "tutor" if f.get("mode") == "tutor" else "exam",
            "timed": f.get("timed", "1") == "1",
            "blueprint": f.get("blueprint") == "1",
        }
        if cfg["pool"] == "ids":
            cfg["ids"] = [i for i in f.get("ids", "").split(",") if i]
            cfg["tier"] = "any"
        rows = pool_for(cfg, u)
        if not rows:
            return redirect(url_for("exam_home_v531", error="No questions match that combination. Widen the pool or domains."))
        random.shuffle(rows)
        if cfg.get("blueprint") and cfg["pool"] != "ids":
            weights = _quality().get("blueprint") or {}
            by_dom = {}
            for q in rows:
                by_dom.setdefault(canon(q.get("domain")), []).append(q)
            total_w = sum(w for d, w in weights.items() if by_dom.get(d)) or 1
            picked = []
            for d, w in weights.items():
                k = int(round(cfg["count"] * w / total_w))
                picked += by_dom.get(d, [])[:k]
            ids = {q["id"] for q in picked}
            picked += [q for q in rows if q["id"] not in ids][: max(0, cfg["count"] - len(picked))]
            random.shuffle(picked)
            rows = picked
        chosen = [q["id"] for q in rows[: cfg["count"]]]
        cfg["count"] = len(chosen)
        limit = len(chosen) * SECONDS_PER_QUESTION if cfg["timed"] else 0
        c = db.conn()
        try:
            cur = db._execute(c, """INSERT INTO exam_sessions (user_id, created_at, config, question_ids, answers, flags, time_limit, started_at, correct, total)
                VALUES (?,?,?,?,?,?,?,?,?,?)""" + (" RETURNING id" if db.USE_POSTGRES else ""),
                (u, datetime.now().isoformat(timespec="minutes"), json.dumps(cfg), json.dumps(chosen), "{}", "[]", limit, time.time(), 0, len(chosen)))
            eid = cur.fetchone()["id"] if db.USE_POSTGRES else cur.lastrowid
            c.commit()
        finally:
            c.close()
        return redirect(url_for("exam_take_v531", eid=eid))

    def exam_take(eid):
        s = _load(eid, uid())
        if not s:
            abort(404)
        if s["finished_at"]:
            return redirect(url_for("exam_report_v531", eid=eid))
        rem = remaining_seconds(s)
        if rem == 0:
            return _finish(s)
        meta = question_meta(uid())
        qs = []
        for i, qid in enumerate(s["question_ids"]):
            q = by_id.get(qid, {})
            item = {"i": i, "id": qid, "domain": q.get("domain"), "topic": q.get("topic"), "stem": q.get("stem"),
                    "choices": q.get("choices", []), "chosen": s["answers"].get(i), "flagged": i in s["flags"],
                    "note": meta.get(qid, {}).get("note", ""),
                    "image_url": q.get("image_url"), "image_credit": q.get("image_credit"), "image_source": q.get("image_source")}
            if s["config"].get("mode") == "tutor" and i in s["answers"]:
                item.update(_reveal_payload(q))
            qs.append(item)
        return render_template("exam_take.html", s=s, qs=qs, remaining=rem, eid=eid)

    def _reveal_payload(q):
        letters = "ABCD"
        why = q.get("why_wrong") or []
        return {"answer": int(q.get("answer", -1)), "explanation": q.get("explanation", ""),
                "why_wrong": [[letters[i], w] for i, w in enumerate(why) if i != int(q.get("answer", -1)) and w],
                "pearl": q.get("board_pearl", "")}

    def exam_save(eid):
        s = _load(eid, uid())
        if not s or s["finished_at"]:
            return jsonify({"ok": False}), 404
        p = request.get_json(force=True) or {}
        i = int(p.get("i", -1))
        if not 0 <= i < len(s["question_ids"]):
            return jsonify({"ok": False}), 400
        out = {"ok": True, "remaining": remaining_seconds(s)}
        if out["remaining"] == 0:
            out["expired"] = True
            return jsonify(out)
        tutor = s["config"].get("mode") == "tutor"
        if "choice" in p and not (tutor and i in s["answers"]):
            ch = p.get("choice")
            if ch is None:
                s["answers"].pop(i, None)
            else:
                s["answers"][i] = int(ch)
            if tutor and ch is not None:
                out.update(_reveal_payload(by_id.get(s["question_ids"][i], {})))
        if "flagged" in p:
            (s["flags"].add if p["flagged"] else s["flags"].discard)(i)
            set_meta(uid(), s["question_ids"][i], flagged=bool(p["flagged"]))
        _save(s)
        return jsonify(out)

    def _finish(s):
        if not s["finished_at"]:
            u = uid()
            correct = 0
            for i, qid in enumerate(s["question_ids"]):
                q = by_id.get(qid)
                if q is None or i not in s["answers"]:
                    continue
                ok = int(s["answers"][i]) == int(q.get("answer", -2))
                correct += ok
                try:
                    _quality().get("record_review_answer", lambda *a: None)(u, qid, ok)
                except Exception:
                    pass
                try:
                    db.record_mastery_event(q.get("concept_id") or q.get("topic", ""), q.get("domain", "ENT"),
                                            "management" if q.get("mode") == "Manage" else "reasoning", 3 if ok else 0,
                                            source_type="clinical_challenge", source_id=qid,
                                            miss_type=None if ok else "discrimination", user_id=u)
                except Exception:
                    pass
            _run("UPDATE exam_sessions SET finished_at=?, correct=? WHERE id=?", (time.time(), correct, s["id"]))
        return redirect(url_for("exam_report_v531", eid=s["id"]))

    def exam_finish(eid):
        s = _load(eid, uid())
        if not s:
            abort(404)
        return _finish(s)

    def exam_report(eid):
        s = _load(eid, uid())
        if not s:
            abort(404)
        if not s["finished_at"]:
            return redirect(url_for("exam_take_v531", eid=eid))
        items, by_dom = [], {}
        for i, qid in enumerate(s["question_ids"]):
            q = by_id.get(qid, {})
            ch = s["answers"].get(i)
            ok = ch is not None and int(ch) == int(q.get("answer", -2))
            d = by_dom.setdefault(q.get("domain", "Other"), {"n": 0, "ok": 0})
            d["n"] += 1
            d["ok"] += ok
            items.append({"i": i, "q": q, "chosen": ch, "ok": ok, "flagged": i in s["flags"]})
        dom_rows = sorted(({"domain": k, **v, "pct": round(100 * v["ok"] / v["n"])} for k, v in by_dom.items()), key=lambda r: r["pct"])
        used = int((s["finished_at"] or time.time()) - (s["started_at"] or 0))
        missed_ids = ",".join(it["q"].get("id", "") for it in items if not it["ok"])
        diff = _quality().get("difficulty_map", lambda: {})()
        for it in items:
            d = diff.get(it["q"].get("id"))
            it["diff"] = d if d and d[1] >= 3 else None
        return render_template("exam_report.html", s=s, items=items, dom_rows=dom_rows,
                               pct=round(100 * s["correct"] / s["total"]) if s["total"] else 0,
                               used_min=used // 60, used_sec=used % 60, missed_ids=missed_ids,
                               unanswered=sum(1 for it in items if it["chosen"] is None))

    def qmeta(qid):
        u = uid()
        if request.method == "POST":
            p = request.get_json(force=True) or {}
            return jsonify({"ok": True, **set_meta(u, qid, flagged=p.get("flagged"), note=p.get("note"))})
        m = question_meta(u).get(qid, {})
        return jsonify({"ok": True, "flagged": bool(m.get("flagged")), "note": m.get("note", ""),
                        "status": question_status(u).get(qid)})

    # Bank page: same filters as before plus Status and grouped Tier.
    def clinical_challenges_v531():
        from flask import request as rq
        a = rq.args
        domain, topic, tier, mode, focus = (a.get(k, "").strip() for k in ("domain", "topic", "tier", "mode", "focus"))
        status, tier_group = a.get("status", "").strip(), a.get("tier_group", "").strip()
        rows = list(bank)
        if domain:
            rows = [q for q in rows if canon(q.get("domain")) == canon(domain)]
        if topic:
            t = topic.lower()
            rows = [q for q in rows if t in q.get("topic", "").lower() or t in q.get("stem", "").lower()]
        if tier:
            rows = [q for q in rows if q.get("tier") == tier]
        if tier_group in TIER_GROUPS:
            rows = [q for q in rows if TIER_GROUPS[tier_group][1](q.get("tier"))]
        if mode:
            rows = [q for q in rows if q.get("mode") == mode]
        if focus:
            rows = [q for q in rows if (q.get("focus") or "") == focus]
        u = uid()
        st, meta = question_status(u), question_meta(u)
        if status == "unused":
            rows = [q for q in rows if q["id"] not in st]
        elif status in ("correct", "incorrect"):
            rows = [q for q in rows if st.get(q["id"]) == status]
        elif status == "flagged":
            rows = [q for q in rows if meta.get(q["id"], {}).get("flagged")]
        elif status == "image":
            rows = [q for q in rows if q.get("image_url")]
        stats = {"questions": len(bank), "topics": len({q.get("concept_id") for q in bank if q.get("concept_id")}),
                 "curated": sum(1 for q in bank if q.get("tier") == "Curated board-style"),
                 "coverage": sum(1 for q in bank if q.get("tier") != "Curated board-style"),
                 "answered": len(st), "incorrect": sum(1 for v in st.values() if v == "incorrect"),
                 "flagged": sum(1 for v in meta.values() if v.get("flagged"))}
        total_filtered = len(rows)
        per_page = getattr(app_mod, "CLINICAL_CHALLENGES_PER_PAGE_V456", 30)
        total_pages = max(1, (total_filtered + per_page - 1) // per_page)
        try:
            page = int(a.get("page", 1))
        except (TypeError, ValueError):
            page = 1
        page = min(max(1, page), total_pages)
        page_rows = rows[(page - 1) * per_page: page * per_page]
        return render_template("clinical_challenges.html", questions=page_rows, domains=domains, domain=domain, topic=topic,
                               tier=tier, mode=mode, focus=focus, stats=stats, page=page, total_pages=total_pages,
                               total_filtered=total_filtered, per_page=per_page, status=status, tier_group=tier_group,
                               q_status=st, q_flags={k for k, v in meta.items() if v.get("flagged")}, tier_groups=TIER_GROUPS)

    def board_readiness():
        """Per-domain readiness from the latest answer to each bank question."""
        u = uid()
        st = question_status(u)
        rows = {}
        for q in bank:
            d = canon(q.get("domain")) or "Other"
            r = rows.setdefault(d, {"domain": d, "total": 0, "answered": 0, "correct": 0})
            r["total"] += 1
            s_ = st.get(q["id"])
            if s_:
                r["answered"] += 1
                r["correct"] += s_ == "correct"
        out = []
        for r in rows.values():
            r["coverage"] = round(100 * r["answered"] / r["total"]) if r["total"] else 0
            r["pct"] = round(100 * r["correct"] / r["answered"]) if r["answered"] else None
            out.append(r)
        out.sort(key=lambda r: (r["pct"] if r["pct"] is not None else 101, r["domain"]))
        exams = _rows("SELECT id, correct, total, finished_at FROM exam_sessions WHERE user_id=? AND finished_at IS NOT NULL ORDER BY id DESC LIMIT 8", (u,))
        exams = [{"id": e["id"], "pct": round(100 * e["correct"] / e["total"]) if e["total"] else 0} for e in reversed(exams)]
        answered = sum(r["answered"] for r in out)
        correct = sum(r["correct"] for r in out)
        return {"domains": out, "exams": exams, "answered": answered,
                "pct": round(100 * correct / answered) if answered else None, "bank": len(bank)}

    app.jinja_env.globals["board_readiness"] = board_readiness

    routes = [
        ("/exam", "exam_home_v531", exam_home, ["GET"]),
        ("/exam/start", "exam_start_v531", exam_start, ["POST"]),
        ("/exam/<int:eid>", "exam_take_v531", exam_take, ["GET"]),
        ("/exam/<int:eid>/finish", "exam_finish_v531", exam_finish, ["POST"]),
        ("/exam/<int:eid>/report", "exam_report_v531", exam_report, ["GET"]),
        ("/api/exam/<int:eid>/save", "exam_save_v531", exam_save, ["POST"]),
        ("/api/qmeta/<qid>", "qmeta_v531", qmeta, ["GET", "POST"]),
    ]
    served = getattr(app, "_got_first_request", False)
    if served:
        app._got_first_request = False
    try:
        for rule, name, fn, methods in routes:
            if name not in app.view_functions:
                app.add_url_rule(rule, name, fn, methods=methods)
        if "clinical_challenges" in app.view_functions:
            app.view_functions["clinical_challenges"] = clinical_challenges_v531
    finally:
        if served:
            app._got_first_request = True
    return {"routes": [r[0] for r in routes], "bank": len(bank)}
