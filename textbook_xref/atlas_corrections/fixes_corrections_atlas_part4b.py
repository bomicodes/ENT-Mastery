"""Atlas review fixes for corrections_atlas_part4b.csv (CONFLICT rows)."""
ANATOMY_FIXES = [  # (or_slug, exact current text, replacement)
    # A-tep.pimp1 (CONFLICT, Atlas 2024 p 406)
    ("tep",
     "(12 o'clock) about 5-10 mm below the stomal mucocutaneous junction",
     "(12 o'clock) about 5-15 mm below the stomal mucocutaneous junction (the Atlas specifies 1-1.5 cm for secondary puncture)"),
    # A-tep.danger3 (CONFLICT, Atlas 2024 p 406)
    ("tep",
     "Keep about 5-10 mm below the mucocutaneous junction",
     "Keep about 5-15 mm (Atlas: 1-1.5 cm) below the mucocutaneous junction"),
]
OR_FIXES = [  # for OR-<slug>.stepN rows: text inside that OR card
]
