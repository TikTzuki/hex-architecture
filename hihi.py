# coding: utf-8
from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()
metadata = BaseModel.metadata

t_los_ma_business_type = Table(
    'los_ma_business_type', metadata,
    Column('id', VARCHAR(10)),
    Column('name', VARCHAR(100)),
    Column('sh', VARCHAR(1)),
    comment='Loại hình doanh nghiệp. công ty'
)

t_los_ma_card_promotion = Table(
    'los_ma_card_promotion', metadata,
    Column('id', Integer, nullable=False),
    Column('name', VARCHAR(100), comment='Thông tin - tiêu đề, vali, miễn phí phí thường niên năm đầu'),
    Column('description', VARCHAR(200)),
    comment='Danh sách các khuyến mại cho thẻ'
)

t_los_ma_cic_score = Table(
    'los_ma_cic_score', metadata,
    Column('id', Integer, nullable=False),
    Column('version', VARCHAR(50), comment='Theo công văn số, quyết định số nào của CIC'),
    Column('start_time', DateTime, comment='Thời gian bắt đầu'),
    Column('end_time', DateTime, comment='Thời gian kết thúc, nếu bỏ trống thì active_flag = Y, đánh dấu đang sử dụng'),
    Column('description', VARCHAR(100)),
    Column('actived_flag', VARCHAR(1), comment='Cờ đánh dấu đang kích hoạt, hay là cái mới nhất'),
    comment='Bảng ghi lại thông tin về điểm và hạng của CIC cho khách hàng vay tín dụng, có thể thay đổi theo thời gian'
)

t_los_ma_cic_score_detail = Table(
    'los_ma_cic_score_detail', metadata,
    Column('id', Integer, nullable=False),
    Column('cic_score_rank', VARCHAR(20), comment='Tham chiếu qua bảng UDTM'),
    Column('min_score', Integer, comment='Điểm cận dưới'),
    Column('max_score', Integer, comment='Điểm cận trên'),
    Column('cic_score_rank_score', VARCHAR(10), comment='Tham chiếu bảng UDTM, điểm hạng 10,9,8.... Mỗi range sẽ có khung điểm'),
    Column('cic_score_id', Integer, comment='Tham chiếu qua bảng MA_CIC_SCORE'),
    comment='Bảng chi tiết và điểm hạng của CIC,'
)

t_los_ma_coll_trans_type = Table(
    'los_ma_coll_trans_type', metadata,
    Column('trans_type_id', VARCHAR(100), comment='Loại hình phương tiện vận tải tham chiếu vào bảng MA_COLL_TYPE'),
    Column('trans_name', VARCHAR(100), comment='Chi tiết tên loại hình con'),
    Column('other_value_flag', VARCHAR(1), server_default=text("'N'")),
    comment='Danh sách các phương tiện phận tải chi tiết dùng cho mục định giá'
)

t_los_ma_credit_card = Table(
    'los_ma_credit_card', metadata,
    Column('id', VARCHAR(20)),
    Column('card_group_id', VARCHAR(100), comment='Nhóm thẻ master, visa, credit....'),
    Column('card_name', VARCHAR(100), comment='Tên thẻ vàng, bạc, chuẩn'),
    Column('is_published_flag', VARCHAR(1), comment='Thẻ dành cho mở thẻ chính'),
    Column('is_supp_flag', VARCHAR(1), comment='Thẻ dành cho mở thẻ phụ'),
    Column('actived_flag', VARCHAR(1)),
    comment='Bảng danh sách các loại thẻ tín dụng'
)

t_los_ma_credit_group_cust = Table(
    'los_ma_credit_group_cust', metadata,
    Column('id', Integer, nullable=False),
    Column('name', VARCHAR(200), comment='Tên,  tiêu đề đối tượng vay vốn'),
    Column('description', VARCHAR(300), comment='Diễn giải chi tiết đối tượng'),
    comment='Lưu trữ thông tin về đối tượng vay vốn, sử dụng cho hồ sơ vay thẻ'
)

