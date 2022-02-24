from sqlalchemy import CHAR, VARCHAR, Column, DateTime, Float, Integer, text
from sqlalchemy.dialects.oracle import VARCHAR2

from database import Base, BaseModel


class CountryManufacture(Base):
    __tablename__ = 'los_ma_coll_coun_manu'
    __table_args__ = {'comment': 'Nơi sản xuất'}

    country_code = Column(VARCHAR(3), primary_key=True)
    name = Column(VARCHAR(105), comment="Tên tiếng Việt")
    other_value_flag = Column(VARCHAR(1), comment='Giá trị khác, khi chọn vào thì chuyển qua nhập tay', server_default=text("""'N'"""))
    display_order = Column(Integer, comment='Số thứ tự hiển thị')


class MaAppraisalUnit(Base):
    __tablename__ = 'los_ma_appraisal_unit'
    __table_args__ = {'comment': 'Danh sách các tổ chức định giá độc lập và Trung tâm thẩm định giá'}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100), comment='Tên đơn vị định giá')
    description = Column(VARCHAR(100), comment='Diễn giải thêm thông tin')
    address = Column(VARCHAR(100), comment='Địa chỉ')
    province_id = Column(VARCHAR(100), comment='Tỉnh / Thành phố')
    district_id = Column(VARCHAR(100), comment='Quận / Huyện')
    ward_id = Column(VARCHAR(100), comment='Phường / Xã')
    tax = Column(VARCHAR(100), comment='Mã số thuế')
    cert_num = Column(VARCHAR(100), comment='Số giấy phép')
    appraisal_unit_type_id = Column(VARCHAR(100), comment='Loại hình (TT.TSTS hoặc TC Định giá độc lập), tham chiếu qua UDTM')
    display_order = Column(Integer)
    other_value_flag = Column(VARCHAR(1), server_default=text("'N'"))


class MaBankCode(Base):
    __tablename__ = 'ud_los_ma_bank_code'

    bank_code = Column("BANK_CODE", VARCHAR(10), primary_key=True)
    bank_name = Column("BANK_NAME", VARCHAR(100))
    bank_status = Column("BANK_STATUS", VARCHAR(1))
    bank_desc = Column("BANK_DESC", VARCHAR(100))
    bank_out = Column("BANK_OUT", VARCHAR(1))
    bank_quick = Column("BANK_QUICK", VARCHAR(1))


class MaBusinessLine(BaseModel):
    __tablename__ = 'los_ma_business_line'
    __table_args__ = {'comment': 'Bảng liên quan tới các nhóm ngành kinh doanh chính, sử dụng cho hộ kinh doanh. '}

    id = Column(CHAR(10), primary_key=True)
    business_name = Column(VARCHAR(255), comment='Nhóm ngành nghề kinh doanh')
    business_code = Column(VARCHAR(10), comment='Mã nhóm ngành nghề liên quan')


class MaBusinessType(Base):
    __tablename__ = 'los_ma_business_type'
    __table_args__ = {'comment': 'Loại hình doanh nghiệp. công ty'}

    id = Column("ID", VARCHAR(20), primary_key=True)

    name = Column("NAME", VARCHAR(100))

    sh = Column("SH", VARCHAR(1))


class MaCardPromotion(Base):
    __tablename__ = 'los_ma_card_promotion'
    __table_args__ = {'comment': 'Danh sách các khuyến mại cho thẻ'}

    id = Column("ID", Integer, primary_key=True)

    name = Column("NAME", VARCHAR(100), comment='Thông tin - tiêu đề, vali, miễn phí phí thường niên năm đầu')

    description = Column("DESCRIPTION", VARCHAR(200))


class MaCicScore(Base):
    __tablename__ = 'los_ma_cic_score'
    __table_args__ = {'comment': 'Bảng ghi lại thông tin về điểm và hạng của CIC cho khách hàng vay tín dụng, có thể thay đổi theo thời gian'}

    id = Column("ID", Integer, primary_key=True)
    version = Column("VERSION", VARCHAR(50), comment='Theo công văn số, quyết định số nào của CIC')
    start_time = Column("START_TIME", DateTime, comment='Thời gian bắt đầu')
    end_time = Column("END_TIME", DateTime,
                      comment='Thời gian kết thúc, nếu bỏ trống thì active_flag = Y, đánh dấu đang sử dụng')
    description = Column("DESCRIPTION", VARCHAR(100))
    actived_flag = Column("ACTIVED_FLAG", VARCHAR(1), comment='Cờ đánh dấu đang kích hoạt, hay là cái mới nhất')


