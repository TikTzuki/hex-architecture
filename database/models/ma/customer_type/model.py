from sqlalchemy import Column
from sqlalchemy.dialects.oracle import VARCHAR2

from app.third_party.oracle.models.utils import Base


class MaCustomerType(Base):
    __tablename__ = 'los_ma_customer_type'
    __table_args__ = {'comment': 'Danh mục khách hàng'}

    id = Column("ID", VARCHAR2(10), primary_key=True)

    name = Column("NAME", VARCHAR2(50), comment='Tên nhóm khách hàng , cá nhân hay doanh nghiệp')
