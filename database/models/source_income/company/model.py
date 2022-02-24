from sqlalchemy import VARCHAR, Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class SourceIncomeCompany(BaseModel):
    __tablename__ = 'los_source_income_company'
    __table_args__ = {'comment': 'Thu nhập từ công ty, doanh nghiệp khách hàng làm chủ'}

    id = Column(Integer, primary_key=True)
    person_group_income_id = Column(ForeignKey('los_person_group_income.id'))
    business_type = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    business_name = Column(VARCHAR(100))
    tax = Column(VARCHAR(20))
    phone = Column(VARCHAR(20))
    license_date = Column(DateTime, comment='Ngày cấp giấy phép')
    profit = Column(Float, comment='Lợi nhuận bình quân được nhận/chia')
    income = Column(Float)
    created_at = Column(DateTime)
    created_by = Column(VARCHAR(20))
    modified_at = Column(DateTime)
    modified_by = Column(VARCHAR(20))
    frequency_type = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    display_order = Column(Integer)
    income_ratio = Column(Float)
    uuid = Column(VARCHAR(50))

    person_group_income = relationship('LosPersonGroupIncome')
