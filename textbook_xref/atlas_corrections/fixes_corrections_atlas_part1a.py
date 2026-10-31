"""Atlas review fixes for corrections_atlas_part1a.csv (CONFLICT rows)."""
ANATOMY_FIXES = [  # (or_slug, exact current text, replacement)
    # A-canalplasty.pimp4 (CONFLICT, Janfaza 1e p 426)
    ("canalplasty",
     "Gaps in the cartilaginous canal that allow infection or tumor to spread to the parotid and infratemporal region",
     "Fibrous-tissue-filled gaps in the cartilage of the lateral canal/tragus (inconstant in number and course) through which infection or tumor can spread to the parotid and infratemporal region"),
    # A-jugular-foramen-tumor.pimp1 (CONFLICT, Janfaza 1e p 495)
    ("jugular-foramen-tumor",
     "with X, XI, Arnold's nerve and the jugular bulb. Rhoton's",
     "with X, XI, Arnold's nerve and the jugular bulb. Janfaza describes three dural-septum compartments: anterior (IX, Jacobson's nerve, IPS), middle (X with Arnold's nerve, XI) and posterior (jugular bulb), which matches the two-part split once middle and posterior are grouped as pars vascularis. Rhoton's"),
    # A-tegmen-repair.landmark2 (CONFLICT, Janfaza 1e p 87)
    ("tegmen-repair",
     "Rounded bump on the middle fossa floor posteromedial to the tegmen, usually overlying",
     "Rounded bump on the middle fossa floor medial to the tegmen tympani (posteromedial in most operative descriptions; Janfaza describes it as anteromedial), usually overlying"),
]
OR_FIXES = [  # for OR-<slug>.stepN rows: text inside that OR card
]
