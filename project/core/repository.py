from loguru import logger
from sqlalchemy.orm import Session
from starlette import status

from . import error_code
from .base import Base
from .exception import LOSException


class RepositoryBase(Base):

    def __init__(self, oracle_session=None):
        super().__init__()
        self.oracle_session: Session = oracle_session

    async def add_and_flush(self, type_, **kwargs):
        try:
            obj = type_(**kwargs)
            self.oracle_session.add(obj)
            self.oracle_session.flush()
            return obj
        except Exception as e:
            logger.exception(e)
            raise LOSException.with_error(loc=[f"add_and_flush(type={type_})"], code=error_code.DATABASE_INSERT_FAILED, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
