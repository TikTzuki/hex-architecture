from sqlalchemy import Column, Integer
from sqlalchemy.dialects.oracle import VARCHAR2

from database.base import BaseModel


class MaLoanProductReport(BaseModel):
    __tablename__ = 'los_ma_loan_product_report'
    # __table_args__ = {'comment': ''}

    id = Column("ID", Integer, primary_key=True)

    loan_product_id = Column("LOAN_PRODUCT_ID", VARCHAR2(10), comment='Mã sản phẩm vay vốn')

    version = Column("VERSION", VARCHAR2(50), comment='Mã số văn bản báo cáo')

    title = Column("TITLE", VARCHAR2(100), comment='Tiêu đề nội dung của báo cáo')

    description = Column("DESCRIPTION", VARCHAR2(200), comment='Diễn giải nhanh nội dung báo cáo')

    report_group_id = Column("REPORT_GROUP_ID", VARCHAR2(105), comment='Nhóm báo cáo, tham chiếu vào bảng UDTM (Tờ trình, giấy đề nghị')

    required_flag = Column('REQUIRED_FLAG', VARCHAR2(1), comment='Bắt buộc phải có trong hồ sơ vay vốn')

    split_flag = Column('SPLIT_FLAG', VARCHAR2(1), comment='Cho phép chia nhỏ báo cáo làm nhiều lần để hoàn thiện')

    display_order = Column("DISPLAY_ORDER", Integer, comment='Thứ tự sắp xếp của văn bản')
