from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class PersonBusiness(BaseModel):
    __tablename__ = 'los_person_business'

    id = Column(Integer, primary_key=True)
    person_id = Column(ForeignKey('los_person.id'))
    business_name = Column(VARCHAR(100), comment='Tên hộ kinh doanh, doanh nghiệp')
    business_line_id = Column(VARCHAR(50), comment='Mã - Ngành nghề kinh doanh hoạt động chính')
    requirement_business = Column(CHAR(1), comment='Doanh nghiệp hoạt động có cần phải có điều kiện kinh doanh không')
    business_category_fcc = Column(VARCHAR(20), comment='Ngành nghê kinh doanh chính trong giấy phép đăng ký')
    business_license_number = Column(VARCHAR(20), comment='Số giấy phép, hoạt động kinh doanh.')
    display_order = Column(Integer)
    license_type = Column(VARCHAR(10))
    issue_date = Column(DateTime, comment='Ngày Cấp')
    place_of_issued = Column(VARCHAR(100))
    year_of_operator = Column(Integer)

    person = relationship('LosPerson')
