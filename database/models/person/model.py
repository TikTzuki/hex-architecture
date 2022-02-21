from sqlalchemy import CHAR, VARCHAR, Column, DateTime, Integer

from database.models.utils import BaseModel


class Person(BaseModel):
    __tablename__ = 'los_person'
    __table_args__ = {'comment': 'Danh sách khách hàng, người hôn phối, liên hệ theo quy định của pháp luật'}

    id = Column("ID", Integer, primary_key=True)

    branch = Column("BRANCH", VARCHAR(20), comment='Mã chi nhánh, ngân hàng đã khởi tạo hồ sơ')

    business_classification = Column("BUSINESS_CLASSIFICATION", VARCHAR(20),
                                     comment='Ngành nghề hoạt động của khách hàng')

    customer_category = Column("CUSTOMER_CATEGORY", VARCHAR(20),
                               comment='Loại khách hàng (Cá nhân, Doanh Nghiệp) (tham chiếu trong bảng los_ma_customer_type )')

    education_status = Column("EDUCATION_STATUS", VARCHAR(20),
                              comment='Trình độ học vấn của khách hàng. (tham chiếu trong bảng udtm )')

    owner_status = Column('OWNER_STATUS', VARCHAR(20),
                          comment='Tình trạng sở hữu về nhà ở hiện tại. (tham chiếu trong bảng udtm )')

    first_name = Column("FIRST_NAME", VARCHAR(50))

    middle_name = Column("MIDDLE_NAME", VARCHAR(100))

    last_name = Column("LAST_NAME", VARCHAR(100))

    full_name = Column("FULL_NAME", VARCHAR(100))

    full_name_no_signal = Column("FULL_NAME_NO_SIGNAL", VARCHAR(150),
                                 comment='Tên tiếng việt không dấu (Hệ thống tự động chạy không nhập tay).')

    sex = Column("SEX", VARCHAR(20), comment='Giới tính')

    date_of_birth = Column("DATE_OF_BIRTH", DateTime, comment='Ngày sinh')

    country = Column("COUNTRY", CHAR(20), comment='Quốc tịch')

    telephone = Column("TELEPHONE", CHAR(10), comment='Điện thoại để bàn')

    mobile = Column("MOBILE", CHAR(20), comment='Điện thoại di động')

    resident_status = Column("RESIDENT_STATUS", CHAR(5), comment='Tình trạng cư trú (tham chiếu trong bảng udtm )')

    cif_created_at = Column("CIF_CREATED_AT", DateTime, comment='Ngày tạo CIF')

    cif = Column("CIF", VARCHAR(15), comment='Mã số CIF trong Core')

    married_status = Column("MARRIED_STATUS", VARCHAR(20), comment='Tình trạng hon nhân ')

    dependent_gt_18 = Column("DEPENDENT_GT_18", Integer, comment='Số người phụ thuộc trên 18')

    dependent_lt_18 = Column("DEPENDENT_LT_18", Integer, comment='Số người phụ thuộc dưới 18')

    email = Column("EMAIL", VARCHAR(100), comment='Email')

    remaining_time_vn = Column("REMAINING_TIME_VN", Integer, comment='Thời gian còn ở lại VN dựa vào cái địa chỉ')

    location = Column("LOCATION", VARCHAR(20), comment='Location trên zeplin')

    birthplace = Column("BIRTHPLACE", VARCHAR(200), comment='Nơi sinh')

    note = Column("NOTE", VARCHAR(500), comment='Ghi chú')

    car_used_flag = Column("CAR_USED_FLAG", VARCHAR(1), comment='Có sử dụng xe ô tô không.')
