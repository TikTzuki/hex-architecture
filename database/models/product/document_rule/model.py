from sqlalchemy import VARCHAR, Column, Integer

from database.base import BaseModel


class ProductDocumentRule(BaseModel):
    __tablename__ = 'los_product_document_rule'
    __table_args__ = {'comment': 'Danh sách các hồ sơ pháp lý phải có theo quy định của sản phẩm.'}

    id = Column("ID", Integer, primary_key=True)

    product_loan_id = Column('PRODUCT_LOAN_ID', Integer, comment='Mã sản phẩm vay vốn')

    document_group_type = Column('DOCUMENT_GROUP_TYPE', VARCHAR(75),
                                 comment='Nhóm tài liệu cần phải có (tham chiếu trong bảng udtm )')

    document_type_id = Column('DOCUMENT_TYPE_ID', Integer,
                              comment='Chỉ định tài liệu cụ thể phải có trong hồ sơ, cho phép null, nếu giá trị là null thì chỉ cần có 1 tài liệu trong nhóm là được')  # noqa

    required_flag = Column('REQUIRED_FLAG', VARCHAR(2), comment='Chỉ định bắt buộc phải có hoặc không')

    actived_flag = Column('ACTIVED_FLAG', VARCHAR(2), comment='Kích hoạt hay không')

    ext_1 = Column('EXT_1', VARCHAR(100), comment='Dự trữ')

    ext_2 = Column('EXT_2', VARCHAR(100), comment='Dữ trữ field')