t_los_ma_credit_group_cust_item = Table(
    'los_ma_credit_group_cust_item', metadata,
    Column('id', Integer, nullable=False),
    Column('credit_group_cust_id', NUMBER(asdecimal=False), comment='Mã đối tượng tham chiếu qua bảng LOS_MA_CREDIT_GROUP_CUST'),
    Column('credit_obj_reference_id', VARCHAR(100)),
    Column('label', VARCHAR(50)),
    Column('name', VARCHAR(150)),
    Column('droplist_item', VARCHAR(100), comment='Giá trị là sử dụng cho select, radio'),
    Column('default_value', VARCHAR(100), comment='Giá trị mặc định'),
    Column('is_numberic', VARCHAR(1), comment='Dữ liệu là dạng số'),
    Column('edit_able_flag', VARCHAR(1), comment='Cho phép chỉnh sửa dữ liệu'),
    Column('required_flag', VARCHAR(1), comment='Dữ liệu y/c phải nhập liệu'),
    Column('display_order', Integer, comment='Thứ tự hiển thị'),
    Column('calculation', VARCHAR(4000), comment='Công thức tính hoặc điều kiện'),
    Column('code', VARCHAR(50), comment='Mã'),
    Column('component', VARCHAR(20)),
    Column('min', Integer),
    Column('max', Integer),
    Column('LEVEL', Integer, server_default=text("0")),
    Column('is_parent_flag', CHAR(1)),
    Column('parent_id', Integer),
    Column('TABLE', VARCHAR(50)),
    Column('loan_product_id', VARCHAR(20), comment='Mã sản phẩm'),
    Column('params', VARCHAR(500), comment='Danh sách đối tượng tryền vào để tính toán'),
    Column('object_id', VARCHAR(10), comment='Đối tượng để tính toán'),
    Column('display_order_calculation', NUMBER(asdecimal=False), comment='Thứ tự để tính toán theo công thức'),
    Column('calculation_type', VARCHAR(30), comment='Loại công thức tính dữ liệu'),
    Column('droplist_item_condition', VARCHAR(100), comment='Điều kiện loại bỏ dữ liệu cho select'),
    Column('info_type', VARCHAR(30), comment='Phân biệt thông tin chi tiết và thông tin tiêu chí'),
    Column('calculation_flag', VARCHAR(1), comment='Khi thay đổi sẽ call api để tính toán cho các item khác.'),
    Column('field_type', VARCHAR(50), comment='Phân biệt field item: Hạn mức tối đa theo đối tượng, Hạn mức tổng đơn vị đề '),
    Column('value_flag', VARCHAR(1), comment='Lấy dữ liệu FE gửi lên (field value hoặc field code)'),
    comment='Bảng mô tả thông tin các đối tượng cho vay thẻ'
)

t_los_ma_credit_product_card = Table(
    'los_ma_credit_product_card', metadata,
    Column('id', Integer, nullable=False),
    Column('credit_card_id', VARCHAR(20), comment='Loại thẻ tham chiếu qua bảng LOS_MA_CREDIT_CARD'),
    Column('loan_product_id', VARCHAR(20), comment='Mã sản phẩm'),
    Column('display_order', Integer),
    Column('actived_flag', VARCHAR(1)),
    comment='Bảng mapping các nhóm thẻ và các sản phẩm vay để biết nếu vay theo đối tượng nào sẽ được dùng những loại thẻ nào'
)

