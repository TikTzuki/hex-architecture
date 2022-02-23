from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class ProfileCreditCardDelivery(BaseModel):
    __tablename__ = 'los_profile_credit_card_delivery'
    __table_args__ = {'comment': 'Bảng ghi nhận thông tin hình thức giao thẻ'}

    id = Column("ID", Integer, primary_key=True)

    credit_published_id = Column('CREDIT_PUBLISHED_ID', Integer, comment='Tham chiếu tới bảng thẻ chính')

    card_delivery_method = Column('CARD_DELIVERY_METHOD', VARCHAR(20), comment='Phương thức giao thẻ')

    branch_id = Column('BRANCH_ID', VARCHAR(100), comment='Tham chiếu vào bảng SCB để biết branch nào')

    address = Column('ADDRESS', VARCHAR(100))

    province_id = Column('PROVINCE_ID', VARCHAR(6))

    district_id = Column('DISTRICT_ID', VARCHAR(6))

    ward_id = Column('WARD_ID', VARCHAR(6))
