from sqlalchemy import VARCHAR, Column, Float, Integer

from database.base import BaseModel


class ProfileCustGroupItem(BaseModel):
    __tablename__ = 'los_profile_cust_group_item'
    __table_args__ = {'comment': 'Lưu lại thông tin mở thẻ theo đối tượng'}

    id = Column("ID", Integer, primary_key=True)

    cust_group_id = Column('CUST_GROUP_ID', Integer, comment='Tham chiếu qua bảng MA_CUST_GROUP_ID')

    cust_group_item_value = Column("CUST_GROUP_ITEM_VALUE", VARCHAR(100), comment='Giá trị của từng item đối tượng')

    profile_credit_sequence_id = Column("PROFILE_CREDIT_SEQUENCE_ID", Integer,
                                        comment='Tham chiếu qua bảng LOS_PROFILE_CREDIT_SEQUENCE')

    cust_group_item_id = Column("CUST_GROUP_ITEM_ID", Float, comment='Tham chiếu qua bảng MA_CUST_GROUP_ITEM_ID')
