from sqlalchemy import VARCHAR, Column, DateTime, Float, Integer

from database.base import BaseModel


class SourceIncomeCompany(BaseModel):
    __tablename__ = 'los_source_income_company'
    __table_args__ = {'comment': 'Thu nhập từ công ty, doanh nghiệp khách hàng làm chủ'}

    id = Column("ID", Integer, primary_key=True)

    person_group_income_id = Column('PERSON_GROUP_INCOME_ID', Integer)

    business_type = Column("BUSINESS_TYPE", VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    business_name = Column("BUSINESS_NAME", VARCHAR(100))

    tax = Column("TAX", VARCHAR(20))

    phone = Column("PHONE", VARCHAR(20))

    license_date = Column("LICENSE_DATE", DateTime, comment='Ngày cấp giấy phép')

    profit = Column("PROFIT", Float, comment='Lợi nhuận bình quân được nhận/chia')

    income = Column("INCOME", Float)

    frequency_type = Column("FREQUENCY_TYPE", VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    display_order = Column("DISPLAY_ORDER", Integer)

    income_ratio = Column("INCOME_RATIO", Float)
