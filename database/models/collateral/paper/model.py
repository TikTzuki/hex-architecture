from sqlalchemy import VARCHAR, Column, ForeignKey
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class CollPaper(BaseModel):
    __tablename__ = 'v_los_coll_paper'
    __table_args__ = {'comment': 'Lọai giấy tờ có giá, sổ tiết kiệm'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    price_cert_asset_appraisal_id = Column(ForeignKey('v_los_coll_price_cert_asset_appraisal.id'), comment='Mã tài sản bảo đảm tham chiếu qua bảng LOS_COLL_PRICE_CERT_ASSET_APPRAISAL')
    coll_type = Column(VARCHAR(100), comment='Loại tài sản')
    license_number = Column(VARCHAR(50), comment='Số giấy đăng ký')
    coll_status_id = Column(VARCHAR(50), comment='Tình trạng tài sản')
    description = Column(VARCHAR(200), comment='Mô tả tài sản')

    price_cert_asset_appraisal = relationship('VLosCollPriceCertAssetAppraisal')


class CollPaperOwner(BaseModel):
    __tablename__ = 'v_los_coll_paper_owner'
    __table_args__ = {'comment': 'Bảng lưu thông tin chủ tài sản: Giấy tờ có giá'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    paper_id = Column(ForeignKey('v_los_coll_paper.id'), comment='Tham chiếu qua bảng LOS_COLL_PAPER')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID')
    owner_type_id = Column(VARCHAR(50), comment='Loại hình sở hữu (Chính chủ, Đồng sở hữu….)')
    display_order = Column(NUMBER(asdecimal=False), comment='Số thứ tự hiển thị ')

    paper = relationship('VLosCollPaper')
