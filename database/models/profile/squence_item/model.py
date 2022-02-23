from sqlalchemy import CHAR, VARCHAR, Column, Float, Integer
from sqlalchemy.dialects.oracle import VARCHAR2

from database.base import BaseModel


class ProfileSequenceItem(BaseModel):
    __tablename__ = 'los_profile_sequence_item'
    __table_args__ = {'comment': 'Ghi lại thông tin của các lần khai báo hồ sơ về nguồn thu và tài sản bảo đảm.'}

    id = Column("ID", Integer, primary_key=True)

    los_id = Column('LOS_ID', VARCHAR2(20), comment='Mã hồ sơ LOS')

    sequence = Column("SEQUENCE", Integer, default=1, comment='Số lần khai báo hồ sơ theo lần (mặc định là 1)')

    title = Column("TITLE", VARCHAR2(100), comment='Tiêu đề khai báo hồ sơ LOS')

    currency_type = Column("CURRENCY_TYPE", VARCHAR2(20), comment='Loại tiền cho vay')

    total_capital = Column("TOTAL_CAPITAL", Float, comment='Tổng như cầu vay vốn')

    owner_capital = Column("OWNER_CAPITAL", Float, comment='Số vốn tự có được')

    loan_amount = Column("LOAN_AMOUNT", Float, comment='Số tiền cần vay')

    lending_method = Column("LENDING_METHOD", VARCHAR2(20), comment='Phương thức đề nghị cấp tín dụng')

    repayment_period = Column("REPAYMENT_PERIOD", Integer, comment='Thời hạn đề nghị CTD/duy trì HMTD (tháng)')

    drawdown_duration = Column("DRAWDOWN_DURATION", Integer, comment='Thời hạn từng lần rút vốn (tháng)')

    grace_period = Column("GRACE_PERIOD", Integer, comment='Thời gian ân hạn (tháng)')

    percent_value = Column("PERCENT_VALUE", Float, comment='Tỷ lệ % giữa vốn vay và tổng số vốn.')

    lending_rate = Column("LENDING_RATE", Float, comment='Lãi suất cho vay (dự kiến)')

    reset_interest_rate = Column("RESET_INTEREST_RATE", VARCHAR2(10), comment='Định kỳ điều chỉnh lãi suất cho vay')

    amplitude_interest_rate = Column("AMPLITUDE_INTEREST_RATE", Float,
                                     comment='Biên độ điều chỉnh lãi suất cho vay (%)')

    disbursement_method = Column("DISBURSEMENT_METHOD", VARCHAR2(20),
                                 comment='Phương thức giải ngân: "Chuyển khoản, tiền mặt, tiền mặt hoặc chuyển khoản". (tham chiếu trong bảng udtm )')

    loan_principal_method = Column("LOAN_PRINCIPAL_METHOD", VARCHAR2(20), comment='Phương thức trả nợ gốc')

    debt_service_method = Column("DEBT_SERVICE_METHOD", VARCHAR2(20), comment='Phương thức trả nợ lãi')

    principal_period_value = Column("PRINCIPAL_PERIOD_VALUE", Float, comment='Số tiền gốc và lãi dự kiến trả mỗi kỳ')

    total_income = Column("TOTAL_INCOME", Float, comment='Tổng thu nhập')

    occasional_income_amount = Column("OCCASIONAL_INCOME_AMOUNT", Float, comment='Tổng thu nhập không thường xuyên')

    permanent_income_amount = Column("PERMANENT_INCOME_AMOUNT", Float, comment='Tổng thu nhập thường xuyên')

    total_cost = Column("TOTAL_COST", Float, comment='Tổng chi phí')

    different_value = Column("DIFFERENT_VALUE", Float, comment='Cân đối thu nhập và chi phí')

    cost_value_max = Column("COST_VALUE_MAX", Float, comment='Số tiền (gốc + lãi) phải trả cao nhất trong thời kỳ vay')

    pni_value = Column("PNI_VALUE", Float, comment='Hệ số đánh giá khả năng trả nợ (PNI)')

    dti_value = Column("DTI_VALUE", Float, comment='Hệ số nợ trên thu nhập (DTI)')

    comment_credit_flag = Column("COMMENT_CREDIT_FLAG", VARCHAR2(20),
                                 comment='Đánh giá khả năng trả nợ (Đảm bảo / Không đảm bảo) (LOS_01_15 -12)')

    description_comment_credit = Column("DESCRIPTION_COMMENT_CREDIT", VARCHAR2(1000),
                                        comment='Diễn giải nội dung của nhận xét (LOS_01_15 -12)')

    accept_credit_flag = Column("ACCEPT_CREDIT_FLAG", VARCHAR2(10),
                                comment='Kiến nghị và đề xuất cấp tín dụng (LOS_01_07-2)')

    reason_credit = Column("REASON_CREDIT", VARCHAR(500),
                           comment='Diễn giải lý do kiến nghị và đề xuất CTD (LOS_01_07-2)')

    actived_flag = Column("ACTIVED_FLAG", CHAR(2), comment='Kích hoạt/không kích hoạt')

    summary = Column("SUMMARY", VARCHAR(500), comment='Nhận xét')

    able_pay_type = Column("ABLE_PAY_TYPE", CHAR(3), comment='Xác nhận đã thẩm định thành công và đủ khả năng về thanh toán chi phí sinh hoạt khác. hoặc khong đủ khả năng thành toán....')

    able_capital_requirement = Column("ABLE_CAPITAL_REQUIREMENT", VARCHAR(100),
                                      comment='Đánh giá  về phương án và nhu cầu vay vốn')
