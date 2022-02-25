from sqlalchemy import VARCHAR, Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class CollReMarket(BaseModel):
    __tablename__ = 'v_los_coll_re_market'
    __table_args__ = {'comment': 'Bảng thông tin lưu trữ tài sản là Sạp chợ/ TTTM'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    price_cert_asset_appraisal_id = Column(ForeignKey('v_los_coll_price_cert_asset_appraisal.id'), comment='Mã tài sản bảo đảm tham chiếu qua bảng LOS_COLL_PRICE_CERT_ASSET_APPRAISAL')
    legal_status = Column(VARCHAR(50), comment='Tình trạng pháp lý')
    name = Column(VARCHAR(200), comment='Tên chợ / TTTM')
    number_market = Column(VARCHAR(50), comment='Số hiệu gian hàng / Sạp chợ')
    position = Column(VARCHAR(100), comment='Vị trí')
    business_category = Column(VARCHAR(50), comment='Ngành hing kinh doanh')
    start_date = Column(DateTime, comment='Thời hạn sử dụng từ')
    end_date = Column(DateTime, comment='Thời hạn sử dụng đến')
    rest_used = Column(NUMBER(asdecimal=False), comment='Thời hạn sử dụng còn lại theo báo cáo thẩm định - định giá (tháng)')
    area_used = Column(Float, comment='Diện tích sử dụng')
    area_value = Column(Float, comment='Diện tích tính giá trị (m2)')
    structural_cert = Column(VARCHAR(200), comment='Kết cấu theo chứng từ pháp lý')

    price_cert_asset_appraisal = relationship('CollPriceCertAssetAppraisal')


class CollReMarketCert(BaseModel):
    __tablename__ = 'v_los_coll_re_market_cert'
    __table_args__ = {'comment': 'Bảng thông tin lưu danh sách giấy chứng nhận về sạp chợ / Ô TTTM'}

    id = Column(Integer, primary_key=True)
    re_market_id = Column(ForeignKey('v_los_coll_re_market.id'), comment='Tham chiếu qua bảng LOS_COLL_RE_MARKET')
    display_order = Column(Integer)
    actived_flag = Column(VARCHAR(10))

    re_market = relationship('CollReMarket')


class CollReMarketCertItem(BaseModel):
    __tablename__ = 'v_los_coll_re_market_cert_item'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin giấy CN pháp lý.'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_market_cert_id = Column(ForeignKey('v_los_coll_re_market_cert.id'), comment='Tham chiếu qua bảng LOS_COLL_RE_MARKET_CERT')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID, người được nhận uỷ quyền')
    name_cert = Column(VARCHAR(100), comment='Tên GCN')
    number_cert = Column(VARCHAR(100), comment='Số GCN')
    published_at = Column(DateTime, comment='Ngày cấp')
    place_of_issued = Column(VARCHAR(100), comment='Nơi cấp')
    contract_name = Column(VARCHAR(100), comment='Tên hợp đồng thuê')
    contract_number = Column(VARCHAR(100), comment='Số hợp đồng thuê')
    contract_date = Column(DateTime, comment='Ngày ký kết')
    lessor = Column(VARCHAR(100), comment='Bên cho thuê')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị ')

    re_market_cert = relationship('CollReMarketCert')


class CollReMarketOwner(BaseModel):
    __tablename__ = 'v_los_coll_re_market_owner'
    __table_args__ = {'comment': 'Bảng lưu thông tin chủ sở hữu sạp chợ / Ô Trung tâm thương mại'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_market_id = Column(ForeignKey('v_los_coll_re_market.id'), comment='Tham chiếu qua bảng RE_MARKET ')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID')
    owner_type_id = Column(VARCHAR(100), comment='Loại hình sở hữu (Chính chủ, Đồng sở hữu….)')
    owner_auth_flag = Column(VARCHAR(1), comment='Có uỷ quyền cho người khác không Y/N')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị ')

    re_market = relationship('CollReMarket')


class CollReMarketOwnerAuth(BaseModel):
    __tablename__ = 'v_los_coll_re_market_owner_auth'
    __table_args__ = {'comment': 'Bảng lưu thông tin về việc uỷ quyền của chủ sở chữ sạp chợ '}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_market_owner_id = Column(ForeignKey('v_los_coll_re_market_owner.id'), comment='Tham chiếu qua bảng LOS_COLL_RE_MARKET_OWNER để biết ai là người uỷ quyền')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID, người được nhận uỷ quyền')
    rel_auth_owner = Column(VARCHAR(100), comment='Môi quan hệ của người được uỷ quyền với chủ tài sản')
    rel_auth_borrower = Column(VARCHAR(100), comment='Mỗi quan hệ của người được uỷ quyền với chính đối tượng vay, Lưu ý có thể chính người đi vay là người được uỷ quyền')
    contract_authorized = Column(VARCHAR(200), comment='Hợp đồng uỷ quyền ')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị ')

    re_market_owner = relationship('CollReMarketOwner')
