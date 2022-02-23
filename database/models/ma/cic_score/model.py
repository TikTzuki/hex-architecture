from sqlalchemy import VARCHAR, Column, Date, Integer

from database import Base


class MaCicScore(Base):
    __tablename__ = 'los_ma_cic_score'
    __table_args__ = {
        'comment': 'Bảng ghi lại thông tin về điểm và hạng của CIC cho khách hàng vay tín dụng, có thể thay đổi theo thời gian'}

    id = Column("ID", Integer, primary_key=True)

    version = Column("VERSION", VARCHAR(50), comment='Theo công văn số, quyết định số nào của CIC')

    start_time = Column("START_TIME", Date, comment='Thời gian bắt đầu')

    end_time = Column("END_TIME", Date,
                      comment='Thời gian kết thúc, nếu bỏ trống thì active_flag = Y, đánh dấu đang sử dụng')

    description = Column("DESCRIPTION", VARCHAR(100))

    actived_flag = Column("ACTIVED_FLAG", VARCHAR(1), comment='Cờ đánh dấu đang kích hoạt, hay là cái mới nhất')


class MaCicScoreDetail(Base):
    __tablename__ = 'los_ma_cic_score_detail'
    __table_args__ = {'comment': 'Bảng chi tiết và điểm hạng của CIC'}

    id = Column("ID", Integer, primary_key=True)

    cic_score_rank = Column("CIC_SCORE_RANK", VARCHAR(20), comment='Tham chiếu qua bảng UDTM')

    min_score = Column("MIN_SCORE", Integer, comment='Điểm cận dưới')

    max_score = Column("MAX_SCORE", Integer, comment='Điểm cận trên')

    cic_score_rank_score = Column("CIC_SCORE_RANK_SCORE", VARCHAR(10),
                                  comment='Tham chiếu bảng UDTM, điểm hạng 10,9,8.... Mỗi range sẽ có khung điểm')

    cic_score_id = Column("CIC_SCORE_ID", Integer, comment='Tham chiếu qua bảng MA_CIC_SCORE')
