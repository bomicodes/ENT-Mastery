# ENT Mastery

A personal otolaryngology learning system designed for longitudinal board preparation, operative learning, active recall, case preparation, and chief-resident teaching.

## What works in this version

- Adaptive Daily Path with 15/20/30/45/60-minute study presets
- Full-site search across curriculum concepts, operations, cases, interpretation, Clinical Challenges, and Concept Checks
- Clinical Challenges with board-style reasoning plus boards / overnight-call / postoperative-call / OR-prep focus tags
- Concept Checks for rapid active recall
- "OR Tomorrow" rapid prep
- Progressive clinical cases with staged reasoning
- Attending Mode and Chief / Teach-It Mode
- Interpretation Atlas and Anatomy Atlas
- Unified mastery, spaced review, and mistake tracking
- Deep curriculum organized across the full ENT subspecialty map
- Source labels and evidence references
- v16.8 reliability layer for canonicalized historical mastery, domain-safe concept routing, mobile navigation, route smoke testing, and optional private access

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app runtime_entry run --debug
```

Then open http://127.0.0.1:5000.

Use `runtime_entry` locally when you want the same assembled runtime used in production. Avoid `python app.py`: `app.py` contains legacy route definitions below its `__main__` block and is kept primarily as an imported application module.

## Deploy to Render

1. Connect the GitHub repository to a Render Web Service.
2. Use the repository `render.yaml` or equivalent service settings.
3. Production commands:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn runtime_entry:app`
4. Pin production Python to the same major/minor line as CI (`3.12`) so release checks and production execute the same runtime generation.
5. Durable learner progress should use PostgreSQL via `DATABASE_URL` (preferred). SQLite fallback uses `SQLITE_PATH`, not `DATABASE_PATH`.
6. Set `ENT_MASTERY_ACCESS_PASSWORD` in production to enable the private single-user access gate. Never commit the password to the repository.
7. `/health` is unauthenticated and can be used by the hosting platform for health checks.

## Persistence

PostgreSQL is the preferred production datastore. The v16.8 startup layer safely migrates retired concept IDs into current canonical IDs and merges keyed mastery rows instead of discarding history.

For local SQLite only:

```bash
export SQLITE_PATH=/absolute/path/to/ent_mastery.db
```

If `DATABASE_URL` is present, PostgreSQL takes precedence over SQLite.

## Quality gates

GitHub Actions now runs when runtime, persistence, hierarchy/canonicalization, template, CSS, JavaScript, deployment, or curriculum files change. The release gate includes:

- production boot preflight
- v16.8 route smoke and persistence/canonical-ID checks
- canonical topic/vignette coverage
- resident-level content quality
- learning-ladder depth
- six-layer curriculum depth
- duplicate architecture reporting
- full Concept Check bank audit

Canonical coverage remains strict; duplicate architecture remains informational while clinically distinct parent/child relationships are reviewed explicitly.

## Educational use

This is a study tool, not a substitute for clinical judgment, local protocols, operative supervision, or the most current specialty guidance.
