from sqlalchemy import VARCHAR, Column, Float, ForeignKey, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class Collateral(BaseModel):
    __tablename__ = 'v_los_collateral'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin hồ sơ tài sản bảo đảm trong hệ thống, 1 hồ sơ LOS chỉ có 1 record, dùng để lưu thông tin tông hợp dùng chung trong hệ thống '}

    id = Column(NUMBER(asdecimal=False), primary_key=True, server_default=text("NULL"))
    code = Column(VARCHAR(50), comment='Mã hồ sơ tài sản bảo đảm')
    sequence_id = Column(ForeignKey('los_profile_sequence_item.id'), comment='Table LOS_PROFILE_SEQUENCE_ITEM tham chiếu')
    credit_sequence_id = Column(ForeignKey('los_profile_credit_sequence_item.id'), comment='Table LOS_CREDIT_SEQUENCE_ITEM tham chiếu')
    gross_value = Column(Float, comment='Tổng số tiền được trong hồ sơ')
    price_cert_actived_flag = Column(VARCHAR(1), comment='Đã được xác nhận bằng chứng thư định giá')

    credit_sequence = relationship('ProfileCreditSequenceItem')
    sequence = relationship('ProfileSequenceItem')
