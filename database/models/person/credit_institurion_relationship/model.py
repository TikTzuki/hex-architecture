from sqlalchemy import (
    CHAR, VARCHAR, Column, DateTime, Float, ForeignKey, Integer
)
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonCreditInstitutionRelationship(BaseModel):
    __tablename__ = 'los_per_credit_insti_rel'
    __table_args__ = {'comment': 'Mối quan hệ của khách hàng với các tổ chức tín dụng - ghi nhạn theo CIC'}

    id = Column(Integer, primary_key=True)
    personal_identity_id = Column(ForeignKey('los_person_identity.id'), comment='CIC theo từng CCCD, CMND, HSVV')
    credit_institution_id = Column(ForeignKey('los_credit_institution.id'), comment='Tổ chức tín dụng liên đới')
    los_id = Column(CHAR(20), comment='Mã hồ sơ vay vốn,')
    loan_amount = Column(Float, comment='Tổng số tiền nợ')
    collateral_amount = Column(Float, comment='Tổng giá trị tài sản đảm bảo')
    debt_classification = Column(VARCHAR(20), comment='Nhóm nợ cao nhất')
    search_date = Column(DateTime, comment='Ngày tra cứu')
    total_cir = Column(Integer, comment='Tổng số khoản nợ trong một tổ chức')

    credit_institution = relationship('LosCreditInstitution')
    personal_identity = relationship('LosPersonIdentity')
