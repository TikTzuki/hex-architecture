from sqlalchemy import VARCHAR, Column, ForeignKey
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class CollMachine(BaseModel):
    __tablename__ = 'v_los_coll_machine'
    __table_args__ = {'comment': 'Bảng lưu thông tin tài sản là Máy móc dây chuyền sản xuất'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    price_cert_asset_appraisal_id = Column(ForeignKey('v_los_coll_price_cert_asset_appraisal.id'), comment='Mã tài sản bảo đảm tham chiếu qua bảng LOS_COLL_PRICE_CERT_ASSET_APPRAISAL')
    coll_type_id = Column(VARCHAR(100), comment='Loại tài sản')
    quantity_each_type = Column(NUMBER(asdecimal=False), comment='Số lượng từng loại')
    year_manufacture = Column(VARCHAR(50), comment='Năm sản xuất')
    machine_brand = Column(VARCHAR(50), comment='Nhãn hiệu')
    model = Column(VARCHAR(50), comment='Model (Số loại)')
    origin_production = Column(VARCHAR(100), comment='Nơi sản xuất / lắp ráp')
    remaining_quality = Column(VARCHAR(100), comment='Chất lượng còn lại (Thẩm định)')
    license_number = Column(VARCHAR(50), comment='Số giấy đăng kí')
    coll_status_id = Column(VARCHAR(50), comment='Tình trạng tài sản')
    description = Column(VARCHAR(200), comment='Mô tả tài sản')
    amount = Column(NUMBER(asdecimal=False), comment='Số lượng (chiếc)')

    price_cert_asset_appraisal = relationship('VLosCollPriceCertAssetAppraisal')


class CollMachineOwner(BaseModel):
    __tablename__ = 'v_los_coll_machine_owner'
    __table_args__ = {'comment': 'Bảng lưu thông tin chủ tài sản Máy móc dây chuyền sản xuất'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    machine_id = Column(ForeignKey('v_los_coll_machine.id'), comment='Tham chiếu qua bảng LOS_COLL_MACHINE')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID')
    owner_type_id = Column(VARCHAR(50), comment='Loại hình sở hữu (Chính chủ, Đồng sở hữu….)')
    display_order = Column(NUMBER(asdecimal=False), comment='Số thứ tự hiển thị ')

    machine = relationship('VLosCollMachine')
