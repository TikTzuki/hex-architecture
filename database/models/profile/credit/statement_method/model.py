from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class ProfileCreditStatementMethod(BaseModel):
    __tablename__ = 'los_profile_credit_statement_method'
    __table_args__ = {'comment': 'Mô tả dùng để lưu thông tin hình thức nhận bảng sao kê thẻ và các thông báo khác'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    credit_published_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu tới thẻ chính')
    statement_method_type_id = Column(VARCHAR(50), comment='Hình thức giao thẻ tham chiếu qua UDTM')
    address = Column(VARCHAR(200), comment='Địa chỉ nhận thông tin')
    province_id = Column(VARCHAR(20), comment='Tỉnh / Thành phố')
    district_id = Column(VARCHAR(20), comment='Quận / Huyện')
    ward_id = Column(VARCHAR(20), comment='Phường / Xã')
