from sqlalchemy import CHAR, VARCHAR, Column, Integer

from database import Base


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

    credit_group_cust_id = Column("CREDIT_GROUP_CUST_ID", Integer,
                                  comment='Mã đối tượng tham chiếu qua bảng LOS_MA_CREDIT_GROUP_CUST')

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

    display_order_calculation = Column("DISPLAY_ORDER_CALCULATION", Integer,
                                       comment='Thứ tự hiển thị để tính toán theo công thức')

    calculation_type = Column("CALCULATION_TYPE", VARCHAR(30), comment='Loại công thức tính dữ liệu')

    droplist_item_condition = Column('DROPLIST_ITEM_CONDITION', VARCHAR(100),
                                     comment='Điều kiện loại bỏ dữ liệu cho select')

    info_type = Column('INFO_TYPE', VARCHAR(30), comment='Phân biệt thông tin chi tiết và thông tin tiêu chí')

    calculation_flag = Column("CALCULATION_FLAG", CHAR(1),
                              comment='Khi thay đổi sẽ call api để tính toán cho các item khác.')

    field_type = Column("FIELD_TYPE", VARCHAR(50),
                        comment='Phân biệt field item: Hạn mức tối đa theo đối tượng, Hạn mức tổng đơn vị đề, ...')

    value_flag = Column("VALUE_FLAG", VARCHAR(1), comment='Lấy dữ liệu FE gửi lên (field value hoặc field code)')
