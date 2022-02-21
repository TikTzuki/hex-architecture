from sqlalchemy import VARCHAR, Column, Integer

from database.models.utils import BaseModel


class ProfileDocument(BaseModel):
    __tablename__ = 'los_profile_document'
    __table_args__ = {'comment': 'Danh mục tài liệu, hồ sơ trong một hồ sơ vay vốn'}

    id = Column("ID", Integer, primary_key=True)

    profile_id = Column('LOS_PROFILE_ID', VARCHAR(20), comment='Hồ sơ vay vốn')

    person_id = Column('LOS_PERSON_ID', VARCHAR(20), comment='Hồ sơ thuộc về người nào theo ID')

    file_extension = Column('FILE_EXTENSION', VARCHAR(200), comment='Định dạng file')

    file_url = Column('FILE_URL', VARCHAR(300), comment='URL liên kết với DMS')

    display_order = Column('DISPLAY_ORDER', Integer, comment='Thứ tự hiển thị (mặc định = 1)')

    actived_flag = Column('ACTIVED_FLAG', VARCHAR(1))

    document_type_id = Column('DOCUMENT_TYPE_ID', VARCHAR(75),
                              comment='Nhóm tài liệu theo loại loại hồ sơ, CMND, CIC, Tài sản bảo đảm, Nguồn thu nhập')

    relationship_type = Column('RELATIONSHIP_TYPE', VARCHAR(75),
                               comment='Quan hệ với người vay, chinh chủ, hôn phối, đồng vay đồng trả nợ (hỗ trợ truy vấn nhanh)')

    sequence = Column('SEQUENCE', Integer, comment='Số tăng tự động để làm thông tin version (mặc định bằng = 1)')

    owner_input_type = Column('OWNER_INPUT_TYPE', VARCHAR(10),
                              comment='Phân biệt hồ sơ này là do bên nào cung cấp, khách hàng hay SCB')

    note = Column('NOTE', VARCHAR(500), comment='Ghi chú về thông tin hồ sơ này')

    ext_1 = Column('EXT_1', VARCHAR(100))
