"""Atlas review fixes for corrections_atlas_part3a.csv (CONFLICT rows)."""
ANATOMY_FIXES = [  # (or_slug, exact current text, replacement)
    # A-parotid-total.pimp2 (CONFLICT, Atlas 2024 p 162 | Janfaza 1e p 42)
    ("parotid-total",
     "Tragal pointer, tympanomastoid suture, posterior belly of digastric, styloid process (and mastoid tip)",
     "Tragal pointer, tympanomastoid suture and posterior belly of digastric (and mastoid tip); the styloid can be palpated (nerve exits just posterior to it, per Janfaza) but the Atlas warns against dissecting onto it because it lies deep to the nerve"),
    # A-parotidectomy.landmark4 (CONFLICT, Janfaza 1e p 44)
    ("parotidectomy",
     "about 0.5 cm below the tragus to about 1.5 cm above the lateral brow",
     "about 0.5 cm below the tragus to about 1.5-2 cm above the lateral brow (Pitanguy 1.5 cm; Janfaza 2 cm)"),
    # A-parotidectomy.danger2 (CONFLICT, Atlas 2024 p 191)
    ("parotidectomy",
     "(Dingman and Grabb: about 1 in 5, within about 1 cm)",
     "(Dingman and Grabb: about 1 in 5, usually within about 1 cm, but loops up to 3 cm below the mandible are described (Atlas))"),
]
OR_FIXES = [  # for OR-<slug>.stepN rows: text inside that OR card
]
