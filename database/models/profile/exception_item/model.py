from sqlalchemy import CHAR, VARCHAR, Column, Integer

from database.models.utils import BaseModel


class ProfileExceptionItem(BaseModel):
    __tablename__ = 'los_profile_exception_item'
    __table_args__ = {'comment': 'Danh sách các ngoại lệ của một hồ sơ'}

    id = Column("ID", Integer, primary_key=True)

    sequence_id = Column("LOS_SEQUENCE_ID", Integer, comment='Link tới table LOS_PROFILE_SEQUENCE_ITEM')

    policy_detail_id = Column("POLICY_DETAIL_ID", Integer, comment='Mã ngoại lệ')

    description = Column("DESCRIPTION", VARCHAR(200), comment='Diễn giải ngoại lệ')

    auto_flag = Column("AUTO_FLAG", CHAR(5), comment='Field ghi nhận đó là hệ thống tự động tạo hay người nhập')

    display_order = Column("DISPLAY_ORDER", Integer)

    credit_sequence_id = Column("LOS_CREDIT_SEQUENCE_ID", Integer,
                                comment='Link tới table LOS_PROFILE_CREDIT_SEQUENCE_ITEM')

    realistic_interpretation = Column("REALISTIC_INTERPRETATION", VARCHAR(200), comment='Diễn giải thực tế')
