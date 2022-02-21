from sqlalchemy import VARCHAR, Column, Float, Integer

from database.models.utils import BaseModel


class AssetTransportation(BaseModel):
    __tablename__ = 'los_asset_transportation'
    __table_args__ = {'comment': 'Tài sản cho thuê từ phương tiện vận tải.'}

    id = Column("ID", Integer, primary_key=True)

    source_income_group_asset_id = Column('SOURCE_INCOME_GROUP_ASSET_ID', Integer)

    transportation_type = Column('TRANSPORTATION_TYPE', VARCHAR(75), comment='Loại phương tiện')

    frequency_type = Column('FREQUENCY_TYPE', VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    model = Column('MODEL', VARCHAR(50))

    license_number = Column('LICENSE_NUMBER', VARCHAR(50))

    owner_status = Column('OWNER_STATUS', VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    note = Column("NOTE", VARCHAR(600))

    price = Column('PRICE', Float)

    income = Column('INCOME', Float)

    display_order = Column("DISPLAY_ORDER", Integer)

    ratio_income = Column("RATIO_INCOME", Float)
