from sqlalchemy import CHAR, VARCHAR, Column

from database.models.utils import BaseModel


class MaBusinessLine(BaseModel):
    __tablename__ = 'los_ma_business_line'
    __table_args__ = {'comment': 'Bảng liên quan tới các nhóm ngành kinh doanh chính, sử dụng cho hộ kinh doanh. '}

    id = Column("ID", CHAR(10), primary_key=True)

    business_name = Column("BUSINESS_NAME", VARCHAR(255))

    business_code = Column("BUSINESS_CODE", VARCHAR(10))
