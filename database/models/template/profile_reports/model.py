from sqlalchemy import Column, Date, Integer
from sqlalchemy.dialects.oracle import VARCHAR2

from database.base import BaseModel


class ProfileReports(BaseModel):
    __tablename__ = 'los_profile_reports'
    __table_args__ = {'comment': 'Mã báo cáo theo hồ sơ vay vốn'}

    id = Column("ID", Integer, primary_key=True)

    loan_product_report_id = Column("LOAN_PRODUCT_REPORT_ID", VARCHAR2(10))

    los_id = Column("LOS_ID", VARCHAR2(20), comment='Mã hồ sơ vay vốn')

    sequence = Column('SEQUENCE', Integer, comment='Số thứ tự hồ sơ, nếu trong trường hợp được chia nhỏ sẽ đánh số 1,2,3. Còn mặc định = 1')

    link = Column("LINK", VARCHAR2(600), comment='Link liên kết với DMS để biết mở được file')

    publish_date = Column("PUBLISH_DATE", Date, comment='Ngày xác nhận hồ sơ, để public thông tin')

    view_total = Column("VIEW_TOTAL", Integer, comment='Tổng số người đã xem')

    download_total = Column("DOWNLOAD_TOTAL", Integer, comment='Tổng số người đã download')

    actived_flag = Column("ACTIVED_FLAG", VARCHAR2(1), comment='Tình trạng đã enabled/disabled')
