from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import Base


class DetmClgBrnCode(Base):
    __tablename__ = 'ud_los_detm_clg_brn_code'

    branch_code = Column(VARCHAR(9), primary_key=True, nullable=False)
    branch_desc = Column(VARCHAR(35))
    sector_code = Column(VARCHAR(9), primary_key=True, nullable=False)
