from sqlalchemy import CHAR, VARCHAR, Column, DateTime, Integer

from database.base import BaseModel


class Policy(BaseModel):
    __tablename__ = 'los_policy'

    id = Column("ID", Integer, primary_key=True)

    customer_type = Column("CUSTOMER_TYPE", VARCHAR(20), comment='Áp dụng cho loại khách hàng nào')

    version = Column("VERSION", VARCHAR(50))

    approval_date = Column("APPROVAL_DATE", DateTime, comment='Ngày áp dụng')

    number_no = Column("NUMBER_NO", CHAR(15), comment='Số hiệu văn bản áp dụng.')

    actived_flag = Column("ACTIVED_FLAG", CHAR(1))
