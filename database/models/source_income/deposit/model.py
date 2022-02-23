from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class SourceIncomeDeposit(BaseModel):
    __tablename__ = 'los_source_income_deposit'
    __table_args__ = {'comment': 'Nguồn thu nhập từ giấy tờ có giá trị'}

    id = Column(Integer, primary_key=True)
    person_group_income_id = Column(ForeignKey('los_person_group_income.id'))
    frequency_type = Column(VARCHAR(75), comment='(tham chiếu trong bảng udtm )')
    publish_unit = Column(VARCHAR(75), comment='Đơn vị phát hành:\\n- SCB\\n- TCTD Khác')
    account_number = Column(VARCHAR(30), comment='Số tài khoản')
    name = Column(VARCHAR(100), comment='Tên loại giấy tờ, tiền gởi, sổ tiết kiệm....')
    currency_type = Column(VARCHAR(75), comment='Loại tiền tệ')
    balance = Column(Float, comment='Số tiền thanh toán, Số tiền gởi, số tiền của giáy tờ có giá trị')
    term = Column(Float, comment='Thời gian duy trì liên tục số dư')
    profit = Column(Float)
    income = Column(Float)
    accept_blocked_account = Column(CHAR(100), comment='Chấp nhận cho phép phong tỏa giấy tờ, sổ tiết kiệm')
    display_order = Column(Integer)
    income_ratio = Column(Float)

    person_group_income = relationship('LosPersonGroupIncome')

