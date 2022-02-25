from sqlalchemy import VARCHAR, Column, ForeignKey, Integer
from sqlalchemy.orm import relationship

from database.base import BaseModel


class FinanceTimeline(BaseModel):
    __tablename__ = 'los_finance_timeline'
    __table_args__ = {'comment': 'Dữ liệu thời gian T-2, T-1, T, T+1, T+2'}

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(100))
    description = Column(VARCHAR(200))
    display_order = Column(Integer)


class FinanceTimelineAssign(BaseModel):
    __tablename__ = 'los_finance_timeline_assign'
    __table_args__ = {'comment': 'Phân định thời gian theo thời gian T, \\nCó 2 dạng :\\n+ Khách hàng đưa dữ liệu, (mặc định)\\n+ NV SCB Tự tính dữ liệu,'}

    id = Column(Integer, primary_key=True)
    time_line_id = Column(ForeignKey('los_finance_timeline.id'), comment='Mã thời gian T-2, T-1, T....')
    owner_input_type = Column(VARCHAR(20), comment='Quy định Timeline đó sẽ có ai nhập dữ liệu (SCB, Khách hàng) (tham chiếu trong bảng udtm )')
    display_order = Column(Integer)

    required_flag = Column(VARCHAR(1), comment='Yêu cầu dữ liệu truyền lên')

    time_line = relationship('FinanceTimeline')
