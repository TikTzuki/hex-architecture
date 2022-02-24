from sqlalchemy import VARCHAR, Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class CreditCard(BaseModel):
    __tablename__ = 'los_credit_card'
    __table_args__ = {'comment': 'Nhóm thẻ nợ tín dụng'}

    id = Column(Integer, primary_key=True)
    personal_cir_id = Column(ForeignKey('los_per_credit_insti_rel.id'))
    credit_name = Column(VARCHAR(50), comment='Tên loại thẻ tin dụng')
    credit_limit = Column(Float, comment='Dư nợ tối đa')
    due_date = Column(DateTime, comment='Thời hạn của thẻ tín dụng')
    debt = Column(Float, comment='Dư nợ thẻ')

    personal_cir = relationship('LosPerCreditInstiRel')
