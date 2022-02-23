from sqlalchemy import VARCHAR, Column, Integer

from database.base import BaseModel


class ProfileCreditStatementMethod(BaseModel):
    __tablename__ = 'los_profile_credit_statement_method'
    __table_args__ = {'comment': 'Mô tả dùng để lưu thông tin hình thức nhận bảng sao kê thẻ và các thông báo khác'}

    id = Column("ID", Integer, primary_key=True)

    credit_published_id = Column('CREDIT_PUBLISHED_ID', Integer, comment='Tham chiếu tới thẻ chính')

    credit_limit = Column("STATEMENT_METHOD_TYPE_ID", VARCHAR(50), comment='Hình thức giao thẻ tham chiếu qua UDTM')

    address = Column("ADDRESS", VARCHAR(200), comment='Địa chỉ nhận thông tin')

    province_id = Column("PROVINCE_ID", VARCHAR(20), comment='Tỉnh / Thành phố')

    district_id = Column("DISTRICT_ID", VARCHAR(20), comment='Quận / Huyện')

    ward_id = Column("WARD_ID", VARCHAR(20), comment='Phường / Xã')
