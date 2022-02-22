from datetime import datetime

from loguru import logger
from sqlalchemy import VARCHAR, Column, DateTime, String, func
from sqlalchemy import create_engine
from sqlalchemy.orm import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import NullPool

from project.settings.configs import DATABASES

engine = create_engine(DATABASES.oracle.url, poolclass=NullPool)
session_factory = sessionmaker(engine, expire_on_commit=False)


def get_session() -> Session:
    """Provide a transactional scope around a series of operations."""
    session = session_factory()
    try:
        yield session
    except Exception as e:
        logger.exception(e)
        session.rollback()
    finally:
        session.commit()
        session.close()


@as_declarative()
class Base:
    __name__: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @declared_attr
    def __tablename__(cls) -> str:  # noqa
        return cls.__name__.lower()


@as_declarative()
class BaseUtils:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:  # noqa
        return cls.__name__.lower()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    created_at = Column("CREATED_AT", DateTime, default=datetime.now, server_default=func.now())

    created_by = Column("CREATED_BY", String(20), default=None)

    modified_at = Column("MODIFIED_AT", DateTime, default=datetime.now, onupdate=datetime.now,
                         server_default=func.now())

    modified_by = Column("MODIFIED_BY", String(20), default=None)

    uuid = Column("UUID", VARCHAR(50))
