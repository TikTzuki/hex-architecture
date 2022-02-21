from sqlalchemy import VARCHAR, Column, Integer

from database.models.utils import BaseModel


class MaQuestion(BaseModel):
    __tablename__ = 'los_ma_question'
    __table_args__ = {'comment': 'Danh sách các câu hỏi xác thực'}

    id = Column('ID', Integer, primary_key=True)

    name = Column('NAME', VARCHAR(100))

    question_type = Column('QUESTION_TYPE', VARCHAR(10),
                           comment='Loại câu hỏi, dùng để gom nhóm, tham chiếu qua bên UDTM')

    actived_flag = Column('ACTIVED_FLAG', VARCHAR(1))

    display_order = Column('DISPLAY_ORDER', Integer)
