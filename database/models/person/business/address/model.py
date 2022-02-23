from sqlalchemy import CHAR, VARCHAR, Column, Float, Integer

from database.base import BaseModel


class PersonBusinessAddress(BaseModel):
    __tablename__ = 'los_person_business_address'
    __table_args__ = {'comment': 'Địa chỉ hoạt động của doanh nghiệp, hộ kinh doanh,'}

    id = Column("ID", Integer, primary_key=True)

    person_business_id = Column('PERSON_BUSINESS_ID', Integer)

    owner_status = Column("OWNER_STATUS", VARCHAR(20),
                          comment='Tình trạng sở hữu địa chỉ này của hộ kinh doanh, (tham chiếu trong bảng udtm )')

    area = Column("AREA", Float, comment='Diện tích')

    ending_lease = Column("ENDING_LEASE", Float, comment='Thời hạn thuê còn lại')

    price_lease = Column("PRICE_LEASE", Float, comment='Giá thuê (nếu tình trạng là thuê)')

    address = Column("ADDRESS", VARCHAR(100), comment='Địa chỉ')

    province_id = Column("PROVINCE_ID", VARCHAR(6))

    district_id = Column("DISTRICT_ID", VARCHAR(6))

    ward_id = Column("WARD_ID", VARCHAR(6))

    actived_flag = Column("ACTIVED_FLAG", CHAR(1))

    business_address_type = Column("BUSINESS_ADDRESS_TYPE", VARCHAR(20),
                                   comment='Loại địa chỉ: Địa chỉ kinh doanh, kho hàng.....')
