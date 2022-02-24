from sqlalchemy import CHAR, VARCHAR, Column, DateTime, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonIdentity(BaseModel):
    __tablename__ = 'los_person_identity'
    __table_args__ = {'comment': 'Danh sách các hồ sơ pháp lý, cccd, cmnd.....'}

    id = Column(Integer, primary_key=True)
    identity_type = Column(VARCHAR(20), comment='Loại hồ sơ: CCCD, CMND, PASSPORT....')
    identity_number = Column(VARCHAR(15))
    place_of_issued = Column(VARCHAR(100), comment='Nơi cấp')
    issue_date = Column(DateTime, comment='Ngày tạo')
    date_of_expiry = Column(DateTime, comment='Ngày hết hạn')
    actived_flag = Column(CHAR(1))
    person_id = Column(ForeignKey('los_person.id'))
    primary_flag = Column(CHAR(1), comment='Loại giấy tờ chính')

    person = relationship('LosPerson')
