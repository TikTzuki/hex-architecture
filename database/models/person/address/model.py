from sqlalchemy import CHAR, VARCHAR, Column, DateTime, Float, Integer

from database.models.utils import BaseModel


class PersonAddress(BaseModel):
    __tablename__ = 'los_person_address'
    __table_args__ = {'comment': 'Địa chỉ khách hàng, mỗi khách hàng hoặc cá nhân có thể có nhiêuf địa chỉ liên hệ.'}

    id = Column("ID", Integer, primary_key=True)

    person_id = Column('PERSON_ID', Integer)

    address_type = Column("ADDRESS_TYPE", VARCHAR(20), comment='Loại địa chỉ: Tạm trú, Thường Trú.')

    owner_status = Column('OWNER_STATUS', VARCHAR(20),
                          comment='Tình trạng sở hữu khách hàng của địa chỉ này (tham chiếu trong bảng udtm )')

    address = Column("ADDRESS", VARCHAR(100), comment='Địa chỉ thực tế')

    province_id = Column("PROVINCE_ID", VARCHAR(6), comment='Mã tỉnh/thành phố')

    district_id = Column("DISTRICT_ID", VARCHAR(6), comment='Mã Quận/Huyện')

    ward_id = Column("WARD_ID", VARCHAR(6), comment='Mã Phường/Xã')

    latitude = Column("LATITUDE", Float, comment='Vĩ độ')

    longitude = Column("LONGITUDE", Float, comment='Kinh độ')

    actived_flag = Column("ACTIVED_FLAG", CHAR(1), comment='Kích hoạt / Vô hiệu hóa')

    approval_date = Column("APPROVAL_DATE", DateTime, comment='Ngày phê duyệt')

    primary_flag = Column("PRIMARY_FLAG", CHAR(1), comment='Địa chỉ chính')

    name_working_unit = Column("NAME_WORKING_UNIT", VARCHAR(200), comment='Tên đơn vị làm việc')
