from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class SourceIncomeStock(BaseModel):
    __tablename__ = 'los_source_income_stock'
    __table_args__ = {'comment': 'Nguồn thu từ chứng khoán, cổ phiếu'}

    id = Column(Integer, primary_key=True)
    person_group_income_id = Column(ForeignKey('los_person_group_income.id'))
    name = Column(VARCHAR(100), comment='Tên cổ phiếu, cổ phần')
    stock_category = Column(VARCHAR(75), comment='Loại hình:\\n- Cổ tức\\n- Cổ phiếu')
    frequency_type = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    year_payment = Column(Float, comment='Số năm nhận')
    total_payment = Column(Float, comment='Số lần nhận trong năm')
    profit = Column(Float)
    income = Column(Float)
    display_order = Column(Integer)
    income_ratio = Column(Float)

    person_group_income = relationship('LosPersonGroupIncome')
