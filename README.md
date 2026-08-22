# ENT Mastery

A personal otolaryngology learning system designed for longitudinal board preparation, operative learning, active recall, case preparation, and chief-resident teaching.

## What works in this version

- Adaptive Today dashboard with 10/20/30/45-minute study presets
- Full-site search across topics, operations, anatomy, cases, and complications
- "Case Tomorrow" rapid prep
- Parathyroid Disease gold-standard module
- Active recall and board-style questions
- Confidence scoring and automatic mistake notebook
- Simple spaced repetition with persistent SQLite storage
- Clinical cases with progressive questions
- Attending Mode
- Chief / Teach-It Mode
- Operative Mastery / Viva
- Anatomy Lab
- Complication Lab
- Imaging/Pathology Lab shell
- Progress dashboard
- Full subspecialty architecture ready for content expansion
- Source labels and "Practice Update" callouts

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open http://127.0.0.1:5000

## Deploy to Render

1. Put this folder in a GitHub repository.
2. In Render, create a new Web Service from the repository.
3. Render will detect `render.yaml`, or manually use:
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
4. For durable progress data on Render, attach a persistent disk and set:
   `DATABASE_PATH=/var/data/ent_mastery.db`

## Educational use

This is a study tool, not a substitute for clinical judgment, local protocols, operative supervision, or the most current specialty guidance.
