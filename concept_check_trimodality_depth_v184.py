"""v18.4 focused clinical completion for the Base-of-Tongue SCC reveal.

The strict v18.4 gate correctly requires the senior decision to appear in the
answer itself, not only in the board pearl/common-trap metadata. Keep the gate
strict and make the runtime payload state the trimodality tradeoff explicitly.
"""

from concept_check_depth_v184 import COHORT

BOT_QID = "cc-v112-rec-head-neck-oncology-base-of-tongue-scc"
TRIMODALITY_SENTENCE = (
    " When adverse features make postoperative chemoradiation highly likely, avoid "
    "a transoral operation that creates predictable trimodality therapy without a "
    "compensating oncologic or functional benefit."
)


def apply_bot_trimodality_depth_v184():
    payload = COHORT[BOT_QID]
    answer = str(payload.get("answer_text") or "").strip()
    if "trimodality" not in answer.lower():
        payload["answer_text"] = answer + TRIMODALITY_SENTENCE
    return {"question_id": BOT_QID, "trimodality_explicit": "trimodality" in payload["answer_text"].lower()}


__all__ = ["apply_bot_trimodality_depth_v184"]
