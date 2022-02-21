from sqlalchemy import Column, Float, Integer
from sqlalchemy.dialects.oracle import VARCHAR2

from database.models.utils import BaseModel


class ProfileIncome(BaseModel):
    __tablename__ = 'los_profile_income'
    __table_args__ = {'comment': 'Ghi nhận các đợt khai báo nguồn thu nhập của từng đối tượng'}

    id = Column("ID", Integer, primary_key=True)

    income_sequence_id = Column('LOS_INCOME_SEQUENCE_ID', Integer, comment='Liên kết với tờ khai báo thu nhập tổng')

    person_id = Column("PERSON_ID", Integer, comment='Mã cá nhân ghi nhận thu nhập')

    total_income = Column("TOTAL_INCOME", Float, comment='Tổng thu nhập của người đang xét')

    relationship_type = Column("RELATIONSHIP_TYPE", VARCHAR2(75),
                               comment='Mối quan hệ của người khai báo thu nhập với người vay chính')
