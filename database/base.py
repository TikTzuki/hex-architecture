from datetime import datetime

from loguru import logger
from sqlalchemy import VARCHAR, Column, DateTime, String, create_engine, func
from sqlalchemy.orm import Session, as_declarative, declared_attr, sessionmaker
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
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class BaseModel(Base):
    __abstract__ = True

    created_at = Column("CREATED_AT", DateTime, default=datetime.now, server_default=func.now())

    created_by = Column("CREATED_BY", String(20), default=None)

    modified_at = Column("MODIFIED_AT", DateTime, default=datetime.now, onupdate=datetime.now,
                         server_default=func.now())

    modified_by = Column("MODIFIED_BY", String(20), default=None)

    uuid = Column("UUID", VARCHAR(50))
