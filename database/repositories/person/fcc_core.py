from sqlalchemy import VARCHAR, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonFccCore(BaseModel):
    __tablename__ = 'los_person_fcc_core'
    __table_args__ = {'comment': 'Nhập các thông tin trong CORE FCC,'}

    id = Column(Integer, primary_key=True)
    person_id = Column(ForeignKey('los_person.id'))
    fcc_core_name = Column(VARCHAR(20), comment='Các trường như sau:\\n+ CN_00_CUNG_CAP_TT_FATCA\\n+ THU_NHAP_BQ_03_THANG\\n+ NGHE_NGHIEP')
    fcc_core_value = Column(VARCHAR(50))

    person = relationship('Person')
