from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonEducation(BaseModel):
    __tablename__ = 'los_person_education'

    id = Column(Integer, primary_key=True)
    person_id = Column(ForeignKey('los_person.id'))
    education_status = Column(VARCHAR(20), comment='(tham chiếu trong bảng udtm )')
    approval_date = Column(DateTime)
    actived_flag = Column(CHAR(1))

    person = relationship('LosPerson')
