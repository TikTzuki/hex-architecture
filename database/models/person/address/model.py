from sqlalchemy import (
    CHAR, VARCHAR, Column, DateTime, Float, ForeignKey, Integer
)
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonAddress(BaseModel):
    __tablename__ = 'los_person_address'
    __table_args__ = {'comment': 'Địa chỉ khách hàng, mỗi khách hàng hoặc cá nhân có thể có nhiêuf địa chỉ liên hệ.'}

    id = Column(Integer, primary_key=True)
    person_id = Column(ForeignKey('los_person.id'), comment='Mã khách hàng.')
    address_type = Column(VARCHAR(20), comment='Loại địa chỉ: Tạm trú, Thường Trú.')
    owner_status = Column(VARCHAR(20), comment='Tình trạng sở hữu khách hàng của địa chỉ này (tham chiếu trong bảng udtm )')
    address = Column(VARCHAR(100), comment='Địa chỉ thực tế')
    province_id = Column(VARCHAR(6), comment='Mã tỉnh/thành phố')
    district_id = Column(VARCHAR(6), comment='Mã Quận/Huyện')
    ward_id = Column(VARCHAR(6), comment='Mã Phường/Xã')
    latitude = Column(Float, comment='Vĩ độ')
    longitude = Column(Float, comment='Kinh độ')
    actived_flag = Column(CHAR(1), comment='Kích hoạt / Vô hiệu hóa')
    approval_date = Column(DateTime, comment='Ngày phê duyệt')
    created_at = Column(DateTime, comment='Ngày tạo record')
    created_by = Column(VARCHAR(20), comment='Người khởi tạo')
    modified_at = Column(DateTime, comment='Ngày chỉnh sửa cuối cùng')
    modified_by = Column(VARCHAR(20), comment='Người chỉnh sửa cuối cùng')
    uuid = Column(VARCHAR(50))
    primary_flag = Column(CHAR(1), comment='Địa chỉ  chính')
    name_working_unit = Column(VARCHAR(200), comment='Tên đơn vị làm việc')

    person = relationship('LosPerson')
