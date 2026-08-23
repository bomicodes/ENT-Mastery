ENT Mastery v9.3 — Coherence + Integration

This patch does not add broad medical content. It makes the existing curriculum behave like one product.

Changes
1. Legacy routes now redirect into the modern curriculum:
   /today → Daily Path
   /learn → Curriculum
   /questions → Daily Path
   /cases → Integrated Cases
   /operate → OR Tomorrow
   /anatomy and /complications → Deep Curriculum
   /chief → Attending / Chief level

2. Dashboard, Progress, and Mistakes now use one unified learner read model across:
   - Daily Path
   - Progressive/Integrated Cases
   - Attending/Chief mastery events
   - Interpretation Atlas

3. Mastery no longer overstates a concept from a single attempted dimension.
   Overall mastery counts untested dimensions as 0 and shows Coverage separately (x/7 dimensions).

4. Daily Path is more curricular:
   - due reviews can come from anywhere
   - most new material stays in one anchor domain
   - explicitly mapped prerequisites block premature advanced concepts
   - unseen material is ordered by curriculum sequence
   - questions are aligned to the stored stage answer rather than forcing a generic “dangerous alternative” prompt

5. Dashboard Integrated Cases show 6 recommendations instead of all 50.

6. Chief Mode is consolidated into Attending / Chief Mode.

7. Sidebar is simplified to the primary resident workflow.

No new Render service or database is required.
