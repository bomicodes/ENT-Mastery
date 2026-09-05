"""v15.0 — turn Clinical Challenges and Concept Checks into sequential practice banks.

Installed at the final production entrypoint so it works with the fully assembled live
question registries. The wrapper preserves the existing answer/mastery APIs and only
adds deterministic next-question context to the two detail views.
"""
from flask import redirect, render_template, url_for


def _ordered_rows(app_module, attr):
    return list(getattr(app_module, attr, []) or [])


def _next_context(rows, qid):
    if not rows:
        return None, 0, 0
    idx = next((i for i, row in enumerate(rows) if str(row.get("id")) == str(qid)), None)
    if idx is None:
        return None, 0, len(rows)
    next_q = rows[idx + 1] if idx + 1 < len(rows) else None
    return next_q, idx + 1, len(rows)


def install_practice_bank_navigation_v150(app, app_module):
    """Replace only the two detail view functions; URLs and mastery endpoints stay stable."""

    def clinical_challenge(qid):
        rows = _ordered_rows(app_module, "CLINICAL_CHALLENGES_V119")
        q = next((row for row in rows if str(row.get("id")) == str(qid)), None)
        if not q:
            return redirect(url_for("clinical_challenges"))
        next_q, position, bank_total = _next_context(rows, qid)
        return render_template(
            "clinical_challenge.html",
            q=q,
            next_q=next_q,
            position=position,
            bank_total=bank_total,
        )

    def concept_check(qid):
        rows = _ordered_rows(app_module, "CONCEPT_CHECKS_V112")
        q = next((row for row in rows if str(row.get("id")) == str(qid)), None)
        if not q:
            return redirect(url_for("concept_checks"))
        next_q, position, bank_total = _next_context(rows, qid)
        return render_template(
            "concept_check.html",
            q=q,
            next_q=next_q,
            position=position,
            bank_total=bank_total,
        )

    app.view_functions["clinical_challenge"] = clinical_challenge
    app.view_functions["concept_check"] = concept_check
    return {
        "clinical_challenges": len(_ordered_rows(app_module, "CLINICAL_CHALLENGES_V119")),
        "concept_checks": len(_ordered_rows(app_module, "CONCEPT_CHECKS_V112")),
    }
