from sqlalchemy import VARCHAR, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonMarried(BaseModel):
    __tablename__ = 'los_person_married'

    id = Column(Integer, primary_key=True)
    person_id = Column(ForeignKey('los_person.id'))
    married_status = Column(VARCHAR(20), comment='(tham chiếu trong bảng udtm )')
    approval_date = Column(DateTime, comment='Bắt đầu tính từ ngày.')

    person = relationship('Person')
