from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import Base


class MaCostType(Base):
    __tablename__ = 'los_ma_cost_type'
    __table_args__ = {'comment': 'Loại chi phí'}

    id = Column(VARCHAR(30), primary_key=True)
    name = Column(VARCHAR(100))
    is_loan_required = Column(VARCHAR(1), comment='Nếu dùng cho vay thường thì đánh dấu Y')
    is_credit_required = Column(VARCHAR(1), comment='Nếu dùng cho vay thẻ thì đánh dấu Y')
    display_order = Column(Integer, comment='Thứ tự hiển thị (mặc định dùng cho vay thẻ) ')

