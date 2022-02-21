from sqlalchemy import Column, Float, Integer

from database.models.utils import BaseModel


class BusinessFinanceCashFlowValue(BaseModel):
    __tablename__ = 'los_business_finance_cashflow_value'
    __table_args__ = {'comment': 'Doanh thu bình quân phải thu theo thời gian'}

    id = Column("ID", Integer, primary_key=True)

    business_finance_cashflow_id = Column('BUSINESS_FINANCE_CASHFLOW_ID', Integer)

    finance_timeline_assign_id = Column("FINANCE_TIMELINE_ASSIGN_ID", Integer,
                                        comment='Tham chiếu qua bảng TIMELINE_ASSIGN để biết được cụ thể là thời gian và người  tạo.')

    value = Column("VALUE", Float)
