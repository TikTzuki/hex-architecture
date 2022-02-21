from sqlalchemy import Column, Integer

from database.models.utils import BaseModel


class PolicyRule(BaseModel):
    __tablename__ = 'los_policy_rule'

    id = Column("ID", Integer, primary_key=True)

    policy_id = Column('POLICY_ID', Integer)

    policy_group_id = Column('POLICY_GROUP_ID', Integer)

    display_order = Column("DISPLAY_ORDER", Integer)
