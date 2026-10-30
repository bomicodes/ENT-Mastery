"""Versioned entrypoint retaining all reviewed ENT Mastery v40.2 startup layers."""
import runtime_entry_pasha as production
from daily_path_integrity_v403 import install

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
from staging_section_v500 import install_staging_v500

TEXTBOOK_CURRICULUM_V470 = install_textbook_curriculum_v470(
    production.runtime_entry.data, production.runtime_entry.app_mod, app)
# v47.1: replace the 309 templated Concept Checks before the Daily Path indexes them.
CONCEPT_CHECKS_V471 = install_concept_checks_v471(production.runtime_entry.data)
TEXTBOOK_XREF_V472 = install_textbook_refs_v472(production.runtime_entry.data, app)
GUIDELINE_CURRENCY_V480 = install_guideline_currency_v480(production.runtime_entry.data)
VIGNETTES_V490 = install_clinical_challenge_vignettes_v490(production.runtime_entry.data, production.runtime_entry.app_mod)
REWRITES_V491 = install_clinical_challenge_rewrites_v491(production.runtime_entry.data, production.runtime_entry.app_mod)
STAGING_V500 = install_staging_v500(production.runtime_entry.data, app)
LEARNING_PATH_V470 = install_learning_path_v470(
    production.runtime_entry.data, production.runtime_entry.app_mod, app)
