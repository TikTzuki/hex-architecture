from sqlalchemy import CHAR, VARCHAR, Column, DateTime, Integer

from database.base import BaseModel


class Policy(BaseModel):
    __tablename__ = 'los_policy'

    id = Column(Integer, primary_key=True)
    customer_type = Column(VARCHAR(20), comment='Áp dụng cho loại khách hàng nào')
    version = Column(VARCHAR(50))
    approval_date = Column(DateTime, comment='Ngày áp dụng')
    number_no = Column(CHAR(15), comment='Số hiệu văn bản áp dụng.')
    actived_flag = Column(CHAR(1))
