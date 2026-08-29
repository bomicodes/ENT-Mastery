"""Production entrypoint with the Pasha review subsystem registered last.

Importing runtime_entry first preserves all existing curriculum/practice repairs before
Pasha maps its review bank to the final live question objects.
"""
import runtime_entry
from interpretation_labs_cleanup_v250 import apply_interpretation_labs_cleanup_v250
from pasha_routes import bp as pasha_review_blueprint
from deep_curriculum_otology_v284 import apply_otology_etd_rebuild_v284

# Apply the source-grounded obstructive/patulous ETD rebuild to the fully assembled
# curriculum. Procfile launches runtime_entry_pasha:app, so this is the final production
# wiring point and prevents the v28.4 source module from being orphaned.
OTOLOGY_ETD_REBUILD_V284 = apply_otology_etd_rebuild_v284(
    runtime_entry.data,
    runtime_entry.app_mod,
)

# Rebuild the live Interpretation Atlas before the production app begins serving.
# This removes retired lab records/resources from the registry rather than hiding cards.
INTERPRETATION_LABS_CLEANUP_V250 = apply_interpretation_labs_cleanup_v250(
    runtime_entry.data,
    runtime_entry.app_mod,
)

app=runtime_entry.app
if "pasha_review" not in app.blueprints:
    app.register_blueprint(pasha_review_blueprint)