class MaCicScoreDetail(Base):
    __tablename__ = 'los_ma_cic_score_detail'
    __table_args__ = {'comment': 'Bảng chi tiết và điểm hạng của CIC'}

    id = Column("ID", Integer, primary_key=True)
    cic_score_rank = Column("CIC_SCORE_RANK", VARCHAR(20), comment='Tham chiếu qua bảng UDTM')
    min_score = Column("MIN_SCORE", Integer, comment='Điểm cận dưới')
    max_score = Column("MAX_SCORE", Integer, comment='Điểm cận trên')
    cic_score_rank_score = Column("CIC_SCORE_RANK_SCORE", VARCHAR(10),
                                  comment='Tham chiếu bảng UDTM, điểm hạng 10,9,8.... Mỗi range sẽ có khung điểm')
    cic_score_id = Column("CIC_SCORE_ID", Integer, comment='Tham chiếu qua bảng MA_CIC_SCORE')


class MaCollType(Base):
    __tablename__ = 'los_ma_coll_type'
    __table_args__ = {'comment': 'Danh mục tài sản bảo đảm'}

    id = Column(VARCHAR(10), primary_key=True)
    name = Column(VARCHAR(100))
    parent_id = Column(VARCHAR(10))
    lev = Column(Integer, comment='Thứ tự sắp cha con dùng nhanh khi search')
    display_order = Column(Integer, comment='Thứ tự hiển thị')


class LosMaCollTransType(Base):
    __tablename__ = 'los_ma_coll_trans_type'
    __table_args__ = {"comment": 'Danh sách các phương tiện phận tải chi tiết dùng cho mục định giá'}

    trans_type_id = Column('TRANS_TYPE_ID', VARCHAR(100), comment='Loại hình phương tiện vận tải tham chiếu vào bảng MA_COLL_TYPE')
    trans_name = Column('TRANS_NAME', VARCHAR(100), comment='Chi tiết tên loại hình con', primary_key=True)
    other_value_flag = Column('OTHER_VALUE_FLAG', VARCHAR(1), comment='Giá trị khác, khi chọn vào thì chuyển qua nhập tay')


class MaCostType(Base):
    __tablename__ = 'los_ma_cost_type'
    __table_args__ = {'comment': 'Loại chi phí'}

    id = Column(VARCHAR(30), primary_key=True)
    name = Column(VARCHAR(100))
    is_loan_required = Column(VARCHAR(1), comment='Nếu dùng cho vay thường thì đánh dấu Y')
    is_credit_required = Column(VARCHAR(1), comment='Nếu dùng cho vay thẻ thì đánh dấu Y')
    display_order = Column(Integer, comment='Thứ tự hiển thị (mặc định dùng cho vay thẻ) ')


class MaCreditCard(Base):
    __tablename__ = 'los_ma_credit_card'
    __table_args__ = {'comment': 'Bảng danh sách các loại thẻ tín dụng'}

    id = Column("ID", VARCHAR(20), primary_key=True)
    card_group_id = Column("CARD_GROUP_ID", VARCHAR(100), comment='Nhóm thẻ master, visa, credit....')
    card_name = Column("CARD_NAME", VARCHAR(100), comment='Tên thẻ vàng, bạc, chuẩn')
    is_published_flag = Column("IS_PUBLISHED_FLAG", VARCHAR(1), comment='Thẻ dành cho mở thẻ chính')
    is_supp_flag = Column("IS_SUPP_FLAG", VARCHAR(1), comment='Thẻ dành cho mở thẻ phụ')
    actived_flag = Column("ACTIVED_FLAG", VARCHAR(1))


class MaCreditProductCard(Base):
    __tablename__ = 'los_ma_credit_product_card'
    __table_args__ = {
        'comment': 'Bảng mapping các nhóm thẻ và các sản phẩm vay để biết nếu vay theo đối tượng nào sẽ được dùng những loại thẻ nào'}

    id = Column("ID", Integer, primary_key=True)
    credit_card_id = Column("CREDIT_CARD_ID", VARCHAR(20), comment='Loại thẻ tham chiếu qua bảng LOS_MA_CREDIT_CARD')
    loan_product_id = Column("LOAN_PRODUCT_ID", VARCHAR(20), comment='Mã sản phẩm')
    display_order = Column("DISPLAY_ORDER", Integer)
    actived_flag = Column("ACTIVED_FLAG", VARCHAR(1))


