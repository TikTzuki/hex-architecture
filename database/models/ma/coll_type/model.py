from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import Base


class MaCollType(Base):
    __tablename__ = 'los_ma_coll_type'
    __table_args__ = {'comment': 'Danh mục tài sản bảo đảm'}

    id = Column(VARCHAR(10), primary_key=True)
    name = Column(VARCHAR(100))
    parent_id = Column(VARCHAR(10))
    lev = Column(Integer, comment='Thứ tự sắp cha con dùng nhanh khi search')
    display_order = Column(Integer, comment='Thứ tự hiển thị')


class LosMaCollTransType(Base):
    __tablename__ = 'los_ma_coll_trans_type'
    __table_args__ = {"comment": 'Danh sách các phương tiện phận tải chi tiết dùng cho mục định giá'}

    trans_type_id = Column('TRANS_TYPE_ID', VARCHAR(100), comment='Loại hình phương tiện vận tải tham chiếu vào bảng MA_COLL_TYPE')
    trans_name = Column('TRANS_NAME', VARCHAR(100), comment='Chi tiết tên loại hình con', primary_key=True)
    other_value_flag = Column('OTHER_VALUE_FLAG', VARCHAR(1), comment='Giá trị khác, khi chọn vào thì chuyển qua nhập tay')
