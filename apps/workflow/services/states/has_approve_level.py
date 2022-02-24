from typing import Dict, Set

from apps.workflow.services.states.base import State


class HasApproveLevel(State):
    @property
    def accessible_permissions(self) -> Dict:
        return {
            # "CPD": "CPD1",
            # "CKS": "CKS1",
            "DPV": "DPV",
            "NVTTD": "NVTTD"
        }

    @property
    def possible_states(self) -> Set:
        return set()
