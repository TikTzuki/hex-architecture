from sqlalchemy import CHAR, VARCHAR, Column, Float, Integer

from database.models.utils import BaseModel


class PersonGroupIncome(BaseModel):
    __tablename__ = 'los_person_group_income'
    __table_args__ = {'comment': 'Tổng thu nhập của từng nhóm'}

    id = Column("ID", Integer, primary_key=True)

    profile_income_id = Column('LOS_PROFILE_INCOME_ID', Integer)

    total_amount = Column("TOTAL_AMOUNT", Integer, comment='Tổng thu nhập trong một nhóm của một người')

    frequency_type = Column("FREQUENCY_TYPE", VARCHAR(75),
                            comment='Tần suất thu nhập: \\n- Thường xuyên\\n- Không thường xuyên')

    ratio_income = Column("RATIO_INCOME", Float, comment='Tỷ lệ nguồn thu này trên tổng nguồn thu nhập chiếm %')

    source_income_type = Column("SOURCE_INCOME_TYPE", VARCHAR(75),
                                comment='Nguồn thu nhập: Nguồn lương, cho thuê tài sản, kinh doanh .... (tham chiếu trong bảng udtm )')

    occasional_income_amount = Column("OCCASIONAL_INCOME_AMOUNT", Float)

    permanent_income_amount = Column("PERMANENT_INCOME_AMOUNT", Float, comment='Tổng thu nhập thường xuyên')


class PersonGroupIncomeDetail(BaseModel):
    __tablename__ = 'los_person_group_income_detail'
    __table_args__ = {'comment': 'Tổng hợp nguồn thu nhập theo từng nhóm'}

    id = Column("ID", Integer, primary_key=True)

    group_income_type = Column("GROUP_INCOME_TYPE", CHAR(5), comment='Loại hình thu nhập, nhóm')

    total_profit = Column("TOTAL_PROFIT", Float, comment='Tổng số tiền thu nhập')

    total_income = Column("TOTAL_INCOME", Float, comment='Tổng số tiền thu thập thực tế được cộng trong từng nhóm')

    person_group_income_id = Column('PERSON_GROUP_INCOME_ID', Integer)
