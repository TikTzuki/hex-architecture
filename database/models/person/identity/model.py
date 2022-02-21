from sqlalchemy import CHAR, VARCHAR, Column, DateTime, Integer

from database.models.utils import BaseModel


class PersonIdentity(BaseModel):
    __tablename__ = 'los_person_identity'
    __table_args__ = {'comment': 'Danh sách các hồ sơ pháp lý, cccd, cmnd.....'}

    id = Column("ID", Integer, primary_key=True)

    person_id = Column('PERSON_ID', Integer)

    identity_type = Column("IDENTITY_TYPE", VARCHAR(20), comment='Loại hồ sơ: CCCD, CMND, PASSPORT....')

    identity_number = Column("IDENTITY_NUMBER", VARCHAR(15))

    place_of_issued = Column("PLACE_OF_ISSUED", VARCHAR(100), comment='Nơi cấp')

    issue_date = Column("ISSUE_DATE", DateTime, comment='Ngày tạo')

    date_of_expiry = Column("DATE_OF_EXPIRY", DateTime, comment='Ngày hết hạn')

    actived_flag = Column("ACTIVED_FLAG", CHAR(1))

    primary_flag = Column("PRIMARY_FLAG", CHAR(1), comment='Giấy tờ định danh chính')
