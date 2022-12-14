from datetime import date
from enum import Enum
from typing import Any, Generic, List, TypeVar, Union

from pydantic import BaseModel, Field, validator
from pydantic.fields import ModelField
from pydantic.generics import GenericModel
from pydantic.json import timedelta_isoformat
from pydantic.schema import datetime, timedelta

TypeX = TypeVar("TypeX")


class CustomBaseModel(BaseModel):
    class Config:
        json_encoders = {
            datetime: lambda v: v.timestamp(),
            date: lambda v: datetime(v.year, v.month, v.day).timestamp(),
            timedelta: timedelta_isoformat
        }
        orm_mode = True

    @validator('*', pre=True)
    def datetime_or_date_to_timestamp(cls, v, **kwargs):
        if v == "":
            raise ValueError('value is not null')
        val: ModelField = kwargs['field']
        if val.type_ is datetime or val.type_ is date:
            if v is not None:
                # check kieu
                data = True
                try:
                    int(float(v))
                except Exception:
                    data = False

                if type(v) is datetime or type(v) is date:
                    return v.replace(tzinfo=None)
                elif type(v) is int or type(v) is float or data:
                    try:
                        element = datetime.fromtimestamp(int(float(v)))
                        return element
                    except Exception:
                        raise ValueError(f'{v} is not valid 1')
                elif type(v) is str and val.type_ is datetime:
                    try:
                        datetime.strptime(v, '%Y-%m-%dT%H:%M:%S').timestamp()
                    except Exception:
                        raise ValueError(f'{v} is not valid 2')
                elif type(v) is str and val.type_ is date:
                    try:
                        datetime.strptime(v, '%Y-%m-%d').timestamp()
                    except Exception:
                        raise ValueError(f'{v} is not valid 3')
        return v


class CustomGenericModel(CustomBaseModel, GenericModel):
    ...


class Warn(BaseModel):
    loc: List[Union[str, int]] = []
    code: str = None
    msg: str = None

    class Config:
        schema_extra = {
            'example': {
                'loc': ['body', 'username'],
                'code': 'USERNAME_IS_EXITS',
                'msg': 'username is exits'
            }
        }


class PageResponse(CustomGenericModel, Generic[TypeX]):
    data: List[TypeX]
    total_items: int = 0
    total_page: int = 0
    current_page: int = 0
    warning: List[Warn] = []


class Page(CustomGenericModel, Generic[TypeX]):
    data: List[TypeX]
    total_items: int = 0
    total_page: int = 0
    current_page: int = 0
    warning: List[Warn] = []


class DataResponse(CustomGenericModel, Generic[TypeX]):
    data: TypeX = None
    warning: List[Warn] = []

    def __init__(self, data: TypeX, **kwargs: Any):
        kwargs.update(data=data)
        super().__init__(**kwargs)


# PAGING
class Sort(BaseModel):
    class Direction(str, Enum):
        ASC = "asc"
        DESC = "desc"

    order_by: str = None
    direction: Direction = None


class Pageable(BaseModel):
    sort: Sort = Field(None)
    limit: int = Field(20, gt=0)
    page: int = Field(1, gt=0)

    def __init__(self, limit, page, direction: Sort.Direction = Sort.Direction.DESC, order_by=None):
        super().__init__()
        self.sort = Sort(order_by=order_by, direction=direction)
        self.limit = limit
        self.page = page

    @classmethod
    def non_sort(cls, page: int = 1, limit: int = 100):
        return cls(limit, page)


# Deprecated
class ExceptionRes(CustomBaseModel):
    class Error(BaseModel):
        loc: List[Union[str, int]] = []
        code: str = None
        msg: str = None

    detail: List[Error]
