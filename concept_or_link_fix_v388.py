"""v38.8: Concept Hub "OR Tomorrow" panel must prefer the OR-prep registry's
own linked_topic field over a word-overlap guess.

_concept_context_v1006 (app.py) built its related_or list purely from
same-domain OR_PREP_REGISTRY entries ranked by token overlap between the
concept's topic string and the OR case's *title* -- it never looked at
linked_topic, the field v38.4 (or_prep_linked_topic_fix_v384) exists
specifically to make authoritative. A case titled "Sistrunk Procedure"
shares no words with its own linked concept "Thyroglossal Duct Cyst", so it
lost the ranking to unrelated same-domain cases and never appeared on that
concept's page -- confirmed for 25 of 73 topics with a real OR-prep link.

This wraps _concept_context_v1006 to rank exact linked_topic matches first,
then fills any remaining slots with the previous overlap heuristic so
concepts without a dedicated OR case keep their existing "nearby" suggestions.
"""


def install_concept_or_link_fix_v388(app_module):
    original_context = app_module._concept_context_v1006

    def fixed_context(dname, mod):
        result = original_context(dname, mod)
        topic = mod.get("topic")
        linked = [
            op for op in app_module.OR_PREP_REGISTRY.values()
            if op.get("linked_topic") == topic
        ]
        if linked:
            linked_titles = {op.get("title") for op in linked}
            fallback = [o for o in result.get("related_or", []) if o.get("title") not in linked_titles]
            result["related_or"] = (linked + fallback)[:4]
        return result

    app_module._concept_context_v1006 = fixed_context
    return {"installed": True}
