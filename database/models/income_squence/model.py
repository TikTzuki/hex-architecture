from sqlalchemy import Column, Float, Integer

from database.base import BaseModel


class IncomeSequence(BaseModel):
    __tablename__ = 'los_income_sequence'

    __table_args__ = {'comment': 'Ghi lại các lần khai báo thông tin thu nhập của hồ sơ LOS'}

    id = Column("ID", Integer, primary_key=True)

    sequence_id = Column("LOS_SEQUENCE_ID", Integer, comment='Link tới table LOS_PROFILE_SEQUENCE_ITEM')

    total_income = Column("TOTAL_INCOME", Float, comment='Tổng thu nhập')

    total_cost = Column("TOTAL_COST", Float, comment='Tổng chi phí')

    net_profit = Column("NET_PROFIT", Float, comment='Thu nhập ròng')

    credit_sequence_id = Column("LOS_CREDIT_SEQUENCE_ID", Integer,
                                comment='Link tới table LOS_PROFILE_CREDIT_SEQUENCE_ITEM')
