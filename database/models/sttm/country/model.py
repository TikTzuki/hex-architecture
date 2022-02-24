from sqlalchemy import VARCHAR, Column

from database import Base


class Country(Base):
    __tablename__ = 'los_sttm_country'

    country_code = Column(VARCHAR(3), primary_key=True)
    description = Column(VARCHAR(105), comment='Tên tiếng Anh')
    name = Column(VARCHAR(105), comment='Tên tiếng Việt')
