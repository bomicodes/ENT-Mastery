"""v44.4/v44.5 multi-user accounts.

Replaces the single shared-password gate (reliability_v168.py's
_install_access_gate, now disabled) with real per-resident accounts: every
read/write in db.py automatically scopes to whoever is logged in (see
db.py's `_current_user_id()`), and progress recorded before accounts existed
is preserved intact under the permanent "Legacy / Shared" account
(db.LEGACY_USER_ID) rather than lost or silently merged into someone's
personal history.

Login uses a typed name and PIN, with no public resident list or program
access code. Chiefs add accounts from /roster; each resident can change their
own PIN after signing in.

PIN attempts are rate-limited per account (in-memory; resets on redeploy,
which is fine at this scale) so a short numeric PIN can't be brute-forced by
someone who has already cleared step 1.

A `role` of 'chief' or 'attending' unlocks the /roster program-wide progress
view (db.roster_summary()) and the "add resident" form on it; new accounts
default to 'resident'. Promoting someone to chief is still direct SQL
(sqlite3 ent_mastery.db "UPDATE users SET role='chief' WHERE id=...") until a
dedicated admin UI is worth building; they need to log out/in for the role
change to take effect since role is cached in their session.
"""

import os
import re
import time

from flask import jsonify, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

PRIVILEGED_ROLES = {"chief", "attending"}
PIN_RE = re.compile(r"^\d{4,8}$")

# Per-user_id failed-PIN-attempt tracking: {user_id: (fail_count, locked_until_ts)}.
# In-memory and module-global on purpose -- a redeploy clearing it is an
# acceptable reset for a residency-sized deployment, and it avoids adding a
# database table (with its own migration) just for a rate limiter.
_PIN_ATTEMPTS = {}
MAX_PIN_ATTEMPTS = 5
LOCKOUT_SECONDS = 300


def _gate_enabled():
    """Production requires an account; local audits remain ungated."""
    return bool(os.environ.get("DATABASE_URL") or os.environ.get("ENT_MASTERY_REQUIRE_ACCOUNTS"))


def _pin_locked(user_id):
    fails, locked_until = _PIN_ATTEMPTS.get(user_id, (0, 0))
    if locked_until and time.time() >= locked_until:
        _PIN_ATTEMPTS.pop(user_id, None)
        return False, 0
    if locked_until and time.time() < locked_until:
        return True, int(locked_until - time.time())
    return False, 0


def _record_pin_failure(user_id):
    fails, _ = _PIN_ATTEMPTS.get(user_id, (0, 0))
    fails += 1
    locked_until = time.time() + LOCKOUT_SECONDS if fails >= MAX_PIN_ATTEMPTS else 0
    _PIN_ATTEMPTS[user_id] = (fails, locked_until)


def _clear_pin_failures(user_id):
    _PIN_ATTEMPTS.pop(user_id, None)


def _login_user(user):
    session["user_id"] = user["id"]
    session["user_name"] = user["name"]
    session["user_role"] = user["role"]


def _safe_next(target):
    if not target or not target.startswith("/") or target.startswith("//"):
        return None
    return target


def _install_context_processor(app, db):
    @app.context_processor
    def inject_current_user_v444():
        uid = session.get("user_id")
        if not uid:
            return {"current_user": None}
        return {
            "current_user": {
                "id": uid,
                "name": session.get("user_name") or "Resident",
                "role": session.get("user_role") or "resident",
                "is_chief": (session.get("user_role") or "") in PRIVILEGED_ROLES,
            }
        }


