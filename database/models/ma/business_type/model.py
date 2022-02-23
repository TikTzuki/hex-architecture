from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import Base


class MaBusinessType(Base):
    __tablename__ = 'los_ma_business_type'
    __table_args__ = {'comment': 'Loại hình doanh nghiệp. công ty'}

    id = Column("ID", VARCHAR(20), primary_key=True)

    name = Column("NAME", VARCHAR(100))

    sh = Column("SH", VARCHAR(1))
