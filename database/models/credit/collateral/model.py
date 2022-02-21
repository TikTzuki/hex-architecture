from sqlalchemy import CHAR, VARCHAR, Column, Float, Integer

from database.models.utils import BaseModel


class CreditCollateral(BaseModel):
    __tablename__ = 'los_credit_collateral'
    __table_args__ = {'comment': 'Nhóm nợ có tài sản đảm bảo'}
    id = Column("ID", Integer, primary_key=True)

    personal_cir_id = Column('PERSONAL_CIR_ID', Integer)

    name = Column("NAME", VARCHAR(100), comment='Tên tài sản bảo đảm: Tài sản số 1, tài sản số 2')

    collateral_type = Column('COLLATERAL_TYPE', VARCHAR(20), comment='Loại tài sản bảo đảm')

    collateral_value = Column("COLLATERAL_VALUE", Float, comment='Giá trị bảo đảm của tài sản')

    actived_flag = Column("ACTIVED_FLAG", CHAR(1))
