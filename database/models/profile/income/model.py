from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.oracle import VARCHAR2

from database.base import BaseModel


class ProfileIncome(BaseModel):
    __tablename__ = 'los_profile_income'
    __table_args__ = {'comment': 'Ghi nhận các đợt khai báo nguồn thu nhập của từng đối tượng'}

    id = Column(Integer, primary_key=True)
    los_income_sequence_id = Column(Integer, comment='Liên kết với tờ khai báo thu nhập tổng')
    person_id = Column(Integer, comment='Mã cá nhân ghi nhận thu nhập')
    total_income = Column(Float, comment='Tổng thu nhập của người đang xét')
    relationship_type = Column(VARCHAR(75), comment='Người đồng vay, người hôn phối.... Dùng để truy xuất nhanh cho các báo cáo')
