"""v15.5 — Pre-flight boot gate.

The single highest-priority process fix identified in the v15.x audit cycle:
the site was down for four consecutive daily passes because nothing in the
pipeline verified the app actually imports before more content was layered
on top of a broken commit.

This script does exactly one thing: import the real production entrypoint
and exit non-zero with a clear message if it throws. It intentionally does
NOT check content quality, coverage, or anything else - that is what the
other audit scripts are for. This script's only job is answering "does the
site currently start" before any of those other checks are allowed to run.

Usage (meant to be the first step of the daily pipeline, before any content
diffing/merging/committing is treated as final):

    python3 preflight_boot_check_v155.py
    # exit 0  -> site boots, safe to proceed
    # exit 1  -> site is broken, STOP. Do not layer more content on top.
                 Fix the reported error before doing anything else today.

Also usable as an importable function for a CI step or scheduled task runner:

    from preflight_boot_check_v155 import check_boot
    ok, detail = check_boot()
"""

import sys
import traceback


def check_boot():
    """Attempts to import the real production entrypoint.

    Returns (ok: bool, detail: str). Never raises - all failure modes are
    captured and returned as a message instead, since this function's whole
    purpose is to be the safe thing you call before trusting anything else.
    """
    try:
        import runtime_entry  # noqa: F401 - import is the test
    except Exception as exc:  # intentionally broad: ANY import-time failure
        tb = traceback.format_exc()
        last_line = tb.strip().splitlines()[-1]
        return False, f"{type(exc).__name__}: {last_line}\n\nFull traceback:\n{tb}"

    # Import succeeding isn't quite enough on its own - also confirm the
    # two objects everything else depends on actually exist and are sane.
    try:
        app = runtime_entry.app
        data = runtime_entry.data
        if not hasattr(app, "test_client"):
            return False, "runtime_entry.app does not look like a Flask app"
        total_topics = sum(len(m) for m in data.DEEP_MODULES_V6.values())
        total_vignettes = len(data.CLINICAL_CHALLENGES_V119)
        if total_topics == 0 or total_vignettes == 0:
            return False, (
                f"App imported but curriculum looks empty "
                f"(topics={total_topics}, vignettes={total_vignettes})"
            )
    except Exception as exc:
        return False, f"App imported but post-import sanity check failed: {exc}"

    # Cheap smoke test: actually render the homepage, not just import cleanly.
    try:
        app.config["TESTING"] = True
        with app.test_client() as c:
            resp = c.get("/")
            if resp.status_code != 200:
                return False, f"Homepage returned {resp.status_code}, expected 200"
    except Exception as exc:
        return False, f"Homepage smoke test raised: {exc}"

    return True, (
        f"OK — {total_topics} topics, {total_vignettes} vignettes, "
        f"homepage renders 200"
    )


if __name__ == "__main__":
    ok, detail = check_boot()
    if ok:
        print(f"PREFLIGHT_BOOT_CHECK|PASS|{detail}")
        sys.exit(0)
    else:
        print(f"PREFLIGHT_BOOT_CHECK|FAIL|{detail}")
        print()
        print(
            "STOP. The site does not currently boot. Do not add, merge, or "
            "commit any further content until this is fixed — a broken boot "
            "blocks every single page, regardless of how good today's new "
            "content is. Fix this specific error first, verify with this "
            "script again, then proceed with the rest of the daily pass."
        )
        sys.exit(1)
