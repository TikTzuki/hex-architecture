from sqlalchemy import VARCHAR, Column, Integer

from database.models.utils import BaseModel


class PersonFccCore(BaseModel):
    __tablename__ = 'los_person_fcc_core'
    __table_args__ = {'comment': 'Nhập các thông tin trong CORE FCC,'}

    id = Column("ID", Integer, primary_key=True)

    person_id = Column('PERSON_ID', Integer)

    fcc_core_name = Column('FCC_CORE_NAME', VARCHAR(20),
                           comment='Các trường như sau:\\n+ CN_00_CUNG_CAP_TT_FATCA\\n+ THU_NHAP_BQ_03_THANG\\n+ NGHE_NGHIEP')

    fcc_core_value = Column('FCC_CORE_VALUE', VARCHAR(50))
