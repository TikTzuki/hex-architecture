from sqlalchemy import VARCHAR, Column, Float, Integer

from database.models.utils import BaseModel


class SourceIncomeBusinessHousehold(BaseModel):
    __tablename__ = 'los_source_income_business_household'
    __table_args__ = {'comment': 'Nguồn thu nhập từ hộ kinh doanh'}

    id = Column("ID", Integer, primary_key=True)

    person_group_income_id = Column('PERSON_GROUP_INCOME_ID', Integer)

    business_housing_type = Column("BUSINESS_HOUSING_TYPE", VARCHAR(75),
                                   comment='Người đại diện hộ kinh doanh:\\n- Chính KH\\n- Người hôn phối')

    frequency_type = Column("FREQUENCY_TYPE", VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    business_name = Column("BUSINESS_NAME", VARCHAR(100))

    business_working_time = Column("BUSINESS_WORKING_TIME", Integer)

    gross_revenue = Column("GROSS_REVENUE", Float, comment='Doanh thu bình quân tháng')

    cost = Column("COST", Float, comment='Chi phí hàng thàng bình quân')

    profit = Column("PROFIT", Float, comment='Lợi nhuạn bình quân (tháng)')

    income = Column("INCOME", Float, comment='Lợi nhuận')

    display_order = Column("DISPLAY_ORDER", Integer)

    income_ratio = Column("INCOME_RATIO", Float)
