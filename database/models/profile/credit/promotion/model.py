from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class ProfileCreditPromotion(BaseModel):
    __tablename__ = 'los_profile_credit_promotion'
    __table_args__ = {'comment': 'Danh sách câu trả lời cho hồ sơ vay vốn của khách hàng'}

    id = Column("ID", Integer, primary_key=True)

    credit_published_id = Column('CREDIT_PUBLISHED_ID', VARCHAR(20))

    profile_credit_promotion_id = Column('PROFILE_CREDIT_PROMOTION_ID', Integer)
