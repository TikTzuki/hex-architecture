from sqlalchemy import VARCHAR, Column, Integer

from database.base import BaseModel


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

    credit_card_type = Column('CREDIT_CARD_TYPE', VARCHAR(20),
                              comment='Dành cho vay thẻ (Thông tin pháp lý). Để phân biệt tài liệu chủ thẻ chính và người hôn phối')
