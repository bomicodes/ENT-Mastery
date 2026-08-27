"""Production entrypoint with the Pasha review subsystem registered last.

Importing runtime_entry first preserves all existing curriculum/practice repairs before
Pasha maps its review bank to the final live question objects.
"""
import runtime_entry
from interpretation_labs_cleanup_v250 import apply_interpretation_labs_cleanup_v250
from pasha_routes import bp as pasha_review_blueprint

# Rebuild the live Interpretation Atlas before the production app begins serving.
# This removes retired lab records/resources from the registry rather than hiding cards.
INTERPRETATION_LABS_CLEANUP_V250 = apply_interpretation_labs_cleanup_v250(
    runtime_entry.data,
    runtime_entry.app_mod,
)

app=runtime_entry.app
if "pasha_review" not in app.blueprints:
    app.register_blueprint(pasha_review_blueprint)
