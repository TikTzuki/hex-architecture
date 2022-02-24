from sqlalchemy import CHAR, VARCHAR, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonalRelationship(BaseModel):
    __tablename__ = 'los_personal_relationship'
    __table_args__ = {'comment': 'Mối quan hệ giữa các person với nhau, người đồng vay, người hôn phối, trả nợ.....'}

    id = Column(Integer, primary_key=True)
    los_id = Column(CHAR(20), comment='Hồ sơ vay vốn')
    person_id = Column(ForeignKey('los_person.id'))
    to_personal_id = Column(Integer)
    relationship_type = Column(VARCHAR(75), comment='Mối liên hệ: Người đồng vay, người vay vốn. người hôn phối,')
    actived_flag = Column(CHAR(1), comment='Kích hoạt / Không kích hoạt')

    family_relationship_type = Column(VARCHAR(20), comment='Mối quan hệ với người vay trong gia đình như anh/chị em, vợ chồng, bố mẹ,con cái')

    person = relationship('Person')
