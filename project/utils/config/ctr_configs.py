import json
from typing import Callable

from app.api.v2.metadata.common.repository import repo_get_udtm_by_fields_name
from app.third_party.core import error_code
from app.third_party.core.exception import LOSException
from app.third_party.redis.redis import (
    get_data_from_redis, insert_data_to_redis
)
from app.utils.configs.switcher_configs import (
    func_config_switcher, func_response_switcher
)
from app.utils.constant.configs import FIELD_UDTM_LOV, FUNC_RESPONSE


async def check_keys(keys: list, **kwargs):
    for key in kwargs:
        if key in keys:
            continue
        else:
            raise LOSException.with_error(
                code=error_code.UNHANDLE_EXCEPTION,
            )


async def get_configs(keys: list, *args, **kwargs):
    """
    Hàm lấy danh sách configs:
    Keys: List danh sách configs thường là constant, ví dụ: [CONST_COUNTRIES, CONST_PROVINCES, CONST_DISTRICTS]
    kwargs: Dictionary lưu id cần filter, ví dụ: PROVINCES=83, DISTRICT=[79, 20]
    Return:  Trả về một dictionary configs, ví dụ: {"COUNTRIES": [...], "PROVINCES": [...], "DISTRICTS": {"79": [...], "20": [...]} }
    """
    if kwargs:
        await check_keys(keys, **kwargs)

    response = dict()
    is_success, response, keys_not_data = await get_data_from_redis(keys)

    set_redis = dict()
    for key in keys_not_data:
        if key in FIELD_UDTM_LOV.keys():
            data = await repo_get_udtm_by_fields_name(FIELD_UDTM_LOV.get(key))
        else:
            func_configs: Callable = func_config_switcher.get(key)
            data = await func_configs()
        response[key] = data
        set_redis[key] = json.dumps(data)

    if keys_not_data and is_success:
        await insert_data_to_redis(set_redis)
    for key in response:
        if key in FUNC_RESPONSE and response[key]:
            func_structure: Callable = func_response_switcher.get(key)
            response[key] = await func_structure(response[key], **kwargs)
    return response
