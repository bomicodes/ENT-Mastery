ENT Mastery v12.0 — Dynamic Content Registry

Fixes the late-added-topic orphaning bug structurally.

Daily Path:
- Adaptive items are now generated from the final DEEP_MODULES_V6 at request time.
- Any topic present in DEEP_MODULES_V6 automatically gets Recognize / Localize / Workup / Manage / Operate / Teach items.
- The three v11.9 allergy topics therefore receive 18 adaptive items immediately.
- v11.4 curated prerequisite gating is unchanged.

Chief / Attending:
- The existing curated 309-topic v11.7 banks are preserved.
- Bespoke Chief and Attending prompts were added for the three new allergy topics.
- Any future topic missing from the curated banks receives a dynamic fallback prompt instead of disappearing.

Curriculum:
- The existing curated sequence remains intact.
- The three allergy additions are added to a visible Allergy / Immunology strand in Rhinology / Allergy / Skull Base.
- This prevents late-added topics from being invisible in the sequence view.

This change is intended to prevent the same file-ordering bug from recurring in future domain expansions.
