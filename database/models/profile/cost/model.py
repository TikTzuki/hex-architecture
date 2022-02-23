from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class ProfileCost(BaseModel):
    __tablename__ = 'los_profile_cost'
    __table_args__ = {'comment': 'Danh sách các chi phí và giá tiền phải nhập'}

    id = Column(Integer, primary_key=True)
    los_sequence_id = Column(Integer)
    cost_type = Column(VARCHAR(75), comment='Loại chi phí:\\n- Sinh hoạt gia đình\\n- Chi phí trả cho các khoản vay khác (cả gốc + lãi)\\n- Chi phí khác')
    value = Column(Float, comment='Giá trị tiền phai chịu cho chi phí đó')
