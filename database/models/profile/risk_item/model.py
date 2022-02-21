from sqlalchemy import VARCHAR, Column, Integer

from database.models.utils import BaseModel


class ProfileRiskItem(BaseModel):
    __tablename__ = 'los_profile_risk_item'
    __table_args__ = {'comment': 'Ghi nhận lại các rủi ro từ hồ sơ'}

    id = Column("ID", Integer, primary_key=True)

    sequence_id = Column("LOS_SEQUENCE_ID", Integer, comment='Link tới table LOS_PROFILE_SEQUENCE_ITEM')

    risk_type = Column("RISK_TYPE", VARCHAR(20), comment='Loại rủi ro (tham chiếu trong bảng udtm )')

    solution = Column("SOLUTION", VARCHAR(255))

    display_order = Column("DISPLAY_ORDER", Integer)

    credit_sequence_id = Column("LOS_CREDIT_SEQUENCE_ID", Integer,
                                comment='Link tới table LOS_PROFILE_CREDIT_SEQUENCE_ITEM')
