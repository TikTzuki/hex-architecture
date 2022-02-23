from sqlalchemy import VARCHAR, Column, Float, Integer

from database.base import BaseModel


class AssetRealEstate(BaseModel):
    __tablename__ = 'los_asset_real_estate'
    __table_args__ = {'comment': 'Nguồn từ bất động sản'}

    id = Column("ID", Integer, primary_key=True)

    source_income_group_asset_id = Column('SOURCE_INCOME_GROUP_ASSET_ID', Integer)

    frequency_type = Column('FREQUENCY_TYPE', VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    address = Column('ADDRESS', VARCHAR(100))

    province_id = Column("PROVINCE_ID", VARCHAR(6))

    district_id = Column("DISTRICT_ID", VARCHAR(6))

    ward_id = Column("WARD_ID", VARCHAR(6))

    latitude = Column('LATITUDE', Float)

    longitude = Column('LONGITUDE', Float)

    owner_status = Column('OWNER_STATUS', VARCHAR(75), comment='Tình trạng sở hữu (tham chiếu trong bảng udtm )')

    note = Column('NOTE', VARCHAR(600))

    price = Column('PRICE', Float, comment='Tổng giá cho thuê')

    income = Column('INCOME', Float, comment='Tổng thu nhập')

    display_order = Column("DISPLAY_ORDER", Integer)

    ratio_income = Column("RATIO_INCOME", Float)
