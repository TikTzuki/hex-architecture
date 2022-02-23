from sqlalchemy import CHAR, VARCHAR, Column, Integer

from database.base import BaseModel


class LoanProduct(BaseModel):
    __tablename__ = 'los_loan_product'
    __table_args__ = {'comment': 'Sản phẩm vốn vay'}

    id = Column("ID", VARCHAR(10), primary_key=True)

    name = Column("NAME", VARCHAR(200))

    description = Column("DESCRIPTION", VARCHAR(200))

    fcc_core_loan_id = Column("FCC_CORE_LOAN_ID", CHAR(5), comment='Mã sản phẩm vay trên CoreFCC')

    product_loan_group_id = Column("PRODUCT_LOAN_GROUP_ID", VARCHAR(20),
                                   comment='Nhóm sản phẩm vay (Vay thông thường, vay thẻ)')

    parent_id = Column("PARENT_ID", VARCHAR(20), comment='Câp cha con theo sản phẩm')

    has_collateral = Column('HAS_COLLATERAL', CHAR(1),
                            comment='Ghi nhận là nếu vay theo gói này thì phải có tài sản bảo đảm')

    display_order = Column("DISPLAY_ORDER", Integer, comment='Thứ tự sắp xếp')

    financial_analysis_flag = Column('FINANCIAL_ANALYSIS_FLAG', VARCHAR(1),
                                     comment='Cờ phân biệt có tính phân tích tài chính (Thông tin khoản vay) hay không ?')


class LoanProductPolicy(BaseModel):
    __tablename__ = 'los_loan_product_policy'
    __table_args__ = {
        'comment': 'Maaping giữa các sản phẩm vay và hồ sơ ngoại lệ. Chỉ cần tạo 1 bộ hồ sơ các sản phẩm khác sẽ dùng theo'}

    id = Column("ID", Integer, primary_key=True)

    name = Column("NAME", VARCHAR(100))

    description = Column("DESCRIPTION", VARCHAR(200))

    policy_detail_id = Column("POLICY_DETAIL_ID", Integer, comment='Tham chiếu trực tiếp vào bảng LOS_POLICY_DETAIL')

    loan_product_id = Column('LOAN_PRODUCT_ID', VARCHAR(20))
