"""v55.1: a first-visit "Start here" page (/welcome) and a dismissible dashboard prompt."""
from flask import render_template


def install_welcome_v551(app, data, app_mod=None):
    def welcome():
        bank = getattr(data, "CLINICAL_CHALLENGES_V119", []) or []
        board = sum(1 for q in bank if q.get("tier") == "Curated board-style")
        labs = getattr(data, "INTERPRETATION_LABS", {}) or {}
        stats = {
            "questions": len(bank),
            "board": board,
            "labs": len(labs),
            "lab_cases": sum(len(l.get("cases", [])) for l in labs.values()),
            "maps": len(getattr(data, "ANATOMY_ATLAS_V97", []) or []),
            "topics": sum(len(v) for v in (getattr(data, "DEEP_MODULES_V6", {}) or {}).values()),
        }
        return render_template("welcome_v551.html", stats=stats)

    served = getattr(app, "_got_first_request", False)
    if served:
        app._got_first_request = False
    try:
        if "welcome_v551" not in app.view_functions:
            app.add_url_rule("/welcome", "welcome_v551", welcome)
    finally:
        if served:
            app._got_first_request = True
    return {"route": "/welcome"}
