from sqlalchemy import CHAR, VARCHAR, Column, DateTime, Float, Integer

from database.base import BaseModel


class SourceIncomeSalary(BaseModel):
    __tablename__ = 'los_source_income_salary'
    __table_args__ = {'comment': 'Nguồn thu nhập từ lương'}

    id = Column("ID", Integer, primary_key=True)

    person_group_income_id = Column('PERSON_GROUP_INCOME_ID', Integer)

    business_type = Column("BUSINESS_TYPE", VARCHAR(75),
                           comment='Loại hình công ty:\\n- Công ty TNHH \\n- Công ty TNHH MTV')

    business_name = Column("BUSINESS_NAME", VARCHAR(100))

    business_fullname = Column("BUSINESS_FULLNAME", VARCHAR(200))

    business_group = Column("BUSINESS_GROUP", VARCHAR(75), comment='Nhà nước, Tư nhân, Nước ngoài')

    business_field = Column("BUSINESS_FIELD", VARCHAR(75),
                            comment='Nhóm ngành chính trong công ty , lãnh vực chuyên môn chính')

    work_experience = Column("WORK_EXPERIENCE", Integer, comment='Số năm Kinh nghiệm làm việc')

    start_working = Column("START_WORKING", DateTime)

    contract_type = Column("CONTRACT_TYPE", VARCHAR(75), comment='Loại hợp đồng')

    frequency_type = Column("FREQUENCY_TYPE", VARCHAR(75), comment='Tần suất thu nhập (tham chiếu trong bảng udtm )')

    salary = Column("SALARY", Float, comment='Số tiền lương')

    income = Column("INCOME", Float,
                    comment='Tổng số tiền thực lĩnh = số tiền thực lãnh * tần suất (frequency type id)')

    method_payment = Column("METHOD_PAYMENT", CHAR(10),
                            comment='Hình thức trả lương, chuỷen khoản, tiền mặt..... (tham chiếu trong bảng udtm )')

    display_order = Column("DISPLAY_ORDER", Integer)

    income_ratio = Column("INCOME_RATIO", Float)

    start_date = Column("START_DATE", DateTime, comment='Thời gian bắt đầu')

    end_date = Column("END_DATE", DateTime, comment='Thời gian kết thúc')

    remaining_time = Column("REMAINING_TIME", Integer, comment='Thời gian còn lại của hồ sơ')

    work_schedule = Column("WORK_SCHEDULE", VARCHAR(100),
                           comment='Tình trạng công việc: Fulltime - partime tham chiếu UDTM')

    address = Column("ADDRESS", VARCHAR(100), comment='Địa chỉ')

    province_id = Column('PROVINCE_ID', VARCHAR(6))

    district_id = Column('DISTRICT_ID', VARCHAR(6))

    ward_id = Column('WARD_ID', VARCHAR(6))

    tax = Column("TAX", VARCHAR(20), comment='Mã số thuế')

    phone = Column("PHONE", VARCHAR(20), comment='Số điện thoại')

    position = Column("POSITION", VARCHAR(100), comment='Chức vụ')
