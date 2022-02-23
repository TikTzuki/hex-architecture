from sqlalchemy import CHAR, VARCHAR, Column, DateTime, Integer

from database.base import BaseModel


class PersonBusiness(BaseModel):
    __tablename__ = 'los_person_business'

    id = Column("ID", Integer, primary_key=True)

    person_id = Column('PERSON_ID', Integer)

    business_name = Column("BUSINESS_NAME", VARCHAR(100), comment='Tên hộ kinh doanh, doanh nghiệp')

    business_line_id = Column("BUSINESS_LINE_ID", VARCHAR(50), comment='Mã - Ngành nghề kinh doanh hoạt động chính')

    requirement_business = Column("REQUIREMENT_BUSINESS", CHAR(1),
                                  comment='Doanh nghiệp hoạt động có cần phải có điều kiện kinh doanh không')

    business_category_fcc = Column("BUSINESS_CATEGORY_FCC", VARCHAR(20),
                                   comment='Ngành nghê kinh doanh chính trong giấy phép đăng ký')

    business_license_number = Column("BUSINESS_LICENSE_NUMBER", VARCHAR(20),
                                     comment='Số giấy phép, hoạt động kinh doanh.')

    display_order = Column("DISPLAY_ORDER", Integer)

    license_type = Column("LICENSE_TYPE", VARCHAR(10))

    issue_date = Column("ISSUE_DATE", DateTime, comment='Ngày Cấp')

    place_of_issued = Column("PLACE_OF_ISSUED", VARCHAR(100), comment='Nơi cấp')

    year_of_operator = Column('YEAR_OF_OPERATOR', Integer)
