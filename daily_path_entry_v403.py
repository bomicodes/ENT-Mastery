"""Versioned entrypoint retaining all reviewed ENT Mastery v40.2 startup layers."""
import runtime_entry_pasha as production
from daily_path_integrity_v403 import install

# v50.1: new canonical topic (Eagle Syndrome). Installed first so the v40.3 text
# cleanup, the v47 textbook/OR-map validation, v49 bank indexing and the Daily Path
# index all see it as an ordinary topic.
from new_topic_eagle_v501 import install_eagle_topic_v501, install_eagle_refs_v501
EAGLE_TOPIC_V501 = install_eagle_topic_v501(production.runtime_entry.data,
                                            production.runtime_entry.app_mod)

DAILY_PATH_INTEGRITY_V403 = install(production.runtime_entry.data,
                                    production.runtime_entry.app_mod)
app = production.app

# v47.0: textbook-style Deep Curriculum (physiology/pathophysiology sections, curated
# OR/case links) and the rebuilt foundation-to-mastery Daily Path.  Installed last so
# nothing later in the chain can override the new routes.
from textbook_curriculum_v470 import install_textbook_curriculum_v470
from learning_path_v470 import install_learning_path_v470
from concept_checks_v471 import install_concept_checks_v471
from textbook_refs_v472 import install_textbook_refs_v472
from guideline_currency_v480 import install_guideline_currency_v480
from clinical_challenge_vignettes_v490 import install_clinical_challenge_vignettes_v490
from clinical_challenge_rewrites_v491 import install_clinical_challenge_rewrites_v491
from concept_check_curveballs_v492 import install_concept_check_curveballs_v492
from staging_section_v500 import install_staging_v500
from progress_reset_v521 import install_progress_reset_v521
from interpretation_atlas_v530 import install_interpretation_atlas_v530
from anatomy_section_v510 import install_anatomy_cases_v510
from or_card_fixes_v511 import install_or_card_fixes_v511
from anatomy_atlas_xref_v512 import install_anatomy_atlas_fixes_v512, install_or_atlas_fixes_v512

TEXTBOOK_CURRICULUM_V470 = install_textbook_curriculum_v470(
    production.runtime_entry.data, production.runtime_entry.app_mod, app)
# v47.1: replace the 309 templated Concept Checks before the Daily Path indexes them.
CONCEPT_CHECKS_V471 = install_concept_checks_v471(production.runtime_entry.data)
TEXTBOOK_XREF_V472 = install_textbook_refs_v472(production.runtime_entry.data, app)
EAGLE_REFS_V501 = install_eagle_refs_v501(production.runtime_entry.data)
GUIDELINE_CURRENCY_V480 = install_guideline_currency_v480(production.runtime_entry.data)
VIGNETTES_V490 = install_clinical_challenge_vignettes_v490(production.runtime_entry.data, production.runtime_entry.app_mod)
REWRITES_V491 = install_clinical_challenge_rewrites_v491(production.runtime_entry.data, production.runtime_entry.app_mod)
CC_CURVEBALLS_V492 = install_concept_check_curveballs_v492(production.runtime_entry.data)
STAGING_V500 = install_staging_v500(production.runtime_entry.data, app)
PROGRESS_RESET_V521 = install_progress_reset_v521(app)
ANATOMY_ATLAS_V512 = install_anatomy_atlas_fixes_v512(production.runtime_entry.data)
ANATOMY_CASES_V510 = install_anatomy_cases_v510(production.runtime_entry.data, production.runtime_entry.app_mod, app)
OR_CARD_FIXES_V511 = install_or_card_fixes_v511(production.runtime_entry.data)
OR_ATLAS_V512 = install_or_atlas_fixes_v512(production.runtime_entry.data)
INTERPRETATION_ATLAS_V530 = install_interpretation_atlas_v530(production.runtime_entry.data)
LEARNING_PATH_V470 = install_learning_path_v470(
    production.runtime_entry.data, production.runtime_entry.app_mod, app)
