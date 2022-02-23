from sqlalchemy import VARCHAR, Column, Integer

from database import Base


class UdtmLov(Base):
    __tablename__ = 'los_udtm_lov'

    field_name = Column("FIELD_NAME", VARCHAR(105), primary_key=True, nullable=False)

    lov = Column("LOV", VARCHAR(75), primary_key=True)

    lov_desc = Column("LOV_DESC", VARCHAR(400))

    is_default_value = Column("IS_DEFAULT_VALUE", VARCHAR(1), default='N')

    display_order = Column("DISPLAY_ORDER", Integer, comment='Thứ tự xuất hiện')

    actived_flag = Column("ACTIVED_FLAG", VARCHAR(1))

    lov_value = Column("LOV_VALUE", VARCHAR(100))

    other_value_flag = Column("OTHER_VALUE_FLAG", VARCHAR(1), comment='Giá trị khác, khi chọn vào thì chuyển qua nhập tay')
