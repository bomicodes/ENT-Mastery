"""Production entrypoint with the Pasha review subsystem registered last.

Importing runtime_entry first preserves all existing curriculum/practice repairs before
Pasha maps its review bank to the final live question objects.
"""
import runtime_entry
from interpretation_labs_cleanup_v250 import apply_interpretation_labs_cleanup_v250
from pasha_routes import bp as pasha_review_blueprint
from deep_curriculum_otology_v284 import apply_otology_etd_rebuild_v284
from deep_curriculum_production_chain_v314 import apply_deep_curriculum_production_chain_v314
from or_tonsil_hemorrhage_rescue_v281 import apply_or_tonsil_hemorrhage_rescue_v281
from or_thyroid_hematoma_rescue_v282 import apply_or_thyroid_hematoma_rescue_v282
from or_tracheostomy_hemorrhage_rescue_v283 import apply_or_tracheostomy_hemorrhage_rescue_v283
from or_septal_hematoma_rescue_v284 import apply_or_septal_hematoma_rescue_v284
from or_esophageal_perforation_rescue_v285 import apply_or_esophageal_perforation_rescue_v285
from or_laryngectomy_fistula_rescue_v287 import apply_or_laryngectomy_fistula_rescue_v287
from or_airway_fire_rescue_v288 import apply_or_airway_fire_rescue_v288
from or_posterior_epistaxis_rescue_v289 import apply_or_posterior_epistaxis_rescue_v289
from or_tep_prosthesis_rescue_v290 import apply_or_tep_prosthesis_rescue_v290

# Apply the source-grounded obstructive/patulous ETD rebuild to the fully assembled
# curriculum. Procfile/Render launches runtime_entry_pasha:app, so this is the final
# production wiring point.
OTOLOGY_ETD_REBUILD_V284 = apply_otology_etd_rebuild_v284(
    runtime_entry.data,
    runtime_entry.app_mod,
)

# Restore and execute the cumulative source-grounded Concept Hub audit chain added
# after v28.4. This intentionally runs before the app begins serving and includes the
# current v31.4 goals-of-care/palliative-intervention distinction.
DEEP_CURRICULUM_PRODUCTION_CHAIN_V314 = apply_deep_curriculum_production_chain_v314(
    runtime_entry.data,
    runtime_entry.app_mod,
)

# Apply the source-grounded post-tonsillectomy hemorrhage rescue to the same final OR
# registry served by /case-tomorrow. Keep this after the historical OR assembly so the
# rescue cannot be overwritten by an earlier generic postoperative layer.
OR_TONSIL_HEMORRHAGE_RESCUE_V281 = apply_or_tonsil_hemorrhage_rescue_v281(
    runtime_entry.data.OR_PREP_REGISTRY,
)

# Apply the post-thyroidectomy hematoma rescue at the same final production boundary.
# This deliberately runs after the historical thyroid/OR assembly so bedside SCOOP
# choreography and its source trail cannot be overwritten by an older generic layer.
OR_THYROID_HEMATOMA_RESCUE_V282 = apply_or_thyroid_hematoma_rescue_v282(
    runtime_entry.data.OR_PREP_REGISTRY,
)

# Apply tracheostomy hemorrhage/TIF rescue at the final OR boundary as well. This keeps
# the established fresh-tract rescue intact while adding sentinel-bleed recognition,
# cuff/digital temporary control and definitive vascular escalation after all older OR
# layers have assembled the live registry.
OR_TRACHEOSTOMY_HEMORRHAGE_RESCUE_V283 = apply_or_tracheostomy_hemorrhage_rescue_v283(
    runtime_entry.data.OR_PREP_REGISTRY,
)

# Extend the recognition-only septoplasty warning into an executable septal
# hematoma/abscess rescue after all historical postoperative layers have run.
OR_SEPTAL_HEMATOMA_RESCUE_V284 = apply_or_septal_hematoma_rescue_v284(
    runtime_entry.data.OR_PREP_REGISTRY,
)

# Convert recognition-only post-esophagoscopy perforation warnings into an executable
# cervical esophageal leak pathway after every historical OR management layer has run.
OR_ESOPHAGEAL_PERFORATION_RESCUE_V285 = apply_or_esophageal_perforation_rescue_v285(
    runtime_entry.data.OR_PREP_REGISTRY,
)

# Add a final-boundary post-laryngectomy PCF pathway so salivary-leak surveillance,
# nutrition, vessel protection and reconstructive escalation cannot be overwritten by
# older generic postoperative content.
OR_LARYNGECTOMY_FISTULA_RESCUE_V287 = apply_or_laryngectomy_fistula_rescue_v287(
    runtime_entry.data.OR_PREP_REGISTRY,
)

# Extend the existing shared-airway fire-safety stop point into an executable fire
# rescue after all historical microlaryngoscopy/RRP layers have assembled the registry.
OR_AIRWAY_FIRE_RESCUE_V288 = apply_or_airway_fire_rescue_v288(
    runtime_entry.data.OR_PREP_REGISTRY,
)

# Deepen the existing SPA-ligation card at the final OR boundary so hemorrhage
# stabilization, complete branch control, failure analysis, and selective embolization
# escalation cannot be overwritten by the historical rhinology management layer.
OR_POSTERIOR_EPISTAXIS_RESCUE_V289 = apply_or_posterior_epistaxis_rescue_v289(
    runtime_entry.data.OR_PREP_REGISTRY,
)

# Convert the recognition-only TEP dislodgement warning into a laryngectomy-airway,
# aspirated-prosthesis and tract-preservation rescue after all older management layers
# have assembled the live card.
OR_TEP_PROSTHESIS_RESCUE_V290 = apply_or_tep_prosthesis_rescue_v290(
    runtime_entry.data.OR_PREP_REGISTRY,
)
runtime_entry.app_mod.OR_PREP_REGISTRY = runtime_entry.data.OR_PREP_REGISTRY

# Rebuild the live Interpretation Atlas before the production app begins serving.
# This removes retired lab records/resources from the registry rather than hiding cards.
INTERPRETATION_LABS_CLEANUP_V250 = apply_interpretation_labs_cleanup_v250(
    runtime_entry.data,
    runtime_entry.app_mod,
)

app=runtime_entry.app
if "pasha_review" not in app.blueprints:
    app.register_blueprint(pasha_review_blueprint)