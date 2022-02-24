from sqlalchemy import CHAR, VARCHAR, Column, Float, ForeignKey, Integer
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class FinanceMetadata(BaseModel):
    __tablename__ = 'los_finance_metadata'
    __table_args__ = {'comment': 'Danh sách các dữ liệu metadata'}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100))
    is_header = Column(CHAR(1))
    is_calculator = Column(CHAR(1))
    parent_id = Column(Integer, comment='Cấp cha - con')
    calculator = Column(VARCHAR(4000), comment='Công thức tính toán metadata')
    metadata_group_id = Column(ForeignKey('los_finance_metadata_group.id'), comment='Nhóm vào trong một group cụ thể')

    edit_flag = Column(VARCHAR(1), comment='Dữ liệu nhập vô')
    required_flag = Column(VARCHAR(1), comment='Yêu cầu nhập dữ liệu')
    parent_lv2_id = Column(NUMBER(asdecimal=False), comment='Cấp cha con level 2')
    object_id = Column(VARCHAR(5), comment='Đối tượng để tính toán')
    params = Column(VARCHAR(4000), comment='Params để tính toán dữ liệu')
    calculator_type = Column(VARCHAR(50), comment='Loại công thức tính toán')
    average_cash_flow_type = Column(VARCHAR(30), comment='Dùng để lấy dữ liệu tính toán thông tin đầu vào, đầu ra hoạt động kdxd')
    display_order_calculator = Column(Integer, comment='Thứ tự để tính toán')
    field_type = Column(VARCHAR(50), comment='Phân biệt field: Tổng tài sản, Nguồn vốn, ...')

    metadata_group = relationship('FinanceMetadataGroup')


class FinanceMetadataGroup(BaseModel):
    __tablename__ = 'los_finance_metadata_group'
    __table_args__ = {'comment': 'Nhóm Metadata ghi Các mục doanh thu: \\n+ Bảng kết quả hoạt động kinh doanh \\n+ Bảng cân đối tài sản nguồn vốn\\n+ Bảng xây dựng HMCTD bổ sung vốn lưu động'}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100))
    description = Column(VARCHAR(500))
    display_order = Column(Integer)


class FinanceMetadataItem(BaseModel):
    __tablename__ = 'los_finance_metadata_item'
    __table_args__ = {'comment': 'Dữ liệu Metadata theo từng report, Chi tiết của một row detail.'}

    id = Column(Integer, primary_key=True)
    business_finance_report_id = Column(ForeignKey('los_person_business_finance_report.id'))
    metadata_id = Column(Integer)
    value = Column(Float)

    finance_timeline_assign_id = Column(VARCHAR(20))

    business_finance_report = relationship('PersonBusinessFinanceReport')
