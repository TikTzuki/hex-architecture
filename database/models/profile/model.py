from sqlalchemy import CHAR, VARCHAR, Column, Integer

from database.base import BaseModel


class Profile(BaseModel):
    __tablename__ = 'los_profile'
    __table_args__ = {'comment': 'Hồ sơ LOS'}

    id = Column("ID", VARCHAR(20), primary_key=True)

    person_id = Column("PERSON_ID", Integer, comment='Người vay vốn chính')

    term = Column("TERM", VARCHAR(20), comment='Loại hình cho vay')

    fcc_purpose = Column("FCC_PURPOSE", CHAR(3), comment='Mục đích vay vốn (dữ liệu theo Core)')

    customer_purpose = Column("CUSTOMER_PURPOSE", CHAR(200), comment='Mục đích vay theo thực tế')

    loan_product_id = Column("LOAN_PRODUCT_ID", VARCHAR(20), comment='Mã sản phẩm vay')

    partner_id = Column("PARTNER_ID", VARCHAR(20), comment='Mã đối tác theo sản phẩm')

    partner_product_id = Column("PARTNER_PRODUCT_ID", Integer, comment='Sản phẩm theo đối tác')

    is_collateral = Column("IS_COLLATERAL", VARCHAR(1), comment='Thông tin về tài sản bảo đảm, có hay không')

    is_exception = Column("IS_EXCEPTION", VARCHAR(2), comment='Thông tin về ngoại lệ, có hay không')

    publication_speed_type = Column("PUBLICATION_SPEED_TYPE", VARCHAR(30),
                                    comment='Dùng cho vay thẻ, loại phát hành, thường hay nhanh, tham chiếu qua UDTM')

    request_created_credit_flag = Column("REQUEST_CREATED_CREDIT_FLAG", VARCHAR(1),
                                         comment='Dùng cho vay thẻ, đánh dấu KH có nhu cầu tạo thẻ mới')

    request_modified_credit_flag = Column("REQUEST_MODIFIED_CREDIT_FLAG", VARCHAR(1),
                                          comment='Dùng cho vay thẻ, đánh dấu KH có nhu cầu thay đổi hạn mức / hình thức bảo đảm thẻ')

    loan_category_id = Column("LOAN_CATEGORY_ID", VARCHAR(10),
                              comment='Đánh dấu vay thường hay vay thẻ (dùng truy xuất, tìm kiếm nhanh)')

    loan_purpose = Column("LOAN_PURPOSE", VARCHAR(20), comment='Mục đích vay theo SP')

    num_license_request = Column("NUM_LICENSE_REQUEST", VARCHAR(20), comment='Số giấy đề nghị')
