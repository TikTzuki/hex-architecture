from sqlalchemy import (
    CHAR, VARCHAR, Column, DateTime, Float, ForeignKey, Integer
)
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonBusinessAddress(BaseModel):
    __tablename__ = 'los_person_business_address'
    __table_args__ = {'comment': 'Địa chỉ hoạt động của doanh nghiệp, hộ kinh doanh,'}

    id = Column(Integer, primary_key=True)
    person_business_id = Column(ForeignKey('los_person_business.id'))
    owner_status = Column(VARCHAR(20), comment='Tình trạng sở hữu địa chỉ này của hộ kinh doanh, (tham chiếu trong bảng udtm )')
    area = Column(Float, comment='Diện tích')
    ending_lease = Column(Float, comment='Thời hạn thuê còn lại')
    price_lease = Column(Float, comment='Giá thuê (nếu tình trạng là thuê)')
    address = Column(VARCHAR(100), comment='Địa chỉ')
    province_id = Column(VARCHAR(6))
    district_id = Column(VARCHAR(6))
    ward_id = Column(VARCHAR(6))
    actived_flag = Column(CHAR(1))
    created_at = Column(DateTime)
    created_by = Column(VARCHAR(20))
    modified_at = Column(DateTime)
    modified_by = Column(VARCHAR(20))
    business_address_type = Column(VARCHAR(20), comment='Loại địa chỉ: Địa chỉ kinh doanh, kho hàng.....')
    uuid = Column(VARCHAR(50))

    person_business = relationship('LosPersonBusines')
