from sqlalchemy import VARCHAR, Column, ForeignKey
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import Base


class ProfileReportLog(Base):
    __tablename__ = 'los_profile_report_log'

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    los_profile_report_id = Column(ForeignKey('los_profile_reports.id'), comment='(̣Mã báo cáo theo hồ sơ vay vốn)')
    user_id = Column(VARCHAR(32), comment='(̣Người được ghi nhận log)')
    method = Column(VARCHAR(12), comment='(̣Download/Viewer/Edit)')

    los_profile_report = relationship('ProfileReports')
