from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class BusinessFinanceCashflowValue(BaseModel):
    __tablename__ = 'los_business_finance_cashflow_value'
    __table_args__ = {'comment': 'Doanh thu bình quân phải thu theo thời gian'}

    id = Column(Integer, primary_key=True)
    business_finance_cashflow_id = Column(ForeignKey('los_business_finance_cashflow.id'))
    finance_timeline_assign_id = Column(Integer, comment='Tham chiếu qua bảng TIMELINE_ASSIGN để biết được cụ thể là thời gian và người  tạo.')
    value = Column(Float)

    business_finance_cashflow = relationship('LosBusinessFinanceCashflow')
