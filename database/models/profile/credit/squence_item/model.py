from sqlalchemy import CHAR, VARCHAR, Column, Float, Integer

from database.models.utils import BaseModel


class ProfileCreditSequenceItem(BaseModel):
    __tablename__ = 'los_profile_credit_sequence_item'
    __table_args__ = {'comment': 'Lưu trữ thông tin về việc vay thẻ/thay đổi hạn mức của thẻ,'}

    id = Column("ID", Integer, primary_key=True)

    profile_id = Column('LOS_PROFILE_ID', VARCHAR(20), comment='Mã hồ sơ vay vốn tham chiếu qua bảng LOS_PROFILE')

    sequence = Column("SEQUENCE", Integer)

    total_primary_cardholder_limit = Column("TOTAL_PRIMARY_CARDHOLDER_LIMIT", Float, comment='Tổng hạn mức thẻ chính')

    total_supp_cardholder_limit = Column("TOTAL_SUPP_CARDHOLDER_LIMIT", Float, comment='Tổng hạn mức thẻ phụ')

    total_income = Column("TOTAL_INCOME", Float, comment='Tổng thu nhập')

    occasional_income_amount = Column("OCCASIONAL_INCOME_AMOUNT", Float, comment='Tổng thu nhập không thường xuyên')

    permanent_income_amount = Column("PERMANENT_INCOME_AMOUNT", Float, comment='Tổng thu nhập thường xuyên')

    total_cost = Column("TOTAL_COST", Float, comment='Tổng chi phí')

    different_value = Column("DIFFERENT_VALUE", Float, comment='Cân đối thu nhập và chi phí')

    comment_credit_flag = Column("COMMENT_CREDIT_FLAG", VARCHAR(100),
                                 comment='Đánh giá khả năng trả nợ (Đảm bảo / Không đảm bảo)')

    description_comment_credit = Column("DESCRIPTION_COMMENT_CREDIT", VARCHAR(100),
                                        comment='Diễn giải nội dung của nhận xét')

    accept_credit_flag = Column("ACCEPT_CREDIT_FLAG", VARCHAR(100), comment='Kiến nghị và đề xuất cấp tín dụng')

    reason_credit = Column("REASON_CREDIT", VARCHAR(100), comment='Diễn giải lý do kiến nghị và đề xuất')

    actived_flag = Column("ACTIVED_FLAG", VARCHAR(1), comment='Kích hoạt/không kích hoạt')

    uuid = Column("UUID", VARCHAR(50))

    minimum_payment = Column("MINIMUM_PAYMENT", Float, comment='Số tiền thanh toán tối thiểu')

    total_line_of_credit = Column("TOTAL_LINE_OF_CREDIT", Float, comment='Tổng hạn mức thẻ tín dụng')

    pni_value = Column("PNI_VALUE", Float, comment='Hệ số đánh giá khả năng trả nợ')

    summary = Column("SUMMARY", VARCHAR(500), comment='Nhận xét')

    able_pay_type = Column("ABLE_PAY_TYPE", CHAR(3),
                           comment='Xác nhận đã thẩm định thành công và đủ khả năng về thanh toán chi phí sinh hoạt khác. hoặc khong đủ khả năng thành toán....')  # noqa

    able_capital_requirement = Column("ABLE_CAPITAL_REQUIREMENT", VARCHAR(100),
                                      comment='Đánh giá  về phương án và nhu cầu vay vốn')
