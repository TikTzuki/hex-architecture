from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PolicyGroup(BaseModel):
    __tablename__ = 'los_policy_group'
    __table_args__ = {'comment': 'Nhóm sản phẩm vay,'}


    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100))
    customer_type = Column(VARCHAR(20))
    description = Column(VARCHAR(300))
