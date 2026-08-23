ENT Mastery v9.2.1 Render Hotfix

Cause addressed:
v9.2 pinned psycopg[binary]==3.2.9. Render is using Python 3.14.
Use psycopg[binary]==3.3.4, which provides CPython 3.14 wheels.

Apply this patch on top of the current v9.2 + Interpretation Atlas rename repository.
No other files need to be reverted.
