from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class CreditCollateral(BaseModel):
    __tablename__ = 'los_credit_collateral'
    __table_args__ = {'comment': 'Nhóm nợ có tài sản đảm bảo'}

    id = Column(Integer, primary_key=True)
    personal_cir_id = Column(ForeignKey('los_per_credit_insti_rel.id'))
    name = Column(VARCHAR(100), comment='Tên tài sản bảo đảm: Tài sản số 1, tài sản số 2')
    collateral_type = Column(VARCHAR(20), comment='Loại tài sản bảo đảm')
    collateral_value = Column(Float, comment='Giá trị bảo đảm của tài sản')
    actived_flag = Column(CHAR(1))

    personal_cir = relationship('LosPerCreditInstiRel')
