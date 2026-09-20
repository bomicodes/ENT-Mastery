"""Versioned entrypoint retaining all reviewed ENT Mastery v40.2 startup layers."""
import runtime_entry_pasha as production
from daily_path_integrity_v403 import install

DAILY_PATH_INTEGRITY_V403 = install(production.runtime_entry.data,
                                    production.runtime_entry.app_mod)
app = production.app
