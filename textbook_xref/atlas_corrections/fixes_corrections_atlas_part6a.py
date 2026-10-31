"""Atlas review fixes for corrections_atlas_part6a.csv (CONFLICT rows)."""
ANATOMY_FIXES = [  # (or_slug, exact current text, replacement)
    # A-orbital-floor.danger1 (CONFLICT, Janfaza 1e p 155)
    ("orbital-floor",
     "about 40-45 mm from the infraorbital rim (range about 37-49 mm)",
     "often quoted as about 40-45 mm from the infraorbital rim (range about 37-49 mm); Janfaza gives average orbital depth from the rim to the optic strut as 45-55 mm, so stay well short of the apex on the floor"),
    # A-hypoglossal-stimulator.landmark2 (CONFLICT, Janfaza 1e p 517)
    ("hypoglossal-stimulator",
     "Bounded by the intermediate digastric tendon, the posterior border of mylohyoid and the hypoglossal nerve; the floor is hyoglossus",
     "Bounded by the intermediate digastric tendon (inferior), the hypoglossal nerve (superior) and the posterior border of mylohyoid (Pirogoff definition; Janfaza calls it Lesser's triangle and names only the tendon and XII); the floor is hyoglossus and it identifies the lingual artery"),
    # A-hypoglossal-stimulator.pimp4 (CONFLICT, Janfaza 1e p 517)
    ("hypoglossal-stimulator",
     "Intermediate digastric tendon, posterior border of mylohyoid and the hypoglossal nerve; floor is hyoglossus with the lingual artery deep to it",
     "Intermediate digastric tendon and the hypoglossal nerve, plus the posterior border of mylohyoid in the Pirogoff definition (Janfaza calls it Lesser's triangle and names only the tendon and XII); floor is hyoglossus with the lingual artery deep to it"),
]
OR_FIXES = [  # for OR-<slug>.stepN rows: text inside that OR card
]
