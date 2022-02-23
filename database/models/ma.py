from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.oracle import NUMBER

from database import Base


class CountryManufacture(Base):
    __tablename__ = 'los_ma_coll_coun_manu'
    __table_args__ = {'comment': 'Nơi sản xuất'}

    country_code = Column(VARCHAR(3), primary_key=True)
    name = Column(VARCHAR(105), comment="Tên tiếng Việt")
    other_value_flag = Column(VARCHAR(1), comment='Giá trị khác, khi chọn vào thì chuyển qua nhập tay', server_default=text("""'N'"""))
    display_order = Column(Integer, comment='Số thứ tự hiển thị')
