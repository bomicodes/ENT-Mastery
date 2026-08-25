"""v16.8 reliability hardening.

Keeps the generated application stable while fixing persistence canonicalization,
concept routing, legacy links, production error leakage, and single-user access.
All database migrations are idempotent and preserve existing learning history.
"""

import hmac
import os
from functools import wraps

from flask import jsonify, redirect, render_template, request, session, url_for


def _canonical_id(data, concept_id, domain=None):
    try:
        return data.canonical_concept_id_v98(concept_id, domain)
    except Exception:
        return concept_id


def _merge_profile(dst, src):
    if not dst:
        return dict(src)
    out = dict(dst)
    out["events"] = int(dst.get("events") or 0) + int(src.get("events") or 0)
    out["last_seen"] = max(str(dst.get("last_seen") or ""), str(src.get("last_seen") or "")) or None
    if src.get("name") and (not out.get("name") or out.get("name") == out.get("concept_id")):
        out["name"] = src["name"]
    if src.get("domain"):
        out["domain"] = src["domain"]
    dims = {k: dict(v) for k, v in (dst.get("dimensions") or {}).items()}
    for dim, val in (src.get("dimensions") or {}).items():
        if dim not in dims:
            dims[dim] = dict(val)
            continue
        a = dims[dim]
        # Preserve the more recently observed score when exact event-level ordering
        # is unavailable in this compatibility fallback. The DB migration below is
        # the authoritative path and normally makes this branch unnecessary.
        a["events"] = int(a.get("events") or 0) + int(val.get("events") or 0)
        a["scores"] = list(a.get("scores") or []) + list(val.get("scores") or [])
        if str(val.get("last") or "") >= str(a.get("last") or ""):
            a["score"] = val.get("score", a.get("score", 0))
            a["last"] = val.get("last")
    out["dimensions"] = dims
    return out


def _migrate_retired_ids(data, db):
    """Move persisted retired concept IDs to canonical IDs without losing history."""
    aliases = dict(getattr(data, "RETIRED_CONCEPT_ALIASES_V167", {}) or {})
    if not aliases:
        return {"aliases": 0, "rows": 0}

    moved = 0
    c = db.conn()
    try:
        # Event/history tables have non-unique concept_id columns and are safe to
        # update directly. Missing legacy tables are tolerated.
        for old, new in aliases.items():
            if not old or not new or old == new:
                continue
            for table in ("daily_path_events", "mastery_events", "attempts", "lab_attempts"):
                try:
                    cur = db._execute(c, f"UPDATE {table} SET concept_id=? WHERE concept_id=?", (new, old))
                    moved += max(0, int(getattr(cur, "rowcount", 0) or 0))
                except Exception:
                    pass

            # curriculum_mastery is keyed by concept_id, so merge before deleting.
            try:
                old_row = db._execute(c, "SELECT * FROM curriculum_mastery WHERE concept_id=?", (old,)).fetchone()
                if old_row:
                    old_d = dict(old_row)
                    new_row = db._execute(c, "SELECT * FROM curriculum_mastery WHERE concept_id=?", (new,)).fetchone()
                    if new_row:
                        a, b = dict(new_row), old_d
                        mastery_level = max(int(a.get("mastery_level") or 0), int(b.get("mastery_level") or 0))
                        attempts = int(a.get("attempts") or 0) + int(b.get("attempts") or 0)
                        correct = int(a.get("correct") or 0) + int(b.get("correct") or 0)
                        last_seen = max(str(a.get("last_seen") or ""), str(b.get("last_seen") or "")) or None
                        dues = [x for x in (a.get("next_due"), b.get("next_due")) if x is not None]
                        next_due = min(dues, key=lambda x: str(x)) if dues else None
                        db._execute(c, "UPDATE curriculum_mastery SET mastery_level=?, attempts=?, correct=?, last_seen=?, next_due=? WHERE concept_id=?",
                                    (mastery_level, attempts, correct, last_seen, next_due, new))
                        db._execute(c, "DELETE FROM curriculum_mastery WHERE concept_id=?", (old,))
                    else:
                        db._execute(c, "UPDATE curriculum_mastery SET concept_id=? WHERE concept_id=?", (new, old))
                    moved += 1
            except Exception:
                pass

            # Legacy concepts table is also keyed by concept_id. Merge counters if
            # both old and new rows exist; otherwise rename the key.
            try:
                old_row = db._execute(c, "SELECT * FROM concepts WHERE concept_id=?", (old,)).fetchone()
                if old_row:
                    new_row = db._execute(c, "SELECT * FROM concepts WHERE concept_id=?", (new,)).fetchone()
                    if new_row:
                        a, b = dict(new_row), dict(old_row)
                        db._execute(c, "UPDATE concepts SET strength=?, interval_days=?, due_at=?, last_seen=?, correct_count=?, wrong_count=? WHERE concept_id=?", (
                            max(float(a.get("strength") or 0), float(b.get("strength") or 0)),
                            max(int(a.get("interval_days") or 0), int(b.get("interval_days") or 0)),
                            min([x for x in (a.get("due_at"), b.get("due_at")) if x], default=None, key=str),
                            max(str(a.get("last_seen") or ""), str(b.get("last_seen") or "")) or None,
                            int(a.get("correct_count") or 0) + int(b.get("correct_count") or 0),
                            int(a.get("wrong_count") or 0) + int(b.get("wrong_count") or 0),
                            new,
                        ))
                        db._execute(c, "DELETE FROM concepts WHERE concept_id=?", (old,))
                    else:
                        db._execute(c, "UPDATE concepts SET concept_id=? WHERE concept_id=?", (new, old))
                    moved += 1
            except Exception:
                pass
        c.commit()
    finally:
        c.close()
    return {"aliases": len(aliases), "rows": moved}


