from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import Base


class RegionalOffice(Base):
    __tablename__ = 'los_sttm_regional_office'
    __table_args__ = {'comment': 'Danh sách khu vực của địa chỉ ngân hàng SCB'}

    regional_code = Column(VARCHAR(10), primary_key=True, comment='Mã vùng')
    regional_name = Column(VARCHAR(100), comment='Tên vùng')
