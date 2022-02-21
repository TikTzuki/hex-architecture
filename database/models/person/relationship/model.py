from sqlalchemy import CHAR, Column, Integer
from sqlalchemy.dialects.oracle import VARCHAR2

from database.models.utils import BaseModel


class PersonalRelationship(BaseModel):
    __tablename__ = 'los_personal_relationship'
    __table_args__ = {'comment': 'Mối quan hệ giữa các person với nhau, người đồng vay, người hôn phối, trả nợ.....'}

    id = Column("ID", Integer, primary_key=True)

    los_id = Column('LOS_ID', CHAR(20))

    person_id = Column('PERSON_ID', Integer)

    to_personal_id = Column('TO_PERSONAL_ID', Integer)

    relationship_type = Column('RELATIONSHIP_TYPE', VARCHAR2(75),
                               comment='Mối liên hệ: Người đồng vay, người vay vốn. người hôn phối,')

    actived_flag = Column('ACTIVED_FLAG', CHAR(1), comment='Kích hoạt / Không kích hoạt')

    family_relationship_type = Column('FAMILY_RELATIONSHIP_TYPE', VARCHAR2(20),
                                      comment='Mối quan hệ với người vay trong gia đình như anh/chị em, vợ chồng, bố mẹ,con cái')
