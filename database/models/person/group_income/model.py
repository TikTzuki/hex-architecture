from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonGroupIncome(BaseModel):
    __tablename__ = 'los_person_group_income'
    __table_args__ = {'comment': 'Tổng thu nhập của từng nhóm'}

    id = Column(Integer, primary_key=True)
    los_profile_income_id = Column(ForeignKey('los_profile_income.id'), comment='Hồ sơ thu nhập của cá nhân')
    total_amount = Column(Integer, comment='Tổng thu nhập trong một nhóm của một người')
    frequency_type = Column(VARCHAR(75), comment='Tần suất thu nhập: \\n- Thường xuyên\\n- Không thường xuyên')
    ratio_income = Column(Float, comment='Tỷ lệ nguồn thu này trên tổng nguồn thu nhập chiếm %')
    source_income_type = Column(VARCHAR(75), comment='Nguồn thu nhập: Nguồn lương, cho thuê tài sản, kinh doanh .... (tham chiếu trong bảng udtm )')
    occasional_income_amount = Column(Float, comment='Tổng thu nhập không thường xuyên')
    permanent_income_amount = Column(Float, comment='Tổng thu nhập thường xuyên')

    los_profile_income = relationship('LosProfileIncome')


class PersonGroupIncomeDetail(BaseModel):
    __tablename__ = 'los_person_group_income_detail'
    __table_args__ = {'comment': 'Tổng hợp nguồn thu nhập theo từng nhóm'}

    id = Column(Integer, primary_key=True)
    group_income_type = Column(CHAR(5), comment='Loại hình thu nhập, nhóm')
    total_profit = Column(Float, comment='Tổng số tiền thu nhập')
    total_income = Column(Float, comment='Tổng số tiền thu thập thực tế được cộng trong từng nhóm')
    person_group_income_id = Column(Integer)
