from sqlalchemy import VARCHAR, Column, DateTime, ForeignKey, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import Base


class ProfileReports(Base):
    __tablename__ = 'los_profile_reports'
    __table_args__ = {'comment': 'Mã báo cáo theo hồ sơ vay vốn'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    loan_product_report_id = Column(ForeignKey('los_ma_loan_product_report.id'))
    los_id = Column(ForeignKey('los_profile.id'), comment='(Mã hồ sơ vay vốn)')
    sequence = Column(NUMBER(asdecimal=False), server_default=text("1"), comment='(̣Số thứ tự hồ sơ, nếu trong trường hợp được chia nhỏ sẽ đánh số 1,2,3)')
    link = Column(VARCHAR(600), comment='(̣Link liên kết với DMS để biết mở được file)')
    publish_date = Column(DateTime, comment='(̣Ngày xác nhận hồ sơ, để public thông tin)')
    view_total = Column(NUMBER(asdecimal=False), server_default=text("0"), comment='(̣Tổng số người đã xem)')
    download_total = Column(NUMBER(asdecimal=False), server_default=text("0"), comment='(̣Tổng số người đã download)')
    actived_flag = Column(VARCHAR(1), comment='(̣Tình trạng đã enabled/disabled)')

    loan_product_report = relationship('MaLoanProductReport')
    los = relationship('Profile')
