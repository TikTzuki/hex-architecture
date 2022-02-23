from sqlalchemy import VARCHAR, Column, Integer

from database import Base


class MaCollType(Base):
    __tablename__ = 'los_ma_coll_type'
    __table_args__ = {'comment': 'Danh mục tài sản bảo đảm'}

    id = Column("ID", VARCHAR(20), primary_key=True)

    name = Column("NAME", VARCHAR(100))

    parent_id = Column("PARENT_ID", VARCHAR(10))

    lev = Column('LEV', Integer, comment='Thứ tự sắp cha con dùng nhanh khi search')

    display_order = Column("DISPLAY_ORDER", Integer, comment='Thứ tự hiển thị')

    # other_value_flag = Column("OTHER_VALUE_FLAG", VARCHAR(1), comment='Giá trị khác, khi chọn vào thì chuyển qua nhập tay')


#
# class LosMaCollMachineLegal(Base):
#     __tablename__ = 'los_ma_coll_machine_legal'
#     __table_args__ = {"comment": 'Danh mục hồ sơ pháp lý của TSBD là Thiết bị máy móc'}
#
#     id = Column('id', VARCHAR(20))
#     name = Column('name', VARCHAR(100))
#     parent_id = Column('parent_id', VARCHAR(100))
#     level = Column('LEVEL', VARCHAR(100))
#     display_order = Column('display_order', Integer)
#     other_value_flag = Column('other_value_flag', VARCHAR(2), comment='Giá trị khác, khi chọn vào thì chuyển qua nhập tay')
#
#
class LosMaCollTransType(Base):
    __tablename__ = 'los_ma_coll_trans_type'
    __table_args__ = {"comment": 'Danh sách các phương tiện phận tải chi tiết dùng cho mục định giá'}

    trans_type_id = Column('TRANS_TYPE_ID', VARCHAR(100), comment='Loại hình phương tiện vận tải tham chiếu vào bảng MA_COLL_TYPE')
    trans_name = Column('TRANS_NAME', VARCHAR(100), comment='Chi tiết tên loại hình con', primary_key=True)
    other_value_flag = Column('OTHER_VALUE_FLAG', VARCHAR(1), comment='Giá trị khác, khi chọn vào thì chuyển qua nhập tay')
