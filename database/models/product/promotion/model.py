from sqlalchemy import VARCHAR, Column, Integer

from app.third_party.oracle.models.utils import Base


class ProductPromotion(Base):
    __tablename__ = 'los_product_promotion'
    __table_args__ = {'comment': 'Danh sách các khuyến mai đi theo sản phẩm.'}

    id = Column("ID", Integer, primary_key=True)

    loan_product_id = Column("LOAN_PRODUCT_ID", VARCHAR(20), comment='Mã sản phẩm vay')

    gift_promotion_id = Column("GIFT_PROMOTION_ID", Integer, comment='Mã khuyến mại')

    display_order = Column("DISPLAY_ORDER", Integer, comment='Thứ tự hiển thị')

    status_flag = Column("STATUS_FLAG", VARCHAR(1), comment='Kích hoạt / không kích hoạt', default='Y')
