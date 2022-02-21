from sqlalchemy import CHAR, VARCHAR, Column, DateTime, Integer

from database.models.utils import BaseModel


class PersonEducation(BaseModel):
    __tablename__ = 'los_person_education'

    id = Column("ID", Integer, primary_key=True)

    person_id = Column('PERSON_ID', Integer)

    education_status = Column("EDUCATION_STATUS", VARCHAR(20), comment='(tham chiếu trong bảng udtm )')

    approval_date = Column("APPROVAL_DATE", DateTime)

    actived_flag = Column("ACTIVED_FLAG", CHAR(1))
