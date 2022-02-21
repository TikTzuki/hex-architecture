from sqlalchemy import VARCHAR, Column, Integer

from app.third_party.oracle.models.utils import Base


class MaCostType(Base):
    __tablename__ = 'los_ma_cost_type'
    __table_args__ = {'comment': 'Loại chi phí'}

    id = Column("ID", VARCHAR(30), primary_key=True)

    name = Column("NAME", VARCHAR(100))

    is_loan_required = Column("IS_LOAN_REQUIRED", VARCHAR(1), default='N',
                              comment='Nếu dùng cho vay thường thì đánh dấu Y')

    is_credit_required = Column("IS_CREDIT_REQUIRED", VARCHAR(1), default='N',
                                comment='Nếu dùng cho vay thẻ thì đánh dấu Y')

    display_order = Column("DISPLAY_ORDER", Integer, comment='Thứ tự hiển thị (mặc định dùng cho vay thẻ)')
