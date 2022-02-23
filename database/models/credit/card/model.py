from sqlalchemy import VARCHAR, Column, DateTime, Float, Integer

from database.base import BaseModel


class CreditCard(BaseModel):
    __tablename__ = 'los_credit_card'
    __table_args__ = {'comment': 'Nhóm thẻ nợ tín dụng'}

    id = Column("ID", Integer, primary_key=True)

    personal_cir_id = Column('PERSONAL_CIR_ID', Integer)

    credit_name = Column("CREDIT_NAME", VARCHAR(50), comment='Tên loại thẻ tin dụng')

    credit_limit = Column("CREDIT_LIMIT", Float, comment='Dư nợ tối đa')

    due_date = Column("DUE_DATE", DateTime, comment='Thời hạn của thẻ tín dụng')

    debt = Column("DEBT", Float, comment='Dư nợ thẻ')
