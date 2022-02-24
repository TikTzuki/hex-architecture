from sqlalchemy import (
    CHAR, VARCHAR, Column, DateTime, Float, ForeignKey, Integer
)
from sqlalchemy.orm import relationship

from database.base import BaseModel


class SourceIncomeSalary(BaseModel):
    __tablename__ = 'los_source_income_salary'
    __table_args__ = {'comment': 'Nguồn thu nhập từ lương'}

    id = Column(Integer, primary_key=True)
    person_group_income_id = Column(ForeignKey('los_person_group_income.id'))
    business_type = Column(VARCHAR(75), comment='Loại hình công ty:\\n- Công ty TNHH \\n- Công ty TNHH MTV')
    business_name = Column(VARCHAR(100))
    business_fullname = Column(VARCHAR(200))
    business_group = Column(VARCHAR(75), comment='Nhà nước, Tư nhân, Nước ngoài')
    business_field = Column(VARCHAR(75), comment='Nhóm ngành chính trong công ty , lãnh vực chuyên môn chính')
    work_experience = Column(Integer, comment='Số năm Kinh nghiệm làm việc')
    start_working = Column(DateTime)
    contract_type = Column(VARCHAR(75), comment='Loại hợp đồng')
    frequency_type = Column(VARCHAR(75), comment='Tần suất thu nhập (tham chiếu trong bảng udtm )')
    salary = Column(Float, comment='Số tiền lương')
    income = Column(Float, comment='Tổng số tiền thực lĩnh = số tiền thực lãnh * tần suất (frequency type id)')
    method_payment = Column(CHAR(10), comment='Hình thức trả lương, chuỷen khoản, tiền mặt..... (tham chiếu trong bảng udtm )')
    display_order = Column(Integer)
    income_ratio = Column(Float)
    start_date = Column(DateTime, comment='Thời gian bắt đầu')
    end_date = Column(DateTime, comment='Thời gian kết thúc')
    remaining_time = Column(Integer, comment='Thời gian còn lại của hồ sơ')
    work_schedule = Column(VARCHAR(100), comment='Tình trạng công việc: Fulltime - partime tham chiếu UDTM')
    address = Column(VARCHAR(100), comment='Địa chỉ')
    province_id = Column(VARCHAR(6))
    district_id = Column(VARCHAR(6))
    ward_id = Column(VARCHAR(6))
    tax = Column(VARCHAR(20), comment='Mã số thuế')
    phone = Column(VARCHAR(20), comment='Số điện thoại')
    position = Column(VARCHAR(100), comment='Chức vụ')

    person_group_income = relationship('LosPersonGroupIncome')
