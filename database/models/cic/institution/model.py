from sqlalchemy import CHAR, VARCHAR, Column, Float, ForeignKey, Integer, text
from sqlalchemy.orm import relationship

from database.base import BaseModel


class CreditInstitution(BaseModel):
    __tablename__ = 'los_credit_institution'
    __table_args__ = {'comment': 'Danh sách các tổ chức tín dụng'}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100))
    code = Column(VARCHAR(9))
    institution_group = Column(VARCHAR(20), comment='Nhóm TCTD như ngân hàng, tổ chức tài chính')
    avatar = Column(VARCHAR(100))

    short_name = Column(VARCHAR(50), comment='Tên viết tắt của một số ngân hàng ví dụ ACB, Agribank, MB')
    other_value_flag = Column(VARCHAR(1), server_default=text("'N'"))


class CreditInstitutionLoan(BaseModel):
    __tablename__ = 'los_credit_institution_loan'
    __table_args__ = {'comment': 'Khai báo khoản vay thông thường trong một tổ chức'}

    id = Column(Integer, primary_key=True)
    personal_cir_id = Column(ForeignKey('los_per_credit_insti_rel.id'))
    property_credit = Column(VARCHAR(20), comment='Phương thức cấp tín dụng: Ngắn hạn, Trung hạn, Dài hạn')
    credit_term = Column(Integer, comment='Thời hạn cấp tín dụng')
    debt = Column(Float, comment='Số dư nợ')
    debt_classification = Column(VARCHAR(20), comment='Nhóm nợ')
    actived_flag = Column(CHAR(1), comment='Tình trạng của khoản nợ.')
    credit_limit = Column(Float)

    personal_cir = relationship('PersonCreditInstitutionRelationship')
