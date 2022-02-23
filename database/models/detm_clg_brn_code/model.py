from sqlalchemy import VARCHAR, Column

from database import Base


class DetmClgBrnCode(Base):
    __tablename__ = 'ud_los_detm_clg_brn_code'

    branch_code = Column("BRANCH_CODE", VARCHAR(9), primary_key=True)

    branch_desc = Column("BRANCH_DESC", VARCHAR(35))

    sector_code = Column("SECTOR_CODE", VARCHAR(9))
