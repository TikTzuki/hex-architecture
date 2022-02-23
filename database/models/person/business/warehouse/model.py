from sqlalchemy import VARCHAR, Column, DateTime, Float, Integer

from database.base import BaseModel


class PersonBusinessWarehouse(BaseModel):
    __tablename__ = 'los_person_business_warehouse'
    __table_args__ = {
        'comment': 'Mỗi hộ kinh doanh của cá nhân có thể tạo nhiều cái kho hàng,\nLOS_PERSON_BUSINESS_ADDRESS'}

    id = Column("ID", Integer, primary_key=True)

    person_business_address_id = Column("PERSON_BUSINESS_ADDRESS_ID", Integer)

    province_id = Column("PROVINCE_ID", VARCHAR(6))

    district_id = Column("DISTRICT_ID", VARCHAR(6))

    ward_id = Column("WARD_ID", VARCHAR(6))

    address = Column("ADDRESS", VARCHAR(100))

    area = Column("AREA", Float, comment='Diện tích của căn nhà kho thuê')

    approval_date = Column("APPROVAL_DATE", DateTime, comment='Ngày phê duyệt')

    price = Column("PRICE", Float, comment='Giá tiền thuê nhà kho')

    latitude = Column("LATITUDE", Float, comment='Vĩ độ')

    longitude = Column("LONGITUDE", Float, comment='Kinh độ')

    is_default = Column("IS_DEFAULT", VARCHAR(1), default='N')
