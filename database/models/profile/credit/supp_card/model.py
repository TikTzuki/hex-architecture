from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class ProfileCreditSuppCard(BaseModel):
    __tablename__ = 'los_profile_credit_supp_card'
    __table_args__ = {'comment': 'Bảng lưu trữ dữ liệu tạo thẻ phụ - trong hồ sơ vay'}

    id = Column("ID", Integer, primary_key=True)

    profile_credit_published_id = Column('PROFILE_CREDIT_PUBLISHED_ID', VARCHAR(100),
                                         comment='Mã hồ sơ thẻ chính')

    los_person_id = Column("LOS_PERSON_ID", VARCHAR(20), comment='Hồ sơ người được tạo thẻ')

    card_category_id = Column("CARD_CATEGORY_ID", VARCHAR(20), comment='Loại thẻ')

    card_color_id = Column("CARD_COLOR_ID", Integer, comment='Màu thẻ')

    credit_limit = Column("CREDIT_LIMIT", Float, comment='Hạn mức thẻ')

    embossed_card_first_name = Column("EMBOSSED_CARD_FIRST_NAME", VARCHAR(100), comment='Tên dập nổi Tên')

    embossed_card_middle_name = Column("EMBOSSED_CARD_MIDDLE_NAME", VARCHAR(100), comment='Tên đệm dập nổi')

    embossed_card_last_name = Column("EMBOSSED_CARD_LAST_NAME", VARCHAR(100), comment='Tên dập nổi họ')

    gift_received_flag = Column("GIFT_RECEIVED_FLAG", VARCHAR(1),
                                comment='Đủ điều kiện nhận quà không - tham chiếu Y/N trong UDTM')
