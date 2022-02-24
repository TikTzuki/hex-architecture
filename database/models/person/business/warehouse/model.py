from sqlalchemy import (
    VARCHAR, Column, DateTime, Float, ForeignKey, Integer, text
)
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonBusinessWarehouse(BaseModel):
    __tablename__ = 'los_person_business_warehouse'
    __table_args__ = {'comment': 'Mỗi hộ kinh doanh của cá nhân có thể tạo nhiều cái kho hàng,\r\nLOS_PERSON_BUSINESS_ADDRESS'}

    id = Column(Integer, primary_key=True)
    person_business_address_id = Column(ForeignKey('los_person_business_address.id'))
    province_id = Column(VARCHAR(6))
    district_id = Column(VARCHAR(6))
    ward_id = Column(VARCHAR(6))
    address = Column(VARCHAR(100))
    area = Column(Float, comment='Diện tích của căn nhà kho thuê')
    approval_date = Column(DateTime, comment='Ngày phê duyệt')
    price = Column(Float, comment='Giá tiền thuê nhà kho')
    latitude = Column(Float, comment='Vĩ độ')
    longitude = Column(Float, comment='Kinh độ')

    is_default = Column(VARCHAR(1), server_default=text("'N'"))

    person_business_address = relationship('PersonBusinessAddress')
