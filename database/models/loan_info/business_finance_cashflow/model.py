from sqlalchemy import VARCHAR, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class BusinessFinanceCashflow(BaseModel):
    __tablename__ = 'los_business_finance_cashflow'
    __table_args__ = {'comment': 'Thông tin đầu ra đầu vào'}

    id = Column(Integer, primary_key=True)
    business_finance_report_id = Column(ForeignKey('los_person_business_finance_report.id'))
    cashflow_type = Column(VARCHAR(20), comment='Loại đầu vào đầu ra (tham chiếu trong bảng udtm )')

    business_finance_report = relationship('LosPersonBusinessFinanceReport')
