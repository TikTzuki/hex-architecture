from sqlalchemy import VARCHAR, Column, Date, Float, Integer

from database.base import BaseModel


class PersonCreditScore(BaseModel):
    __tablename__ = 'los_person_credit_score'
    __table_args__ = {'comment': 'Thông tin điểm tín dụng CIC của một khách hàng - theo giấy tờ tùy thân'}

    id = Column("ID", Integer, primary_key=True)

    personal_identity_id = Column("PERSONAL_IDENTITY_ID", Integer)

    los_id = Column("LOS_ID", VARCHAR(100), comment='Mã hồ sơ vay vốn')

    score_value = Column("SCORE_VALUE", Integer, comment='Điểm tín dụng')

    score_rank = Column("SCORE_RANK", VARCHAR(10), comment='Hạng')

    publish_date = Column("PUBLISH_DATE", Date, comment='Ngày chấm điểm')

    evaluation = Column("EVALUATION", Float, comment='Cờ đánh dấu đang kích hoạt, hay là cái mới nhất')


class PersonCreditScoreSegment(BaseModel):
    __tablename__ = 'los_person_credit_score_segment'
    __table_args__ = {'comment': 'Bảng phân loại khách hàng theo CIC đánh giá'}

    id = Column("ID", Integer, primary_key=True)

    credit_score_id = Column("CREDIT_SCORE_ID", Integer, comment='Tham chiếu qua bảng LOS_PERSON_CREDIT_SCORE')

    cic_cus_segment = Column("CIC_CUS_SEGMENT", VARCHAR(10), comment='Tham chiếu qua bảng UDTM')
