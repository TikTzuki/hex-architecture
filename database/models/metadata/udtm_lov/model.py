from sqlalchemy import VARCHAR, Column, Integer, text

from database import Base


class UdtmLov(Base):
    __tablename__ = 'los_udtm_lov'

    field_name = Column(VARCHAR(105), primary_key=True, nullable=False)
    lov = Column(VARCHAR(75), primary_key=True, nullable=False)
    lov_desc = Column(VARCHAR(400))
    is_default_value = Column(VARCHAR(1), server_default=text("'N'"))
    display_order = Column(Integer)
    actived_flag = Column(VARCHAR(1))
    lov_value = Column(VARCHAR(100))
    other_value_flag = Column(VARCHAR(1), server_default=text("'N'"))
