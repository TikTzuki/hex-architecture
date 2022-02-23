from sqlalchemy import CHAR, VARCHAR, Column, Integer

from database.base import BaseModel


class BusinessFinanceCashFlowVendor(BaseModel):
    __tablename__ = 'los_business_finance_cashflow_vendor'
    __table_args__ = {'comment': 'Khai báo thông tin doanh nghiệp đầu vào / đầu ra'}

    id = Column("ID", Integer, primary_key=True)

    business_finance_cashflow_id = Column('BUSINESS_FINANCE_CASHFLOW_ID', Integer)

    name = Column("NAME", VARCHAR(100), comment='Thông tin nhà cung cấp chính ( nhập tay )')

    exchange_method = Column("EXCHANGE_METHOD", CHAR(20), comment='Hình thức thanh toán (tham chiếu trong bảng udtm )')

    payment_method = Column("PAYMENT_METHOD", CHAR(20),
                            comment='Phương thức thanh toán: \n- Tiền mặt\n- Chuyển khoản (tham chiếu trong bảng udtm )')

    actived_flag = Column('ACTIVED_FLAG', VARCHAR(1))

    is_default = Column('IS_DEFAULT', VARCHAR(1), comment='Đánh dấu có phải nhà cung cấp chính hay không')
