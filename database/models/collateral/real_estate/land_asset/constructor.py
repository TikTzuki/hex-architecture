from sqlalchemy import VARCHAR, Column, DateTime, Float, Integer
from sqlalchemy.dialects.oracle import NUMBER

from database.models.utils import BaseModel


class CollReLandConst(BaseModel):
    __tablename__ = 'v_los_coll_re_land_const'
    __table_args__ = {'comment': 'Bảng thông tin CTXD trên trên Đất'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_land_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Đất để biết CTXD này thuộc về đất nào')
    asset_credit_flag = Column(VARCHAR(1), comment='Tài sản được hình thành từ nguồn vốn CTD')
    source_income_asset_flag = Column(VARCHAR(1), comment='Nguồn trả tiền nợ là nguôn tiền hình thành từ việc kinh doanh, khai thác chính TSBD')
    asset_used_loan_flag = Column(VARCHAR(1), comment='TS đang đảm bảo cho nghĩa vụ CTD ')
    re_no_business_ratio = Column(Float, comment='Tỷ lệ diện tích BDS không kinh doanh')
    amount_loan_ratio = Column(Float, comment='Tỷ lệ cho vay tối đa theo quy định')
    description = Column(VARCHAR(200), comment='Thông tin nghĩa vụ bảo đảm')
    gross_value_cons = Column(Float, comment='Giá trị CTXD trên đất theo từng GCN')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị')


class CollReLandConstItem(BaseModel):
    __tablename__ = 'v_los_coll_re_land_const_item'
    __table_args__ = {'comment': 'Bảng danh sách thông tin CTXD trên Đất'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_land_const_id = Column(NUMBER(asdecimal=False), comment='Công trình đi theo bảng GCN tham chiếu qua bảng LOS_COLL_RE_LAND_CONST')
    const_cert_type = Column(VARCHAR(50), comment='Pháp lý CTXD ')
    const_cert_other = Column(VARCHAR(200), comment='Pháp lý CTXD Khác')
    address = Column(VARCHAR(200), comment='Địa chỉ thực tế nhà ở / CTXD')
    province_id = Column(VARCHAR(20), comment='Tỉnh / Thành phố')
    district_id = Column('distinct_id', VARCHAR(20))
    ward_id = Column(VARCHAR(20), comment='Quận / Huyện')
    cert_address = Column(VARCHAR(200), comment='Địa chỉ theo GCN')
    cert_province_id = Column(VARCHAR(20), comment='Tỉnh / Thành phố')
    cert_district_id = Column('cert_distinct_id', VARCHAR(20), comment='Quận / Huyện')
    cert_ward_id = Column(VARCHAR(20), comment='Phường / Xã')


class CollReLandConstItemDetail(BaseModel):
    __tablename__ = 'v_los_coll_re_land_const_item_detail'
    __table_args__ = {'comment': 'Bảng chi tiết các CTXD'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_land_const_item_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng LOS_COLL_RE_LAND_CONST_ITEM, để biết chi tiết CTXD này thuộc trong nhóm nào')
    const_type_id = Column(VARCHAR(50), comment='Loại công trình ')
    const_type_other = Column(VARCHAR(200), comment='Loại công trình khác')
    area_cert = Column(Float, comment='Diện tích xây dựng theo GCN')
    area_real = Column(Float, comment='Diện tích xây dựng thực tế')
    area_floor_cert = Column(Float, comment='Diện tích sử dụng theo GCN (m2)')
    area_floor_real = Column(Float, comment='Diện tích sử dụng thực tế')
    area_used_cert = Column(Float)
    area_used_real = Column(Float)
    term = Column(VARCHAR(50), comment='Thời hạn sở hữu')
    owner_method_id = Column(VARCHAR(50), comment='Hình thức sở hữu')
    structural_cert = Column(VARCHAR(100), comment='Kết cấu công trình theo GCN')
    structural_real = Column(VARCHAR(100), comment='Kết cấu công trình thực tế')
    level_cert = Column(VARCHAR(100), comment='Cấp (Hạng) theo GCN')
    num_floor_cert = Column(NUMBER(asdecimal=False), comment='Số tầng theo GCN')
    num_floor_real = Column(NUMBER(asdecimal=False), comment='Số tầng thực tế')
    used_time = Column(VARCHAR(50), comment='Thời gian đưa vào sử dụng ')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị')


class CollReLandConstItemOwner(BaseModel):
    __tablename__ = 'v_los_coll_re_land_const_item_owner'
    __table_args__ = {'comment': 'Thông tin chủ sở hữu CTXD'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_land_const_id = Column(NUMBER(asdecimal=False), comment='Công trình đi theo bảng GCN tham chiếu qua bảng LOS_COLL_RE_LAND_CONST')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID')
    owner_type_id = Column(VARCHAR(50), comment='Loại hình sở hữu (Chính chủ, Đồng sở hữu….)')
    owner_auth_flag = Column(VARCHAR(1), comment='Có uỷ quyền cho người khác không Y/N')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị ')


class CollReLandConstItemOwnerAuth(BaseModel):
    __tablename__ = 'v_los_coll_re_land_const_item_owner_auth'
    __table_args__ = {'comment': 'Bảng lưu thông tin về việc uỷ quyền (chỉ dành cho CTXD riêng)'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_land_const_item_owner_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng LOS_COLL_RE_LAND_CONST_ITEM_OWNER để biết ai là người uỷ quyền')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID, người được nhận uỷ quyền')
    rel_auth_owner = Column(VARCHAR(50), comment='Môi quan hệ của người được uỷ quyền với chủ tài sản')
    rel_auth_borrower = Column(VARCHAR(50), comment='Mỗi quan hệ của người được uỷ quyền với chính đối tượng vay, Lưu ý có thể chính người đi vay là người được uỷ quyền ')
    contract_authorized = Column(VARCHAR(200), comment='Sô hợp đồng uỷ quyền')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị ')


class CollReLandConstItemCert(BaseModel):
    __tablename__ = 'v_los_coll_re_land_const_item_cert'
    __table_args__ = {'comment': 'Bảng lưu thông tin danh sách những người có giấy chứng nhận công trình xây dựng'}

    id = Column('id', Integer, primary_key=True)
    re_land_const_id = Column('re_land_const_id', Integer, comment='Công trình đi theo bảng GCN tham chiếu qua bảng LOS_COLLL_RE_LAND_CONS')
    actived_flag = Column('actived_flag', VARCHAR(10))
    display_order = Column('display_order', Integer)


class CollReLandConstItemCertItem(BaseModel):
    __tablename__ = 'v_los_coll_re_land_const_item_cert_item'
    __table_args__ = {'comment': 'Thông tin giấy CN CTXD'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    re_land_const_item_cert_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng RE_LAND_CONST_ITEM_CERT để biết ngừoi này thuộc về GCN nào')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID, người được nhận uỷ quyền')
    land_owner_cert_type_id = Column(VARCHAR(50), comment='Loại GCN quyền sở hữu nhà ở / CTXD')
    land_owner_cert_other = Column(VARCHAR(200), comment='Loại GCN quyền sở hữu nhà ở / CTXD Khác')
    number_cert = Column(VARCHAR(100), comment='Số GCN/ giấy tờ pháp lý')
    book_number_cert = Column(VARCHAR(100), comment='Số vào sổ cấp GCN ')
    published_at = Column(DateTime, comment='Ngày cấp')
    place_of_issued = Column(VARCHAR(50), comment='Nơi cấp')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị ')
