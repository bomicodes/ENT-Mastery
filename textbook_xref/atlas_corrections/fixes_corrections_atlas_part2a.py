"""Atlas review fixes for corrections_atlas_part2a.csv (CONFLICT rows)."""
ANATOMY_FIXES = [  # (or_slug, exact current text, replacement)
    # A-free-flap-takeback.pimp3 (CONFLICT, Atlas 2024 Ch 50 p 543)
    ("free-flap-takeback",
     "Within the first 24-72 hours (most in the first 24 hours)",
     "Within the first few postoperative days (classically 24-72 h; the Atlas gives the first 3-5 days), so monitor hourly for the first 24-48 h"),
]
OR_FIXES = [  # for OR-<slug>.stepN rows: text inside that OR card
]
