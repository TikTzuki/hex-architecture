from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.oracle import NUMBER

from database import Base


class CytmCcyDefnMaster(Base):
    __tablename__ = 'los_cytm_ccy_defn_master'

    ccy_code = Column(VARCHAR(3), primary_key=True)
    ccy_name = Column(VARCHAR(105))
    ccy_decimals = Column(NUMBER(1, 0, False))
    ccy_round_rule = Column(CHAR(1))
    ccy_round_unit = Column(NUMBER(7, 3, True))
