from sqlalchemy import VARCHAR, Column, Integer

from app.third_party.oracle.models.utils import Base


class MaPersonalRep(Base):
    __tablename__ = 'los_ma_personal_rep'
    __table_args__ = {'comment': 'Personal representative Danh mục người đại điện như người vay hôn phối....'}

    id = Column("ID", VARCHAR(20), primary_key=True)

    name = Column("NAME", VARCHAR(100))

    description = Column("DESCRIPTION", VARCHAR(100))

    is_default = Column("IS_DEFAULT", VARCHAR(1), default='N')

    display_order = Column("DISPLAY_ORDER", Integer, comment='Thứ tự xuất hiện')

    loan_category_id = Column("LOAN_CATEGORY_ID", VARCHAR(20))

    actived_flag = Column("ACTIVED_FLAG", VARCHAR(1), default='N')
