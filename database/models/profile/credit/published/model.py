from sqlalchemy import VARCHAR, Column, Float, Integer

from database.models.utils import BaseModel


class ProfileCreditPublished(BaseModel):
    __tablename__ = 'los_profile_credit_published'
    __table_args__ = {'comment': 'Hồ sơ vay cho việc phát hành thẻ mới.'}

    id = Column("ID", Integer, primary_key=True)

    card_category_id = Column('CARD_CATEGORY_ID', VARCHAR(10), comment='Loại thẻ, master card, visa....')

    credit_limit = Column("CREDIT_LIMIT", Float, comment='Hạn mức của thẻ')

    promotion_id = Column("PROMOTION_ID", Float, comment='Thông tin lựa chọn quà tặng')

    profile_credit_sequence_id = Column("PROFILE_CREDIT_SEQUENCE_ID", VARCHAR(100), comment='Mã hồ sơ vay')

    embossed_card_first_name = Column("EMBOSSED_CARD_FIRST_NAME", VARCHAR(100), comment='Tên dập nổi Tên')

    embossed_card_middle_name = Column("EMBOSSED_CARD_MIDDLE_NAME", VARCHAR(100), comment='Tên đệm dập nổi')

    embossed_card_last_name = Column("EMBOSSED_CARD_LAST_NAME", VARCHAR(100), comment='Tên dập nổi họ')

    gift_received_flag = Column("GIFT_RECEIVED_FLAG", VARCHAR(1),
                                comment='Đủ điều kiện nhận quà không - tham chiếu Y/N trong UDTM')

    payment_method_type_id = Column("PAYMENT_METHOD_TYPE_ID", VARCHAR(50),
                                    comment='Hình thức thanh toán dự nợ (PAYMENT_METHOD_TYPE), link sang bảng UDTM các giá trị.')

    debt_deduction_account = Column("DEBT_DEDUCTION_ACCOUNT", VARCHAR(200),
                                    comment='Tài khoản dùng trích nợ, sẽ móc nối với các system khác để fill giá trị mỗi lần chạy, hiện tại setup sẵn, chưa sử dụng được')
