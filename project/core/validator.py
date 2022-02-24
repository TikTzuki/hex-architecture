from typing import Optional

from sqlalchemy.orm import Session

from .base import Base


class Validator(Base):
    def __init__(self, oracle_session: Session = None, current_user=None):
        super().__init__()
        self.current_user = current_user
        self.oracle_session: Optional[Session] = oracle_session
