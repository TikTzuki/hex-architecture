from sqlalchemy import VARCHAR, Column, Float, Integer

from database.models.utils import BaseModel


class SourceIncomeStock(BaseModel):
    __tablename__ = 'los_source_income_stock'
    __table_args__ = {'comment': 'Nguồn thu từ chứng khoán, cổ phiếu'}

    id = Column("ID", Integer, primary_key=True)

    person_group_income_id = Column('PERSON_GROUP_INCOME_ID', Integer)

    name = Column("NAME", VARCHAR(100), comment='Tên cổ phiếu, cổ phần')

    stock_category = Column("STOCK_CATEGORY", VARCHAR(75), comment='Loại hình:\\n- Cổ tức\\n- Cổ phiếu')

    frequency_type = Column("FREQUENCY_TYPE", VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    year_payment = Column("YEAR_PAYMENT", Float, comment='Số năm nhận')

    total_payment = Column("TOTAL_PAYMENT", Float, comment='Số lần nhận trong năm')

    profit = Column("PROFIT", Float)

    income = Column("INCOME", Float)

    display_order = Column("DISPLAY_ORDER", Integer)

    income_ratio = Column("INCOME_RATIO", Float)
