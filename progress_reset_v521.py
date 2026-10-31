"""v52.1: let a learner reset their own progress.

/account/reset shows what will be erased and asks the learner to type RESET.
The POST deletes only the current user's rows from every progress table; the
account itself, its PIN and other residents' progress are untouched.
"""
import db

# Every table that stores per-user learning progress (all carry user_id).
PROGRESS_TABLES = (
    "attempts",            # question answers (Clinical Challenges, Concept Checks, Daily Path)
    "concepts",            # spaced-review strength and due dates
    "mastery_events",      # competency-dimension evidence
    "lab_attempts",        # Interpretation Atlas ratings
    "curriculum_mastery",  # Daily Path stage per topic
    "daily_path_events",   # Daily Path history
    "pasha_attempts",      # Pasha chapter review answers
)
CONFIRM_WORD = "RESET"


def progress_counts(user_id):
    c = db.conn()
    out = {}
    try:
        for t in PROGRESS_TABLES:
            if db._table_exists(c, t) and "user_id" in db._table_columns(c, t):
                row = db._execute(c, f"SELECT COUNT(*) AS n FROM {t} WHERE user_id=?", (user_id,)).fetchone()
                out[t] = row["n"] if isinstance(row, dict) or hasattr(row, "keys") else row[0]
            else:
                out[t] = 0
    finally:
        c.close()
    return out


def reset_progress(user_id):
    """Delete this user's progress rows. Returns {table: rows_deleted}."""
    before = progress_counts(user_id)
    c = db.conn()
    try:
        for t in PROGRESS_TABLES:
            if db._table_exists(c, t) and "user_id" in db._table_columns(c, t):
                db._execute(c, f"DELETE FROM {t} WHERE user_id=?", (user_id,))
        c.commit()
    finally:
        c.close()
    return before


def install_progress_reset_v521(app):
    from flask import render_template, request, redirect, url_for

    def reset_view():
        uid = db._current_user_id()
        error = None
        if request.method == "POST":
            if request.form.get("confirm", "").strip().upper() == CONFIRM_WORD:
                reset_progress(uid)
                return redirect(url_for("progress", reset=1))
            error = f'Type {CONFIRM_WORD} in the box to confirm. Nothing was erased.'
        counts = progress_counts(uid)
        return render_template("progress_reset.html", counts=counts,
                               total=sum(counts.values()), error=error, confirm_word=CONFIRM_WORD)

    if "progress_reset_v521" not in app.view_functions:
        served = getattr(app, "_got_first_request", False)
        if served:
            app._got_first_request = False
        try:
            app.add_url_rule("/account/reset", "progress_reset_v521", reset_view, methods=["GET", "POST"])
        finally:
            if served:
                app._got_first_request = True
    return {"route": "/account/reset", "tables": list(PROGRESS_TABLES)}
