from sqlalchemy import CHAR, VARCHAR, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PolicyDetail(BaseModel):
    __tablename__ = 'los_policy_detail'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100))
    description = Column(VARCHAR(300))
    code = Column(VARCHAR(5), comment='Mã ngoại lệ')
    policy_group_id = Column(ForeignKey('los_policy_group.id'), comment='Nhóm mã ngoại lệ')
    actived_flag = Column(CHAR(1))

    policy_group = relationship('PolicyGroup')
