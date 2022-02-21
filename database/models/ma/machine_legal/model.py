from sqlalchemy import VARCHAR, Column, Integer

from app.third_party.oracle.models.utils import Base


class MaCollMachineLegal(Base):
    __tablename__ = 'los_ma_coll_machine_legal'
    __table_args__ = {'comment': 'Danh mục hồ sơ pháp lý của TSBD là Thiết bị máy móc'}

    id = Column(VARCHAR(20), primary_key=True)
    name = Column(VARCHAR(100))
    parent_id = Column(VARCHAR(100))
    LEVEL = Column(Integer)
    display_order = Column(Integer)
    other_value_flag = Column(VARCHAR(2), comment='Giá trị khác, khi chọn vào thì chuyển qua nhập tay')
