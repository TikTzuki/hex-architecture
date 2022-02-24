from sqlalchemy import VARCHAR, Column, Float, Integer

from database.base import BaseModel


class ProfileCreditModified(BaseModel):
    __tablename__ = 'los_profile_credit_modified'
    __table_args__ = {'comment': 'Bảng lưu hồ sơ thay đổi hạn mức thẻ/thay đổi hình thức bảo đảm thẻ'}

    id = Column("ID", Integer, primary_key=True)

    profile_credit_sequence_id = Column('PROFILE_CREDIT_SEQUENCE_ID', Integer, comment='Mã hồ sơ vay vốn')

    person_credit_card_id = Column("PERSON_CREDIT_CARD_ID", VARCHAR(100),
                                   comment='Mã thẻ của khách hàng cần điều chỉnh thay đổi.')

    card_category_id = Column("CARD_CATEGORY_ID", VARCHAR(10), comment='Hạng thẻ. loại thẻ cần nâng cấp')

    credit_limit = Column("CREDIT_LIMIT", Float, comment='Hạn mức của thẻ cần nâng cấp')

    card_color_id = Column("CARD_COLOR_ID", VARCHAR(10), comment='Thay đổi màu thẻ')

    security_interests_type = Column("SECURITY_INTERESTS_TYPE", VARCHAR(10),
                                     comment='Hình thức bảo đảm thẻ được thay đổi')

    security_interests_flag = Column("SECURITY_INTERESTS_FLAG", VARCHAR(1),
                                     comment='Đánh dấu có thay đổi hình  thức bảo đảm thẻ không')

    credit_card_type = Column("CREDIT_CARD_TYPE", VARCHAR(10), comment='Thay đổi thẻ chính thức/hay thẻ tạm thời')
