from sqlalchemy import VARCHAR, Column, ForeignKey, Integer, CHAR, Float
from sqlalchemy.orm import relationship

from database.base import BaseModel


class BusinessFinanceCashflow(BaseModel):
    __tablename__ = 'los_business_finance_cashflow'
    __table_args__ = {'comment': 'Thông tin đầu ra đầu vào'}

    id = Column(Integer, primary_key=True)
    business_finance_report_id = Column(ForeignKey('los_person_business_finance_report.id'))
    cashflow_type = Column(VARCHAR(20), comment='Loại đầu vào đầu ra (tham chiếu trong bảng udtm )')

    business_finance_report = relationship('PersonBusinessFinanceReport')


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


class BusinessFinanceCashflowValue(BaseModel):
    __tablename__ = 'los_business_finance_cashflow_value'
    __table_args__ = {'comment': 'Doanh thu bình quân phải thu theo thời gian'}

    id = Column(Integer, primary_key=True)
    business_finance_cashflow_id = Column(ForeignKey('los_business_finance_cashflow.id'))
    finance_timeline_assign_id = Column(Integer, comment='Tham chiếu qua bảng TIMELINE_ASSIGN để biết được cụ thể là thời gian và người  tạo.')
    value = Column(Float)

    business_finance_cashflow = relationship('BusinessFinanceCashflow')
