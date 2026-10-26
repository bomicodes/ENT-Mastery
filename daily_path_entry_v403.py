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

TEXTBOOK_CURRICULUM_V470 = install_textbook_curriculum_v470(
    production.runtime_entry.data, production.runtime_entry.app_mod, app)
# v47.1: replace the 309 templated Concept Checks before the Daily Path indexes them.
CONCEPT_CHECKS_V471 = install_concept_checks_v471(production.runtime_entry.data)
LEARNING_PATH_V470 = install_learning_path_v470(
    production.runtime_entry.data, production.runtime_entry.app_mod, app)
