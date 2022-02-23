from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class IncomeSequence(BaseModel):
    __tablename__ = 'los_income_sequence'
    __table_args__ = {'comment': 'Ghi lại các lần khai báo thông tin thu nhập của hồ sơ LOS'}

    id = Column(Integer, primary_key=True)
    los_sequence_id = Column(ForeignKey('los_profile_sequence_item.id'), comment='Link tới table LOS_PROFILE_SEQUENCE_ITEM')
    total_income = Column(Float, comment='Tổng thu nhập của các nhóm')
    total_cost = Column(Float, comment='Tổng chi phí')
    net_profit = Column(Float, comment='Thu nhập ròng')

    los_credit_sequence_id = Column(NUMBER(asdecimal=False), comment='Link tới table LOS_PROFILE_CREDIT_SEQUENCE_ITEM')

    los_sequence = relationship('LosProfileSequenceItem')
