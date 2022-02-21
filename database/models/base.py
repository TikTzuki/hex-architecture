from loguru import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.pool import NullPool

from app.settings.database import ORACLE_CONFIG

DATABASE_URL = "oracle+cx_oracle://{username}:{password}@{host}:{port}/?service_name={service_name}".format_map({
    'host': ORACLE_CONFIG['host'],
    'port': ORACLE_CONFIG['port'],
    'username': ORACLE_CONFIG['username'],
    'password': ORACLE_CONFIG['password'],
    'service_name': ORACLE_CONFIG['service_name']
})

engine = create_engine(
    DATABASE_URL,
    poolclass=NullPool
)
SessionLocal = sessionmaker(
    engine,
    expire_on_commit=False
)


def get_session():
    """Provide a transactional scope around a series of operations."""
    session = SessionLocal()
    try:
        yield session
    except Exception as e:
        logger.exception(e)
        session.rollback()
    finally:
        session.commit()
        session.close()