def _install_auth_routes(app, db):
    def login_v444():
        error = None
        if request.method == "POST":
            name = (request.form.get("name") or "").strip()
            pin = request.form.get("pin") or ""
            user = db.get_user_by_name(name) if name else None
            if not user:
                error = "Incorrect name or PIN."
            else:
                locked, remaining = _pin_locked(user["id"])
                if locked:
                    error = f"Too many incorrect attempts. Try again in {max(1, remaining // 60 + 1)} minute(s)."
                elif user.get("pin_hash") and check_password_hash(user["pin_hash"], pin):
                    _clear_pin_failures(user["id"])
                    _login_user(user)
                    target = _safe_next(request.args.get("next")) or url_for("dashboard")
                    return redirect(target)
                else:
                    _record_pin_failure(user["id"])
                    error = "Incorrect name or PIN."
        return render_template("login.html", error=error)

    def logout_v444():
        session.pop("user_id", None)
        session.pop("user_name", None)
        session.pop("user_role", None)
        session.pop("program_ok", None)
        return redirect(url_for("login_v168"))

    def change_pin_v444():
        uid = session.get("user_id")
        if not uid:
            return redirect(url_for("login_v168", next=request.path))
        error = success = None
        if request.method == "POST":
            old_pin = request.form.get("old_pin") or ""
            new_pin = request.form.get("new_pin") or ""
            confirmation = request.form.get("confirm_pin") or ""
            user = db.get_user_by_id(uid)
            locked, remaining = _pin_locked(uid)
            if locked:
                error = f"Too many incorrect attempts. Try again in {max(1, remaining // 60 + 1)} minute(s)."
            elif not user or not user.get("pin_hash") or not check_password_hash(user["pin_hash"], old_pin):
                _record_pin_failure(uid)
                error = "Current PIN is incorrect."
            elif not PIN_RE.fullmatch(new_pin):
                error = "New PIN must be 4–8 digits."
            elif new_pin != confirmation:
                error = "New PINs do not match."
            elif new_pin == old_pin:
                error = "Choose a different PIN."
            else:
                db.update_user_pin(uid, generate_password_hash(new_pin))
                _clear_pin_failures(uid)
                success = "Your PIN has been changed. Use the new PIN next time you sign in."
        return render_template("change_pin.html", error=error, success=success)

    def roster_v444():
        if (session.get("user_role") or "") not in PRIVILEGED_ROLES:
            return render_template(
                "login.html",
                error="That page is limited to chief residents and attendings.",
            ), 403
        return render_template("roster.html", roster=db.roster_summary(), add_error=None)

    def add_resident_v444():
        if (session.get("user_role") or "") not in PRIVILEGED_ROLES:
            return render_template(
                "login.html",
                error="That page is limited to chief residents and attendings.",
            ), 403
        name = (request.form.get("name") or "").strip()
        pin = request.form.get("pin") or ""
        role = request.form.get("role") or "resident"
        if role not in {"resident", "chief", "attending"}:
            role = "resident"
        error = None
        if not name:
            error = "Enter a name."
        elif not PIN_RE.match(pin):
            error = "PIN must be 4-8 digits."
        elif any(u["name"].casefold() == name.casefold() for u in db.list_users(include_legacy=False)):
            error = "That name is already on the roster. Add a distinguishing name."
        else:
            db.create_resident_pin(name, generate_password_hash(pin), role=role)
        return render_template("roster.html", roster=db.roster_summary(), add_error=error)

    # Endpoint names intentionally reuse "login_v168" / route "/login" so the
    # existing sidebar's `url_for('login_v168')` / "/logout" links keep working
    # without touching every template that references them.
    app.add_url_rule("/login", "login_v168", login_v444, methods=["GET", "POST"])
    app.add_url_rule("/logout", "logout_v168", logout_v444)
    app.add_url_rule("/roster", "roster_v444", roster_v444)
    app.add_url_rule("/roster/add", "add_resident_v444", add_resident_v444, methods=["POST"])
    app.add_url_rule("/account/pin", "change_pin_v444", change_pin_v444, methods=["GET", "POST"])

    @app.before_request
    def require_account_v444():
        if not _gate_enabled():
            return None
        if request.endpoint in {"login_v168", "health_v168", "static"}:
            return None
        if session.get("user_id"):
            return None
        return redirect(url_for("login_v168", next=request.full_path.rstrip("?")))


def _bootstrap_chief(db):
    """Guarantee a way in on a fresh deployment.

    Only a chief/attending can add a resident from /roster, and /roster
    itself requires being logged in as one -- so with zero accounts, nobody
    could ever create the first one. If ENT_MASTERY_CHIEF_NAME and
    ENT_MASTERY_CHIEF_PIN are both set, ensure that chief account exists
    (idempotent -- checked by name, safe to run every boot, matches the
    pattern db.py already uses to seed the Legacy/Shared account). Once any
    chief exists, this account can add everyone else from /roster and the
    env vars can be left in place harmlessly or removed.
    """
    name = os.environ.get("ENT_MASTERY_CHIEF_NAME")
    pin = os.environ.get("ENT_MASTERY_CHIEF_PIN")
    if not name or not pin or not PIN_RE.match(pin):
        return
    name = name.strip()
    if any(u["name"].strip().lower() == name.lower() for u in db.list_users(include_legacy=False)):
        return
    db.create_resident_pin(name, generate_password_hash(pin), role="chief")


def apply_accounts_v444(app, data, app_mod):
    import db

    app.config["SESSION_COOKIE_HTTPONLY"] = True
    app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
    if os.environ.get("DATABASE_URL"):
        # Only force Secure cookies where we know the deploy is behind HTTPS
        # (Render/Postgres implies a real deployment); local sqlite dev over
        # plain http would otherwise silently drop the session cookie.
        app.config["SESSION_COOKIE_SECURE"] = True

    _install_context_processor(app, db)
    _install_auth_routes(app, db)
    _bootstrap_chief(db)

    result = {
        "account_gated": _gate_enabled(),
        "legacy_user_id": db.LEGACY_USER_ID,
    }
    data.ACCOUNTS_V444 = result
    return result
