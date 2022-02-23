from sqlalchemy import VARCHAR, Column, Integer

from database.base import BaseModel


class BusinessFinanceCashFlow(BaseModel):
    __tablename__ = 'los_business_finance_cashflow'
    __table_args__ = {'comment': 'Thông tin đầu ra đầu vào'}

    id = Column("ID", Integer, primary_key=True)

    business_finance_report_id = Column('BUSINESS_FINANCE_REPORT_ID', Integer)

    cashflow_type = Column("CASHFLOW_TYPE", VARCHAR(20), comment='Loại đầu vào đầu ra (tham chiếu trong bảng udtm )')
