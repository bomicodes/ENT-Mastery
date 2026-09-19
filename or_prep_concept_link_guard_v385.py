"""v38.5: Only advertise an OR-to-concept link when its topic resolves.

Uses the live resolver at render time so subsequent curriculum updates are honored.
"""


def install_or_prep_concept_link_guard_v385(app_module):
    def concept_resolves(domain, topic):
        if not topic:
            return False
        try:
            _, module = app_module._find_deep_module_v94(domain, topic)
            return module is not None
        except Exception:
            return False

    app_module.app.jinja_env.globals["concept_resolves"] = concept_resolves
    return {"registered": True}
