from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.oracle import VARCHAR2

from database.base import BaseModel


class Partner(BaseModel):
    __tablename__ = 'los_partner'
    __table_args__ = {'comment': 'Danh sách các đối tác'}

    id = Column("ID", VARCHAR2(10), primary_key=True)

    name = Column("NAME", VARCHAR2(100))

    tax = Column("TAX", VARCHAR2(20))

    phone = Column("PHONE", VARCHAR2(30))

    address = Column("ADDRESS", VARCHAR2(50))

    ward_id = Column("WARD_ID", VARCHAR2(20))

    district_id = Column("DISTRICT_ID", VARCHAR2(10))

    province_id = Column("PROVINCE_ID", VARCHAR2(20))

    email = Column("EMAIL", VARCHAR2(50))

    website = Column("WEBSITE", VARCHAR2(100))


class PartnerProduct(BaseModel):
    __tablename__ = 'los_partner_product'
    __table_args__ = {'comment': 'Danh sách các sản phẩm của riêng đối tác.'}

    id = Column("ID", Integer, primary_key=True)

    partner_id = Column("PARTNER_ID", VARCHAR2(20), comment='Mã đối tác')

    name = Column("NAME", VARCHAR2(100), comment='Tên sản phẩm của đố tác')

    actived_flag = Column("ACTIVED_FLAG", CHAR(1))

    display_order = Column("DISPLAY_ORDER", Integer, comment='Thứ tự hiển thị sản phẩm')


class PartnerLoanProduct(BaseModel):
    __tablename__ = 'los_partner_loan_product'
    __table_args__ = {'comment': 'Bảng liên kết của các sản phẩm vay (của SCB) cho các Đối tác'}

    id = Column("ID", Integer, primary_key=True)

    partner_id = Column("PARTNER_ID", VARCHAR2(20), comment='Mã đối tác')

    loan_product_id = Column("LOAN_PRODUCT_ID", VARCHAR2(100), comment='Mã sản phẩm vay của SCB')

    actived_flag = Column("ACTIVED_FLAG", CHAR(1))

    display_order = Column("DISPLAY_ORDER", Integer, comment='Thứ tự xuất hiện, hay thứ tự ưu tiên.')