class MaCustomerType(Base):
    __tablename__ = 'los_ma_customer_type'
    __table_args__ = {'comment': 'Danh mục khách hàng'}

    id = Column("ID", VARCHAR2(10), primary_key=True)

    name = Column("NAME", VARCHAR2(50), comment='Tên nhóm khách hàng , cá nhân hay doanh nghiệp')


class MaDocumentType(BaseModel):
    __tablename__ = 'los_ma_document_type'
    __table_args__ = {'comment': 'Danh mục các loại tài liệu, hồ sơ văn bản cần phải có trong các step thực hiện'}

    id = Column('ID', Integer, primary_key=True)
    name = Column('NAME', VARCHAR(100), comment='Tên, tiêu đề của văn loại hình')
    description = Column('DESCRIPTION', VARCHAR(500), comment='Diễn giải chi tiết hơn về loại văn bản')
    document_group_type = Column('DOCUMENT_GROUP_TYPE', VARCHAR(100), comment='Nhóm tài liệu tham chiếu qua UDTM')
    actived_flag = Column('ACTIVED_FLAG', VARCHAR(1), comment='Kích hoạt hoặc không')
    ext_1 = Column('EXT_1', VARCHAR(100), comment='Dữ trữ')
    ext_2 = Column('EXT_2', VARCHAR(100), comment='Dữ trữ')
    parent_id = Column('PARENT_ID', Integer)
    loan_category_id = Column('LOAN_CATEGORY_ID', VARCHAR(20), comment='Vay thường hoặc vay thẻ')
    credit_card_type = Column('CREDIT_CARD_TYPE', VARCHAR(20), comment='Dành cho vay thẻ (Thông tin pháp lý). Để phân biệt tài liệu chủ thẻ chính và người hôn phối')


class MaFrequence(BaseModel):
    __tablename__ = 'los_ma_frequence'
    __table_args__ = {'comment': 'Ghi lại nhóm thu nhập nào và tần suất thu nhập để tính ra giá trị phần trăm thu nhập'}

    id = Column("ID", Integer, primary_key=True)
    frequence_type = Column("FREQUENCE_TYPE", Integer)
    income_group_type = Column("INCOME_GROUP_TYPE", Integer)
    income_ratio = Column("INCOME_RATIO", Float)


class MaCreditGroupCustomer(Base):
    __tablename__ = 'los_ma_credit_group_cust'
    __table_args__ = {'comment': 'Lưu trữ thông tin về đối tượng vay vốn, sử dụng cho hồ sơ vay thẻ'}

    id = Column("ID", Integer, primary_key=True)
    name = Column("NAME", VARCHAR(200), comment='Tên,  tiêu đề đối tượng vay vốn')
    description = Column("DESCRIPTION", VARCHAR(300), comment='Diễn giải chi tiết đối tượng')


