"""v27.0 quality alignment for reused General ENT application material."""

def apply_general_ent_v270_quality_fix(challenges):
    """Preserve the strong v139 triage case while making its stem runtime-substantive."""
    for q in challenges:
        if str(q.get("id")) == "v139_gen_04":
            q["stem"] = (
                "Several ENT consults arrive simultaneously overnight. Which patient should be evaluated first based on immediate physiologic risk?"
            )
            return {"updated": 1}
    raise RuntimeError("v270 quality fix missing reused case v139_gen_04")
