from sqlalchemy import VARCHAR, Column, Integer

from database.base import BaseModel


class FinanceTimeline(BaseModel):
    __tablename__ = 'los_finance_timeline'
    __table_args__ = {'comment': 'Dữ liệu thời gian T-2, T-1, T, T+1, T+2'}

    id = Column("ID", Integer, primary_key=True)

    name = Column("NAME", VARCHAR(100))

    description = Column("DESCRIPTION", VARCHAR(200))

    display_order = Column("DISPLAY_ORDER", Integer)


class FinanceTimelineAssign(BaseModel):
    __tablename__ = 'los_finance_timeline_assign'
    __table_args__ = {
        'comment': 'Phân định thời gian theo thời gian T, \\nCó 2 dạng :\\n+ Khách hàng đưa dữ liệu, (mặc định)\\n+ NV SCB Tự tính dữ liệu,'}

    id = Column("ID", Integer, primary_key=True)

    time_line_id = Column('TIME_LINE_ID', Integer)

    owner_input_type = Column("OWNER_INPUT_TYPE", VARCHAR(20),
                              comment='Quy định Timeline đó sẽ có ai nhập dữ liệu (SCB, Khách hàng) (tham chiếu trong bảng udtm )')

    display_order = Column("DISPLAY_ORDER", Integer)

    required_flag = Column('REQUIRED_FLAG', VARCHAR(1), comment='Yêu cầu truyền dữ liệu')
