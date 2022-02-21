from sqlalchemy import VARCHAR, Column

from app.third_party.oracle.models.utils import Base


class MaBusinessType(Base):
    __tablename__ = 'los_ma_business_type'
    __table_args__ = {'comment': 'Loại hình doanh nghiệp. công ty'}

    id = Column("ID", VARCHAR(20), primary_key=True)

    name = Column("NAME", VARCHAR(100))

    sh = Column("SH", VARCHAR(1))
