from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import Base


class MaBankCode(Base):
    __tablename__ = 'ud_los_ma_bank_code'

    bank_code = Column("BANK_CODE", VARCHAR(10), primary_key=True)
    bank_name = Column("BANK_NAME", VARCHAR(100))
    bank_status = Column("BANK_STATUS", VARCHAR(1))
    bank_desc = Column("BANK_DESC", VARCHAR(100))
    bank_out = Column("BANK_OUT", VARCHAR(1))
    bank_quick = Column("BANK_QUICK", VARCHAR(1))
