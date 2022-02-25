from sqlalchemy import Column, Integer

from database.base import BaseModel


class PolicyRule(BaseModel):
    __tablename__ = 'los_policy_rule'

    id = Column(Integer, primary_key=True)
    policy_id = Column(Integer)
    policy_group_id = Column(Integer)
    display_order = Column(Integer)
