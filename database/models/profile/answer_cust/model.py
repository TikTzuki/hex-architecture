from sqlalchemy import VARCHAR, Column, Integer

from database.base import BaseModel


class ProfileAnswerCus(BaseModel):
    __tablename__ = 'los_profile_answer_cust'
    __table_args__ = {'comment': 'Danh sách câu trả lời cho hồ sơ vay vốn của khách hàng'}

    id = Column("ID", Integer, primary_key=True)

    profile_id = Column('LOS_PROFILE_ID', VARCHAR(20), comment='Mã hồ sơ vay vốn')

    profile_question_id = Column('PROFILE_QUESTION_ID', Integer, comment='Mã câu hỏi theo hồ sơ')

    answer = Column('ANSWER', VARCHAR(100), comment='Câu trả lời của khách hàng')

    person_id = Column('PERSON_ID', Integer, comment='Người trả lời câu hỏi (Chủ thẻ chính, chủ thẻ phụ, ...)')

    actived_flag = Column('ACTIVED_FLAG', VARCHAR(1), comment='Trạng thái chấp nhận câu trả lời')
