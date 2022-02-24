from typing import Set

from apps.workflow.services.states.base import State


class Reevaluating(State):
    @property
    def possible_states(self) -> Set:
        return set()
