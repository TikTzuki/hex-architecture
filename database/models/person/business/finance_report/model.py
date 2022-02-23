from sqlalchemy import CHAR, VARCHAR, Column, DateTime, Integer

from database.base import BaseModel


class PersonBusinessFinanceReport(BaseModel):
    __tablename__ = 'los_person_business_finance_report'
    __table_args__ = {
        'comment': 'Mỗi Doanh nghiệp (Hộ kinh doanh) của KH có thể có nhiều bản báo cáo Tình hình kinh doanh'}

    id = Column("ID", Integer, primary_key=True)

    person_business_id = Column('PERSON_BUSINESS_ID', Integer)

    description = Column("DESCRIPTION", VARCHAR(100))

    approval_date = Column("APPROVAL_DATE", DateTime)

    creditworthiness = Column("CREDITWORTHINESS", VARCHAR(100), comment='Phân tích khả năng trả nợ gốc')

    cashflow_note = Column("CASHFLOW_NOTE", VARCHAR(600), comment='Nhận xét chung về đầu vào đầu ra')

    proposal = Column("PROPOSAL", VARCHAR(200), comment='Đề xuất khác')

    able_loan_principal = Column("ABLE_LOAN_PRINCIPAL", VARCHAR(100),
                                 comment='Phân tích/Nhận xét về  khả năng trả nợ gốc')

    actived_flag = Column("ACTIVED_FLAG", CHAR(1))

    summary = Column("SUMMARY", VARCHAR(500), comment='Nhận xét tổng quan')

    able_pay_type = Column("ABLE_PAY_TYPE", CHAR(3), comment='Xác nhận đã thẩm định thành công và đủ khả năng về thanh toán chi phí sinh hoạt khác. hoặc khong đủ khả năng thành toán....')

    able_capital_requirement = Column("ABLE_CAPITAL_REQUIREMENT", VARCHAR(100),
                                      comment='Đánh giá  về phương án và nhu cầu vay vốn')
