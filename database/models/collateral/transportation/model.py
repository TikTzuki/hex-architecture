from sqlalchemy import VARCHAR, Column
from sqlalchemy.dialects.oracle import NUMBER

from app.third_party.oracle.models.utils import Base, BaseModel


class CollTran(BaseModel):
    __tablename__ = 'v_los_coll_trans'
    __table_args__ = {'comment': 'Bảng lưu thông tin tài sản là PTVT Đường bộ.'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    price_cert_asset_appraisal_id = Column(NUMBER(asdecimal=False), comment='Mã tài sản bảo đảm tham chiếu qua bảng LOS_COLL_PRICE_CERT_ASSET_APPRAISAL')
    person_id = Column(NUMBER(asdecimal=False))
    trans_type = Column("trans_name", VARCHAR(50), comment='Loại phương tiện ')
    trans_type_other = Column("trans_name_other", VARCHAR(100), comment='Chi tiết loại phương tiện khác')
    trans_brand = Column("trans_brand_id", VARCHAR(50), comment='Nhãn hiệu')
    trans_brand_other = Column(VARCHAR(100), comment='Nhãn hiệu khác')
    model = Column(VARCHAR(50), comment='Model (số loại)')
    model_other = Column(VARCHAR(100), comment='Model (số loại) khác')
    origin_production = Column(VARCHAR(50), comment='Nơi sản xuất / lắp ráp')
    origin_production_other = Column(VARCHAR(100), comment='Nơi sản xuất / lắp ráp khác')
    license_number = Column(VARCHAR(50), comment='Sô giấy đăng ký / HSPL')
    trans_status = Column(VARCHAR(50), comment='Tình trạng PTVT ')
    structure_number = Column(VARCHAR(50), comment='Sô khung')
    machine_number = Column(VARCHAR(50), comment='Số máy')
    license_plate = Column(VARCHAR(500), comment='Biển số đăng ký')
    description = Column(VARCHAR(100), comment='Mô tả tài sản')
    quality_rest_ratio = Column(VARCHAR(50), comment='Tỷ lệ chất lượng còn lại của tài sản ')


class CollTransLegalDocument(BaseModel):
    __tablename__ = 'v_los_coll_trans_legal_document'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin về danh mục hồ sơ pháp lý của PTVT'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    trans_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng LOS_COLL_TRANS')
    trans_legal_doc_type_id = Column(VARCHAR(50),
                                     comment='Loại hồ sơ pháp lý\n'
                                             '- Giấy chứng nhận\n'
                                             '- Tờ khai\n'
                                             '- Hợp đồng\n'
                                             '- Hoá đơn')
    trans_legal_value = Column(VARCHAR(200),
                               comment='Chi tiết hồ sơ pháp lý theo loại: (lưu\n'
                                       '- GCN đăng ký xe ô tô, GCN kiểm định…..\n'
                                       '- Tờ khai hải quan, tờ khai nguồn gốc, tờ khai khác\n'
                                       '- Hợp đồng thương mại, hợp đồng mua bán, hoá đơn (invoice), Khác….\n'
                                       '- Hoá đơn tài chính, Khác….')


class CollTransOwner(BaseModel):
    __tablename__ = 'v_los_coll_trans_owner'
    __table_args__ = {'comment': 'Thông tin pháp lý chủ sở hữu'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    trans_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng LOS_COLL_TRANS')
    person_id = Column(NUMBER(asdecimal=False), comment='Tham chiếu qua bảng Person để lấy đúng ID ')
    owner_type_id = Column(VARCHAR(50), comment='Loại hình sở hữu (Chính chủ, Đồng sở hữu….)')
    display_order = Column(NUMBER(asdecimal=False), comment='Số thứ tự hiển thị ')


class CountryManufacture(Base):
    __tablename__ = 'los_ma_coll_coun_manu'

    country_code = Column("COUNTRY_CODE", VARCHAR(3), primary_key=True)

    name = Column("NAME", VARCHAR(105), comment="Tên tiếng Việt")

    other_value_flag = Column("OTHER_VALUE_FLAG", VARCHAR(1), comment='Giá trị khác, khi chọn vào thì chuyển qua nhập tay')

    display_order = Column("DISPLAY_ORDER", NUMBER(asdecimal=False), comment='Số thứ tự hiển thị')
