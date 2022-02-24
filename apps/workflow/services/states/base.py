import abc
from typing import Dict, Set


class Context(metaclass=abc.ABCMeta):
    def __init__(self, state: 'State'):
        self.state = state

    def set_state(self, state: 'State') -> None:
        self.state = state


class State(metaclass=abc.ABCMeta):

    def __init__(self, ctx: Context):
        self.ctx = ctx

    @property
    @abc.abstractmethod
    def possible_states(self) -> Set:
        ...

    @property
    @abc.abstractmethod
    def accessible_permissions(self) -> Dict:
        ...