class MaCreditGroupCustomerItem(Base):
    __tablename__ = 'los_ma_credit_group_cust_item'
    __table_args__ = {'comment': 'Bảng mô tả thông tin các đối tượng cho vay thẻ'}

    id = Column("ID", Integer, primary_key=True)
    credit_group_cust_id = Column("CREDIT_GROUP_CUST_ID", Integer, comment='Mã đối tượng tham chiếu qua bảng LOS_MA_CREDIT_GROUP_CUST')
    credit_obj_reference_id = Column("CREDIT_OBJ_REFERENCE_ID", VARCHAR(100), comment='Diễn giải chi tiết đối tượng')
    label = Column("LABEL", VARCHAR(50), comment='Diễn giải chi tiết đối tượng')
    name = Column("NAME", VARCHAR(150), comment='Diễn giải chi tiết đối tượng')
    droplist_item = Column("DROPLIST_ITEM", VARCHAR(100), comment='Giá trị là sử dụng cho select, radio')
    default_value = Column("DEFAULT_VALUE", VARCHAR(100), comment='Giá trị mặc định')
    is_numberic = Column("IS_NUMBERIC", VARCHAR(1), comment='Dữ liệu là dạng số')
    edit_able_flag = Column("EDIT_ABLE_FLAG", VARCHAR(1), comment='Cho phép chỉnh sửa dữ liệu')
    required_flag = Column("REQUIRED_FLAG", VARCHAR(1), comment='Dữ liệu y/c phải nhập liệu')
    display_order = Column("DISPLAY_ORDER", Integer, comment='Thứ tự hiển thị')
    calculation = Column("CALCULATION", VARCHAR(4000), comment='Công thức tính hoặc điều kiện')
    code = Column("CODE", VARCHAR(50), comment='Mã')
    component = Column("COMPONENT", VARCHAR(20), comment='Diễn giải chi tiết đối tượng')
    min = Column("MIN", Integer)
    max = Column("MAX", Integer)
    level = Column("LEVEL", Integer, default=0)
    is_parent_flag = Column("IS_PARENT_FLAG", CHAR(1))
    parent_id = Column("PARENT_ID", Integer)
    table = Column("TABLE", VARCHAR(50))
    loan_product_id = Column('LOAN_PRODUCT_ID', VARCHAR(20), comment='Mã sản phẩm')
    params = Column('PARAMS', VARCHAR(500), comment='Danh sách đối tượng tryền vào để tính toán')
    object_id = Column('OBJECT_ID', VARCHAR(10), comment='Đối tượng để tính toán')
    display_order_calculation = Column("DISPLAY_ORDER_CALCULATION", Integer, comment='Thứ tự hiển thị để tính toán theo công thức')
    calculation_type = Column("CALCULATION_TYPE", VARCHAR(30), comment='Loại công thức tính dữ liệu')
    droplist_item_condition = Column('DROPLIST_ITEM_CONDITION', VARCHAR(100), comment='Điều kiện loại bỏ dữ liệu cho select')
    info_type = Column('INFO_TYPE', VARCHAR(30), comment='Phân biệt thông tin chi tiết và thông tin tiêu chí')
    calculation_flag = Column("CALCULATION_FLAG", CHAR(1), comment='Khi thay đổi sẽ call api để tính toán cho các item khác.')
    field_type = Column("FIELD_TYPE", VARCHAR(50), comment='Phân biệt field item: Hạn mức tối đa theo đối tượng, Hạn mức tổng đơn vị đề, ...')
    value_flag = Column("VALUE_FLAG", VARCHAR(1), comment='Lấy dữ liệu FE gửi lên (field value hoặc field code)')


class MaCollMachineLegal(Base):
    __tablename__ = 'los_ma_coll_machine_legal'
    __table_args__ = {'comment': 'Danh mục hồ sơ pháp lý của TSBD là Thiết bị máy móc'}

    id = Column(VARCHAR(20), primary_key=True)
    name = Column(VARCHAR(100))
    parent_id = Column(VARCHAR(100))
    LEVEL = Column(VARCHAR(100))
    display_order = Column(Integer)
    other_value_flag = Column(VARCHAR(2), comment='Giá trị khác, khi chọn vào thì chuyển qua nhập tay')


class MaPersonalRep(Base):
    __tablename__ = 'los_ma_personal_rep'
    __table_args__ = {'comment': 'Personal representative Danh mục người đại điện như người vay hôn phối....'}

    id = Column(VARCHAR(20), primary_key=True)
    name = Column(VARCHAR(100))
    description = Column(VARCHAR(100))
    created_at = Column(DateTime)
    created_by = Column(VARCHAR(20))
    modified_at = Column(DateTime)
    modified_by = Column(VARCHAR(20))
    is_default = Column(VARCHAR(1), server_default=text("'N'"))
    display_order = Column(Integer)
    loan_category_id = Column(VARCHAR(20), nullable=False)
    actived_flag = Column(VARCHAR(1))


class MaQuestion(BaseModel):
    __tablename__ = 'los_ma_question'
    __table_args__ = {'comment': 'Danh sách các câu hỏi xác thực'}

    id = Column('ID', Integer, primary_key=True)
    name = Column('NAME', VARCHAR(100))
    question_type = Column('QUESTION_TYPE', VARCHAR(10), comment='Loại câu hỏi, dùng để gom nhóm, tham chiếu qua bên UDTM')
    actived_flag = Column('ACTIVED_FLAG', VARCHAR(1))
    display_order = Column('DISPLAY_ORDER', Integer)
