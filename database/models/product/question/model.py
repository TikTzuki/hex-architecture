from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class ProductQuestion(BaseModel):
    __tablename__ = 'los_product_question'
    __table_args__ = {'comment': 'Danh sách tương ứng mỗi sản phẩm vay sẽ có những câu hỏi nào'}

    id = Column("ID", Integer, primary_key=True)

    loan_product_id = Column('loan_product_id', VARCHAR(20), comment='Mã sản phẩm')

    question_id = Column('question_id', Integer, comment='Mã câu hỏi')

    display_order = Column('display_order', Integer, comment='Thứ tự câu hỏi hiển thị')

    required_flag = Column('required_flag', VARCHAR(1), comment='Yêu cầu phải nhập dữ liệu')
