import json
from datetime import datetime
from typing import Dict, List, Union

from sqlalchemy import VARCHAR, Column, DateTime, String, TypeDecorator, func
from sqlalchemy.orm import as_declarative, declarative_base, declared_attr


# Dành cho những model nào không có field (created_at, created_by,modified_at,modified_by, uuid)
@as_declarative()
class Base:
    __name__: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @declared_attr
    def __tablename__(cls) -> str:  # noqa
        return cls.__name__.lower()


# Dành cho những model nào có field (created_at, created_by,modified_at,modified_by, uuid)
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


class JSONSQL(TypeDecorator):

    @property
    def python_type(self):
        return Union[List, Dict]

    impl = VARCHAR

    def process_bind_param(self, value, dialect):
        if value is None:
            return None
        return json.dumps(value)

    def process_result_value(self, value, dialect):
        if not value:
            return None
        return json.loads(value)


BaseModel = declarative_base(cls=BaseUtils)
