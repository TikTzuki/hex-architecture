from sqlalchemy import CHAR, VARCHAR, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class BusinessFinanceCashflowVendor(BaseModel):
    __tablename__ = 'los_business_finance_cashflow_vendor'
    __table_args__ = {'comment': 'Khai báo thông tin doanh nghiệp đầu vào / đầu ra'}

    id = Column(Integer, primary_key=True)
    business_finance_cashflow_id = Column(ForeignKey('los_business_finance_cashflow.id'))
    name = Column(VARCHAR(100), comment='Thông tin nhà cung cấp chính ( nhập tay )')
    exchange_method = Column(CHAR(20), comment='Hình thức thanh toán (tham chiếu trong bảng udtm )')
    payment_method = Column(CHAR(20), comment='Phương thức thanh toán: \\n- Tiền mặt\\n- Chuyển khoản (tham chiếu trong bảng udtm )')
    actived_flag = Column(VARCHAR(1))
    is_default = Column(VARCHAR(1), comment='Đánh dấu có phải nhà cung cấp chính hay không')

    business_finance_cashflow = relationship('BusinessFinanceCashflow')
