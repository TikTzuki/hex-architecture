from sqlalchemy import VARCHAR, Column, DateTime, Float, Integer
from sqlalchemy.dialects.oracle import NUMBER

from app.third_party.oracle.models.utils import JSONSQL, BaseModel


class CollReLand(BaseModel):
    __tablename__ = 'v_los_coll_re_land'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin lưu trữ loại TSBD là Đất, thông tin định giá và thẩm định tài sản'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    price_cert_asset_appraisal_id = Column(NUMBER(asdecimal=False), comment='Mã tài sản bảo đảm tham chiếu qua bảng LOS_COLL_PRICE_CERT_ASSET_APPRAISAL')
    asset_land_flag = Column(VARCHAR(1), comment='Mã tài sản chi tiết trong bảng lưu trữ thông tin các tài sản bảo đảm (Bảng LOS_COLL_PRICE_CERT_ASSET)')
    asset_land_private_flag = Column(VARCHAR(1), comment='Nguồn trả tiền nợ là nguôn tiền hình thành từ việc kinh doanh, khai thác chính TSBD')
    address = Column(VARCHAR(200), comment='TS đang đảm bảo cho nghĩa vụ CTD')
    province_id = Column(VARCHAR(20), comment='Tỉnh / Thành phố')
    district_id = Column("distinct_id", VARCHAR(20))
    ward_id = Column(VARCHAR(20), comment='Quận / Huyện')
    cert_address = Column(VARCHAR(200), comment='Địa chỉ theo GCN')
    cert_province_id = Column(VARCHAR(20), comment='Tỉnh / Thành phố')
    cert_district_id = Column('cert_distinct_id', VARCHAR(20), comment='Quận / Huyện')
    cert_ward_id = Column(VARCHAR(20), comment='Phường / Xã')
    purpose_land_id = Column(JSONSQL(500), comment='Lưu theo dạng format: 1,2,4,5. Tham chiéu qua bảng UDTM')
    purpose_land_other = Column(VARCHAR(200), comment='Lưu trực tiêp value của mục đích sử dụng')


class CollReLandOwner(BaseModel):
    __tablename__ = 'v_los_coll_re_land_owner'
    __table_args__ = {'comment': 'Bảng ghi nhận thông tin người chủ sở hữu tài sản đất'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_land_id = Column(NUMBER(asdecimal=False), comment='Bất động sản, tham chiếu qua bảng LOS_COLL_RE_LAND')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID')
    owner_type_id = Column(VARCHAR(50), comment='Loại hình sở hữu (Chính chủ, Đồng sở hữu….)')
    owner_auth_flag = Column(VARCHAR(1), comment='Có uỷ quyền cho người khác không Y/N')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị')


class CollReLandOwnerAuth(BaseModel):
    __tablename__ = 'v_los_coll_re_land_owner_auth'
    __table_args__ = {'comment': 'Bảng ghi nhận thông tin về việc uỷ quyền của chủ sở hữu tài sản Đất'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_land_owner_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng LOS_COLL_RE_LAND_OWNER để biết ai là người uỷ quyền')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID, người được nhận uỷ quyền')
    rel_auth_owner = Column(VARCHAR(50), comment='Môi quan hệ của người được uỷ quyền với chủ tài sản')
    rel_auth_borrower = Column("rel_auth_browser", VARCHAR(50), comment='Mỗi quan hệ của người được uỷ quyền với chính đối tượng vay, Lưu ý có thể chính người đi vay là người được uỷ quyền')
    contract_authorized = Column(VARCHAR(200), comment='Hợp đồng uỷ quyền ')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị')


class CollReLandCert(BaseModel):
    __tablename__ = 'v_los_coll_re_land_cert'
    __table_args__ = {'comment': 'Bảng lưu thông tin danh sách giấy chứng nhận của một mảnh đất'}
    id = Column('id', Integer, primary_key=True)
    re_land_id = Column('re_land_id', Integer, comment='Tham chiếu qua bảng LOS_COLL_RE_LAND để biết mảnh đất nào')
    display_order = Column('display_order', Integer, comment='Số thứ tự của giấy chứng nhận')
    actived_flag = Column('actived_flag', VARCHAR(10), comment='Có kích hoạt không (Y/N)')


class CollReLandCertItem(BaseModel):
    __tablename__ = 'v_los_coll_re_land_cert_item'
    __table_args__ = {'comment': 'Bảng ghi nhận thông tin về việc uỷ quyền của chủ sở hữu tài sản Đất'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_land_cert_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng COLL_RE_LAND_CERT để biết người này thuộc về giấy chứng nhận nào')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID, người được xác nhận là sở hữu CTXD')
    land_owner_cert_type_id = Column(VARCHAR(50), comment='Loại giấy chứng nhận quyền sử dụng đất')
    land_owner_cert_other = Column(VARCHAR(200), comment='Loại giấy chứng nhận quyền sử dụng đất khác')
    number_cert = Column(VARCHAR(50), comment='Số GCN/ Giấy tờ pháp lý')
    book_number_cert = Column(VARCHAR(50), comment='Số vào sổ cấp GCN')
    published_at = Column(DateTime, comment='Ngày cấp')
    place_of_issued = Column(VARCHAR(200), comment='Nơi cấp')
    display_order = Column(NUMBER(asdecimal=False), comment='Số thứ tự hiển thị')


class CollReLandUsed(BaseModel):
    __tablename__ = 'v_los_coll_re_land_used'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin mục đích sử dụng Đất'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_land_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng LOS_COLL_RE_LAND để biết mảnh đất nào')
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
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị ')
