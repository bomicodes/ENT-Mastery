"""v55.0: account administration for chiefs, plus deployment safety checks.

- A chief or attending can reset a resident's PIN and change a role from /roster.
  Before this, both needed direct SQL. You cannot demote or lock out the last
  chief/attending.
- SECRET_KEY guard: when accounts are enforced (production) and SECRET_KEY is
  missing or still the development default, a random key is used for this
  process. A guessable key would let anyone forge a signed-in session. Sessions
  then reset on each restart, and the roster's setup panel tells the chief to
  set a real key.
- Setup panel on /roster shows what is configured, so a chief can confirm the
  live deployment before inviting residents.
"""
import os
import secrets

from flask import redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash

import db

DEV_DEFAULT_KEYS = {"", "dev-ent-mastery-change-me", "change-me", "dev"}
ROLES = ("resident", "chief", "attending")
STATE = {"secret_key_replaced": False}


def _privileged():
    from accounts_v444 import PRIVILEGED_ROLES
    return (session.get("user_role") or "") in PRIVILEGED_ROLES


def _set_role(user_id, role):
    c = db.conn()
    db._execute(c, "UPDATE users SET role=? WHERE id=? AND id<>?", (role, user_id, db.LEGACY_USER_ID))
    c.commit()
    c.close()


def setup_health():
    from accounts_v444 import _gate_enabled
    users = db.list_users(include_legacy=False)
    leaders = [u for u in users if (u.get("role") or "") in ("chief", "attending")]
    key = os.environ.get("SECRET_KEY", "")
    checks = [
        ("Sign-in required", _gate_enabled(),
         "Accounts are enforced." if _gate_enabled() else
         "The site is open to anyone. Set DATABASE_URL (production) or ENT_MASTERY_REQUIRE_ACCOUNTS."),
        ("Secret key", key not in DEV_DEFAULT_KEYS and len(key) >= 24,
         "A strong SECRET_KEY is set." if key not in DEV_DEFAULT_KEYS and len(key) >= 24 else
         ("SECRET_KEY is missing or weak; a temporary random key is in use, so everyone is signed out on each restart. "
          "Set SECRET_KEY to a long random value in Render's environment settings.")),
        ("Persistent database", bool(os.environ.get("DATABASE_URL")),
         "Progress is stored in Postgres." if os.environ.get("DATABASE_URL") else
         "No DATABASE_URL: progress is stored in a local SQLite file, which Render wipes on each deploy."),
        ("At least two chiefs or attendings", len(leaders) >= 2,
         f"{len(leaders)} chief/attending account(s). " + ("Good." if len(leaders) >= 2 else
         "Add a second one so someone else can reset PINs if you are away.")),
        ("Bootstrap PIN removed", not os.environ.get("ENT_MASTERY_CHIEF_PIN"),
         "ENT_MASTERY_CHIEF_PIN is not set." if not os.environ.get("ENT_MASTERY_CHIEF_PIN") else
         "ENT_MASTERY_CHIEF_PIN is still set. It is only needed for the very first login; remove it now."),
    ]
    return [{"label": a, "ok": bool(b), "detail": c} for a, b, c in checks]


def install_accounts_admin_v550(app, data=None, app_mod=None):
    from accounts_v444 import PIN_RE, _clear_pin_failures, _gate_enabled

    key = os.environ.get("SECRET_KEY", "")
    if _gate_enabled() and (key in DEV_DEFAULT_KEYS or len(key) < 24) and app.secret_key in DEV_DEFAULT_KEYS | {key}:
        app.secret_key = secrets.token_hex(32)
        STATE["secret_key_replaced"] = True

    def _render(msg=None, err=None):
        return render_template("roster.html", roster=db.roster_summary(), add_error=None,
                               admin_msg=msg, admin_err=err, health=setup_health())

    def _deny():
        return render_template("login.html", error="That page is limited to chief residents and attendings."), 403

    def reset_pin():
        if os.environ.get("ENT_MASTERY_AUDIT_MODE") == "1":
            return redirect(url_for("dashboard"))
        if not _privileged():
            return _deny()
        try:
            uid = int(request.form.get("user_id") or 0)
        except ValueError:
            uid = 0
        pin = request.form.get("pin") or ""
        user = db.get_user_by_id(uid) if uid else None
        if not user or uid == db.LEGACY_USER_ID:
            return _render(err="Account not found.")
        if not PIN_RE.fullmatch(pin):
            return _render(err="The new PIN must be 4–8 digits.")
        db.update_user_pin(uid, generate_password_hash(pin))
        _clear_pin_failures(uid)
        return _render(msg=f"PIN reset for {user['name']}. Give them the new PIN privately; they can change it under Account → Change PIN.")

    def change_role():
        if os.environ.get("ENT_MASTERY_AUDIT_MODE") == "1":
            return redirect(url_for("dashboard"))
        if not _privileged():
            return _deny()
        try:
            uid = int(request.form.get("user_id") or 0)
        except ValueError:
            uid = 0
        role = request.form.get("role") or ""
        user = db.get_user_by_id(uid) if uid else None
        if not user or uid == db.LEGACY_USER_ID or role not in ROLES:
            return _render(err="Account or role not found.")
        leaders = [u for u in db.list_users(include_legacy=False) if (u.get("role") or "") in ("chief", "attending")]
        if role == "resident" and (user.get("role") in ("chief", "attending")) and len(leaders) <= 1:
            return _render(err="That is the only chief/attending account. Promote someone else first.")
        _set_role(uid, role)
        note = " They need to sign out and back in for it to take effect." if uid != session.get("user_id") else ""
        if uid == session.get("user_id"):
            session["user_role"] = role
        return _render(msg=f"{user['name']} is now {role}.{note}")

    def roster_view():
        if os.environ.get("ENT_MASTERY_AUDIT_MODE") == "1":
            return redirect(url_for("dashboard"))
        if not _privileged():
            return _deny()
        return _render()

    app.jinja_env.globals["setup_health_v550"] = setup_health
    served = getattr(app, "_got_first_request", False)
    if served:
        app._got_first_request = False
    try:
        if "roster_reset_pin_v550" not in app.view_functions:
            app.add_url_rule("/roster/reset-pin", "roster_reset_pin_v550", reset_pin, methods=["POST"])
            app.add_url_rule("/roster/role", "roster_role_v550", change_role, methods=["POST"])
        app.view_functions["roster_v444"] = roster_view
    finally:
        if served:
            app._got_first_request = True
    return {"secret_key_replaced": STATE["secret_key_replaced"]}
