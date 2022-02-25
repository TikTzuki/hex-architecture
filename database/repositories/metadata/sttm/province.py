from sqlalchemy import (
    CHAR, VARCHAR, CheckConstraint, Column, DateTime, Float, Text
)
from sqlalchemy.dialects.oracle import NUMBER

from database import Base


class Province(Base):
    __tablename__ = 'los_sttm_province'
    __table_args__ = (
        CheckConstraint('GEOJSON IS JSON'),
    )

    province_code = Column(VARCHAR(6), primary_key=True)
    description = Column(VARCHAR(105))
    loc_code = Column(VARCHAR(3))
    record_stat = Column(CHAR(1))
    auth_stat = Column(CHAR(1))
    once_auth = Column(CHAR(1))
    mod_no = Column(NUMBER(4, 0, False))
    maker_id = Column(VARCHAR(12))
    maker_dt_stamp = Column(DateTime)
    checker_id = Column(VARCHAR(12))
    checker_dt_stamp = Column(DateTime)
    geojson = Column(Text)
    geom_area = Column(Float)
