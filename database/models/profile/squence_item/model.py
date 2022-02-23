from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.oracle import VARCHAR2

from database.base import BaseModel


class ProfileSequenceItem(BaseModel):
    __tablename__ = 'los_profile_sequence_item'
    __table_args__ = {'comment': 'Ghi lại thông tin của các lần khai báo hồ sơ về nguồn thu và tài sản bảo đảm.'}

    id = Column(Integer, primary_key=True)
    los_id = Column(VARCHAR(20), comment='Mã hồ sơ LOS')
    sequence = Column(Integer, server_default=text("1"), comment='Số lần khai báo hồ sơ theo lần (mặc định là 1)')
    title = Column(VARCHAR(100), comment='Tiêu đề khai báo hồ sơ LOS')
    currency_type = Column(VARCHAR(20), comment='Loại tiền cho vay')
    total_capital = Column(Float, comment='Tổng nhu cầu vay vốn')
    owner_capital = Column(Float, comment='Số vốn tự có')
    loan_amount = Column(Float, comment='Số tiền cần vay')
    lending_method = Column(VARCHAR(20), comment='Phương thức đề nghị cấp tín dụng')
    repayment_period = Column(Integer, comment='Thời hạn đề nghị CTD/duy trì HMTD (tháng)')
    drawdown_duration = Column(Integer, comment='Thời hạn từng lần rút vốn (tháng)')
    grace_period = Column(Integer, comment='Thời gian ân hạn (tháng)')
    percent_value = Column(Float, comment='Tỷ lệ tài trợ của SCB (Tiền vay / Tổng số vốn)')
    lending_rate = Column(Float, comment='Lãi suất cho vay (dự kiến)')
    reset_interest_rate = Column(VARCHAR(10), comment='Định kỳ điều chỉnh lãi suất cho vay')
    amplitude_interest_rate = Column(Float, comment='Biên độ điều chỉnh lãi suất cho vay (%)')
    disbursement_method = Column(VARCHAR(20), comment='Phương thức giải ngân: "Chuyển khoản, tiền mặt, tiền mặt hoặc chuyển khoản". (tham chiếu trong bảng udtm )')
    loan_principal_method = Column(VARCHAR(20), comment='Phương thức trả nợ gốc')
    debt_service_method = Column(VARCHAR(20), comment='Phương thức trả nợ lãi')
    principal_period_value = Column(Float, comment='Số tiền gốc và lãi dự kiến trả mỗi kỳ')
    total_income = Column(Float, comment='Tổng thu nhập')
    occasional_income_amount = Column(Float, comment='Tổng thu nhập không thường xuyên')
    permanent_income_amount = Column(Float, comment='Tổng thu nhập thường xuyên')
    total_cost = Column(Float, comment='Tổng chi phí')
    different_value = Column(Float, comment='Cân đối thu nhập và chi phí')
    cost_value_max = Column(Float, comment='Số tiền (gốc + lãi) phải trả cao nhất trong thời kỳ vay')
    pni_value = Column(Float, comment='Hệ số đánh giá khả năng trả nợ (PNI)')
    dti_value = Column(Float, comment='Hệ số nợ trên thu nhập (DTI)')
    comment_credit_flag = Column(VARCHAR(10), comment='Đánh giá khả năng trả nợ (Đảm bảo / Không đảm bảo) (LOS_01_15 -12)')
    description_comment_credit = Column(VARCHAR(1000), comment='Diễn giải nội dung của nhận xét (LOS_01_15 -12)')
    accept_credit_flag = Column(VARCHAR(10), comment='Kiến nghị và đề xuất cấp tín dụng (LOS_01_07-2)')
    reason_credit = Column(VARCHAR(500), comment='Diễn giải lý do kiến nghị và đề xuất CTD (LOS_01_07-2)')
    actived_flag = Column(VARCHAR(1), comment='Kích hoạt/không kích hoạt')
    uuid = Column(VARCHAR(100))
    created_at = Column(DateTime)
    created_by = Column(VARCHAR(20))
    modified_at = Column(DateTime)
    modified_by = Column(VARCHAR(20))
    able_pay_type = Column(VARCHAR(3), comment='Xác nhận đã thẩm định thành công và đủ khả năng về thanh toán chi phí sinh hoạt khác. hoặc khong đủ khả năng thành toán....')
    able_capital_requirement = Column(VARCHAR(100), comment='Đánh giá  về phương án và nhu cầu vay vốn')
    summary = Column(VARCHAR(500), comment='Nhận xét')

