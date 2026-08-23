ENT Mastery v10.0.6 — Concept Hub + Anatomy Image Reliability Fix

- Hardens /concept and /concept/id routes so related-content or mastery-profile failures no longer produce a 500.
- Makes Concept Hub template tolerant of missing profile fields.
- Simplifies Wikimedia image URLs and adds no-referrer loading.
- Adds a visible per-card source-image fallback if the remote image is blocked by the browser/CDN.
- Keeps all 50 anatomy image mappings.

If a specific Concept Hub still errors on Render, use the route traceback to identify the remaining production-only dependency.
