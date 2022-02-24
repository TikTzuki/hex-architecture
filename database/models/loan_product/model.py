from sqlalchemy import CHAR, VARCHAR, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class LoanProduct(BaseModel):
    __tablename__ = 'los_loan_product'
    __table_args__ = {'comment': 'Sản phẩm vốn vay'}

    id = Column(VARCHAR(10), primary_key=True, comment='  ')
    name = Column(VARCHAR(200))
    description = Column(VARCHAR(200))
    fcc_core_loan_id = Column(CHAR(5), comment='Mã sản phẩm vay trên CoreFCC')
    product_loan_group_id = Column(VARCHAR(20), comment='Nhóm sản phẩm vay (Vay thông thường, vay thẻ)')
    parent_id = Column(VARCHAR(20), comment='Câp cha con theo sản phẩm')
    has_collateral = Column(CHAR(1), comment='Ghi nhận là nếu vay theo gói này thì phải có tài sản bảo đảm')
    display_order = Column(Integer, comment='Thứ tự sắp xếp ')
    financial_analysis_flag = Column(VARCHAR(1), comment='Cờ phân biệt có tính phân tích tài chính (Thông tin khoản vay) hay không ?')


class LoanProductPolicy(BaseModel):
    __tablename__ = 'los_loan_product_policy'
    __table_args__ = {'comment': 'Maaping giữa các sản phẩm vay và hồ sơ ngoại lệ. Chỉ cần tạo 1 bộ hồ sơ các sản phẩm khác sẽ dùng theo'}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100))
    description = Column(VARCHAR(200))
    policy_detail_id = Column(Integer, comment='Tham chiếu trực tiếp vào bảng LOS_POLICY_DETAIL')
    loan_product_id = Column(ForeignKey('los_loan_product.id'))

    loan_product = relationship('LosLoanProduct')
