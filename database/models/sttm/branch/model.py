from sqlalchemy import VARCHAR, Column

from database import Base


class Branch(Base):
    __tablename__ = 'los_sttm_branch'
    __table_args__ = {'comment': 'Danh sách các chi nhánh SCB'}

    branch_code = Column(VARCHAR(3), primary_key=True)
    branch_name = Column(VARCHAR(105))
    branch_addr1 = Column(VARCHAR(105))
    branch_addr2 = Column(VARCHAR(105))
    branch_addr3 = Column(VARCHAR(105))
    parent_branch = Column(VARCHAR(3))
    regional_office = Column(VARCHAR(3))
    walkin_customer = Column(VARCHAR(9))
    branch_unit_type = Column(VARCHAR(100), comment='Loại đơn vị chi nhánh')
    actived_flag = Column(VARCHAR(1))
