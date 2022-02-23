from typing import Dict

from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv
from sqlacodegen.codegen import CodeGenerator
from sqlalchemy import MetaData
from sqlalchemy.orm import Session

from database.base import get_session, engine


class TestService:
    def get_name(self) -> str:
        return "name"


router = APIRouter()


@cbv(router)
class APIVersion1:
    session: Session = Depends(get_session)
    service: TestService = Depends(TestService)

    @router.post("/test/")
    async def get_st(self) -> Dict:
        # print(self.session.execute("SELECT name FROM sqlite_schema").all())
        # print(self.session.execute("SELECT table_name FROM user_tables").all())
        name = self.service.get_name()
        return {"name": name}

    @router.post("/generate")
    def generate_model(self, file):
        metadata = MetaData(bind=engine)
        metadata.reflect()
        outfile = open(file, "w", encoding="utf-8")
        generator = CodeGenerator(metadata)
        generator.render(outfile)
