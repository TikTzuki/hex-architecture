from sqlalchemy import VARCHAR, Column, Integer

from app.third_party.oracle.models.utils import Base


class MaCardPromotion(Base):
    __tablename__ = 'los_ma_card_promotion'
    __table_args__ = {'comment': 'Danh sách các khuyến mại cho thẻ'}

    id = Column("ID", Integer, primary_key=True)

    name = Column("NAME", VARCHAR(100), comment='Thông tin - tiêu đề, vali, miễn phí phí thường niên năm đầu')

    description = Column("DESCRIPTION", VARCHAR(200))
