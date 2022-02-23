from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class SourceIncomeOther(BaseModel):
    __tablename__ = 'los_source_income_other'
    __table_args__ = {'comment': 'Nguồn thu nhập khác'}

    id = Column(Integer, primary_key=True)
    person_group_income_id = Column(ForeignKey('los_person_group_income.id'))
    frequency_type = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    frequence_year = Column(Integer)
    note = Column(VARCHAR(600))
    payment_method = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    profit = Column(Float)
    income = Column(Float)
    income_ratio = Column(Float)

    person_group_income = relationship('LosPersonGroupIncome')
