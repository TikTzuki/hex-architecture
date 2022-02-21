from sqlalchemy import VARCHAR, Column, Integer

from database.models.utils import BaseModel


class ProfileCreditPromotion(BaseModel):
    __tablename__ = 'los_profile_credit_promotion'
    __table_args__ = {'comment': 'Danh sách câu trả lời cho hồ sơ vay vốn của khách hàng'}

    id = Column("ID", Integer, primary_key=True)

    credit_published_id = Column('CREDIT_PUBLISHED_ID', VARCHAR(20))

    profile_credit_promotion_id = Column('PROFILE_CREDIT_PROMOTION_ID', Integer)
