from sqlalchemy import VARCHAR, Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class AssetRealEstate(BaseModel):
    __tablename__ = 'los_asset_real_estate'
    __table_args__ = {'comment': 'Nguồn từ bất động sản'}

    id = Column(Integer, primary_key=True)
    source_income_group_asset_id = Column(ForeignKey('los_source_income_group_asset.id'))
    frequency_type = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    address = Column(VARCHAR(100))
    province_id = Column(VARCHAR(6))
    district_id = Column(VARCHAR(6))
    ward_id = Column(VARCHAR(6))
    latitude = Column(Float)
    longitude = Column(Float)
    owner_status = Column(VARCHAR(75), comment='Tình trạng sở hữu (tham chiếu trong bảng udtm )')
    note = Column(VARCHAR(600))
    price = Column(Float, comment='Tổng giá cho thuê')
    income = Column(Float, comment='Tổng thu nhập')
    display_order = Column(Integer)
    ratio_income = Column(Float)

    source_income_group_asset = relationship('SourceIncomeGroupAsset')
