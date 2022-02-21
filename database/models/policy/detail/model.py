from sqlalchemy import CHAR, VARCHAR, Column, Integer

from database.models.utils import BaseModel


class PolicyDetail(BaseModel):
    __tablename__ = 'los_policy_detail'

    id = Column("ID", Integer, primary_key=True)

    name = Column('NAME', VARCHAR(100))

    description = Column("DESCRIPTION", VARCHAR(300))

    code = Column('CODE', CHAR(5), comment='Mã ngoại lệ')

    policy_group_id = Column('POLICY_GROUP_ID', Integer)

    actived_flag = Column('ACTIVED_FLAG', CHAR(1))
