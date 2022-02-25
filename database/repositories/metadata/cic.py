from sqlalchemy import VARCHAR, Column, Integer, text

from database.base import BaseModel


class CreditInstitution(BaseModel):
    __tablename__ = 'los_credit_institution'
    __table_args__ = {'comment': 'Danh sách các tổ chức tín dụng'}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100))
    code = Column(VARCHAR(9))
    institution_group = Column(VARCHAR(20), comment='Nhóm TCTD như ngân hàng, tổ chức tài chính')
    avatar = Column(VARCHAR(100))

    short_name = Column(VARCHAR(50), comment='Tên viết tắt của một số ngân hàng ví dụ ACB, Agribank, MB')
    other_value_flag = Column(VARCHAR(1), server_default=text("'N'"))
