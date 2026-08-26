"""Production entrypoint with the Pasha review subsystem registered last.

Importing runtime_entry first preserves all existing curriculum/practice repairs before
Pasha maps its review bank to the final live question objects.
"""
import runtime_entry
from pasha_routes import bp as pasha_review_blueprint

app=runtime_entry.app
if "pasha_review" not in app.blueprints:
    app.register_blueprint(pasha_review_blueprint)
