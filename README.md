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

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
flask --app app run --debug
```

Then open http://127.0.0.1:5000.

`flask --app app run` is preferred over `python app.py` because it imports the complete module before starting the development server, including routes defined in the later adaptive-curriculum section.

## Deploy to Render

1. Put this folder in a GitHub repository.
2. In Render, create or connect the Web Service from the repository.
3. Render can use `render.yaml`; the production start command is:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn runtime_entry:app`
4. `runtime_entry.py` imports the fully assembled `wsgi` runtime and adds lightweight production integrations such as practice-bank search discovery.
5. For durable progress data on Render, attach a persistent disk and set:
   `DATABASE_PATH=/var/data/ent_mastery.db`

## Quality gates

- Canonical topic/vignette coverage is checked in GitHub Actions and must stay at 100%.
- `audit_quality_v149.py` separately measures resident-level question quality, distractor reasoning, decision-depth, duplicate stems, and answer-position bias. It is intentionally informational while remaining content debt is upgraded rather than hidden.

## Educational use

This is a study tool, not a substitute for clinical judgment, local protocols, operative supervision, or the most current specialty guidance.
