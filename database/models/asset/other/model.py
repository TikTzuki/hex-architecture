from sqlalchemy import VARCHAR, Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class AssetOther(BaseModel):
    __tablename__ = 'los_asset_other'
    __table_args__ = {'comment': 'Tài sản khác'}

    id = Column(Integer, primary_key=True)
    source_income_group_asset_id = Column(ForeignKey('los_source_income_group_asset.id'))
    frequency_type = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    owner_status = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    price = Column(Float)
    income = Column(Float)
    note = Column(VARCHAR(600))
    display_order = Column(Integer)
    income_ratio = Column(Float)
    license = Column(VARCHAR(100), comment='Giấy chứng nhận, số giấy chứng nhận .....')

    source_income_group_asset = relationship('SourceIncomeGroupAsset')
