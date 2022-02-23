from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class SourceIncomeGroupAsset(BaseModel):
    __tablename__ = 'los_source_income_group_asset'
    __table_args__ = {'comment': 'Nhóm thu nhập từ tài sản cho thuê'}

    id = Column(Integer, primary_key=True)
    person_group_income_id = Column(ForeignKey('los_person_group_income.id'))
    total_amount = Column(Float)
    frequency_type = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    ratio_income = Column(Float)
    asset_type = Column(VARCHAR(75), comment='Nhóm loại tài sản: bất động sản, phương tiện, máy móc')
    income_amount = Column(Float)
    display_order = Column(Integer)

    person_group_income = relationship('LosPersonGroupIncome')
