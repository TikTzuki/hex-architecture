from sqlalchemy import VARCHAR, Column, DateTime, Float, Integer

from database.models.utils import BaseModel


class SourceIncomePension(BaseModel):
    __tablename__ = 'los_source_income_pension'
    __table_args__ = {'comment': 'Nguồn thu nhập từ lương hưu'}

    id = Column("ID", Integer, primary_key=True)

    person_group_income_id = Column('PERSON_GROUP_INCOME_ID', Integer)

    license_number = Column("LICENSE_NUMBER", VARCHAR(20), comment='Số sổ, số giấy phép.....')

    start_date = Column("START_DATE", DateTime, comment='Ngày bắt đầu')

    insurance_number = Column("INSURANCE_NUMBER", VARCHAR(20), comment='Số sổ bảo hiểm....')

    salary = Column("SALARY", Float)

    income = Column("INCOME", Float, comment='Nguồn thu nhập')

    frequency_type = Column("FREQUENCY_TYPE", VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    display_order = Column("DISPLAY_ORDER", Integer)

    income_ratio = Column("INCOME_RATIO", Float)
