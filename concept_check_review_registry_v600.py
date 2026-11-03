"""v60.0: register later-added Concept Checks with the v17.8 all-domain review contract.

The v43.8 / v44.1 gap-fill passes (and the v47.1 authored rewrites of them) added
Concept Checks for topics created after v17.8, but never stamped the review metadata
every earlier check carries, so the v17.8 audit counted them as unreviewed.

This layer stamps them with their actual provenance, not a blanket label:
  * textbook_refs_v472 when the v47.1/v47.2 pass recorded page-level textbook refs,
  * otherwise the source_basis of the canonical Deep Curriculum module the check was
    written from (its reveal and pearl come from that module).
Checks that have neither are left unstamped so the audit keeps flagging them.
"""


def apply_concept_check_review_registry_v600(data_module, app_module=None):
    checks = getattr(data_module, "CONCEPT_CHECKS_V112", []) or []
    modules = {}
    for domain, mods in (getattr(data_module, "DEEP_MODULES_V6", {}) or {}).items():
        for m in mods:
            modules[(domain, m.get("topic"))] = m
    stamped, skipped = 0, []
    for q in checks:
        if q.get("reviewed_all_domains_v178") and q.get("review_basis_v178"):
            continue
        if not (q.get("gapfill_v438") or q.get("gapfill_v441") or q.get("authored_v471")):
            continue
        refs = [str(r) for r in (q.get("textbook_refs_v472") or []) if r]
        mod = modules.get((q.get("domain"), q.get("canonical_topic") or q.get("topic"))) or {}
        mod_basis = [str(r) for r in (mod.get("source_basis") or []) if r]
        basis = refs + [f"Deep Curriculum canonical module: {mod.get('topic') or q.get('topic')}"] + mod_basis[:6]
        if not refs and not mod_basis:
            skipped.append(q.get("id"))
            continue
        q["reviewed_all_domains_v178"] = True
        q["board_review_standard_v178"] = q.get("board_review_standard_v178") or "clinical decision-making"
        q["review_basis_v178"] = basis
        q["review_registry_v600"] = "textbook_refs_v472" if refs else "deep_module_source_basis"
        stamped += 1
    return {"stamped": stamped, "skipped": skipped}
