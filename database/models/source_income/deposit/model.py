from sqlalchemy import CHAR, VARCHAR, Column, Float, Integer

from database.models.utils import BaseModel


class SourceIncomeDeposit(BaseModel):
    __tablename__ = 'los_source_income_deposit'
    __table_args__ = {'comment': 'Nguồn thu nhập từ giấy tờ có giá trị'}

    id = Column("ID", Integer, primary_key=True)

    person_group_income_id = Column('PERSON_GROUP_INCOME_ID', Integer)

    frequency_type = Column("FREQUENCY_TYPE", VARCHAR(75), comment='(tham chiếu trong bảng udtm )')

    publish_unit = Column("PUBLISH_UNIT", VARCHAR(75), comment='Đơn vị phát hành:\\n- SCB\\n- TCTD Khác')

    account_number = Column("ACCOUNT_NUMBER", VARCHAR(30), comment='Số tài khoản')

    name = Column("NAME", VARCHAR(100), comment='Tên loại giấy tờ, tiền gởi, sổ tiết kiệm....')

    currency_type = Column("CURRENCY_TYPE", VARCHAR(75), comment='Loại tiền tệ')

    balance = Column("BALANCE", Float, comment='Số tiền thanh toán, Số tiền gởi, số tiền của giáy tờ có giá trị')

    term = Column("TERM", Float, comment='Thời gian duy trì liên tục số dư')

    profit = Column("PROFIT", Float)

    income = Column("INCOME", Float)

    accept_blocked_account = Column("ACCEPT_BLOCKED_ACCOUNT", CHAR(100),
                                    comment='Chấp nhận cho phép phong tỏa giấy tờ, sổ tiết kiệm')

    display_order = Column("DISPLAY_ORDER", Integer)

    income_ratio = Column("INCOME_RATIO", Float)