def _install_profile_canonicalization(data, db, app_mod):
    raw = db.unified_mastery_profiles
    if getattr(raw, "_v168_canonical", False):
        return

    def unified_mastery_profiles_v168():
        profiles = raw()
        out = {}
        for cid, profile in profiles.items():
            canonical = _canonical_id(data, cid, profile.get("domain"))
            p = dict(profile)
            p["concept_id"] = canonical
            out[canonical] = _merge_profile(out.get(canonical), p)
        # Recompute conservative summary values after any compatibility merge.
        dims_all = list(getattr(db, "UNIFIED_DIMENSIONS", []))
        for p in out.values():
            if dims_all:
                scores = [p.get("dimensions", {}).get(dim, {}).get("score", 0) for dim in dims_all]
                p["overall"] = round(sum(scores) / len(dims_all))
                p["coverage_count"] = sum(1 for dim in dims_all if dim in p.get("dimensions", {}))
                p["coverage"] = round(100 * p["coverage_count"] / len(dims_all))
        return out

    unified_mastery_profiles_v168._v168_canonical = True
    db.unified_mastery_profiles = unified_mastery_profiles_v168
    app_mod.unified_mastery_profiles = unified_mastery_profiles_v168


def _install_safe_concept_lookup(data, app_mod):
    import difflib

    def find_deep_module_v168(domain, topic):
        nt = app_mod._norm_topic_v94(topic)
        target_domain = data.canonical_domain_v94(domain) if domain else None

        # Domain-specific exact match first. This prevents duplicate topic names in
        # different specialties from silently resolving to the first registry hit.
        if target_domain:
            for dname, mods in data.DEEP_MODULES_V6.items():
                if data.canonical_domain_v94(dname) != target_domain:
                    continue
                for mod in mods:
                    if app_mod._norm_topic_v94(mod.get("topic", "")) == nt:
                        return dname, mod

        # If no domain was supplied, a globally unique exact title is safe.
        exact = []
        for dname, mods in data.DEEP_MODULES_V6.items():
            for mod in mods:
                if app_mod._norm_topic_v94(mod.get("topic", "")) == nt:
                    exact.append((dname, mod))
        if len(exact) == 1:
            return exact[0]
        if len(exact) > 1:
            return None, None

        # Fuzzy matching is intentionally conservative. A bad/stale medical link
        # should fall back to search rather than open a plausible but wrong topic.
        best = None
        for dname, mods in data.DEEP_MODULES_V6.items():
            if target_domain and data.canonical_domain_v94(dname) != target_domain:
                continue
            for mod in mods:
                ratio = difflib.SequenceMatcher(None, nt, app_mod._norm_topic_v94(mod.get("topic", ""))).ratio()
                if best is None or ratio > best[0]:
                    best = (ratio, dname, mod)
        if best and best[0] >= 0.78:
            return best[1], best[2]
        return None, None

    app_mod._find_deep_module_v94 = find_deep_module_v168


