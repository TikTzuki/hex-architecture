from sqlalchemy import VARCHAR, Column, DateTime, Integer

from database.models.utils import BaseModel


class PersonMarried(BaseModel):
    __tablename__ = 'los_person_married'

    id = Column("ID", Integer, primary_key=True)

    person_id = Column('PERSON_ID', Integer)

    married_status = Column("MARRIED_STATUS", VARCHAR(20), comment='(tham chiếu trong bảng udtm )')

    approval_date = Column("APPROVAL_DATE", DateTime, comment='Bắt đầu tính từ ngày.')
