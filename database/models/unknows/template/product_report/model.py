from sqlalchemy import VARCHAR, Column, ForeignKey
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import Base


class MaLoanProductReport(Base):
    __tablename__ = 'los_ma_loan_product_report'

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    loan_product_id = Column(ForeignKey('los_loan_product.id'), comment='(Mã sản phẩm vay vốn)')
    version = Column(VARCHAR(50), comment='(Mã số văn bản báo cáo)')
    title = Column(VARCHAR(100), comment='(Tiêu đề nội dung của báo cáo)')
    description = Column(VARCHAR(200), comment='(Diễn giải nhanh nội dung báo cáo)')
    report_group_id = Column(VARCHAR(105), comment='(Tham chiếu trong bảng udtm, Tờ trình, giấy đề nghị)')
    required_flag = Column(VARCHAR(1), comment='(Bắt buộc phải có trong hồ sơ vay vốn)')
    split_flag = Column(VARCHAR(1), comment='(̣Cho phép chia nhỏ báo cáo làm nhiều lần để hoàn thiện)')
    display_order = Column(NUMBER(asdecimal=False), comment='(̣Thứ tự hiển thị của văn bản, Số thứ tự đi theo nhóm mỗi nhóm lại lặp lại 1,2,3)')

    loan_product = relationship('LoanProduct')
