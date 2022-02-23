from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.oracle import VARCHAR2

from database.base import BaseModel


class ProfileScore(BaseModel):
    __tablename__ = 'los_profile_score'
    __table_args__ = {'comment': 'Bảng ghi nhận điểm XHTDNB của một hồ sơ.'}

    id = Column("ID", Integer, primary_key=True)

    sequence_id = Column('LOS_SEQUENCE_ID', Integer, comment='Link tới table LOS_PROFILE_SEQUENCE_ITEM')

    score = Column("SCORE", Float, comment='Tổng điểm của hồ sơ')

    score_rank_type = Column("SCORE_RANK_TYPE", VARCHAR2(20), comment='Hạng của hồ sơ')

    approval_date = Column("APPROVAL_DATE", DateTime, comment='Thời gian phê duyệt điểm trên hồ sơ')

    description = Column("DESCRIPTION", VARCHAR2(500), comment='Ghi chú')

    department_id = Column("DEPARTMENT_ID", VARCHAR2(10), comment='Bộ phận đánh giá điểm (NVKD, Cấp Phê Duyệt, QLRR)')

    display_order = Column("DISPLAY_ORDER", Integer, comment='Thứ tự xuất hiện')

    score_fcc = Column("LOS_SCORE_FCC", VARCHAR2(20), comment='Mã hồ sơ xếp hạng tín dụng nội bộ (chưa sử dụng)')

    credit_sequence_id = Column("LOS_CREDIT_SEQUENCE_ID", Integer,
                                comment='Link tới table LOS_PROFILE_CREDIT_SEQUENCE_ITEM')
