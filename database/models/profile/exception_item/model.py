from sqlalchemy import CHAR, VARCHAR, Column, ForeignKey, Integer
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class ProfileExceptionItem(BaseModel):
    __tablename__ = 'los_profile_exception_item'
    __table_args__ = {'comment': 'Danh sách các ngoại lệ của một hồ sơ'}

    id = Column(Integer, primary_key=True)
    los_sequence_id = Column(ForeignKey('los_profile_sequence_item.id'), comment='link tới table LOS_PROFILE_SEQUENCE_ITEM')
    policy_detail_id = Column(Integer, comment='Mã ngoại lệ')
    description = Column(VARCHAR(200), comment='Diễn giải ngoại lệ')
    auto_flag = Column(CHAR(5), comment='Field ghi nhận đó là hệ thống tự động tạo hay người nhập')
    display_order = Column(Integer)

    los_credit_sequence_id = Column(NUMBER(asdecimal=False), comment='link tới table LOS_PROFILE_CREDIT_SEQUENCE_ITEM')
    realistic_interpretation = Column(VARCHAR(200), comment='Diễn giải thực tế')

    los_sequence = relationship('LosProfileSequenceItem')
