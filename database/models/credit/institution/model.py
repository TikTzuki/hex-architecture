from sqlalchemy import CHAR, VARCHAR, Column, Float, Integer
from sqlalchemy.dialects.oracle import VARCHAR2

from database.models.utils import BaseModel


class CreditInstitution(BaseModel):
    __tablename__ = 'los_credit_institution'
    __table_args__ = {'comment': 'Nhóm nợ có tài sản đảm bảo'}

    id = Column("ID", Integer, primary_key=True)

    name = Column("NAME", VARCHAR(100))

    code = Column("CODE", VARCHAR(9))

    institution_group = Column("INSTITUTION_GROUP", VARCHAR(20), comment='Nhóm TCTD')

    avatar = Column("AVATAR", VARCHAR(100))

    short_name = Column("SHORT_NAME", VARCHAR(50))

    other_value_flag = Column("OTHER_VALUE_FLAG", VARCHAR2(1), comment='Cờ kiểm tra có giá trị "khác"')


class CreditInstitutionLoan(BaseModel):
    __tablename__ = 'los_credit_institution_loan'
    __table_args__ = {'comment': 'Khai báo khoản vay thông thường trong một tổ chức'}
    id = Column("ID", Integer, primary_key=True)

    personal_cir_id = Column('PERSONAL_CIR_ID', Integer)

    property_credit = Column("PROPERTY_CREDIT", VARCHAR(20),
                             comment='Phương thức cấp tín dụng: Ngắn hạn, Trung hạn, Dài hạn')

    credit_term = Column("CREDIT_TERM", Integer, comment='Thời hạn cấp tín dụng')

    credit_limit = Column("CREDIT_LIMIT", Float, comment='Giới hạn tín dụng')

    debt = Column("DEBT", Float, comment='Số dư nợ')

    debt_classification = Column("DEBT_CLASSIFICATION", VARCHAR2(20), comment='Nhóm nợ')

    actived_flag = Column("ACTIVED_FLAG", CHAR(1), comment='Tình trạng của khoản nợ.')
