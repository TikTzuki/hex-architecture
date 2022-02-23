from sqlalchemy import VARCHAR, Column, Float, Integer

from database.base import BaseModel


class SourceIncomeGroupAsset(BaseModel):
    __tablename__ = 'los_source_income_group_asset'
    __table_args__ = {'comment': 'Nhóm thu nhập từ tài sản cho thuê'}

    id = Column("ID", Integer, primary_key=True)

    person_group_income_id = Column('PERSON_GROUP_INCOME_ID', Integer)

    total_amount = Column("TOTAL_AMOUNT", Float)

    frequency_type = Column("FREQUENCY_TYPE", VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    ratio_income = Column("RATIO_INCOME", Float)

    asset_type = Column("ASSET_TYPE", VARCHAR(75), comment='Nhóm loại tài sản: bất động sản, phương tiện, máy móc')

    income_amount = Column("INCOME_AMOUNT", Float)

    display_order = Column("DISPLAY_ORDER", Integer)
