from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import Base


class MaPersonalRep(Base):
    __tablename__ = 'los_ma_personal_rep'
    __table_args__ = {'comment': 'Personal representative Danh mục người đại điện như người vay hôn phối....'}

    id = Column(VARCHAR(20), primary_key=True)
    name = Column(VARCHAR(100))
    description = Column(VARCHAR(100))
    created_at = Column(DateTime)
    created_by = Column(VARCHAR(20))
    modified_at = Column(DateTime)
    modified_by = Column(VARCHAR(20))
    is_default = Column(VARCHAR(1), server_default=text("'N'"))
    display_order = Column(Integer)
    loan_category_id = Column(VARCHAR(20), nullable=False)
    actived_flag = Column(VARCHAR(1))
