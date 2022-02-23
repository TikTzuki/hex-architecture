from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class SourceIncomePension(BaseModel):
    __tablename__ = 'los_source_income_pension'
    __table_args__ = {'comment': 'Nguồn thu nhập từ lương hưu'}

    id = Column(Integer, primary_key=True)
    person_group_income_id = Column(ForeignKey('los_person_group_income.id'))
    license_number = Column(VARCHAR(20), comment='Số sổ, số giấy phép.....')
    start_date = Column(DateTime, comment='Ngày bắt đầu')
    insurance_number = Column(VARCHAR(20), comment='Số sổ bảo hiểm....')
    salary = Column(Float)
    income = Column(Float, comment='Nguồn thu nhập')
    frequency_type = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    display_order = Column(Integer)
    income_ratio = Column(Float)

    person_group_income = relationship('LosPersonGroupIncome')
