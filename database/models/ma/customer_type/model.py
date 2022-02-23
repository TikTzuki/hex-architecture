from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.oracle import VARCHAR2

from database import Base


class MaCustomerType(Base):
    __tablename__ = 'los_ma_customer_type'
    __table_args__ = {'comment': 'Danh mục khách hàng'}

    id = Column("ID", VARCHAR2(10), primary_key=True)

    name = Column("NAME", VARCHAR2(50), comment='Tên nhóm khách hàng , cá nhân hay doanh nghiệp')
