from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import Base


class Country(Base):
    __tablename__ = 'los_sttm_country'

    country_code = Column(VARCHAR(3), primary_key=True)
    description = Column(VARCHAR(105), comment='Tên tiếng Anh')
    name = Column(VARCHAR(105), comment='Tên tiếng Việt')
