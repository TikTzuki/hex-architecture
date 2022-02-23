from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class MaBusinessLine(BaseModel):
    __tablename__ = 'los_ma_business_line'
    __table_args__ = {'comment': 'Bảng liên quan tới các nhóm ngành kinh doanh chính, sử dụng cho hộ kinh doanh. '}

    id = Column(CHAR(10), primary_key=True)
    business_name = Column(VARCHAR(255), comment='Nhóm ngành nghề kinh doanh')
    business_code = Column(VARCHAR(10), comment='Mã nhóm ngành nghề liên quan')
