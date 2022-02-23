from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import Base


class MaAppraisalUnit(Base):
    __tablename__ = 'los_ma_appraisal_unit'
    __table_args__ = {'comment': 'Danh sách các tổ chức định giá độc lập và Trung tâm thẩm định giá'}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), comment='Tên đơn vị định giá')
    description = Column(VARCHAR(100), comment='Diễn giải thêm thông tin')
    address = Column(VARCHAR(100), comment='Địa chỉ')
    province_id = Column(VARCHAR(100), comment='Tỉnh / Thành phố')
    district_id = Column(VARCHAR(100), comment='Quận / Huyện')
    ward_id = Column(VARCHAR(100), comment='Phường / Xã')
    tax = Column(VARCHAR(100), comment='Mã số thuế')
    cert_num = Column(VARCHAR(100), comment='Số giấy phép')
    appraisal_unit_type_id = Column(VARCHAR(100), comment='Loại hình (TT.TSTS hoặc TC Định giá độc lập), tham chiếu qua UDTM')
    display_order = Column(Integer)
    other_value_flag = Column(VARCHAR(1), server_default=text("'N'"))
