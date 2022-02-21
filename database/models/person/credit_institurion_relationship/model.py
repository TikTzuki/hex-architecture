from sqlalchemy import CHAR, Column, DateTime, Integer, Float
from sqlalchemy.dialects.oracle import VARCHAR2

from database.models.utils import BaseModel


class PersonCreditInstitutionRelationship(BaseModel):
    __tablename__ = 'los_per_credit_insti_rel'

    id = Column("ID", Integer, primary_key=True)

    personal_identity_id = Column('PERSONAL_IDENTITY_ID', Integer)

    credit_institution_id = Column('CREDIT_INSTITUTION_ID', Integer,
                                   comment='Mối quan hệ của khách hàng với các tổ chức tín dụng - ghi nhạn theo CIC')

    los_id = Column('LOS_ID', CHAR(20))

    loan_amount = Column("LOAN_AMOUNT", Float, comment='Tổng số tiền nợ')

    collateral_amount = Column("COLLATERAL_AMOUNT", Float, comment='Tổng giá trị tài sản đảm bảo')

    debt_classification = Column("DEBT_CLASSIFICATION", VARCHAR2(20), comment='Nhóm nợ cao nhất')

    search_date = Column("SEARCH_DATE", DateTime, comment='Ngày tra cứu')

    total_cir = Column("TOTAL_CIR", Integer, comment='Tổng số khoản nợ trong một tổ chức')