t_los_ma_customer_type = Table(
    'los_ma_customer_type', metadata,
    Column('id', VARCHAR(10)),
    Column('name', VARCHAR(50), comment='Tên nhóm khách hàng , cá nhân hay doanh nghiệp'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    comment='Danh mục khách hàng'
)

t_los_ma_document_type = Table(
    'los_ma_document_type', metadata,
    Column('id', Integer, nullable=False),
    Column('name', VARCHAR(100), comment='Tên, tiêu đề của văn loại hình'),
    Column('description', VARCHAR(500), comment='Diễn giải chi tiết hơn về loại văn bản'),
    Column('document_group_type', VARCHAR(100), comment='Nhóm tài liệu tham chiếu qua UDTM'),
    Column('actived_flag', VARCHAR(1), comment='Kích hoạt hoặc không'),
    Column('ext_1', VARCHAR(100), comment='Dữ trữ'),
    Column('ext_2', VARCHAR(100), comment='Dữ trữ'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    Column('parent_id', NUMBER(asdecimal=False)),
    Column('loan_category_id', VARCHAR(20), comment='Vay thường hoặc vay thẻ'),
    Column('credit_card_type', VARCHAR(20), comment='Dành cho vay thẻ (Thông tin pháp lý). Để phân biệt tài liệu chủ thẻ chính và người hôn phối'),
    comment='Danh mục các loại tài liệu, hồ sơ văn bản cần phải có trong các step thực hiện'
)

t_los_ma_frequence = Table(
    'los_ma_frequence', metadata,
    Column('id', Integer),
    Column('frequence_type', Integer, comment='Tần suất thu nhập '),
    Column('income_group_type', Integer, comment='Nhóm thu nhập '),
    Column('income_ratio', Float, comment='Giá trị % của nhóm thu nhập với tần suất'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Ghi lại nhóm thu nhập nào và tần suất thu nhập để tính ra giá trị phần trăm thu nhập'
)

t_los_ma_question = Table(
    'los_ma_question', metadata,
    Column('id', NUMBER(38, 0, False), nullable=False),
    Column('name', VARCHAR(100)),
    Column('question_type', VARCHAR(10), comment='Loại câu hỏi, dùng để gom nhóm, tham chiếu qua bên UDTM'),
    Column('actived_flag', VARCHAR(1)),
    Column('display_order', Integer),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Danh sách các câu hỏi xác thực'
)

t_los_partner = Table(
    'los_partner', metadata,
    Column('id', VARCHAR(10)),
    Column('name', VARCHAR(100), comment='Tên đối tác'),
    Column('tax', VARCHAR(20)),
    Column('phone', VARCHAR(30)),
    Column('address', VARCHAR(50)),
    Column('ward_id', VARCHAR(20)),
    Column('district_id', VARCHAR(10)),
    Column('province_id', VARCHAR(20)),
    Column('email', VARCHAR(50)),
    Column('website', VARCHAR(100)),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Danh sách các đối tác'
)

t_los_partner_loan_product = Table(
    'los_partner_loan_product', metadata,
    Column('id', Integer, nullable=False),
    Column('partner_id', VARCHAR(20), comment='Mã đối tác'),
    Column('loan_product_id', VARCHAR(100), comment='Mã sản phẩm vay của SCB'),
    Column('display_order', Integer),
    Column('actived_flag', VARCHAR(2)),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Bảng liên kết của các sản phẩm vay (của SCB) cho các Đối tác'
)

t_los_partner_product = Table(
    'los_partner_product', metadata,
    Column('id', Integer, nullable=False),
    Column('partner_id', VARCHAR(20), comment='Mã đối tác'),
    Column('name', VARCHAR(100), comment='Tên sản phẩm của đố tác'),
    Column('description', VARCHAR(100)),
    Column('actived_flag', VARCHAR(1)),
    Column('display_order', Integer, comment='Thứ tự hiển thị sản phẩm'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(100)),
    comment='Danh sách các sản phẩm của riêng đối tác.'
)

t_los_person_credit_score = Table(
    'los_person_credit_score', metadata,
    Column('id', Integer, nullable=False),
    Column('personal_identity_id', NUMBER(asdecimal=False)),
    Column('los_id', VARCHAR(100), comment='Mã hồ sơ vay vốn'),
    Column('score_value', Integer, comment='Điểm tín dụng'),
    Column('score_rank', VARCHAR(10), comment='Hạng'),
    Column('publish_date', DateTime, comment='Ngày chấm điểm'),
    Column('evaluation', Float, comment='Điểm đánh giá tín dụng (%)'),
    Column('uuid', VARCHAR(50)),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    comment='Thông tin điểm tín dụng CIC của một khách hàng - theo giấy tờ tùy thân'
)

t_los_person_credit_score_segment = Table(
    'los_person_credit_score_segment', metadata,
    Column('id', Integer, nullable=False),
    Column('credit_score_id', Integer, comment='Tham chiếu qua bảng LOS_PERSON_CREDIT_SCORE'),
    Column('cic_cus_segment', VARCHAR(10), comment='Tham chiếu qua bảng UDTM'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Bảng phân loại khách hàng theo CIC đánh giá'
)

t_los_product_document_rule = Table(
    'los_product_document_rule', metadata,
    Column('id', Integer, nullable=False),
    Column('product_loan_id', Integer, comment='Mã sản phẩm vay vốn'),
    Column('document_group_type', VARCHAR(75), comment='Nhóm tài liệu cần phải có (tham chiếu trong bảng udtm )'),
    Column('document_type_id', Integer, comment='Chỉ định tài liệu cụ thể phải có trong hồ sơ, cho phép null, nếu giá trị là null thì chỉ cần có 1 tài liệu trong nhóm là được'),
    Column('required_flag', VARCHAR(2), comment='Chỉ định bắt buộc phải có hoặc không'),
    Column('actived_flag', VARCHAR(2), comment='Kích hoạt hay không'),
    Column('ext_1', VARCHAR(100), comment='Dự trữ'),
    Column('ext_2', VARCHAR(100), comment='Dữ trữ field'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Danh sách các hồ sơ pháp lý phải có theo quy định của sản phẩm.'
)

t_los_product_promotion = Table(
    'los_product_promotion', metadata,
    Column('id', Integer, nullable=False),
    Column('loan_product_id', VARCHAR(20), comment='Mã sản phẩm vay'),
    Column('gift_promotion_id', Integer, comment='Mã khuyến mại'),
    Column('display_order', Integer, comment='Thứ tự hiển thị'),
    Column('status_flag', VARCHAR(1), server_default=text("'Y'"), comment='Kích hoạt / không kích hoạt'),
    comment='Danh sách các khuyến mai đi theo sản phẩm.'
)

t_los_product_question = Table(
    'los_product_question', metadata,
    Column('id', Integer),
    Column('loan_product_id', VARCHAR(20), comment='Mã sản phẩm'),
    Column('question_id', Integer, comment='Mã câu hỏi'),
    Column('display_order', Integer, comment='Thứ tự câu hỏi hiển thị'),
    Column('required_flag', VARCHAR(1), comment='Yêu cầu phải nhập dữ liệu'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Danh sách tương ứng mỗi sản phẩm vay sẽ có những câu hỏi nào'
)

t_los_profile_answer_cust = Table(
    'los_profile_answer_cust', metadata,
    Column('id', Integer, nullable=False),
    Column('los_profile_id', VARCHAR(20), comment='Mã hồ sơ vay vốn'),
    Column('profile_question_id', Integer, comment='Mã câu hỏi theo hồ sơ'),
    Column('answer', VARCHAR(100), comment='Câu trả lời của khách hàng'),
    Column('person_id', NUMBER(asdecimal=False), comment='Người trả lời câu hỏi (Chủ thẻ chính, chủ thẻ phụ, ...)'),
    Column('actived_flag', VARCHAR(1), comment='Trạng thái chấp nhận câu trả lời'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Danh sách câu trả lời cho hồ sơ vay vốn của khách hàng'
)

t_los_profile_credit_card_delivery = Table(
    'los_profile_credit_card_delivery', metadata,
    Column('id', Integer, nullable=False),
    Column('credit_published_id', Integer, comment='Tham chiếu tới bảng thẻ chính'),
    Column('card_delivery_method', VARCHAR(20), comment='Phương thức giao thẻ'),
    Column('branch_id', VARCHAR(100), comment='Tham chiếu vào bảng SCB để biết branch nào'),
    Column('address', VARCHAR(100)),
    Column('province_id', VARCHAR(6)),
    Column('district_id', VARCHAR(6)),
    Column('ward_id', VARCHAR(6)),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Bảng ghi nhận thông tin hình thức giao thẻ'
)

t_los_profile_credit_modified = Table(
    'los_profile_credit_modified', metadata,
    Column('id', Integer),
    Column('profile_credit_sequence_id', Integer, comment='Mã hồ sơ vay vốn'),
    Column('person_credit_card_id', VARCHAR(100), comment='Mã thẻ của khách hàng cần điều chỉnh thay đổi.'),
    Column('card_category_id', VARCHAR(10), comment='Hạng thẻ. loại thẻ cần nâng cấp'),
    Column('credit_limit', Float, comment='Hạn mức của thẻ cần nâng cấp'),
    Column('card_color_id', VARCHAR(10), comment='Thay đổi màu thẻ'),
    Column('security_interests_type', VARCHAR(10), comment='Hình thức bảo đảm thẻ được thay đổi'),
    Column('security_interests_flag', VARCHAR(1), comment='Đánh dấu có thay đổi hình  thức bảo đảm thẻ không'),
    Column('credit_card_type', VARCHAR(10), comment='Thay đổi thẻ chính thức/hay thẻ tạm thời'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Bảng lưu hồ sơ thay đổi hạn mức thẻ/thay đổi hình thức bảo đảm thẻ'
)

t_los_profile_credit_promotion = Table(
    'los_profile_credit_promotion', metadata,
    Column('id', Integer, nullable=False),
    Column('credit_published_id', Integer),
    Column('profile_credit_promotion_id', Integer),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50))
)

t_los_profile_credit_published = Table(
    'los_profile_credit_published', metadata,
    Column('id', Integer),
    Column('card_category_id', VARCHAR(10), comment='Loại thẻ, master card, visa....'),
    Column('credit_limit', Float, comment='Hạn mức của thẻ'),
    Column('promotion_id', Integer, comment='Thông tin lựa chọn quà tặng'),
    Column('profile_credit_sequence_id', VARCHAR(100), comment='Mã hồ sơ vay'),
    Column('embossed_card_first_name', VARCHAR(100), comment='Tên dập nổi Tên'),
    Column('embossed_card_middle_name', VARCHAR(100), comment='Tên đệm dập nổi'),
    Column('embossed_card_last_name', VARCHAR(100), comment='Tên dập nổi họ'),
    Column('gift_received_flag', VARCHAR(1), comment='Đủ điều kiện nhận quà không - tham chiếu Y/N trong UDTM'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    Column('payment_method_type_id', VARCHAR(50), comment='Hình thức thanh toán dự nợ (PAYMENT_METHOD_TYPE), link sang bảng UDTM các giá trị.'),
    Column('debt_deduction_account', VARCHAR(200), comment='Tài khoản dùng trích nợ, sẽ móc nối với các system khác để fill giá trị mỗi lần chạy, hiện tại setup sẵn, chưa sử dụng được'),
    comment='Hồ sơ vay cho việc phát hành thẻ mới.'
)

t_los_profile_credit_supp_card = Table(
    'los_profile_credit_supp_card', metadata,
    Column('id', Integer, nullable=False),
    Column('profile_credit_published_id', VARCHAR(100), comment='Mã hồ sơ thẻ chính'),
    Column('los_person_id', VARCHAR(20), comment='Hồ sơ người được tạo thẻ'),
    Column('card_category_id', VARCHAR(10), comment='Loại thẻ'),
    Column('card_color_id', Integer, comment='Màu thẻ'),
    Column('credit_limit', Float, comment='Hạn mức thẻ'),
    Column('embossed_card_first_name', VARCHAR(100), comment='Tên dập nổi Tên'),
    Column('gift_received_flag', VARCHAR(1), comment='Đủ điều kiện nhận quà không - tham chiếu Y/N trong UDTM'),
    Column('embossed_card_middle_name', VARCHAR(100), comment='Tên đệm dập nổi'),
    Column('embossed_card_last_name', VARCHAR(100), comment='Tên dập nổi họ'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Bảng lưu trữ dữ liệu tạo thẻ phụ - trong hồ sơ vay'
)

t_los_profile_cust_group_item = Table(
    'los_profile_cust_group_item', metadata,
    Column('id', Integer, nullable=False),
    Column('cust_group_id', Integer, comment='Tham chiếu qua bảng MA_CUST_GROUP_ID'),
    Column('cust_group_item_value', VARCHAR(100), comment='Giá trị của từng item đối tượng'),
    Column('profile_credit_sequence_id', Integer, comment='Tham chiếu qua bảng LOS_PROFILE_CREDIT_SEQUENCE'),
    Column('cust_group_item_id', NUMBER(asdecimal=False), comment='Tham chiếu qua bảng MA_CUST_GROUP_ITEM_ID'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    comment='Lưu lại thông tin mở thẻ theo đối tượng'
)

t_los_profile_document = Table(
    'los_profile_document', metadata,
    Column('id', Integer, nullable=False),
    Column('los_profile_id', VARCHAR(20), comment='Hồ sơ vay vốn'),
    Column('los_person_id', VARCHAR(20), comment='Hồ sơ thuộc về người nào theo ID'),
    Column('file_extension', VARCHAR(200), comment='Định dạng file'),
    Column('file_url', VARCHAR(300), comment='URL liên kết với DMS'),
    Column('display_order', Integer, comment='Thứ tự hiển thị (mặc định = 1)'),
    Column('actived_flag', VARCHAR(1)),
    Column('document_type_id', VARCHAR(75), comment='Nhóm tài liệu theo loại loại hồ sơ, CMND, CIC, Tài sản bảo đảm, Nguồn thu nhập'),
    Column('relationship_type', VARCHAR(75), comment='Quan hệ với người vay, chinh chủ, hôn phối, đồng vay đồng trả nợ (hỗ trợ truy vấn nhanh)/'),
    Column('sequence', Integer, comment='Số tăng tự động để làm thông tin version (mặc định bằng = 1)'),
    Column('owner_input_type', VARCHAR(10), comment='Phân biệt hồ sơ này là do bên nào cung cấp, khách hàng hay SCB (tham chiếu trong bảng udtm )'),
    Column('note', VARCHAR(500), comment='Ghi chú về thông tin hồ sơ này'),
    Column('ext_1', VARCHAR(100)),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(100)),
    comment='Danh mục tài liệu, hồ sơ trong một hồ sơ vay vốn'
)

t_los_profile_score = Table(
    'los_profile_score', metadata,
    Column('id', Integer),
    Column('los_sequence_id', Integer, comment='Link tới table LOS_PROFILE_SEQUENCE_ITEM'),
    Column('score', Float, comment='Tổng điểm của hồ sơ'),
    Column('score_rank_type', VARCHAR(20), comment='Hạng của hồ sơ'),
    Column('approval_date', DateTime, comment='Thời gian phê duyệt điểm trên hồ sơ'),
    Column('description', VARCHAR(500), comment='Ghi chú'),
    Column('department_id', VARCHAR(10), comment='Bộ phận đánh giá điểm (NVKD, Cấp Phê Duyệt, QLRR)'),
    Column('display_order', Integer, comment='Thứ tự xuất hiện'),
    Column('los_score_fcc', VARCHAR(20), comment='Mã hồ sơ xếp hạng tín dụng nội bộ (chưa sử dụng)'),
    Column('created_at', DateTime),
    Column('created_by', VARCHAR(20)),
    Column('modified_at', DateTime),
    Column('modified_by', VARCHAR(20)),
    Column('uuid', VARCHAR(50)),
    Column('los_credit_sequence_id', NUMBER(asdecimal=False), comment='Link tới table LOS_PROFILE_CREDIT_SEQUENCE_ITEM'),
    comment='Bảng ghi nhận điểm XHTDNB của một hồ sơ.'
)

t_ud_los_getm_coll_category = Table(
    'ud_los_getm_coll_category', metadata,
    Column('id', NUMBER(20, 0, False)),
    Column('category_name', VARCHAR(50)),
    Column('description', VARCHAR(105)),
    Column('coll_type_id', NUMBER(20, 0, False)),
    Column('category_type', VARCHAR(1)),
    Column('secured', VARCHAR(1)),
    Column('review_date', DateTime),
    Column('tangible', VARCHAR(1)),
    Column('reval_frequency', VARCHAR(50)),
    Column('reval_due_date', NUMBER(3, 0, False)),
    Column('reval_start_month', VARCHAR(3)),
    Column('remarks', VARCHAR(255)),
    Column('record_stat', VARCHAR(1)),
    Column('auth_stat', VARCHAR(1)),
    Column('mod_no', NUMBER(4, 0, False)),
    Column('maker_id', VARCHAR(50)),
    Column('maker_dt_stamp', DateTime),
    Column('checker_id', VARCHAR(50)),
    Column('checker_dt_stamp', DateTime),
    Column('once_auth', VARCHAR(1)),
    Column('source', VARCHAR(35)),
    Column('user_refno', VARCHAR(50)),
    Column('udf_value_1', VARCHAR(4000)),
    Column('udf_value_2', VARCHAR(4000)),
    Column('udf_value_3', VARCHAR(4000)),
    Column('udf_value_4', VARCHAR(4000)),
    Column('udf_value_5', VARCHAR(4000)),
    Column('udf_value_6', VARCHAR(4000)),
    Column('udf_value_7', VARCHAR(4000)),
    Column('udf_value_8', VARCHAR(4000)),
    Column('udf_value_9', VARCHAR(4000)),
    Column('udf_value_10', VARCHAR(4000)),
    Column('udf_value_11', VARCHAR(4000)),
    Column('udf_value_12', VARCHAR(4000)),
    Column('udf_value_13', VARCHAR(4000)),
    Column('udf_value_14', VARCHAR(4000)),
    Column('udf_value_15', VARCHAR(4000)),
    Column('udf_value_16', VARCHAR(4000)),
    Column('udf_value_17', VARCHAR(4000)),
    Column('udf_value_18', VARCHAR(4000)),
    Column('udf_value_19', VARCHAR(4000)),
    Column('udf_value_20', VARCHAR(4000)),
    Column('udf_value_21', VARCHAR(4000)),
    Column('udf_value_22', VARCHAR(4000)),
    Column('udf_value_23', VARCHAR(4000)),
    Column('udf_value_24', VARCHAR(4000)),
    Column('udf_value_25', VARCHAR(4000)),
    Column('udf_value_26', VARCHAR(4000)),
    Column('udf_value_27', VARCHAR(4000)),
    Column('udf_value_28', VARCHAR(4000)),
    Column('udf_value_29', VARCHAR(4000)),
    Column('udf_value_30', VARCHAR(4000)),
    Column('udf_value_31', VARCHAR(4000)),
    Column('udf_value_32', VARCHAR(4000)),
    Column('udf_value_33', VARCHAR(4000)),
    Column('udf_value_34', VARCHAR(4000)),
    Column('udf_value_35', VARCHAR(4000)),
    Column('udf_value_36', VARCHAR(4000)),
    Column('udf_value_37', VARCHAR(4000)),
    Column('udf_value_38', VARCHAR(4000)),
    Column('udf_value_39', VARCHAR(4000)),
    Column('udf_value_40', VARCHAR(4000)),
    Column('udf_value_41', VARCHAR(4000)),
    Column('udf_value_42', VARCHAR(4000)),
    Column('udf_value_43', VARCHAR(4000)),
    Column('udf_value_44', VARCHAR(4000)),
    Column('udf_value_45', VARCHAR(4000)),
    Column('udf_value_46', VARCHAR(4000)),
    Column('udf_value_47', VARCHAR(4000)),
    Column('udf_value_48', VARCHAR(4000)),
    Column('udf_value_49', VARCHAR(4000)),
    Column('udf_value_50', VARCHAR(4000))
)

t_ud_los_ma_bank_code = Table(
    'ud_los_ma_bank_code', metadata,
    Column('bank_code', VARCHAR(10), nullable=False, index=True),
    Column('bank_name', VARCHAR(100), nullable=False),
    Column('bank_status', VARCHAR(1), nullable=False),
    Column('bank_desc', VARCHAR(200)),
    Column('bank_out', VARCHAR(1)),
    Column('bank_quick', VARCHAR(1))
)
