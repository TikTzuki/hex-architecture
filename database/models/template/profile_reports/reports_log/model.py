from sqlalchemy import Column, Integer
from sqlalchemy.dialects.oracle import VARCHAR2

from database.base import BaseModel


class ProfileReportLog(BaseModel):
    __tablename__ = 'los_profile_report_log'
    # __table_args__ = {'comment': ''}

    id = Column("ID", Integer, primary_key=True)

    user_id = Column("USER_ID", VARCHAR2(32), comment='Người được ghi nhận log')

    method = Column("METHOD", VARCHAR2(12), comment='Download/Viewer/Edit')
