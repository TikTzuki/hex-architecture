import json
from typing import Dict, List, Union

from sqlalchemy import VARCHAR, TypeDecorator


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
