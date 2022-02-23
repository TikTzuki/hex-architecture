from sqlalchemy import CHAR, VARCHAR, Column, Float, Integer

from database.base import BaseModel


class FinanceMetadata(BaseModel):
    __tablename__ = 'los_finance_metadata'
    __table_args__ = {'comment': 'Danh sách các dữ liệu metadata'}

    id = Column("ID", Integer, primary_key=True)

    name = Column("NAME", VARCHAR(100))

    is_header = Column("IS_HEADER", CHAR(1))

    is_calculator = Column("IS_CALCULATOR", CHAR(1))

    parent_id = Column("PARENT_ID", Integer, comment='Cấp cha - con')

    calculator = Column("CALCULATOR", VARCHAR(4000), comment='Công thức tính toán metadata')

    metadata_group_id = Column('METADATA_GROUP_ID', Integer)

    edit_flag = Column('EDIT_FLAG', VARCHAR(1), comment='Dữ liệu nhập vô')

    required_flag = Column('REQUIRED_FLAG', VARCHAR(1), comment='Yêu cầu nhập dữ liệu')

    parent_lv2_id = Column("PARENT_LV2_ID", Integer, comment='Cấp cha - con level 2')

    object_id = Column("OBJECT_ID", VARCHAR(5), comment='Đối tượng để tính toán')

    params = Column("PARAMS", VARCHAR(4000), comment='Params để tính toán dữ liệu')

    calculator_type = Column("CALCULATOR_TYPE", VARCHAR(50), comment='Loại công thức tính toán')

    average_cash_flow_type = Column("AVERAGE_CASH_FLOW_TYPE", VARCHAR(30),
                                    comment='Dùng để lấy dữ liệu tính toán thông tin đầu vào, đầu ra hoạt động kdxd')

    display_order_calculator = Column("DISPLAY_ORDER_CALCULATOR", Integer, comment='Thứ tự để tính toán')

    field_type = Column("FIELD_TYPE", VARCHAR(50), comment='Phân biệt field: Tổng tài sản, Nguồn vốn, ...')


class FinanceMetadataGroup(BaseModel):
    __tablename__ = 'los_finance_metadata_group'
    __table_args__ = {'comment': 'Nhóm Metadata ghi Các mục doanh thu: \\n+ Bảng kết quả hoạt động kinh doanh \\n+ Bảng cân đối tài sản nguồn vốn\\n+ Bảng xây dựng HMCTD bổ sung vốn lưu động'}

    id = Column("ID", Integer, primary_key=True)

    name = Column("NAME", VARCHAR(100))

    description = Column("DESCRIPTION", VARCHAR(500))

    display_order = Column("DISPLAY_ORDER", Integer)


class FinanceMetadataItem(BaseModel):
    __tablename__ = 'los_finance_metadata_item'
    __table_args__ = {'comment': 'Dữ liệu Metadata theo từng report, Chi tiết của một row detail.'}

    id = Column("ID", Integer, primary_key=True)

    finance_timeline_assign_id = Column('FINANCE_TIMELINE_ASSIGN_ID', VARCHAR(20))

    business_finance_report_id = Column('BUSINESS_FINANCE_REPORT_ID', Integer)

    metadata_id = Column('METADATA_ID', Integer)

    value = Column("VALUE", Float)
