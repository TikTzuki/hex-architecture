from sqlalchemy import Column, Float, Integer

from database.base import BaseModel


class MaFrequence(BaseModel):
    __tablename__ = 'los_ma_frequence'
    __table_args__ = {'comment': 'Ghi lại nhóm thu nhập nào và tần suất thu nhập để tính ra giá trị phần trăm thu nhập'}

    id = Column("ID", Integer, primary_key=True)

    frequence_type = Column("FREQUENCE_TYPE", Integer)

    income_group_type = Column("INCOME_GROUP_TYPE", Integer)

    income_ratio = Column("INCOME_RATIO", Float)
