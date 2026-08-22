ENT Mastery v6.0 — Adaptive + Deep Curriculum

WHAT CHANGED
1. Adaptive Daily Path
   - 15/20/30/45/60-minute sessions
   - mixed ENT or domain focus
   - prioritizes due reviews, unseen foundations, then next mastery step
   - learner rates Missed / Hard / Got it / Easy
   - persists concept mastery and next-due date in the existing PostgreSQL database
   - no new Render database is required; tables are created in the existing DB

2. Six-layer deep modules
   - Recognize
   - Localize
   - Work up
   - Manage
   - Operate
   - Teach / Boards
   38 high-yield deep modules across the core residency domains, producing 228 adaptive learning items.

3. Existing v5 curriculum retained
   - 229 mapped topics
   - integrated progressive cases
   - interpretation labs
   - OR Tomorrow
   - Attending Mode
   - thyroid/rhinology expansions

4. Evidence hierarchy
   - current guidelines for time-sensitive management
   - uploaded reference texts for anatomy/physiology/operative mental models
   - visual atlases for pattern recognition
   - ENT Mastery synthesis for retrieval/cases

DEPLOYMENT
Use the PATCH over the current v5 repository.
The app creates curriculum_mastery and daily_path_events tables automatically in the existing PostgreSQL DB.
No separate database should be provisioned.

VALIDATION
app.py, data.py and db.py compile successfully.
