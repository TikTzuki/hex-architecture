from sqlalchemy import CHAR, CheckConstraint, Column, DateTime, Float, ForeignKey, Integer, Table, Text, VARCHAR, text
from sqlalchemy.dialects.oracle import NUMBER
from sqlalchemy.orm import relationship

from database.base import BaseModel


class MaQuestion(BaseModel):
    __tablename__ = 'los_ma_question'
    __table_args__ = {'comment': 'Danh sách các câu hỏi xác thực'}

    id = Column('ID', Integer, primary_key=True)

    name = Column('NAME', VARCHAR(100))

    question_type = Column('QUESTION_TYPE', VARCHAR(10),
                           comment='Loại câu hỏi, dùng để gom nhóm, tham chiếu qua bên UDTM')

    actived_flag = Column('ACTIVED_FLAG', VARCHAR(1))

    display_order = Column('DISPLAY_ORDER', Integer)
