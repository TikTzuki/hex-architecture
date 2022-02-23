from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonBusinessFinanceReport(BaseModel):
    __tablename__ = 'los_person_business_finance_report'
    __table_args__ = {
        'comment': 'Mỗi Doanh nghiệp (Hộ kinh doanh) của KH có thể có nhiều bản báo cáo Tình hình kinh doanh'}

    id = Column(Integer, primary_key=True)
    person_business_id = Column(ForeignKey('los_person_business.id'), comment='Mã hộ kinh doanh của khách hàng')
    description = Column(VARCHAR(100))
    approval_date = Column(DateTime)
    creditworthiness = Column(VARCHAR(100), comment='Phân tích khả năng trả nợ gốc')
    cashflow_note = Column(VARCHAR(600), comment='Nhận xét chung về đầu vào đầu ra')
    proposal = Column(VARCHAR(200), comment='Đề xuất khác')
    able_loan_principal = Column(VARCHAR(100), comment='Phân tích/Nhận xét về  khả năng trả nợ gốc')
    actived_flag = Column(CHAR(1))
    summary = Column(VARCHAR(500), comment='Nhận xét')
    able_pay_type = Column(CHAR(3), comment='Xác nhận đã thẩm định thành công và đủ khả năng về thanh toán chi phí sinh hoạt khác. hoặc khong đủ khả năng thành toán....')
    able_capital_requirement = Column(VARCHAR(100), comment='Đánh giá  về phương án và nhu cầu vay vốn')

    person_business = relationship('LosPersonBusines')
