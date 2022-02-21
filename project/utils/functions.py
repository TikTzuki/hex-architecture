import decimal
import uuid
from datetime import date, datetime
from typing import Callable, Collection, Dict, List, Set, Tuple, Union

from pydantic import UUID4
from pydantic.fields import ModelField

from app.repositories.utils.repo_utils import repo_base_get_utdm_by_fields_name
from app.third_party.core.schemas import CustomBaseModel


def today():
    """
    get today
    :return: date
    """
    return date.today()


def get_current_date():
    return datetime.now()


def fields_required(fields: Union[Dict, List, Set, str, int], data_check: Union[Dict, List]) -> (bool, List):
    _data_check = []
    if isinstance(data_check, Dict):
        _data_check.append(data_check)
    elif isinstance(data_check, List):
        _data_check = [*_data_check, *data_check]

    _fields = set()
    if isinstance(fields, (List, Tuple, Set)):
        _fields = {*list(data_check)}
    elif isinstance(fields, (str, int)):
        _fields.add(fields)

    miss_key = set()

    for temp in _data_check:
        if isinstance(data_check, Dict):
            _key = set(temp.keys()) - _fields
            if _key:
                miss_key = {*miss_key, *_key}
        else:
            miss_key = _fields
            break
    if miss_key:
        return False, miss_key
    return True, None


def generate_uuid() -> str:
    """
    :return: str
    """
    return str(uuid.uuid4())


def set_id_after_inserted(schema, db_model):
    """
    Cần set uuid từ model vừa insert dưới db SQL lên schema của object tương ứng với đối tượng đó để insert vào mongdb
    :param schema:
    :param model:
    :return:
    """
    schema.set_uuid(db_model.uuid)


def travel_dict(d: dict, process_func: Callable):
    process_func(d)
    if isinstance(d, Dict):
        for key, value in d.items():
            if type(value) is dict:
                travel_dict(value, process_func)
            elif isinstance(value, (list, set, tuple,)):
                for item in value:
                    travel_dict(item, process_func)
            else:
                process_func((key, value))
    return d


def travel_dict_v2(d: dict, process_funcs: List[Callable]):
    for func in process_funcs:
        func(d)
    if isinstance(d, Dict):
        for key, value in d.items():
            if type(value) is dict:
                travel_dict_v2(value, process_funcs)
            elif isinstance(value, (list, set, tuple,)):
                for item in value:
                    travel_dict_v2(item, process_funcs)
            else:
                for func in process_funcs:
                    func((key, value))
    return d


def process_generate_uuid(d):
    if isinstance(d, dict) and ("uuid" in d) and (d["uuid"] is None):
        d.update({"uuid": generate_uuid()})


def process_generate_uuid4(d):
    if isinstance(d, dict) and ("uuid" in d) and (d["uuid"] is None):
        d.update({"uuid": uuid.uuid4()})


def convert_to_num(n):
    if not n:
        return None
    try:
        n = float(n)
    except ValueError:
        return None

    if float(n).is_integer():
        return int(n)

    return float(n)


def is_integer_num(n):
    if not n:
        return None
    try:
        float(n)
    except ValueError:
        return 0

    if float(n).is_integer():
        return int(n)

    return float(n)


async def get_data_udtm_by_fields_name(oracle_session, fields_name: list) -> dict:
    """
        Lấy dữ liệu table UDTM dựa theo fields_name

        :params :
            - field_name: [ABLE_PAY_LABEL, ACCEPT_CREDIT_LABEL, ...]

        :response:
            data = {
                ABLE_PAY_LABEL: [Y, N,..],
                ACCEPT_CREDIT_LABEL: [Y, N,..],
            }
    """

    is_status, data_udtm = await repo_base_get_utdm_by_fields_name(
        oracle_session=oracle_session,
        fields_name=fields_name
    )
    if not is_status:
        return {}
    data = {}
    for udtm in data_udtm:
        if data.get(udtm.field_name):
            data[udtm.field_name].append(udtm.lov)
        else:
            data[udtm.field_name] = [udtm.lov]
    return data


def los_round(num, d_places):
    rs = float(decimal.Decimal(str(num)).quantize(decimal.Decimal('0.' + ('0' * d_places)), rounding=decimal.ROUND_HALF_UP))
    return rs


def to_lower_dash(s: str):
    return s.lower().replace("_", "-")


def insert_body(e):
    loc = list(e["loc"])
    loc.insert(0, "body")
    e["loc"] = tuple(loc)
    return e


def insert_pre_loc(e: Dict, loc: Collection = ("body",)) -> Dict:
    e["loc"] = (*loc, *e["loc"],)
    return e


def insert_pre_locs(errors: List[Dict], pre_loc=("body",)) -> List[Dict]:
    for e in errors:
        insert_pre_loc(e, pre_loc)
    return errors


def travel_schema(schema: CustomBaseModel, process_funcs: List[Callable]):
    for func in process_funcs:
        func(schema)

    for key in schema.__fields_set__:
        if isinstance(schema.__getattribute__(key), CustomBaseModel):
            # If value is dict then iterate over all its values
            travel_schema(schema.__getattribute__(key), process_funcs)
        elif isinstance(schema.__getattribute__(key), List):
            # If value is not dict type then yield the value
            for item in schema.__getattribute__(key):
                travel_schema(item, process_funcs)


def handle_generate_uuid4(object_, erase_old_value: bool = False) -> None:
    if isinstance(object_, CustomBaseModel):
        for name, info in object_.__fields__.items():
            value = object_.__getattribute__(name)
            info: ModelField
            if info.field_info.extra.get("gen_uuid") and (erase_old_value or value is None) and info.type_ == UUID4:
                object_.__setattr__(name, uuid.uuid4())


def emp_str(v) -> str:
    return str(v) if v is not None else ""
