from sqlalchemy import VARCHAR, Column, Float, Integer

from database.base import BaseModel


class ProfileCost(BaseModel):
    __tablename__ = 'los_profile_cost'
    __table_args__ = {'comment': 'Danh sách các chi phí và giá tiền phải nhập'}

    id = Column("ID", Integer, primary_key=True)

    sequence_id = Column('LOS_SEQUENCE_ID', Integer)

    cost_type = Column("COST_TYPE", VARCHAR(75),
                       comment='Loại chi phí:\\n- Sinh hoạt gia đình\\n- Chi phí trả cho các khoản vay khác (cả gốc + lãi)\\n- Chi phí khác')

    value = Column("VALUE", Float, comment='Giá trị tiền phai chịu cho chi phí đó')
