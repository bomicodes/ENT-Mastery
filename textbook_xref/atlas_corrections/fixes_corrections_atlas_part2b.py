"""Atlas review fixes for corrections_atlas_part2b.csv (CONFLICT rows)."""
ANATOMY_FIXES = [  # (or_slug, exact current text, replacement)
    # A-tors.landmark3 (CONFLICT, Atlas 2024 Ch 35 p 351)
    ("tors",
     "the ICA lies just posterior (deep) to the styloid muscles",
     "the ICA lies just deep to the styloid muscles (lateral to stylopharyngeus/styloglossus at the oropharynx, per the Atlas; posterior/deep from the transoral view)"),
]
OR_FIXES = [  # for OR-<slug>.stepN rows: text inside that OR card
]
