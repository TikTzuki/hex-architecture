from typing import Dict, Set

from apps.workflow.services.states.base import Context, State


class HasApprover(State):
    def __init__(self, ctx: Context, user_cpd, user_cks):
        super().__init__(ctx)

    @property
    def possible_states(self) -> Set:
        return set()

    @property
    def accessible_permissions(self) -> Dict:
        return {
            "CPD": "CPD1",
            "CKS": "CKS1",
            # "DPV": "DPV",
            # "NVTTD": "NVTTD"
        }
