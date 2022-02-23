from sqlalchemy import VARCHAR, Column, Float, Integer

from database.base import BaseModel


class SourceIncomeOther(BaseModel):
    __tablename__ = 'los_source_income_other'
    __table_args__ = {'comment': 'Nguồn thu nhập khác'}

    id = Column("ID", Integer, primary_key=True)

    person_group_income_id = Column('PERSON_GROUP_INCOME_ID', Integer)

    frequency_type = Column("FREQUENCY_TYPE", VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    frequence_year = Column("FREQUENCE_YEAR", Integer)

    note = Column("NOTE", VARCHAR(600))

    payment_method = Column("PAYMENT_METHOD", VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    profit = Column("PROFIT", Float)

    income = Column("INCOME", Float)

    income_ratio = Column("INCOME_RATIO", Float)
