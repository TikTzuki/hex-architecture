from sqlalchemy import VARCHAR, Column, Float, Integer

from database.models.utils import BaseModel


class AssetOther(BaseModel):
    __tablename__ = 'los_asset_other'
    __table_args__ = {'comment': 'Tài sản khác'}

    id = Column('ID', Integer, primary_key=True)

    source_income_group_asset_id = Column('SOURCE_INCOME_GROUP_ASSET_ID', Integer)

    frequency_type = Column('FREQUENCY_TYPE', VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    owner_status = Column('OWNER_STATUS', VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    price = Column('PRICE', Float)

    income = Column('INCOME', Float)

    note = Column('NOTE', VARCHAR(600))

    display_order = Column("DISPLAY_ORDER", Integer)

    income_ratio = Column("INCOME_RATIO", Float)

    license = Column("LICENSE", VARCHAR(100), comment='Giấy chứng nhận, số giấy chứng nhận .....')
