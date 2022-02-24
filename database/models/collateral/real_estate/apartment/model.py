from sqlalchemy import VARCHAR, Column, DateTime, Float, ForeignKey, Integer
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database import JSONSQL, BaseModel


class CollReApart(BaseModel):
    __tablename__ = 'v_los_coll_re_apart'
    __table_args__ = {'comment': 'Bảng thông tin lưu trữ tài sản là Căn hộ chung cư, thông tin định giá và thẩm định tài sản'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    price_cert_asset_appraisal_id = Column(ForeignKey('v_los_coll_price_cert_asset_appraisal.id'), comment='Mã tài sản bảo đảm tham chiếu qua bảng LOS_COLL_PRICE_CERT_ASSET_APPRAISAL')
    legal_status = Column(VARCHAR(50), comment='Tình trạng pháp lý ')
    apartment_name = Column(VARCHAR(200), comment='Tên chung cư dự án')

    price_cert_asset_appraisal = relationship('VLosCollPriceCertAssetAppraisal')


class CollReApartRoom(BaseModel):
    __tablename__ = 'v_los_coll_re_apart_room'
    __table_args__ = {'comment': 'Thông tin về căn hộ trong chung cư, có thể nhập nhiều căn'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_apart_id = Column(ForeignKey('v_los_coll_re_apart.id'), comment='Tham chiếu vào bảng RE_APART để biêt chung cư nào')
    apart_type_id = Column(VARCHAR(200), comment='Loại nhà ở')
    room_type_id = Column(VARCHAR(50), comment='Loại căn hộ')
    room_type_other = Column(VARCHAR(200), comment='Loại căn hộ khác')
    number_room = Column(VARCHAR(50), comment='Căn hộ số')
    block = Column(VARCHAR(50), comment='Block/ Tháp')
    floor = Column(VARCHAR(50), comment='Tầng')
    used_time = Column(DateTime, comment='Thời gian đưa vào sử dụng')
    area_cert = Column(Float, comment='Diện tích căn hộ theo pháp lý')
    area_real = Column(Float)
    owner_cert_id = Column(VARCHAR(200), comment='Hình thức sở hữu theo GCN')
    duration_cert = Column(VARCHAR(200), comment='Thời hạn sở hữu theo GCN')
    components = Column(VARCHAR(200), comment='Hạng mục được sở hữu chung ngoài căn hộ theo GCN')

    re_apart = relationship('VLosCollReApart')


class CollReApartLand(BaseModel):
    __tablename__ = 'v_los_coll_re_apart_land'
    __table_args__ = {'comment': 'Bảng thông tin về đất của Căn hộ chung cư'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_apart_id = Column(ForeignKey('v_los_coll_re_apart.id'), comment='Tham chiếu qua bảng LOS_COLL_RE_APART để biết căn hộ chung cư nào ')
    address = Column(VARCHAR(200), comment='Địa chỉ thực tế thửa đất')
    province_id = Column(VARCHAR(50), comment='Tình / TP')
    district_id = Column("distinct_id", VARCHAR(50), comment='Quận / Huyện')
    ward_id = Column(VARCHAR(50), comment='Phường / Xã')
    cert_address = Column(VARCHAR(200), comment='Địa chỉ theo GCN ')
    cert_province_id = Column(VARCHAR(50), comment='Tình / TP')
    cert_district_id = Column('cert_distinct_id', VARCHAR(50), comment='Quận / Huyện')
    cert_ward_id = Column(VARCHAR(50), comment='Phường / Xã')
    purpose_land_id = Column(JSONSQL(50), comment='Mục đích sử dụng đất ( theo thẩm định giá)')
    purpose_land_other = Column(VARCHAR(200), comment='Mục đích sử dụng đất ( theo thẩm định giá) khác')

    re_apart = relationship('VLosCollReApart')


class CollReApartLandUsed(BaseModel):
    __tablename__ = 'v_los_coll_re_apart_land_used'
    __table_args__ = {'comment': 'Bảng thông tin về mục đích sử dụng đất của căn hộ chung cư'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_apart_land_id = Column(ForeignKey('v_los_coll_re_apart_land.id'), comment='Tham chiếu vào bảng LOS_COLL_RE_APART_LAND, để mục đích của Đất nào')
    purpose_cert = Column(VARCHAR(200), comment='Mục đích sử dụng theo GCN')
    land_number = Column(NUMBER(asdecimal=False), comment='Số thửa đất')
    map_number = Column(NUMBER(asdecimal=False), comment='Tờ bản đồ số')
    area_cert_value = Column(Float, comment='Diện tích đất theo GCN (m2)')
    area_used_value = Column(Float, comment='Diện tích đất thực tế (m2)')
    source_cert_id = Column(VARCHAR(50), comment='Nguồn gốc sử dụng đất theo GCN')
    source_cert_other = Column(VARCHAR(200), comment='Nguồn gốc sử dụng đất theo GCN (Khác)')
    time_used_cert = Column(VARCHAR(50), comment='Thời hạn sử dụng đất theo GCN')
    method_used_cert = Column(VARCHAR(50), comment='Hình thức sử dụng đất theo GCN')
    method_used_other = Column(VARCHAR(200), comment='Hình thức sử dụng đất theo GCN Khác')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị')

    re_apart_land = relationship('VLosCollReApartLand')


class CollReApartOwner(BaseModel):
    __tablename__ = 'v_los_coll_re_apart_owner'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin chủ sở hữu căn hộ chung cư'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_apart_id = Column(ForeignKey('v_los_coll_re_apart.id'), comment='Tham chiếu qua bảng TSBD Căn hộ chung cư (LOS_COLL_RE_APART)')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID')
    owner_type_id = Column(VARCHAR(50), comment='Loại hình sở hữu (Chính chủ, Đồng sở hữu….)')
    owner_auth_flag = Column(VARCHAR(1), comment='Có uỷ quyền cho người khác không Y/N')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị')

    re_apart = relationship('VLosCollReApart')


class CollReApartOwnerCert(BaseModel):
    __tablename__ = 'v_los_coll_re_apart_owner_cert'
    __table_args__ = {'comment': 'Bảng lưu trữ danh sách các giấy chứng nhận theo 1 căn hộ chung cư'}

    id = Column(Integer, primary_key=True)
    re_apart_id = Column(ForeignKey('v_los_coll_re_apart.id'), comment='Tham chiếu qua bảng LOS_COLL_RE_APART để biết căn hộ chung cư nào')
    display_order = Column(Integer)
    actived_flag = Column(VARCHAR(2))

    re_apart = relationship('VLosCollReApart')


class CollReApartOwnerCertItem(BaseModel):
    __tablename__ = 'v_los_coll_re_apart_owner_cert_item'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin hồ sơ Giấy CN Sở hữu căn hộ chung cư'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_apart_owner_cert_id = Column(ForeignKey('v_los_coll_re_apart_owner_cert.id'), comment='Tham chiếu qua bảng RE_APART_OWNER_CERT để có thể có chi tiết của giấy chứng nhận nào')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID, người được xác nhận là sở hữu CTXD')
    land_owner_cert_type_id = Column(VARCHAR(50), comment='Loại giấy chứng nhận quyền sử dụng đất')
    land_owner_cert_other = Column(VARCHAR(200), comment='Loại giấy chứng nhận quyền sử dụng đất khác')
    number_cert = Column(VARCHAR(50), comment='Số GCN/ Giấy tờ pháp lý')
    book_number_cert = Column(VARCHAR(50), comment='Số vào sổ cấp GCN')
    published_at = Column(DateTime, comment='Ngày cấp')
    place_of_issued = Column(VARCHAR(200), comment='Nơi cấp')
    contract_type = Column(VARCHAR(200), comment='Loại hợp đồng')
    contract_number = Column(VARCHAR(200), comment='Số hợp đồng')
    contract_date = Column(DateTime, comment='Ngày hợp đồng')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị')

    re_apart_owner_cert = relationship('VLosCollReApartOwnerCert')


class CollReApartOwnerAuth(BaseModel):
    __tablename__ = 'v_los_coll_re_apart_owner_auth'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin về việc uỷ quyền của chủ sở hữu căn hộ chung cư'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_apart_owner_id = Column(ForeignKey('v_los_coll_re_apart_owner.id'), comment='Tham chiếu qua bảng LOS_COLL_RE_APART_OWNER để biết ai là người uỷ quyền')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID, người được nhận uỷ quyền')
    rel_auth_owner = Column(VARCHAR(200), comment='Môi quan hệ của người được uỷ quyền với chủ tài sản')
    rel_auth_borrower = Column(VARCHAR(200), comment='Mỗi quan hệ của người được uỷ quyền với chính đối tượng vay, Lưu ý có thể chính người đi vay là người được uỷ quyền ')
    contract_authorized = Column(VARCHAR(200), comment='Hợp đồng uỷ quyền ')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị')

    re_apart_owner = relationship('VLosCollReApartOwner')
