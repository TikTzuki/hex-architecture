from sqlalchemy.orm import Session

from .base import Base


class Service(Base):
    """
    Controller use business
    """

    def __init__(
            self,
            oracle_session: Session = None,
            current_user=None
    ):
        super().__init__()
        self.warnings = []
        self.current_user = current_user
        self.oracle_session: Session = oracle_session
