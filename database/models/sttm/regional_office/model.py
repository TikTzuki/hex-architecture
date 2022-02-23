from sqlalchemy import VARCHAR, Column

from database import Base


class RegionalOffice(Base):
    __tablename__ = 'los_sttm_regional_office'
    __table_args__ = {'comment': 'Danh sách khu vực của địa chỉ ngân hàng SCB'}

    regional_code = Column("REGIONAL_CODE", VARCHAR(10), primary_key=True, comment='Mã vùng')

    regional_name = Column("REGIONAL_NAME", VARCHAR(100), comment='Tên vùng')
