"""Atlas review fixes for corrections_atlas_part1b.csv (CONFLICT rows).

Not applied: A-retrosigmoid-skull-base.pimp2 -- the current answer is the bare string "AICA", which
also occurs in nine other strings of that case; an exact-substring replacement cannot target only the
pimp answer. The current answer already matches the usual teaching (and the question says "usually").
"""
ANATOMY_FIXES = [  # (or_slug, exact current text, replacement)
    # A-csf-nasoseptal.landmark2 (CONFLICT, Janfaza 1e p 312)
    ("csf-nasoseptal",
     "preserve during sphenoidotomy (open the ostium superiorly and medially, not inferiorly)",
     "preserve during sphenoidotomy: when a nasoseptal flap may be needed, enlarge the ostium superiorly and medially (away from the posterior septal artery) while staying below the skull base; the classic rule of inferomedial enlargement (Janfaza) avoids lateral sphenopalatine injury but endangers the pedicle"),
    # A-csf-nasoseptal.danger6 (CONFLICT, Janfaza 1e p 312)
    ("csf-nasoseptal",
     "Harvest early; widen the sphenoidotomy superiorly;",
     "Harvest early; when the flap pedicle must be kept, widen the sphenoidotomy superiorly and medially rather than inferiorly, staying below the planum/skull base (Janfaza's general rule is inferomedial enlargement);"),
]
OR_FIXES = [  # for OR-<slug>.stepN rows: text inside that OR card
]
