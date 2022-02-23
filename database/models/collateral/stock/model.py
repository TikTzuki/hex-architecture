from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.oracle import NUMBER

from database.base import BaseModel


class CollRightStock(BaseModel):
    __tablename__ = 'v_los_coll_right_stock'
    __table_args__ = {'comment': 'Tài sản là cổ phiếu cổ phần, chứng khoán'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    price_cert_asset_appraisal_id = Column(ForeignKey('v_los_coll_price_cert_asset_appraisal.id'), comment='Mã tài sản bảo đảm tham chiếu qua bảng LOS_COLL_PRICE_CERT_ASSET_APPRAISAL')
    coll_type = Column(VARCHAR(100), comment='Loại tài sản')
    license_number = Column(VARCHAR(50), comment='Số giấy đăng ký')
    coll_status_id = Column(VARCHAR(50), comment='Tình trạng tài sản')
    description = Column(VARCHAR(200), comment='Mô tả tài sản')

    price_cert_asset_appraisal = relationship('VLosCollPriceCertAssetAppraisal')


class CollRightStockOwner(BaseModel):
    __tablename__ = 'v_los_coll_right_stock_owner'
    __table_args__ = {'comment': 'Bảng lưu thông tin chủ tài sản: Cổ phần chứng khoán'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    right_stock_id = Column(ForeignKey('v_los_coll_right_stock.id'), comment='Tham chiếu qua bảng LOS_COLL_RIGHT_STOCK')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID')
    owner_type_id = Column(VARCHAR(50), comment='Loại hình sở hữu (Chính chủ, Đồng sở hữu….)')
    display_order = Column(NUMBER(asdecimal=False), comment='Số thứ tự hiển thị ')

    right_stock = relationship('VLosCollRightStock')
