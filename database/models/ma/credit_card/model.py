from sqlalchemy import VARCHAR, Column, Integer

from database import Base


class MaCreditCard(Base):
    __tablename__ = 'los_ma_credit_card'
    __table_args__ = {'comment': 'Bảng danh sách các loại thẻ tín dụng'}

    id = Column("ID", VARCHAR(20), primary_key=True)

    card_group_id = Column("CARD_GROUP_ID", VARCHAR(100), comment='Nhóm thẻ master, visa, credit....')

    card_name = Column("CARD_NAME", VARCHAR(100), comment='Tên thẻ vàng, bạc, chuẩn')

    is_published_flag = Column("IS_PUBLISHED_FLAG", VARCHAR(1), comment='Thẻ dành cho mở thẻ chính')

    is_supp_flag = Column("IS_SUPP_FLAG", VARCHAR(1), comment='Thẻ dành cho mở thẻ phụ')

    actived_flag = Column("ACTIVED_FLAG", VARCHAR(1))


class MaCreditProductCard(Base):
    __tablename__ = 'los_ma_credit_product_card'
    __table_args__ = {
        'comment': 'Bảng mapping các nhóm thẻ và các sản phẩm vay để biết nếu vay theo đối tượng nào sẽ được dùng những loại thẻ nào'}

    id = Column("ID", Integer, primary_key=True)

    credit_card_id = Column("CREDIT_CARD_ID", VARCHAR(20), comment='Loại thẻ tham chiếu qua bảng LOS_MA_CREDIT_CARD')

    loan_product_id = Column("LOAN_PRODUCT_ID", VARCHAR(20), comment='Mã sản phẩm')

    display_order = Column("DISPLAY_ORDER", Integer)

    actived_flag = Column("ACTIVED_FLAG", VARCHAR(1))
