from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship

from database.base import BaseModel


class AssetTransportation(BaseModel):
    __tablename__ = 'los_asset_transportation'
    __table_args__ = {'comment': 'Tài sản cho thuê từ phương tiện vận tải.'}

    id = Column(Integer, primary_key=True)
    source_income_group_asset_id = Column(ForeignKey('los_source_income_group_asset.id'))
    transportation_type = Column(VARCHAR(75), comment='Loại phương tiện')
    frequency_type = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    model = Column(VARCHAR(50))
    license_number = Column(VARCHAR(50))
    owner_status = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    note = Column(VARCHAR(600))
    price = Column(Float)
    income = Column(Float)
    display_order = Column(Integer)
    ratio_income = Column(Float)

    source_income_group_asset = relationship('LosSourceIncomeGroupAsset')
