from sqlalchemy import VARCHAR, Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class SourceIncomeBusinessHousehold(BaseModel):
    __tablename__ = 'los_source_income_business_household'
    __table_args__ = {'comment': 'Nguồn thu nhập từ hộ kinh doanh'}

    id = Column(Integer, primary_key=True)
    person_group_income_id = Column(ForeignKey('los_person_group_income.id'))
    business_housing_type = Column(VARCHAR(75), comment='Người đại diện hộ kinh doanh:\\n- Chính KH\\n- Người hôn phối')
    frequency_type = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    business_name = Column(VARCHAR(100))
    business_working_time = Column(Integer)
    gross_revenue = Column(Float, comment='Doanh thu bình quân tháng')
    cost = Column(Float, comment='Chi phí hàng thàng bình quân')
    profit = Column(Float, comment='Lợi nhuạn bình quân (tháng)')
    income = Column(Float, comment='Lợi nhuận')
    display_order = Column(Integer, comment='Thứ tự sắp xêp ')
    income_ratio = Column(Float)

    person_group_income = relationship('LosPersonGroupIncome')
