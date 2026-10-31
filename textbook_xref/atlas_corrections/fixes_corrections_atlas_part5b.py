"""Atlas review fixes for corrections_atlas_part5b.csv (CONFLICT rows)."""
ANATOMY_FIXES = [  # (or_slug, exact current text, replacement)
    # A-frontal-sinus-trauma.landmark5 (CONFLICT, Janfaza 1e p 44)
    ("frontal-sinus-trauma",
     "(0.5 cm below the tragus to 1.5 cm above the lateral brow)",
     "(0.5 cm below the tragus to about 1.5-2 cm above the lateral brow; Janfaza uses 2 cm)"),
    # A-frontal-sinus-trauma.pimp5 (CONFLICT, Janfaza 1e p 44)
    ("frontal-sinus-trauma",
     "From 0.5 cm below the tragus to 1.5 cm above the lateral brow, approximating",
     "From 0.5 cm below the tragus to about 1.5-2 cm above the lateral brow (Janfaza uses 2 cm), approximating"),
]
OR_FIXES = [  # for OR-<slug>.stepN rows: text inside that OR card
]