def _install_relationship_context(data, app_mod):
    raw = app_mod._concept_context_v1006
    if getattr(raw, "_v168_relationships", False):
        return

    def concept_context_v168(dname, mod):
        ctx = raw(dname, mod)
        topic = mod.get("topic", "")
        rels = dict(getattr(data, "CURRICULUM_RELATIONSHIPS_V167", {}) or {})
        rel = dict(rels.get(topic, {}) or {})
        children = []
        for child, child_rel in rels.items():
            if topic in (child_rel.get("parents") or []):
                children.append({"topic": child, "role": child_rel.get("role", "related")})
        ctx["clinical_relationship"] = rel
        ctx["clinical_children"] = children
        return ctx

    concept_context_v168._v168_relationships = True
    app_mod._concept_context_v1006 = concept_context_v168


def _install_route_hardening(app, data, app_mod):
    # Do not expose database/runtime exception strings to the browser.
    def daily_adaptive_answer_v168():
        from data import REVIEW_INTERVALS_V6
        import db
        payload = request.get_json(silent=True) or request.form
        try:
            rating = int(payload.get("rating", 2))
            level = int(payload.get("level", 1))
        except Exception:
            return jsonify({"ok": False, "error": "Invalid rating payload."}), 400
        try:
            new_level = db.record_adaptive_result(
                payload.get("concept_id"), payload.get("item_id"), payload.get("domain"),
                payload.get("topic"), payload.get("stage"), level, rating,
                REVIEW_INTERVALS_V6.get(level, 7),
            )
            state = db.adaptive_mastery_map().get(_canonical_id(data, payload.get("concept_id"), payload.get("domain")), {})
            due = state.get("next_due")
            next_level = min(6, new_level + 1) if new_level < 6 else None
            next_stage = {1:"Recognize",2:"Localize",3:"Evaluate",4:"Manage",5:"Advanced",6:"Teach"}.get(next_level)
            return jsonify({"ok":True,"mastery_level":new_level,"next_due":str(due) if due else None,
                            "passed":rating>=2,"next_level":next_level,"next_stage":next_stage})
        except Exception:
            app.logger.exception("Daily Path answer save failed")
            return jsonify({"ok": False, "error": "Could not save progress. Please retry."}), 500

    app.view_functions["daily_adaptive_answer"] = daily_adaptive_answer_v168

    # Preserve old case deep links when the target still exists.
    def legacy_case_v168(cid):
        try:
            if app_mod.get_integrated_case(cid):
                return redirect(url_for("integrated_case", case_id=cid), code=301)
        except Exception:
            pass
        return redirect(url_for("integrated_index"), code=302)

    app.view_functions["case"] = legacy_case_v168

    if "health_v168" not in app.view_functions:
        app.add_url_rule("/health", "health_v168", lambda: jsonify({"ok": True, "version": "16.8"}))


def _install_access_gate(app):
    password = os.environ.get("ENT_MASTERY_ACCESS_PASSWORD", "")
    if not password:
        return False

    app.config.update(
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE="Lax",
        SESSION_COOKIE_SECURE=True,
    )

    def login_v168():
        error = None
        if request.method == "POST":
            supplied = request.form.get("password", "")
            if hmac.compare_digest(supplied, password):
                session["ent_mastery_authenticated"] = True
                target = request.args.get("next") or url_for("dashboard")
                if not target.startswith("/") or target.startswith("//"):
                    target = url_for("dashboard")
                return redirect(target)
            error = "Incorrect access password."
        return render_template("login.html", error=error)

    def logout_v168():
        session.pop("ent_mastery_authenticated", None)
        return redirect(url_for("login_v168"))

    app.add_url_rule("/login", "login_v168", login_v168, methods=["GET", "POST"])
    app.add_url_rule("/logout", "logout_v168", logout_v168)

    @app.before_request
    def require_access_v168():
        if request.endpoint in {"login_v168", "health_v168", "static"}:
            return None
        if session.get("ent_mastery_authenticated"):
            return None
        return redirect(url_for("login_v168", next=request.full_path.rstrip("?")))

    return True


def apply_reliability_v168(app, data, app_mod):
    import db

    migration = _migrate_retired_ids(data, db)
    _install_profile_canonicalization(data, db, app_mod)
    _install_safe_concept_lookup(data, app_mod)
    _install_relationship_context(data, app_mod)
    _install_route_hardening(app, data, app_mod)
    auth_enabled = _install_access_gate(app)

    data.RELIABILITY_V168 = {
        "migration": migration,
        "auth_enabled": auth_enabled,
        "concept_fuzzy_threshold": 0.78,
    }
    return data.RELIABILITY_V168
