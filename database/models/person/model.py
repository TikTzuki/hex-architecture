from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class Person(BaseModel):
    __tablename__ = 'los_person'
    __table_args__ = {'comment': 'Danh sách khách hàng, người hôn phối, liên hệ theo quy định của pháp luật'}

    id = Column(Integer, primary_key=True, comment='Mã hồ sơ LOS')
    branch = Column(VARCHAR(20), comment='Mã chi nhánh, ngân hàng đã khởi tạo hồ sơ')
    business_classification = Column(VARCHAR(20), comment='Ngành nghề hoạt động của khách hàng')
    customer_category = Column(VARCHAR(20), comment='Loại khách hàng (Cá nhân, Doanh Nghiệp) (tham chiếu trong bảng los_ma_customer_type )')
    education_status = Column(VARCHAR(20), comment='Trình độ học vấn của khách hàng. (tham chiếu trong bảng udtm )')
    owner_status = Column(VARCHAR(20), comment='Tình trạng sở hữu về nhà ở hiện tại. (tham chiếu trong bảng udtm )')
    first_name = Column(VARCHAR(50))
    middle_name = Column(VARCHAR(100))
    last_name = Column(VARCHAR(100))
    full_name = Column(VARCHAR(100))
    full_name_no_signal = Column(VARCHAR(150), comment='Tên tiếng việt không dấu (Hệ thống tự động chạy không nhập tay).')
    sex = Column(VARCHAR(20), comment='Giới tính')
    date_of_birth = Column(DateTime, comment='Ngày sinh')
    country = Column(CHAR(20), comment='Quốc tịch')
    telephone = Column(CHAR(10), comment='Điện thoại để bàn')
    mobile = Column(CHAR(20), comment='Điện thoại di động')
    resident_status = Column(CHAR(20), comment='Tình trạng cư trú (tham chiếu trong bảng udtm )')
    cif_created_at = Column(DateTime, comment='Ngày tạo CIF')
    created_at = Column(DateTime)
    created_by = Column(VARCHAR(20), comment='Người khởi tạo')
    modified_at = Column(DateTime, comment='Ngày chỉnh sửa cuối cùng')
    modified_by = Column(VARCHAR(50), comment='Người chỉnh sửa cuối cùng')
    cif = Column(VARCHAR(15), comment='Mã số CIF trong Core')
    married_status = Column(VARCHAR(20), comment='Tình trạng hon nhân ')
    dependent_gt_18 = Column(Integer, comment='Số người phụ thuộc trên 18')
    dependent_lt_18 = Column(Integer, comment='Số người phụ thuộc dưới 18')
    uuid = Column(VARCHAR(50))
    email = Column(VARCHAR(100), comment='Email')
    remaining_time_vn = Column(Integer, comment='Thời gian còn ở lại VN dựa vào cái địa chỉ')
    location = Column(VARCHAR(20), comment='Location trên zeplin')
    birthplace = Column(VARCHAR(200), comment='Nơi sinh')
    note = Column(VARCHAR(500), comment='Ghi chú')
    car_used_flag = Column(VARCHAR(1), comment='Có sử dụng xe ô tô không. ')


