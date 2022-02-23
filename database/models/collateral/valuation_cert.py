from sqlalchemy import VARCHAR, Column, DateTime, Float
from sqlalchemy.dialects.oracle import NUMBER

from database.base import BaseModel


class CollPriceCert(BaseModel):
    __tablename__ = 'v_los_coll_price_cert'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin chứng thư thẩm định giá của tài sản.'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    collateral_id = Column(NUMBER(asdecimal=False), comment='Mã hồ sơ tài sản bảo đảm, tham chiếu qua bảng LOS_COLLATERAL')
    asset_block_flag = Column(VARCHAR(1), comment='Tài sản có hợp khối không (chỉ dành cho ts, bất động sản). Dữ liệu dạng Có / Không')
    re_status = Column(VARCHAR(50), comment='Trạng thái BĐS (chỉ dành cho bất động sản)')
    report_code = Column(VARCHAR(100), comment='Mã báo cáo / Chứng thư thảm định giá')
    published_at = Column(DateTime, comment='Thời điểm báo cáo / Chưng thư TĐ Giá')
    appraisal_unit_id = Column(VARCHAR(50),
                               comment='Đơn vị thực hiện thẩm định giá.\n'
                                       'Có 3 options:\n'
                                       '- Đơn vị kinh doanh (BRANCH_ID)\n'
                                       '- TT. TDTS Thực hiện thẩm định giá\n'
                                       '- Tổ chức định giá độc lập')
    branch_id = Column(VARCHAR(50), comment='Chi tiết đơn vị thẩm định giá cụ thể, có thể là đối tác, bên thứ ba hoặc SCB, tham chiếu qua các bảng tương ứng')
    appraisal_center_id = Column(VARCHAR(50), comment='TT Thẩm định Tài sản thực hiện thẩm định giá, tham chiếu qua bảng trung tâm thẩm định giá')
    appraisal_center_note = Column("appraisal_center_node", VARCHAR(200), comment='Ý kiến tái thẩm, tái định giá cả TT. TĐTS')
    appraisal_id = Column(VARCHAR(50), comment='Tổ chức định giá độc lập, tham chiếu qua bảng các tổ chức định giá độc lập')
    appraisal_unit_other = Column(VARCHAR(200), comment='Tổ chức độc lập khác, field đánh dấu, nếu YES thì lấy cái FIELD tổ chức định giá độc lập làm NAME')
    purpose_id = Column(VARCHAR(50), comment='Mục đích giá, tham chiếu qua bảng UDTM')
    purpose_other = Column(VARCHAR(200), comment='Mục đích khác, nếu trong trường hợp mục đích giá là khác, ghi thẳng value của mục đích giá khác vào đây')
    gross_asset_value = Column(Float, comment='Tổng giá trị tài sản bảo đảm theo chứng thư, tính tổng tự động')
    loan_to_value = Column(Float, comment='Tỷ lệ cho vay / Gía trị TSBD (%) Loan to Value: LTV')
    province_id = Column(VARCHAR(50), comment='Tình / TP Thẩm định (dùng cho tài sản không phải BĐS)')
    district_id = Column('distinct_id', VARCHAR(50), comment='Quận / Huyện Thẩm định (dùng cho tài sản không phải BĐS)')

    collateral_type_id = Column(VARCHAR(50), comment='Loại tài sản bảo đảm cấp 1')


class CollRe(BaseModel):
    __tablename__ = 'v_los_coll_re'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin chứng thư thẩm định giá của tài sản.'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    price_cert_id = Column(NUMBER(asdecimal=False), comment='Mã hồ sơ chứng thư định giá')
    address = Column(VARCHAR(200), comment='Địa chỉ thực tế')
    province_id = Column(VARCHAR(50), comment='Tỉnh/TP')
    district_id = Column(VARCHAR(50), comment='Quận/Huyện')
    ward_id = Column(VARCHAR(50), comment='Phường/ Xã')
    real_estate_position_type_id = Column(VARCHAR(50), comment='Loại vị trí')
    real_estate_position_type_other = Column(VARCHAR(200), comment='Loại vị trí khác')
    roadway_width = Column(VARCHAR(50), comment='Chiều rộng đường hiện hữu')
    description = Column(VARCHAR(300), comment='Tình / TP Thẩm định (dùng cho tài sản không phải BĐS)')
    order_display = Column(NUMBER(asdecimal=False), comment='Thứ tự sắp xếp hiển thị')


class CollPriceCertAsset(BaseModel):
    __tablename__ = 'v_los_coll_price_cert_asset'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin các tài sản được định giá trong chứng thư. Lưu trữ mã tài sản bảo đảm'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    price_cert_id = Column(NUMBER(asdecimal=False), comment='Mã hồ sơ chứng thư định giá')
    collateral_type_id = Column(VARCHAR(50),
                                comment='Mã loại tài sản cấp 2 của BDS,Phương tiện máy móc, Mã cấp 1 của các loại tài sản khác\n'
                                        '- Bất động sản:\n'
                                        '+ QSH là đất và/hoặc nhà riêng lẻ\n'
                                        '+ Quyền sở hữu căn hộ chung cư\n'
                                        '+ Quyền sở hữu sạp chợ/ Ô TTTM\n'
                                        '- Máy móc.\n'
                                        '- Nguồn lương\n'
                                        '- Giấy tờ có giá…. ')
    collateral_code = Column(VARCHAR(50), comment='Mã tài sản bảo đảm (đang đợi format tự động)')
    total_asset_value = Column(Float, comment='Tổng số tiền định giá theo tài sản')
    display_order = Column(NUMBER(asdecimal=False), comment='Thứ tự hiển thị ')


class CollPriceCertAssetAppraisal(BaseModel):
    __tablename__ = 'v_los_coll_price_cert_asset_appraisal'
    __table_args__ = {'comment': 'Bảng lưu trữ thông tin về thông tin định giá và thẩm định tài sản - Mục A'}

    id = Column(NUMBER(asdecimal=False), primary_key=True)
    price_cert_asset_id = Column(NUMBER(asdecimal=False), comment='Mã tài sản chi tiết trong bảng lưu trữ thông tin các tài sản bảo đảm (Bảng LOS_COLL_PRICE_CERT_ASSET)')
    asset_credit_flag = Column(VARCHAR(1))
    source_income_asset_flag = Column(VARCHAR(1), comment='Nguồn trả tiền nợ là nguôn tiền hình thành từ việc kinh doanh, khai thác chính TSBD')
    asset_used_loan_flag = Column(VARCHAR(1), comment='TS đang đảm bảo cho nghĩa vụ CTD')
    re_no_business_ratio = Column(Float, comment='Tỷ lệ diện tích BDS không kinh doanh')
    amount_loan_ratio = Column(Float, comment='Tỷ lệ cho vay tối đa theo quy định.')
    amount_value = Column(Float, comment='Giá trị QSD đất theo từng GCN (VNĐ)')
    description = Column(VARCHAR(200), comment='Thông tin nghĩa vụ bảo đảm')
