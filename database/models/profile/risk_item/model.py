from sqlalchemy import VARCHAR, Column, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class ProfileRiskItem(BaseModel):
    __tablename__ = 'los_profile_risk_item'
    __table_args__ = {'comment': 'Ghi nhận lại các rủi ro từ hồ sơ'}

    id = Column(Integer, primary_key=True)
    los_sequence_id = Column(ForeignKey('los_profile_sequence_item.id'), comment='link tới table LOS_PROFILE_SEQUENCE_ITEM')
    risk_type = Column(VARCHAR(20), comment='Loại rủi ro (tham chiếu trong bảng udtm )')
    solution = Column(VARCHAR(255), comment='Biện pháp hạn chế rủi ro')
    display_order = Column(Integer, comment='Thứ tự sắp xếp')
    created_at = Column(DateTime)
    created_by = Column(VARCHAR(20))
    modified_at = Column(DateTime)
    modified_by = Column(VARCHAR(255))
    uuid = Column(VARCHAR(50))
    los_credit_sequence_id = Column(NUMBER(asdecimal=False), comment='link tới table LOS_PROFILE_CREDIT_SEQUENCE_ITEM')

    los_sequence = relationship('LosProfileSequenceItem')
