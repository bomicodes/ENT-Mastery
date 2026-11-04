FIXES = {
    # v64.0: the source question was rewritten (Pasha audit) so it no longer contradicts
    # v135_fprs_02 (alar sidewall collapse over weak lateral crura -> batten grafts).
    "v11_fprs_05": {"mode": "trim", "cards": [
        {"front": "Narrow middle vault with inspiratory collapse at the upper lateral cartilage, relieved by lifting it off the septum: cause?",
         "back": "Internal valve weakness from flaccid upper lateral cartilages (treat with spreader grafts or flaps)"}]},
    # v69.0: third card duplicated v11_fprs_01~2 (dead-space closure after septal hematoma drainage).
    "v490-topup-facial-44": {"mode": "split", "cards": [
        {"front": 'Septal hematoma in an anticoagulated patient: drain now or after INR correction?',
         "back": 'Drain now; correct INR at the same time'},
        {"front": 'Undrained septal hematoma: nasal deformity it can cause?',
         "back": 'Saddle nose'}]},
}
