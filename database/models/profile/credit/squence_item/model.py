from sqlalchemy import VARCHAR, Column, DateTime, Float, Integer, text

from database.base import BaseModel


class ProfileCreditSequenceItem(BaseModel):
    __tablename__ = 'los_profile_credit_sequence_item'
    __table_args__ = {'comment': 'Lưu trữ thông tin về việc vay thẻ/thay đổi hạn mức của thẻ,'}

    id = Column(Integer, primary_key=True)
    los_profile_id = Column(VARCHAR(20), comment='Mã hồ sơ vay vốn tham chiếu qua bảng LOS_PROFILE')
    sequence = Column(Integer, server_default=text("1"), comment='1')
    total_primary_cardholder_limit = Column(Float, comment='Tổng hạn mức thẻ chính')
    total_supp_cardholder_limit = Column(Float, comment='Tổng hạn mức thẻ phụ')
    total_income = Column(Float, comment='Tổng thu nhập')
    occasional_income_amount = Column(Float, comment='Tổng thu nhập không thường xuyên')
    permanent_income_amount = Column(Float, comment='Tổng thu nhập thường xuyên')
    total_cost = Column(Float, comment='Tổng chi phí')
    different_value = Column(Float, comment='Cân đối thu nhập và chi phí')
    comment_credit_flag = Column(VARCHAR(100), comment='Đánh giá khả năng trả nợ (Đảm bảo / Không đảm bảo)')
    description_comment_credit = Column(VARCHAR(100), comment='Diễn giải nội dung của nhận xét')
    accept_credit_flag = Column(VARCHAR(100), comment='Kiến nghị và đề xuất cấp tín dụng')
    reason_credit = Column(VARCHAR(100), comment='Diễn giải lý do kiến nghị và đề xuất')
    actived_flag = Column(VARCHAR(1), comment='Kích hoạt/không kích hoạt')
    uuid = Column(VARCHAR(50))
    minimum_payment = Column(Float, comment='Số tiền thanh toán tối thiểu')
    total_line_of_credit = Column(Float, comment='Tổng hạn mức thẻ tín dụng')
    pni_value = Column(Float, comment='Hệ số đánh giá khả năng trả nợ')
    able_pay_type = Column(VARCHAR(3), comment='Xác nhận đã thẩm định thành công và đủ khả năng về thanh toán chi phí sinh hoạt khác. hoặc khong đủ khả năng thành toán....')
    able_capital_requirement = Column(VARCHAR(100), comment='Đánh giá  về phương án và nhu cầu vay vốn')
    summary = Column(VARCHAR(500), comment='Nhận xét')
    created_at = Column(DateTime)
    created_by = Column(VARCHAR(20))
    modified_at = Column(DateTime)
    modified_by = Column(VARCHAR(20))
    dti_value = Column(Float, comment='Hệ số nợ trên thu nhập (DTI - Debt to Income Ratio) = tổng nợ / tổng thu nhập')
