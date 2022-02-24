from loguru import logger
from sqlalchemy.orm import Session

from database.models import __all__


async def test_model(oracle_session: Session):
    models = __all__
    for model in models:
        try:
            oracle_session.query(model).fist()
        except Exception as ex:
            logger.error(model)
            logger.warning(ex)
