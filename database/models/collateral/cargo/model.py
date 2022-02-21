from sqlalchemy import Column, DateTime, VARCHAR
from sqlalchemy.dialects.oracle import NUMBER

from database.models.utils import BaseModel


class CollCargo(BaseModel):
    __tablename__ = 'v_los_coll_cargo'
    __table_args__ = {'comment': 'Tài sản là vật tư hàng hóa'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    price_cert_asset_appraisal_id = Column(NUMBER(asdecimal=False), comment='Mã tài sản bảo đảm tham chiếu qua bảng LOS_COLL_PRICE_CERT_ASSET_APPRAISAL')
    coll_type = Column(VARCHAR(100), comment='Loại tài sản')
    license_number = Column(VARCHAR(50), comment='Số giấy đăng ký')
    coll_status_id = Column(VARCHAR(50), comment='Tình trạng tài sản')
    description = Column(VARCHAR(200), comment='Mô tả tài sản')



class CollCargoOwner(BaseModel):
    __tablename__ = 'v_los_coll_cargo_owner'
    __table_args__ = {'comment': 'Bảng lưu thông tin chủ tài sản Hàng hoá'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    cargo_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng LOS_COLL_CARGO')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID')
    owner_type_id = Column(VARCHAR(50), comment='Loại hình sở hữu (Chính chủ, Đồng sở hữu….)')
    display_order = Column(NUMBER(asdecimal=False), comment='Số thứ tự hiển thị ')

